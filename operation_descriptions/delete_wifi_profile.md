The delete_wifi_profile command removes a saved Wi-Fi profile from the reader.

When you run this command, the profile identified by ESSID is deleted from stored Wi-Fi configurations.

Use this command to:
- Remove obsolete or incorrect Wi-Fi profiles
- Clean up profile lists before adding updated configurations
- Manage active and fallback network profile sets

### Command Details

| Property | Value |
|---|---|
| Pattern Name | Wi-Fi Profile Deletion |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | RFD40 Series, RFD90 Series |
| Related commands | [set_wifi](#op-set-wifi), [get_wifi](#op-get-wifi), [delete_certificate](#op-delete-certificate) |
| Parameters | command, requestId, wifiProfileInfo |
| Supported Identifier | essid |
