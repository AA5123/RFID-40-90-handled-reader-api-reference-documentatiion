The dataEVT event provides structured tag and barcode read output from active inventory operations.

This event includes:
- Tag EPC, TID, and USER memory read data
- Read telemetry fields such as RSSI, phase, channel, and seen count
- Access operation results for read, write, lock, and kill actions

Use this event to:
- Consume real-time tag read data from inventory activity
- Track read quality metrics such as RSSI, phase, and seen count
- Capture access operation outcomes for read and write results

### Event Details

| Property | Value |
|---|---|
| Event Type | Data Event |
| Communication Type | Device to Cloud |
| Applies To | RFD40 Series, RFD90 Series |
| Trigger Condition | Generated during an active RFID inventory operation when tags are read |
| Related Events | [heartBeatEVT](#op-heartbeat-evt), [exceptionEVT](#op-exception-evt), [alerts](#op-alerts) |
| Supported API Versions | V1.0, V1.1 |
