## 1. Description

The `set_os` command starts a firmware update workflow on the reader using a provided firmware source URL and connection/authentication settings.

This command allows you to configure:

- Firmware download source URL
- Authentication mode for firmware access
- TLS verification mode
- Optional certificate material

Use this command to:

- Roll out firmware upgrades to devices
- Apply maintenance and security firmware releases
- Control how firmware is downloaded and verified

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Firmware Update |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | RFD40 Series, RFD90 Series |
| Related Commands | [get_version](get_version.md), [reboot](reboot.md), [install_certificate](install_certificate.md) |
| Required Request Fields | `command`, `requestId`, `OSUpdateDetails` |
| Supported Operations | Start firmware update using URL, authentication, and verification settings |
| Supported Authentication Types | `NONE`, `CERTIFICATE` |
| Supported Verification Types | `NONE`, `VERIFY_PEER`, `VERIFY_HOST`, `VERIFY_HOST_PEER` |
| Supported Protocols | URI-based firmware source URLs |
| Supported API Versions | V1.0, V1.1 |

## 3. Before You Begin

Prepare your firmware source and access credentials before sending this command. An incorrect URL, authentication mismatch, or missing certificate will cause the update to fail.

| What You Need | Details |
|---|---|
| Firmware URL | Have the full, valid URI to the firmware file ready. The device will download from this URL directly. Verify the URL is reachable from the device's network. |
| Authentication type | Know which authentication method the firmware server requires — `NONE` for open access or `CERTIFICATE` for certificate-based access. |
| Certificate material | For `CERTIFICATE` authentication: either provide the CA certificate content inline as a PEM-formatted string in `caCertificateFileContent`, or provide the file path to a preinstalled certificate in `caCertificateFile`. |
| Verification type | Decide the TLS verification level — `NONE` to skip verification, `VERIFY_PEER` to verify the server's certificate, `VERIFY_HOST` to verify the hostname, or `VERIFY_HOST_PEER` to verify both. |
| Device battery level | Ensure the device is sufficiently charged or connected to external power before initiating a firmware update. A low battery will cause the update to be rejected with error code 14. |
| Flash availability | Confirm there is enough free flash storage on the device to hold the firmware file. Insufficient space returns error code 8. |

## 4. Authentication Types

The `authenticationType` field defines how the device authenticates to the firmware source server.

| authenticationType | Description | Required Fields |
|---|---|---|
| `NONE` | No authentication. The firmware URL is publicly accessible. | None |
| `CERTIFICATE` | Certificate-based authentication. Supply CA certificate content inline or as a file reference. | `caCertificateFileContent` or `caCertificateFile` |

## 5. Verification Types

The `verificationType` field controls the TLS verification behavior during the firmware download connection.

| verificationType | Description |
|---|---|
| `NONE` | No TLS verification is performed. Use only in trusted network environments. |
| `VERIFY_PEER` | Verifies the server's certificate against trusted CAs. |
| `VERIFY_HOST` | Verifies that the server's hostname matches the certificate. |
| `VERIFY_HOST_PEER` | Verifies both the hostname and the server's certificate. Recommended for production environments. |

## 6. Rules and Constraints

Violating any of these rules will cause the command to fail or the firmware update to not complete.

### Firmware URL

- `url` must be a valid URI. The device will attempt to download the firmware directly from this address.
- Ensure the URL is reachable from the device's active network interface before sending the command.

### Device State

- A firmware update cannot be started while another update is already in progress. Sending `set_os` during an active update returns error code 4. Wait for the current update to complete before retrying.
- The device must have sufficient battery charge before initiating a firmware update. A low battery returns error code 14. Connect to external power or charge the device before retrying.
- The device must have sufficient free flash storage to hold the firmware file. Insufficient space returns error code 8.
