# TDM Gating Manual Test Checklist

Manual verification procedures for the hardware TDM gating logic.
Run these before using the taVNS module in any human study.

## Equipment needed

- Oscilloscope
- Multimeter
- ESP32-S3 development board
- Prototype taVNS circuit (before connecting to participant)

## Test 1: Electrical isolation

**Pass criterion:** No continuity between taVNS stimulator ground and EEG sensing ground.

Procedure:
1. Power both circuits from their separate battery rails
2. Measure resistance between stimulator GND and EEG GND
3. Must read >1 MΩ

## Test 2: Kill switch

**Pass criterion:** Stimulation stops within 1ms of kill switch press.

Procedure:
1. Enable TDM gating: `tdm_set_active(true)`
2. Monitor stim gate pin (GPIO33) on oscilloscope
3. Press kill switch (GPIO35)
4. Confirm stim gate goes low within 1ms
5. Confirm stim gate does NOT restart with `tdm_set_active(true)` until hardware reset

## Test 3: TDM timing

**Pass criterion:** Stimulation 400ms, silent 100ms, cycle repeats accurately.

Procedure:
1. Monitor stim gate (GPIO33) and EEG ready (GPIO32) on oscilloscope
2. Enable TDM: `tdm_set_active(true)`
3. Measure: stimulation window = 400ms ± 5ms
4. Measure: silent window = 100ms ± 2ms
5. Confirm EEG ready (GPIO32) goes high only during silent window
6. Confirm settling delay within silent window is ≥ 50ms before EEG ready

## Test 4: No EEG sampling during stimulation

**Pass criterion:** Python signal pipeline rejects all windows flagged as overlapping.

Procedure:
1. Run `closed_loop_controller.py` with Layer 3 active
2. Monitor log output for TDM overlap rejection messages
3. Confirm zero EEG features are computed while stimulation is active

## Test 5: Current limit

**Pass criterion:** Peak output current does not exceed 2.0 mA.

Procedure:
1. Connect 1kΩ test resistor in place of electrode
2. Measure voltage across resistor with oscilloscope
3. Peak current = V / 1000 must be ≤ 2.0 mA
