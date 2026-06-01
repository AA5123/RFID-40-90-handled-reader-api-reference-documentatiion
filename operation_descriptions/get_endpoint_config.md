## 1. Description

The `get_endpoint_config` command retrieves endpoint configuration details from the reader.

This command returns:

- Active endpoint configuration including protocol, connection, and topic settings
- MQTT parameters and security configuration for active endpoints
- Event routing configuration for active endpoints
- List of all saved endpoint names on the device

No additional payload fields are required for retrieving all active endpoints. To query a specific endpoint, include the optional `endpointDetails` object with the endpoint name.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Endpoint Configuration Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | RFD40 Series, RFD90 Series |
| Related Commands | [config_endpoint](config_endpoint.md) |
| Required Request Fields | command, requestId |
| Supported Operations | Retrieve active and saved endpoint configuration details |
| Supported Response Sections | endpointResponse, response |
| Supported API Versions | V1.0, V1.1 |

## 3. When to Use This Command

Use `get_endpoint_config` to:

- Verify active endpoint configuration before making changes
- Confirm MQTT topic assignments and QoS levels
- Audit security and event routing settings across endpoints
- Retrieve the list of all saved endpoints on the device

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `activate` | Is the endpoint active? | An inactive endpoint does not connect. Confirm before expecting data flow. |
| `protocol` | Is the correct protocol configured? | A protocol mismatch (e.g., MQTT vs MQTT_TLS) prevents broker connection. |
| `url` and `port` | Are the broker address and port correct? | Incorrect values prevent the reader from reaching the broker. |
| `verificationType` | Is TLS verification set correctly? | Mismatched verification type causes TLS handshake failures. |
| `publishTopics` | Are the correct topics configured? | The reader publishes data only to explicitly listed topics. |
| `subscribeTopics` | Is the command topic correct? | The reader only receives commands on subscribed topics. |
| `savedEndpoints.epNames` | What endpoints are saved on the device? | Lists all endpoint names available for activation or deletion. |

> **Note:** Use `get_endpoint_config` before calling `config_endpoint` to review existing configuration. This prevents overwriting active endpoint settings unexpectedly.
