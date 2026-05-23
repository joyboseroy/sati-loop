# Acoustic DSP Specification: Subtractive Cue v1.0

## Design principle

The primary cue is a subtractive acoustic shift in a continuous ambient soundscape. This avoids habituation and autonomic startle that fixed-frequency additive tones cause over repeated sessions.

Fallback: 440 Hz sine wave, 200ms, 20ms fade-in/out — only when no ambient audio is active.

## DSP parameters

| Parameter | Value |
|-----------|-------|
| Filter type | 2nd-order resonant low-pass |
| Cutoff: start | 16,000 Hz |
| Cutoff: end | 1,200 Hz |
| Attack | 100ms logarithmic ramp |
| Sustain | 500ms hold |
| Release | 1,500ms linear recovery |
| Maximum SPL | 65 dB (hardware-enforced) |

## DSP flow

```
[ Ambient soundscape ]
        ↓ [ Cue trigger ]
[ Low-pass filter sweep: 16kHz → 1.2kHz, 100ms ramp ]
[ Hold at 1.2kHz for 500ms ]
[ Recover to 16kHz over 1500ms ]
[ Full soundscape resumes ]
```

ESP32 receives command flag `DSP_FILTER_SWEEP` via BLE and drives the MAX98357A I2S amplifier.
