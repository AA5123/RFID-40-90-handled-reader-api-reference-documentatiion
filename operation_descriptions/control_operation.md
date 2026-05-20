## 1. Description

The `control_operation` command configures or updates the active radio or scanner operation state on the reader.

This command allows you to configure:

- Control type selection (RFID or SCANNER)
- Start or stop operation for the selected control type

Use this command to:

- Start RFID inventory operations on demand
- Stop active radio or scanner operations

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | RFID Operation Control |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | RFD40 Series, RFD90 Series |
| Related Commands | [get_operating_mode](get_operating_mode.md), [set_operating_mode](set_operating_mode.md), [get_status](get_status.md) |
| Required Request Fields | `command`, `requestId`, `ctrlOprPayload` |
| Supported Operations | `START`, `STOP` |
| Supported Control Types | `RFID`, `SCANNER` |
| Supported API Versions | V1.0, V1.1 |

## 3. Before You Begin

This is a lightweight command with only two required payload fields. Confirm the following before sending.

| What You Need | Details |
|---|---|
| Control type | Decide which reader subsystem to control — `RFID` for the radio frequency inventory engine, or `SCANNER` for the barcode scanner. |

## 4. Operations

The `operation` field inside `ctrlOprPayload` determines the action performed on the selected reader subsystem.

- **START** — Begins the operation for the selected control type. For `RFID`, this starts the inventory cycle using the currently configured operating mode. 
- **STOP** — Halts the active operation for the selected control type.

## 5. Rules and Constraints

Violating any of these rules will cause the command to fail or the device to return an unexpected response.

### Start Operation

- Sending `START` while an inventory is already running returns error code 11. Use `get_status` to check the current device state before sending `START` if the inventory state is uncertain.
- `control_operation` does not configure operating parameters. Always configure the desired behavior using `set_operating_mode` before sending a `START` command.

### Stop Operation

- Sending `STOP` when no operation is active returns error code 12. This is not a failure — the device is already in the desired idle state. No corrective action is required.


