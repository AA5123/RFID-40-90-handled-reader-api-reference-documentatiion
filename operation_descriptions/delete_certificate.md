The delete_certificate command removes installed certificates from the reader certificate store.

When you run this command, you can delete certificates by type and optionally by name.

Use this command to:
- Remove expired or replaced certificates
- Clean up unused certificate entries
- Manage certificate lifecycle for Wi-Fi, MQTT, and file-store integrations

### Command Details

| Property | Value |
|---|---|
| Pattern Name | Certificate Deletion |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | RFD40 Series, RFD90 Series |
| Related commands | [install_certificate](#op-install-certificate), [get_installed_certificate](#op-get-installed-certificate), [delete_wifi_profile](#op-delete-wifi-profile) |
| Parameters | command, requestId, certificateInfo |
| Supported Certificate Types | server, client, mqtt, wifi, filestore |
| Supported Delete Scope | By type (required), by name (optional), or all certificates of a type |
