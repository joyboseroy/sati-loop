"""
Sati-Loop: Artifact Rejection

Cleans raw EEG windows before feature extraction.
Handles: amplitude threshold, eye blinks, jaw clenches, TDM overlap rejection.

Author: Joy Bose (2026)
License: MIT
"""

import numpy as np
from scipy.signal import butter, lfilter


def notch_filter(data, fs, notch_freq=50.0, Q=30.0):
    """Notch filter for line noise (50 Hz or 60 Hz)."""
    from scipy.signal import iirnotch, filtfilt
    b, a = iirnotch(notch_freq, Q, fs)
    return filtfilt(b, a, data)


def bandpass_filter(data, fs, lowcut=0.5, highcut=40.0, order=4):
    nyq = 0.5 * fs
    b, a = butter(order, [lowcut / nyq, highcut / nyq], btype='band')
    return lfilter(b, a, data)


def amplitude_reject(eeg_window, threshold_uv=100.0):
    """Return True if any sample exceeds amplitude threshold (window is bad)."""
    return np.any(np.abs(eeg_window) > threshold_uv)


def blink_detect(fp1, fp2, threshold_uv=75.0):
    """
    Detect eye blink in frontopolar channels.
    Blink: large amplitude, low frequency, symmetric across Fp1/Fp2.
    Returns True if blink detected (treat as missing data, not distraction).
    """
    corr = np.corrcoef(fp1, fp2)[0, 1]
    amp = max(np.max(np.abs(fp1)), np.max(np.abs(fp2)))
    return amp > threshold_uv and corr > 0.7


def jaw_clench_detect(eeg_window, broadband_threshold=150.0):
    """Detect jaw clench as broadband power spike across all channels."""
    rms_per_channel = np.sqrt(np.mean(eeg_window ** 2, axis=1))
    return np.all(rms_per_channel > broadband_threshold)


def tdm_overlap_reject(window_timestamp, stimulation_active_periods):
    """
    Reject EEG window if it overlaps with any taVNS stimulation period.

    Parameters
    ----------
    window_timestamp : float
        Start time of the window (seconds since session start).
    stimulation_active_periods : list of (start, end) tuples
        Periods when stimulation was active.

    Returns
    -------
    bool : True if window overlaps with stimulation (reject it).
    """
    for start, end in stimulation_active_periods:
        if window_timestamp < end and (window_timestamp + 0.5) > start:
            return True
    return False


def preprocess_window(eeg_window, fs=250, stimulation_periods=None, window_ts=None):
    """
    Full preprocessing pipeline for a single EEG window.

    Returns
    -------
    clean : np.ndarray or None
        Cleaned EEG window, or None if window should be rejected.
    reason : str
        Rejection reason, or 'ok'.
    """
    if stimulation_periods and window_ts is not None:
        if tdm_overlap_reject(window_ts, stimulation_periods):
            return None, 'tdm_overlap'

    if amplitude_reject(eeg_window):
        return None, 'amplitude_threshold'

    if eeg_window.shape[0] >= 2:
        if blink_detect(eeg_window[0], eeg_window[1]):
            return None, 'blink'

    if jaw_clench_detect(eeg_window):
        return None, 'jaw_clench'

    # Apply notch (both 50 and 60 Hz) and bandpass
    clean = np.zeros_like(eeg_window)
    for i in range(eeg_window.shape[0]):
        ch = notch_filter(eeg_window[i], fs, 50.0)
        ch = notch_filter(ch, fs, 60.0)
        ch = bandpass_filter(ch, fs, 0.5, 40.0)
        clean[i] = ch

    return clean, 'ok'
