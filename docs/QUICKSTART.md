# Quick Start

Entry-level prototype: Muse S headband + ESP32-S3 module (~$450).

## 1. Install dependencies

```bash
pip install -r requirements.txt
```

## 2. Validate the EEG stream

```bash
python signal_pipeline/pipeline.py --validate --mac <your_muse_mac>
```

Confirm four EEG channels with reasonable signal quality before proceeding.

## 3. Calibrate resonant frequency

Run the 10-minute breathing calibration to find your personal HRV resonant frequency:

```bash
python signal_pipeline/calibration/baseline_session.py --mode resonance
```

## 4. Phase A — Passive baseline (weeks 1-2)

No cues. Phenomenological probes at random intervals. Respond honestly: settled, wandering, or unclear.

```bash
python signal_pipeline/pipeline.py --phase A --mac <your_muse_mac>
```

## 5. Train the classifier

After two weeks of Phase A data:

```bash
python signal_pipeline/classifier.py --train
```

## 6. Phase B — Active training (weeks 3-8)

The device will cue distraction and gradually fade its own support.

```bash
python signal_pipeline/pipeline.py --phase B --mac <your_muse_mac>
```

Run a weekly device-absent transfer session to measure whether skill is transferring:

```bash
python signal_pipeline/pipeline.py --transfer-test
```
