## Overview

Query the device's current state without changing any settings. These read-only commands provide health monitoring, device identification, and regulatory compliance information.

## Commands

| Command | Returns |
|---|---|
| [`get_status`](#get_status) | Real-time health — battery level, temperature, radio activity, power source, NTP sync, terminal connection |
| [`get_version`](#get_version) | Device identity — model, serial number, SKU, firmware versions (main, scanner, radio, IoTC) |
| [`get_current_region`](#get_current_region) | Radio regulation — country code, frequency channels, power limits, frequency hopping, LBT |

