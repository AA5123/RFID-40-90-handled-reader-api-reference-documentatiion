## Overview

Restart the device or trigger a firmware update. Both operations interrupt normal device operation and require careful timing.

## Commands

| Command | Description |
|---|---|
| `reboot` | Restart the device and apply pending configuration changes |
| `set_os` | Trigger a firmware update on the device |

## Requirements

- Reboot: No active inventory operation
- Firmware update: Sufficient battery level required
- Both operations apply configuration changes
- Device will reconnect to broker after reboot
