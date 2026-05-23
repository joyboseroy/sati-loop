/**
 * Sati-Loop: Pin Assignments (ESP32-S3-DevKitC-1)
 *
 * IMPORTANT: GPIO22 is I2C SCL only. Do not use for I2S.
 * I2S DIN is assigned to GPIO26.
 *
 * Author: Joy Bose (2026) | License: MIT
 */
#pragma once

// I2C bus
#define PIN_I2C_SDA         21
#define PIN_I2C_SCL         22    // SCL only — not available for I2S

// I2S audio output (MAX98357A)
#define PIN_I2S_BCLK        27
#define PIN_I2S_LRC         25
#define PIN_I2S_DIN         26

// ADC
#define PIN_RESP_ADC        34    // Stretch sensor (ADC1_CH6)

// UART (OpenBCI Cyton path)
#define PIN_CYTON_RX        16
#define PIN_CYTON_TX        17

// Layer 3 taVNS (off by default — research only)
#define PIN_TDM_STIM_GATE   33
#define PIN_TDM_EEG_READY   32
#define PIN_TDM_KILL_SWITCH 35    // Normally-closed, active-low
