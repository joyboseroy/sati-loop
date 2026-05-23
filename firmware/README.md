# ESP32 Firmware

This directory contains embedded firmware scaffolding for the Sati-Loop runtime environment.

Current targets:
- ESP32-S3
- BLE streaming
- session timing
- cue cooldown logic
- TDM gating for future taVNS integration

---

# Current Status

Implemented:
- session timer scaffold
- cooldown state machine
- TDM gating ISR structure
- hardware kill-switch interrupt path

Not implemented:
- production BLE transport
- real EEG acquisition
- persistent storage
- OTA updates

---

# Safety Philosophy

Firmware is intentionally conservative.

The runtime must:
- fail closed,
- reject invalid stimulation states,
- prevent overlapping stimulation/acquisition windows,
- enforce cooldown periods.

---

# TDM Gating

When taVNS is active:
- stimulation and EEG acquisition are temporally separated.

Current target schedule:
- 400ms stimulation
- 100ms silent EEG acquisition

The ADS1299 front-end must never sample during active stimulation.

---

# Future Work

- BLE packet synchronization
- watchdog timer
- battery monitoring
- latency benchmarking
- hardware abstraction layer
