/**
 * Sati-Loop: Safety Limits (Firmware-Enforced)
 *
 * These values enforce the hard-coded safety rules from the design spec.
 * Do not increase without safety review.
 *
 * Author: Joy Bose (2026) | License: MIT
 */
#pragma once

// Session duration limits
#define SESSION_MAX_MS      (90UL * 60UL * 1000UL)   // 90 minutes
#define COOLDOWN_MS         (15UL * 60UL * 1000UL)   // 15-minute cooldown

// Audio SPL — hardware gain is set to enforce this; do not increase
#define AUDIO_MAX_SPL_DB     65

// Maximum audio event duration for any state-triggered sound
#define AUDIO_MAX_DURATION_MS  500

// taVNS Layer 3 limits
#define TAVNS_MAX_CURRENT_MA    2.0f   // mA
#define TAVNS_FREQ_HZ           25
#define TAVNS_PULSE_WIDTH_US   250
#define TAVNS_STIM_WINDOW_MS   400     // TDM: stimulation window
#define TAVNS_QUIET_WINDOW_MS  100     // TDM: EEG acquisition window
#define TAVNS_SETTLE_MS         50     // Discharge settling within quiet window
#define TAVNS_MAX_SESSION_S   (30 * 60)  // 30 minutes active stimulation max
#define TAVNS_COOLDOWN_S      (15 * 60)  // 15-minute lockout after trigger
