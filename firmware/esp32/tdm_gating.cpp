/**
 * Sati-Loop: TDM Gating — ESP32-S3 Implementation
 * Uses esp_timer for sub-millisecond accuracy.
 * WARNING: Do not modify timing constants without safety review.
 * Author: Joy Bose (2026) | License: MIT
 */
#include "tdm_gating.h"
#include "esp_timer.h"
#include "driver/gpio.h"

static uint8_t _stim_pin, _eeg_ready_pin, _kill_pin;
static volatile TDMState _state = TDM_IDLE;
static volatile bool _kill_triggered = false;
static esp_timer_handle_t _tdm_timer;

static void IRAM_ATTR kill_isr(void*) {
    _kill_triggered = true;
    gpio_set_level((gpio_num_t)_stim_pin, 0);
    _state = TDM_IDLE;
}

static void timer_cb(void*) {
    if (_kill_triggered) return;
    switch (_state) {
        case TDM_STIMULATING:
            gpio_set_level((gpio_num_t)_stim_pin, 0);
            gpio_set_level((gpio_num_t)_eeg_ready_pin, 0);
            _state = TDM_SETTLING;
            esp_timer_start_once(_tdm_timer, TDM_SETTLE_MS * 1000);
            break;
        case TDM_SETTLING:
            gpio_set_level((gpio_num_t)_eeg_ready_pin, 1);
            _state = TDM_ACQUIRING;
            esp_timer_start_once(_tdm_timer, TDM_ACQUIRE_MS * 1000);
            break;
        case TDM_ACQUIRING:
            gpio_set_level((gpio_num_t)_eeg_ready_pin, 0);
            gpio_set_level((gpio_num_t)_stim_pin, 1);
            _state = TDM_STIMULATING;
            esp_timer_start_once(_tdm_timer, TDM_STIM_DURATION_MS * 1000);
            break;
        default: break;
    }
}

void tdm_init(uint8_t sp, uint8_t ep, uint8_t kp) {
    _stim_pin = sp; _eeg_ready_pin = ep; _kill_pin = kp;
    gpio_set_direction((gpio_num_t)sp, GPIO_MODE_OUTPUT);
    gpio_set_direction((gpio_num_t)ep, GPIO_MODE_OUTPUT);
    gpio_set_level((gpio_num_t)sp, 0); gpio_set_level((gpio_num_t)ep, 0);
    gpio_set_direction((gpio_num_t)kp, GPIO_MODE_INPUT);
    gpio_set_pull_mode((gpio_num_t)kp, GPIO_PULLUP_ONLY);
    gpio_set_intr_type((gpio_num_t)kp, GPIO_INTR_NEGEDGE);
    gpio_isr_handler_add((gpio_num_t)kp, kill_isr, NULL);
    esp_timer_create_args_t a = {.callback = timer_cb, .name = "tdm"};
    esp_timer_create(&a, &_tdm_timer);
}

void tdm_set_active(bool on) {
    if (_kill_triggered) return;
    if (on && _state == TDM_IDLE) {
        _state = TDM_STIMULATING;
        gpio_set_level((gpio_num_t)_stim_pin, 1);
        esp_timer_start_once(_tdm_timer, TDM_STIM_DURATION_MS * 1000);
    } else if (!on) {
        esp_timer_stop(_tdm_timer);
        gpio_set_level((gpio_num_t)_stim_pin, 0);
        gpio_set_level((gpio_num_t)_eeg_ready_pin, 0);
        _state = TDM_IDLE;
    }
}

bool tdm_eeg_window_open(void) { return _state == TDM_ACQUIRING; }
bool tdm_kill_switch_triggered(void) { return _kill_triggered; }
TDMState tdm_get_state(void) { return _state; }
