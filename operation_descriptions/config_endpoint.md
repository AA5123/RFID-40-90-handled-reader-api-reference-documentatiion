The config_endpoint command configures or updates endpoint definitions used by the reader.

This command allows you to configure:
- Endpoint identity and type
- Protocol and connection parameters (URL, port, QoS, tenant)
- Activation status
- Protocol-specific settings such as keep-alive, reconnect behavior, and topic mapping

Use this command to:
- Add new endpoint configurations
- Update existing endpoint settings
- Delete endpoints that are no longer required
- Control which endpoint is active for communication

### Command Details

| Property | Value |
|---|---|
| Pattern Name | Endpoint Configuration Management |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | RFD40 Series, RFD90 Series |
| Related Commands | [get_endpoint_config](#op-get-endpoint-config), [config_events](#op-config-events), [set_config](#op-set-config), [reboot](#op-reboot) |
| Required Request Fields | command, requestId, epConfig |
| Supported Operations | add, update, delete |
| Supported Types | Endpoint types: MGMT, MGMT_EVT, CTRL, DATA1, DATA2, SOTI, MDM; verification types: NONE, VERIFY_PEER, VERIFY_HOST, VERIFY_HOST_PEER |
| Supported Profiles | Endpoint configuration profiles with protocol-specific connection and topic settings |
| Supported Protocols | MQTT, MQTT_WS, MQTT_WSS, MQTT_TLS, TCP, HTTP, HTTPS, WS, WSS, AWS, AZURE, HID |
| Supported API Versions | V1.0, V1.1 |
