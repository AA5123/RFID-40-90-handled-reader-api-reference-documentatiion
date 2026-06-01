## 1. Description

The `set_wifi` command configures or updates Wi-Fi interface and access point profile settings on the reader.

This command allows you to configure:

- Wi-Fi profile create and modify operations
- Interface enablement and preferred connection behavior
- Access point ESSID and connection settings
- Security type and authentication details for protected networks

Use this command to:

- Provision new Wi-Fi profiles during device onboarding
- Update existing Wi-Fi settings for network changes
- Control security and connection behavior for wireless access

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Wi-Fi Configuration |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | RFD40 Series, RFD90 Series |
| Related Commands | [get_wifi](get_wifi.md), [delete_wifi_profile](delete_wifi_profile.md), [install_certificate](install_certificate.md) |
| Required Request Fields | `command`, `requestId`, `wifiConfig` |
| Supported Operations | `CREATE`, `MODIFY` |
| Supported Security Types | WPA2Personal, WPA3Personal, WPA2Enterprise, WPA3Enterprise |
| Enterprise Auth Methods | `tls`, `ttls`, `peap` |
| Supported Profiles | ESSID-based Wi-Fi access point profiles with optional preferred and autoconnect behavior |
| Supported API Versions | V1.0, V1.1 |


## 3. Before You Begin

Gather the access point details and security credentials before sending this command. An incorrect ESSID or security mismatch will result in a saved but non-functional profile, and the reader will not connect.

| What You Need | Details |
|---|---|
| Operation type | Decide whether you are creating a new profile (`CREATE`) or updating an existing one (`MODIFY`). Use `CREATE` for first-time provisioning. Use `MODIFY` to update the password, security settings, or connection behavior of an existing profile. |
| ESSID | Have the exact access point network name (ESSID/SSID). The value is case-sensitive. A mismatch results in error code 15 (SSID not found) for `MODIFY`, or creates an unreachable profile for `CREATE`. |
| Security type | Know which security protocol the access point uses — WPA2Personal, WPA3Personal, WPA2Enterprise, or WPA3Enterprise. Must match the AP configuration exactly. |
| Security credentials | For Personal networks: have the passphrase ready. For Enterprise networks: know the authentication protocol (`tls`, `ttls`, `peap`), identity, password, and certificate names already installed on the device. |
| Certificate names (Enterprise) | For WPA2/WPA3 Enterprise with TLS authentication, the `ca_cert`, `client_cert`, and `client_key` must already be installed on the device via `install_certificate`. Have their logical names ready to reference in the `certificate` array. |
| IPv4 strategy | Decide whether the reader will use DHCP (`enableDhcp: true`) or a static IP address. For static, have the IP address, subnet mask, gateway, and DNS server ready. |
| Connection behavior | Decide whether the command should immediately connect (`connect: true`) and whether this profile should always be preferred (`isPreferred: true`). |

## 4. Operations

The `operation` field inside `wifiConfig` determines whether you are creating a new Wi-Fi profile or modifying an existing one.

- **CREATE** — Creates a new Wi-Fi access point profile on the device. The ESSID must not already exist. If a profile with the same ESSID already exists, the command returns error code 18.
- **MODIFY** — Updates an existing Wi-Fi access point profile. The ESSID must already exist on the device. If the ESSID is not found, the command returns error code 15.


## 5. Security Types

The `securityType` field in the `security` object defines the authentication and encryption method for the access point. Choose the type that matches your network's security configuration.

| securityType | Description | Authentication |
|---|---|---|
| WPA2Personal | WPA2 with Pre-Shared Key. Standard password-protected home and office Wi-Fi. | Password |
| WPA3Personal | WPA3 with Simultaneous Authentication of Equals (SAE). More secure than WPA2. | Password |
| WPA2Enterprise | WPA2 with 802.1X authentication. Used in corporate and institutional networks. | `tls` \| `ttls` \| `peap` |
| WPA3Enterprise | WPA3 with 802.1X authentication. Higher security for enterprise environments. | `tls` \| `ttls` \| `peap` |

## 6. Rules and Constraints

Violating any of these rules will cause the command to fail or the Wi-Fi profile to be configured incorrectly.

### Profile Operations

- `CREATE` fails with error code 18 if a profile with the same ESSID already exists. Delete the existing profile first, or use `MODIFY` to update it.
- `MODIFY` fails with error code 15 if the ESSID does not exist. Use `CREATE` for new profiles.

### Connection Behavior

- `connect: true` — The device disconnects from the currently active profile and immediately connects to the specified ESSID.
- `connect: false` — The profile is saved but the device does not switch connections. Use this for pre-provisioning profiles.
- `isPreferred: true` — The device will always attempt to connect to this ESSID when it is in range.

### Enterprise Authentication

- Certificates referenced in the `certificate` array must already be installed on the device using `install_certificate` before this command is sent.
- `innerAuthentication` is optional for `ttls` and `peap` authentication methods.

### Profile Limits

- The device has a maximum number of saved Wi-Fi profiles. Exceeding this limit returns error code 19. Maximum 10 profiles.

- Delete unused profiles using `delete_wifi_profile` before adding new ones when the limit is reached.

