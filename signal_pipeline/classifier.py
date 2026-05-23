"""
Sati-Loop: Personalised Mind-Wandering Classifier (Layer 1)

Uses EEG-only features from fast_features.py.
Do not pass somatic context features (HRV, respiration, IMU) to this classifier.

Class labels:
    0 = attentive
    1 = wandering
    2 = laxity

Author: Joy Bose (2026)
License: MIT
"""

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import label_binarize
import joblib


LABEL_MAP = {0: 'attentive', 1: 'wandering', 2: 'laxity'}
LABEL_RMAP = {v: k for k, v in LABEL_MAP.items()}


class SatiClassifier:
    """
    Personalised binary-plus classifier for mind-wandering detection.
    Trained on individual Phase A calibration data only.
    """

    def __init__(self):
        self.model = RandomForestClassifier(
            n_estimators=100,
            max_depth=6,
            min_samples_leaf=3,
            class_weight='balanced',
            random_state=42,
        )
        self.feature_names = None
        self.is_calibrated = False

    def train(self, X, y):
        """
        Train on Phase A calibration data.

        Parameters
        ----------
        X : np.ndarray, shape (n_samples, n_features)
            Feature matrix from fast_features.extract_layer1_features().
        y : array-like
            Labels: 0=attentive, 1=wandering, 2=laxity
        """
        if len(np.unique(y)) < 2:
            raise ValueError("Training requires at least two distinct classes.")
        self.model.fit(X, y)
        self.is_calibrated = True

    def predict_proba(self, feature_vector):
        """
        Return probability vector [P(attentive), P(wandering), P(laxity)].

        Parameters
        ----------
        feature_vector : np.ndarray, shape (n_features,)
            Output of fast_features.extract_layer1_features() as array.
        """
        if not self.is_calibrated:
            return np.array([0.33, 0.33, 0.34])
        probs = self.model.predict_proba(feature_vector.reshape(1, -1))[0]
        # Align with [0, 1, 2] even if some classes absent from training
        full = np.zeros(3)
        for i, cls in enumerate(self.model.classes_):
            full[cls] = probs[i]
        return full

    def save(self, path):
        joblib.dump(self, path)

    @classmethod
    def load(cls, path):
        return joblib.load(path)
