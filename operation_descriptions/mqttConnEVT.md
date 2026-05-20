## 1. Description

The `mqttConnEVT` event provides endpoint connectivity state changes and device identity context for the reader.

This event includes:

- Connection state indicating CONNECTED or DISCONNECTED
- Device model and serial number at the time of the transition
- API and protocol version metadata for the active connection

Use this event to:

- Monitor endpoint connectivity transitions in real time
- Detect reconnect and disconnect behavior in deployment environments
- Correlate connection state with device identity and version context

## 2. Event Details

| Property | Value |
|---|---|
| Event Type | Connection Event |
| Communication Type | Device to Cloud |
| Applies To | RFD40 Series, RFD90 Series |
| Trigger Condition | Generated when the device establishes or loses endpoint connectivity |
| Related Events | [alerts](alerts.md), [heartBeatEVT](heartBeatEVT.md)|
| Supported API Versions | V1.0, V1.1 |

## 3. When This Event Is Published

The reader publishes `mqttConnEVT` automatically whenever the MQTT endpoint connection state changes. No command is required.

| Condition | `connectionState` | Notes |
|---|---|---|
| Device successfully connects to the MQTT broker | `CONNECTED` | Published immediately after a successful connection or reconnection. Includes `timestamp`. |
| Device loses connection to the MQTT broker | `DISCONNECTED` | Published when the connection drops. `timestamp` may not be present if the device cannot reach the broker at the time of disconnect. |
| Device reconnects after a drop | `CONNECTED` | A new CONNECTED event is published each time the device re-establishes the connection. |

