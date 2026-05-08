The alert_short event provides a compact, human-readable alert notification for lightweight event logging and real-time monitoring.

This event includes:
- A short alert identifier and type classification
- Priority level for triage and routing
- A human-readable description of the alert condition

Use this event to:
- Monitor important device notifications in a concise format
- Track firmware, certificate, and network-related outcomes
- Surface battery and power alerts quickly in dashboards and logs

### Event Details

| Property | Value |
|---|---|
| Event Type | Alert Notification |
| Communication Type | Device to Cloud |
| Applies To | RFD40 Series, RFD90 Series |
| Trigger Condition | Generated when a device condition matches a monitored alert threshold or state change |
| Related Events | [alerts](#op-alerts), [heartBeatEVT](#op-heartbeat-evt), [exceptionEVT](#op-exception-evt) |
| Supported API Versions | V1.0, V1.1 |
