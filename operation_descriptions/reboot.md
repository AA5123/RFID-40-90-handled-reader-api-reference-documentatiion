## Overview

The `reboot` command performs a warm reset of the device. After a successful reboot, the device automatically reinitializes its connection to the previously connected server. If the reboot fails, a failure notification is sent.

Use this command to:
- Restart the device for applying configuration changes
- Recover from error states
- Reinitialize device connections
- Apply pending device updates

---

## Command Details

| Property | Value |
|---|---|
| Pattern Name | Device Reboot |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | RFD40 Series, RFD90 Series |

---

## Request Parameters

| Parameter | Description |
|---|---|
| `command` | Specifies the operation to be executed. Must be set to `reboot`. |
| `requestId` | A unique identifier for the request, allowing tracking and debugging of the operation. |

---

## Important Notes

- Upon successful reboot, the device will reconnect to the previously connected server.
- Configuration changes made via `config_events` and `set_operating_mode` require a reboot to take effect.
- The device may be temporarily unavailable during the reboot process.

---

### Related Commands

| Command | Description |
|---|---|
| `config_events` | Configures device events (changes require reboot). |
| `config_endpoint` | Configures data transmission endpoints. |
| `set_operating_mode` | Configures operating mode (changes may require reboot). |
