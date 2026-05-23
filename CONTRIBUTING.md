# Contributing to Sati-Loop

Thank you for your interest. Sati-Loop is an alignment-aware project. Contributions must respect the non-optimisation constraints in the design specification. Any pull request that violates them will be rejected.

## Before you start

Read the [Design Specification](hardware/SatiLoop_Design_Spec_v1_1.md), especially Section 10 (Non-Optimization Constraints) and Section 11 (Dependency Minimisation Protocol).

## Contribution validation rules

All pull requests must satisfy three criteria:

**1. Subtractive feedback verification**
No persistent visual metrics, continuous audio feedback, gamified scoring, or session ratings. The output engine must remain silent during aligned states.

**2. Device-absent transfer verification**
Any new classification feature or intervention modality must be validated against Phase C transfer testing. If it improves in-session performance but does not transfer to unassisted practice, it is rejected.

**3. Modulation decoupling rule**
No modification may link classifier probabilities to automatic adjustment of stimulation parameters (taVNS, tDCS, tACS). Stimulation amplitude is set manually at session start. The classifier may trigger stimulation onset/offset but may not tune its magnitude.

## What we accept

- Bug fixes to firmware, signal pipeline, or app
- Improvements to calibration or scaffold withdrawal logic that preserve alignment
- Additional sensor support (e.g., GSR) as long as it does not feed Layer 1 cue triggering
- Documentation improvements, assembly guides, translations
- Validated improvements to the artifact rejection pipeline

## What we do not accept

- Any form of positive reinforcement (scores, chimes, good-session indicators)
- Gamification (streaks, achievements, levels)
- Real-time adaptation of stimulation parameters based on classifier output
- Claims of detecting Tier 3 or Tier 4 states (equanimity, insight, rigpa, etc.)
- tDCS/tACS in consumer-targeted code paths
- Modifications that disable or bypass the mandatory transfer test protocol

## How to submit

1. Fork the repository
2. Create a feature branch from `main`
3. Make your changes, ensuring existing tests pass
4. Open a pull request against `main`
5. In the PR description, explicitly state how your change satisfies the three validation rules above

## Questions

Open an issue with the label `question`.
