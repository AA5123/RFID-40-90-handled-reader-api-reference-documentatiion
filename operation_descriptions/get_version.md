## 1. Description

The `get_version` command retrieves reader identity and software version information.

This command returns:

- Reader model information
- Reader serial number and SKU
- Firmware version and component versions
- Manufacturer and company identity metadata


## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Device Identity and Firmware Retrieval |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | RFD40 Series, RFD90 Series |
| Related Commands | [get_status](get_status.md), [set_os](set_os.md) |
| Required Request Fields | command, requestId |
| Supported Operations | Read reader identity and version details |
| Supported Response Sections | readerVersion, response |
| Supported API Versions | V1.0, V1.1 |

## 3. When to Use This Command

Use `get_version` to:

- Identify the exact device model and serial number
- Verify firmware and component version alignment
- Confirm device software baseline before updates or troubleshooting

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `model` | RFD40 or RFD90? | Confirm the correct device type is connected before applying model-specific configurations. |
| `firmwareVersion` | Is the firmware up to date? | Compare against the expected baseline before running updates or diagnosing issues. |
| `serialNumber` | Does it match the device label? | Used for asset tracking, support tickets, and device registration. |
| `sku` | Is the correct variant deployed? | SKU identifies the regional and hardware variant of the reader. |
| `detailedVersions.iotcVersion` | Is IoTC at the expected version? | IoTC version determines which MQTT API commands and features are available. |
