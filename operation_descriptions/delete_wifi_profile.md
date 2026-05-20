## 1. Description

The `delete_wifi_profile` command removes a saved Wi-Fi profile from the reader. When you run this command, the profile identified by ESSID is deleted from stored Wi-Fi configurations.

Use this command to:

- Remove obsolete or incorrect Wi-Fi profiles
- Clean up profile lists before adding updated configurations
- Manage active and fallback network profile sets

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Wi-Fi Profile Deletion |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | RFD40 Series, RFD90 Series |
| Related Commands | [set_wifi](set_wifi.md), [get_wifi](get_wifi.md), [delete_certificate](delete_certificate.md) |
| Required Request Fields | `command`, `requestId`, `wifiProfileInfo` |
| Supported Identifier | essid |
| Supported API Versions | V1.0, V1.1 |

## 3. Before You Begin

Gather Wi-Fi profile information before sending this command. An invalid SSID or attempting to delete an active connection will cause the command to fail.

| What You Need | Details |
|---|---|
| SSID | Identify the exact ESSID of the Wi-Fi profile you want to delete. The profile must exist in the saved Wi-Fi configurations. |
| Connection Status | Verify the profile is not currently active. You cannot delete a profile that the device is actively connected to. |

> **Important:** Before deleting a Wi-Fi profile, ensure you are not currently connected to that network. Attempting to delete an active SSID will result in error code 16.
