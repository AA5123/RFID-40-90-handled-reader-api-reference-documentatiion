## 1. Description

The `get_operating_mode` command retrieves the reader's current RFID operating mode configuration.

This command returns:

- Active operating profile configuration
- Radio trigger and query behavior settings
- Access operation and metadata reporting configuration
- Response metadata for command execution

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Operating Mode Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | RFD40 Series, RFD90 Series |
| Related Commands | [set_operating_mode](set_operating_mode.md), [control_operation](control_operation.md), [get_post_filter](get_post_filter.md) |
| Required Request Fields | command, requestId |
| Supported Operations | Retrieve active RFID operating mode and profile settings |
| Supported Response Sections | operatingMode, response |
| Supported API Versions | V1.0, V1.1 |

## 3. When to Use This Command

Use `get_operating_mode` to:

- Verify current RFID operating profile selection
- Inspect current query and radio trigger behavior
- Confirm active metadata and access operation settings

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `profiles` | Which profile is currently active? | Confirms whether the reader is running the intended performance profile before starting inventory. |
| `radioStartConditions.trigger` | What starts the inventory? | Verify the trigger mode matches the application — IMMEDIATE for autonomous, PRESSED for manual. |
| `radioStopConditions.trigger` | What stops the inventory? | Prevents unexpected behavior where inventory runs indefinitely or stops too early. |
| `query.session` | Which Gen2 session is in use? | Confirms session alignment with tag population management strategy. |
| `query.tagPopulation` | Is the tag estimate configured correctly? | An inaccurate estimate degrades inventory performance in dense environments. |
| `tagMetaDataToEnable` | Which data fields are being reported? | Unused fields add overhead. Verify only required fields are enabled before a production run. |
