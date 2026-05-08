The get_version command retrieves reader identity and software version information.

This command returns:
- Reader model information
- Reader serial number and SKU
- Firmware version and component versions
- Manufacturer and company identity metadata

Use this command to:
- Identify the exact device model and serial number
- Verify firmware and component version alignment
- Confirm device software baseline before updates or troubleshooting

No additional command-specific payload fields are required beyond the standard request envelope fields.

### Command Details

| Property | Value |
|---|---|
| Pattern Name | Device Identity and Firmware Retrieval |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | RFD40 Series, RFD90 Series |
| Related Commands | [get_config](#op-get-config), [get_status](#op-get-status), [set_os](#op-set-os) |
| Required Request Fields | command, requestId |
| Supported Operations | Read reader identity and version details |
| Supported Response Sections | readerVersion, response |
| Supported API Versions | V1.0, V1.1 |
