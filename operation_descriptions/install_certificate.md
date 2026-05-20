## 1. Description

The `install_certificate` command installs certificates on the device for authentication purposes. Certificates can be downloaded from HTTP sources or provided inline, and stored for WiFi, MQTT, and file store authentication. This command supports various certificate types including CA certificates, client certificates, and client keys.

Use this command to:

- Install WiFi authentication certificates
- Deploy MQTT client and CA certificates
- Configure file store authentication certificates
- Update device security credentials
- Establish secure communication channels

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Certificate Installation |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | RFD40 Series, RFD90 Series |
| Related Commands | [delete_certificate](delete_certificate.md), [get_installed_certificate](get_installed_certificate.md), [config_endpoint](config_endpoint.md) |
| Required Request Fields | `command`, `requestId`, `certDetails` |
| Supported Certificate Types | `client`, `server`, `mqtt`, `wifi`, `filestore`  |
| Supported Authentication Types | `NONE`, `CERTIFICATE` |
| Supported Certificate Sources | `HTTP`, `DIRECT` |
| Supported Verification Types | `NONE`, `VERIFY_PEER`, `VERIFY_HOST`, `VERIFY_HOST_PEER` |
| Supported API Versions | V1.0, V1.1 |

## 3. Before You Begin

Gather certificate details and source information before sending this command. A missing URL, incorrect certificate type, or unsupported authentication method will cause installation to fail.

| What You Need | Details |
|---|---|
| Certificate type | Identify where the certificate will be used — `wifi` for WiFi network authentication, `mqtt` for MQTT client and CA certificates, `filestore` for file store authentication, `client` for client certificates, or `server` for server certificates. |
| Certificate source | Decide how the certificate content is supplied — `HTTP` to download from a remote URL, or `DIRECT` to provide content inline in `certificateBundle`. If `certSource` is omitted, the device defaults to `HTTP`. |
| Certificate URLs | For `HTTP` source: have the full URLs ready for each certificate component (`ca_cert`, `client_cert`, `client_key`). Verify the URLs are reachable from the device's network. |
| Inline certificate content | For `DIRECT` source: have the PEM or base64-encoded certificate content ready to supply in `certificateBundle`. |
| Authentication type | Decide how the certificate download server is secured — `NONE` for open servers, or `CERTIFICATE` for certificate-based download authentication. |
| TLS verification type | Decide the verification level for the remote certificate source connection — `NONE`, `VERIFY_PEER`, `VERIFY_HOST`, or `VERIFY_HOST_PEER`. |
| Logical name | Assign a meaningful logical name for the certificate entry via the `name` field. This name is used when referencing the certificate in other commands such as `set_wifi` and `config_endpoint`. |

## 4. Certificate Types

The `type` field in `certDetails` defines where the certificate will be used. Choose the correct type based on the service that will consume the certificate.

- `filestore` — File store authentication certificates used for authenticating certificate downloads.
- `wifi` — WiFi network authentication certificates for enterprise wireless connections.
- `mqtt` — MQTT client certificates and CA certificates used for TLS-secured broker connections.
- `client` — Client-side certificates for general authentication.
- `server` — Server-side certificates.

## 5. Authentication and Verification Options

### Authentication Types (`authenticationType`)

Specifies the authentication method used to access the remote certificate source when `certSource` is `HTTP`.

- `NONE` — No authentication is used when downloading certificates.
- `CERTIFICATE` — Certificate-based authentication used to download or retrieve certificates. Supply inline CA cert via `caCertificateFileContent`, or leave empty to use an already installed filestore certificate.

### Certificate Sources (`certSource`)

Specifies how the certificate content is supplied. This field is optional — if omitted, the device defaults to `HTTP`.

- `HTTP` — Certificate content is downloaded from remote URLs specified in the `url` array. This is the default when `certSource` is omitted.
- `DIRECT` — Certificate content is provided inline in the `certificateBundle` object. No network download occurs.

### Verification Types (`verificationType`)

Specifies the TLS verification mode used when validating remote endpoints during certificate download.

- `NONE` — No TLS verification is performed.
- `VERIFY_PEER` — Verifies the peer's certificate.
- `VERIFY_HOST` — Verifies the host name matches the certificate.
- `VERIFY_HOST_PEER` — Verifies both the host name and the peer certificate. Recommended for production.

## 6. Rules and Constraints

Violating any of these rules will cause the command to fail or the certificate to be installed incorrectly.

### certSource Defaults

- If `certSource` is omitted, the device defaults to `HTTP` and attempts to download from the URLs in the `url` array.
- If `certSource` is `DIRECT`, the `url` array is ignored — provide content in `certificateBundle` instead.
- `DIRECT` and `HTTP` cannot be combined in the same request.

### Authentication

- `CERTIFICATE` authentication can use inline CA certificate content in `caCertificateFileContent`, or an already installed filestore certificate if that field is empty.
