## 1. Description

`config_endpoint` manages the communication endpoints on the RFD40/RFD90 reader. An endpoint is a named connection profile that tells the reader how to reach an external system — specifying the protocol, broker URL, port, credentials, and MQTT topic mappings for that connection.

Before the reader can send or receive any data, at least one endpoint must be configured and set as active. This command is typically the first step when setting up a reader for the first time, and is used again whenever a connection needs to change — rotating credentials, switching broker environments, or removing a decommissioned connection.



## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Endpoint Configuration Management |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | RFD40 Series, RFD90 Series |
| Related Commands | [get_endpoint_config](#op-get-endpoint-config), [config_events](#op-config-events), [set_config](#op-set-config), [reboot](#op-reboot) |
| Required Request Fields | `command`, `requestId`, `epConfig` |
| Supported Operations | `add`, `update`, `delete` |
| Supported Endpoint Types | `MGMT`, `MGMT_EVT`, `CTRL`, `DATA1`, `DATA2`, `SOTI`, `MDM` |
| Supported Protocols | `MQTT`, `MQTT_TLS` |
| Supported Verification Types | `NONE`, `VERIFY_PEER`, `VERIFY_HOST`, `VERIFY_HOST_PEER` |
| Supported API Versions | V1.0, V1.1 |

## 3. Endpoint Provisioning Behavior

Understanding how endpoints are provisioned helps you know which endpoints to configure yourself and which are handled automatically by the system.

### Initial Provisioning — Management Endpoint

The initial management endpoint is provisioned by the 123RFID application — not through this command. The 123RFID application sets up the `MGMT` or `MDM` endpoint that gives the reader its first connection to the broker and enables device management communication.

> **Note:** You do not need to use `config_endpoint` to set up the initial management endpoint. That is handled by 123RFID during reader onboarding.

### Remote Provisioning — Operational Endpoints

Once the reader is connected to the broker and management communication is established, operational endpoints can be configured remotely using this command over MQTT. These endpoints are not provisioned by the 123RFID application.

Operational endpoints you configure using `config_endpoint`:

- `CTRL` — For controlling reader operations remotely.
- `DATA1` / `DATA2` — For streaming RFID tag read data to a backend system.

### Provisioning Flow Summary

| Endpoint Type | Role | Provisioned By | When |
|---|---|---|---|
| `MGMT` / `MDM` | Initial broker connectivity and device management | 123RFID application | During reader onboarding, before broker connection is established |
| `CTRL` | Remote operational control of the reader | `config_endpoint` command via MQTT | After broker connection is established |
| `DATA1` / `DATA2` | RFID tag data streaming to backend | `config_endpoint` command via MQTT | After broker connection is established |

> **Important:** `config_endpoint` can only be sent after the reader has an active management endpoint and is connected to the broker. If the management endpoint is not yet established, this command cannot reach the reader.

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

## 5. Before You Begin

Gather the following before sending the command. Missing any of these will cause the endpoint to fail to connect even if the command succeeds.

| What You Need | Details |
|---|---|
| Broker URL and port | The hostname or IP address of the MQTT broker, and the port it listens on. Port 1883 for standard MQTT, 8883 for MQTT over TLS. |
| Authentication credentials | Username and password for the broker. Never hardcode these — supply them from a secrets manager or environment variable at runtime. |
| MQTT topic names | The topics the reader will publish to (up to 3) and subscribe to (up to 1). Confirm these with your broker or platform configuration. |
| Endpoint type | The role this endpoint will play — management, control, data, or MDM. See the Choosing an Endpoint Type section above. |
| Protocol | The connection protocol — `MQTT` for standard connections or `MQTT_TLS` for encrypted connections. |
| Certificates (if using TLS) |  Install them using `install_certificate` before sending this command. |

## 6. Operations

The `operation` field inside `epConfig` determines the action performed on the endpoint definition.

- **add** — Creates a new endpoint on the device. The `endpointName` must not already exist. Returns error code 10 if a configuration with the same name already exists.
- **update** — Modifies an existing endpoint. The `endpointName` must already exist on the device.
- **delete** — Permanently removes an existing endpoint. Only `endpointName` and `epType` are required for this operation.

## 7. Rules and Constraints

Violating any of these rules will cause the command to fail or the endpoint to be configured incorrectly.

### Endpoint Name

- `endpointName` is required for all operations.
- Attempting to `add` an endpoint with a name that already exists returns error code 10. Use `update` to modify an existing endpoint, or delete it first.
- For `delete` and `update` operations, the endpoint must already exist on the device.

### Topics

- `publishTopics` supports a maximum of 3 entries per endpoint. Exceeding this returns error code 25.
- `subscribeTopics` supports a maximum of 1 entry per endpoint. Exceeding this returns error code 26.


### Certificates

- Certificate files referenced in `securityParams` (`caCertificateFile`, `clientCert`, `clientKey`) must already be installed on the device using `install_certificate` before this command is sent.
- Only `PEM` format is currently supported for `securityParams.format`.

### Activation

- `activate: true` marks the endpoint active immediately. `activate: false` saves the configuration without activating it.
- Only one endpoint of each type should be active at a time.
