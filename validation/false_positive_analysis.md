# False Positive Analysis

False-positive distraction detection is one of the most important failure modes in contemplative cybernetic systems.

Incorrect cue delivery may:
- interrupt genuine settling,
- induce vigilance,
- increase self-monitoring,
- destabilize meditation practice,
- reinforce dependency on external correction.

For this reason:
- classifier precision is prioritized over recall.

---

# Planned Metrics

## False Positive Rate (FPR)

Definition:
```text
FP / (FP + TN)
````

Tracked:

* per session,
* per participant,
* across longitudinal use.

---

# Probe-Verified False Positives

A cue is considered a probable false positive if:

* participant reports stable attention immediately following cue,
* physiological context shows low agitation,
* no self-reported wandering occurs within probe window.

---

# Candidate False Positive Sources

* eye blinks
* jaw clench artifacts
* posture adjustment
* alpha burst unrelated to distraction
* respiratory shifts
* drowsiness transitions
* sensor dropout

---

# Mitigation Strategies

* cooldown periods
* probabilistic hysteresis
* artifact rejection
* minimum persistence thresholds
* individualized calibration

---

# Open Research Question

An unresolved question is whether:

* occasional false positives
  may themselves train maladaptive hypervigilance.

This remains empirically unknown.
