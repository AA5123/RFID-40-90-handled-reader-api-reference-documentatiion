# Zebra Handheld RFID IoT Connector (IoTC): End-to-End Deployment Guide

**Applicable Devices:** RFD40 / RFD90 Handheld RFID Sleds
**Document Version:** 2.2.3
**Last Updated:** May 2026

---

## About This Guide

This guide provides a step-by-step deployment walkthrough for the **Zebra IoT Connector (IoTC)** feature on the **RFD40** and **RFD90** handheld RFID sleds. It covers everything required to take a device from unboxing to fully configured MQTT endpoints, ready for RFID operations.

The IoT Connector enables efficient communication and device management through the MQTT protocol. It exposes a JSON-formatted interface that can be integrated with web applications deployed in the cloud or on-premises. Using MQTT topic-based routing, it cleanly separates management traffic from real-time RFID control and data telemetry.

> **Important:** The 123RFID Desktop application is a Windows-only utility. All instructions in this guide assume a Windows operating environment.

---

## What This Guide Covers

| Stage | Description |
|---|---|
| Environment Setup | Network baseline, MQTT broker installation, client configuration |
| Device Bootstrap | Reader discovery, Wi-Fi provisioning, and MDM endpoint creation via **123RFID Desktop** |
| Connection Validation | Topic architecture discovery and first API call |
| Endpoint Configuration | Dedicated Control and Data endpoints configured via **MQTT JSON commands** sent through the MDM endpoint |
| RFID Operations | Inventory start/stop, performance profiles, access operations, pre-filters, post-filters, tag metadata |
| Security | TLS certificates, secure MQTT (port 8883), credential management |

---

## Table of Contents

| # | Document | Description |
|---|---|---|
| 1 | [Architecture Overview](./architecture.md) | Endpoint types, data flow, MDM / CTRL / DATA endpoint roles |
| 2 | [Prerequisites](./prerequisites.md) | Hardware, software, and network requirements |
| 3 | [Phase 1 — Environment Setup](./phase1-environment-setup.md) | Subnet setup, broker install, MQTT client configuration |
| 4 | [Phase 2 — Device Bootstrap](./phase2-device-bootstrap.md) | 123RFID Desktop: Wi-Fi provisioning and MDM endpoint creation |
| 5 | [Phase 3 — Connection Validation](./phase3-connection-validation.md) | Topic architecture, serial number discovery, wildcard subscription |
| 6 | [Phase 4 — First API Command](./phase4-first-command.md) | Sending `get_version` to validate the MDM communication loop |
| 7 | [Phase 5 — Endpoint Configuration](./phase5-endpoint-configuration.md) | Adding Control and Data endpoints via MQTT JSON commands |
| 8 | [API Reference Index](./api-reference-index.md) | Links and task map to the full RFD40/RFD90 MQTT API Reference |

---

## Deployment Flow at a Glance

```
Unbox Reader
     │
     ▼
[Phase 1] Set up PC environment (broker + client)
     │
     ▼
[Phase 2] Connect reader via 123RFID Desktop
          → Provision Wi-Fi
          → Configure MDM endpoint
     │
     ▼
[Phase 3] Subscribe wildcard topic → capture serial number
     │
     ▼
[Phase 4] Send get_version → confirm MDM loop works
     │
     ▼
[Phase 5] Add CTRL and DATA endpoints via MQTT
          → Reboot to activate
     │
     ▼
Ready for RFID Operations (see API Reference)
```
