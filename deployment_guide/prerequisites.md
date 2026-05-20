# Prerequisites

> Part of the [Deployment Guide](./README.md)

---

## Overview

Before starting deployment, confirm that all hardware, software, and network requirements listed in this section are met. Proceeding without meeting these requirements is the most common cause of connectivity failures and difficult-to-diagnose issues.

---

## 3.1 Hardware Requirements

| Component | Requirement | Notes |
|---|---|---|
| **RFID Reader** | Zebra RFD40 or RFD90 Handheld RFID Sled | Must run firmware version that supports IoTC |
| **Host Computer** | Windows PC (64-bit) | Required for 123RFID Desktop |
| **Mobile Device** | Android smartphone or tablet compatible with the RFD40/RFD90 | The sled attaches to the Android device via USB-C or Bluetooth |
| **Network Hardware** | Wi-Fi access point or router with DHCP | Both the PC and the reader must be on the same subnet for initial setup |

---

## 3.2 Software Requirements

| Software | Version | Purpose | Download |
|---|---|---|---|
| **123RFID Desktop** | Latest stable | Device discovery, Wi-Fi provisioning, MDM endpoint bootstrap | [zebra.com/123rfid](https://www.zebra.com/us/en/software/rfid-software/123rfid-desktop.html) |
| **Mosquitto MQTT Broker** | 2.x | MQTT broker (accepts connections from the reader) | [mosquitto.org](https://mosquitto.org/download/) |
| **MQTTX** | Latest stable | MQTT desktop client (subscribing to topics, publishing commands) | [mqttx.app](https://mqttx.app) |
| **RFD40/RFD90 Firmware** | IoTC-compatible build | Required on reader before 123RFID Desktop setup | Provided by Zebra |

---

## 3.3 Network Requirements

| Requirement | Value / Spec | Why It Matters |
|---|---|---|
| **Protocol** | MQTT over TCP (port 1883) — unencrypted for lab/development | Matches Mosquitto's default listener configuration |
| **Secure protocol** | MQTT over TLS (port 8883) — required for production | Reader supports certificate-based and username/password auth |
| **Subnet visibility** | PC and reader on same /24 subnet (e.g., `192.168.1.0/24`) | 123RFID Desktop uses mDNS-based discovery; cross-subnet discovery does not work |
| **Broker reachability** | PC running Mosquitto must be reachable from reader (no blocking firewall rules) | Reader initiates the outbound connection to the broker |
| **Firewall** | TCP port 1883 (or 8883) open inbound on the PC running Mosquitto | Windows Defender Firewall blocks new listeners by default |
| **DHCP** | Reader must receive a valid IP address on the Wi-Fi network | Static IP assignment is supported but requires manual configuration |

> **Tip:** For initial testing and validation, use an isolated Wi-Fi network (a standalone router or a mobile hotspot) with no enterprise firewall policies. This eliminates the most common sources of connectivity issues.
