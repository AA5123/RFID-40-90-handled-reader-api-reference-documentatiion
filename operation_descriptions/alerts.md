The alerts event provides detailed, structured alert information from the device for operational monitoring and troubleshooting.

This event includes:
- Alert type, state, and priority classification
- A structured alertDetails payload with domain-specific fields
- Alert identifiers covering battery, power, firmware, and network conditions

Use this event to:
- Monitor important status transitions and critical conditions
- Track device health and infrastructure-related changes
- Feed alert pipelines that require structured alert context

### Event Details

| Property | Value |
|---|---|
| Event Type | Alert |
| Communication Type | Device to Cloud |
| Applies To | RFD40 Series, RFD90 Series |
| Trigger Condition | Generated when a device condition transitions state or crosses a monitored threshold |
| Related Events | [alert_short](#op-alert-short), [heartBeatEVT](#op-heartbeat-evt), [exceptionEVT](#op-exception-evt) |
| Supported API Versions | V1.0, V1.1 |
