## 1. Description

`config_endpoint` manages the communication endpoints on the RFD40/RFD90 reader. An endpoint is a named connection profile that tells the reader how to reach an external system — specifying the protocol, broker URL, port, credentials, and MQTT topic mappings for that connection.

Before the reader can send or receive any data, at least one endpoint must be configured and set as active. This command is typically the first step when setting up a reader for the first time, and is used again whenever a connection needs to change — rotating credentials, switching broker environments, or removing a decommissioned connection.

This command supports three operations:

- **add** — create a new endpoint on the reader
- **update** — modify settings on an existing endpoint
- **delete** — permanently remove an endpoint

> **Important:** The reader cannot communicate with any external system until at least one endpoint is configured and active. Always verify the response code after sending this command before expecting the reader to connect.

---

## 2. Endpoint Provisioning Behavior

Understanding how endpoints are provisioned helps you know which endpoints to configure yourself and which are handled automatically by the system.

### Initial Provisioning — Management Endpoint

The initial management endpoint is provisioned by the **123RFID application** — not through this command. The 123RFID application sets up the `MGMT` or `MDM` endpoint that gives the reader its first connection to the broker and enables device management communication.

> **Note:** You do not need to use `config_endpoint` to set up the initial management endpoint. That is handled by 123RFID during reader onboarding.

### Remote Provisioning — Operational Endpoints

Once the reader is connected to the broker and management communication is established, operational endpoints can be configured remotely using this command over MQTT. These endpoints are not provisioned by the 123RFID application.

Operational endpoints you configure using `config_endpoint`:

- `CTRL` — for controlling reader operations remotely
- `DATA1` / `DATA2` — for streaming RFID tag read data to a backend system

### Provisioning Flow Summary

| Endpoint Type | Role | Provisioned By | When |
|---|---|---|---|
| MGMT / MDM | Initial broker connectivity and device management | 123RFID application | During reader onboarding, before broker connection is established |
| CTRL | Remote operational control of the reader | `config_endpoint` via MQTT | After broker connection is established |
| DATA1 / DATA2 | RFID tag data streaming to backend | `config_endpoint` via MQTT | After broker connection is established |

> **Important:** `config_endpoint` can only be sent after the reader has an active management endpoint and is connected to the broker. If the management endpoint is not yet established, this command cannot reach the reader.

---

## 3. Before You Begin

Gather the following before sending the command. Missing any of these will cause the endpoint to fail to connect even if the command succeeds.

| What You Need | Details |
|---|---|
| Broker URL and port | The hostname or IP address of the MQTT broker. Port `1883` for standard MQTT, `8883` for MQTT over TLS. |
| Authentication credentials | Username and password for the broker. Never hardcode these — supply them from a secrets manager or environment variable at runtime. |
| MQTT topic names | The topics the reader will publish to (up to 3) and subscribe to (up to 1). Confirm these with your broker or platform configuration. |
| Endpoint type | The role this endpoint will play — management, control, data, or MDM. See Section 4 for guidance. |
| Protocol | MQTT for standard connections, `MQTT_TLS` for encrypted connections, or a cloud-specific protocol such as `AWS` or `AZURE`. |
| Certificates (if using TLS) | CA certificate, client certificate, and client private key files provisioned on the device. Required when `verificationType` is not `NONE`. |

---

## 4. Choosing an Endpoint Type

The `epType` field defines the role of the endpoint. A reader can have multiple endpoints with different types simultaneously — for example, one `MGMT` endpoint for commands and one `DATA1` endpoint for tag data. Choose based on what this connection will carry.

| epType | Role | Use This When |
|---|---|---|
| `MGMT` | Management | You need to send commands to the reader and receive responses — the primary control channel. |
| `MGMT_EVT` | Management events | You want the reader to push device events (connection status, firmware updates, alerts) to your system. |
| `CTRL` | Control | You need to control reader operations such as starting or stopping inventory, or changing operating modes. |
| `DATA1` / `DATA2` | Data | You want the reader to stream RFID tag read data to a backend system. Use `DATA2` for a secondary data destination. |
| `SOTI` | SOTI MDM | Your device management platform is SOTI MobiControl. |
| `MDM` | Generic MDM | Your device management platform is not covered by a dedicated type. |

---

## 5. Rules and Constraints

Violating any of these rules will cause the command to fail or the connection to behave unexpectedly.

### Endpoint Name

- `endpointName` must be unique on the reader. If it already exists, the command fails with error code `10`.
- For `update` and `delete`, `endpointName` and `epType` must exactly match the existing endpoint.

### Activation

- `activate: true` — the reader connects using this endpoint immediately after the operation.
- `activate: false` — the configuration is saved but the reader does not connect. Use this to pre-configure or temporarily disable an endpoint.
- Updating a URL or credentials on an active endpoint drops the current connection and reconnects with the new settings immediately.

### Topics

- `publishTopics` — maximum **3** per endpoint. Exceeding this returns error code `25`.
- `subscribeTopics` — maximum **1** per endpoint. Exceeding this returns error code `26`.
- Per-topic `qos` overrides `qosCommon` for that specific topic. Set `qosCommon` as your default and use per-topic `qos` only when a topic needs a different level.

### Tenant ID

- `tenantId` must not exceed **27 characters**. Error code `27` is returned if it does.

### MQTT Parameters

- `mqttParams` is required when `protocol` is `MQTT`, `MQTT_TLS`, `MQTT_WS`, or `MQTT_WSS`.
- `reconnectDelayMin` and `reconnectDelayMax` are in **milliseconds**, not seconds.

### Security Parameters

- `securityParams` is required when `verificationType` is `VERIFY_PEER`, `VERIFY_HOST`, or `VERIFY_HOST_PEER`.
- Certificate files must already be provisioned on the device before sending this command. This command references the file path — it does not upload the certificate.
- `format` — only `PEM` is currently supported.

### Credentials

> **Security Note:** Never hardcode credentials in your payload. Use placeholders and supply actual values from a secrets manager or environment variable at runtime.

### update Operation

- Always send the full configuration payload when updating — not just the fields being changed. Partial payloads may result in missing fields being reset to defaults.

