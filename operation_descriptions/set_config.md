## 1. Description

The `set_config` command applies multiple configuration settings to the reader in a single request.

This command allows you to configure:

- Wi-Fi settings through `wifiConfig`
- Endpoint settings through `epConfig`
- Deferred application behavior through `applyAfterReboot`
- Combined network and endpoint updates in one transaction

Use this command to:

- Apply combined Wi-Fi and endpoint changes together
- Reduce multiple configuration round trips
- Control whether changes apply immediately or after reboot

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Device Configuration Management |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | RFD40 Series, RFD90 Series |
| Related Commands | [set_wifi](set_wifi.md), [config_endpoint](config_endpoint.md), [config_events](config_events.md) |
| Required Request Fields | `command`, `requestId`, `configData` |
| Supported Operations | `CREATE` and `MODIFY` Wi-Fi profiles; `add`, `update`, and `delete` endpoint configuration; apply after reboot |
| Supported Endpoint Types | `MGMT`, `MGMT_EVT`, `CTRL`, `DATA1`, `DATA2`, `SOTI`, `MDM` |
| Supported Protocols | `MQTT`, `MQTT_TLS` |
| Supported Verification Types | `NONE`, `VERIFY_PEER`, `VERIFY_HOST`, `VERIFY_HOST_PEER` |
| Supported API Versions | V1.0, V1.1 |

## 3. Before You Begin

Decide which configuration areas you need to update before sending this command. `wifiConfig` and `epConfig` are independent — include only the sub-objects relevant to your use case.

| What You Need | Details |
|---|---|
| Wi-Fi operation | Decide whether you are creating (`CREATE`) or modifying (`MODIFY`) a Wi-Fi profile. Have the ESSID, security type, and credentials ready. |
| Endpoint operation | Decide whether you are adding (`add`), updating (`update`), or deleting (`delete`) an endpoint. Have the endpoint name, type, protocol, URL, port, QoS, and MQTT parameters ready. |
| Apply timing | Decide whether changes should take effect immediately or after the next reboot. Set `applyAfterReboot: true` to defer application. |
| Publish and subscribe topics | Endpoint configurations support up to 3 publish topics and 1 subscribe topic. Exceeding these limits returns error codes 25 and 26 respectively. |
| Tenant ID length | Ensure the `tenantId` value is within the allowed character length. An oversized value returns error code 27. |
| Existing configurations | Attempting to `add` an endpoint with a name that already exists returns error code 10. Use `update` to modify an existing endpoint, or delete it first. |

## 4. Rules and Constraints

Violating any of these rules will cause the command to fail or the configuration to be applied incorrectly.

### Wi-Fi Configuration

- `CREATE` fails with error code 18 if a profile with the same ESSID already exists. Delete the existing profile first or use `MODIFY` to update it.
- `MODIFY` fails with error code 15 if the ESSID does not exist. Use `CREATE` for new profiles.
- `essid` is required for both `CREATE` and `MODIFY` operations. A missing ESSID returns error code 17.

### Endpoint Configuration

- Attempting to `add` an endpoint with a name that already exists returns error code 10. Use a different name or delete the existing endpoint first.
- `publishTopics` supports a maximum of 3 entries per endpoint. Exceeding this limit returns error code 25.
- `subscribeTopics` supports a maximum of 1 entry per endpoint. Exceeding this limit returns error code 26.
- `tenantId` must be within the allowed character length. An oversized value returns error code 27.

### Apply Timing

- When `applyAfterReboot` is `true`, configuration changes are staged and do not take effect until the device is rebooted.
- When `applyAfterReboot` is `false` or omitted, changes are applied immediately.

### Security Note

- Never hardcode Wi-Fi passwords, MQTT credentials, or endpoint secrets in your payload. Use a secrets manager or environment variable to supply sensitive values at runtime.
