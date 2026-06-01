## 1. Description

The `alerts` event provides detailed, structured alert information from the device for operational monitoring and troubleshooting.

This event includes:

- Alert type, state, and priority classification
- A structured `alertDetails` payload with domain-specific fields
- Alert identifiers covering battery, power, firmware, and network conditions

Use this event to:

- Monitor important status transitions and critical conditions
- Track device health and infrastructure-related changes
- Feed alert pipelines that require structured alert context

## 2. Event Details

| Property | Value |
|---|---|
| Event Type | Alert |
| Communication Type | Device to Cloud |
| Applies To | RFD40 Series, RFD90 Series |
| Trigger Condition | Generated when a device condition transitions state or crosses a monitored threshold |
| Related Events | [heartBeatEVT](heartBeatEVT.md) |
| Supported API Versions | V1.0, V1.1 |

## 3. When This Event Is Published

The reader publishes `alerts` automatically when a monitored device condition changes state or crosses a threshold. No command is required.

| `id` | Trigger Condition | `state` Values |
|---|---|---|
| `BATTERY` | Battery charge or health state changes. | `ONESHOT` |
| `POWER` | Power source changes (e.g., USB to battery). | `ONESHOT` |
| `NETWORK_EVENT` | Wi-Fi or Ethernet interface connects, disconnects, or changes IP. | `ONESHOT` |
| `FIRMWARE_UPDATE` | Firmware update starts, progresses, or completes. | `SET` while in progress, `CLEAR` on completion |
| `TEMPERATURE` | Device temperature crosses a monitored threshold. | `SET` when threshold crossed, `CLEAR` when resolved |
| `GPI_EVENT` | A GPI input state changes. | `ONESHOT` |
| `ANTENNA_EVENT` | An antenna state changes. | `ONESHOT` |

> **Note:** The `state` field tells you whether an alert condition is active or resolved. `SET` means the condition is currently active. `CLEAR` means it has been resolved. `ONESHOT` is a one-time informational event with no persistent state — it fires once and does not require a corresponding CLEAR.
