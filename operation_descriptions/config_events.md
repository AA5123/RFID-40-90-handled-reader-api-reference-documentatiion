## 1. Description

The `config_events` command configures or updates event and alert behavior on the reader.

This command allows you to configure:

- Enable or disable individual event streams
- Heartbeat interval and heartbeat payload options
- Threshold values for CPU, RAM, flash, and temperature alerts
- Monitoring and notification behavior for supported device events

Use this command to:

- Control which operational events are emitted by the device
- Tune heartbeat reporting to match monitoring requirements
- Configure threshold-based alerts for proactive device health monitoring

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Event Configuration |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | RFD40 Series, RFD90 Series |
| Related Commands | [config_endpoint](config_endpoint.md), [reboot](reboot.md), [get_status](get_status.md) |
| Required Request Fields | `command`, `requestId`, `eventConfiguration` |
| Supported Operations | Enable and disable events; configure heartbeat and threshold parameters |
| Supported Event Flags | `antenna`, `terminalConnection`, `firmwareUpdate`, `gpi`, `network`, `exceptions`, `ntp`, `userApp`, `heartbeat`, `power`, `battery`, `temperature`, `fileDownload`, `cpuUsage`, `flashUsage`, `ramUsage` |
| Supported Threshold Fields | `cpuThreshold`, `ramThreshold`, `flashThreshold`, `temperatureThreshold` |
| Supported API Versions | V1.0, V1.1 |

## 3. Before You Begin

Decide which events and alerts your application needs before sending this command. All event flags and threshold fields inside `eventConfiguration` are optional — include only what you need to change.

| What You Need | Details |
|---|---|
| Event flags | Determine which event streams your application needs. Set the corresponding boolean flag to `true` to enable or `false` to disable. Omitted flags retain their current device state. |
| Heartbeat configuration | If enabling the `heartbeat` event, decide the reporting interval (in seconds) and which status fields — `inventoryStatus`, `batteryStatus`, and `userApps` — should be included in each heartbeat message. |
| CPU alert threshold | Know the CPU usage percentage above which you want a CPU alert triggered. Only relevant when `cpuUsage` is enabled. |
| RAM alert threshold | Know the RAM usage percentage above which you want a RAM alert triggered. Only relevant when `ramUsage` is enabled. |
| Flash alert threshold | Know the flash usage percentage above which you want a flash alert triggered. Only relevant when `flashUsage` is enabled. |
| Temperature alert threshold | Know the temperature value above which you want a temperature alert triggered. Only relevant when `temperature` is enabled. |

## 4. Event Types

Each boolean flag in `eventConfiguration` controls an independent event stream on the device.

| Event Flag | Description |
|---|---|
| `antenna` | Antenna-related events, such as connection or disconnection of an antenna. |
| `terminalConnection` | Terminal connection and disconnection events. |
| `firmwareUpdate` | Events related to firmware update progress and completion. |
| `gpi` | General Purpose Input (GPI) state change events. |
| `network` | Network interface events, such as connectivity changes. |
| `exceptions` | Exception and error events from the device runtime. |
| `ntp` | NTP synchronization events. |
| `userApp` | User application lifecycle events. |
| `heartbeat` | Periodic heartbeat messages from the device. Requires `heartbeatConfiguration` if interval or payload options need to be set. |
| `power` | Power source change events, such as switching between battery and external power. |
| `battery` | Battery status events, such as low battery warnings. |
| `temperature` | Temperature monitoring events. Requires `temperatureThreshold` to define the trigger level. |
| `fileDownload` | File download progress and completion events. |
| `cpuUsage` | CPU usage alert events. Requires `cpuThreshold` to define the trigger level. |
| `flashUsage` | Flash storage usage alert events. Requires `flashThreshold` to define the trigger level. |
| `ramUsage` | RAM usage alert events. Requires `ramThreshold` to define the trigger level. |

