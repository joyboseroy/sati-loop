/**
 * Sati-Loop: TDM Gate Interface (Layer 3 taVNS / EEG co-acquisition)
 *
 * Enforces temporal separation: stimulate 400ms, silent 100ms.
 * EEG extraction only in silent window. Kill switch is hardware-level.
 *
 * Author: Joy Bose (2026) | License: MIT
 */
#pragma once
#include <stdbool.h>
#include <stdint.h>

#define TDM_STIM_DURATION_MS   400
#define TDM_SILENT_DURATION_MS 100
#define TDM_SETTLE_MS           50
#define TDM_ACQUIRE_MS          50

typedef enum { TDM_IDLE, TDM_STIMULATING, TDM_SETTLING, TDM_ACQUIRING } TDMState;

void     tdm_init(uint8_t stim_pin, uint8_t eeg_ready_pin, uint8_t kill_pin);
void     tdm_set_active(bool active);
bool     tdm_eeg_window_open(void);
bool     tdm_kill_switch_triggered(void);
TDMState tdm_get_state(void);
