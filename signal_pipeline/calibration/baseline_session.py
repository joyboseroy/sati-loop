"""
Sati-Loop: Phase A Baseline Session

Runs the 2-week passive sensing baseline.
Delivers phenomenological probes at random intervals.
Saves timestamped labels for classifier training.

Also implements the resonant frequency calibration protocol:
  5.0, 5.5, 6.0, 6.5, 7.0 bpm x 90 seconds each
  Selects rate with highest HRV coherence.

Author: Joy Bose (2026)
License: MIT
"""

import time
import random
import json
import argparse
import numpy as np
from datetime import datetime
from pathlib import Path


PROBE_LABELS = {
    's': 'settled',
    'w': 'wandering',
    'u': 'unclear',
    'l': 'laxity',
}

RESONANCE_RATES = [5.0, 5.5, 6.0, 6.5, 7.0]  # breaths per minute
RESONANCE_DURATION = 90  # seconds per rate


def phenomenological_probe():
    """Display probe and collect user response."""
    print("\n" + "="*40)
    print("  PROBE: What is your state right now?")
    print("  [s] Settled / attentive")
    print("  [w] Wandering / distracted")
    print("  [l] Laxity / dull")
    print("  [u] Unclear")
    print("="*40)
    response = input("  Response (s/w/l/u): ").strip().lower()
    return PROBE_LABELS.get(response, 'unclear')


def save_label(label, timestamp, session_dir):
    entry = {'timestamp': timestamp, 'label': label, 'datetime': datetime.now().isoformat()}
    label_file = Path(session_dir) / 'labels.jsonl'
    with open(label_file, 'a') as f:
        f.write(json.dumps(entry) + '\n')


def resonance_calibration():
    """
    Run the resonant frequency calibration protocol.
    Returns the rate (bpm) with the highest HRV coherence.
    Defaults to 6.0 bpm if no clear peak.
    """
    print("\n[CALIBRATION] Starting resonant frequency calibration.")
    print("Breathe at each indicated rate for 90 seconds.\n")

    results = {}
    for rate in RESONANCE_RATES:
        period = 60.0 / rate
        print(f"  Breathe at {rate} bpm (one cycle every {period:.1f}s)")
        # In a full implementation, collect HRV and compute coherence here
        # Placeholder: prompt user to rate perceived ease
        input(f"  Press Enter when ready, wait 90 seconds, then press Enter again...")
        coherence = float(input(f"  HRV coherence score (0-1, estimated): ") or "0.5")
        results[rate] = coherence

    best_rate = max(results, key=results.get)
    if results[best_rate] < 0.3:
        best_rate = 6.0
        print(f"  No clear peak found. Defaulting to 6.0 bpm.")
    else:
        print(f"  Resonant frequency: {best_rate} bpm (coherence={results[best_rate]:.2f})")

    return best_rate


def run_phase_a(session_dir, duration_minutes=45, mean_probe_interval=180):
    """
    Run a Phase A session with random phenomenological probes.
    """
    Path(session_dir).mkdir(parents=True, exist_ok=True)
    session_start = time.time()
    session_end = session_start + (duration_minutes * 60)
    next_probe = session_start + random.uniform(
        mean_probe_interval * 0.5, mean_probe_interval * 1.5
    )

    print(f"\n[PHASE A] Session started. Duration: {duration_minutes} min.")
    print("Meditate as usual. Probes will appear at random intervals.")
    print("Press Ctrl+C to end early.\n")

    try:
        while time.time() < session_end:
            if time.time() >= next_probe:
                label = phenomenological_probe()
                save_label(label, time.time(), session_dir)
                jitter = random.uniform(0.5, 1.5)
                next_probe = time.time() + mean_probe_interval * jitter
            time.sleep(1.0)
    except KeyboardInterrupt:
        pass

    print("\n[PHASE A] Session complete.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', choices=['session', 'resonance'], default='session')
    parser.add_argument('--output', default='data/phase_a')
    parser.add_argument('--duration', type=int, default=45)
    args = parser.parse_args()

    if args.mode == 'resonance':
        rate = resonance_calibration()
        config = {'resonant_frequency_bpm': rate}
        Path(args.output).mkdir(parents=True, exist_ok=True)
        with open(f"{args.output}/resonant_frequency.json", 'w') as f:
            json.dump(config, f)
    else:
        run_phase_a(args.output, args.duration)
