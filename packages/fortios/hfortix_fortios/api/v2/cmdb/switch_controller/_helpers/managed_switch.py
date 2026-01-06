"""Validation helpers for switch_controller/managed_switch - Auto-generated"""

from typing import Any, TypedDict, NotRequired, Literal

# Import common validators from central _helpers module
from hfortix_fortios._helpers import (
    validate_enable_disable,
    validate_integer_range,
    validate_string_length,
    validate_port_number,
    validate_ip_address,
    validate_ipv6_address,
    validate_mac_address,
)

# ============================================================================
# Required Fields Validation
# Auto-generated from schema
# ============================================================================

# ⚠️  IMPORTANT: FortiOS schemas have known issues with required field marking:

# Do NOT use this list for strict validation - test with the actual FortiOS API!

# Fields marked as required (after filtering false positives)
REQUIRED_FIELDS = [
    "switch-id",  # Managed-switch name.
    "sn",  # Managed-switch serial number.
    "fsw-wan1-peer",  # FortiSwitch WAN1 peer port.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "switch-id": "",
    "sn": "",
    "description": "",
    "switch-profile": "default",
    "access-profile": "default",
    "purdue-level": "3",
    "fsw-wan1-peer": "",
    "fsw-wan1-admin": "discovered",
    "poe-pre-standard-detection": "disable",
    "dhcp-server-access-list": "global",
    "poe-detection-type": 0,
    "max-poe-budget": 0,
    "directly-connected": 0,
    "version": 0,
    "max-allowed-trunk-members": 0,
    "pre-provisioned": 0,
    "l3-discovered": 0,
    "mgmt-mode": 0,
    "tunnel-discovered": 0,
    "tdr-supported": "",
    "dynamic-capability": "0x00000000000000000000000000000000",
    "switch-device-tag": "",
    "switch-dhcp_opt43_key": "",
    "mclag-igmp-snooping-aware": "enable",
    "dynamically-discovered": 0,
    "ptp-status": "disable",
    "ptp-profile": "default",
    "radius-nas-ip-override": "disable",
    "radius-nas-ip": "0.0.0.0",
    "route-offload": "disable",
    "route-offload-mclag": "disable",
    "type": "physical",
    "owner-vdom": "",
    "flow-identity": "00000000",
    "staged-image-version": "",
    "delayed-restart-trigger": 0,
    "firmware-provision": "disable",
    "firmware-provision-version": "",
    "firmware-provision-latest": "disable",
    "override-snmp-sysinfo": "disable",
    "override-snmp-trap-threshold": "disable",
    "override-snmp-community": "disable",
    "override-snmp-user": "disable",
    "qos-drop-policy": "taildrop",
    "qos-red-probability": 12,
}

# ============================================================================
# Deprecated Fields
# Auto-generated from schema - warns users about deprecated fields
# ============================================================================

# Deprecated fields with migration guidance
DEPRECATED_FIELDS = {
}

# ============================================================================
# Field Metadata (Type Information & Descriptions)
# Auto-generated from schema - use for IDE autocomplete and documentation
# ============================================================================

# Field types mapping
FIELD_TYPES = {
    "switch-id": "string",  # Managed-switch name.
    "sn": "string",  # Managed-switch serial number.
    "description": "string",  # Description.
    "switch-profile": "string",  # FortiSwitch profile.
    "access-profile": "string",  # FortiSwitch access profile.
    "purdue-level": "option",  # Purdue Level of this FortiSwitch.
    "fsw-wan1-peer": "string",  # FortiSwitch WAN1 peer port.
    "fsw-wan1-admin": "option",  # FortiSwitch WAN1 admin status; enable to authorize the Forti
    "poe-pre-standard-detection": "option",  # Enable/disable PoE pre-standard detection.
    "dhcp-server-access-list": "option",  # DHCP snooping server access list.
    "poe-detection-type": "integer",  # PoE detection type for FortiSwitch.
    "max-poe-budget": "integer",  # Max PoE budget for FortiSwitch.
    "directly-connected": "integer",  # Directly connected FortiSwitch.
    "version": "integer",  # FortiSwitch version.
    "max-allowed-trunk-members": "integer",  # FortiSwitch maximum allowed trunk members.
    "pre-provisioned": "integer",  # Pre-provisioned managed switch.
    "l3-discovered": "integer",  # Layer 3 management discovered.
    "mgmt-mode": "integer",  # FortiLink management mode.
    "tunnel-discovered": "integer",  # SOCKS tunnel management discovered.
    "tdr-supported": "string",  # TDR supported.
    "dynamic-capability": "user",  # List of features this FortiSwitch supports (not configurable
    "switch-device-tag": "string",  # User definable label/tag.
    "switch-dhcp_opt43_key": "string",  # DHCP option43 key.
    "mclag-igmp-snooping-aware": "option",  # Enable/disable MCLAG IGMP-snooping awareness.
    "dynamically-discovered": "integer",  # Dynamically discovered FortiSwitch.
    "ptp-status": "option",  # Enable/disable PTP profile on this FortiSwitch.
    "ptp-profile": "string",  # PTP profile configuration.
    "radius-nas-ip-override": "option",  # Use locally defined NAS-IP.
    "radius-nas-ip": "ipv4-address",  # NAS-IP address.
    "route-offload": "option",  # Enable/disable route offload on this FortiSwitch.
    "route-offload-mclag": "option",  # Enable/disable route offload MCLAG on this FortiSwitch.
    "route-offload-router": "string",  # Configure route offload MCLAG IP address.
    "vlan": "string",  # Configure VLAN assignment priority.
    "type": "option",  # Indication of switch type, physical or virtual.
    "owner-vdom": "string",  # VDOM which owner of port belongs to.
    "flow-identity": "user",  # Flow-tracking netflow ipfix switch identity in hex format(00
    "staged-image-version": "string",  # Staged image version for FortiSwitch.
    "delayed-restart-trigger": "integer",  # Delayed restart triggered for this FortiSwitch.
    "firmware-provision": "option",  # Enable/disable provisioning of firmware to FortiSwitches on 
    "firmware-provision-version": "string",  # Firmware version to provision to this FortiSwitch on bootup 
    "firmware-provision-latest": "option",  # Enable/disable one-time automatic provisioning of the latest
    "ports": "string",  # Managed-switch port list.
    "ip-source-guard": "string",  # IP source guard.
    "stp-settings": "string",  # Configuration method to edit Spanning Tree Protocol (STP) se
    "stp-instance": "string",  # Configuration method to edit Spanning Tree Protocol (STP) in
    "override-snmp-sysinfo": "option",  # Enable/disable overriding the global SNMP system information
    "snmp-sysinfo": "string",  # Configuration method to edit Simple Network Management Proto
    "override-snmp-trap-threshold": "option",  # Enable/disable overriding the global SNMP trap threshold val
    "snmp-trap-threshold": "string",  # Configuration method to edit Simple Network Management Proto
    "override-snmp-community": "option",  # Enable/disable overriding the global SNMP communities.
    "snmp-community": "string",  # Configuration method to edit Simple Network Management Proto
    "override-snmp-user": "option",  # Enable/disable overriding the global SNMP users.
    "snmp-user": "string",  # Configuration method to edit Simple Network Management Proto
    "qos-drop-policy": "option",  # Set QoS drop-policy.
    "qos-red-probability": "integer",  # Set QoS RED/WRED drop probability.
    "switch-log": "string",  # Configuration method to edit FortiSwitch logging settings (l
    "remote-log": "string",  # Configure logging by FortiSwitch device to a remote syslog s
    "storm-control": "string",  # Configuration method to edit FortiSwitch storm control for m
    "mirror": "string",  # Configuration method to edit FortiSwitch packet mirror.
    "static-mac": "string",  # Configuration method to edit FortiSwitch Static and Sticky M
    "custom-command": "string",  # Configuration method to edit FortiSwitch commands to be push
    "dhcp-snooping-static-client": "string",  # Configure FortiSwitch DHCP snooping static clients.
    "igmp-snooping": "string",  # Configure FortiSwitch IGMP snooping global settings.
    "802-1X-settings": "string",  # Configuration method to edit FortiSwitch 802.1X global setti
    "router-vrf": "string",  # Configure VRF.
    "system-interface": "string",  # Configure system interface on FortiSwitch.
    "router-static": "string",  # Configure static routes.
    "system-dhcp-server": "string",  # Configure DHCP servers.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "switch-id": "Managed-switch name.",
    "sn": "Managed-switch serial number.",
    "description": "Description.",
    "switch-profile": "FortiSwitch profile.",
    "access-profile": "FortiSwitch access profile.",
    "purdue-level": "Purdue Level of this FortiSwitch.",
    "fsw-wan1-peer": "FortiSwitch WAN1 peer port.",
    "fsw-wan1-admin": "FortiSwitch WAN1 admin status; enable to authorize the FortiSwitch as a managed switch.",
    "poe-pre-standard-detection": "Enable/disable PoE pre-standard detection.",
    "dhcp-server-access-list": "DHCP snooping server access list.",
    "poe-detection-type": "PoE detection type for FortiSwitch.",
    "max-poe-budget": "Max PoE budget for FortiSwitch.",
    "directly-connected": "Directly connected FortiSwitch.",
    "version": "FortiSwitch version.",
    "max-allowed-trunk-members": "FortiSwitch maximum allowed trunk members.",
    "pre-provisioned": "Pre-provisioned managed switch.",
    "l3-discovered": "Layer 3 management discovered.",
    "mgmt-mode": "FortiLink management mode.",
    "tunnel-discovered": "SOCKS tunnel management discovered.",
    "tdr-supported": "TDR supported.",
    "dynamic-capability": "List of features this FortiSwitch supports (not configurable) that is sent to the FortiGate device for subsequent configuration initiated by the FortiGate device.",
    "switch-device-tag": "User definable label/tag.",
    "switch-dhcp_opt43_key": "DHCP option43 key.",
    "mclag-igmp-snooping-aware": "Enable/disable MCLAG IGMP-snooping awareness.",
    "dynamically-discovered": "Dynamically discovered FortiSwitch.",
    "ptp-status": "Enable/disable PTP profile on this FortiSwitch.",
    "ptp-profile": "PTP profile configuration.",
    "radius-nas-ip-override": "Use locally defined NAS-IP.",
    "radius-nas-ip": "NAS-IP address.",
    "route-offload": "Enable/disable route offload on this FortiSwitch.",
    "route-offload-mclag": "Enable/disable route offload MCLAG on this FortiSwitch.",
    "route-offload-router": "Configure route offload MCLAG IP address.",
    "vlan": "Configure VLAN assignment priority.",
    "type": "Indication of switch type, physical or virtual.",
    "owner-vdom": "VDOM which owner of port belongs to.",
    "flow-identity": "Flow-tracking netflow ipfix switch identity in hex format(00000000-FFFFFFFF default=0).",
    "staged-image-version": "Staged image version for FortiSwitch.",
    "delayed-restart-trigger": "Delayed restart triggered for this FortiSwitch.",
    "firmware-provision": "Enable/disable provisioning of firmware to FortiSwitches on join connection.",
    "firmware-provision-version": "Firmware version to provision to this FortiSwitch on bootup (major.minor.build, i.e. 6.2.1234).",
    "firmware-provision-latest": "Enable/disable one-time automatic provisioning of the latest firmware version.",
    "ports": "Managed-switch port list.",
    "ip-source-guard": "IP source guard.",
    "stp-settings": "Configuration method to edit Spanning Tree Protocol (STP) settings used to prevent bridge loops.",
    "stp-instance": "Configuration method to edit Spanning Tree Protocol (STP) instances.",
    "override-snmp-sysinfo": "Enable/disable overriding the global SNMP system information.",
    "snmp-sysinfo": "Configuration method to edit Simple Network Management Protocol (SNMP) system info.",
    "override-snmp-trap-threshold": "Enable/disable overriding the global SNMP trap threshold values.",
    "snmp-trap-threshold": "Configuration method to edit Simple Network Management Protocol (SNMP) trap threshold values.",
    "override-snmp-community": "Enable/disable overriding the global SNMP communities.",
    "snmp-community": "Configuration method to edit Simple Network Management Protocol (SNMP) communities.",
    "override-snmp-user": "Enable/disable overriding the global SNMP users.",
    "snmp-user": "Configuration method to edit Simple Network Management Protocol (SNMP) users.",
    "qos-drop-policy": "Set QoS drop-policy.",
    "qos-red-probability": "Set QoS RED/WRED drop probability.",
    "switch-log": "Configuration method to edit FortiSwitch logging settings (logs are transferred to and inserted into the FortiGate event log).",
    "remote-log": "Configure logging by FortiSwitch device to a remote syslog server.",
    "storm-control": "Configuration method to edit FortiSwitch storm control for measuring traffic activity using data rates to prevent traffic disruption.",
    "mirror": "Configuration method to edit FortiSwitch packet mirror.",
    "static-mac": "Configuration method to edit FortiSwitch Static and Sticky MAC.",
    "custom-command": "Configuration method to edit FortiSwitch commands to be pushed to this FortiSwitch device upon rebooting the FortiGate switch controller or the FortiSwitch.",
    "dhcp-snooping-static-client": "Configure FortiSwitch DHCP snooping static clients.",
    "igmp-snooping": "Configure FortiSwitch IGMP snooping global settings.",
    "802-1X-settings": "Configuration method to edit FortiSwitch 802.1X global settings.",
    "router-vrf": "Configure VRF.",
    "system-interface": "Configure system interface on FortiSwitch.",
    "router-static": "Configure static routes.",
    "system-dhcp-server": "Configure DHCP servers.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "switch-id": {"type": "string", "max_length": 35},
    "sn": {"type": "string", "max_length": 16},
    "description": {"type": "string", "max_length": 63},
    "switch-profile": {"type": "string", "max_length": 35},
    "access-profile": {"type": "string", "max_length": 31},
    "fsw-wan1-peer": {"type": "string", "max_length": 35},
    "poe-detection-type": {"type": "integer", "min": 0, "max": 255},
    "max-poe-budget": {"type": "integer", "min": 0, "max": 65535},
    "directly-connected": {"type": "integer", "min": 0, "max": 1},
    "version": {"type": "integer", "min": 0, "max": 255},
    "max-allowed-trunk-members": {"type": "integer", "min": 0, "max": 255},
    "pre-provisioned": {"type": "integer", "min": 0, "max": 255},
    "l3-discovered": {"type": "integer", "min": 0, "max": 1},
    "mgmt-mode": {"type": "integer", "min": 0, "max": 255},
    "tunnel-discovered": {"type": "integer", "min": 0, "max": 1},
    "tdr-supported": {"type": "string", "max_length": 31},
    "switch-device-tag": {"type": "string", "max_length": 32},
    "switch-dhcp_opt43_key": {"type": "string", "max_length": 63},
    "dynamically-discovered": {"type": "integer", "min": 0, "max": 1},
    "ptp-profile": {"type": "string", "max_length": 63},
    "owner-vdom": {"type": "string", "max_length": 31},
    "staged-image-version": {"type": "string", "max_length": 127},
    "delayed-restart-trigger": {"type": "integer", "min": 0, "max": 255},
    "firmware-provision-version": {"type": "string", "max_length": 35},
    "qos-red-probability": {"type": "integer", "min": 0, "max": 100},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "route-offload-router": {
        "vlan-name": {
            "type": "string",
            "help": "VLAN name.",
            "default": "",
            "max_length": 15,
        },
        "router-ip": {
            "type": "ipv4-address",
            "help": "Router IP address.",
            "required": True,
            "default": "0.0.0.0",
        },
    },
    "vlan": {
        "vlan-name": {
            "type": "string",
            "help": "VLAN name.",
            "default": "",
            "max_length": 15,
        },
        "assignment-priority": {
            "type": "integer",
            "help": "802.1x Radius (Tunnel-Private-Group-Id) VLANID assign-by-name priority. A smaller value has a higher priority.",
            "required": True,
            "default": 128,
            "min_value": 1,
            "max_value": 255,
        },
    },
    "ports": {
        "port-name": {
            "type": "string",
            "help": "Switch port name.",
            "required": True,
            "default": "",
            "max_length": 15,
        },
        "port-owner": {
            "type": "string",
            "help": "Switch port name.",
            "default": "",
            "max_length": 15,
        },
        "switch-id": {
            "type": "string",
            "help": "Switch id.",
            "default": "",
            "max_length": 35,
        },
        "speed": {
            "type": "option",
            "help": "Switch port speed; default and available settings depend on hardware.",
            "default": "auto",
            "options": [{"help": "10M half-duplex.", "label": "10Half", "name": "10half"}, {"help": "10M full-duplex.", "label": "10Full", "name": "10full"}, {"help": "100M half-duplex.", "label": "100Half", "name": "100half"}, {"help": "100M full-duplex.", "label": "100Full", "name": "100full"}, {"help": "1G full-duplex", "label": "1000Full", "name": "1000full"}, {"help": "10G full-duplex", "label": "10000Full", "name": "10000full"}, {"help": "Auto-negotiation.", "label": "Auto", "name": "auto"}, {"help": "Auto-negotiation (1G full-duplex only).", "label": "1000Auto", "name": "1000auto"}, {"help": "1G full-duplex (fiber SFPs only)", "label": "1000Full Fiber", "name": "1000full-fiber"}, {"help": "40G full-duplex", "label": "40000Full", "name": "40000full"}, {"help": "Auto Module.", "label": "Auto Module", "name": "auto-module"}, {"help": "100Mbps half-duplex.100Base-FX.", "label": "100Fx Half", "name": "100FX-half"}, {"help": "100Mbps full-duplex.100Base-FX.", "label": "100Fx Full", "name": "100FX-full"}, {"help": "100Gbps full-duplex.", "label": "100000Full", "name": "100000full"}, {"help": "Auto-Negotiation (2.5Gbps Only).", "label": "2500Auto", "name": "2500auto"}, {"help": "2.5Gbps full-duplex.", "label": "2500Full", "name": "2500full"}, {"help": "25Gbps full-duplex.", "label": "25000Full", "name": "25000full"}, {"help": "50Gbps full-duplex.", "label": "50000Full", "name": "50000full"}, {"help": "10Gbps copper interface.", "label": "10000Cr", "name": "10000cr"}, {"help": "10Gbps SFI interface.", "label": "10000Sr", "name": "10000sr"}, {"help": "100Gbps SFI interface.", "label": "100000Sr4", "name": "100000sr4"}, {"help": "100Gbps copper interface.", "label": "100000Cr4", "name": "100000cr4"}, {"help": "40Gbps SFI interface.", "label": "40000Sr4", "name": "40000sr4"}, {"help": "40Gbps copper interface.", "label": "40000Cr4", "name": "40000cr4"}, {"help": "Auto-Negotiation (40Gbps Only).", "label": "40000Auto", "name": "40000auto"}, {"help": "25Gbps copper interface.", "label": "25000Cr", "name": "25000cr"}, {"help": "25Gbps SFI interface.", "label": "25000Sr", "name": "25000sr"}, {"help": "50Gbps copper interface.", "label": "50000Cr", "name": "50000cr"}, {"help": "50Gbps SFI interface.", "label": "50000Sr", "name": "50000sr"}, {"help": "5Gbps full-duplex.", "label": "5000Auto", "name": "5000auto"}, {"help": "Auto-negotiation in SGMII mode.", "label": "Sgmii Auto", "name": "sgmii-auto"}],
        },
        "status": {
            "type": "option",
            "help": "Switch port admin status: up or down.",
            "default": "up",
            "options": [{"help": "Set admin status up.", "label": "Up", "name": "up"}, {"help": "Set admin status down.", "label": "Down", "name": "down"}],
        },
        "poe-status": {
            "type": "option",
            "help": "Enable/disable PoE status.",
            "default": "enable",
            "options": [{"help": "Enable PoE status.", "label": "Enable", "name": "enable"}, {"help": "Disable PoE status.", "label": "Disable", "name": "disable"}],
        },
        "ip-source-guard": {
            "type": "option",
            "help": "Enable/disable IP source guard.",
            "default": "disable",
            "options": [{"help": "Disable IP source guard.", "label": "Disable", "name": "disable"}, {"help": "Enable IP source guard.", "label": "Enable", "name": "enable"}],
        },
        "ptp-status": {
            "type": "option",
            "help": "Enable/disable PTP policy on this FortiSwitch port.",
            "default": "enable",
            "options": [{"help": "Disable PTP policy.", "label": "Disable", "name": "disable"}, {"help": "Enable PTP policy.", "label": "Enable", "name": "enable"}],
        },
        "ptp-policy": {
            "type": "string",
            "help": "PTP policy configuration.",
            "default": "default",
            "max_length": 63,
        },
        "aggregator-mode": {
            "type": "option",
            "help": "LACP member select mode.",
            "default": "bandwidth",
            "options": [{"help": "Member selection based on largest total bandwidth of links of similar speed.", "label": "Bandwidth", "name": "bandwidth"}, {"help": "Member selection based on largest count of similar link speed.", "label": "Count", "name": "count"}],
        },
        "flapguard": {
            "type": "option",
            "help": "Enable/disable flap guard.",
            "default": "disable",
            "options": [{"help": "Enable FlapGuard for this port.", "label": "Enable", "name": "enable"}, {"help": "Disable FlapGuard for this port.", "label": "Disable", "name": "disable"}],
        },
        "flap-rate": {
            "type": "integer",
            "help": "Number of stage change events needed within flap-duration.",
            "default": 5,
            "min_value": 1,
            "max_value": 30,
        },
        "flap-duration": {
            "type": "integer",
            "help": "Period over which flap events are calculated (seconds).",
            "default": 30,
            "min_value": 5,
            "max_value": 300,
        },
        "flap-timeout": {
            "type": "integer",
            "help": "Flap guard disabling protection (min).",
            "default": 0,
            "min_value": 0,
            "max_value": 120,
        },
        "rpvst-port": {
            "type": "option",
            "help": "Enable/disable inter-operability with rapid PVST on this interface.",
            "default": "disabled",
            "options": [{"help": "Disable inter-operability with rapid PVST on this interface.", "label": "Disabled", "name": "disabled"}, {"help": "Enable inter-operability with rapid PVST on this interface.", "label": "Enabled", "name": "enabled"}],
        },
        "poe-pre-standard-detection": {
            "type": "option",
            "help": "Enable/disable PoE pre-standard detection.",
            "default": "disable",
            "options": [{"help": "Enable PoE pre-standard detection.", "label": "Enable", "name": "enable"}, {"help": "Disable PoE pre-standard detection.", "label": "Disable", "name": "disable"}],
        },
        "port-number": {
            "type": "integer",
            "help": "Port number.",
            "default": 0,
            "min_value": 1,
            "max_value": 64,
        },
        "port-prefix-type": {
            "type": "integer",
            "help": "Port prefix type.",
            "default": 0,
            "min_value": 0,
            "max_value": 1,
        },
        "fortilink-port": {
            "type": "integer",
            "help": "FortiLink uplink port.",
            "default": 0,
            "min_value": 0,
            "max_value": 1,
        },
        "poe-capable": {
            "type": "integer",
            "help": "PoE capable.",
            "default": 0,
            "min_value": 0,
            "max_value": 1,
        },
        "pd-capable": {
            "type": "integer",
            "help": "Powered device capable.",
            "default": 0,
            "min_value": 0,
            "max_value": 1,
        },
        "stacking-port": {
            "type": "integer",
            "help": "Stacking port.",
            "default": 0,
            "min_value": 0,
            "max_value": 1,
        },
        "p2p-port": {
            "type": "integer",
            "help": "General peer to peer tunnel port.",
            "default": 0,
            "min_value": 0,
            "max_value": 1,
        },
        "mclag-icl-port": {
            "type": "integer",
            "help": "MCLAG-ICL port.",
            "default": 0,
            "min_value": 0,
            "max_value": 1,
        },
        "authenticated-port": {
            "type": "integer",
            "help": "Peer to Peer Authenticated port.",
            "default": 0,
            "min_value": 0,
            "max_value": 1,
        },
        "restricted-auth-port": {
            "type": "integer",
            "help": "Peer to Peer Restricted Authenticated port.",
            "default": 0,
            "min_value": 0,
            "max_value": 1,
        },
        "encrypted-port": {
            "type": "integer",
            "help": "Peer to Peer Encrypted port.",
            "default": 0,
            "min_value": 0,
            "max_value": 1,
        },
        "fiber-port": {
            "type": "integer",
            "help": "Fiber-port.",
            "default": 0,
            "min_value": 0,
            "max_value": 1,
        },
        "media-type": {
            "type": "string",
            "help": "Media type.",
            "default": "",
            "max_length": 31,
        },
        "poe-standard": {
            "type": "string",
            "help": "PoE standard supported.",
            "default": "",
            "max_length": 63,
        },
        "poe-max-power": {
            "type": "string",
            "help": "PoE maximum power.",
            "default": "",
            "max_length": 35,
        },
        "poe-mode-bt-cabable": {
            "type": "integer",
            "help": "PoE mode IEEE 802.3BT capable.",
            "default": 0,
            "min_value": 0,
            "max_value": 1,
        },
        "poe-port-mode": {
            "type": "option",
            "help": "Configure PoE port mode.",
            "default": "ieee802-3at",
            "options": [{"help": "IEEE802.3 AF.", "label": "Ieee802 3Af", "name": "ieee802-3af"}, {"help": "IEEE802.3 AT.", "label": "Ieee802 3At", "name": "ieee802-3at"}, {"help": "IEEE802.3 BT.", "label": "Ieee802 3Bt", "name": "ieee802-3bt"}],
        },
        "poe-port-priority": {
            "type": "option",
            "help": "Configure PoE port priority.",
            "default": "low-priority",
            "options": [{"help": "Critical Priority.", "label": "Critical Priority", "name": "critical-priority"}, {"help": "High Priority.", "label": "High Priority", "name": "high-priority"}, {"help": "Low Priority.", "label": "Low Priority", "name": "low-priority"}, {"help": "Medium Priority.", "label": "Medium Priority", "name": "medium-priority"}],
        },
        "poe-port-power": {
            "type": "option",
            "help": "Configure PoE port power.",
            "default": "normal",
            "options": [{"help": "Power not delivered during boot.", "label": "Normal", "name": "normal"}, {"help": "Power delivered during soft reboot.", "label": "Perpetual", "name": "perpetual"}, {"help": "Early power delivered during cold boot.", "label": "Perpetual Fast", "name": "perpetual-fast"}],
        },
        "flags": {
            "type": "integer",
            "help": "Port properties flags.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "isl-local-trunk-name": {
            "type": "string",
            "help": "ISL local trunk name.",
            "default": "",
            "max_length": 15,
        },
        "isl-peer-port-name": {
            "type": "string",
            "help": "ISL peer port name.",
            "default": "",
            "max_length": 15,
        },
        "isl-peer-device-name": {
            "type": "string",
            "help": "ISL peer device name.",
            "default": "",
            "max_length": 35,
        },
        "isl-peer-device-sn": {
            "type": "string",
            "help": "ISL peer device serial number.",
            "default": "",
            "max_length": 16,
        },
        "fgt-peer-port-name": {
            "type": "string",
            "help": "FGT peer port name.",
            "default": "",
            "max_length": 15,
        },
        "fgt-peer-device-name": {
            "type": "string",
            "help": "FGT peer device name.",
            "default": "",
            "max_length": 35,
        },
        "vlan": {
            "type": "string",
            "help": "Assign switch ports to a VLAN.",
            "default": "",
            "max_length": 15,
        },
        "allowed-vlans-all": {
            "type": "option",
            "help": "Enable/disable all defined vlans on this port.",
            "default": "disable",
            "options": [{"help": "Enable all defined VLANs on this port.", "label": "Enable", "name": "enable"}, {"help": "Disable all defined VLANs on this port.", "label": "Disable", "name": "disable"}],
        },
        "allowed-vlans": {
            "type": "string",
            "help": "Configure switch port tagged VLANs.",
        },
        "untagged-vlans": {
            "type": "string",
            "help": "Configure switch port untagged VLANs.",
        },
        "type": {
            "type": "option",
            "help": "Interface type: physical or trunk port.",
            "default": "physical",
            "options": [{"help": "Physical port.", "label": "Physical", "name": "physical"}, {"help": "Trunk port.", "label": "Trunk", "name": "trunk"}],
        },
        "access-mode": {
            "type": "option",
            "help": "Access mode of the port.",
            "default": "static",
            "options": [{"help": "Dynamic mode.", "label": "Dynamic", "name": "dynamic"}, {"help": "NAC mode.", "label": "Nac", "name": "nac"}, {"help": "Static mode.", "label": "Static", "name": "static"}],
        },
        "matched-dpp-policy": {
            "type": "string",
            "help": "Matched child policy in the dynamic port policy.",
            "default": "",
            "max_length": 63,
        },
        "matched-dpp-intf-tags": {
            "type": "string",
            "help": "Matched interface tags in the dynamic port policy.",
            "default": "",
            "max_length": 63,
        },
        "acl-group": {
            "type": "string",
            "help": "ACL groups on this port.",
        },
        "fortiswitch-acls": {
            "type": "string",
            "help": "ACLs on this port.",
        },
        "dhcp-snooping": {
            "type": "option",
            "help": "Trusted or untrusted DHCP-snooping interface.",
            "default": "untrusted",
            "options": [{"help": "Untrusted DHCP snooping interface.", "label": "Untrusted", "name": "untrusted"}, {"help": "Trusted DHCP snooping interface.", "label": "Trusted", "name": "trusted"}],
        },
        "dhcp-snoop-option82-trust": {
            "type": "option",
            "help": "Enable/disable allowance of DHCP with option-82 on untrusted interface.",
            "default": "disable",
            "options": [{"help": "Enable allowance of DHCP with option-82 on untrusted interface.", "label": "Enable", "name": "enable"}, {"help": "Disable allowance of DHCP with option-82 on untrusted interface.", "label": "Disable", "name": "disable"}],
        },
        "dhcp-snoop-option82-override": {
            "type": "string",
            "help": "Configure DHCP snooping option 82 override.",
        },
        "arp-inspection-trust": {
            "type": "option",
            "help": "Trusted or untrusted dynamic ARP inspection.",
            "default": "untrusted",
            "options": [{"help": "Untrusted dynamic ARP inspection.", "label": "Untrusted", "name": "untrusted"}, {"help": "Trusted dynamic ARP inspection.", "label": "Trusted", "name": "trusted"}],
        },
        "igmp-snooping-flood-reports": {
            "type": "option",
            "help": "Enable/disable flooding of IGMP reports to this interface when igmp-snooping enabled.",
            "default": "disable",
            "options": [{"help": "Enable flooding of IGMP snooping reports to this interface.", "label": "Enable", "name": "enable"}, {"help": "Disable flooding of IGMP snooping reports to this interface.", "label": "Disable", "name": "disable"}],
        },
        "mcast-snooping-flood-traffic": {
            "type": "option",
            "help": "Enable/disable flooding of IGMP snooping traffic to this interface.",
            "default": "disable",
            "options": [{"help": "Enable flooding of IGMP snooping traffic to this interface.", "label": "Enable", "name": "enable"}, {"help": "Disable flooding of IGMP snooping traffic to this interface.", "label": "Disable", "name": "disable"}],
        },
        "stp-state": {
            "type": "option",
            "help": "Enable/disable Spanning Tree Protocol (STP) on this interface.",
            "default": "enabled",
            "options": [{"help": "Enable STP on this interface.", "label": "Enabled", "name": "enabled"}, {"help": "Disable STP on this interface.", "label": "Disabled", "name": "disabled"}],
        },
        "stp-root-guard": {
            "type": "option",
            "help": "Enable/disable STP root guard on this interface.",
            "default": "disabled",
            "options": [{"help": "Enable STP root-guard on this interface.", "label": "Enabled", "name": "enabled"}, {"help": "Disable STP root-guard on this interface.", "label": "Disabled", "name": "disabled"}],
        },
        "stp-bpdu-guard": {
            "type": "option",
            "help": "Enable/disable STP BPDU guard on this interface.",
            "default": "disabled",
            "options": [{"help": "Enable STP BPDU guard on this interface.", "label": "Enabled", "name": "enabled"}, {"help": "Disable STP BPDU guard on this interface.", "label": "Disabled", "name": "disabled"}],
        },
        "stp-bpdu-guard-timeout": {
            "type": "integer",
            "help": "BPDU Guard disabling protection (0 - 120 min).",
            "default": 5,
            "min_value": 0,
            "max_value": 120,
        },
        "edge-port": {
            "type": "option",
            "help": "Enable/disable this interface as an edge port, bridging connections between workstations and/or computers.",
            "default": "enable",
            "options": [{"help": "Enable this interface as an edge port.", "label": "Enable", "name": "enable"}, {"help": "Disable this interface as an edge port.", "label": "Disable", "name": "disable"}],
        },
        "discard-mode": {
            "type": "option",
            "help": "Configure discard mode for port.",
            "default": "none",
            "options": [{"help": "Discard disabled.", "label": "None", "name": "none"}, {"help": "Discard all frames that are untagged.", "label": "All Untagged", "name": "all-untagged"}, {"help": "Discard all frames that are tagged.", "label": "All Tagged", "name": "all-tagged"}],
        },
        "packet-sampler": {
            "type": "option",
            "help": "Enable/disable packet sampling on this interface.",
            "default": "disabled",
            "options": [{"help": "Enable packet sampling on this interface.", "label": "Enabled", "name": "enabled"}, {"help": "Disable packet sampling on this interface.", "label": "Disabled", "name": "disabled"}],
        },
        "packet-sample-rate": {
            "type": "integer",
            "help": "Packet sampling rate (0 - 99999 p/sec).",
            "default": 512,
            "min_value": 0,
            "max_value": 99999,
        },
        "sflow-counter-interval": {
            "type": "integer",
            "help": "sFlow sampling counter polling interval in seconds (0 - 255).",
            "default": 0,
            "min_value": 0,
            "max_value": 255,
        },
        "sample-direction": {
            "type": "option",
            "help": "Packet sampling direction.",
            "default": "both",
            "options": [{"help": "Monitor transmitted traffic.", "label": "Tx", "name": "tx"}, {"help": "Monitor received traffic.", "label": "Rx", "name": "rx"}, {"help": "Monitor transmitted and received traffic.", "label": "Both", "name": "both"}],
        },
        "fec-capable": {
            "type": "integer",
            "help": "FEC capable.",
            "default": 0,
            "min_value": 0,
            "max_value": 1,
        },
        "fec-state": {
            "type": "option",
            "help": "State of forward error correction.",
            "default": "detect-by-module",
            "options": [{"help": "Disable forward error correction.", "label": "Disabled", "name": "disabled"}, {"help": "Enable Clause 74 FC-FEC, which only applies to 25Gbps.", "label": "Cl74", "name": "cl74"}, {"help": "Enable Clause 91 RS-FEC, which only applies to 100Gbps.", "label": "Cl91", "name": "cl91"}, {"help": "FEC supported by module.", "label": "Detect By Module", "name": "detect-by-module"}],
        },
        "flow-control": {
            "type": "option",
            "help": "Flow control direction.",
            "default": "disable",
            "options": [{"help": "Disable flow control.", "label": "Disable", "name": "disable"}, {"help": "Enable flow control for transmission pause control frames.", "label": "Tx", "name": "tx"}, {"help": "Enable flow control for receive pause control frames.", "label": "Rx", "name": "rx"}, {"help": "Enable flow control for both transmission and receive pause control frames.", "label": "Both", "name": "both"}],
        },
        "pause-meter": {
            "type": "integer",
            "help": "Configure ingress pause metering rate, in kbps (default = 0, disabled).",
            "default": 0,
            "min_value": 128,
            "max_value": 2147483647,
        },
        "pause-meter-resume": {
            "type": "option",
            "help": "Resume threshold for resuming traffic on ingress port.",
            "default": "50%",
            "options": [{"help": "Back pressure state won\u0027t be cleared until bucket count falls below 75% of pause threshold.", "label": "75%", "name": "75%"}, {"help": "Back pressure state won\u0027t be cleared until bucket count falls below 50% of pause threshold.", "label": "50%", "name": "50%"}, {"help": "Back pressure state won\u0027t be cleared until bucket count falls below 25% of pause threshold.", "label": "25%", "name": "25%"}],
        },
        "loop-guard": {
            "type": "option",
            "help": "Enable/disable loop-guard on this interface, an STP optimization used to prevent network loops.",
            "default": "disabled",
            "options": [{"help": "Enable loop-guard on this interface.", "label": "Enabled", "name": "enabled"}, {"help": "Disable loop-guard on this interface.", "label": "Disabled", "name": "disabled"}],
        },
        "loop-guard-timeout": {
            "type": "integer",
            "help": "Loop-guard timeout (0 - 120 min, default = 45).",
            "default": 45,
            "min_value": 0,
            "max_value": 120,
        },
        "port-policy": {
            "type": "string",
            "help": "Switch controller dynamic port policy from available options.",
            "default": "",
            "max_length": 63,
        },
        "qos-policy": {
            "type": "string",
            "help": "Switch controller QoS policy from available options.",
            "default": "default",
            "max_length": 63,
        },
        "storm-control-policy": {
            "type": "string",
            "help": "Switch controller storm control policy from available options.",
            "default": "default",
            "max_length": 63,
        },
        "port-security-policy": {
            "type": "string",
            "help": "Switch controller authentication policy to apply to this managed switch from available options.",
            "default": "",
            "max_length": 31,
        },
        "export-to-pool": {
            "type": "string",
            "help": "Switch controller export port to pool-list.",
            "default": "",
            "max_length": 35,
        },
        "interface-tags": {
            "type": "string",
            "help": "Tag(s) associated with the interface for various features including virtual port pool, dynamic port policy.",
        },
        "learning-limit": {
            "type": "integer",
            "help": "Limit the number of dynamic MAC addresses on this Port (1 - 128, 0 = no limit, default).",
            "default": 0,
            "min_value": 0,
            "max_value": 128,
        },
        "sticky-mac": {
            "type": "option",
            "help": "Enable or disable sticky-mac on the interface.",
            "default": "disable",
            "options": [{"help": "Enable sticky mac on the interface.", "label": "Enable", "name": "enable"}, {"help": "Disable sticky mac on the interface.", "label": "Disable", "name": "disable"}],
        },
        "lldp-status": {
            "type": "option",
            "help": "LLDP transmit and receive status.",
            "default": "tx-rx",
            "options": [{"help": "Disable LLDP TX and RX.", "label": "Disable", "name": "disable"}, {"help": "Enable LLDP as RX only.", "label": "Rx Only", "name": "rx-only"}, {"help": "Enable LLDP as TX only.", "label": "Tx Only", "name": "tx-only"}, {"help": "Enable LLDP TX and RX.", "label": "Tx Rx", "name": "tx-rx"}],
        },
        "lldp-profile": {
            "type": "string",
            "help": "LLDP port TLV profile.",
            "default": "default-auto-isl",
            "max_length": 63,
        },
        "export-to": {
            "type": "string",
            "help": "Export managed-switch port to a tenant VDOM.",
            "default": "",
            "max_length": 31,
        },
        "mac-addr": {
            "type": "mac-address",
            "help": "Port/Trunk MAC.",
            "default": "00:00:00:00:00:00",
        },
        "allow-arp-monitor": {
            "type": "option",
            "help": "Enable/Disable allow ARP monitor.",
            "default": "disable",
            "options": [{"help": "Disable allow ARP monitor.", "label": "Disable", "name": "disable"}, {"help": "Enable allow ARP monitor.", "label": "Enable", "name": "enable"}],
        },
        "qnq": {
            "type": "string",
            "help": "802.1AD VLANs in the VDom.",
            "default": "",
            "max_length": 15,
        },
        "log-mac-event": {
            "type": "option",
            "help": "Enable/disable logging for dynamic MAC address events.",
            "default": "disable",
            "options": [{"help": "Disable log MAC event for this interface.", "label": "Disable", "name": "disable"}, {"help": "Enable log MAC event for this interface.", "label": "Enable", "name": "enable"}],
        },
        "port-selection-criteria": {
            "type": "option",
            "help": "Algorithm for aggregate port selection.",
            "default": "src-dst-ip",
            "options": [{"help": "Source MAC address.", "label": "Src Mac", "name": "src-mac"}, {"help": "Destination MAC address.", "label": "Dst Mac", "name": "dst-mac"}, {"help": "Source and destination MAC address.", "label": "Src Dst Mac", "name": "src-dst-mac"}, {"help": "Source IP address.", "label": "Src Ip", "name": "src-ip"}, {"help": "Destination IP address.", "label": "Dst Ip", "name": "dst-ip"}, {"help": "Source and destination IP address.", "label": "Src Dst Ip", "name": "src-dst-ip"}],
        },
        "description": {
            "type": "string",
            "help": "Description for port.",
            "default": "",
            "max_length": 63,
        },
        "lacp-speed": {
            "type": "option",
            "help": "End Link Aggregation Control Protocol (LACP) messages every 30 seconds (slow) or every second (fast).",
            "default": "slow",
            "options": [{"help": "Send LACP message every 30 seconds.", "label": "Slow", "name": "slow"}, {"help": "Send LACP message every second.", "label": "Fast", "name": "fast"}],
        },
        "mode": {
            "type": "option",
            "help": "LACP mode: ignore and do not send control messages, or negotiate 802.3ad aggregation passively or actively.",
            "default": "static",
            "options": [{"help": "Static aggregation, do not send and ignore any control messages.", "label": "Static", "name": "static"}, {"help": "Passively use LACP to negotiate 802.3ad aggregation.", "label": "Lacp Passive", "name": "lacp-passive"}, {"help": "Actively use LACP to negotiate 802.3ad aggregation.", "label": "Lacp Active", "name": "lacp-active"}],
        },
        "bundle": {
            "type": "option",
            "help": "Enable/disable Link Aggregation Group (LAG) bundling for non-FortiLink interfaces.",
            "default": "disable",
            "options": [{"help": "Enable bundling.", "label": "Enable", "name": "enable"}, {"help": "Disable bundling.", "label": "Disable", "name": "disable"}],
        },
        "member-withdrawal-behavior": {
            "type": "option",
            "help": "Port behavior after it withdraws because of loss of control packets.",
            "default": "block",
            "options": [{"help": "Forward traffic.", "label": "Forward", "name": "forward"}, {"help": "Block traffic.", "label": "Block", "name": "block"}],
        },
        "mclag": {
            "type": "option",
            "help": "Enable/disable multi-chassis link aggregation (MCLAG).",
            "default": "disable",
            "options": [{"help": "Enable MCLAG.", "label": "Enable", "name": "enable"}, {"help": "Disable MCLAG.", "label": "Disable", "name": "disable"}],
        },
        "min-bundle": {
            "type": "integer",
            "help": "Minimum size of LAG bundle (1 - 24, default = 1).",
            "default": 1,
            "min_value": 1,
            "max_value": 24,
        },
        "max-bundle": {
            "type": "integer",
            "help": "Maximum size of LAG bundle (1 - 24, default = 24).",
            "default": 24,
            "min_value": 1,
            "max_value": 24,
        },
        "members": {
            "type": "string",
            "help": "Aggregated LAG bundle interfaces.",
        },
        "fallback-port": {
            "type": "string",
            "help": "LACP fallback port.",
            "default": "",
            "max_length": 79,
        },
    },
    "ip-source-guard": {
        "port": {
            "type": "string",
            "help": "Ingress interface to which source guard is bound.",
            "default": "",
            "max_length": 15,
        },
        "description": {
            "type": "string",
            "help": "Description.",
            "default": "",
            "max_length": 63,
        },
        "binding-entry": {
            "type": "string",
            "help": "IP and MAC address configuration.",
            "required": True,
        },
    },
    "stp-settings": {
        "local-override": {
            "type": "option",
            "help": "Enable to configure local STP settings that override global STP settings.",
            "default": "disable",
            "options": [{"help": "Override global STP settings.", "label": "Enable", "name": "enable"}, {"help": "Use global STP settings.", "label": "Disable", "name": "disable"}],
        },
        "name": {
            "type": "string",
            "help": "Name of local STP settings configuration.",
            "default": "",
            "max_length": 31,
        },
        "revision": {
            "type": "integer",
            "help": "STP revision number (0 - 65535).",
            "default": 0,
            "min_value": 0,
            "max_value": 65535,
        },
        "hello-time": {
            "type": "integer",
            "help": "Period of time between successive STP frame Bridge Protocol Data Units (BPDUs) sent on a port (1 - 10 sec, default = 2).",
            "default": 2,
            "min_value": 1,
            "max_value": 10,
        },
        "forward-time": {
            "type": "integer",
            "help": "Period of time a port is in listening and learning state (4 - 30 sec, default = 15).",
            "default": 15,
            "min_value": 4,
            "max_value": 30,
        },
        "max-age": {
            "type": "integer",
            "help": "Maximum time before a bridge port saves its configuration BPDU information (6 - 40 sec, default = 20).",
            "default": 20,
            "min_value": 6,
            "max_value": 40,
        },
        "max-hops": {
            "type": "integer",
            "help": "Maximum number of hops between the root bridge and the furthest bridge (1- 40, default = 20).",
            "default": 20,
            "min_value": 1,
            "max_value": 40,
        },
        "pending-timer": {
            "type": "integer",
            "help": "Pending time (1 - 15 sec, default = 4).",
            "default": 4,
            "min_value": 1,
            "max_value": 15,
        },
    },
    "stp-instance": {
        "id": {
            "type": "string",
            "help": "Instance ID.",
            "default": "",
            "max_length": 2,
        },
        "priority": {
            "type": "option",
            "help": "Priority.",
            "default": "32768",
            "options": [{"help": "0.", "label": "0", "name": "0"}, {"help": "4096.", "label": "4096", "name": "4096"}, {"help": "8192.", "label": "8192", "name": "8192"}, {"help": "12288.", "label": "12288", "name": "12288"}, {"help": "16384.", "label": "16384", "name": "16384"}, {"help": "20480.", "label": "20480", "name": "20480"}, {"help": "24576.", "label": "24576", "name": "24576"}, {"help": "28672.", "label": "28672", "name": "28672"}, {"help": "32768.", "label": "32768", "name": "32768"}, {"help": "36864.", "label": "36864", "name": "36864"}, {"help": "40960.", "label": "40960", "name": "40960"}, {"help": "45056.", "label": "45056", "name": "45056"}, {"help": "49152.", "label": "49152", "name": "49152"}, {"help": "53248.", "label": "53248", "name": "53248"}, {"help": "57344.", "label": "57344", "name": "57344"}, {"help": "61440.", "label": "61440", "name": "61440"}],
        },
    },
    "snmp-sysinfo": {
        "status": {
            "type": "option",
            "help": "Enable/disable SNMP.",
            "default": "disable",
            "options": [{"help": "Disable SNMP.", "label": "Disable", "name": "disable"}, {"help": "Enable SNMP.", "label": "Enable", "name": "enable"}],
        },
        "engine-id": {
            "type": "string",
            "help": "Local SNMP engine ID string (max 24 char).",
            "default": "",
            "max_length": 24,
        },
        "description": {
            "type": "string",
            "help": "System description.",
            "default": "",
            "max_length": 35,
        },
        "contact-info": {
            "type": "string",
            "help": "Contact information.",
            "default": "",
            "max_length": 35,
        },
        "location": {
            "type": "string",
            "help": "System location.",
            "default": "",
            "max_length": 35,
        },
    },
    "snmp-trap-threshold": {
        "trap-high-cpu-threshold": {
            "type": "integer",
            "help": "CPU usage when trap is sent.",
            "default": 80,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "trap-low-memory-threshold": {
            "type": "integer",
            "help": "Memory usage when trap is sent.",
            "default": 80,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "trap-log-full-threshold": {
            "type": "integer",
            "help": "Log disk usage when trap is sent.",
            "default": 90,
            "min_value": 0,
            "max_value": 4294967295,
        },
    },
    "snmp-community": {
        "id": {
            "type": "integer",
            "help": "SNMP community ID.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "name": {
            "type": "string",
            "help": "SNMP community name.",
            "required": True,
            "default": "",
            "max_length": 35,
        },
        "status": {
            "type": "option",
            "help": "Enable/disable this SNMP community.",
            "default": "enable",
            "options": [{"help": "Disable SNMP community.", "label": "Disable", "name": "disable"}, {"help": "Enable SNMP community.", "label": "Enable", "name": "enable"}],
        },
        "hosts": {
            "type": "string",
            "help": "Configure IPv4 SNMP managers (hosts).",
        },
        "query-v1-status": {
            "type": "option",
            "help": "Enable/disable SNMP v1 queries.",
            "default": "enable",
            "options": [{"help": "Disable SNMP v1 queries.", "label": "Disable", "name": "disable"}, {"help": "Enable SNMP v1 queries.", "label": "Enable", "name": "enable"}],
        },
        "query-v1-port": {
            "type": "integer",
            "help": "SNMP v1 query port (default = 161).",
            "default": 161,
            "min_value": 0,
            "max_value": 65535,
        },
        "query-v2c-status": {
            "type": "option",
            "help": "Enable/disable SNMP v2c queries.",
            "default": "enable",
            "options": [{"help": "Disable SNMP v2c queries.", "label": "Disable", "name": "disable"}, {"help": "Enable SNMP v2c queries.", "label": "Enable", "name": "enable"}],
        },
        "query-v2c-port": {
            "type": "integer",
            "help": "SNMP v2c query port (default = 161).",
            "default": 161,
            "min_value": 0,
            "max_value": 65535,
        },
        "trap-v1-status": {
            "type": "option",
            "help": "Enable/disable SNMP v1 traps.",
            "default": "enable",
            "options": [{"help": "Disable SNMP v1 traps.", "label": "Disable", "name": "disable"}, {"help": "Enable SNMP v1 traps.", "label": "Enable", "name": "enable"}],
        },
        "trap-v1-lport": {
            "type": "integer",
            "help": "SNMP v2c trap local port (default = 162).",
            "default": 162,
            "min_value": 0,
            "max_value": 65535,
        },
        "trap-v1-rport": {
            "type": "integer",
            "help": "SNMP v2c trap remote port (default = 162).",
            "default": 162,
            "min_value": 0,
            "max_value": 65535,
        },
        "trap-v2c-status": {
            "type": "option",
            "help": "Enable/disable SNMP v2c traps.",
            "default": "enable",
            "options": [{"help": "Disable SNMP v2c traps.", "label": "Disable", "name": "disable"}, {"help": "Enable SNMP v2c traps.", "label": "Enable", "name": "enable"}],
        },
        "trap-v2c-lport": {
            "type": "integer",
            "help": "SNMP v2c trap local port (default = 162).",
            "default": 162,
            "min_value": 0,
            "max_value": 65535,
        },
        "trap-v2c-rport": {
            "type": "integer",
            "help": "SNMP v2c trap remote port (default = 162).",
            "default": 162,
            "min_value": 0,
            "max_value": 65535,
        },
        "events": {
            "type": "option",
            "help": "SNMP notifications (traps) to send.",
            "default": "cpu-high mem-low log-full intf-ip ent-conf-change l2mac",
            "options": [{"help": "Send a trap when CPU usage too high.", "label": "Cpu High", "name": "cpu-high"}, {"help": "Send a trap when available memory is low.", "label": "Mem Low", "name": "mem-low"}, {"help": "Send a trap when log disk space becomes low.", "label": "Log Full", "name": "log-full"}, {"help": "Send a trap when an interface IP address is changed.", "label": "Intf Ip", "name": "intf-ip"}, {"help": "Send a trap when an entity MIB change occurs (RFC4133).", "label": "Ent Conf Change", "name": "ent-conf-change"}, {"help": "Send a trap for Learning event (add/delete/movefrom/moveto).", "label": "L2Mac", "name": "l2mac"}],
        },
    },
    "snmp-user": {
        "name": {
            "type": "string",
            "help": "SNMP user name.",
            "default": "",
            "max_length": 32,
        },
        "queries": {
            "type": "option",
            "help": "Enable/disable SNMP queries for this user.",
            "default": "enable",
            "options": [{"help": "Disable SNMP queries for this user.", "label": "Disable", "name": "disable"}, {"help": "Enable SNMP queries for this user.", "label": "Enable", "name": "enable"}],
        },
        "query-port": {
            "type": "integer",
            "help": "SNMPv3 query port (default = 161).",
            "default": 161,
            "min_value": 0,
            "max_value": 65535,
        },
        "security-level": {
            "type": "option",
            "help": "Security level for message authentication and encryption.",
            "default": "no-auth-no-priv",
            "options": [{"help": "Message with no authentication and no privacy (encryption).", "label": "No Auth No Priv", "name": "no-auth-no-priv"}, {"help": "Message with authentication but no privacy (encryption).", "label": "Auth No Priv", "name": "auth-no-priv"}, {"help": "Message with authentication and privacy (encryption).", "label": "Auth Priv", "name": "auth-priv"}],
        },
        "auth-proto": {
            "type": "option",
            "help": "Authentication protocol.",
            "default": "sha256",
            "options": [{"help": "HMAC-MD5-96 authentication protocol.", "label": "Md5", "name": "md5"}, {"help": "HMAC-SHA-1 authentication protocol.", "label": "Sha1", "name": "sha1"}, {"help": "HMAC-SHA-224 authentication protocol.", "label": "Sha224", "name": "sha224"}, {"help": "HMAC-SHA-256 authentication protocol.", "label": "Sha256", "name": "sha256"}, {"help": "HMAC-SHA-384 authentication protocol.", "label": "Sha384", "name": "sha384"}, {"help": "HMAC-SHA-512 authentication protocol.", "label": "Sha512", "name": "sha512"}],
        },
        "auth-pwd": {
            "type": "password",
            "help": "Password for authentication protocol.",
            "required": True,
            "max_length": 128,
        },
        "priv-proto": {
            "type": "option",
            "help": "Privacy (encryption) protocol.",
            "default": "aes128",
            "options": [{"help": "CFB128-AES-128 symmetric encryption protocol.", "label": "Aes128", "name": "aes128"}, {"help": "CFB128-AES-192 symmetric encryption protocol.", "label": "Aes192", "name": "aes192"}, {"help": "CFB128-AES-192-C symmetric encryption protocol.", "label": "Aes192C", "name": "aes192c"}, {"help": "CFB128-AES-256 symmetric encryption protocol.", "label": "Aes256", "name": "aes256"}, {"help": "CFB128-AES-256-C symmetric encryption protocol.", "label": "Aes256C", "name": "aes256c"}, {"help": "CBC-DES symmetric encryption protocol.", "label": "Des", "name": "des"}],
        },
        "priv-pwd": {
            "type": "password",
            "help": "Password for privacy (encryption) protocol.",
            "required": True,
            "max_length": 128,
        },
    },
    "switch-log": {
        "local-override": {
            "type": "option",
            "help": "Enable to configure local logging settings that override global logging settings.",
            "default": "disable",
            "options": [{"help": "Override global logging settings.", "label": "Enable", "name": "enable"}, {"help": "Use global logging settings.", "label": "Disable", "name": "disable"}],
        },
        "status": {
            "type": "option",
            "help": "Enable/disable adding FortiSwitch logs to the FortiGate event log.",
            "default": "enable",
            "options": [{"help": "Add FortiSwitch logs to the FortiGate event log.", "label": "Enable", "name": "enable"}, {"help": "Do not add FortiSwitch logs to the FortiGate event log.", "label": "Disable", "name": "disable"}],
        },
        "severity": {
            "type": "option",
            "help": "Severity of FortiSwitch logs that are added to the FortiGate event log.",
            "default": "notification",
            "options": [{"help": "Emergency level.", "label": "Emergency", "name": "emergency"}, {"help": "Alert level.", "label": "Alert", "name": "alert"}, {"help": "Critical level.", "label": "Critical", "name": "critical"}, {"help": "Error level.", "label": "Error", "name": "error"}, {"help": "Warning level.", "label": "Warning", "name": "warning"}, {"help": "Notification level.", "label": "Notification", "name": "notification"}, {"help": "Information level.", "label": "Information", "name": "information"}, {"help": "Debug level.", "label": "Debug", "name": "debug"}],
        },
    },
    "remote-log": {
        "name": {
            "type": "string",
            "help": "Remote log name.",
            "required": True,
            "default": "",
            "max_length": 35,
        },
        "status": {
            "type": "option",
            "help": "Enable/disable logging by FortiSwitch device to a remote syslog server.",
            "default": "disable",
            "options": [{"help": "Enable logging by FortiSwitch device to a remote syslog server.", "label": "Enable", "name": "enable"}, {"help": "Disable logging by FortiSwitch device to a remote syslog server.", "label": "Disable", "name": "disable"}],
        },
        "server": {
            "type": "string",
            "help": "IPv4 address of the remote syslog server.",
            "required": True,
            "default": "",
            "max_length": 63,
        },
        "port": {
            "type": "integer",
            "help": "Remote syslog server listening port.",
            "default": 514,
            "min_value": 0,
            "max_value": 65535,
        },
        "severity": {
            "type": "option",
            "help": "Severity of logs to be transferred to remote log server.",
            "default": "information",
            "options": [{"help": "Emergency level.", "label": "Emergency", "name": "emergency"}, {"help": "Alert level.", "label": "Alert", "name": "alert"}, {"help": "Critical level.", "label": "Critical", "name": "critical"}, {"help": "Error level.", "label": "Error", "name": "error"}, {"help": "Warning level.", "label": "Warning", "name": "warning"}, {"help": "Notification level.", "label": "Notification", "name": "notification"}, {"help": "Information level.", "label": "Information", "name": "information"}, {"help": "Debug level.", "label": "Debug", "name": "debug"}],
        },
        "csv": {
            "type": "option",
            "help": "Enable/disable comma-separated value (CSV) strings.",
            "default": "disable",
            "options": [{"help": "Enable comma-separated value (CSV) strings.", "label": "Enable", "name": "enable"}, {"help": "Disable comma-separated value (CSV) strings.", "label": "Disable", "name": "disable"}],
        },
        "facility": {
            "type": "option",
            "help": "Facility to log to remote syslog server.",
            "default": "local7",
            "options": [{"help": "Kernel messages.", "label": "Kernel", "name": "kernel"}, {"help": "Random user-level messages.", "label": "User", "name": "user"}, {"help": "Mail system.", "label": "Mail", "name": "mail"}, {"help": "System daemons.", "label": "Daemon", "name": "daemon"}, {"help": "Security/authorization messages.", "label": "Auth", "name": "auth"}, {"help": "Messages generated internally by syslogd.", "label": "Syslog", "name": "syslog"}, {"help": "Line printer subsystem.", "label": "Lpr", "name": "lpr"}, {"help": "Network news subsystem.", "label": "News", "name": "news"}, {"help": "UUCP server messages.", "label": "Uucp", "name": "uucp"}, {"help": "Clock daemon.", "label": "Cron", "name": "cron"}, {"help": "Security/authorization messages (private).", "label": "Authpriv", "name": "authpriv"}, {"help": "FTP daemon.", "label": "Ftp", "name": "ftp"}, {"help": "NTP daemon.", "label": "Ntp", "name": "ntp"}, {"help": "Log audit.", "label": "Audit", "name": "audit"}, {"help": "Log alert.", "label": "Alert", "name": "alert"}, {"help": "Clock daemon.", "label": "Clock", "name": "clock"}, {"help": "Reserved for local use.", "label": "Local0", "name": "local0"}, {"help": "Reserved for local use.", "label": "Local1", "name": "local1"}, {"help": "Reserved for local use.", "label": "Local2", "name": "local2"}, {"help": "Reserved for local use.", "label": "Local3", "name": "local3"}, {"help": "Reserved for local use.", "label": "Local4", "name": "local4"}, {"help": "Reserved for local use.", "label": "Local5", "name": "local5"}, {"help": "Reserved for local use.", "label": "Local6", "name": "local6"}, {"help": "Reserved for local use.", "label": "Local7", "name": "local7"}],
        },
    },
    "storm-control": {
        "local-override": {
            "type": "option",
            "help": "Enable to override global FortiSwitch storm control settings for this FortiSwitch.",
            "default": "disable",
            "options": [{"help": "Override global storm control settings.", "label": "Enable", "name": "enable"}, {"help": "Use global storm control settings.", "label": "Disable", "name": "disable"}],
        },
        "rate": {
            "type": "integer",
            "help": "Rate in packets per second at which storm control drops excess traffic(0-10000000, default=500, drop-all=0).",
            "default": 500,
            "min_value": 0,
            "max_value": 10000000,
        },
        "burst-size-level": {
            "type": "integer",
            "help": "Increase level to handle bursty traffic (0 - 4, default = 0).",
            "default": 0,
            "min_value": 0,
            "max_value": 4,
        },
        "unknown-unicast": {
            "type": "option",
            "help": "Enable/disable storm control to drop unknown unicast traffic.",
            "default": "disable",
            "options": [{"help": "Drop unknown unicast traffic.", "label": "Enable", "name": "enable"}, {"help": "Allow unknown unicast traffic.", "label": "Disable", "name": "disable"}],
        },
        "unknown-multicast": {
            "type": "option",
            "help": "Enable/disable storm control to drop unknown multicast traffic.",
            "default": "disable",
            "options": [{"help": "Drop unknown multicast traffic.", "label": "Enable", "name": "enable"}, {"help": "Allow unknown multicast traffic.", "label": "Disable", "name": "disable"}],
        },
        "broadcast": {
            "type": "option",
            "help": "Enable/disable storm control to drop broadcast traffic.",
            "default": "disable",
            "options": [{"help": "Drop broadcast traffic.", "label": "Enable", "name": "enable"}, {"help": "Allow broadcast traffic.", "label": "Disable", "name": "disable"}],
        },
    },
    "mirror": {
        "name": {
            "type": "string",
            "help": "Mirror name.",
            "default": "",
            "max_length": 63,
        },
        "status": {
            "type": "option",
            "help": "Active/inactive mirror configuration.",
            "default": "inactive",
            "options": [{"help": "Activate mirror configuration.", "label": "Active", "name": "active"}, {"help": "Deactivate mirror configuration.", "label": "Inactive", "name": "inactive"}],
        },
        "switching-packet": {
            "type": "option",
            "help": "Enable/disable switching functionality when mirroring.",
            "default": "disable",
            "options": [{"help": "Enable switching functionality when mirroring.", "label": "Enable", "name": "enable"}, {"help": "Disable switching functionality when mirroring.", "label": "Disable", "name": "disable"}],
        },
        "dst": {
            "type": "string",
            "help": "Destination port.",
            "default": "",
            "max_length": 63,
        },
        "src-ingress": {
            "type": "string",
            "help": "Source ingress interfaces.",
        },
        "src-egress": {
            "type": "string",
            "help": "Source egress interfaces.",
        },
    },
    "static-mac": {
        "id": {
            "type": "integer",
            "help": "ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "type": {
            "type": "option",
            "help": "Type.",
            "default": "static",
            "options": [{"help": "Static MAC.", "label": "Static", "name": "static"}, {"help": "Sticky MAC.", "label": "Sticky", "name": "sticky"}],
        },
        "vlan": {
            "type": "string",
            "help": "Vlan.",
            "default": "",
            "max_length": 15,
        },
        "mac": {
            "type": "mac-address",
            "help": "MAC address.",
            "default": "00:00:00:00:00:00",
        },
        "interface": {
            "type": "string",
            "help": "Interface name.",
            "default": "",
            "max_length": 35,
        },
        "description": {
            "type": "string",
            "help": "Description.",
            "default": "",
            "max_length": 63,
        },
    },
    "custom-command": {
        "command-entry": {
            "type": "string",
            "help": "List of FortiSwitch commands.",
            "default": "",
            "max_length": 35,
        },
        "command-name": {
            "type": "string",
            "help": "Names of commands to be pushed to this FortiSwitch device, as configured under config switch-controller custom-command.",
            "required": True,
            "default": "",
            "max_length": 35,
        },
    },
    "dhcp-snooping-static-client": {
        "name": {
            "type": "string",
            "help": "Client name.",
            "default": "",
            "max_length": 35,
        },
        "vlan": {
            "type": "string",
            "help": "VLAN name.",
            "required": True,
            "default": "",
            "max_length": 15,
        },
        "ip": {
            "type": "ipv4-address",
            "help": "Client static IP address.",
            "required": True,
            "default": "0.0.0.0",
        },
        "mac": {
            "type": "mac-address",
            "help": "Client MAC address.",
            "required": True,
            "default": "00:00:00:00:00:00",
        },
        "port": {
            "type": "string",
            "help": "Interface name.",
            "required": True,
            "default": "",
            "max_length": 15,
        },
    },
    "igmp-snooping": {
        "local-override": {
            "type": "option",
            "help": "Enable/disable overriding the global IGMP snooping configuration.",
            "default": "disable",
            "options": [{"help": "Override the global IGMP snooping configuration.", "label": "Enable", "name": "enable"}, {"help": "Use the global IGMP snooping configuration.", "label": "Disable", "name": "disable"}],
        },
        "aging-time": {
            "type": "integer",
            "help": "Maximum time to retain a multicast snooping entry for which no packets have been seen (15 - 3600 sec, default = 300).",
            "default": 300,
            "min_value": 15,
            "max_value": 3600,
        },
        "flood-unknown-multicast": {
            "type": "option",
            "help": "Enable/disable unknown multicast flooding.",
            "default": "disable",
            "options": [{"help": "Enable unknown multicast flooding.", "label": "Enable", "name": "enable"}, {"help": "Disable unknown multicast flooding.", "label": "Disable", "name": "disable"}],
        },
        "vlans": {
            "type": "string",
            "help": "Configure IGMP snooping VLAN.",
        },
    },
    "802-1X-settings": {
        "local-override": {
            "type": "option",
            "help": "Enable to override global 802.1X settings on individual FortiSwitches.",
            "default": "disable",
            "options": [{"help": "Override global 802.1X settings.", "label": "Enable", "name": "enable"}, {"help": "Use global 802.1X settings.", "label": "Disable", "name": "disable"}],
        },
        "link-down-auth": {
            "type": "option",
            "help": "Authentication state to set if a link is down.",
            "default": "set-unauth",
            "options": [{"help": "Interface set to unauth when down. Reauthentication is needed.", "label": "Set Unauth", "name": "set-unauth"}, {"help": "Interface reauthentication is not needed.", "label": "No Action", "name": "no-action"}],
        },
        "reauth-period": {
            "type": "integer",
            "help": "Reauthentication time interval (1 - 1440 min, default = 60, 0 = disable).",
            "default": 60,
            "min_value": 0,
            "max_value": 1440,
        },
        "max-reauth-attempt": {
            "type": "integer",
            "help": "Maximum number of authentication attempts (0 - 15, default = 3).",
            "default": 3,
            "min_value": 0,
            "max_value": 15,
        },
        "tx-period": {
            "type": "integer",
            "help": "802.1X Tx period (seconds, default=30).",
            "default": 30,
            "min_value": 12,
            "max_value": 60,
        },
        "mab-reauth": {
            "type": "option",
            "help": "Enable or disable MAB reauthentication settings.",
            "default": "disable",
            "options": [{"help": "Disable MAB re-authentication setttings.", "label": "Disable", "name": "disable"}, {"help": "Enable MAB re-authentication setttings.", "label": "Enable", "name": "enable"}],
        },
        "mac-username-delimiter": {
            "type": "option",
            "help": "MAC authentication username delimiter (default = hyphen).",
            "default": "hyphen",
            "options": [{"help": "Use colon as delimiter for MAC auth username.", "label": "Colon", "name": "colon"}, {"help": "Use hyphen as delimiter for MAC auth username.", "label": "Hyphen", "name": "hyphen"}, {"help": "No delimiter for MAC auth username.", "label": "None", "name": "none"}, {"help": "Use single hyphen as delimiter for MAC auth username.", "label": "Single Hyphen", "name": "single-hyphen"}],
        },
        "mac-password-delimiter": {
            "type": "option",
            "help": "MAC authentication password delimiter (default = hyphen).",
            "default": "hyphen",
            "options": [{"help": "Use colon as delimiter for MAC auth password.", "label": "Colon", "name": "colon"}, {"help": "Use hyphen as delimiter for MAC auth password.", "label": "Hyphen", "name": "hyphen"}, {"help": "No delimiter for MAC auth password.", "label": "None", "name": "none"}, {"help": "Use single hyphen as delimiter for MAC auth password.", "label": "Single Hyphen", "name": "single-hyphen"}],
        },
        "mac-calling-station-delimiter": {
            "type": "option",
            "help": "MAC calling station delimiter (default = hyphen).",
            "default": "hyphen",
            "options": [{"help": "Use colon as delimiter for calling station.", "label": "Colon", "name": "colon"}, {"help": "Use hyphen as delimiter for calling station.", "label": "Hyphen", "name": "hyphen"}, {"help": "No delimiter for calling station.", "label": "None", "name": "none"}, {"help": "Use single hyphen as delimiter for calling station.", "label": "Single Hyphen", "name": "single-hyphen"}],
        },
        "mac-called-station-delimiter": {
            "type": "option",
            "help": "MAC called station delimiter (default = hyphen).",
            "default": "hyphen",
            "options": [{"help": "Use colon as delimiter for called station.", "label": "Colon", "name": "colon"}, {"help": "Use hyphen as delimiter for called station.", "label": "Hyphen", "name": "hyphen"}, {"help": "No delimiter for called station.", "label": "None", "name": "none"}, {"help": "Use single hyphen as delimiter for called station.", "label": "Single Hyphen", "name": "single-hyphen"}],
        },
        "mac-case": {
            "type": "option",
            "help": "MAC case (default = lowercase).",
            "default": "lowercase",
            "options": [{"help": "Use lowercase MAC.", "label": "Lowercase", "name": "lowercase"}, {"help": "Use uppercase MAC.", "label": "Uppercase", "name": "uppercase"}],
        },
    },
    "router-vrf": {
        "name": {
            "type": "string",
            "help": "VRF entry name.",
            "required": True,
            "default": "",
            "max_length": 35,
        },
        "switch-id": {
            "type": "string",
            "help": "Switch ID.",
            "default": "",
            "max_length": 35,
        },
        "vrfid": {
            "type": "integer",
            "help": "VRF ID.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 1023,
        },
    },
    "system-interface": {
        "name": {
            "type": "string",
            "help": "Interface name.",
            "default": "",
            "max_length": 15,
        },
        "switch-id": {
            "type": "string",
            "help": "Switch ID.",
            "default": "",
            "max_length": 35,
        },
        "mode": {
            "type": "option",
            "help": "Interface addressing mode.",
            "default": "static",
            "options": [{"help": "static addressing mode.", "label": "Static", "name": "static"}, {"help": "DHCP addressing mode.", "label": "Dhcp", "name": "dhcp"}],
        },
        "ip": {
            "type": "ipv4-classnet-host",
            "help": "IP and mask for this interface.",
            "required": True,
            "default": "0.0.0.0 0.0.0.0",
        },
        "status": {
            "type": "option",
            "help": "Enable/disable interface status.",
            "default": "enable",
            "options": [{"help": "Disable interface.", "label": "Disable", "name": "disable"}, {"help": "Enable interface.", "label": "Enable", "name": "enable"}],
        },
        "allowaccess": {
            "type": "option",
            "help": "Permitted types of management access to this interface.",
            "default": "",
            "options": [{"help": "PING.", "label": "Ping", "name": "ping"}, {"help": "HTTPS.", "label": "Https", "name": "https"}, {"help": "HTTP.", "label": "Http", "name": "http"}, {"help": "SSH.", "label": "Ssh", "name": "ssh"}, {"help": "SNMP.", "label": "Snmp", "name": "snmp"}, {"help": "TELNET.", "label": "Telnet", "name": "telnet"}, {"help": "RADIUS ACCOUNTING.", "label": "Radius Acct", "name": "radius-acct"}],
        },
        "vlan": {
            "type": "string",
            "help": "VLAN name.",
            "required": True,
            "default": "",
            "max_length": 15,
        },
        "type": {
            "type": "option",
            "help": "Interface type.",
            "default": "vlan",
            "options": [{"help": "VLAN interface.", "label": "Vlan", "name": "vlan"}, {"help": "Physical interface.", "label": "Physical", "name": "physical"}],
        },
        "interface": {
            "type": "string",
            "help": "Interface name.",
            "required": True,
            "default": "",
            "max_length": 63,
        },
        "vrf": {
            "type": "string",
            "help": "VRF for this route.",
            "default": "",
            "max_length": 63,
        },
    },
    "router-static": {
        "id": {
            "type": "integer",
            "help": "Entry sequence number.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "switch-id": {
            "type": "string",
            "help": "Switch ID.",
            "default": "",
            "max_length": 35,
        },
        "blackhole": {
            "type": "option",
            "help": "Enable/disable blackhole on this route.",
            "default": "disable",
            "options": [{"help": "Disable blackhole on this route.", "label": "Disable", "name": "disable"}, {"help": "Enable blackhole on this route.", "label": "Enable", "name": "enable"}],
        },
        "comment": {
            "type": "string",
            "help": "Comment.",
            "default": "",
            "max_length": 63,
        },
        "device": {
            "type": "string",
            "help": "Gateway out interface.",
            "default": "",
            "max_length": 35,
        },
        "distance": {
            "type": "integer",
            "help": "Administrative distance for the route (1 - 255, default = 10).",
            "default": 10,
            "min_value": 1,
            "max_value": 255,
        },
        "dst": {
            "type": "ipv4-classnet",
            "help": "Destination ip and mask for this route.",
            "required": True,
            "default": "0.0.0.0 0.0.0.0",
        },
        "dynamic-gateway": {
            "type": "option",
            "help": "Enable/disable dynamic gateway.",
            "default": "disable",
            "options": [{"help": "Disable dynamic gateway on this route.", "label": "Disable", "name": "disable"}, {"help": "Disable dynamic gateway on this route.", "label": "Enable", "name": "enable"}],
        },
        "gateway": {
            "type": "ipv4-address",
            "help": "Gateway ip for this route.",
            "required": True,
            "default": "0.0.0.0",
        },
        "status": {
            "type": "option",
            "help": "Enable/disable route status.",
            "default": "enable",
            "options": [{"help": "Disable route status.", "label": "Disable", "name": "disable"}, {"help": "Enable route status.", "label": "Enable", "name": "enable"}],
        },
        "vrf": {
            "type": "string",
            "help": "VRF for this route.",
            "default": "",
            "max_length": 35,
        },
    },
    "system-dhcp-server": {
        "id": {
            "type": "integer",
            "help": "ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "switch-id": {
            "type": "string",
            "help": "Switch ID.",
            "default": "",
            "max_length": 35,
        },
        "status": {
            "type": "option",
            "help": "Enable/disable this DHCP configuration.",
            "default": "enable",
            "options": [{"help": "Do not use this DHCP server configuration.", "label": "Disable", "name": "disable"}, {"help": "Use this DHCP server configuration.", "label": "Enable", "name": "enable"}],
        },
        "lease-time": {
            "type": "integer",
            "help": "Lease time in seconds, 0 means unlimited.",
            "default": 604800,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "dns-service": {
            "type": "option",
            "help": "Options for assigning DNS servers to DHCP clients.",
            "default": "specify",
            "options": [{"help": "IP address of the interface the DHCP server is added to becomes the client\u0027s DNS server IP address.", "label": "Local", "name": "local"}, {"help": "Clients are assigned the FortiGate\u0027s configured DNS servers.", "label": "Default", "name": "default"}, {"help": "Specify up to 3 DNS servers in the DHCP server configuration.", "label": "Specify", "name": "specify"}],
        },
        "dns-server1": {
            "type": "ipv4-address",
            "help": "DNS server 1.",
            "default": "0.0.0.0",
        },
        "dns-server2": {
            "type": "ipv4-address",
            "help": "DNS server 2.",
            "default": "0.0.0.0",
        },
        "dns-server3": {
            "type": "ipv4-address",
            "help": "DNS server 3.",
            "default": "0.0.0.0",
        },
        "ntp-service": {
            "type": "option",
            "help": "Options for assigning Network Time Protocol (NTP) servers to DHCP clients.",
            "default": "specify",
            "options": [{"help": "IP address of the interface the DHCP server is added to becomes the client\u0027s NTP server IP address.", "label": "Local", "name": "local"}, {"help": "Clients are assigned the FortiGate\u0027s configured NTP servers.", "label": "Default", "name": "default"}, {"help": "Specify up to 3 NTP servers in the DHCP server configuration.", "label": "Specify", "name": "specify"}],
        },
        "ntp-server1": {
            "type": "ipv4-address",
            "help": "NTP server 1.",
            "default": "0.0.0.0",
        },
        "ntp-server2": {
            "type": "ipv4-address",
            "help": "NTP server 2.",
            "default": "0.0.0.0",
        },
        "ntp-server3": {
            "type": "ipv4-address",
            "help": "NTP server 3.",
            "default": "0.0.0.0",
        },
        "default-gateway": {
            "type": "ipv4-address",
            "help": "Default gateway IP address assigned by the DHCP server.",
            "default": "0.0.0.0",
        },
        "netmask": {
            "type": "ipv4-netmask",
            "help": "Netmask assigned by the DHCP server.",
            "required": True,
            "default": "0.0.0.0",
        },
        "interface": {
            "type": "string",
            "help": "DHCP server can assign IP configurations to clients connected to this interface.",
            "required": True,
            "default": "",
            "max_length": 15,
        },
        "ip-range": {
            "type": "string",
            "help": "DHCP IP range configuration.",
        },
        "options": {
            "type": "string",
            "help": "DHCP options.",
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_PURDUE_LEVEL = [
    "1",  # Level 1 - Basic Control
    "1.5",  # Level 1.5
    "2",  # Level 2 - Area Supervisory Control
    "2.5",  # Level 2.5
    "3",  # Level 3 - Operations & Control
    "3.5",  # Level 3.5
    "4",  # Level 4 - Business Planning & Logistics
    "5",  # Level 5 - Enterprise Network
    "5.5",  # Level 5.5
]
VALID_BODY_FSW_WAN1_ADMIN = [
    "discovered",  # Link waiting to be authorized.
    "disable",  # Link unauthorized.
    "enable",  # Link authorized.
]
VALID_BODY_POE_PRE_STANDARD_DETECTION = [
    "enable",  # Enable PoE pre-standard detection.
    "disable",  # Disable PoE pre-standard detection.
]
VALID_BODY_DHCP_SERVER_ACCESS_LIST = [
    "global",  # Use global setting for DHCP snooping server access list.
    "enable",  # Override global setting and enable DHCP server access list.
    "disable",  # Override global setting and disable DHCP server access list.
]
VALID_BODY_MCLAG_IGMP_SNOOPING_AWARE = [
    "enable",  # Enable MCLAG IGMP-snooping awareness.
    "disable",  # Disable MCLAG IGMP-snooping awareness.
]
VALID_BODY_PTP_STATUS = [
    "disable",  # Disable PTP profile.
    "enable",  # Enable PTP profile.
]
VALID_BODY_RADIUS_NAS_IP_OVERRIDE = [
    "disable",  # Disable radius-nas-ip-override.
    "enable",  # Enable radius-nas-ip-override.
]
VALID_BODY_ROUTE_OFFLOAD = [
    "disable",  # Disable route offload.
    "enable",  # Enable route offload.
]
VALID_BODY_ROUTE_OFFLOAD_MCLAG = [
    "disable",  # Disable route offload MCLAG.
    "enable",  # Enable route offload MCLAG.
]
VALID_BODY_TYPE = [
    "virtual",  # Switch is of type virtual.
    "physical",  # Switch is of type physical.
]
VALID_BODY_FIRMWARE_PROVISION = [
    "enable",  # Enable firmware-provision.
    "disable",  # Disable firmware-provision.
]
VALID_BODY_FIRMWARE_PROVISION_LATEST = [
    "disable",  # Do not automatically provision the latest available firmware.
    "once",  # Automatically attempt a one-time upgrade to the latest available firmware version.
]
VALID_BODY_OVERRIDE_SNMP_SYSINFO = [
    "disable",  # Use the global SNMP system information.
    "enable",  # Override the global SNMP system information.
]
VALID_BODY_OVERRIDE_SNMP_TRAP_THRESHOLD = [
    "enable",  # Override the global SNMP trap threshold values.
    "disable",  # Use the global SNMP trap threshold values.
]
VALID_BODY_OVERRIDE_SNMP_COMMUNITY = [
    "enable",  # Override the global SNMP communities.
    "disable",  # Use the global SNMP communities.
]
VALID_BODY_OVERRIDE_SNMP_USER = [
    "enable",  # Override the global SNMPv3 users.
    "disable",  # Use the global SNMPv3 users.
]
VALID_BODY_QOS_DROP_POLICY = [
    "taildrop",  # Taildrop policy.
    "random-early-detection",  # Random early detection drop policy.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_switch_controller_managed_switch_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for switch_controller/managed_switch."""
    # Validate query parameters if present
    if "action" in params:
        value = params.get("action")
        if value and value not in VALID_QUERY_ACTION:
            return (
                False,
                f"Invalid query parameter 'action'='{value}'. Must be one of: {', '.join(VALID_QUERY_ACTION)}",
            )

    return (True, None)


# ============================================================================
# POST Validation
# ============================================================================


def validate_required_fields(payload: dict) -> tuple[bool, str | None]:
    """Validate required fields for switch_controller/managed_switch."""
    # Check always-required fields
    missing_fields = []
    for field in REQUIRED_FIELDS:
        if field not in payload:
            missing_fields.append(field)
    
    if missing_fields:
        # Build enhanced error message
        error_parts = [f"Missing required field(s): {', '.join(missing_fields)}"]
        
        # Add descriptions for first few missing fields
        for field in missing_fields[:3]:
            desc = FIELD_DESCRIPTIONS.get(field)
            if desc:
                error_parts.append(f"  • {field}: {desc}")
        
        if len(missing_fields) > 3:
            error_parts.append(f"  ... and {len(missing_fields) - 3} more")
        
        return (False, "\n".join(error_parts))

    return (True, None)


def validate_switch_controller_managed_switch_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new switch_controller/managed_switch object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "purdue-level" in payload:
        value = payload["purdue-level"]
        if value not in VALID_BODY_PURDUE_LEVEL:
            desc = FIELD_DESCRIPTIONS.get("purdue-level", "")
            error_msg = f"Invalid value for 'purdue-level': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PURDUE_LEVEL)}"
            error_msg += f"\n  → Example: purdue-level='{{ VALID_BODY_PURDUE_LEVEL[0] }}'"
            return (False, error_msg)
    if "fsw-wan1-admin" in payload:
        value = payload["fsw-wan1-admin"]
        if value not in VALID_BODY_FSW_WAN1_ADMIN:
            desc = FIELD_DESCRIPTIONS.get("fsw-wan1-admin", "")
            error_msg = f"Invalid value for 'fsw-wan1-admin': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FSW_WAN1_ADMIN)}"
            error_msg += f"\n  → Example: fsw-wan1-admin='{{ VALID_BODY_FSW_WAN1_ADMIN[0] }}'"
            return (False, error_msg)
    if "poe-pre-standard-detection" in payload:
        value = payload["poe-pre-standard-detection"]
        if value not in VALID_BODY_POE_PRE_STANDARD_DETECTION:
            desc = FIELD_DESCRIPTIONS.get("poe-pre-standard-detection", "")
            error_msg = f"Invalid value for 'poe-pre-standard-detection': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_POE_PRE_STANDARD_DETECTION)}"
            error_msg += f"\n  → Example: poe-pre-standard-detection='{{ VALID_BODY_POE_PRE_STANDARD_DETECTION[0] }}'"
            return (False, error_msg)
    if "dhcp-server-access-list" in payload:
        value = payload["dhcp-server-access-list"]
        if value not in VALID_BODY_DHCP_SERVER_ACCESS_LIST:
            desc = FIELD_DESCRIPTIONS.get("dhcp-server-access-list", "")
            error_msg = f"Invalid value for 'dhcp-server-access-list': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DHCP_SERVER_ACCESS_LIST)}"
            error_msg += f"\n  → Example: dhcp-server-access-list='{{ VALID_BODY_DHCP_SERVER_ACCESS_LIST[0] }}'"
            return (False, error_msg)
    if "mclag-igmp-snooping-aware" in payload:
        value = payload["mclag-igmp-snooping-aware"]
        if value not in VALID_BODY_MCLAG_IGMP_SNOOPING_AWARE:
            desc = FIELD_DESCRIPTIONS.get("mclag-igmp-snooping-aware", "")
            error_msg = f"Invalid value for 'mclag-igmp-snooping-aware': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MCLAG_IGMP_SNOOPING_AWARE)}"
            error_msg += f"\n  → Example: mclag-igmp-snooping-aware='{{ VALID_BODY_MCLAG_IGMP_SNOOPING_AWARE[0] }}'"
            return (False, error_msg)
    if "ptp-status" in payload:
        value = payload["ptp-status"]
        if value not in VALID_BODY_PTP_STATUS:
            desc = FIELD_DESCRIPTIONS.get("ptp-status", "")
            error_msg = f"Invalid value for 'ptp-status': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PTP_STATUS)}"
            error_msg += f"\n  → Example: ptp-status='{{ VALID_BODY_PTP_STATUS[0] }}'"
            return (False, error_msg)
    if "radius-nas-ip-override" in payload:
        value = payload["radius-nas-ip-override"]
        if value not in VALID_BODY_RADIUS_NAS_IP_OVERRIDE:
            desc = FIELD_DESCRIPTIONS.get("radius-nas-ip-override", "")
            error_msg = f"Invalid value for 'radius-nas-ip-override': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_RADIUS_NAS_IP_OVERRIDE)}"
            error_msg += f"\n  → Example: radius-nas-ip-override='{{ VALID_BODY_RADIUS_NAS_IP_OVERRIDE[0] }}'"
            return (False, error_msg)
    if "route-offload" in payload:
        value = payload["route-offload"]
        if value not in VALID_BODY_ROUTE_OFFLOAD:
            desc = FIELD_DESCRIPTIONS.get("route-offload", "")
            error_msg = f"Invalid value for 'route-offload': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ROUTE_OFFLOAD)}"
            error_msg += f"\n  → Example: route-offload='{{ VALID_BODY_ROUTE_OFFLOAD[0] }}'"
            return (False, error_msg)
    if "route-offload-mclag" in payload:
        value = payload["route-offload-mclag"]
        if value not in VALID_BODY_ROUTE_OFFLOAD_MCLAG:
            desc = FIELD_DESCRIPTIONS.get("route-offload-mclag", "")
            error_msg = f"Invalid value for 'route-offload-mclag': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ROUTE_OFFLOAD_MCLAG)}"
            error_msg += f"\n  → Example: route-offload-mclag='{{ VALID_BODY_ROUTE_OFFLOAD_MCLAG[0] }}'"
            return (False, error_msg)
    if "type" in payload:
        value = payload["type"]
        if value not in VALID_BODY_TYPE:
            desc = FIELD_DESCRIPTIONS.get("type", "")
            error_msg = f"Invalid value for 'type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TYPE)}"
            error_msg += f"\n  → Example: type='{{ VALID_BODY_TYPE[0] }}'"
            return (False, error_msg)
    if "firmware-provision" in payload:
        value = payload["firmware-provision"]
        if value not in VALID_BODY_FIRMWARE_PROVISION:
            desc = FIELD_DESCRIPTIONS.get("firmware-provision", "")
            error_msg = f"Invalid value for 'firmware-provision': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FIRMWARE_PROVISION)}"
            error_msg += f"\n  → Example: firmware-provision='{{ VALID_BODY_FIRMWARE_PROVISION[0] }}'"
            return (False, error_msg)
    if "firmware-provision-latest" in payload:
        value = payload["firmware-provision-latest"]
        if value not in VALID_BODY_FIRMWARE_PROVISION_LATEST:
            desc = FIELD_DESCRIPTIONS.get("firmware-provision-latest", "")
            error_msg = f"Invalid value for 'firmware-provision-latest': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FIRMWARE_PROVISION_LATEST)}"
            error_msg += f"\n  → Example: firmware-provision-latest='{{ VALID_BODY_FIRMWARE_PROVISION_LATEST[0] }}'"
            return (False, error_msg)
    if "override-snmp-sysinfo" in payload:
        value = payload["override-snmp-sysinfo"]
        if value not in VALID_BODY_OVERRIDE_SNMP_SYSINFO:
            desc = FIELD_DESCRIPTIONS.get("override-snmp-sysinfo", "")
            error_msg = f"Invalid value for 'override-snmp-sysinfo': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OVERRIDE_SNMP_SYSINFO)}"
            error_msg += f"\n  → Example: override-snmp-sysinfo='{{ VALID_BODY_OVERRIDE_SNMP_SYSINFO[0] }}'"
            return (False, error_msg)
    if "override-snmp-trap-threshold" in payload:
        value = payload["override-snmp-trap-threshold"]
        if value not in VALID_BODY_OVERRIDE_SNMP_TRAP_THRESHOLD:
            desc = FIELD_DESCRIPTIONS.get("override-snmp-trap-threshold", "")
            error_msg = f"Invalid value for 'override-snmp-trap-threshold': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OVERRIDE_SNMP_TRAP_THRESHOLD)}"
            error_msg += f"\n  → Example: override-snmp-trap-threshold='{{ VALID_BODY_OVERRIDE_SNMP_TRAP_THRESHOLD[0] }}'"
            return (False, error_msg)
    if "override-snmp-community" in payload:
        value = payload["override-snmp-community"]
        if value not in VALID_BODY_OVERRIDE_SNMP_COMMUNITY:
            desc = FIELD_DESCRIPTIONS.get("override-snmp-community", "")
            error_msg = f"Invalid value for 'override-snmp-community': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OVERRIDE_SNMP_COMMUNITY)}"
            error_msg += f"\n  → Example: override-snmp-community='{{ VALID_BODY_OVERRIDE_SNMP_COMMUNITY[0] }}'"
            return (False, error_msg)
    if "override-snmp-user" in payload:
        value = payload["override-snmp-user"]
        if value not in VALID_BODY_OVERRIDE_SNMP_USER:
            desc = FIELD_DESCRIPTIONS.get("override-snmp-user", "")
            error_msg = f"Invalid value for 'override-snmp-user': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OVERRIDE_SNMP_USER)}"
            error_msg += f"\n  → Example: override-snmp-user='{{ VALID_BODY_OVERRIDE_SNMP_USER[0] }}'"
            return (False, error_msg)
    if "qos-drop-policy" in payload:
        value = payload["qos-drop-policy"]
        if value not in VALID_BODY_QOS_DROP_POLICY:
            desc = FIELD_DESCRIPTIONS.get("qos-drop-policy", "")
            error_msg = f"Invalid value for 'qos-drop-policy': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_QOS_DROP_POLICY)}"
            error_msg += f"\n  → Example: qos-drop-policy='{{ VALID_BODY_QOS_DROP_POLICY[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_switch_controller_managed_switch_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update switch_controller/managed_switch."""
    # Step 1: Validate enum values
    if "purdue-level" in payload:
        value = payload["purdue-level"]
        if value not in VALID_BODY_PURDUE_LEVEL:
            return (
                False,
                f"Invalid value for 'purdue-level'='{value}'. Must be one of: {', '.join(VALID_BODY_PURDUE_LEVEL)}",
            )
    if "fsw-wan1-admin" in payload:
        value = payload["fsw-wan1-admin"]
        if value not in VALID_BODY_FSW_WAN1_ADMIN:
            return (
                False,
                f"Invalid value for 'fsw-wan1-admin'='{value}'. Must be one of: {', '.join(VALID_BODY_FSW_WAN1_ADMIN)}",
            )
    if "poe-pre-standard-detection" in payload:
        value = payload["poe-pre-standard-detection"]
        if value not in VALID_BODY_POE_PRE_STANDARD_DETECTION:
            return (
                False,
                f"Invalid value for 'poe-pre-standard-detection'='{value}'. Must be one of: {', '.join(VALID_BODY_POE_PRE_STANDARD_DETECTION)}",
            )
    if "dhcp-server-access-list" in payload:
        value = payload["dhcp-server-access-list"]
        if value not in VALID_BODY_DHCP_SERVER_ACCESS_LIST:
            return (
                False,
                f"Invalid value for 'dhcp-server-access-list'='{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_SERVER_ACCESS_LIST)}",
            )
    if "mclag-igmp-snooping-aware" in payload:
        value = payload["mclag-igmp-snooping-aware"]
        if value not in VALID_BODY_MCLAG_IGMP_SNOOPING_AWARE:
            return (
                False,
                f"Invalid value for 'mclag-igmp-snooping-aware'='{value}'. Must be one of: {', '.join(VALID_BODY_MCLAG_IGMP_SNOOPING_AWARE)}",
            )
    if "ptp-status" in payload:
        value = payload["ptp-status"]
        if value not in VALID_BODY_PTP_STATUS:
            return (
                False,
                f"Invalid value for 'ptp-status'='{value}'. Must be one of: {', '.join(VALID_BODY_PTP_STATUS)}",
            )
    if "radius-nas-ip-override" in payload:
        value = payload["radius-nas-ip-override"]
        if value not in VALID_BODY_RADIUS_NAS_IP_OVERRIDE:
            return (
                False,
                f"Invalid value for 'radius-nas-ip-override'='{value}'. Must be one of: {', '.join(VALID_BODY_RADIUS_NAS_IP_OVERRIDE)}",
            )
    if "route-offload" in payload:
        value = payload["route-offload"]
        if value not in VALID_BODY_ROUTE_OFFLOAD:
            return (
                False,
                f"Invalid value for 'route-offload'='{value}'. Must be one of: {', '.join(VALID_BODY_ROUTE_OFFLOAD)}",
            )
    if "route-offload-mclag" in payload:
        value = payload["route-offload-mclag"]
        if value not in VALID_BODY_ROUTE_OFFLOAD_MCLAG:
            return (
                False,
                f"Invalid value for 'route-offload-mclag'='{value}'. Must be one of: {', '.join(VALID_BODY_ROUTE_OFFLOAD_MCLAG)}",
            )
    if "type" in payload:
        value = payload["type"]
        if value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid value for 'type'='{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )
    if "firmware-provision" in payload:
        value = payload["firmware-provision"]
        if value not in VALID_BODY_FIRMWARE_PROVISION:
            return (
                False,
                f"Invalid value for 'firmware-provision'='{value}'. Must be one of: {', '.join(VALID_BODY_FIRMWARE_PROVISION)}",
            )
    if "firmware-provision-latest" in payload:
        value = payload["firmware-provision-latest"]
        if value not in VALID_BODY_FIRMWARE_PROVISION_LATEST:
            return (
                False,
                f"Invalid value for 'firmware-provision-latest'='{value}'. Must be one of: {', '.join(VALID_BODY_FIRMWARE_PROVISION_LATEST)}",
            )
    if "override-snmp-sysinfo" in payload:
        value = payload["override-snmp-sysinfo"]
        if value not in VALID_BODY_OVERRIDE_SNMP_SYSINFO:
            return (
                False,
                f"Invalid value for 'override-snmp-sysinfo'='{value}'. Must be one of: {', '.join(VALID_BODY_OVERRIDE_SNMP_SYSINFO)}",
            )
    if "override-snmp-trap-threshold" in payload:
        value = payload["override-snmp-trap-threshold"]
        if value not in VALID_BODY_OVERRIDE_SNMP_TRAP_THRESHOLD:
            return (
                False,
                f"Invalid value for 'override-snmp-trap-threshold'='{value}'. Must be one of: {', '.join(VALID_BODY_OVERRIDE_SNMP_TRAP_THRESHOLD)}",
            )
    if "override-snmp-community" in payload:
        value = payload["override-snmp-community"]
        if value not in VALID_BODY_OVERRIDE_SNMP_COMMUNITY:
            return (
                False,
                f"Invalid value for 'override-snmp-community'='{value}'. Must be one of: {', '.join(VALID_BODY_OVERRIDE_SNMP_COMMUNITY)}",
            )
    if "override-snmp-user" in payload:
        value = payload["override-snmp-user"]
        if value not in VALID_BODY_OVERRIDE_SNMP_USER:
            return (
                False,
                f"Invalid value for 'override-snmp-user'='{value}'. Must be one of: {', '.join(VALID_BODY_OVERRIDE_SNMP_USER)}",
            )
    if "qos-drop-policy" in payload:
        value = payload["qos-drop-policy"]
        if value not in VALID_BODY_QOS_DROP_POLICY:
            return (
                False,
                f"Invalid value for 'qos-drop-policy'='{value}'. Must be one of: {', '.join(VALID_BODY_QOS_DROP_POLICY)}",
            )

    return (True, None)


# ============================================================================
# Metadata Access Functions
# Imported from central module to avoid duplication across 1,062 files
# ============================================================================

from hfortix_fortios._helpers.metadata import (
    get_field_description as _get_field_description,
    get_field_type as _get_field_type,
    get_field_constraints as _get_field_constraints,
    get_field_default as _get_field_default,
    get_field_options as _get_field_options,
    get_nested_schema as _get_nested_schema,
    get_all_fields as _get_all_fields,
    get_field_metadata as _get_field_metadata,
    validate_field_value as _validate_field_value,
)

# Wrapper functions that bind module-specific data to central functions
def get_field_description(field_name: str) -> str | None:
    """Get description/help text for a field."""
    return _get_field_description(FIELD_DESCRIPTIONS, field_name)

def get_field_type(field_name: str) -> str | None:
    """Get the type of a field."""
    return _get_field_type(FIELD_TYPES, field_name)

def get_field_constraints(field_name: str) -> dict[str, Any] | None:
    """Get constraints for a field (min/max values, string length)."""
    return _get_field_constraints(FIELD_CONSTRAINTS, field_name)

def get_field_default(field_name: str) -> Any | None:
    """Get default value for a field."""
    return _get_field_default(FIELDS_WITH_DEFAULTS, field_name)

def get_field_options(field_name: str) -> list[str] | None:
    """Get valid enum options for a field."""
    return _get_field_options(globals(), field_name)

def get_nested_schema(field_name: str) -> dict[str, Any] | None:
    """Get schema for nested table/list fields."""
    return _get_nested_schema(NESTED_SCHEMAS, field_name)

def get_all_fields() -> list[str]:
    """Get list of all field names."""
    return _get_all_fields(FIELD_TYPES)

def get_field_metadata(field_name: str) -> dict[str, Any] | None:
    """Get complete metadata for a field (type, description, constraints, defaults, options)."""
    return _get_field_metadata(
        FIELD_TYPES, FIELD_DESCRIPTIONS, FIELD_CONSTRAINTS,
        FIELDS_WITH_DEFAULTS, REQUIRED_FIELDS, NESTED_SCHEMAS,
        globals(), field_name
    )

def validate_field_value(field_name: str, value: Any) -> tuple[bool, str | None]:
    """Validate a single field value against its constraints."""
    return _validate_field_value(
        FIELD_TYPES, FIELD_DESCRIPTIONS, FIELD_CONSTRAINTS,
        globals(), field_name, value
    )


# ============================================================================
# Schema Information
# Metadata about this endpoint schema
# ============================================================================

SCHEMA_INFO = {
    "endpoint": "switch_controller/managed_switch",
    "category": "cmdb",
    "api_path": "switch-controller/managed-switch",
    "mkey": "switch-id",
    "mkey_type": "string",
    "help": "Configure FortiSwitch devices that are managed by this FortiGate.",
    "total_fields": 68,
    "required_fields_count": 3,
    "fields_with_defaults_count": 45,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
