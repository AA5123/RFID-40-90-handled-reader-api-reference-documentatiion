## 1. Description

The `set_operating_mode` command updates RFID operating behavior on the RFD40/RFD90 reader, covering profile selection, radio conditions, query behavior, tag access operations, and metadata reporting.

**This command allows you to configure:**

- Reader operating profile and advanced radio settings
- Access operations such as read, write, lock, and kill
- Radio start and stop trigger conditions
- Query and select behavior used during inventory

**Use this command to:**

- Optimize performance for your use case
- Tune inventory behavior for dense or dynamic tag populations
- Enable only the tag data fields needed by your application

### Command Details

| Property | Value |
|---|---|
| Pattern Name | Operating Mode Configuration |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | RFD40 Series, RFD90 Series |
| Related Commands | [get_operating_mode](get_operating_mode.md), [control_operation](control_operation.md), [set_post_filter](set_post_filter.md) |
| Required Request Fields | `command`, `requestId`, `operatingMode` |
| Supported Operations | Configure operating profile, query/select behavior, radio triggers, access operations, and metadata reporting |
| Supported Access Operations | READ, WRITE, ACCESS, LOCK, KILL |
| Supported Memory Banks | EPC, TID, USER, RESERVED |
| Supported Query States | STATE_A, STATE_B, STATE_AB |
| Supported SL Flags | ALL, ASSERTED, DEASSERTED |
| Supported Profiles | CYCLE_COUNT, DENSE_READERS, OPTIMAL_BATTERY, BALANCED_PERFORMANCE, ADVANCED |
| Supported Link Profiles | M4_256K, M2_240K, M2_256K, M2_320K, M4_240K, M4_320K, FM0_0K, FM0_320K, M8_240K, M8_256K, M8_320K |
| Supported Sessions | SESSION_0, SESSION_1, SESSION_2, SESSION_3 |
| Supported API Versions | V1.0, V1.1 |

## 2. Before You Begin

Decide which aspects of the operating mode you need to configure before sending this command. You can send a minimal payload targeting only one sub-section (for example, only `profiles` or only `query`), or send a full configuration in a single command.

| What You Need | Details |
|---|---|
| Operating profile decision | Choose a preset profile (e.g., `BALANCED_PERFORMANCE`, `CYCLE_COUNT`) or use `ADVANCED` if you need to set a specific link profile, transmit power, or session manually. |
| Access operation types | Know which tag memory banks you will read from or write to, and whether lock or kill operations are required. Have passwords ready for access, lock, or kill operations. |
| Radio trigger strategy | Decide when the reader should start and stop inventory — immediately, on trigger press, or on trigger release. Know thresholds such as tag count or inventory count for auto-stop. |
| Query parameters | Know your expected tag population size and whether you need to target a specific inventory state (`STATE_A`, `STATE_B`) or SL flag. |
| Select / prefilter criteria | If filtering tags by memory content, have the tag pattern (hex string), memory bank, bit offset, and pattern length ready. |
| Metadata requirements | Know which tag metadata fields (RSSI, TID, USER, MAC, etc.) your backend application needs. Enabling unnecessary fields increases data volume. |
| Inventory state | `set_operating_mode` cannot be sent while inventory is in progress. Stop any active inventory first — error code 11 is returned if violated. |

## 3. Choosing an Operating Profile

The `profiles` field selects the reader's overall RF operating mode. Choose based on your deployment environment and performance priorities.

| Profile | Description |
|---|---|
| `CYCLE_COUNT` | Reads as many unique tags as possible in each inventory cycle. |
| `DENSE_READERS` | Optimised for environments with multiple readers operating in proximity. |
| `OPTIMAL_BATTERY` | Prioritises battery longevity over read performance. |
| `BALANCED_PERFORMANCE` | Maintains a balance between read performance and battery life. **This is the default.** |
| `ADVANCED` | Unlocks manual control of `transmitPower`, `linkProfile`, `session`, and `dynamicPower` via `advancedConfigurations`. `advancedConfigurations` is required when this profile is selected. |

## 4. Choosing Access Operations

Access operations let the reader do more than just read the EPC during inventory. Each entry in the `accessOperations` array runs against every tag singulated in that inventory cycle. Choose operations based on what your application needs to do with each tag.

| Operation | What It Does | Key Constraints |
|---|---|---|
| `READ` | Reads a block of words from a specific memory bank starting at a given word offset. | `offset` is in 16-bit words. `length` is the number of words to read. Multiple READ operations targeting different banks can be combined. |
| `WRITE` | Writes a hex data string to a specific memory bank location. | `data` must be a hex string with an even character count and a length that is a multiple of 16-bit words. `password` (8 hex chars) is required even if no access password is set — use `00000000`. |
| `ACCESS` | Authenticates to the tag using the access password, enabling subsequent protected operations. | `password` must be exactly 8 hex characters (32 bits). If the tag has no password set, use `00000000`. |
| `LOCK` | Locks or unlocks a specified memory bank, or permanently locks it so it can never be changed again. | `lockAction: PERMANENT_LOCK` is irreversible. `lockMemBank` additionally supports `ACCESS_PWD` and `KILL_PWD` beyond the standard memory banks. |
| `KILL` | Permanently and irreversibly disables the tag. The tag will never respond to any reader again. | This operation cannot be undone. `password` must match the tag's kill password exactly. |

## 5. Choosing Radio Start and Stop Conditions

Radio conditions define when the reader begins and ends an inventory round. Start and stop conditions are configured independently — you can mix trigger types across start and stop.

### Start Trigger

| `trigger` Value | Behavior |
|---|---|
| `IMMEDIATE` | Inventory starts as soon as the command is applied. No physical action required. |
| `PRESSED` | Inventory starts when the operator presses the physical trigger button. |
| `RELEASED` | Inventory starts when the operator releases the trigger button. |

### Stop Trigger and Thresholds

| Field | What It Controls |
|---|---|
| `trigger: RELEASED` | Inventory stops when the operator releases the trigger. |
| `trigger: PRESSED` | Inventory stops when the trigger is pressed. |
| `trigger: IMMEDIATE` | Inventory stops based on threshold conditions rather than a physical action. |
| `tagCount` | Stops inventory after the specified number of unique tags have been read. |
| `stopTimeout` | Stops inventory after the specified duration in milliseconds. |
| `inventoryCount` | Stops inventory after the specified number of full inventory cycles complete. |

## 6. Choosing Query Settings

Query parameters directly affect how the reader singulates tags during inventory. Choosing the right session, inventory state, SL flag, and tag population estimate can significantly improve read rates in dense environments.

### `session`

| Value | Persistence |
|---|---|
| `SESSION_0` | Tag forgets its state immediately after leaving the RF field. |
| `SESSION_1` | Tag retains state for 500 ms to 5 seconds after leaving the RF field. |
| `SESSION_2` | Tag retains state for >2 seconds (implementation-dependent; can be much longer). |
| `SESSION_3` | Tag retains state indefinitely until changed by a reader. |

### `inventoryState`

| Value | Which Tags Respond |
|---|---|
| `STATE_A` | Only tags currently in inventory state A respond. |
| `STATE_B` | Only tags currently in inventory state B respond. |
| `STATE_AB` | Reader alternates between STATE_A and STATE_B across inventory rounds. |

### `slFlag`

| Value | Which Tags Are Selected |
|---|---|
| `ALL` | All tags regardless of SL flag state. |
| `ASSERTED` | Only tags with the SL flag asserted (set to 1). |
| `DEASSERTED` | Only tags with the SL flag deasserted (set to 0). |

### `tagPopulation`

`tagPopulation` is an estimate of how many tags the reader expects to find in the field. The reader uses this to tune its Q parameter — the algorithm that controls how many slots are allocated during singulation.

## 7. Choosing Select (Prefilter) Settings

Select filters instruct the reader to pre-screen tags before inventory — only tags whose memory content matches the pattern are eligible to respond. This reduces unnecessary singulation and improves performance in mixed-tag environments.

### Choosing the Right `memoryBank` for Filtering

| `memoryBank` | Filter Based On |
|---|---|
| `EPC` | The tag's EPC identifier — company prefix, item reference, or serial portion. |
| `TID` | The factory-programmed chip identifier — chip type, manufacturer, and unique serial. |
| `USER` | Application-specific data written to the tag's user memory bank. |

### Understanding `offset` and `length`

> Unlike `accessOperations` where `offset` is in **16-bit words**, select `offset` is always in **bits**.

| Field | Unit | Example |
|---|---|---|
| `offset` | Bits | `offset: 32` starts matching from bit 32 of the EPC bank — skipping the first 2 words. For a GS1 EPC, bit 32 is the start of the company prefix portion. |
| `length` | Bits | `length: 96` matches 96 bits (the full EPC). `length: 24` matches only the first 24 bits — useful for matching a company prefix without caring about the item or serial number. |
| `tagPattern` | Hex string | `"E2800011"` — each hex character = 4 bits, so 8 hex chars = 32 bits matched. Must have an even number of characters, max 64 characters. |

### Choosing the `action` Field

The `action` field defines what happens to the SL flag and inventory state when a tag's memory matches (or does not match) the `tagPattern`.

| Action | On Match | On Mismatch |
|---|---|---|
| `INV_A_NOT_INV_B_OR_ASRT_SL_NOT_DSRT_SL` | Set to INV_A / Assert SL | Set to INV_B / Deassert SL |
| `INV_B_NOT_INV_A_OR_DSRT_SL_NOT_ASRT_SL` | Set to INV_B / Deassert SL | Set to INV_A / Assert SL |
| `INV_A_OR_ASRT_SL` | Set to INV_A / Assert SL | No change |
| `INV_B_OR_DSRT_SL` | Set to INV_B / Deassert SL | No change |
| `NOT_INV_B_OR_NOT_DSRT_SL` | No change | Set to INV_A / Assert SL |
| `NOT_INV_A_OR_NOT_ASRT_SL` | No change | Set to INV_B / Deassert SL |
| `INV_A2BB2A_NOT_INV_A_OR_NEG_SL_NOT_ASRT_SL` | Flip A↔B / Negate SL | Set to INV_A / Assert SL |
| `NOT_INV_A2BB2A_OR_NOT_NEG_SL` | No change | Flip A↔B / Negate SL |

## 8. Rules and Constraints

### Inventory State

- `set_operating_mode` cannot be sent while an RFID inventory is in progress. If inventory is running, stop it first — the command will be rejected with error code **11**.



### Access Operations

- `password` must be exactly **8 hex characters (32 bits)** for ACCESS, LOCK, and KILL operations.
- `data` for WRITE must be a hex string with an even number of characters and a length that is a multiple of 16-bit words.
- `lockMemBank` for LOCK additionally supports `ACCESS_PWD` and `KILL_PWD` beyond the standard EPC, TID, USER memory banks.

### Select / Prefilter

- A maximum of **32 select filters** are supported. Sending more than 32 entries returns error code **24**.
- `tagPattern` must be a hex string with an even number of characters, **maximum 64 characters**. Exceeding this returns error code **28**.
- `offset` in `select` is a **bit position**, not a word offset — unlike `accessOperations.offset` which is in 16-bit words.


