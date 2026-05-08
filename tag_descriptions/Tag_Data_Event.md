## Overview

Receive RFID tag data published by the device during an active inventory scan. Tag data streams continuously during operations.

## Events

| Event | Description |
|---|---|
| `dataEVT` | Tag data including EPC, RSSI, antenna, timestamp, TID, user memory, access results |

## Content

Each tag data event contains:
- Electronic Product Code (EPC)
- Signal strength (RSSI)
- Tag identification (TID)
- Optional memory bank data
- Access operation results
- Read metadata (antenna, frequency, phase)
