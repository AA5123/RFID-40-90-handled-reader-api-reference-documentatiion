## 1. Description

The `dataEVT` event provides structured tag and barcode read output from active inventory operations.

This event includes:

- Tag EPC, TID, and USER memory read data
- Read telemetry fields such as RSSI, phase, channel, and seen count
- Access operation results for read, write, lock, and kill actions

Use this event to:

- Consume real-time tag read data from inventory activity
- Track read quality metrics such as RSSI, phase, and seen count
- Capture access operation outcomes for read and write results

## 2. Event Details

| Property | Value |
|---|---|
| Event Type | Data Event |
| Communication Type | Device to Cloud |
| Applies To | RFD40 Series, RFD90 Series |
| Trigger Condition | Generated during an active RFID inventory operation when tags are read |
| Related Events | [heartBeatEVT](heartBeatEVT.md), [alerts](alerts.md) |
| Supported API Versions | V1.0, V1.1 |

## 3. When This Event Is Published

The reader publishes `dataEVT` automatically when an active RFID inventory operation is in progress and one or more tags are read. No command is required.

| Condition | State / Behavior | Notes |
|---|---|---|
| Active inventory operation running | Event published per tag read or per report interval | Frequency depends on `reportFilter` duration setting |
| Tag inventoried by the reader | Tag data fields populated and emitted in payload | Fields such as `channel` and `phase` are only included when `reportFilter` duration is `0` |
| Barcode scanned during operation | `barcodeData` array populated in payload | Includes decoded barcode string and symbology type |

> **Note:** Certain telemetry fields — `channel`, `phase`, and `seenCount` behavior — depend on the `reportFilter` duration setting in the **operating mode configuration**. When `reportFilter` duration is `0`, each individual tag read is reported separately. Otherwise, tags are aggregated and reported at intervals, and `peakRssi` reflects the peak value since the last report.
