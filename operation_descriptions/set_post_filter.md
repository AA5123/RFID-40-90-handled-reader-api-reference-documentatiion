The set_post_filter command configures which tag reads should be reported by the reader after matching rules are applied.

This command allows you to configure:
- Operation type (ADD, MODIFY, DELETE)
- Data endpoint target (DATA_EP1 or DATA_EP2)
- Match pattern value
- Match method (PREFIX, SUFFIX, REGEX)

Use this command to:
- Reduce unwanted tag reports
- Focus reporting on specific tag patterns
- Update filter logic without changing the inventory command flow

### Command Details

| Property | Value |
|---|---|
| Pattern Name | Post-Filter Configuration |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | RFD40 Series, RFD90 Series |
| Related Commands | [get_post_filter](#op-get-post-filter), [get_operating_mode](#op-get-operating-mode), [control_operation](#op-control-operation) |
| Required Request Fields | command, requestId, postFilterPayload |
| Supported Operations | ADD, MODIFY, DELETE |
| Supported Types | Data endpoint types: DATA_EP1, DATA_EP2; match methods: PREFIX, SUFFIX, REGEX |
| Supported Profiles | Report behavior profiles: INCLUDE, EXCLUDE |
| Supported Protocols | Not applicable |
| Supported API Versions | V1.0, V1.1 |
