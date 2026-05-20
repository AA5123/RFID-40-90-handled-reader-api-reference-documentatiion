# Phase 2 — Device Bootstrap via 123RFID Desktop

> Part of the [Deployment Guide](./README.md)
> **Previous:** [Phase 1 — Environment Setup](./phase1-environment-setup.md)
> **Next:** [Phase 3 — Connection Validation](./phase3-connection-validation.md)

---

## Overview

This phase connects the physical RFID reader to your Wi-Fi network and provisions the initial Management (MDM) endpoint using the **123RFID Desktop** Windows application. At the end of this phase, the reader will be actively connected to your Mosquitto broker and publishing heartbeat telemetry.

**Estimated time:** 10–20 minutes

**Requirement:** Windows PC with 123RFID Desktop installed (see [Prerequisites](./prerequisites.md)).

---

## Step 1 — Discover the Reader

123RFID Desktop discovers RFD40/RFD90 readers on the local network using mDNS (Multicast DNS). Both the PC and the reader must be on the **same subnet**.

1. Connect the RFD40/RFD90 sled to a paired Android device (USB-C or Bluetooth).
2. Power on the sled and ensure Wi-Fi is enabled on the Android device (if sharing connection via tethering, verify the reader is associated with the same Wi-Fi network as the PC).
3. Launch **123RFID Desktop** on the PC.
4. Click **Discover Devices** (or the equivalent scan button).

**Expected result:** The reader appears in the device list with its model name and current IP address.

> **If the reader does not appear:**
> - Confirm the PC and reader are on the same /24 subnet.
> - Disable Windows Firewall temporarily to rule out mDNS blocking.
> - Ensure the sled is powered on and the Android host has an active network connection.
> - Try restarting the 123RFID Desktop application.

5. Select the reader from the list to open its configuration panel.

---

## Step 2 — Configure Wi-Fi (if not already connected)

If the reader is not yet connected to the target Wi-Fi network, configure it through 123RFID Desktop before proceeding.

1. In the device configuration panel, navigate to **Wi-Fi Settings** (or **Network**).
2. Click **Add Wi-Fi Profile**.
3. Enter the Wi-Fi credentials:

| Field | Value |
|---|---|
| **SSID** | Your Wi-Fi network name |
| **Security Type** | WPA2-Personal (or your network's security type) |
| **Password** | Your Wi-Fi password |

4. Click **Apply** or **Save Profile**.
5. The reader will attempt to connect. Wait for the status to show **Connected** with an assigned IP address.

> **Note:** If the enterprise Wi-Fi uses certificate-based authentication (WPA2-Enterprise / EAP), install the Wi-Fi certificate first using the `install_certificate` command. Refer to the [API Reference Index](./api-reference-index.md) for the `install_certificate` and `set_wifi` commands.

---

## Step 3 — Configure the MDM Endpoint

The Management (MDM) endpoint is the primary connection between the reader and the MQTT broker. It is the only endpoint that can be provisioned via 123RFID Desktop; all other endpoints (CTRL, DATA) are configured via MQTT JSON commands after this step.

1. In the 123RFID Desktop device panel, navigate to **IoT Connector** or **MQTT Configuration**.
2. Locate the **Management Endpoint** section.
3. Configure the endpoint with the following values:

| Field | Value | Notes |
|---|---|---|
| **Endpoint Type** | `MGMT` | Management endpoint |
| **Host / Broker Address** | Your PC's Wi-Fi IP (e.g., `192.168.1.100`) | Must match the IP running Mosquitto |
| **Port** | `1883` | Unencrypted for lab use; use `8883` for TLS |
| **Client ID** | A unique string (e.g., `rfd40-reader-01`) | Must be unique per reader on the same broker |
| **Command Topic** | `zebra/rfid/{serial}/cmd` | Replace `{serial}` with the reader's serial number — or leave as-is if 123RFID Desktop populates it automatically |
| **Response Topic** | `zebra/rfid/{serial}/rsp` | The reader publishes its responses here |
| **Event Topic** | `zebra/rfid/{serial}/evt` | The reader publishes telemetry here |
| **Authentication** | None (for lab) | Configure username/password or certificate for production |
| **Keep Alive** | 60 seconds | Standard MQTT keep-alive interval |

4. Click **Apply** or **Save**.

> **Important:** If you do not know the reader's serial number at this point, you can use a wildcard approach. Leave the topic prefix as-is in 123RFID Desktop (it may auto-populate the serial), then use the wildcard subscription in Phase 3 to discover it from the first `heartBeatEVT` the reader publishes.

5. Click **Connect** (or the equivalent apply/commit action). 

**Expected result in Mosquitto console:**
```
New client connected from 192.168.1.xxx as rfd40-reader-01
```

**Expected result in MQTTX:** If you have a wildcard subscription active (e.g., `zebra/rfid/#`), the reader will begin publishing `heartBeatEVT` messages within a few seconds.

---

## Phase 2 Checklist

| Item | Status |
|---|---|
| Reader discovered in 123RFID Desktop | ☐ |
| Reader connected to target Wi-Fi network | ☐ |
| MDM endpoint configured with broker IP and topics | ☐ |
| Connection confirmed in Mosquitto console (client connected log) | ☐ |
| `heartBeatEVT` messages visible in MQTTX | ☐ |

---

**Next:** Proceed to [Phase 3 — Connection Validation](./phase3-connection-validation.md) to identify the reader's serial number and understand the full topic architecture.
