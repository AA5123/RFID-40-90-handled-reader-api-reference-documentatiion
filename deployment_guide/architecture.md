# Architecture Overview

> Part of the [Deployment Guide](./README.md)

---

## Endpoint Types and Data Flow

The Zebra IoTC architecture defines three logical endpoint categories. Each category can be directed to a separate MQTT broker endpoint to segregate traffic, and each carries specific types of JSON payloads (Commands, Responses, and Events).

| # | Endpoint Type | Traffic Handled | Purpose |
|---|---|---|---|
| 1 | **Management (MDM)** | Commands, Responses, & Events | **IT Administration:** Device health, configuration, firmware updates, battery alerts, and keep-alive pulses (heartBeatEVT). |
| 2 | **Control (CTRL)** | Commands, Responses, & Events | **Hardware Triggers:** Actively driving the physical radio (start/stop inventory, change antenna power) and reporting hardware triggers (triggerEVT). |
| 3 | **Data (DATA1 / DATA2)** | Events only (Outbound) | **Telemetry Streams:** The pure, uninterrupted flow of scanned RFID tags (dataEVT) and barcode data to external databases. |

> **Note:** The IoTC firmware supports seven endpoint types in total: `MGMT`, `MGMT_EVT`, `CTRL`, `DATA1`, `DATA2`, `SOTI`, and `MDM`. This guide uses the three most common types for a standard deployment. See the API Reference for the full endpoint type list.

**Design Principle:** Operational RFID commands (start/stop inventory) must be sent to the **Control** endpoint, not the Management endpoint. The Management endpoint is reserved for IT/device-management functions. This separation ensures that RFID operations use the correct payload structures defined in the OpenAPI schema (`ctrlOprPayload` for `control_operation`, `operatingMode` for `set_operating_mode`, `postFilterPayload` for `set_post_filter`).

---

## The Management Endpoint (MDM)

The **Management (MDM)** endpoint acts as the primary IT administrative lifeline for the device. Rather than splitting traffic into separate network connections, the MDM endpoint utilizes distinct MQTT **Topics** to handle both two-way administrative operations and one-way health telemetry over a single network pipe.

### 1. Command & Response Traffic (The Administrative Loop)

For device management, the endpoint utilizes a request-response pattern. The broker publishes a command to the *Command Topic*, and the reader processes it and asynchronously publishes the answer to the *Response Topic*.

**Administrative commands include:**
`get_version`, `get_status`, `get_config`, `config_endpoint`, `set_config`, `get_endpoint_config`, `set_wifi`, `get_wifi`, `delete_wifi_profile`, `get_eth`, `get_current_region`, `set_os`, `config_events`, `install_certificate`, `get_installed_certificates`, `delete_certificate`, `reboot`

### 2. Event Telemetry (The Outbound Broadcast)

In addition to answering direct commands, the reader uses the MGMT endpoint to publish unsolicited, asynchronous telemetry to the *Event Topic*. These payloads notify the IT department of physical or software changes without requiring the server to ask for them.

- **Health events:** Periodic `heartBeatEVT` payloads detailing reader temperature, battery status, and inventory status.
- **Alerts:** Proactive notifications regarding low battery levels, file download progress, and network drops.
- **Errors and warnings:** Logs of operational anomalies.

### Configuration

The complete Management endpoint — including the definition of its specific Command, Response, and Event topics — is provisioned out-of-the-box via the **123RFID Desktop** application (see [Phase 2 — Device Bootstrap](./phase2-device-bootstrap.md)).

---

## The Control Endpoint (CTRL)

The **Control (CTRL)** endpoint is the operational command center for the physical RFID radio. It is designed to be utilized by local factory servers, edge computers, or automation scripts to directly drive the hardware and configure scanning logic in real-time.

Like the Management endpoint, the Control endpoint segregates its traffic using distinct MQTT Topics (Command, Response, and Event) over a single dedicated network connection.

### 1. Operational Commands (Inbound & Outbound Loop)

The Control endpoint accepts commands that actively modify the physical state of the antenna or its filtering logic.

- **Triggering:** Start and stop the RFID inventory process (`control_operation`).
- **Hardware Tuning:** Set transmit power, antenna selection, link profiles, and session parameters (`set_operating_mode`).
- **Filtering:** Define complex pre-filters (Select), post-filters, and access filters to isolate specific RFID tags in a crowded environment.
- **Memory Operations:** Execute advanced Read, Write, Lock, or Kill access operations on specific tag memory banks.
- **Profile Management:** Dynamically switch between predefined operating profiles based on environmental needs.

### 2. Hardware Events (Asynchronous Telemetry)

Beyond receiving commands, the Control endpoint publishes asynchronous hardware events to its dedicated Event topic.

- **Trigger Events (`triggerEVT`):** Instantly notifies the broker if a human operator squeezes or releases the physical trigger on the handheld sled, allowing remote software to react to physical user inputs.

---

## The Data Endpoint (DATA)

The **Data** endpoint is the high-bandwidth pipeline dedicated exclusively to streaming the massive volume of real-time RFID and barcode telemetry. To support complex enterprise architectures, the Zebra firmware supports multiplexing through two independent data endpoints: **DATA1** and **DATA2**.

The Data endpoint functions almost entirely as an asynchronous, high-speed outbound channel. Unlike the Management and Control endpoints, Data endpoints do not require subscribe topics — they only publish outbound telemetry.

### Payload Contents (dataEVT)

When the radio is active, the Data endpoint floods its designated event topic with structured JSON payloads containing:

| Field Group | Fields |
|---|---|
| RFID Tag Identifiers | Electronic Product Code (EPC), Tag Identifier (TID), User memory banks |
| Protocol Metadata | Protocol Control (PC) bits, Cyclic Redundancy Check (CRC), Extended PC (XPC) bits |
| RF Diagnostics | RSSI, RF phase angle, channel frequency |
| Temporal Data | First-seen and last-seen timestamps (milliseconds since epoch) |
| Session Metrics | Total `seenCount` for a specific tag since the last report interval |
| Operation Results | Success/failure outcomes of Read, Write, Lock, or Kill access operations |
| Barcode Telemetry | Decoded string values and symbology detected (e.g., `CODE_39`, `QR_CODE`) |
