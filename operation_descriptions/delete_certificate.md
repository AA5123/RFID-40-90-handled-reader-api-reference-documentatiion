## 1. Description

The `delete_certificate` command removes a saved certificate from the reader. When you run this command, the certificate identified by name and type is deleted from the device's certificate store.

Use this command to:

- Remove expired or revoked certificates
- Clean up the certificate store before installing updated certificates
- Delete certificates that are no longer needed for Wi-Fi, MQTT, or file store authentication

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Certificate Deletion |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | RFD40 Series, RFD90 Series |
| Related Commands | [install_certificate](install_certificate.md), [get_installed_certificate](get_installed_certificate.md) |
| Required Request Fields | `command`, `requestId`, `certificateInfo` |
| Required Certificate Fields | `type` |
| Supported Certificate Types | `client`, `server`, `mqtt`, `wifi`, `filestore` |
| Supported API Versions | V1.0, V1.1 |

## 3. Before You Begin

Gather certificate information before sending this command. An incorrect type or name that does not match a stored certificate will cause the command to fail.

| What You Need | Details |
|---|---|
| Certificate type | Identify the type of certificate to delete — `wifi`, `mqtt`, `filestore`, `client`, or `server`. The `type` field is required. |
| Certificate name | Provide the logical name of the certificate to delete. If `name` is omitted, all certificates of the matching `type` are deleted. |



## 4. Rules and Constraints

Violating any of these rules will cause the command to fail.

- The `type` field is required. The command will be rejected if `type` is missing.
- If `name` is not provided, all certificates of the specified `type` are deleted.
- The certificate must exist on the device. Attempting to delete a certificate that has not been installed will result in an error.
- Certificates currently in active use (for example, an active Wi-Fi or MQTT connection) should be replaced before deletion.
