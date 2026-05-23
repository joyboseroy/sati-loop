# Bill of Materials — taVNS Module (~USD 80 DIY)

Layer 3 experimental module. Research use only. Requires electronics experience and safety review before use.

| Component | Part / Source | Cost (USD) | Notes |
|-----------|---------------|-----------|-------|
| Constant current source | XTR111 or Howland pump (discrete) | 15 | Isolated constant current |
| Optocouplers | PC817 x2 (generic) | 3 | Digital isolation from EEG electronics |
| Isolated battery rail | 9V or 3.7V 100mAh LiPo | 10 | Separate from sensing rail |
| Tragus electrode clip | Custom or TENS supplier | 15 | Left ear tragus; stainless steel |
| Manual potentiometer | 10k linear + knob | 5 | Sets current; not software-controlled |
| Kill switch | Normally-closed push-button | 3 | Hardware interrupt; cannot be overridden |
| PCB fabrication | OSHPark or JLCPCB | 25 | With optocoupler isolation barrier |
| Misc | Resistors, capacitors, connectors | 5 | |
| **Total** | | **~81** | |

## Safety requirements

See [../safety/HARDWARE_INTERLOCKS.md](../safety/HARDWARE_INTERLOCKS.md) before building or using this module.

Contraindications: cardiac pacemaker, implanted neural devices, pregnancy, active epilepsy.
