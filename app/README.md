# Mobile App

The Sati-Loop mobile app handles:
- Phase A calibration probe delivery
- Phase B active session interface
- Weekly transfer test scheduling
- Adverse effect questionnaire

## Status

Not started. No UI implementation exists.

## Design principles

The app must follow the same constraints as the rest of the system:
- No session scores or performance ratings
- No streaks, badges, or gamification
- No "good session" or "bad session" framing
- Only information shown: session duration, cue count (declining is good), transfer trend

## Planned stack

Flutter (cross-platform iOS and Android). BLE communication with ESP32 via Nordic UART Service.

## Interface screens planned

- Calibration: probe delivery with 4-option response
- Session: minimal — start/stop, session timer only
- Transfer test: weekly unassisted session with app-timed prompts
- Adverse effects: weekly safety questionnaire, separate from session screen
