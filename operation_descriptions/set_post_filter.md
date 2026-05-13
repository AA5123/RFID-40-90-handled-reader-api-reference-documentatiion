## 1. Description

The `set_post_filter` command configures which tag reads should be reported by the reader after matching rules are applied.

This command allows you to configure:

- Operation type (ADD, MODIFY, DELETE)
- Data endpoint target (DATA_EP1 or DATA_EP2)
- Match pattern value
- Match method (PREFIX, SUFFIX, REGEX)

Use this command to:

- Reduce unwanted tag reports
- Focus reporting on specific tag patterns
- Update filter logic without changing the inventory command flow

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Post-Filter Configuration |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | RFD40 Series, RFD90 Series |
| Related Commands | [get_post_filter](get_post_filter.md), [get_operating_mode](get_operating_mode.md), [control_operation](control_operation.md) |
| Required Request Fields | `command`, `requestId`, `postFilterPayload` |
| Supported Operations | `ADD`, `MODIFY`, `DELETE` |
| Supported Data Endpoints | `DATA_EP1`, `DATA_EP2` |
| Supported Match Methods | `PREFIX`, `SUFFIX`, `REGEX` |
| Supported Report Behaviors | `INCLUDE`, `EXCLUDE` |
| Supported API Versions | V1.0, V1.1 |

## 3. Before You Begin

Gather the filter details before sending this command. An incorrect match pattern or method mismatch will result in a saved but non-functional filter.

| What You Need | Details |
|---|---|
| Operation type | Decide whether you are adding a new filter (`ADD`), updating an existing one (`MODIFY`), or removing one (`DELETE`). |
| Data endpoint | Identify which data endpoint the filter should apply to — `DATA_EP1` or `DATA_EP2`. |
| Match pattern | Prepare the value to match against the tag ID. For `PREFIX` and `SUFFIX` methods, only hexadecimal digits are allowed and the number of digits must be even. For `REGEX`, prepare a valid regular expression string. |
| Match method | Choose how the pattern is applied — `PREFIX` matches the beginning of the tag ID, `SUFFIX` matches the end, and `REGEX` matches using a regular expression. |
| Report operation | Decide whether matching tags should be reported (`INCLUDE`) or suppressed (`EXCLUDE`). |

## 4. Operations

The `operation` field inside `postFilterPayload` determines the action performed on the post filter.

- **ADD** — Creates a new post filter rule on the specified data endpoint.
- **MODIFY** — Updates an existing post filter rule on the specified data endpoint.
- **DELETE** — Removes an existing post filter rule from the specified data endpoint.

## 5. Match Methods

The `matchPatternMethod` field defines how the `matchPattern` value is compared against the tag ID.

| matchPatternMethod | Description |
|---|---|
| `PREFIX` | Matches the beginning of the tag ID. |
| `SUFFIX` | Matches the end of the tag ID. |
| `REGEX` | Matches the tag ID using a regular expression. |

## 6. Rules and Constraints

Violating any of these rules will cause the command to fail or the filter to behave incorrectly.

### Match Pattern

- For `PREFIX` and `SUFFIX` methods, `matchPattern` must contain only hexadecimal digits (0–9, a–f, A–F) and must have an even number of characters.
- For `REGEX` method, `matchPattern` must be a valid regular expression string.
- An incorrectly formatted pattern will result in a saved but non-functional filter.

### Data Endpoints

- Each filter is scoped to a specific data endpoint (`DATA_EP1` or `DATA_EP2`). Filters applied to one endpoint do not affect the other.
