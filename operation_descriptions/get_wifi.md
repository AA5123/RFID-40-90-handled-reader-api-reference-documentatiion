## 1. Description

The `get_wifi` command retrieves saved and active Wi-Fi configuration details from the reader.

This command returns:

- Saved and active Wi-Fi profile configuration details
- Interface network settings and DHCP addressing state
- Access point and security configuration parameters
- Response metadata for command execution

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Wi-Fi Configuration Retrieval |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | RFD40 Series, RFD90 Series |
| Related Commands | [set_wifi](set_wifi.md), [delete_wifi_profile](delete_wifi_profile.md), [get_eth](get_eth.md) |
| Required Request Fields | command, requestId |
| Supported Operations | Retrieve Wi-Fi interface and profile configuration details |
| Supported Response Sections | wifiProfiles, response |
| Supported API Versions | V1.0, V1.1 |

## 3. When to Use This Command

Use `get_wifi` to:

- Verify connected and saved Wi-Fi profiles
- Check interface addressing and DHCP state
- Validate security setup and profile preference behavior
- Troubleshoot Wi-Fi availability and profile issues

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `accessPoint.status` | Is the desired profile CONNECTED? | Confirms the reader is actively using that Wi-Fi network. |
| `accessPoint.essid` | Is it the correct network? | Multiple profiles can be saved — verify the active one is as expected. |
| `accessPoint.isPreferred` | Is the preferred profile set correctly? | The preferred profile is the one the reader always connects to when in range. |
| `accessPoint.securityType` | Does the security type match the AP? | A mismatch prevents connection even if the password is correct. |
| `ipv4Configuration.ipAddress` | Has the device received a valid IP? | No IP address means DHCP failed or the network is unreachable. |
| `ipv4Configuration.enableDhcp` | Is DHCP or static addressing in use? | Determines how the IP address is assigned. |

> **Note:** The response contains an array of all saved Wi-Fi profiles under `wifiProfiles.wifiConfig`. Only the currently connected profile includes `interfaceName`, `macAddress`, `hostname`, and `ipv4Configuration`. Disconnected saved profiles contain only `accessPoint` and `securityDetails`.
