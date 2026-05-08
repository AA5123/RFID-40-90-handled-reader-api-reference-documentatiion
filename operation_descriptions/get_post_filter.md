The get_post_filter command retrieves the post-filter rules currently configured on the reader.

This command returns:
- Active post-filter criteria currently applied on the device
- Data endpoint filter assignment information
- Match method and pattern behavior configuration
- Report operation filtering settings

Use this command to:
- Verify the active tag post-filter configuration
- Confirm data endpoint filter assignments
- Validate match pattern and report operation behavior

No additional command-specific payload fields are required beyond the standard request envelope fields.

### Command Details

| Property | Value |
|---|---|
| Pattern Name | Post-Filter Configuration Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | RFD40 Series, RFD90 Series |
| Related Commands | [set_post_filter](#op-set-post-filter), [get_operating_mode](#op-get-operating-mode), [control_operation](#op-control-operation) |
| Required Request Fields | command, requestId |
| Supported Operations | Retrieve active post-filter configuration |
| Supported Response Sections | postFilterPayload, response |
| Supported API Versions | V1.0, V1.1 |
