"""
Sati-Loop: Slow Somatic Context Extraction (Layers 2-3 only)

Computes slow-timescale physiological context over 10-30 second windows.
These features must NEVER be used in the Layer 1 mind-wandering classifier.
They are used for gross agitation/dullness estimation in Layers 2 and 3 only.

Author: Joy Bose (2026)
License: MIT
"""

import numpy as np
from collections import deque


def compute_rmssd(ibi_sequence):
    """Root-mean-square of successive IBI differences. Indexes vagal tone."""
    if len(ibi_sequence) < 2:
        return 0.0
    diffs = np.diff(ibi_sequence)
    return float(np.sqrt(np.mean(diffs ** 2)))


def compute_lf_hf_ratio(ibi_sequence, fs_ibi=4.0):
    """LF/HF ratio from interpolated IBI sequence. Sympathovagal balance."""
    if len(ibi_sequence) < 10:
        return 1.0
    from scipy.signal import welch
    f, psd = welch(ibi_sequence, fs_ibi, nperseg=min(len(ibi_sequence), 64))
    lf = float(np.trapz(psd[(f >= 0.04) & (f < 0.15)], f[(f >= 0.04) & (f < 0.15)]))
    hf = float(np.trapz(psd[(f >= 0.15) & (f < 0.40)], f[(f >= 0.15) & (f < 0.40)]))
    return lf / max(hf, 1e-10)


def respiration_stats(resp_signal):
    """
    Rate (breaths/min) and irregularity from raw respiration signal.
    Uses zero-crossings of the detrended signal.
    """
    detrended = resp_signal - np.mean(resp_signal)
    crossings = np.where(np.diff(np.sign(detrended)))[0]
    if len(crossings) < 2:
        return {'rate_bpm': 0.0, 'irregularity': 0.0, 'amplitude': 0.0}
    half_cycles = len(crossings) - 1
    duration_s = len(resp_signal) / 50.0  # assumed 50 Hz
    rate = (half_cycles / 2.0) / duration_s * 60.0
    cycle_lengths = np.diff(crossings) * 2  # full cycle estimates
    irregularity = float(np.std(cycle_lengths) / max(np.mean(cycle_lengths), 1e-10))
    return {
        'rate_bpm':     float(rate),
        'irregularity': irregularity,
        'amplitude':    float(np.std(resp_signal)),
    }


def posture_stats(imu_pitch_data):
    """Mean and drift of head pitch angle. Detects postural collapse (dullness)."""
    return {
        'mean_pitch':   float(np.mean(imu_pitch_data)),
        'pitch_drift':  float(np.std(imu_pitch_data)),
        'max_droop':    float(np.max(imu_pitch_data) - np.min(imu_pitch_data)),
    }


def extract_somatic_context(ppg_ibi, resp_signal, imu_pitch):
    """
    Slow context feature vector for Layers 2-3 state estimation.
    Must not be passed to the Layer 1 classifier.

    Parameters
    ----------
    ppg_ibi : array-like
        Inter-beat intervals from PPG (seconds).
    resp_signal : array-like
        Raw respiration sensor values at 50 Hz.
    imu_pitch : array-like
        Head pitch angle (degrees) at 100 Hz.

    Returns
    -------
    dict of feature name -> float value
    """
    features = {}
    features['rmssd'] = compute_rmssd(ppg_ibi)
    features['lf_hf_ratio'] = compute_lf_hf_ratio(ppg_ibi)
    features.update(respiration_stats(resp_signal))
    features.update(posture_stats(imu_pitch))
    return features
