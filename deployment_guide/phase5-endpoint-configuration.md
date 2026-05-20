# Phase 5 — Configuring Control and Data Endpoints

> Part of the [Deployment Guide](./README.md)
> **Previous:** [Phase 4 — First API Command](./phase4-first-command.md)
> **Next:** [API Reference Index](./api-reference-index.md)

---

## Overview

The MDM endpoint (provisioned in Phase 2) handles management and administration. To send RFID operational commands and receive tag scan data, you must add dedicated **Control (CTRL)** and **Data (DATA1)** endpoints.

Endpoints are configured using the `config_endpoint` command, sent through the existing MDM endpoint. Changes take effect after a device reboot.

**Estimated time:** 10–20 minutes

---

## Endpoint Parameter Reference

All `config_endpoint` commands use the following parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `id` | string | Yes | A logical name for the endpoint (e.g., `ctrl-endpoint-01`). Used to reference the endpoint in update/delete operations. |
| `type` | string | Yes | Endpoint category. Supported values: `MGMT`, `MGMT_EVT`, `CTRL`, `DATA1`, `DATA2`, `SOTI`, `MDM`. |
| `host` | string | Yes | The MQTT broker hostname or IP address. |
| `port` | integer | Yes | MQTT broker port. `1883` for unencrypted; `8883` for TLS. |
| `clientId` | string | Yes | A unique MQTT client identifier for this endpoint connection. Must be unique per reader per broker. |
| `cmdTopic` | string | Conditional | The MQTT topic the reader subscribes to for inbound commands. Required for `CTRL` endpoints. |
| `rspTopic` | string | Conditional | The MQTT topic the reader publishes responses to. Required for `CTRL` endpoints. |
| `evtTopic` | string | Yes | The MQTT topic the reader publishes events/telemetry to. |
| `authType` | string | No | Authentication type. `NONE` (default), `BASIC`, `TOKEN`, or `CERTIFICATE`. |
| `username` | string | Conditional | Required if `authType` is `BASIC`. |
| `password` | string | Conditional | Required if `authType` is `BASIC`. |
| `keepAlive` | integer | No | MQTT keep-alive interval in seconds. Default: `60`. |
| `cleanSession` | boolean | No | Whether to start a clean MQTT session. Default: `true`. |
| `qos` | integer | No | Quality of Service level: `0`, `1`, or `2`. Default: `1`. |

---

## Step 1 — Add the Control (CTRL) Endpoint

The CTRL endpoint receives RFID operational commands and publishes responses and hardware trigger events.

### Publish to:
```
zebra/rfid/{SN}/cmd/MGMT
```

### Command Payload

```json
{
  "command": "config_endpoint",
  "data": {
    "operation": "add",
    "id": "ctrl-endpoint-01",
    "type": "CTRL",
    "host": "192.168.1.100",
    "port": 1883,
    "clientId": "rfd40-ctrl-01",
    "cmdTopic": "zebra/rfid/{SN}/cmd/CTRL",
    "rspTopic": "zebra/rfid/{SN}/rsp/CTRL",
    "evtTopic": "zebra/rfid/{SN}/evt/CTRL",
    "authType": "NONE",
    "keepAlive": 60,
    "cleanSession": true,
    "qos": 1
  }
}
```

Replace `{SN}` with your reader's serial number and `192.168.1.100` with your broker's IP.

### Expected Response (on `rsp/MGMT`)

```json
{
  "response": "config_endpoint",
  "status": "success",
  "data": {
    "id": "ctrl-endpoint-01",
    "operation": "add"
  }
}
```

> **Note:** The endpoint is saved to the device configuration but does **not** activate until the device reboots (Step 4).

---

## Step 2 — Add the Data (DATA1) Endpoint

The DATA1 endpoint is an outbound-only high-speed stream of RFID tag scan events (`dataEVT`). It does not require command or response topics.

### Command Payload

Publish to `zebra/rfid/{SN}/cmd/MGMT`:

```json
{
  "command": "config_endpoint",
  "data": {
    "operation": "add",
    "id": "data-endpoint-01",
    "type": "DATA1",
    "host": "192.168.1.100",
    "port": 1883,
    "clientId": "rfd40-data1-01",
    "evtTopic": "zebra/rfid/{SN}/evt/DATA1",
    "authType": "NONE",
    "keepAlive": 60,
    "cleanSession": true,
    "qos": 1
  }
}
```

### Expected Response

```json
{
  "response": "config_endpoint",
  "status": "success",
  "data": {
    "id": "data-endpoint-01",
    "operation": "add"
  }
}
```

---

## Step 3 — Verify Endpoint Configuration

Before rebooting, confirm that both endpoints were saved correctly using `get_endpoint_config`.

### Command Payload

Publish to `zebra/rfid/{SN}/cmd/MGMT`:

```json
{
  "command": "get_endpoint_config"
}
```

### Expected Response

The response returns a list of all configured endpoints. Verify that `ctrl-endpoint-01` and `data-endpoint-01` appear in the list with the correct `type`, `host`, and `port` values.

---

## Step 4 — Reboot to Activate Endpoints

Endpoint configuration changes do not take effect until the reader reboots. Use the `reboot` command to trigger a controlled restart.

> **Important:** All management endpoint configurations are restored after reboot. Only radio operation configurations from control endpoint operations are lost on reboot.

### Command Payload

Publish to `zebra/rfid/{SN}/cmd/MGMT`:

```json
{
  "command": "reboot"
}
```

The reader will disconnect from the broker, reboot, and reconnect within 30–60 seconds. Watch the Mosquitto console for the reconnection log entries.

**After reboot, the reader will establish three separate MQTT connections:**
1. The Management endpoint (existing)
2. The new Control endpoint
3. The new Data endpoint

---

## Step 5 — Validate Endpoint Activation

After the reader reconnects, validate that all three endpoints are active.

1. In the Mosquitto console, look for three distinct `client connected` log entries — one per endpoint client ID.

2. Subscribe to the CTRL event topic in MQTTX:
   - Topic: `zebra/rfid/{SN}/evt/CTRL`

3. Subscribe to the DATA1 event topic:
   - Topic: `zebra/rfid/{SN}/evt/DATA1`

4. Trigger the reader (press the physical scan trigger) to generate a `triggerEVT` on the CTRL event topic.

5. Start an inventory scan (via `control_operation`) and observe `dataEVT` payloads on the DATA1 event topic.

---

## Additional Management Commands

| Task | Command | Topic |
|---|---|---|
| List all configured endpoints | `get_endpoint_config` | `cmd/MGMT` |
| Update an existing endpoint | `config_endpoint` with `"operation": "update"` | `cmd/MGMT` |
| Remove an endpoint | `config_endpoint` with `"operation": "delete"` | `cmd/MGMT` |
| Add a second data stream (DATA2) | `config_endpoint` with `"type": "DATA2"` | `cmd/MGMT` |

See the full [API Reference Index](./api-reference-index.md) for complete parameter documentation on all endpoint management commands.

---

## Phase 5 Checklist

| Item | Status |
|---|---|
| CTRL endpoint added via `config_endpoint` | ☐ |
| DATA1 endpoint added via `config_endpoint` | ☐ |
| Endpoint list verified with `get_endpoint_config` | ☐ |
| Device rebooted with `reboot` command | ☐ |
| Three MQTT client connections visible in Mosquitto console | ☐ |
| `triggerEVT` received on CTRL event topic | ☐ |
| `dataEVT` received on DATA1 event topic after inventory scan | ☐ |

---

**Deployment Complete.** The reader is now fully configured with Management, Control, and Data endpoints. See the [API Reference Index](./api-reference-index.md) for the full command set available for RFID operations, device management, security, and telemetry.
