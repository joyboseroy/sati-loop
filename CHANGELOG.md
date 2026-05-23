# Changelog

## [v1.1] — 2026-05-23

### Changed
- Layer 1 classifier constraint: EEG-only features for temporal precision
- Added temporal processing separation (fast neural path vs slow somatic context)
- Refined cue: subtractive high-frequency roll-off primary, 440 Hz fallback
- State-responsive ambient audio deferred to v1.2 (safety review required)
- Improved TDM gating specification with discharge settling time requirement
- Fixed ESP32 pin conflict (GPIO 22 I2C SCL / I2S DIN collision corrected)

### Added
- Section 4.4 Temporal Processing Separation in spec
- Known Unknowns and Limitations section (Section 9)
- Non-Optimization Constraints section (Section 10)
- Dependency Minimisation Protocol (Section 11)
- fast_features.py and slow_context.py in signal_pipeline/
- tdm_gating.cpp and tdm_gating.h in firmware/esp32/
- safety/ folder with HARDWARE_INTERLOCKS.md and FIRMWARE_SAFETY_RULES.md
- KNOWN_LIMITATIONS.md, Philosophy.md in docs/
- acoustic_dsp.md in protocol/feedback/
- STATUS.md and ROADMAP.md at repo root

### Fixed
- Section numbering corrected throughout spec
- Pin conflict note labelled correctly as v1.0 correction

## [v1.0] — 2026-05-10

### Added
- Initial design specification
- Three-layer architecture (Attentional Scaffold, Autonomic Support, Experimental Modulation)
- Two prototyping paths: Muse S entry (~$450) and OpenBCI research (~$1300)
- Transfer test protocol as primary success metric
- Non-optimisation constraints (hard rules)
- Dependency minimisation protocol
- Bill of materials for both paths and taVNS module
- Companion preprint: The Contemplative Alignment Problem (PsyArXiv)
