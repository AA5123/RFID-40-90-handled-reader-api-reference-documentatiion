## 1. Description

The `get_installed_certificate` command retrieves certificate entries currently installed on the reader.

This command returns:

- Installed certificate names and certificate types
- Certificate issuer, serial, and key algorithm details
- Certificate validity period metadata
- Response metadata for query execution


## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Installed Certificate Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | RFD40 Series, RFD90 Series |
| Related Commands | [install_certificate](install_certificate.md), [delete_certificate](delete_certificate.md), [config_endpoint](config_endpoint.md) |
| Required Request Fields | command, requestId |
| Supported Operations | Retrieve installed certificate inventory details |
| Supported Response Sections | installedCerts, response |
| Supported API Versions | V1.0, V1.1 |

## 3. When to Use This Command

Use `get_installed_certificate` to:

- Audit installed certificate inventory on the device
- Confirm certificate availability before endpoint or Wi-Fi configuration
- Verify certificate validity windows for rotation planning

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `type` | Is the correct certificate type installed? | Certificates are scoped by type (`mqtt`, `wifi`, `filestore`). A certificate installed for one type cannot be used by another. |
| `name` | Does the name match what config_endpoint or set_wifi expects? | The `name` is what other commands reference when configuring TLS connections. |
| `validTill` | Is the certificate still within its validity window? | An expired certificate causes TLS connection failures. Check before configuring or rotating. |
| `validFrom` | Is the certificate already active? | A future `validFrom` means the certificate is not yet valid and will be rejected by the broker. |
| `issuerName` | Does it match the expected CA? | Confirms the certificate chain is from the correct issuer for your environment. |
| `serial` | Does the serial match the expected certificate? | Used to uniquely identify a certificate when multiple entries share the same name and type. |
