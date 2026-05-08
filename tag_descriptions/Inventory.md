## Overview

Retrieve complete device inventory and tag reading capabilities information. Query device inventory status and supported features.

## Commands

| Command | Description |
|---|---|
| `start_inventory` | Initiate RFID tag inventory scanning operation |
| `get_status` | Query current inventory status and progress |

## Data

Inventory operations return:
- Tag count
- Scan count
- Operation status (IDLE, INPROGRESS, COMPLETED)
- Tagged data with EPC and metadata
