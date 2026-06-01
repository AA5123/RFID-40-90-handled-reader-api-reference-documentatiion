## 1. Description

`config_endpoint` configures the communication endpoints on the RFD40/RFD90 reader. Use this command to add, update, or delete endpoint connections — including setting the broker URL, port, protocol, credentials, and MQTT topics for each connection.

## 2. Command Details

|Property                    |Value                                                         |
|----------------------------|--------------------------------------------------------------|
|Pattern Name                |Endpoint Configuration Management                             |
|Communication Type          |Bidirectional (Cloud to Device, Device to Cloud)              |
|Applies To                  |RFD40 Series, RFD90 Series                                    |
|Related Commands            | [get_endpoint_config](get_endpoint_config.md), [config_events](config_events.md), [reboot](reboot.md) |
|Required Request Fields     |`command`, `requestId`, `epConfig`                            |
|Supported Operations        |`add`, `update`, `delete`                                     |
|Supported Endpoint Types    |`MGMT`, `MGMT_EVT`, `CTRL`, `DATA1`, `DATA2`, `SOTI`, `MDM`   |
|Supported Protocols         |`MQTT`, `MQTT_TLS`                                            |
|Supported Verification Types|`NONE`, `VERIFY_PEER`, `VERIFY_HOST`, `VERIFY_HOST_PEER`      |
|Supported API Versions      |V1.0, V1.1                                                    |

## 3. Endpoint Provisioning Behavior

Understanding how endpoints are provisioned helps you know which endpoints to configure yourself and which are handled by the 123RFID application.

### Initial Provisioning — MDM Endpoint

The MDM endpoint is the first endpoint that must exist on the reader. It is manually configured using the **123RFID application** during reader onboarding. This gives the reader its initial connection to the broker.

> **Note:** The MDM endpoint is the only endpoint configured through the 123RFID application. All other endpoints are configured through the broker using `config_endpoint` after the MDM endpoint is active.

### Remote Provisioning — All Other Endpoints

Once the reader is connected to the broker via the MDM endpoint, all other endpoints are configured remotely using `config_endpoint` over MQTT. This includes:

- `MGMT` — Dedicated management command and response channel
- `MGMT_EVT` — Dedicated management events channel
- `CTRL` — Remote operational control of the reader
- `DATA1` / `DATA2` — RFID tag data streaming to a backend system

Additional `MDM` endpoints can also be added through the broker using `config_endpoint` after the initial MDM endpoint is active.

> **Note:** The MDM endpoint handles both management and management events on a single connection. Separate `MGMT` and `MGMT_EVT` endpoints provide dedicated channels for these roles when finer control is needed. The active endpoint determines which connection profile the reader uses — whichever endpoint is marked `activate: true` handles communication for that role.

## 4. Choosing an Endpoint Type

The `epType` field defines the role of the endpoint. A reader can have multiple endpoints with different types simultaneously — for example, one `MGMT` endpoint for commands and one `DATA1` endpoint for tag data. Choose based on what this connection will carry.

|epType           |Role                          |Use This When                                                                                                                  |
|-----------------|------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
|`MGMT`           |Management                    |You need a dedicated channel to send commands to the reader and receive responses.                                             |
|`MGMT_EVT`       |Management events             |You want a dedicated channel for the reader to push device events (connection status, firmware updates, alerts) to your system.|
|`MDM`            |Management + Management events|Your device management platform requires a single endpoint that handles both management commands and device events.            |
|`CTRL`           |Control                       |You need to control reader operations such as starting or stopping inventory, or changing operating modes.                     |
|`DATA1` / `DATA2`|Data                          |You want the reader to stream RFID tag read data to a backend system. Use `DATA2` for a secondary data destination.            |
|`SOTI`           |SOTI MDM                      |Your device management platform is SOTI MobiControl.                                                                           |

## 5. Before You Begin

Gather the following before sending the command. Missing any of these will cause the endpoint to fail to connect even if the command succeeds.

|What You Need              |Details                                                                                                                                                                             |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|Broker URL and port        |The hostname or IP address of the MQTT broker, and the port it listens on. Port `1883` for standard MQTT, `8883` for MQTT over TLS.                                                 |
|Authentication credentials |Username and password for the broker. Never hardcode these — supply them from a secrets manager or environment variable at runtime.                                                 |
|MQTT topic names           |The middle segment of the topic path the reader will publish to (up to 3) and subscribe to (up to 1). The reader constructs the full topic at runtime — see MQTT Topic Format below.|
|Endpoint type              |The role this endpoint will play. See the Choosing an Endpoint Type section above.                                                                                                  |
|Protocol                   |`MQTT` for standard connections, `MQTT_TLS` for encrypted connections.                                                                                                              |
|Certificates (if using TLS)|CA certificate, client certificate, and client private key files must be installed on the device using `install_certificate` before sending this command.                           |

## 6. MQTT Topic Format

All topics on the RFD40/RFD90 follow a fixed three-part hierarchy. The reader constructs the full topic at runtime — you configure only the middle segment in the `topic` field.

**Format:**

```
<tenantId> / <topic> / <deviceSerialNumber>
```

**Example:**

If `tenantId` is `zebra`, `topic` is `MDM/clients/resp`, and the device serial is `RFD40-24190525100255`, the reader publishes to:

```
zebra/MDM/clients/resp/RFD40-24190525100255
```

> **Important:** Never include the `tenantId` or device serial number in the `topic` field. These are added automatically by the reader.

## 7. Operations

The `operation` field inside `epConfig` determines the action performed on the endpoint definition.

- **add** — Creates a new endpoint on the device. The `endpointName` must not already exist. Returns error code 10 if a configuration with the same name already exists.
- **update** — Modifies an existing endpoint. The `endpointName` must already exist on the device.
- **delete** — Permanently removes an existing endpoint. Only `endpointName` and `epType` are required for this operation.

## 8. Rules and Constraints

Violating any of these rules will cause the command to fail or the endpoint to be configured incorrectly.

### Endpoint Name

- `endpointName` is required for all operations.
- Attempting to `add` an endpoint with a name that already exists returns error code 10. Use `update` to modify an existing endpoint, or delete it first.
- For `delete` and `update` operations, the endpoint must already exist on the device.

### Topics

- `publishTopics` supports a maximum of 3 entries per endpoint. Exceeding this returns error code 25.
- `subscribeTopics` supports a maximum of 1 entry per endpoint. Exceeding this returns error code 26.
- Configure only the middle segment in the `topic` field. The reader prepends `tenantId` and appends the device serial number automatically at runtime.

### Certificates

- Certificate files referenced in `securityParams` (`caCertificateFile`, `clientCert`, `clientKey`) must already be installed on the device using `install_certificate` before this command is sent.

### Activation

- `activate: true` marks the endpoint active immediately after the command succeeds.
- `activate: false` saves the configuration on the device without activating it. The endpoint can be activated later using the `update` operation.
