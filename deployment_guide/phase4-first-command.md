# Phase 4 — Sending the First API Command

> Part of the [Deployment Guide](./README.md)
> **Previous:** [Phase 3 — Connection Validation](./phase3-connection-validation.md)
> **Next:** [Phase 5 — Endpoint Configuration](./phase5-endpoint-configuration.md)

---

## Overview

This phase validates the complete command-response loop by sending `get_version` — the simplest read-only management command — to the reader and confirming a structured JSON response. This is the first integration test of the MQTT API.

**Estimated time:** 5 minutes

---

## Before You Begin

Confirm the following from the previous phases:

- Mosquitto is running on your PC.
- MQTTX is connected to the broker.
- The reader's serial number has been recorded (from Phase 3).
- The reader is publishing `heartBeatEVT` messages (confirming it is connected).

---

## Step 1 — Prepare the Target Topics

In MQTTX, set up two subscriptions before publishing the command so responses are captured:

1. **Subscribe to the response topic:**
   - Topic: `zebra/rfid/{SN}/rsp/MGMT`
   - Replace `{SN}` with your reader's serial number.

2. **Subscribe to the event topic** (already active from Phase 3):
   - Topic: `zebra/rfid/{SN}/evt/MGMT` (or the existing `zebra/rfid/#` wildcard)

---

## Step 2 — Execute `get_version`

The `get_version` command requests the current firmware version, hardware model, and IoTC application version from the reader.

1. In MQTTX, in the **Publish** section, set the **Topic** to:
   ```
   zebra/rfid/{SN}/cmd/MGMT
   ```
   Replace `{SN}` with your reader's serial number.

2. Set the **Payload** to:
   ```json
   {
     "command": "get_version"
   }
   ```

3. Set the **QoS** to `1` (At least once) — recommended for commands.

4. Click **Publish**.

---

## Step 3 — Confirm the Response

Within 1–3 seconds, the reader publishes a JSON response to:
```
zebra/rfid/{SN}/rsp/MGMT
```

### Example Response

```json
{
  "response": "get_version",
  "status": "success",
  "data": {
    "firmware": "NRGDWRFR0003120",
    "hardware": "RFD90",
    "application": "IoTC/2.2.3",
    "serial": "21347120910084"
  }
}
```

| Field | Description |
|---|---|
| `response` | Echoes the command name that generated this response |
| `status` | `success` or `error` |
| `data.firmware` | The reader's current firmware build string |
| `data.hardware` | The hardware model identifier |
| `data.application` | IoTC application version running on the reader |
| `data.serial` | The reader's serial number (confirms which device responded) |

---

## Troubleshooting

| Symptom | Likely Cause | Resolution |
|---|---|---|
| No response after 5 seconds | Wrong command topic | Verify the topic exactly matches `zebra/rfid/{SN}/cmd/MGMT` |
| No response after 5 seconds | Reader not connected | Check Mosquitto console for the reader's client ID |
| No response after 5 seconds | Response subscription missing | Confirm you subscribed to `rsp/MGMT` before publishing |
| `"status": "error"` in response | Malformed JSON payload | Validate JSON syntax — check for missing quotes, trailing commas |
| Error message references unknown command | Typo in `"command"` value | Verify: `"get_version"` (lowercase, underscore) |

---

## Phase 4 Checklist

| Item | Status |
|---|---|
| Response topic subscribed in MQTTX | ☐ |
| `get_version` command published to `cmd/MGMT` | ☐ |
| JSON response received on `rsp/MGMT` | ☐ |
| Response contains `"status": "success"` | ☐ |
| Firmware and hardware model recorded | ☐ |

---

**Next:** Proceed to [Phase 5 — Endpoint Configuration](./phase5-endpoint-configuration.md) to add the Control and Data endpoints via MQTT commands.
