# Dataset Format Specification

## Timestamp Standard

All timestamps use:
- Unix epoch milliseconds (UTC)

Example:
```text
1716123456789
````

---

# EEG Stream

Shape:

```python
(samples, channels)
```

Recommended channel order:

```text
FP1, FP2, Fz, Cz, TP9, TP10
```

Sampling rate:

```text
250 Hz
```

---

# HRV / PPG

Fields:

```text
timestamp
heart_rate
rmssd
lf_hf_ratio
signal_quality
```

Update frequency:

```text
1 Hz
```

---

# Respiration

Fields:

```text
timestamp
resp_rate
resp_variance
breath_hold_flag
```

---

# IMU

Fields:

```text
timestamp
pitch
roll
yaw
motion_energy
```

---

# Phenomenological Labels

Labels are participant-generated self-reports delivered during calibration probes.

Current baseline taxonomy:

```text
attentive
wandering
laxity
agitated
uncertain
```

Labels are probabilistic and treated as noisy observations.

---

# Cue Events

Cue log format:

```text
timestamp
cue_type
classifier_probability
cooldown_state
```

---

# File Structure

Recommended session structure:

```text
participant_001/
  eeg.csv
  hrv.csv
  respiration.csv
  imu.csv
  labels.csv
  cues.csv
```

---

# Synchronization

All modalities must:

* synchronize to shared system clock,
* record acquisition latency,
* log dropped packets where applicable.

````

