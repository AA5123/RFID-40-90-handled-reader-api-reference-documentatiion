## 1. Description

The `get_post_filter` command retrieves the post-filter rules currently configured on the reader.

This command returns:

- Active post-filter criteria currently applied on the device
- Data endpoint filter assignment information
- Match method and pattern behavior configuration
- Report operation filtering settings

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Post-Filter Configuration Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | RFD40 Series, RFD90 Series |
| Related Commands | [set_post_filter](set_post_filter.md), [get_operating_mode](get_operating_mode.md), [control_operation](control_operation.md) |
| Required Request Fields | command, requestId |
| Supported Operations | Retrieve active post-filter configuration |
| Supported Response Sections | postFilterPayload, response |
| Supported API Versions | V1.0, V1.1 |

## 3. When to Use This Command

Use `get_post_filter` to:

- Verify the active tag post-filter configuration
- Confirm data endpoint filter assignments
- Validate match pattern and report operation behavior

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `dataEpType` | Which endpoint does this filter apply to? | Filters are scoped per data endpoint (`DATA_EP1` or `DATA_EP2`). Confirm the correct endpoint has the correct rule. |
| `matchPattern` | Is the pattern correct? | An incorrect pattern means the wrong tags are being included or excluded from reports. |
| `matchPatternMethod` | Is the match method correct? | `PREFIX`, `SUFFIX`, and `REGEX` behave differently. A method mismatch causes incorrect filtering even with a correct pattern. |
| `reportOperation` | Is the filter set to INCLUDE or EXCLUDE? | Determines whether matching tags are reported or suppressed. Verify this before a production inventory run. |

