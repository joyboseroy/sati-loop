# Firmware Safety Rules

Enforced at firmware level. Cannot be overridden by application software.

1. No stimulation from Layer 1 or Layer 2 hardware pins
2. Maximum bone conduction SPL: 65 dB (hardware-enforced gain limit)
3. Session duration limit: 90 minutes, then 15-minute mandatory cooldown
4. No continuous audio triggered by positive state classification lasting >500ms
5. Kill switch overrides everything and requires hardware reset to restart

Implementation files: `main.cpp`, `audio.cpp`, `tdm_gating.cpp`.

Firmware runs self-test at boot. If any safety constraint cannot be enforced, the device refuses to start a session.
