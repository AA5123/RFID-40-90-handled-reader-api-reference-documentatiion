# Phase 1 — Environment and Network Baseline

> Part of the [Deployment Guide](./README.md)
> **Next:** [Phase 2 — Device Bootstrap](./phase2-device-bootstrap.md)

---

## Overview

This phase prepares the host PC environment before the RFID reader is connected. By the end of this phase, you will have a running MQTT broker, a configured MQTT client, and a verified local network ready to accept connections from the reader.

**Estimated time:** 15–30 minutes

---

## Step 1 — Unify Your Subnet

Both the host PC and the RFID reader must be on the **same Wi-Fi subnet**. The 123RFID Desktop application uses mDNS-based device discovery, which only works within a single subnet.

1. Connect the PC to a Wi-Fi network (e.g., a standalone router or mobile hotspot).
2. Note the IP address assigned to the PC:
   - Open **Settings > Network & Internet > Wi-Fi > Hardware Properties**
   - Record the **IPv4 address** (e.g., `192.168.1.100`) — this becomes your broker address.
3. Ensure the Wi-Fi access point uses DHCP to assign addresses in the same /24 block.

> **Tip:** A dedicated portable router or mobile hotspot creates the most isolated and controllable lab environment, avoiding conflicts with enterprise firewalls.

---

## Step 2 — Determine Your Host IP Address

Before configuring the broker or the reader, record your PC's IP address on the Wi-Fi interface. This IP is required when:

- Configuring the MDM endpoint in 123RFID Desktop (Phase 2)
- Configuring CTRL and DATA endpoints via MQTT commands (Phase 5)

```powershell
# Run in PowerShell or Command Prompt to view Wi-Fi IP
ipconfig | findstr /i "IPv4"
```

Note the address listed under the Wi-Fi adapter (not Ethernet or virtual adapters).

---

## Step 3 — Install and Configure the Mosquitto MQTT Broker

The reader connects **outbound** to the broker. The broker must be running on the PC before the reader attempts its first connection.

### 3a. Install Mosquitto

1. Download the Mosquitto Windows installer from [mosquitto.org/download](https://mosquitto.org/download/).
2. Run the installer. Accept the default install location (`C:\Program Files\mosquitto\`).
3. When prompted, install the optional **service** to auto-start Mosquitto with Windows.

### 3b. Create a Minimal Broker Configuration

The default Mosquitto 2.x config is locked down and does not accept anonymous clients. For lab/development use, create a permissive config:

1. Open Notepad as Administrator.
2. Create a file at `C:\Program Files\mosquitto\mosquitto_lab.conf` with the following content:

```
# Mosquitto lab configuration — anonymous, unencrypted
listener 1883
allow_anonymous true
```

3. Save the file.

### 3c. Start the Broker

Open **Command Prompt as Administrator** and run:

```cmd
cd "C:\Program Files\mosquitto"
mosquitto -c mosquitto_lab.conf -v
```

The `-v` flag (verbose) prints each connection and published message to the console — essential for initial debugging.

> **Expected output:**
> ```
> mosquitto version 2.x.x starting
> Listening on port 1883
> ```

Leave this window open. Closing it stops the broker.

> **Production note:** For production deployments, replace anonymous access with username/password authentication or mTLS certificate authentication. See the `install_certificate` and `set_os` commands in the [API Reference](./api-reference-index.md).

---

## Step 4 — Install and Configure MQTTX

MQTTX is a cross-platform desktop MQTT client used to subscribe to topics (to observe traffic) and publish commands to the reader.

### 4a. Install MQTTX

1. Download MQTTX from [mqttx.app](https://mqttx.app).
2. Install and launch it.

### 4b. Create a Connection Profile

1. Click **+ New Connection**.
2. Configure the connection:

| Field | Value |
|---|---|
| **Name** | Local Lab Broker |
| **Host** | `mqtt://` + your PC's IP (e.g., `mqtt://192.168.1.100`) |
| **Port** | `1883` |
| **Client ID** | `mqttx-dev-client` (or any unique string) |
| **Username / Password** | Leave blank (anonymous) |

3. Click **Connect**. A green indicator confirms a successful connection.

---

## Step 5 — Verify Broker Connectivity (Self-Test)

Before connecting the reader, validate that the broker and client are functioning correctly with a loopback test.

1. In MQTTX, with the connection active, click **+ New Subscription**.
2. Enter the topic `test/#` and click **Confirm**.
3. In the **Publish** area, enter:
   - **Topic:** `test/hello`
   - **Payload:** `{"message": "broker is alive"}`
4. Click **Publish**.

**Expected result:** The message you just published appears in the subscription feed. If it does not appear, check:
- Mosquitto console — is it still running?
- Windows Firewall — is TCP port 1883 allowed inbound?
- Verify MQTTX is connecting to the correct IP address

Once the self-test passes, your environment is ready for [Phase 2 — Device Bootstrap](./phase2-device-bootstrap.md).

---

## Phase 1 Checklist

| Item | Status |
|---|---|
| PC and router on the same /24 subnet | ☐ |
| PC Wi-Fi IP address recorded | ☐ |
| Mosquitto installed and running on port 1883 | ☐ |
| MQTTX installed and connected to broker | ☐ |
| Loopback self-test passed | ☐ |
