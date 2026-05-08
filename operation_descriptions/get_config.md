The get_config command retrieves a consolidated device configuration snapshot in a single response.

This command returns:
- Device identity, status, and regional configuration data
- Network configuration details for Wi-Fi and Ethernet
- Endpoint and event routing configuration settings
- Certificate inventory and related configuration state

Use this command to:
- Capture full-device configuration for diagnostics
- Validate baseline settings during onboarding or audits
- Compare runtime configuration across devices in a fleet

No additional command-specific payload fields are required beyond the standard request envelope fields.

### Command Details

| Property | Value |
|---|---|
| Pattern Name | Complete Device Configuration Retrieval |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | RFD40 Series, RFD90 Series |
| Related Commands | [get_version](#op-get-version), [get_status](#op-get-status), [get_current_region](#op-get-current-region), [set_config](#op-set-config) |
| Required Request Fields | command, requestId |
| Supported Operations | Retrieve complete device configuration snapshot |
| Supported Response Sections | currentConfig, response |
| Supported API Versions | V1.0, V1.1 |
