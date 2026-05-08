The set_operating_mode command updates RFID operating behavior on the reader, including profile selection, radio conditions, query behavior, tag access operations, and metadata reporting.

This command allows you to configure:
- Reader operating profile and advanced radio settings
- Access operations such as read, write, lock, and kill
- Radio start and stop trigger conditions
- Query and select behavior used during inventory

Use this command to:
- Optimize performance for your use case
- Tune inventory behavior for dense or dynamic tag populations
- Enable only the tag data fields needed by your application

### Command Details

| Property | Value |
|---|---|
| Pattern Name | Operating Mode Configuration |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | RFD40 Series, RFD90 Series |
| Related Commands | [get_operating_mode](#op-get-operating-mode), [control_operation](#op-control-operation), [set_post_filter](#op-set-post-filter) |
| Required Request Fields | command, requestId, operatingMode |
| Supported Operations | Configure operating profile, query/select behavior, radio triggers, access operations, and metadata reporting |
| Supported Types | Access operations: READ, WRITE, ACCESS, LOCK, KILL; memory banks: EPC, TID, USER, RESERVED; query states: STATE_A, STATE_B, STATE_AB; SL flags: ALL, ASSERTED, DEASSERTED |
| Supported Profiles | Profiles: FAST_READ, CYCLE_COUNT, DENSE_READERS, OPTIMAL_BATTERY, BALANCED_PERFORMANCE, ADVANCED; link profiles: M4_256K, M2_240K, M2_256K, M2_320K, M4_240K, M4_320K, FM0_0K, FM0_320K, M8_240K, M8_256K, M8_320K; sessions: SESSION_0, SESSION_1, SESSION_2, SESSION_3 |
| Supported Protocols | Not applicable |
| Supported API Versions | V1.0, V1.1 |
