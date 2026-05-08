The get_operating_mode command retrieves the reader’s current RFID operating mode configuration.

This command returns:
- Active operating profile configuration
- Radio trigger and query behavior settings
- Access operation and metadata reporting configuration
- Response metadata for command execution

Use this command to:
- Verify current RFID operating profile selection
- Inspect current query and radio trigger behavior
- Confirm active metadata and access operation settings

No additional command-specific payload fields are required beyond the standard request envelope fields.

### Command Details

| Property | Value |
|---|---|
| Pattern Name | Operating Mode Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | RFD40 Series, RFD90 Series |
| Related Commands | [set_operating_mode](#op-set-operating-mode), [control_operation](#op-control-operation), [get_post_filter](#op-get-post-filter) |
| Required Request Fields | command, requestId |
| Supported Operations | Retrieve active RFID operating mode and profile settings |
| Supported Response Sections | operatingMode, response |
| Supported API Versions | V1.0, V1.1 |
