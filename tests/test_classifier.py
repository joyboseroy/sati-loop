"""
Tests for signal_pipeline/classifier.py
Author: Joy Bose (2026) | License: MIT
"""

import numpy as np
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'signal_pipeline'))

from classifier import SatiClassifier


def make_training_data(n=60):
    np.random.seed(42)
    X = np.random.randn(n, 10)
    y = np.array([0]*20 + [1]*20 + [2]*20)
    return X, y


def test_uncalibrated_returns_uniform():
    clf = SatiClassifier()
    vec = np.random.randn(10)
    probs = clf.predict_proba(vec)
    assert len(probs) == 3
    assert abs(sum(probs) - 1.0) < 0.01


def test_train_and_predict():
    clf = SatiClassifier()
    X, y = make_training_data()
    clf.train(X, y)
    assert clf.is_calibrated
    probs = clf.predict_proba(X[0])
    assert len(probs) == 3
    assert abs(sum(probs) - 1.0) < 0.01
    assert all(p >= 0 for p in probs)


def test_probabilities_bounded():
    clf = SatiClassifier()
    X, y = make_training_data()
    clf.train(X, y)
    for i in range(10):
        probs = clf.predict_proba(np.random.randn(10))
        assert all(0.0 <= p <= 1.0 for p in probs), f"Probability out of bounds: {probs}"


def test_single_class_raises():
    clf = SatiClassifier()
    X = np.random.randn(20, 10)
    y = np.zeros(20, dtype=int)
    try:
        clf.train(X, y)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass


if __name__ == '__main__':
    test_uncalibrated_returns_uniform()
    test_train_and_predict()
    test_probabilities_bounded()
    test_single_class_raises()
    print("All tests passed.")
