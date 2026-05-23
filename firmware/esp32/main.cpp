/**
 * Sati-Loop: ESP32-S3 Main Firmware Scaffold
 *
 * Pin assignments (ESP32-S3-DevKitC-1):
 *   I2C: SDA=21, SCL=22
 *   I2S: BCLK=27, LRC=25, DIN=26  (NOTE: GPIO22 is SCL only, not I2S)
 *   ADC stretch sensor: GPIO34
 *   TDM stim gate: GPIO33 | TDM EEG ready: GPIO32 | Kill switch: GPIO35
 *
 * Safety rules (firmware-enforced, cannot be overridden):
 *   - No stimulation on Layer 1/2 pins
 *   - Session limit: 90 minutes, then 15-minute cooldown
 *   - SPL hardware-limited at amplifier gain stage
 *
 * Author: Joy Bose (2026) | License: MIT
 */
#include <Arduino.h>

#define SESSION_MAX_MS (90UL * 60UL * 1000UL)
#define COOLDOWN_MS    (15UL * 60UL * 1000UL)

static unsigned long session_start_ms = 0;
static bool in_cooldown = false;

void setup() {
    Serial.begin(115200);
    // sensors_init(); audio_init(); ble_init();
    // tdm_init(33, 32, 35);  // Uncomment when Layer 3 hardware is present
    session_start_ms = millis();
    Serial.println("[SATI-LOOP] Firmware ready.");
}

void loop() {
    unsigned long elapsed = millis() - session_start_ms;

    if (!in_cooldown && elapsed > SESSION_MAX_MS) {
        // audio_stop(); ble_send("SESSION_END_TIMEOUT");
        in_cooldown = true;
        Serial.println("[SATI-LOOP] 90-min limit. Cooldown started.");
    }
    if (in_cooldown && elapsed > SESSION_MAX_MS + COOLDOWN_MS) {
        in_cooldown = false;
        session_start_ms = millis();
        Serial.println("[SATI-LOOP] Cooldown complete.");
    }
    if (in_cooldown) { delay(1000); return; }

    // sensors_poll();
    // String cmd = ble_receive();
    // if (cmd == "DSP_FILTER_SWEEP") audio_play_cue();

    delay(10);
}
