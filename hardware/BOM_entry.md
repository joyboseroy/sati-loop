# Bill of Materials — Entry-Level Prototype (~USD 450)

Muse S headband + ESP32-S3 module. Sufficient for software validation and personal practice research.

| Component | Part / Source | Cost (USD) | Notes |
|-----------|---------------|-----------|-------|
| EEG headband | Muse S Gen 2 (InteraXon) | 380 | BrainFlow MUSE_S_BOARD; BLE; dry electrodes |
| Microcontroller | ESP32-S3-DevKitC-1 (Espressif / Mouser) | 20 | BLE, WiFi, sufficient SRAM |
| PPG sensor | MAX30102 breakout (Adafruit 4046) | 9 | I2C 0x57; ear clip |
| Respiration sensor | Conductive stretch sensor (Adafruit 1171) | 10 | Voltage divider to GPIO34 |
| IMU | BNO085 breakout (Adafruit 4754) | 15 | I2C 0x4A; on-board fusion |
| Bone conduction transducer | Dayton Audio BCT-2 (Parts Express 295-238) | 13 | 0.5W |
| Audio amplifier | MAX98357A I2S (Adafruit 3006) | 10 | BCLK=27, LRC=25, DIN=26 |
| LiPo battery | 1000 mAh 3.7V (Adafruit 1578) | 10 | 8+ hours |
| Charger | TP4056 USB-C module (generic) | 3 | |
| Misc | Wires, connectors, fabric headband, 3D print | 20 | |
| **Total** | | **~490** | |

## Pin assignments

See [wiring/esp32_pinmap.md](wiring/esp32_pinmap.md) for full pinout.
Critical: GPIO22 is I2C SCL only. I2S DIN must use GPIO26.

## Assembly

See docs/QUICKSTART.md for step-by-step instructions.
