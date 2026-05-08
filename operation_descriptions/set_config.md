The set_config command applies multiple configuration settings to the reader in a single request.

This command allows you to configure:
- Wi-Fi settings through wifiConfig
- Endpoint settings through epConfig
- Deferred application behavior through applyAfterReboot
- Combined network and endpoint updates in one transaction

Use this command to:
- Apply combined Wi-Fi and endpoint changes together
- Reduce multiple configuration round trips
- Control whether changes apply immediately or after reboot

### Command Details

| Property | Value |
|---|---|
| Pattern Name | Device Configuration Management |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | RFD40 Series, RFD90 Series |
| Related Commands | [get_config](#op-get-config), [set_wifi](#op-set-wifi), [config_endpoint](#op-config-endpoint), [config_events](#op-config-events) |
| Required Request Fields | command, requestId, configData |
| Supported Operations | CREATE and MODIFY Wi-Fi profiles; add, update, and delete endpoint configuration; apply after reboot option |
| Supported Types | Endpoint types: MGMT, MGMT_EVT, CTRL, DATA1, DATA2, SOTI, MDM; verification types: NONE, VERIFY_PEER, VERIFY_HOST, VERIFY_HOST_PEER |
| Supported Profiles | Wi-Fi access point profiles identified by ESSID with security configuration |
| Supported Protocols | MQTT, MQTT_WS, MQTT_WSS, MQTT_TLS, TCP, HTTP, HTTPS, WS, WSS, AWS, AZURE, HID |
| Supported API Versions | V1.0, V1.1 |
