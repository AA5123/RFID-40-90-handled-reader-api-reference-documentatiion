## Overview

Receive automatic alert events when the device crosses a threshold or changes state. Alerts are push-based notifications triggered by device conditions.

## Events

| Event | Description |
|---|---|
| `alerts` | Full alert details including battery, temperature, power, network, firmware conditions |
| `alert_short` | Compact alert summary with human-readable message descriptions |

## Configuration

Enable or disable specific alert types via `config_events` command. Use `config_endpoint` to specify delivery endpoints.
