"""
Tests for signal_pipeline/fast_features.py
Author: Joy Bose (2026) | License: MIT
"""

import numpy as np
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'signal_pipeline'))

from fast_features import (
    frontal_alpha_asymmetry,
    phase_locking_value,
    theta_beta_ratio,
    hjorth_mobility,
    hjorth_complexity,
    extract_layer1_features,
)

FS = 250
N = 125  # 500ms window


def make_signal(freq=10.0, amplitude=1.0, noise=0.1):
    t = np.arange(N) / FS
    return amplitude * np.sin(2 * np.pi * freq * t) + noise * np.random.randn(N)


def test_alpha_asymmetry_returns_float():
    fp1 = make_signal(10)
    fp2 = make_signal(10)
    result = frontal_alpha_asymmetry(fp1, fp2, FS)
    assert isinstance(result, float), "Alpha asymmetry must return a float"


def test_alpha_asymmetry_symmetric_signals_near_zero():
    sig = make_signal(10, noise=0.0)
    result = frontal_alpha_asymmetry(sig.copy(), sig.copy(), FS)
    assert abs(result) < 0.01, "Identical signals should give near-zero asymmetry"


def test_plv_bounds():
    ch1 = make_signal(6)
    ch2 = make_signal(6)
    plv = phase_locking_value(ch1, ch2, FS, 4, 8)
    assert 0.0 <= plv <= 1.0, f"PLV must be in [0,1], got {plv}"


def test_theta_beta_ratio_positive():
    sig = make_signal(6)
    ratio = theta_beta_ratio(sig, FS)
    assert ratio >= 0.0, "Theta/beta ratio must be non-negative"


def test_hjorth_mobility_positive():
    sig = make_signal(10)
    mob = hjorth_mobility(sig)
    assert mob >= 0.0


def test_extract_layer1_features_returns_dict():
    eeg = np.stack([make_signal(f) for f in [10, 10, 6, 6]])
    features = extract_layer1_features(eeg, FS)
    assert isinstance(features, dict)
    assert len(features) > 0


def test_extract_layer1_features_all_finite():
    eeg = np.stack([make_signal(f) for f in [10, 10, 6, 6]])
    features = extract_layer1_features(eeg, FS)
    for k, v in features.items():
        assert np.isfinite(v), f"Feature {k} is not finite: {v}"


if __name__ == '__main__':
    test_alpha_asymmetry_returns_float()
    test_alpha_asymmetry_symmetric_signals_near_zero()
    test_plv_bounds()
    test_theta_beta_ratio_positive()
    test_hjorth_mobility_positive()
    test_extract_layer1_features_returns_dict()
    test_extract_layer1_features_all_finite()
    print("All tests passed.")
