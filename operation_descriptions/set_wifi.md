The set_wifi command configures or updates Wi-Fi interface and access point profile settings on the reader.

This command allows you to configure:
- Wi-Fi profile create and modify operations
- Interface enablement and preferred connection behavior
- Access point ESSID and connection settings
- Security type and authentication details for protected networks

Use this command to:
- Provision new Wi-Fi profiles during device onboarding
- Update existing Wi-Fi settings for network changes
- Control security and connection behavior for wireless access

### Command Details

| Property | Value |
|---|---|
| Pattern Name | Wi-Fi Configuration |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | RFD40 Series, RFD90 Series |
| Related Commands | [get_wifi](#op-get-wifi), [delete_wifi_profile](#op-delete-wifi-profile), [set_config](#op-set-config), [install_certificate](#op-install-certificate) |
| Required Request Fields | command, requestId, wifiConfig |
| Supported Operations | CREATE, MODIFY |
| Supported Types | Security types: WPA2Personal, WPA3Personal, WPA2Enterprise, WPA3Enterprise, OWEPublic, Open; enterprise authentication: tls, ttls, peap |
| Supported Profiles | ESSID-based Wi-Fi access point profiles with optional preferred and auto-connect behavior |
| Supported Protocols | Not applicable |
| Supported API Versions | V1.0, V1.1 |

wifiConfig contains the configuration and operation details required by the command.
