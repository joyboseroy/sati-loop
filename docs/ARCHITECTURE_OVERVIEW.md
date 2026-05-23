# Architecture Overview

Sati-Loop is an experimental open research platform for alignment-aware contemplative cybernetics.

## What it does

Detects probable mind-wandering onset earlier than the practitioner consciously notices it, delivers a single neutral cue, and systematically withdraws that support as metacognitive skill develops. Transfer to unassisted practice is the only success criterion.

## What it does not do

- Reward calm EEG or any proxy physiological signal
- Detect equanimity, insight, compassion, or any Tier 3/4 contemplative state
- Optimise stimulation parameters against classifier output
- Gamify practice or track streaks

## Three-layer architecture

```
Layer 1 — Attentional Scaffold
  Sensors:       EEG (Fp1, Fp2, Fz, Cz, TP9, TP10)
  Features:      Fast EEG-only, 500ms windows
  Classifier:    Personalised Random Forest
  Output:        Single neutral cue on confirmed distraction
  Constraint:    No positive reinforcement; no stimulation

Layer 2 — Autonomic Support (optional)
  Sensors:       PPG (HRV), respiration, IMU
  Features:      Slow context, 10-30s windows
  Output:        HRV-guided breath pacing; ambient audio
  Constraint:    Does not feed Layer 1 classifier; no proxy reward

Layer 3 — Experimental Modulation (research only)
  Modality:      taVNS (transcutaneous auricular vagus nerve stimulation)
  Constraint:    Hardware-isolated; manual current; TDM gated;
                 never controlled by classifier; off by default
```

## Critical architectural constraint

The intervention engine must never optimise directly against the classifier output.

Stimulation parameters, audio parameters, and cue parameters are fixed at session start. The classifier triggers interventions; it does not tune their magnitude.

## Temporal processing separation

```
Fast neural path (Layer 1)
  Input:    EEG only
  Window:   500ms, step 250ms
  Code:     signal_pipeline/fast_features.py

Slow somatic context path (Layers 2-3)
  Input:    HRV, respiration, IMU
  Window:   10-30 seconds
  Code:     signal_pipeline/slow_context.py
```

Slow modalities must never participate in Layer 1 cue triggering.

## Information flow

```
EEG stream (250 Hz)
    ↓ artifact_rejection.py
    ↓ fast_features.py        ← EEG only
    ↓ classifier.py
    ↓ closed_loop_controller.py
    ↓ cue trigger → ESP32 BLE → bone conduction transducer

PPG / respiration / IMU
    ↓ slow_context.py         ← never to Layer 1
    ↓ Layer 2 breath pacing / ambient audio
```

## Scaffold withdrawal

As the practitioner's unassisted Delta t improves, the classifier threshold T and confirmation window tau are automatically widened, requiring more self-correction before a cue fires. The device fades its own support over weeks.

## Success criterion

    Delta t (Phase C, device absent) < Delta t (Phase A, baseline)

See protocol/Transfer_Test_Protocol.md.
