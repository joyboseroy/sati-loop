/**
 * Sati-Loop: BLE Nordic UART Service Interface
 * Streams sensor data to phone/laptop; receives cue commands.
 * Author: Joy Bose (2026) | License: MIT
 */
#pragma once
#include <Arduino.h>

void ble_init(void);
void ble_send(const String& message);
String ble_receive(void);     // Returns "" if no command pending
bool ble_connected(void);
