## Overview

Manage the device's WiFi and Ethernet connections. The device supports both interfaces simultaneously for flexible networking.

## Commands

| Command | Description |
|---|---|
| `get_wifi` | Retrieve WiFi status including connected SSID, IP, signal strength, security type |
| `set_wifi` | Configure WiFi access point, security (WPA2/WPA3/Enterprise), and IP settings |
| `delete_wifi_profile` | Remove a saved WiFi profile by SSID |
| `get_eth` | Retrieve Ethernet status including link state, speed, IP address, security |

## Features

- WiFi profiles stored on device
- Automatic reconnection after reboot
- IPv4 DHCP addressing
- WPA2/WPA3 security support
