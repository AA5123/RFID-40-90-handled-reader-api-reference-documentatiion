## 1. Description

The `heartbeatEVT` event provides a periodic liveness and health update from the device.

This event includes:

- Device uptime and event sequence number
- Inventory status details such as RFID state and tag count
- Battery health data including charge percentage and state of health

Use this event to:

- Confirm that devices remain online and active
- Monitor inventory progression over time
- Track battery condition in routine health telemetry

## 2. Event Details

| Property | Value |
|---|---|
| Event Type | Heartbeat Event |
| Communication Type | Device to Cloud |
| Applies To | RFD40 Series, RFD90 Series |
| Trigger Condition | Generated at the configured heartbeat interval while the device is active |
| Related Events | [dataEVT](dataEVT.md), [alerts](alerts.md) |
| Supported API Versions | V1.0, V1.1 |

## 3. When This Event Is Published

The reader publishes `heartbeatEVT` automatically at the interval configured in `eventConfiguration.heartbeatConfiguration.interval`. No command is required to trigger it.

| Condition | Behavior |
|---|---|
| Heartbeat is enabled and interval is set | Reader publishes the event at every configured interval while active. |
| `inventoryStatus` is enabled in heartbeatConfiguration | The `data.inventoryStatus` block is included in the payload. |
| `batteryStatus` is enabled in heartbeatConfiguration | The `data.batteryAlert` block is included in the payload. |
| Device goes offline | Heartbeat stops. The absence of heartbeat events can itself indicate a connectivity or power issue. |

> **Note:** The heartbeat interval and payload contents are configured via `config_endpoint` under `eventConfiguration.heartbeatConfiguration`. If no heartbeat events are arriving, verify that `heartbeat` is set to `true` and the interval is greater than 0.
