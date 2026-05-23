/**
 * Sati-Loop: Sensor Abstraction Interface
 * Initialises and polls MAX30102 PPG, BNO085 IMU, stretch sensor ADC.
 * Author: Joy Bose (2026) | License: MIT
 */
#pragma once
#include <stdint.h>

void sensors_init(void);
void sensors_poll(void);

float sensors_get_heart_rate(void);
float sensors_get_spo2(void);
float sensors_get_ibi_ms(void);
float sensors_get_pitch_deg(void);
float sensors_get_roll_deg(void);
float sensors_get_resp_raw(void);
