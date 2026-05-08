The get_wifi command retrieves saved and active Wi-Fi configuration details from the reader.

This command returns:
- Saved and active Wi-Fi profile configuration details
- Interface network settings and DHCP addressing state
- Access point and security configuration parameters
- Response metadata for command execution

Use this command to:
- Verify connected and saved Wi-Fi profiles
- Check interface addressing and DHCP state
- Validate security setup and profile preference behavior
- Troubleshoot Wi-Fi availability and profile issues

No additional command-specific payload fields are required beyond the standard request envelope fields.

### Command Details

| Property | Value |
|---|---|
| Pattern Name | Wi-Fi Configuration Retrieval |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | RFD40 Series, RFD90 Series |
| Related Commands | [set_wifi](#op-set-wifi), [delete_wifi_profile](#op-delete-wifi-profile), [get_eth](#op-get-eth), [get_config](#op-get-config) |
| Required Request Fields | command, requestId |
| Supported Operations | Retrieve Wi-Fi interface and profile configuration details |
| Supported Response Sections | wifiProfiles, response |
| Supported API Versions | V1.0, V1.1 |
