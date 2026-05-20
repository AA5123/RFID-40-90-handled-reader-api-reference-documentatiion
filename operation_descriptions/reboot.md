## 1. Description

The `reboot` command performs a warm reset of the device. After a successful reboot, the device automatically reinitializes its connection to the previously connected server. If the reboot fails, a failure notification is sent.

Use this command to:

- Restart the device for applying configuration changes
- Recover from error states
- Reinitialize device connections
- Apply pending device updates

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Device Reboot |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | RFD40 Series, RFD90 Series |
| Related Commands | [config_events](config_events.md), [config_endpoint](config_endpoint.md), [set_operating_mode](set_operating_mode.md) |
| Required Request Fields | `command`, `requestId` |
| Supported Operations | Warm reset of the device |
| Supported API Versions | V1.0, V1.1 |

## 3. Before You Begin

This is a minimal command with no configuration payload. Confirm the following before sending.

| What You Need | Details |
|---|---|
| Inventory state | The device cannot be rebooted while an RFID inventory operation is in progress. Stop the active inventory using `control_operation` before sending this command. Attempting to reboot during an active inventory returns error code 5. |
| Server reconnection | After a successful reboot, the device automatically reconnects to the previously connected server. No manual reconnection is required. |
| Configuration persistence | All management endpoint configurations are restored after reboot. Only radio operation configurations from control endpoint operations are lost on reboot. |

## 4. Rules and Constraints

Violating any of these rules will cause the command to be rejected.

### Inventory State

- The device cannot be rebooted while an RFID inventory operation is active. Sending `reboot` during an active inventory returns error code 5.
- Use `control_operation` with `operation: STOP` to halt the inventory before sending this command.
