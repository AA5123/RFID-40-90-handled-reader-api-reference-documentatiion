The get_current_region command retrieves the reader’s currently applied regulatory region settings.

This command returns:
- Active country and regulatory region assignment
- Supported channel set for the selected region
- Allowed transmit power range information
- Region-level compliance parameters used by the radio

Use this command to:
- Confirm that the device is configured for the correct regulatory region
- Validate channel and power constraints before inventory operations
- Audit compliance settings across deployments

No additional command-specific payload fields are required beyond the standard request envelope fields.

### Command Details

| Property | Value |
|---|---|
| Pattern Name | Regulatory Configuration Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | RFD40 Series, RFD90 Series |
| Related Commands | [get_config](#op-get-config), [get_status](#op-get-status), [get_version](#op-get-version) |
| Required Request Fields | command, requestId |
| Supported Operations | Retrieve active regulatory region settings |
| Supported Response Sections | currentRegion, response |
| Supported API Versions | V1.0, V1.1 |
