## 1. Description

The `get_config` command retrieves a consolidated device configuration snapshot in a single response.

This command returns:

- Device identity, status, and regional configuration data
- Network configuration details for Wi-Fi and Ethernet
- Endpoint and event routing configuration settings
- Certificate inventory and related configuration state

No additional payload fields are required beyond `command` and `requestId`.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Complete Device Configuration Retrieval |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | RFD40 Series, RFD90 Series |
| Related Commands | [get_version](get_version.md), [get_status](get_status.md), [get_current_region](get_current_region.md) |
| Required Request Fields | command, requestId |
| Supported Operations | Retrieve complete device configuration snapshot |
| Supported Response Sections | currentConfig, response |
| Supported API Versions | V1.0, V1.1 |

## 3. When to Use This Command

Use `get_config` to:

- Capture full-device configuration for diagnostics
- Validate baseline settings during onboarding or audits
- Compare runtime configuration across devices in a fleet

Key sections to check in the response:

| Section | What to Check | Why It Matters |
|---|---|---|
| `readerVersion` | Model, firmware, IoTC version | Confirm device identity and software baseline before applying changes. |
| `deviceStatus` | Radio state, power source, battery | Verify the device is ready before starting inventory operations. |
| `currentRegion` | Country, regulatory standard, power range | Confirm compliance settings match the deployment location. |
| `wifiConfig` | Connected SSID, IP address, security type | Validate network connectivity and Wi-Fi profile configuration. |
| `ethConfig` | Interface status, link state, IP address | Check Ethernet connectivity when Wi-Fi is not the primary network. |
| `epConfig` | Endpoint type, protocol, active topics | Confirm MQTT endpoint configuration and event routing settings. |
| `installedCerts` | Certificate names, types, validity dates | Audit installed certificates before TLS-secured operations. |

> **Note:** `get_config` is the most comprehensive read command available. Use it for full-device audits, onboarding validation, and fleet comparison. For targeted queries, prefer `get_status`, `get_version`, or `get_current_region`.
