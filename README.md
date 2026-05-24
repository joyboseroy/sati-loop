# Sati-Loop

**Alignment-aware contemplative cybernetic platform**

> A closed-loop system that fades itself into obsolescence.

> **Experimental open research platform. Not a medical device. Not intended to diagnose, treat, or induce altered states.**

---

Sati-Loop is an open-source hardware and software platform for contemplative neurotechnology. Unlike existing meditation devices that reward proxy physiological signals (calm EEG, HRV coherence, breathing resonance scores), Sati-Loop uses **negative-only feedback**, **scaffold withdrawal**, and **transfer to unassisted practice** as the only success criterion.

It is built from the ground up to avoid the contemplative alignment problem formalised in the companion paper.

---

## Core principles

- **No positive reinforcement** — the device never rewards calm states
- **No gamification** — no scores, dashboards, streaks, or progress bars
- **Minimal cue only** — a single neutral bone-conduction cue when distraction is detected
- **Scaffold withdrawal** — the device systematically fades its own support as skill develops
- **Transfer test** — the only metric that matters is unassisted practice improvement

---

## Architecture

```
[ Sensors: EEG + PPG + Respiration + IMU ]
                    ↓
[ Layer 1: Attentional Scaffold ]
  EEG-only fast path (500ms windows)
  Mind-wandering onset detection
  Single neutral cue on distraction
                    ↓
[ Layer 2: Autonomic Support (optional) ]
  HRV-guided breath pacing
  Fixed non-contingent ambient audio
                    ↓
[ Layer 3: Experimental Modulation (research only) ]
  taVNS — hardware-isolated, manual current setting
  TDM gating for EEG/stimulation isolation

X  Classifier does NOT tune stimulation
X  No positive reinforcement at any layer
```

---

## Quick start (~$450 entry path)

1. Order the [entry-level BOM](hardware/BOM_entry.md) (Muse S + ESP32 + sensors)
2. Flash the [ESP32 firmware](firmware/esp32/)
3. Install dependencies: `pip install -r requirements.txt`
4. Run the Python signal pipeline: `python signal_pipeline/pipeline.py`
5. Complete the 2-week passive calibration (Phase A)
6. Begin active training (Phase B) — device cues distraction and fades over time

For research-grade EEG see the [research BOM](hardware/BOM_research.md).

---

## Current status

See [STATUS.md](STATUS.md) for what is implemented vs. conceptual.

---

## Companion paper

> Bose, J. (2026). *The Contemplative Alignment Problem: Reward Misspecification in Closed-Loop Meditation Systems.* 

---

## Repository structure

```
sati-loop/
  README.md
  STATUS.md
  ROADMAP.md
  CHANGELOG.md
  CONTRIBUTING.md
  LICENSE
  requirements.txt
  requirements-dev.txt
  .gitignore
  paper/               Link to preprint and figures
  hardware/            Design spec, BOMs, schematics, STL files
  firmware/            ESP32 code including TDM gating
  signal_pipeline/     Python: fast_features, slow_context, classifier
  app/                 Mobile app (in progress)
  protocol/            Transfer test, calibration, taVNS safety
  docs/                Philosophy, known limitations, assembly guide
  safety/              Hardware interlocks, firmware safety rules
  research/            Literature, experiments (future)
```

---

## License

- **Hardware** (schematics, PCB, STL): CERN-OHL-S v2
- **Software / firmware**: MIT
- **Documentation**: CC BY 4.0

Use of the name Sati-Loop for any system that rewards proxy contemplative states, claims Tier 3 or Tier 4 attainments, or connects stimulation to the classifier reward loop is prohibited.

---

## Citation

```
Bose, J. (2026). Sati-Loop: Design Specification for an Alignment-Aware
Contemplative Cybernetic Platform, v1.1. GitHub.
https://github.com/joyboseroy/sati-loop

Bose, J. (2026). The Contemplative Alignment Problem: Reward Misspecification
in Closed-Loop Meditation Systems. 
```
