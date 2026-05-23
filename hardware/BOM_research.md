# Bill of Materials — Research-Grade Prototype (~USD 1,300)

OpenBCI Cyton board. 8-channel, 24-bit EEG. Recommended for publication-grade data collection.

| Component | Part / Source | Cost (USD) | Notes |
|-----------|---------------|-----------|-------|
| EEG board | OpenBCI Cyton (openbci.com) | 999 | 8ch, 24-bit ADS1299, open ecosystem |
| EEG electrodes | OpenBCI dry comb x8 | 200 | Fp1, Fp2, Fz, Cz, TP9, TP10, C3, C4 |
| Microcontroller | ESP32-S3-DevKitC-1 | 20 | Co-processor for other sensors + BLE |
| PPG sensor | MAX30102 breakout | 9 | As above |
| Respiration sensor | Conductive stretch sensor | 10 | As above |
| IMU | BNO085 breakout | 15 | As above |
| Bone conduction transducer | Dayton Audio BCT-2 | 13 | As above |
| Audio amplifier | MAX98357A I2S | 10 | As above |
| LiPo battery | 1000 mAh 3.7V | 10 | As above |
| Charger | TP4056 USB-C module | 3 | As above |
| 5V boost converter | Adafruit 2030 | 8 | Powers Cyton from LiPo |
| Misc | Wires, connectors, enclosure, 3D print | 30 | |
| **Total** | | **~1,327** | |

## BrainFlow configuration

```python
board_id = BoardIds.CYTON_BOARD
```
