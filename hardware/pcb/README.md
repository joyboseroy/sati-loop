# PCB Files

KiCad project files and Gerbers will be added here when available.

## Planned boards

- ESP32-S3 sensor carrier (I2C bus, ADC, I2S, BLE antenna)
- taVNS isolated constant-current stimulator (optocoupler-isolated, separate battery rail)

## Status

Not yet implemented.

## Design constraints

Any PCB design must:
- maintain electrical isolation between the taVNS stimulation rail and the EEG sensing rail
- include a hardware kill switch in series with the stimulation output
- expose TDM gating control lines for firmware synchronisation
