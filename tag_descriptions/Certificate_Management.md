## Overview

Install, remove, and inspect TLS/SSL certificates used for secure communication and authentication.

## Commands

| Command | Description |
|---|---|
| `install_certificate` | Upload a certificate (CA, client, MQTT, WiFi) to the device |
| `delete_certificate` | Remove an installed certificate by name |
| `get_installed_certificate` | List all certificates currently on the device |

## Requirements

- Certificates required for MQTT-TLS connections
- Certificates needed for WPA2/WPA3 Enterprise WiFi authentication
- File store certificates for secure file operations
