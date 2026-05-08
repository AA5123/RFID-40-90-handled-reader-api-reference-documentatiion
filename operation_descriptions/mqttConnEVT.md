The mqttConnEVT event provides endpoint connectivity state changes and device identity context for the reader.

This event includes:
- Connection state indicating CONNECTED or DISCONNECTED
- Device model and serial number at the time of the transition
- API and protocol version metadata for the active connection

Use this event to:
- Monitor endpoint connectivity transitions in real time
- Detect reconnect and disconnect behavior in deployment environments
- Correlate connection state with device identity and version context

### Event Details

| Property | Value |
|---|---|
| Event Type | Connection Event |
| Communication Type | Device to Cloud |
| Applies To | RFD40 Series, RFD90 Series |
| Trigger Condition | Generated when the device establishes or loses endpoint connectivity |
| Related Events | [alerts](#op-alerts), [heartBeatEVT](#op-heartbeat-evt), [exceptionEVT](#op-exception-evt) |
| Supported API Versions | V1.0, V1.1 |
