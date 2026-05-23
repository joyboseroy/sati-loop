"""
Sati-Loop: Core Closed-Loop Control Pipeline

Ingests BrainFlow streams, runs Layer 1 fast-path classification,
and triggers subtractive acoustic cue on detected mind-wandering.

Usage:
    python pipeline.py --phase A --mac XX:XX:XX:XX:XX:XX
    python pipeline.py --phase B --mac XX:XX:XX:XX:XX:XX
    python pipeline.py --transfer-test

Author: Joy Bose (2026)
License: MIT
"""

import time
import argparse
import numpy as np
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds

from fast_features import extract_layer1_features
from slow_context import extract_somatic_context
from classifier import SatiClassifier


# ── Configuration ────────────────────────────────────────────────────────────

EEG_CHANNELS = [0, 1, 2, 3]        # Fp1, Fp2, Fz, Cz (0-indexed)
FS = 250                            # Hz
WINDOW_SAMPLES = 125                # 500ms at 250 Hz
STEP_SAMPLES = 62                   # 250ms step (50% overlap)

ALPHA_DEFAULT = 0.70                # Initial wandering threshold
TAU_DEFAULT = 3.0                   # Confirmation window (seconds)
ALPHA_MAX = 0.92
TAU_MAX = 8.0


# ── Board initialisation ─────────────────────────────────────────────────────

def init_board(mac_address, use_openbci=False):
    params = BrainFlowInputParams()
    params.mac_address = mac_address
    board_id = BoardIds.CYTON_BOARD if use_openbci else BoardIds.MUSE_S_BOARD
    board = BoardShim(board_id, params)
    board.prepare_session()
    board.start_stream(450000)
    return board


# ── Cue delivery ─────────────────────────────────────────────────────────────

def dispatch_cue():
    """
    Send subtractive acoustic cue command.
    In physical builds, write to BLE characteristic.
    Primary: subtractive high-frequency roll-off in ambient soundscape.
    Fallback (no ambient audio active): 440 Hz sine, 200ms.
    """
    print("[SATI-LOOP CUE] DSP_FILTER_SWEEP: 16kHz -> 1.2kHz, 100ms ramp, 500ms hold")
    # Physical build: board.config_board("DSP_FILTER_SWEEP")


# ── Scaffold withdrawal ──────────────────────────────────────────────────────

def update_scaffold(alpha, tau, session_avg_delta_t, week):
    """Widen threshold and confirmation window as skill improves."""
    if week > 2 and session_avg_delta_t < tau:
        alpha = min(ALPHA_MAX, alpha + 0.02)
        tau = min(TAU_MAX, tau + 0.5)
    return alpha, tau


# ── Main loop ────────────────────────────────────────────────────────────────

def run_session(board, classifier, alpha, tau, phase='B'):
    drift_counter = 0.0
    cue_times = []
    session_start = time.time()

    print(f"[SATI-LOOP] Phase {phase} session started. Alpha={alpha:.2f}, tau={tau:.1f}s")

    try:
        while True:
            raw = board.get_current_board_data(WINDOW_SAMPLES)
            if raw.shape[1] < WINDOW_SAMPLES:
                time.sleep(0.05)
                continue

            eeg_window = raw[EEG_CHANNELS, :]

            # Layer 1: fast EEG features only
            feat_dict = extract_layer1_features(eeg_window, fs=FS)
            feat_vec = np.array(list(feat_dict.values()))
            probs = classifier.predict_proba(feat_vec)
            p_attentive, p_wandering, p_laxity = probs

            # Cue logic
            if p_wandering > alpha:
                drift_counter += (STEP_SAMPLES / FS)
                if drift_counter >= tau:
                    if phase == 'B':
                        dispatch_cue()
                        cue_times.append(time.time())
                    drift_counter = 0.0
            else:
                drift_counter = max(0.0, drift_counter - (STEP_SAMPLES / FS))

            time.sleep(STEP_SAMPLES / FS)

    except KeyboardInterrupt:
        print(f"[SATI-LOOP] Session ended. Cues delivered: {len(cue_times)}")


# ── Entry point ──────────────────────────────────────────────────────────────

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Sati-Loop pipeline')
    parser.add_argument('--phase', choices=['A', 'B'], default='B')
    parser.add_argument('--mac', default='', help='Muse S MAC address')
    parser.add_argument('--openbci', action='store_true')
    parser.add_argument('--transfer-test', action='store_true')
    args = parser.parse_args()

    classifier = SatiClassifier()
    try:
        classifier = SatiClassifier.load('models/classifier.pkl')
        print("[SATI-LOOP] Loaded personalised classifier.")
    except FileNotFoundError:
        print("[SATI-LOOP] No calibrated classifier found. Run Phase A first.")

    board = init_board(args.mac, args.openbci)
    try:
        run_session(board, classifier, ALPHA_DEFAULT, TAU_DEFAULT, phase=args.phase)
    finally:
        board.stop_stream()
        board.release_session()
