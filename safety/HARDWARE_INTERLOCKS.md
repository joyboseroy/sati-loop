# Hardware Interlocks for Layer 3 (taVNS)

These constraints are mandatory. Any taVNS implementation not satisfying all four is not Sati-Loop compliant.

## 1. Electrical isolation
The taVNS circuit must run on a physically separate battery rail. It must not share ground with EEG electronics. All digital control lines must pass through optocouplers (e.g., PC817).

## 2. Manual current setting
Stimulation amplitude (0.5 to 2.0 mA) is set by a physical potentiometer at session start. Software may read but must not write the current setting during a session.

## 3. Hardware kill switch
A normally-closed push-button accessible during the session immediately opens the stimulation circuit at hardware level. Software cannot override it.

## 4. TDM gating
Stimulate 400ms, silent acquisition 100ms (including settling time). EEG extraction only in silent windows. Implementation: `firmware/esp32/tdm_gating.cpp`.

> **WARNING:** Layer 3 is research use only. Contraindications: cardiac pacemaker, implanted neural devices, pregnancy, active epilepsy.
