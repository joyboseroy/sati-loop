# Calibration Protocol

## Purpose

Phase A calibration collects personalised EEG baselines and phenomenological labels to train the individual classifier. Label quality directly affects classifier quality.

## Duration

2 weeks. Minimum 5 sessions of 30-45 minutes each.

## Procedure

### Session setup
- Fit headband, verify electrode contact quality
- Confirm BrainFlow stream is stable (check artifact rate)
- Sit in usual meditation posture

### Passive sensing
- Begin normal meditation practice
- No cues are delivered during Phase A
- Practice as you normally would

### Phenomenological probes
- Random intervals (mean 3 minutes, jitter +/- 90 seconds)
- Soft auditory probe tone (distinct from distraction cue)
- Respond within 5 seconds:
  - **S** = settled / attentive
  - **W** = wandering / distracted
  - **L** = laxity / dull and foggy
  - **U** = unclear

### Important instructions for participants
Explain the settled/laxity distinction carefully before starting. Laxity often feels like settled awareness to beginners. Ask: "Is your awareness bright and clear, or is it there but a bit heavy or foggy?" Laxity is the foggy version.

## Resonant frequency calibration

Run once at end of Week 1. See `calibration/baseline_session.py --mode resonance`.

Breathe at each rate for 90 seconds: 5.0, 5.5, 6.0, 6.5, 7.0 bpm. The rate producing highest HRV coherence is stored as the personal resonant frequency for Layer 2 breath pacing.

## Output

- `data/phase_a/labels.jsonl` — timestamped probe responses
- `data/phase_a/resonant_frequency.json` — personal resonant frequency
- After training: `signal_pipeline/models/classifier_<id>.pkl`

## Minimum label counts

- At least 30 labelled instances per class for a usable classifier
- Discard "unclear" responses from training (use for uncertainty estimation)
