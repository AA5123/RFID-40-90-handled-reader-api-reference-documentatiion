## 1. Description

The `get_status` command retrieves a live health and readiness snapshot from the reader.

This command returns:

- Power source and charging state details
- RFID radio activity and connectivity status
- Device time and NTP synchronization state
- Battery health and capacity metrics


## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Device Status Retrieval |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | RFD40 Series, RFD90 Series |
| Related Commands | [get_version](get_version.md), [get_current_region](get_current_region.md) |
| Required Request Fields | command, requestId |
| Supported Operations | Status retrieval |
| Supported Response Sections | deviceStatus, response |
| Supported API Versions | V1.0, V1.1 |

## 3. When to Use This Command

Use `get_status` to:

- Monitor device health and readiness before starting operations
- Verify device connectivity before starting RFID operations
- Troubleshoot communication, radio, or battery-related issues

Key fields to check in the response:

| Field | What to Check | Expected State |
|---|---|---|
| `radioActivity` | Is an inventory already running? | INACTIVE before starting a new operation. |
| `radioConnection` | Is the radio connected to the broker? | CONNECTED for normal operation. |
| `powerSource` | What is powering the device? | USB, WALLCHARGER, or CRADLE for powered operation. |
| `chargePercentage` | Is the battery sufficient for the task? | Verify before long inventory runs on battery power. |
| `ntp.reach` | Is the NTP server reachable? | Non-zero means NTP is reachable and syncing. 0 means the NTP server is not reachable. |
| `stateOfHealth` | Is the battery healthy? | GOOD for normal operation. AVERAGE or POOR may indicate battery replacement is needed. |

