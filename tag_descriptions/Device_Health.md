## Overview

Receive periodic heartbeat events from the device to confirm active status and connection. Monitor continuous device health.

## Events

| Event | Description |
|---|---|
| `heartBeatEVT` | Periodic health pulse including battery status, inventory state, connectivity confirmation |

## Monitoring

Heartbeat events confirm:
- Device is alive and operational
- Connection to broker is active
- Battery and power status
- Inventory operation progress

Configure heartbeat interval via `config_events`. Absence of heartbeats indicates device offline.
