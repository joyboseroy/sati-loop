/**
 * Sati-Loop: Audio Output Interface
 * Bone conduction cue delivery via MAX98357A I2S.
 * I2S pins: BCLK=27, LRC=25, DIN=26 (GPIO22 is I2C SCL only).
 * Author: Joy Bose (2026) | License: MIT
 */
#pragma once

void audio_init(void);
void audio_play_cue(void);   // Subtractive DSP sweep or 440Hz fallback
void audio_stop(void);
void audio_set_volume(float level_0_to_1);
