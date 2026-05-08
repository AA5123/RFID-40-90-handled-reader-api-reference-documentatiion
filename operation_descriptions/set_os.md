The set_os command starts a firmware update workflow on the reader using a provided firmware source URL and connection/authentication settings.

This command allows you to configure:
- Firmware download source URL
- Authentication mode for firmware access
- TLS verification mode
- Optional authentication credentials, headers, query parameters, and certificate material

Use this command to:
- Roll out firmware upgrades to devices
- Apply maintenance and security firmware releases
- Control how firmware is downloaded and verified

### Command Details

| Property | Value |
|---|---|
| Pattern Name | Firmware Update |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | RFD40 Series, RFD90 Series |
| Related Commands | [get_version](#op-get-version), [reboot](#op-reboot), [install_certificate](#op-install-certificate) |
| Required Request Fields | command, requestId, OSUpdateDetails |
| Supported Operations | Start firmware update using URL, authentication, and verification settings |
| Supported Types | Authentication types: NONE, BASIC, TOKEN, CERTIFICATE; verification types: NONE, VERIFY_PEER, VERIFY_HOST, VERIFY_HOST_PEER |
| Supported Profiles | Not applicable |
| Supported Protocols | URI-based firmware source URLs |
| Supported API Versions | V1.0, V1.1 |
