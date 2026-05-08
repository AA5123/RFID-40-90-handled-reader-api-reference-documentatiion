The heartBeatEVT event provides a periodic liveness and health update from the device.

This event includes:
- Device uptime and event sequence number
- Inventory status details such as RFID state and tag count
- Battery health data including charge percentage and state of health

Use this event to:
- Confirm that devices remain online and active
- Monitor inventory progression over time
- Track battery condition in routine health telemetry

### Event Details

| Property | Value |
|---|---|
| Event Type | Heartbeat Event |
| Communication Type | Device to Cloud |
| Applies To | RFD40 Series, RFD90 Series |
| Trigger Condition | Generated at the configured heartbeat interval while the device is active |
| Related Events | [dataEVT](#op-data-evt), [alerts](#op-alerts), [exceptionEVT](#op-exception-evt) |
| Supported API Versions | V1.0, V1.1 |
