/**
 * Sati-Loop: BLE Service Scaffold
 * Full NimBLE / ArduinoBLE integration pending.
 * Author: Joy Bose (2026) | License: MIT
 */
#include "ble_service.h"
#include <Arduino.h>

static String _pending_cmd = "";

void ble_init(void) {
    // TODO: Initialise BLE Nordic UART Service
    // UUID: 6E400001-B5A3-F393-E0A9-E50E24DCCA9E
    Serial.println("[BLE] Init placeholder.");
}

void ble_send(const String& message) {
    // TODO: Write to TX characteristic
    Serial.println("[BLE TX] " + message);
}

String ble_receive(void) {
    // TODO: Read from RX characteristic
    return _pending_cmd;
}

bool ble_connected(void) {
    return false;  // TODO
}
