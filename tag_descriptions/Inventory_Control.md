## Overview

Start and stop RFID tag reading operations on the device. During active inventory, the device continuously reads tags and publishes tag data events.

## Commands

| Command | Description |
|---|---|
| `control_operation` | Start or stop RFID inventory scanning operations |
| `start_inventory` | Initiate RFID tag reading based on current configuration |

## Behavior

While running, the device continuously reads RFID tags and publishes tag data events. Operating mode and post-filter settings affect read behavior.
