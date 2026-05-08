The get_endpoint_config command retrieves endpoint configuration details stored on the reader.

This command returns:
- Configured endpoint definitions on the reader
- Active endpoint routing and transport settings
- Saved endpoint names and endpoint metadata
- Response metadata for query execution

Use this command to:
- Inspect active endpoint connectivity configuration
- Retrieve settings for a specific endpoint by name
- Audit saved endpoint inventory on the device

No additional command-specific payload fields are required beyond the standard request envelope fields.

### Command Details

| Property | Value |
|---|---|
| Pattern Name | Endpoint Configuration Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | RFD40 Series, RFD90 Series |
| Related Commands | [config_endpoint](#op-config-endpoint), [config_events](#op-config-events), [get_config](#op-get-config) |
| Required Request Fields | command, requestId |
| Supported Operations | Retrieve all endpoint configuration or query a specific endpoint by name |
| Supported Response Sections | epDetails, response |
| Supported API Versions | V1.0, V1.1 |
