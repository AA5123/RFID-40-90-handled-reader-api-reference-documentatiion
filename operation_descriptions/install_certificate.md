## Overview

The `install_certificate` command installs certificates on the device for authentication purposes. Certificates can be downloaded from HTTP sources and stored for WiFi, MQTT, and file store authentication. This command supports various certificate types including CA certificates, client certificates, and client keys.

Use this command to:
- Install WiFi authentication certificates
- Deploy MQTT client and CA certificates
- Configure file store authentication certificates
- Update device security credentials
- Establish secure communication channels

---

### Command Details

| Property | Value |
|---|---|
| Pattern Name | Certificate Installation |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | RFD40 Series, RFD90 Series |

---

## Request Parameters

| Parameter | Description |
|---|---|
| `command` | Specifies the operation to be executed. Must be set to `install_certificate`. |
| `requestId` | A unique identifier for the request allowing tracking and debugging. |
| `certDetails` | Contains certificate installation details including name, type, authentication method, source URL, and verification type. |

---

## Certificate Types

- **filestore** - File store authentication certificates
- **wifi** - WiFi network authentication certificates
- **mqtt** - MQTT client certificates and CA certificates

---

## Authentication & Verification Options

- **Authentication Types**: CERTIFICATE, PASSWORD
- **Sources**: HTTP for certificate download
- **Verification Types**: VERIFY_HOST_PEER, VERIFY_HOST, VERIFY_PEER, NONE

---

## Related Commands

| Command | Description |
|---|---|
| `delete_certificate` | Removes installed certificates from the device. |
| `get_installed_certificate` | Retrieves the list of installed certificates. |
| `config_endpoint` | Configures endpoints that use certificates for authentication. |
