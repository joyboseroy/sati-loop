# Phenomenological Probe Design

## Purpose

Probes collect first-person reports that serve as training labels for the personalised classifier. Label quality directly determines classifier quality. Beginners often mislabel subtle laxity as settled — this bias is documented in KNOWN_LIMITATIONS.md.

## Probe delivery

- Timing: random intervals, mean 3 minutes, jitter +/- 90 seconds
- Cue: soft auditory tone (distinct from distraction cue)
- Response window: 5 seconds
- Interface: 3-button response (settled / wandering / unclear)

## Label taxonomy

| Label | Description |
|-------|-------------|
| settled (0) | Attention is with the intended object. Awareness feels clear and present. |
| wandering (1) | Attention has moved away from the intended object to thought content, planning, memory. |
| laxity (2) | Attention is nominally on the object but awareness feels heavy, foggy, or reduced in clarity. |
| unclear | State is genuinely ambiguous. Excluded from training. |

## Important caveats

The distinction between settled and laxity is the most important and the most difficult. Laxity often feels like settled awareness to beginners. Users should be instructed on this distinction before Phase A begins. Even with instruction, early labels will have bias. This is expected and documented.
