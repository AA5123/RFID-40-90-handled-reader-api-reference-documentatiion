The exceptionEVT event provides details about runtime component failures and system anomalies on the reader.

This event includes:
- Exception source identification across radio, scanner, and system modules
- Exception code and message for each affected component
- Device uptime and event sequence number at the time of the exception

Use this event to:
- Detect and diagnose radio module failures and configuration errors
- Monitor scanner connectivity and operational issues
- Track system-level resource or runtime anomalies

### Event Details

| Property | Value |
|---|---|
| Event Type | Exception Event |
| Communication Type | Device to Cloud |
| Applies To | RFD40 Series, RFD90 Series |
| Trigger Condition | Generated when a radio, scanner, or system module encounters a runtime error or anomaly |
| Related Events | [alerts](#op-alerts), [heartBeatEVT](#op-heartbeat-evt), [dataEVT](#op-data-evt) |
| Supported API Versions | V1.0, V1.1 |
