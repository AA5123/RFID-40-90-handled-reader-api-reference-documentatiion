## 1. Description

The `get_current_region` command retrieves the reader's currently applied regulatory region settings.

This command returns:

- Active country and regulatory region assignment
- Supported channel set for the selected region
- Allowed transmit power range information
- Region-level compliance parameters used by the radio

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Regulatory Configuration Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | RFD40 Series, RFD90 Series |
| Related Commands | [get_status](get_status.md), [get_version](get_version.md) |
| Required Request Fields | command, requestId |
| Supported Operations | Retrieve active regulatory region settings |
| Supported Response Sections | currentRegion, response |
| Supported API Versions | V1.0, V1.1 |

## 3. When to Use This Command

Use `get_current_region` to:

- Confirm that the device is configured for the correct regulatory region
- Validate channel and power constraints before inventory operations
- Audit compliance settings across deployments

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `country` | Is the correct country configured? | The reader must match the regulatory region of its deployment location. |
| `regulatoryStandard` | FCC, ETSI, or another standard? | Determines which transmission rules apply — channels, power limits, and LBT behavior. |
| `maxTxPowerSupported` | What is the allowed power ceiling? | Use this to validate transmit power settings before starting inventory. |
| `lbtEnabled` | Is Listen Before Talk active? | Required in some regions (e.g., ETSI). Affects inventory start behavior. |
| `frequencyHopping` | Is frequency hopping enabled? | Mandatory in most regions. Confirms the radio is operating compliantly. |
| `channelData` | How many channels are available? | The channel list defines where the reader can operate within the region. |

> **Note:** Always run `get_current_region` after device provisioning or region changes to confirm the regulatory settings are correct before starting inventory operations.
