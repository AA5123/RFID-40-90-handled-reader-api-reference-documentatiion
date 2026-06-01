## 1. Description

The `get_eth` command retrieves Ethernet interface configuration and connection state from the reader.

This command returns:

- Ethernet interface status and link state details
- DHCP enablement and IPv4 addressing information
- Interface-level network parameters and connectivity metadata
- Response metadata for command execution

No additional payload fields are required beyond `command` and `requestId`.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Ethernet Configuration Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | RFD40 Series, RFD90 Series |
| Related Commands | [get_wifi](get_wifi.md) |
| Required Request Fields | command, requestId |
| Supported Operations | Retrieve Ethernet network configuration and interface status |
| Supported Response Sections | ethConfig, response |
| Supported API Versions | V1.0, V1.1 |

## 3. When to Use This Command

Use `get_eth` to:

- Verify Ethernet connectivity and link speed
- Check interface status and network addressing
- Confirm DHCP-based IPv4 network configuration
- Troubleshoot wired network availability

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `interfaceDetails.status` | Is the Ethernet interface enabled? | If disabled, no wired network traffic is possible regardless of link state. |
| `linkStatus.status` | Is the physical link connected? | Confirms a cable is plugged in and the switch port is active. |
| `linkStatus.linkSpeed` | What speed is the link negotiated at? | Unexpected speeds (e.g., 10Mbps instead of 100Mbps) can indicate cable or switch issues. |
| `ipv4Configuration.ipAddress` | Has the device received an IP address? | No IP address means DHCP failed or static addressing is not configured. |
| `ipv4Configuration.enableDhcp` | Is DHCP enabled or static? | Determines whether the IP address is assigned automatically or must be configured manually. |
| `ipv4Configuration.gateway` | Is the gateway correct? | An incorrect gateway prevents the device from reaching external networks or the MQTT broker. |

> **Note:** When the Ethernet interface is disabled, the response only contains `interfaceName` and `status`. Fields such as `linkStatus` and `ipv4Configuration` are not present in the response.
