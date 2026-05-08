The control_operation command configures or updates the active radio or scanner operation state on the reader.

This command allows you to configure:
- Control type selection (RFID or SCANNER)
- Start or stop operation for the selected control type
- Real-time radio activity state management
- Inventory operation lifecycle control

Use this command to:
- Start RFID inventory operations on demand
- Stop active radio or scanner operations
- Manage device activity state in real-time

### Command Details

| Property | Value |
|---|---|
| Pattern Name | RFID Operation Control |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | RFD40 Series, RFD90 Series |
| Related Commands | [get_operating_mode](#op-get-operating-mode), [set_operating_mode](#op-set-operating-mode), [get_status](#op-get-status) |
| Required Request Fields | command, requestId, ctrlOprPayload |
| Supported Operations | START, STOP |
| Supported Types | Control types: RFID, SCANNER |
| Supported Profiles | Not applicable |
| Supported Protocols | Not applicable |
| Supported API Versions | V1.0, V1.1 |
