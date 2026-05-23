"""
Tests for signal_pipeline/artifact_rejection.py
Author: Joy Bose (2026) | License: MIT
"""

import numpy as np
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'signal_pipeline'))

from artifact_rejection import (
    amplitude_reject,
    blink_detect,
    jaw_clench_detect,
    tdm_overlap_reject,
    preprocess_window,
)

FS = 250
N = 125


def clean_eeg():
    return np.random.randn(4, N) * 10  # Normal amplitude ~10 uV


def test_amplitude_reject_clean():
    eeg = clean_eeg()
    assert not amplitude_reject(eeg), "Clean signal should not be rejected"


def test_amplitude_reject_dirty():
    eeg = clean_eeg()
    eeg[0, 50] = 200.0  # Spike above 100 uV threshold
    assert amplitude_reject(eeg), "Spike should trigger rejection"


def test_blink_detect_no_blink():
    fp1 = np.random.randn(N) * 10
    fp2 = np.random.randn(N) * 10
    assert not blink_detect(fp1, fp2), "Random signal should not be detected as blink"


def test_blink_detect_with_blink():
    blink = np.zeros(N)
    blink[30:50] = 100.0  # Large correlated spike
    assert blink_detect(blink, blink.copy()), "Correlated large spike should be detected"


def test_jaw_clench_detect_clean():
    eeg = clean_eeg()
    assert not jaw_clench_detect(eeg), "Clean signal should not be detected as clench"


def test_tdm_overlap_reject():
    stim_periods = [(10.0, 10.4)]  # stimulation active 10.0 to 10.4s
    assert tdm_overlap_reject(10.2, stim_periods), "Overlapping window should be rejected"
    assert not tdm_overlap_reject(11.0, stim_periods), "Non-overlapping window should pass"


def test_preprocess_clean_returns_array():
    eeg = clean_eeg()
    clean, reason = preprocess_window(eeg, FS)
    assert clean is not None, f"Clean window rejected with reason: {reason}"
    assert reason == 'ok'


def test_preprocess_spike_rejected():
    eeg = clean_eeg()
    eeg[0, 50] = 200.0
    clean, reason = preprocess_window(eeg, FS)
    assert clean is None
    assert reason == 'amplitude_threshold'


if __name__ == '__main__':
    test_amplitude_reject_clean()
    test_amplitude_reject_dirty()
    test_blink_detect_no_blink()
    test_blink_detect_with_blink()
    test_jaw_clench_detect_clean()
    test_tdm_overlap_reject()
    test_preprocess_clean_returns_array()
    test_preprocess_spike_rejected()
    print("All tests passed.")
