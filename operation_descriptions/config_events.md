The config_events command configures or updates event and alert behavior on the reader.

This command allows you to configure:
- Enable or disable individual event streams
- Heartbeat interval and heartbeat payload options
- Threshold values for CPU, RAM, flash, and temperature alerts
- Monitoring and notification behavior for supported device events

Use this command to:
- Control which operational events are emitted by the device
- Tune heartbeat reporting to match monitoring requirements
- Configure threshold-based alerts for proactive device health monitoring

### Command Details

| Property | Value |
|---|---|
| Pattern Name | Event Configuration |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | RFD40 Series, RFD90 Series |
| Related Commands | [config_endpoint](#op-config-endpoint), [reboot](#op-reboot), [get_status](#op-get-status), [set_config](#op-set-config) |
| Required Request Fields | command, requestId, eventConfiguration |
| Supported Operations | Enable and disable events; configure heartbeat and threshold parameters |
| Supported Types | Boolean enable flags for events and integer threshold fields for cpuThreshold, ramThreshold, flashThreshold, temperatureThreshold |
| Supported Profiles | Event profile includes terminalConnection, firmwareUpdate, network, exceptions, ntp, heartbeat, power, battery, and fileDownload |
| Supported Protocols | Not applicable |
| Supported API Versions | V1.0, V1.1 |
