## 1. Description

The `alert_short` event provides a compact, human-readable alert notification for lightweight event logging and real-time monitoring.

This event includes:

- A short alert identifier and type classification
- Priority level for triage and routing
- A human-readable description of the alert condition

Use this event to:

- Monitor important device notifications in a concise format
- Track firmware, certificate, and network-related outcomes
- Surface battery and power alerts quickly in dashboards and logs

## 2. Event Details

| Property | Value |
|---|---|
| Event Type | Alert Notification |
| Communication Type | Device to Cloud |
| Applies To | RFD40 Series, RFD90 Series |
| Trigger Condition | Generated when a device condition matches a monitored alert threshold or state change |
| Related Events | [alerts](alerts.md), [heartBeatEVT](heartBeatEVT.md) |
| Supported API Versions | V1.0, V1.1 |

## 3. When This Event Is Published

The reader publishes `alert_short` automatically when a monitored device condition is triggered. No command is required.

| Trigger Category | Example Conditions |
|---|---|
| Firmware | Firmware download or update succeeded or failed. |
| Battery | Battery level dropped to LOW or CRITICAL threshold, battery reached FULL charge. |
| Temperature | Temperature crossed HIGH or CRITICAL threshold, or returned to normal. |
| Network | Network interface changed state (e.g., Wi-Fi connected or disconnected). |
| Wi-Fi Configuration | Wi-Fi profile configuration succeeded or failed. |
| Ethernet Configuration | Ethernet configuration succeeded or failed. |
| Power | Power source changed (e.g., switched from battery to USB). |
| Certificate — MQTT | MQTT certificate download or install succeeded or failed (CA, client cert, client key). |
| Certificate — Wi-Fi | Wi-Fi certificate download or install succeeded or failed (CA, client cert, client key). |
| Certificate — Filestore | Filestore certificate download or install succeeded or failed (CA, client cert, client key). |

> **Note:** The `priority` field indicates urgency — `CRITICAL` alerts (e.g., `BATTERY_CRITICAL_SET`) require immediate attention. `LOW` alerts (e.g., `FIRMWARE_DOWNLOAD_SUCCESS`) are informational. Use `priority` to route alerts to the appropriate handler in your application.
