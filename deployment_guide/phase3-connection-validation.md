# Phase 3 — Connection Validation and Topic Architecture

> Part of the [Deployment Guide](./README.md)
> **Previous:** [Phase 2 — Device Bootstrap](./phase2-device-bootstrap.md)
> **Next:** [Phase 4 — First API Command](./phase4-first-command.md)

---

## Overview

This phase validates that the reader is connected and communicating, identifies the reader's serial number from live traffic, and establishes a clear understanding of the MQTT topic naming architecture used by the IoTC firmware.

**Estimated time:** 5–10 minutes

---

## Step 1 — Subscribe to the Wildcard Topic

Before the reader's serial number is known, use a wildcard subscription to capture all traffic from all readers.

1. In MQTTX, with your broker connection active, click **+ New Subscription**.
2. Enter the topic: `zebra/rfid/#`
3. Click **Confirm**.

Within seconds, you should see `heartBeatEVT` payloads appearing in the subscription feed — one every 30–60 seconds (configurable).

> **If no messages appear:**
> - Return to the Mosquitto console — is the reader shown as connected?
> - Check that the reader's configured Event Topic matches the prefix you're subscribed to.
> - Confirm the broker IP in the reader's MDM endpoint configuration is correct.

---

## Step 2 — Identify the Reader's Serial Number

Inspect the topic path of the first `heartBeatEVT` message that arrives. The topic format is:

```
zebra/rfid/{SERIAL_NUMBER}/evt/MGMT
```

**Example:**

```
zebra/rfid/21347120910084/evt/MGMT
```

In this example, `21347120910084` is the reader's serial number. Record this value — it is used in all subsequent topic construction.

You can also extract the serial number from the `heartBeatEVT` payload itself:

```json
{
  "event": "heartBeatEVT",
  "version": "1.0",
  "serial": "21347120910084",
  "hostname": "rfd40-reader-01",
  "battery": { "level": 87, "status": "discharging" },
  "temperature": { "celsius": 32.5 },
  "inventory": { "status": "idle" }
}
```

---

## Step 3 — MQTT Topic Architecture Reference

All IoTC topics follow a consistent hierarchical structure. Understanding this format is essential for sending commands and reading responses.

### Topic Format

```
zebra/rfid/{SERIAL_NUMBER}/{direction}/{ENDPOINT_TYPE}
```

| Segment | Description |
|---|---|
| `zebra/rfid` | Fixed root prefix for all IoTC traffic |
| `{SERIAL_NUMBER}` | The unique serial number of the physical reader |
| `{direction}` | `cmd` (command, inbound to reader), `rsp` (response, outbound from reader), `evt` (event/telemetry, outbound from reader) |
| `{ENDPOINT_TYPE}` | `MGMT`, `CTRL`, `DATA1`, `DATA2`, or other supported endpoint type |

### Full Topic Reference Table

Replace `{SN}` with your reader's serial number.

| Topic | Direction | Endpoint | Purpose |
|---|---|---|---|
| `zebra/rfid/{SN}/cmd/MGMT` | Inbound (Broker → Reader) | Management | Send administrative commands (`get_version`, `get_config`, `reboot`, etc.) |
| `zebra/rfid/{SN}/rsp/MGMT` | Outbound (Reader → Broker) | Management | Reader responses to management commands |
| `zebra/rfid/{SN}/evt/MGMT` | Outbound (Reader → Broker) | Management | Unsolicited telemetry: `heartBeatEVT`, alerts, errors |
| `zebra/rfid/{SN}/cmd/CTRL` | Inbound (Broker → Reader) | Control | RFID control commands (`control_operation`, `set_operating_mode`, etc.) |
| `zebra/rfid/{SN}/rsp/CTRL` | Outbound (Reader → Broker) | Control | Reader responses to control commands |
| `zebra/rfid/{SN}/evt/CTRL` | Outbound (Reader → Broker) | Control | Hardware trigger events (`triggerEVT`) |
| `zebra/rfid/{SN}/evt/DATA1` | Outbound (Reader → Broker) | Data 1 | High-speed RFID tag scan stream (`dataEVT`) |
| `zebra/rfid/{SN}/evt/DATA2` | Outbound (Reader → Broker) | Data 2 | Secondary RFID/barcode data stream |

### Publish vs. Subscribe Summary

| Role | What the broker/client does |
|---|---|
| **Publish** | `cmd/MGMT` — send management commands; `cmd/CTRL` — send RFID control commands |
| **Subscribe** | `rsp/MGMT` — read responses; `evt/MGMT` — read heartbeats and alerts; `rsp/CTRL` — read control responses; `evt/CTRL` — read trigger events; `evt/DATA1` — read tag scan stream |

### Last Will and Testament (LWT)

The reader configures an MQTT **Last Will and Testament (LWT)** message when it connects to the broker. If the reader disconnects unexpectedly (power loss, Wi-Fi drop, crash), the broker automatically publishes the LWT to the designated topic, alerting subscribed clients of the disconnection without requiring a polling mechanism.

The LWT is published to the Event topic of the Management endpoint:
```
zebra/rfid/{SN}/evt/MGMT
```

---

## Phase 3 Checklist

| Item | Status |
|---|---|
| Wildcard subscription active (`zebra/rfid/#`) | ☐ |
| `heartBeatEVT` messages received | ☐ |
| Reader serial number recorded | ☐ |
| Topic architecture understood | ☐ |

---

**Next:** Proceed to [Phase 4 — First API Command](./phase4-first-command.md) to send your first management command and validate the full request-response loop.
