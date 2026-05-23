/**
 * Sati-Loop: Sampling Rate Configuration
 * Author: Joy Bose (2026) | License: MIT
 */
#pragma once

#define FS_EEG_HZ           250     // EEG: 250 Hz (Muse S and OpenBCI Cyton)
#define FS_PPG_HZ            50     // PPG: 50 Hz
#define FS_RESP_HZ           50     // Respiration: 50 Hz
#define FS_IMU_HZ           100     // IMU: 100 Hz

// Window sizes in samples
#define WINDOW_FAST_MS      500     // Layer 1 fast EEG window: 500ms
#define WINDOW_STEP_MS      250     // Step: 250ms (50% overlap)
#define WINDOW_SLOW_S        30     // Slow somatic context: 30s

#define WINDOW_FAST_SAMPLES (FS_EEG_HZ * WINDOW_FAST_MS / 1000)   // 125
#define WINDOW_STEP_SAMPLES (FS_EEG_HZ * WINDOW_STEP_MS / 1000)   //  62
