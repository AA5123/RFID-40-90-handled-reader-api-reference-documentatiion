The get_status command retrieves a live health and readiness snapshot from the reader.

This command returns:
- Power source and charging state details
- RFID radio activity and connectivity status
- Device time and NTP synchronization state
- Battery health and capacity metrics

Use this command to:
- Monitor device health and readiness
- Verify device connectivity before starting RFID operations
- Troubleshoot communication, radio, or battery-related issues

No additional command-specific payload fields are required beyond the standard request envelope fields.

### Command Details

| Property | Value |
|---|---|
| Pattern Name | Device Status Retrieval |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | RFD40 Series, RFD90 Series |
| Related Commands | [get_version](#op-get-version), [get_current_region](#op-get-current-region), [get_config](#op-get-config) |
| Required Request Fields | command, requestId |
| Supported Operations | Status retrieval |
| Supported Response Sections | deviceStatus, response |
| Supported API Versions | V1.0, V1.1 |
