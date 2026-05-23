"""
Sati-Loop: Fast Neural Feature Extraction (Layer 1 only)

Computes high-temporal-resolution EEG features on 500ms windows.
These are the ONLY features permitted in the Layer 1 mind-wandering classifier.

PPG, HRV, respiration, and IMU metrics are excluded here.
See slow_context.py for slow-timescale somatic features (Layers 2-3 only).

Author: Joy Bose (2026)
License: MIT
"""

import numpy as np
from scipy.signal import butter, lfilter, welch


def bandpass_filter(data, lowcut, highcut, fs, order=4):
    nyq = 0.5 * fs
    b, a = butter(order, [lowcut / nyq, highcut / nyq], btype='band')
    return lfilter(b, a, data)


def compute_band_power(data, fs, fmin, fmax):
    f, psd = welch(data, fs, nperseg=min(len(data), 128))
    idx = np.where((f >= fmin) & (f <= fmax))[0]
    return float(np.trapz(psd[idx], f[idx]))


def frontal_alpha_asymmetry(fp1, fp2, fs=250):
    """log(alpha_Fp2) - log(alpha_Fp1). Maps early task-negative orienting."""
    p1 = compute_band_power(fp1, fs, 8, 12)
    p2 = compute_band_power(fp2, fs, 8, 12)
    return np.log(max(p2, 1e-10)) - np.log(max(p1, 1e-10))


def phase_locking_value(ch1, ch2, fs, fmin, fmax):
    """PLV between two channels in a frequency band."""
    c1 = bandpass_filter(ch1, fmin, fmax, fs)
    c2 = bandpass_filter(ch2, fmin, fmax, fs)
    ph1 = np.angle(c1 + 1j * np.gradient(c1))
    ph2 = np.angle(c2 + 1j * np.gradient(c2))
    return float(np.abs(np.mean(np.exp(1j * (ph1 - ph2)))))


def theta_beta_ratio(data, fs=250):
    theta = compute_band_power(data, fs, 4, 8)
    beta = compute_band_power(data, fs, 13, 30)
    return theta / max(beta, 1e-10)


def hjorth_mobility(data):
    return np.sqrt(np.var(np.diff(data)) / max(np.var(data), 1e-10))


def hjorth_complexity(data):
    return hjorth_mobility(np.diff(data)) / max(hjorth_mobility(data), 1e-10)


def extract_layer1_features(eeg_window, fs=250):
    """
    Full Layer 1 feature vector from a 500ms EEG window.

    Parameters
    ----------
    eeg_window : np.ndarray, shape (n_channels, n_samples)
        Channel order: [Fp1, Fp2, Fz, Cz] at indices 0-3.
    fs : int
        Sampling rate in Hz.

    Returns
    -------
    dict of feature name -> float value
    """
    fp1, fp2 = eeg_window[0], eeg_window[1]
    fz, cz = eeg_window[2], eeg_window[3]
    return {
        'alpha_asymmetry':      frontal_alpha_asymmetry(fp1, fp2, fs),
        'theta_plv_fz_cz':      phase_locking_value(fz, cz, fs, 4, 8),
        'beta_plv_fz_cz':       phase_locking_value(fz, cz, fs, 13, 30),
        'theta_beta_ratio_fz':  theta_beta_ratio(fz, fs),
        'theta_beta_ratio_cz':  theta_beta_ratio(cz, fs),
        'hjorth_mob_fp1':       hjorth_mobility(fp1),
        'hjorth_cmp_fp1':       hjorth_complexity(fp1),
        'alpha_power_fp1':      compute_band_power(fp1, fs, 8, 12),
        'alpha_power_fp2':      compute_band_power(fp2, fs, 8, 12),
        'theta_power_fz':       compute_band_power(fz, fs, 4, 8),
    }
