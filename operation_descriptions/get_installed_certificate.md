The get_installed_certificate command retrieves certificate entries currently installed on the reader.

This command returns:
- Installed certificate names and certificate types
- Certificate issuer, serial, and key algorithm details
- Certificate validity period metadata
- Response metadata for query execution

Use this command to:
- Audit installed certificate inventory on the device
- Confirm certificate availability before endpoint or Wi-Fi configuration
- Verify certificate validity windows for rotation planning

No additional command-specific payload fields are required beyond the standard request envelope fields.

### Command Details

| Property | Value |
|---|---|
| Pattern Name | Installed Certificate Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | RFD40 Series, RFD90 Series |
| Related Commands | [install_certificate](#op-install-certificate), [delete_certificate](#op-delete-certificate), [config_endpoint](#op-config-endpoint) |
| Required Request Fields | command, requestId |
| Supported Operations | Retrieve installed certificate inventory details |
| Supported Response Sections | installedCerts, response |
| Supported API Versions | V1.0, V1.1 |
