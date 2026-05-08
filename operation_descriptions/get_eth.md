The get_eth command retrieves Ethernet interface configuration and connection state from the reader.

This command returns:
- Ethernet interface status and link state details
- DHCP enablement and IPv4 addressing information
- Interface-level network parameters and connectivity metadata
- Response metadata for command execution

Use this command to:
- Verify Ethernet connectivity and link speed
- Check interface status and network addressing
- Confirm DHCP-based IPv4 network configuration
- Troubleshoot wired network availability

No additional command-specific payload fields are required beyond the standard request envelope fields.

### Command Details

| Property | Value |
|---|---|
| Pattern Name | Ethernet Configuration Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | RFD40 Series, RFD90 Series |
| Related Commands | [get_wifi](#op-get-wifi), [get_config](#op-get-config), [set_config](#op-set-config) |
| Required Request Fields | command, requestId |
| Supported Operations | Retrieve Ethernet network configuration and interface status |
| Supported Response Sections | ethConfig, response |
| Supported API Versions | V1.0, V1.1 |
