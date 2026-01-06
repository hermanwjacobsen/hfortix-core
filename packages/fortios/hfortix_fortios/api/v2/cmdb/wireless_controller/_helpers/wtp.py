"""
Validation helpers for wireless_controller/wtp endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification
Customize as needed for endpoint-specific business logic.
"""

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
#
# 1. FALSE POSITIVES: Some fields marked "required" have default values,
#    meaning they're optional (filtered out by generator)
#
# 2. CONDITIONAL REQUIREMENTS: Many endpoints require EITHER field A OR field B:
#    - firewall.policy: requires (srcaddr + dstaddr) OR (srcaddr6 + dstaddr6)
#    - These conditional requirements cannot be expressed in a simple list
#
# 3. SPECIALIZED FEATURES: Fields for WAN optimization, VPN, NAT64, etc.
#    are marked "required" but only apply when using those features
#
# The REQUIRED_FIELDS list below is INFORMATIONAL ONLY and shows fields that:
# - Are marked required in the schema
# - Don't have non-empty default values
# - Aren't specialized feature fields
#
# Do NOT use this list for strict validation - test with the actual FortiOS API!

# Fields marked as required (after filtering false positives)
REQUIRED_FIELDS = [
    "wtp-id",  # WTP ID.
    "wtp-profile",  # WTP profile name to apply to this WTP, AP or FortiAP.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "wtp-id": "",
    "index": 0,
    "uuid": "00000000-0000-0000-0000-000000000000",
    "admin": "enable",
    "name": "",
    "location": "",
    "region": "",
    "region-x": "0",
    "region-y": "0",
    "firmware-provision": "",
    "firmware-provision-latest": "disable",
    "wtp-profile": "",
    "apcfg-profile": "",
    "bonjour-profile": "",
    "ble-major-id": 0,
    "ble-minor-id": 0,
    "override-led-state": "disable",
    "led-state": "enable",
    "override-wan-port-mode": "disable",
    "wan-port-mode": "wan-only",
    "override-ip-fragment": "disable",
    "ip-fragment-preventing": "tcp-mss-adjust",
    "tun-mtu-uplink": 0,
    "tun-mtu-downlink": 0,
    "override-split-tunnel": "disable",
    "split-tunneling-acl-path": "local",
    "split-tunneling-acl-local-ap-subnet": "disable",
    "override-lan": "disable",
    "override-allowaccess": "disable",
    "allowaccess": "",
    "override-login-passwd-change": "disable",
    "login-passwd-change": "no",
    "override-default-mesh-root": "disable",
    "default-mesh-root": "disable",
    "image-download": "enable",
    "mesh-bridge-enable": "default",
    "purdue-level": "3",
    "coordinate-latitude": "",
    "coordinate-longitude": "",
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
    "wtp-id": "string",  # WTP ID.
    "index": "integer",  # Index (0 - 4294967295).
    "uuid": "uuid",  # Universally Unique Identifier (UUID; automatically assigned 
    "admin": "option",  # Configure how the FortiGate operating as a wireless controll
    "name": "string",  # WTP, AP or FortiAP configuration name.
    "location": "string",  # Field for describing the physical location of the WTP, AP or
    "comment": "var-string",  # Comment.
    "region": "string",  # Region name WTP is associated with.
    "region-x": "string",  # Relative horizontal region coordinate (between 0 and 1).
    "region-y": "string",  # Relative vertical region coordinate (between 0 and 1).
    "firmware-provision": "string",  # Firmware version to provision to this FortiAP on bootup (maj
    "firmware-provision-latest": "option",  # Enable/disable one-time automatic provisioning of the latest
    "wtp-profile": "string",  # WTP profile name to apply to this WTP, AP or FortiAP.
    "apcfg-profile": "string",  # AP local configuration profile name.
    "bonjour-profile": "string",  # Bonjour profile name.
    "ble-major-id": "integer",  # Override BLE Major ID.
    "ble-minor-id": "integer",  # Override BLE Minor ID.
    "override-led-state": "option",  # Enable to override the profile LED state setting for this Fo
    "led-state": "option",  # Enable to allow the FortiAPs LEDs to light. Disable to keep 
    "override-wan-port-mode": "option",  # Enable/disable overriding the wan-port-mode in the WTP profi
    "wan-port-mode": "option",  # Enable/disable using the FortiAP WAN port as a LAN port.
    "override-ip-fragment": "option",  # Enable/disable overriding the WTP profile IP fragment preven
    "ip-fragment-preventing": "option",  # Method(s) by which IP fragmentation is prevented for control
    "tun-mtu-uplink": "integer",  # The maximum transmission unit (MTU) of uplink CAPWAP tunnel 
    "tun-mtu-downlink": "integer",  # The MTU of downlink CAPWAP tunnel (576 - 1500 bytes or 0; 0 
    "override-split-tunnel": "option",  # Enable/disable overriding the WTP profile split tunneling se
    "split-tunneling-acl-path": "option",  # Split tunneling ACL path is local/tunnel.
    "split-tunneling-acl-local-ap-subnet": "option",  # Enable/disable automatically adding local subnetwork of Fort
    "split-tunneling-acl": "string",  # Split tunneling ACL filter list.
    "override-lan": "option",  # Enable to override the WTP profile LAN port setting.
    "lan": "string",  # WTP LAN port mapping.
    "override-allowaccess": "option",  # Enable to override the WTP profile management access configu
    "allowaccess": "option",  # Control management access to the managed WTP, FortiAP, or AP
    "override-login-passwd-change": "option",  # Enable to override the WTP profile login-password (administr
    "login-passwd-change": "option",  # Change or reset the administrator password of a managed WTP,
    "login-passwd": "password",  # Set the managed WTP, FortiAP, or AP's administrator password
    "override-default-mesh-root": "option",  # Enable to override the WTP profile default mesh root SSID se
    "default-mesh-root": "option",  # Configure default mesh root SSID when it is not included by 
    "radio-1": "string",  # Configuration options for radio 1.
    "radio-2": "string",  # Configuration options for radio 2.
    "radio-3": "string",  # Configuration options for radio 3.
    "radio-4": "string",  # Configuration options for radio 4.
    "image-download": "option",  # Enable/disable WTP image download.
    "mesh-bridge-enable": "option",  # Enable/disable mesh Ethernet bridge when WTP is configured a
    "purdue-level": "option",  # Purdue Level of this WTP.
    "coordinate-latitude": "string",  # WTP latitude coordinate.
    "coordinate-longitude": "string",  # WTP longitude coordinate.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "wtp-id": "WTP ID.",
    "index": "Index (0 - 4294967295).",
    "uuid": "Universally Unique Identifier (UUID; automatically assigned but can be manually reset).",
    "admin": "Configure how the FortiGate operating as a wireless controller discovers and manages this WTP, AP or FortiAP.",
    "name": "WTP, AP or FortiAP configuration name.",
    "location": "Field for describing the physical location of the WTP, AP or FortiAP.",
    "comment": "Comment.",
    "region": "Region name WTP is associated with.",
    "region-x": "Relative horizontal region coordinate (between 0 and 1).",
    "region-y": "Relative vertical region coordinate (between 0 and 1).",
    "firmware-provision": "Firmware version to provision to this FortiAP on bootup (major.minor.build, i.e. 6.2.1234).",
    "firmware-provision-latest": "Enable/disable one-time automatic provisioning of the latest firmware version.",
    "wtp-profile": "WTP profile name to apply to this WTP, AP or FortiAP.",
    "apcfg-profile": "AP local configuration profile name.",
    "bonjour-profile": "Bonjour profile name.",
    "ble-major-id": "Override BLE Major ID.",
    "ble-minor-id": "Override BLE Minor ID.",
    "override-led-state": "Enable to override the profile LED state setting for this FortiAP. You must enable this option to use the led-state command to turn off the FortiAP's LEDs.",
    "led-state": "Enable to allow the FortiAPs LEDs to light. Disable to keep the LEDs off. You may want to keep the LEDs off so they are not distracting in low light areas etc.",
    "override-wan-port-mode": "Enable/disable overriding the wan-port-mode in the WTP profile.",
    "wan-port-mode": "Enable/disable using the FortiAP WAN port as a LAN port.",
    "override-ip-fragment": "Enable/disable overriding the WTP profile IP fragment prevention setting.",
    "ip-fragment-preventing": "Method(s) by which IP fragmentation is prevented for control and data packets through CAPWAP tunnel (default = tcp-mss-adjust).",
    "tun-mtu-uplink": "The maximum transmission unit (MTU) of uplink CAPWAP tunnel (576 - 1500 bytes or 0; 0 means the local MTU of FortiAP; default = 0).",
    "tun-mtu-downlink": "The MTU of downlink CAPWAP tunnel (576 - 1500 bytes or 0; 0 means the local MTU of FortiAP; default = 0).",
    "override-split-tunnel": "Enable/disable overriding the WTP profile split tunneling setting.",
    "split-tunneling-acl-path": "Split tunneling ACL path is local/tunnel.",
    "split-tunneling-acl-local-ap-subnet": "Enable/disable automatically adding local subnetwork of FortiAP to split-tunneling ACL (default = disable).",
    "split-tunneling-acl": "Split tunneling ACL filter list.",
    "override-lan": "Enable to override the WTP profile LAN port setting.",
    "lan": "WTP LAN port mapping.",
    "override-allowaccess": "Enable to override the WTP profile management access configuration.",
    "allowaccess": "Control management access to the managed WTP, FortiAP, or AP. Separate entries with a space.",
    "override-login-passwd-change": "Enable to override the WTP profile login-password (administrator password) setting.",
    "login-passwd-change": "Change or reset the administrator password of a managed WTP, FortiAP or AP (yes, default, or no, default = no).",
    "login-passwd": "Set the managed WTP, FortiAP, or AP's administrator password.",
    "override-default-mesh-root": "Enable to override the WTP profile default mesh root SSID setting.",
    "default-mesh-root": "Configure default mesh root SSID when it is not included by radio's SSID configuration.",
    "radio-1": "Configuration options for radio 1.",
    "radio-2": "Configuration options for radio 2.",
    "radio-3": "Configuration options for radio 3.",
    "radio-4": "Configuration options for radio 4.",
    "image-download": "Enable/disable WTP image download.",
    "mesh-bridge-enable": "Enable/disable mesh Ethernet bridge when WTP is configured as a mesh branch/leaf AP.",
    "purdue-level": "Purdue Level of this WTP.",
    "coordinate-latitude": "WTP latitude coordinate.",
    "coordinate-longitude": "WTP longitude coordinate.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "wtp-id": {"type": "string", "max_length": 35},
    "index": {"type": "integer", "min": 0, "max": 4294967295},
    "name": {"type": "string", "max_length": 35},
    "location": {"type": "string", "max_length": 35},
    "region": {"type": "string", "max_length": 35},
    "region-x": {"type": "string", "max_length": 15},
    "region-y": {"type": "string", "max_length": 15},
    "firmware-provision": {"type": "string", "max_length": 35},
    "wtp-profile": {"type": "string", "max_length": 35},
    "apcfg-profile": {"type": "string", "max_length": 35},
    "bonjour-profile": {"type": "string", "max_length": 35},
    "ble-major-id": {"type": "integer", "min": 0, "max": 65535},
    "ble-minor-id": {"type": "integer", "min": 0, "max": 65535},
    "tun-mtu-uplink": {"type": "integer", "min": 576, "max": 1500},
    "tun-mtu-downlink": {"type": "integer", "min": 576, "max": 1500},
    "coordinate-latitude": {"type": "string", "max_length": 19},
    "coordinate-longitude": {"type": "string", "max_length": 19},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "split-tunneling-acl": {
        "id": {
            "type": "integer",
            "help": "ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "dest-ip": {
            "type": "ipv4-classnet",
            "help": "Destination IP and mask for the split-tunneling subnet.",
            "required": True,
            "default": "0.0.0.0 0.0.0.0",
        },
    },
    "lan": {
        "port-mode": {
            "type": "option",
            "help": "LAN port mode.",
            "default": "offline",
            "options": [{"help": "Offline.", "label": "Offline", "name": "offline"}, {"help": "NAT WTP LAN port to WTP WAN port.", "label": "Nat To Wan", "name": "nat-to-wan"}, {"help": "Bridge WTP LAN port to WTP WAN port.", "label": "Bridge To Wan", "name": "bridge-to-wan"}, {"help": "Bridge WTP LAN port to SSID.", "label": "Bridge To Ssid", "name": "bridge-to-ssid"}],
        },
        "port-ssid": {
            "type": "string",
            "help": "Bridge LAN port to SSID.",
            "default": "",
            "max_length": 15,
        },
        "port1-mode": {
            "type": "option",
            "help": "LAN port 1 mode.",
            "default": "offline",
            "options": [{"help": "Offline.", "label": "Offline", "name": "offline"}, {"help": "NAT WTP LAN port to WTP WAN port.", "label": "Nat To Wan", "name": "nat-to-wan"}, {"help": "Bridge WTP LAN port to WTP WAN port.", "label": "Bridge To Wan", "name": "bridge-to-wan"}, {"help": "Bridge WTP LAN port to SSID.", "label": "Bridge To Ssid", "name": "bridge-to-ssid"}],
        },
        "port1-ssid": {
            "type": "string",
            "help": "Bridge LAN port 1 to SSID.",
            "default": "",
            "max_length": 15,
        },
        "port2-mode": {
            "type": "option",
            "help": "LAN port 2 mode.",
            "default": "offline",
            "options": [{"help": "Offline.", "label": "Offline", "name": "offline"}, {"help": "NAT WTP LAN port to WTP WAN port.", "label": "Nat To Wan", "name": "nat-to-wan"}, {"help": "Bridge WTP LAN port to WTP WAN port.", "label": "Bridge To Wan", "name": "bridge-to-wan"}, {"help": "Bridge WTP LAN port to SSID.", "label": "Bridge To Ssid", "name": "bridge-to-ssid"}],
        },
        "port2-ssid": {
            "type": "string",
            "help": "Bridge LAN port 2 to SSID.",
            "default": "",
            "max_length": 15,
        },
        "port3-mode": {
            "type": "option",
            "help": "LAN port 3 mode.",
            "default": "offline",
            "options": [{"help": "Offline.", "label": "Offline", "name": "offline"}, {"help": "NAT WTP LAN port to WTP WAN port.", "label": "Nat To Wan", "name": "nat-to-wan"}, {"help": "Bridge WTP LAN port to WTP WAN port.", "label": "Bridge To Wan", "name": "bridge-to-wan"}, {"help": "Bridge WTP LAN port to SSID.", "label": "Bridge To Ssid", "name": "bridge-to-ssid"}],
        },
        "port3-ssid": {
            "type": "string",
            "help": "Bridge LAN port 3 to SSID.",
            "default": "",
            "max_length": 15,
        },
        "port4-mode": {
            "type": "option",
            "help": "LAN port 4 mode.",
            "default": "offline",
            "options": [{"help": "Offline.", "label": "Offline", "name": "offline"}, {"help": "NAT WTP LAN port to WTP WAN port.", "label": "Nat To Wan", "name": "nat-to-wan"}, {"help": "Bridge WTP LAN port to WTP WAN port.", "label": "Bridge To Wan", "name": "bridge-to-wan"}, {"help": "Bridge WTP LAN port to SSID.", "label": "Bridge To Ssid", "name": "bridge-to-ssid"}],
        },
        "port4-ssid": {
            "type": "string",
            "help": "Bridge LAN port 4 to SSID.",
            "default": "",
            "max_length": 15,
        },
        "port5-mode": {
            "type": "option",
            "help": "LAN port 5 mode.",
            "default": "offline",
            "options": [{"help": "Offline.", "label": "Offline", "name": "offline"}, {"help": "NAT WTP LAN port to WTP WAN port.", "label": "Nat To Wan", "name": "nat-to-wan"}, {"help": "Bridge WTP LAN port to WTP WAN port.", "label": "Bridge To Wan", "name": "bridge-to-wan"}, {"help": "Bridge WTP LAN port to SSID.", "label": "Bridge To Ssid", "name": "bridge-to-ssid"}],
        },
        "port5-ssid": {
            "type": "string",
            "help": "Bridge LAN port 5 to SSID.",
            "default": "",
            "max_length": 15,
        },
        "port6-mode": {
            "type": "option",
            "help": "LAN port 6 mode.",
            "default": "offline",
            "options": [{"help": "Offline.", "label": "Offline", "name": "offline"}, {"help": "NAT WTP LAN port to WTP WAN port.", "label": "Nat To Wan", "name": "nat-to-wan"}, {"help": "Bridge WTP LAN port to WTP WAN port.", "label": "Bridge To Wan", "name": "bridge-to-wan"}, {"help": "Bridge WTP LAN port to SSID.", "label": "Bridge To Ssid", "name": "bridge-to-ssid"}],
        },
        "port6-ssid": {
            "type": "string",
            "help": "Bridge LAN port 6 to SSID.",
            "default": "",
            "max_length": 15,
        },
        "port7-mode": {
            "type": "option",
            "help": "LAN port 7 mode.",
            "default": "offline",
            "options": [{"help": "Offline.", "label": "Offline", "name": "offline"}, {"help": "NAT WTP LAN port to WTP WAN port.", "label": "Nat To Wan", "name": "nat-to-wan"}, {"help": "Bridge WTP LAN port to WTP WAN port.", "label": "Bridge To Wan", "name": "bridge-to-wan"}, {"help": "Bridge WTP LAN port to SSID.", "label": "Bridge To Ssid", "name": "bridge-to-ssid"}],
        },
        "port7-ssid": {
            "type": "string",
            "help": "Bridge LAN port 7 to SSID.",
            "default": "",
            "max_length": 15,
        },
        "port8-mode": {
            "type": "option",
            "help": "LAN port 8 mode.",
            "default": "offline",
            "options": [{"help": "Offline.", "label": "Offline", "name": "offline"}, {"help": "NAT WTP LAN port to WTP WAN port.", "label": "Nat To Wan", "name": "nat-to-wan"}, {"help": "Bridge WTP LAN port to WTP WAN port.", "label": "Bridge To Wan", "name": "bridge-to-wan"}, {"help": "Bridge WTP LAN port to SSID.", "label": "Bridge To Ssid", "name": "bridge-to-ssid"}],
        },
        "port8-ssid": {
            "type": "string",
            "help": "Bridge LAN port 8 to SSID.",
            "default": "",
            "max_length": 15,
        },
        "port-esl-mode": {
            "type": "option",
            "help": "ESL port mode.",
            "default": "offline",
            "options": [{"help": "Offline.", "label": "Offline", "name": "offline"}, {"help": "NAT WTP ESL port to WTP WAN port.", "label": "Nat To Wan", "name": "nat-to-wan"}, {"help": "Bridge WTP ESL port to WTP WAN port.", "label": "Bridge To Wan", "name": "bridge-to-wan"}, {"help": "Bridge WTP ESL port to SSID.", "label": "Bridge To Ssid", "name": "bridge-to-ssid"}],
        },
        "port-esl-ssid": {
            "type": "string",
            "help": "Bridge ESL port to SSID.",
            "default": "",
            "max_length": 15,
        },
    },
    "radio-1": {
        "override-band": {
            "type": "option",
            "help": "Enable to override the WTP profile band setting.",
            "default": "disable",
            "options": [{"help": "Override the WTP profile band setting.", "label": "Enable", "name": "enable"}, {"help": "Use the WTP profile band setting.", "label": "Disable", "name": "disable"}],
        },
        "band": {
            "type": "option",
            "help": "WiFi band that Radio 1 operates on.",
            "default": "",
            "options": [{"help": "802.11a.", "label": "802.11A", "name": "802.11a"}, {"help": "802.11b.", "label": "802.11B", "name": "802.11b"}, {"help": "802.11g.", "label": "802.11G", "name": "802.11g"}, {"help": "802.11n (WiFi 4) at 2.4GHz.", "label": "802.11N 2G", "name": "802.11n-2G"}, {"help": "802.11n (WiFi 4) at 5GHz.", "label": "802.11N 5G", "name": "802.11n-5G"}, {"help": "802.11ac (WiFi 5) at 2.4GHz.", "label": "802.11Ac 2G", "name": "802.11ac-2G"}, {"help": "802.11ac (WiFi 5) at 5GHz.", "label": "802.11Ac 5G", "name": "802.11ac-5G"}, {"help": "802.11ax (WiFi 6) at 2.4GHz.", "label": "802.11Ax 2G", "name": "802.11ax-2G"}, {"help": "802.11ax (WiFi 6) at 5GHz.", "label": "802.11Ax 5G", "name": "802.11ax-5G"}, {"help": "802.11ax (WiFi 6) at 6GHz.", "label": "802.11Ax 6G", "name": "802.11ax-6G"}, {"help": "802.11be (WiFi 7) at 2.4GHz.", "label": "802.11Be 2G", "name": "802.11be-2G"}, {"help": "802.11be (WiFi 7) at 5GHz.", "label": "802.11Be 5G", "name": "802.11be-5G"}, {"help": "802.11be (WiFi 7) at 6GHz.", "label": "802.11Be 6G", "name": "802.11be-6G"}],
        },
        "override-txpower": {
            "type": "option",
            "help": "Enable to override the WTP profile power level configuration.",
            "default": "disable",
            "options": [{"help": "Override the WTP profile power level configuration.", "label": "Enable", "name": "enable"}, {"help": "Use the WTP profile power level configuration.", "label": "Disable", "name": "disable"}],
        },
        "auto-power-level": {
            "type": "option",
            "help": "Enable/disable automatic power-level adjustment to prevent co-channel interference (default = enable).",
            "default": "disable",
            "options": [{"help": "Enable automatic transmit power adjustment.", "label": "Enable", "name": "enable"}, {"help": "Disable automatic transmit power adjustment.", "label": "Disable", "name": "disable"}],
        },
        "auto-power-high": {
            "type": "integer",
            "help": "The upper bound of automatic transmit power adjustment in dBm (the actual range of transmit power depends on the AP platform type).",
            "default": 17,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "auto-power-low": {
            "type": "integer",
            "help": "The lower bound of automatic transmit power adjustment in dBm (the actual range of transmit power depends on the AP platform type).",
            "default": 10,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "auto-power-target": {
            "type": "string",
            "help": "Target of automatic transmit power adjustment in dBm (-95 to -20, default = -70).",
            "default": "-70",
            "max_length": 7,
        },
        "power-mode": {
            "type": "option",
            "help": "Set radio effective isotropic radiated power (EIRP) in dBm or by a percentage of the maximum EIRP (default = percentage). This power takes into account both radio transmit power and antenna gain. Higher power level settings may be constrained by local regulatory requirements and AP capabilities.",
            "default": "percentage",
            "options": [{"help": "Set radio EIRP power in dBm.", "label": "Dbm", "name": "dBm"}, {"help": "Set radio EIRP power by percentage.", "label": "Percentage", "name": "percentage"}],
        },
        "power-level": {
            "type": "integer",
            "help": "Radio EIRP power level as a percentage of the maximum EIRP power (0 - 100, default = 100).",
            "default": 100,
            "min_value": 0,
            "max_value": 100,
        },
        "power-value": {
            "type": "integer",
            "help": "Radio EIRP power in dBm (1 - 33, default = 27).",
            "default": 27,
            "min_value": 1,
            "max_value": 33,
        },
        "override-vaps": {
            "type": "option",
            "help": "Enable to override WTP profile Virtual Access Point (VAP) settings.",
            "default": "disable",
            "options": [{"help": "Override WTP profile VAP settings.", "label": "Enable", "name": "enable"}, {"help": "Use WTP profile VAP settings.", "label": "Disable", "name": "disable"}],
        },
        "vap-all": {
            "type": "option",
            "help": "Configure method for assigning SSIDs to this FortiAP (default = automatically assign tunnel SSIDs).",
            "default": "tunnel",
            "options": [{"help": "Automatically select tunnel SSIDs.", "label": "Tunnel", "name": "tunnel"}, {"help": "Automatically select local-bridging SSIDs.", "label": "Bridge", "name": "bridge"}, {"help": "Manually select SSIDs.", "label": "Manual", "name": "manual"}],
        },
        "vaps": {
            "type": "string",
            "help": "Manually selected list of Virtual Access Points (VAPs).",
        },
        "override-channel": {
            "type": "option",
            "help": "Enable to override WTP profile channel settings.",
            "default": "disable",
            "options": [{"help": "Override WTP profile channel settings.", "label": "Enable", "name": "enable"}, {"help": "Use WTP profile channel settings.", "label": "Disable", "name": "disable"}],
        },
        "channel": {
            "type": "string",
            "help": "Selected list of wireless radio channels.",
        },
        "drma-manual-mode": {
            "type": "option",
            "help": "Radio mode to be used for DRMA manual mode (default = ncf).",
            "default": "ncf",
            "options": [{"help": "Set the radio to AP mode.", "label": "Ap", "name": "ap"}, {"help": "Set the radio to monitor mode", "label": "Monitor", "name": "monitor"}, {"help": "Select and set the radio mode based on NCF score.", "label": "Ncf", "name": "ncf"}, {"help": "Select the radio mode based on NCF score, but do not apply.", "label": "Ncf Peek", "name": "ncf-peek"}],
        },
    },
    "radio-2": {
        "override-band": {
            "type": "option",
            "help": "Enable to override the WTP profile band setting.",
            "default": "disable",
            "options": [{"help": "Override the WTP profile band setting.", "label": "Enable", "name": "enable"}, {"help": "Use the WTP profile band setting.", "label": "Disable", "name": "disable"}],
        },
        "band": {
            "type": "option",
            "help": "WiFi band that Radio 2 operates on.",
            "default": "",
            "options": [{"help": "802.11a.", "label": "802.11A", "name": "802.11a"}, {"help": "802.11b.", "label": "802.11B", "name": "802.11b"}, {"help": "802.11g.", "label": "802.11G", "name": "802.11g"}, {"help": "802.11n (WiFi 4) at 2.4GHz.", "label": "802.11N 2G", "name": "802.11n-2G"}, {"help": "802.11n (WiFi 4) at 5GHz.", "label": "802.11N 5G", "name": "802.11n-5G"}, {"help": "802.11ac (WiFi 5) at 2.4GHz.", "label": "802.11Ac 2G", "name": "802.11ac-2G"}, {"help": "802.11ac (WiFi 5) at 5GHz.", "label": "802.11Ac 5G", "name": "802.11ac-5G"}, {"help": "802.11ax (WiFi 6) at 2.4GHz.", "label": "802.11Ax 2G", "name": "802.11ax-2G"}, {"help": "802.11ax (WiFi 6) at 5GHz.", "label": "802.11Ax 5G", "name": "802.11ax-5G"}, {"help": "802.11ax (WiFi 6) at 6GHz.", "label": "802.11Ax 6G", "name": "802.11ax-6G"}, {"help": "802.11be (WiFi 7) at 2.4GHz.", "label": "802.11Be 2G", "name": "802.11be-2G"}, {"help": "802.11be (WiFi 7) at 5GHz.", "label": "802.11Be 5G", "name": "802.11be-5G"}, {"help": "802.11be (WiFi 7) at 6GHz.", "label": "802.11Be 6G", "name": "802.11be-6G"}],
        },
        "override-txpower": {
            "type": "option",
            "help": "Enable to override the WTP profile power level configuration.",
            "default": "disable",
            "options": [{"help": "Override the WTP profile power level configuration.", "label": "Enable", "name": "enable"}, {"help": "Use the WTP profile power level configuration.", "label": "Disable", "name": "disable"}],
        },
        "auto-power-level": {
            "type": "option",
            "help": "Enable/disable automatic power-level adjustment to prevent co-channel interference (default = enable).",
            "default": "disable",
            "options": [{"help": "Enable automatic transmit power adjustment.", "label": "Enable", "name": "enable"}, {"help": "Disable automatic transmit power adjustment.", "label": "Disable", "name": "disable"}],
        },
        "auto-power-high": {
            "type": "integer",
            "help": "The upper bound of automatic transmit power adjustment in dBm (the actual range of transmit power depends on the AP platform type).",
            "default": 17,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "auto-power-low": {
            "type": "integer",
            "help": "The lower bound of automatic transmit power adjustment in dBm (the actual range of transmit power depends on the AP platform type).",
            "default": 10,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "auto-power-target": {
            "type": "string",
            "help": "Target of automatic transmit power adjustment in dBm (-95 to -20, default = -70).",
            "default": "-70",
            "max_length": 7,
        },
        "power-mode": {
            "type": "option",
            "help": "Set radio effective isotropic radiated power (EIRP) in dBm or by a percentage of the maximum EIRP (default = percentage). This power takes into account both radio transmit power and antenna gain. Higher power level settings may be constrained by local regulatory requirements and AP capabilities.",
            "default": "percentage",
            "options": [{"help": "Set radio EIRP power in dBm.", "label": "Dbm", "name": "dBm"}, {"help": "Set radio EIRP power by percentage.", "label": "Percentage", "name": "percentage"}],
        },
        "power-level": {
            "type": "integer",
            "help": "Radio EIRP power level as a percentage of the maximum EIRP power (0 - 100, default = 100).",
            "default": 100,
            "min_value": 0,
            "max_value": 100,
        },
        "power-value": {
            "type": "integer",
            "help": "Radio EIRP power in dBm (1 - 33, default = 27).",
            "default": 27,
            "min_value": 1,
            "max_value": 33,
        },
        "override-vaps": {
            "type": "option",
            "help": "Enable to override WTP profile Virtual Access Point (VAP) settings.",
            "default": "disable",
            "options": [{"help": "Override WTP profile VAP settings.", "label": "Enable", "name": "enable"}, {"help": "Use WTP profile VAP settings.", "label": "Disable", "name": "disable"}],
        },
        "vap-all": {
            "type": "option",
            "help": "Configure method for assigning SSIDs to this FortiAP (default = automatically assign tunnel SSIDs).",
            "default": "tunnel",
            "options": [{"help": "Automatically select tunnel SSIDs.", "label": "Tunnel", "name": "tunnel"}, {"help": "Automatically select local-bridging SSIDs.", "label": "Bridge", "name": "bridge"}, {"help": "Manually select SSIDs.", "label": "Manual", "name": "manual"}],
        },
        "vaps": {
            "type": "string",
            "help": "Manually selected list of Virtual Access Points (VAPs).",
        },
        "override-channel": {
            "type": "option",
            "help": "Enable to override WTP profile channel settings.",
            "default": "disable",
            "options": [{"help": "Override WTP profile channel settings.", "label": "Enable", "name": "enable"}, {"help": "Use WTP profile channel settings.", "label": "Disable", "name": "disable"}],
        },
        "channel": {
            "type": "string",
            "help": "Selected list of wireless radio channels.",
        },
        "drma-manual-mode": {
            "type": "option",
            "help": "Radio mode to be used for DRMA manual mode (default = ncf).",
            "default": "ncf",
            "options": [{"help": "Set the radio to AP mode.", "label": "Ap", "name": "ap"}, {"help": "Set the radio to monitor mode", "label": "Monitor", "name": "monitor"}, {"help": "Select and set the radio mode based on NCF score.", "label": "Ncf", "name": "ncf"}, {"help": "Select the radio mode based on NCF score, but do not apply.", "label": "Ncf Peek", "name": "ncf-peek"}],
        },
    },
    "radio-3": {
        "override-band": {
            "type": "option",
            "help": "Enable to override the WTP profile band setting.",
            "default": "disable",
            "options": [{"help": "Override the WTP profile band setting.", "label": "Enable", "name": "enable"}, {"help": "Use the WTP profile band setting.", "label": "Disable", "name": "disable"}],
        },
        "band": {
            "type": "option",
            "help": "WiFi band that Radio 3 operates on.",
            "default": "",
            "options": [{"help": "802.11a.", "label": "802.11A", "name": "802.11a"}, {"help": "802.11b.", "label": "802.11B", "name": "802.11b"}, {"help": "802.11g.", "label": "802.11G", "name": "802.11g"}, {"help": "802.11n (WiFi 4) at 2.4GHz.", "label": "802.11N 2G", "name": "802.11n-2G"}, {"help": "802.11n (WiFi 4) at 5GHz.", "label": "802.11N 5G", "name": "802.11n-5G"}, {"help": "802.11ac (WiFi 5) at 2.4GHz.", "label": "802.11Ac 2G", "name": "802.11ac-2G"}, {"help": "802.11ac (WiFi 5) at 5GHz.", "label": "802.11Ac 5G", "name": "802.11ac-5G"}, {"help": "802.11ax (WiFi 6) at 2.4GHz.", "label": "802.11Ax 2G", "name": "802.11ax-2G"}, {"help": "802.11ax (WiFi 6) at 5GHz.", "label": "802.11Ax 5G", "name": "802.11ax-5G"}, {"help": "802.11ax (WiFi 6) at 6GHz.", "label": "802.11Ax 6G", "name": "802.11ax-6G"}, {"help": "802.11be (WiFi 7) at 2.4GHz.", "label": "802.11Be 2G", "name": "802.11be-2G"}, {"help": "802.11be (WiFi 7) at 5GHz.", "label": "802.11Be 5G", "name": "802.11be-5G"}, {"help": "802.11be (WiFi 7) at 6GHz.", "label": "802.11Be 6G", "name": "802.11be-6G"}],
        },
        "override-txpower": {
            "type": "option",
            "help": "Enable to override the WTP profile power level configuration.",
            "default": "disable",
            "options": [{"help": "Override the WTP profile power level configuration.", "label": "Enable", "name": "enable"}, {"help": "Use the WTP profile power level configuration.", "label": "Disable", "name": "disable"}],
        },
        "auto-power-level": {
            "type": "option",
            "help": "Enable/disable automatic power-level adjustment to prevent co-channel interference (default = enable).",
            "default": "disable",
            "options": [{"help": "Enable automatic transmit power adjustment.", "label": "Enable", "name": "enable"}, {"help": "Disable automatic transmit power adjustment.", "label": "Disable", "name": "disable"}],
        },
        "auto-power-high": {
            "type": "integer",
            "help": "The upper bound of automatic transmit power adjustment in dBm (the actual range of transmit power depends on the AP platform type).",
            "default": 17,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "auto-power-low": {
            "type": "integer",
            "help": "The lower bound of automatic transmit power adjustment in dBm (the actual range of transmit power depends on the AP platform type).",
            "default": 10,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "auto-power-target": {
            "type": "string",
            "help": "Target of automatic transmit power adjustment in dBm (-95 to -20, default = -70).",
            "default": "-70",
            "max_length": 7,
        },
        "power-mode": {
            "type": "option",
            "help": "Set radio effective isotropic radiated power (EIRP) in dBm or by a percentage of the maximum EIRP (default = percentage). This power takes into account both radio transmit power and antenna gain. Higher power level settings may be constrained by local regulatory requirements and AP capabilities.",
            "default": "percentage",
            "options": [{"help": "Set radio EIRP power in dBm.", "label": "Dbm", "name": "dBm"}, {"help": "Set radio EIRP power by percentage.", "label": "Percentage", "name": "percentage"}],
        },
        "power-level": {
            "type": "integer",
            "help": "Radio EIRP power level as a percentage of the maximum EIRP power (0 - 100, default = 100).",
            "default": 100,
            "min_value": 0,
            "max_value": 100,
        },
        "power-value": {
            "type": "integer",
            "help": "Radio EIRP power in dBm (1 - 33, default = 27).",
            "default": 27,
            "min_value": 1,
            "max_value": 33,
        },
        "override-vaps": {
            "type": "option",
            "help": "Enable to override WTP profile Virtual Access Point (VAP) settings.",
            "default": "disable",
            "options": [{"help": "Override WTP profile VAP settings.", "label": "Enable", "name": "enable"}, {"help": "Use WTP profile VAP settings.", "label": "Disable", "name": "disable"}],
        },
        "vap-all": {
            "type": "option",
            "help": "Configure method for assigning SSIDs to this FortiAP (default = automatically assign tunnel SSIDs).",
            "default": "tunnel",
            "options": [{"help": "Automatically select tunnel SSIDs.", "label": "Tunnel", "name": "tunnel"}, {"help": "Automatically select local-bridging SSIDs.", "label": "Bridge", "name": "bridge"}, {"help": "Manually select SSIDs.", "label": "Manual", "name": "manual"}],
        },
        "vaps": {
            "type": "string",
            "help": "Manually selected list of Virtual Access Points (VAPs).",
        },
        "override-channel": {
            "type": "option",
            "help": "Enable to override WTP profile channel settings.",
            "default": "disable",
            "options": [{"help": "Override WTP profile channel settings.", "label": "Enable", "name": "enable"}, {"help": "Use WTP profile channel settings.", "label": "Disable", "name": "disable"}],
        },
        "channel": {
            "type": "string",
            "help": "Selected list of wireless radio channels.",
        },
        "drma-manual-mode": {
            "type": "option",
            "help": "Radio mode to be used for DRMA manual mode (default = ncf).",
            "default": "ncf",
            "options": [{"help": "Set the radio to AP mode.", "label": "Ap", "name": "ap"}, {"help": "Set the radio to monitor mode", "label": "Monitor", "name": "monitor"}, {"help": "Select and set the radio mode based on NCF score.", "label": "Ncf", "name": "ncf"}, {"help": "Select the radio mode based on NCF score, but do not apply.", "label": "Ncf Peek", "name": "ncf-peek"}],
        },
    },
    "radio-4": {
        "override-band": {
            "type": "option",
            "help": "Enable to override the WTP profile band setting.",
            "default": "disable",
            "options": [{"help": "Override the WTP profile band setting.", "label": "Enable", "name": "enable"}, {"help": "Use the WTP profile band setting.", "label": "Disable", "name": "disable"}],
        },
        "band": {
            "type": "option",
            "help": "WiFi band that Radio 4 operates on.",
            "default": "",
            "options": [{"help": "802.11a.", "label": "802.11A", "name": "802.11a"}, {"help": "802.11b.", "label": "802.11B", "name": "802.11b"}, {"help": "802.11g.", "label": "802.11G", "name": "802.11g"}, {"help": "802.11n (WiFi 4) at 2.4GHz.", "label": "802.11N 2G", "name": "802.11n-2G"}, {"help": "802.11n (WiFi 4) at 5GHz.", "label": "802.11N 5G", "name": "802.11n-5G"}, {"help": "802.11ac (WiFi 5) at 2.4GHz.", "label": "802.11Ac 2G", "name": "802.11ac-2G"}, {"help": "802.11ac (WiFi 5) at 5GHz.", "label": "802.11Ac 5G", "name": "802.11ac-5G"}, {"help": "802.11ax (WiFi 6) at 2.4GHz.", "label": "802.11Ax 2G", "name": "802.11ax-2G"}, {"help": "802.11ax (WiFi 6) at 5GHz.", "label": "802.11Ax 5G", "name": "802.11ax-5G"}, {"help": "802.11ax (WiFi 6) at 6GHz.", "label": "802.11Ax 6G", "name": "802.11ax-6G"}, {"help": "802.11be (WiFi 7) at 2.4GHz.", "label": "802.11Be 2G", "name": "802.11be-2G"}, {"help": "802.11be (WiFi 7) at 5GHz.", "label": "802.11Be 5G", "name": "802.11be-5G"}, {"help": "802.11be (WiFi 7) at 6GHz.", "label": "802.11Be 6G", "name": "802.11be-6G"}],
        },
        "override-txpower": {
            "type": "option",
            "help": "Enable to override the WTP profile power level configuration.",
            "default": "disable",
            "options": [{"help": "Override the WTP profile power level configuration.", "label": "Enable", "name": "enable"}, {"help": "Use the WTP profile power level configuration.", "label": "Disable", "name": "disable"}],
        },
        "auto-power-level": {
            "type": "option",
            "help": "Enable/disable automatic power-level adjustment to prevent co-channel interference (default = enable).",
            "default": "disable",
            "options": [{"help": "Enable automatic transmit power adjustment.", "label": "Enable", "name": "enable"}, {"help": "Disable automatic transmit power adjustment.", "label": "Disable", "name": "disable"}],
        },
        "auto-power-high": {
            "type": "integer",
            "help": "The upper bound of automatic transmit power adjustment in dBm (the actual range of transmit power depends on the AP platform type).",
            "default": 17,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "auto-power-low": {
            "type": "integer",
            "help": "The lower bound of automatic transmit power adjustment in dBm (the actual range of transmit power depends on the AP platform type).",
            "default": 10,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "auto-power-target": {
            "type": "string",
            "help": "Target of automatic transmit power adjustment in dBm (-95 to -20, default = -70).",
            "default": "-70",
            "max_length": 7,
        },
        "power-mode": {
            "type": "option",
            "help": "Set radio effective isotropic radiated power (EIRP) in dBm or by a percentage of the maximum EIRP (default = percentage). This power takes into account both radio transmit power and antenna gain. Higher power level settings may be constrained by local regulatory requirements and AP capabilities.",
            "default": "percentage",
            "options": [{"help": "Set radio EIRP power in dBm.", "label": "Dbm", "name": "dBm"}, {"help": "Set radio EIRP power by percentage.", "label": "Percentage", "name": "percentage"}],
        },
        "power-level": {
            "type": "integer",
            "help": "Radio EIRP power level as a percentage of the maximum EIRP power (0 - 100, default = 100).",
            "default": 100,
            "min_value": 0,
            "max_value": 100,
        },
        "power-value": {
            "type": "integer",
            "help": "Radio EIRP power in dBm (1 - 33, default = 27).",
            "default": 27,
            "min_value": 1,
            "max_value": 33,
        },
        "override-vaps": {
            "type": "option",
            "help": "Enable to override WTP profile Virtual Access Point (VAP) settings.",
            "default": "disable",
            "options": [{"help": "Override WTP profile VAP settings.", "label": "Enable", "name": "enable"}, {"help": "Use WTP profile VAP settings.", "label": "Disable", "name": "disable"}],
        },
        "vap-all": {
            "type": "option",
            "help": "Configure method for assigning SSIDs to this FortiAP (default = automatically assign tunnel SSIDs).",
            "default": "tunnel",
            "options": [{"help": "Automatically select tunnel SSIDs.", "label": "Tunnel", "name": "tunnel"}, {"help": "Automatically select local-bridging SSIDs.", "label": "Bridge", "name": "bridge"}, {"help": "Manually select SSIDs.", "label": "Manual", "name": "manual"}],
        },
        "vaps": {
            "type": "string",
            "help": "Manually selected list of Virtual Access Points (VAPs).",
        },
        "override-channel": {
            "type": "option",
            "help": "Enable to override WTP profile channel settings.",
            "default": "disable",
            "options": [{"help": "Override WTP profile channel settings.", "label": "Enable", "name": "enable"}, {"help": "Use WTP profile channel settings.", "label": "Disable", "name": "disable"}],
        },
        "channel": {
            "type": "string",
            "help": "Selected list of wireless radio channels.",
        },
        "drma-manual-mode": {
            "type": "option",
            "help": "Radio mode to be used for DRMA manual mode (default = ncf).",
            "default": "ncf",
            "options": [{"help": "Set the radio to AP mode.", "label": "Ap", "name": "ap"}, {"help": "Set the radio to monitor mode", "label": "Monitor", "name": "monitor"}, {"help": "Select and set the radio mode based on NCF score.", "label": "Ncf", "name": "ncf"}, {"help": "Select the radio mode based on NCF score, but do not apply.", "label": "Ncf Peek", "name": "ncf-peek"}],
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_ADMIN = [
    "discovered",  # FortiGate wireless controller discovers the WTP, AP, or FortiAP though discovery or join request messages.
    "disable",  # FortiGate wireless controller is configured to not provide service to this WTP.
    "enable",  # FortiGate wireless controller is configured to provide service to this WTP.
]
VALID_BODY_FIRMWARE_PROVISION_LATEST = [
    "disable",  # Do not automatically provision the latest available firmware.
    "once",  # Automatically attempt a one-time upgrade to the latest available firmware version.
]
VALID_BODY_OVERRIDE_LED_STATE = [
    "enable",  # Override the WTP profile LED state.
    "disable",  # Use the WTP profile LED state.
]
VALID_BODY_LED_STATE = [
    "enable",  # Allow the LEDs on this FortiAP to light.
    "disable",  # Keep the LEDs on this FortiAP off.
]
VALID_BODY_OVERRIDE_WAN_PORT_MODE = [
    "enable",  # Override the WTP profile wan-port-mode.
    "disable",  # Use the wan-port-mode in the WTP profile.
]
VALID_BODY_WAN_PORT_MODE = [
    "wan-lan",  # Use the FortiAP WAN port as a LAN port.
    "wan-only",  # Do not use the WAN port as a LAN port.
]
VALID_BODY_OVERRIDE_IP_FRAGMENT = [
    "enable",  # Override the WTP profile IP fragment prevention setting.
    "disable",  # Use the WTP profile IP fragment prevention setting.
]
VALID_BODY_IP_FRAGMENT_PREVENTING = [
    "tcp-mss-adjust",  # TCP maximum segment size adjustment.
    "icmp-unreachable",  # Drop packet and send ICMP Destination Unreachable
]
VALID_BODY_OVERRIDE_SPLIT_TUNNEL = [
    "enable",  # Override the WTP profile split tunneling setting.
    "disable",  # Use the WTP profile split tunneling setting.
]
VALID_BODY_SPLIT_TUNNELING_ACL_PATH = [
    "tunnel",  # Split tunneling ACL list traffic will be tunnel.
    "local",  # Split tunneling ACL list traffic will be local NATed.
]
VALID_BODY_SPLIT_TUNNELING_ACL_LOCAL_AP_SUBNET = [
    "enable",  # Enable automatically adding local subnetwork of FortiAP to split-tunneling ACL.
    "disable",  # Disable automatically adding local subnetwork of FortiAP to split-tunneling ACL.
]
VALID_BODY_OVERRIDE_LAN = [
    "enable",  # Override the WTP profile LAN port setting.
    "disable",  # Use the WTP profile LAN port setting.
]
VALID_BODY_OVERRIDE_ALLOWACCESS = [
    "enable",  # Override the WTP profile management access configuration.
    "disable",  # Use the WTP profile management access configuration.
]
VALID_BODY_ALLOWACCESS = [
    "https",  # HTTPS access.
    "ssh",  # SSH access.
    "snmp",  # SNMP access.
]
VALID_BODY_OVERRIDE_LOGIN_PASSWD_CHANGE = [
    "enable",  # Override the WTP profile login-password (administrator password) setting.
    "disable",  # Use the the WTP profile login-password (administrator password) setting.
]
VALID_BODY_LOGIN_PASSWD_CHANGE = [
    "yes",  # Change the managed WTP, FortiAP or AP's administrator password. Use the login-password option to set the password.
    "default",  # Keep the managed WTP, FortiAP or AP's administrator password set to the factory default.
    "no",  # Do not change the managed WTP, FortiAP or AP's administrator password.
]
VALID_BODY_OVERRIDE_DEFAULT_MESH_ROOT = [
    "enable",  # Override the WTP profile default mesh root SSID setting.
    "disable",  # Use the WTP profile default mesh root SSID setting.
]
VALID_BODY_DEFAULT_MESH_ROOT = [
    "enable",  # Enable default mesh root SSID if it is not included by radio's SSID configuration.
    "disable",  # Do not enable default mesh root SSID if it is not included by radio's SSID configuration.
]
VALID_BODY_IMAGE_DOWNLOAD = [
    "enable",  # Enable WTP image download at join time.
    "disable",  # Disable WTP image download at join time.
]
VALID_BODY_MESH_BRIDGE_ENABLE = [
    "default",  # Use mesh Ethernet bridge local setting on the WTP.
    "enable",  # Turn on mesh Ethernet bridge on the WTP.
    "disable",  # Turn off mesh Ethernet bridge on the WTP.
]
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
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_wireless_controller_wtp_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for wireless_controller/wtp.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_wireless_controller_wtp_get()
        >>> assert is_valid == True
        
        >>> # Valid - Get specific item by wtp-id
        >>> is_valid, error = validate_wireless_controller_wtp_get(wtp_id="test-item")
        >>> assert is_valid == True
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_wireless_controller_wtp_get(
        ...     filters={"format": "name|type"}
        ... )
        >>> assert is_valid == True
    """
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
    """
    Validate required fields for wireless_controller/wtp.

    This validator checks:
    1. Always-required fields are present
    2. Mutually exclusive groups have at least one field

    Args:
        payload: The request payload to validate

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "test"}
        >>> is_valid, error = validate_required_fields(payload)
    """
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


def validate_wireless_controller_wtp_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new wireless_controller/wtp object.

    This validator performs two-stage validation:
    1. Required fields check (schema-based)
    2. Field value validation (enums, ranges, formats)

    Args:
        payload: Request body data with configuration
        **params: Query parameters (vdom, etc.)

    Returns:
        Tuple of (is_valid, error_message)
        - is_valid: True if payload is valid, False otherwise
        - error_message: None if valid, detailed error string if invalid

    Examples:
        >>> # ✅ Valid - Minimal required fields
        >>> payload = {
        ...     "wtp-id": True,  # WTP ID.
        ...     "wtp-profile": True,  # WTP profile name to apply to this WTP, AP or Forti
        ... }
        >>> is_valid, error = validate_wireless_controller_wtp_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "wtp-id": True,
        ...     "admin": "{'name': 'discovered', 'help': 'FortiGate wireless controller discovers the WTP, AP, or FortiAP though discovery or join request messages.', 'label': 'Discovered', 'description': 'FortiGate wireless controller discovers the WTP, AP, or FortiAP though discovery or join request messages'}",  # Valid enum value
        ... }
        >>> is_valid, error = validate_wireless_controller_wtp_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["admin"] = "invalid-value"
        >>> is_valid, error = validate_wireless_controller_wtp_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_wireless_controller_wtp_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "admin" in payload:
        value = payload["admin"]
        if value not in VALID_BODY_ADMIN:
            desc = FIELD_DESCRIPTIONS.get("admin", "")
            error_msg = f"Invalid value for 'admin': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADMIN)}"
            error_msg += f"\n  → Example: admin='{{ VALID_BODY_ADMIN[0] }}'"
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
    if "override-led-state" in payload:
        value = payload["override-led-state"]
        if value not in VALID_BODY_OVERRIDE_LED_STATE:
            desc = FIELD_DESCRIPTIONS.get("override-led-state", "")
            error_msg = f"Invalid value for 'override-led-state': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OVERRIDE_LED_STATE)}"
            error_msg += f"\n  → Example: override-led-state='{{ VALID_BODY_OVERRIDE_LED_STATE[0] }}'"
            return (False, error_msg)
    if "led-state" in payload:
        value = payload["led-state"]
        if value not in VALID_BODY_LED_STATE:
            desc = FIELD_DESCRIPTIONS.get("led-state", "")
            error_msg = f"Invalid value for 'led-state': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LED_STATE)}"
            error_msg += f"\n  → Example: led-state='{{ VALID_BODY_LED_STATE[0] }}'"
            return (False, error_msg)
    if "override-wan-port-mode" in payload:
        value = payload["override-wan-port-mode"]
        if value not in VALID_BODY_OVERRIDE_WAN_PORT_MODE:
            desc = FIELD_DESCRIPTIONS.get("override-wan-port-mode", "")
            error_msg = f"Invalid value for 'override-wan-port-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OVERRIDE_WAN_PORT_MODE)}"
            error_msg += f"\n  → Example: override-wan-port-mode='{{ VALID_BODY_OVERRIDE_WAN_PORT_MODE[0] }}'"
            return (False, error_msg)
    if "wan-port-mode" in payload:
        value = payload["wan-port-mode"]
        if value not in VALID_BODY_WAN_PORT_MODE:
            desc = FIELD_DESCRIPTIONS.get("wan-port-mode", "")
            error_msg = f"Invalid value for 'wan-port-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WAN_PORT_MODE)}"
            error_msg += f"\n  → Example: wan-port-mode='{{ VALID_BODY_WAN_PORT_MODE[0] }}'"
            return (False, error_msg)
    if "override-ip-fragment" in payload:
        value = payload["override-ip-fragment"]
        if value not in VALID_BODY_OVERRIDE_IP_FRAGMENT:
            desc = FIELD_DESCRIPTIONS.get("override-ip-fragment", "")
            error_msg = f"Invalid value for 'override-ip-fragment': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OVERRIDE_IP_FRAGMENT)}"
            error_msg += f"\n  → Example: override-ip-fragment='{{ VALID_BODY_OVERRIDE_IP_FRAGMENT[0] }}'"
            return (False, error_msg)
    if "ip-fragment-preventing" in payload:
        value = payload["ip-fragment-preventing"]
        if value not in VALID_BODY_IP_FRAGMENT_PREVENTING:
            desc = FIELD_DESCRIPTIONS.get("ip-fragment-preventing", "")
            error_msg = f"Invalid value for 'ip-fragment-preventing': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IP_FRAGMENT_PREVENTING)}"
            error_msg += f"\n  → Example: ip-fragment-preventing='{{ VALID_BODY_IP_FRAGMENT_PREVENTING[0] }}'"
            return (False, error_msg)
    if "override-split-tunnel" in payload:
        value = payload["override-split-tunnel"]
        if value not in VALID_BODY_OVERRIDE_SPLIT_TUNNEL:
            desc = FIELD_DESCRIPTIONS.get("override-split-tunnel", "")
            error_msg = f"Invalid value for 'override-split-tunnel': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OVERRIDE_SPLIT_TUNNEL)}"
            error_msg += f"\n  → Example: override-split-tunnel='{{ VALID_BODY_OVERRIDE_SPLIT_TUNNEL[0] }}'"
            return (False, error_msg)
    if "split-tunneling-acl-path" in payload:
        value = payload["split-tunneling-acl-path"]
        if value not in VALID_BODY_SPLIT_TUNNELING_ACL_PATH:
            desc = FIELD_DESCRIPTIONS.get("split-tunneling-acl-path", "")
            error_msg = f"Invalid value for 'split-tunneling-acl-path': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SPLIT_TUNNELING_ACL_PATH)}"
            error_msg += f"\n  → Example: split-tunneling-acl-path='{{ VALID_BODY_SPLIT_TUNNELING_ACL_PATH[0] }}'"
            return (False, error_msg)
    if "split-tunneling-acl-local-ap-subnet" in payload:
        value = payload["split-tunneling-acl-local-ap-subnet"]
        if value not in VALID_BODY_SPLIT_TUNNELING_ACL_LOCAL_AP_SUBNET:
            desc = FIELD_DESCRIPTIONS.get("split-tunneling-acl-local-ap-subnet", "")
            error_msg = f"Invalid value for 'split-tunneling-acl-local-ap-subnet': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SPLIT_TUNNELING_ACL_LOCAL_AP_SUBNET)}"
            error_msg += f"\n  → Example: split-tunneling-acl-local-ap-subnet='{{ VALID_BODY_SPLIT_TUNNELING_ACL_LOCAL_AP_SUBNET[0] }}'"
            return (False, error_msg)
    if "override-lan" in payload:
        value = payload["override-lan"]
        if value not in VALID_BODY_OVERRIDE_LAN:
            desc = FIELD_DESCRIPTIONS.get("override-lan", "")
            error_msg = f"Invalid value for 'override-lan': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OVERRIDE_LAN)}"
            error_msg += f"\n  → Example: override-lan='{{ VALID_BODY_OVERRIDE_LAN[0] }}'"
            return (False, error_msg)
    if "override-allowaccess" in payload:
        value = payload["override-allowaccess"]
        if value not in VALID_BODY_OVERRIDE_ALLOWACCESS:
            desc = FIELD_DESCRIPTIONS.get("override-allowaccess", "")
            error_msg = f"Invalid value for 'override-allowaccess': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OVERRIDE_ALLOWACCESS)}"
            error_msg += f"\n  → Example: override-allowaccess='{{ VALID_BODY_OVERRIDE_ALLOWACCESS[0] }}'"
            return (False, error_msg)
    if "allowaccess" in payload:
        value = payload["allowaccess"]
        if value not in VALID_BODY_ALLOWACCESS:
            desc = FIELD_DESCRIPTIONS.get("allowaccess", "")
            error_msg = f"Invalid value for 'allowaccess': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ALLOWACCESS)}"
            error_msg += f"\n  → Example: allowaccess='{{ VALID_BODY_ALLOWACCESS[0] }}'"
            return (False, error_msg)
    if "override-login-passwd-change" in payload:
        value = payload["override-login-passwd-change"]
        if value not in VALID_BODY_OVERRIDE_LOGIN_PASSWD_CHANGE:
            desc = FIELD_DESCRIPTIONS.get("override-login-passwd-change", "")
            error_msg = f"Invalid value for 'override-login-passwd-change': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OVERRIDE_LOGIN_PASSWD_CHANGE)}"
            error_msg += f"\n  → Example: override-login-passwd-change='{{ VALID_BODY_OVERRIDE_LOGIN_PASSWD_CHANGE[0] }}'"
            return (False, error_msg)
    if "login-passwd-change" in payload:
        value = payload["login-passwd-change"]
        if value not in VALID_BODY_LOGIN_PASSWD_CHANGE:
            desc = FIELD_DESCRIPTIONS.get("login-passwd-change", "")
            error_msg = f"Invalid value for 'login-passwd-change': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOGIN_PASSWD_CHANGE)}"
            error_msg += f"\n  → Example: login-passwd-change='{{ VALID_BODY_LOGIN_PASSWD_CHANGE[0] }}'"
            return (False, error_msg)
    if "override-default-mesh-root" in payload:
        value = payload["override-default-mesh-root"]
        if value not in VALID_BODY_OVERRIDE_DEFAULT_MESH_ROOT:
            desc = FIELD_DESCRIPTIONS.get("override-default-mesh-root", "")
            error_msg = f"Invalid value for 'override-default-mesh-root': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OVERRIDE_DEFAULT_MESH_ROOT)}"
            error_msg += f"\n  → Example: override-default-mesh-root='{{ VALID_BODY_OVERRIDE_DEFAULT_MESH_ROOT[0] }}'"
            return (False, error_msg)
    if "default-mesh-root" in payload:
        value = payload["default-mesh-root"]
        if value not in VALID_BODY_DEFAULT_MESH_ROOT:
            desc = FIELD_DESCRIPTIONS.get("default-mesh-root", "")
            error_msg = f"Invalid value for 'default-mesh-root': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DEFAULT_MESH_ROOT)}"
            error_msg += f"\n  → Example: default-mesh-root='{{ VALID_BODY_DEFAULT_MESH_ROOT[0] }}'"
            return (False, error_msg)
    if "image-download" in payload:
        value = payload["image-download"]
        if value not in VALID_BODY_IMAGE_DOWNLOAD:
            desc = FIELD_DESCRIPTIONS.get("image-download", "")
            error_msg = f"Invalid value for 'image-download': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IMAGE_DOWNLOAD)}"
            error_msg += f"\n  → Example: image-download='{{ VALID_BODY_IMAGE_DOWNLOAD[0] }}'"
            return (False, error_msg)
    if "mesh-bridge-enable" in payload:
        value = payload["mesh-bridge-enable"]
        if value not in VALID_BODY_MESH_BRIDGE_ENABLE:
            desc = FIELD_DESCRIPTIONS.get("mesh-bridge-enable", "")
            error_msg = f"Invalid value for 'mesh-bridge-enable': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MESH_BRIDGE_ENABLE)}"
            error_msg += f"\n  → Example: mesh-bridge-enable='{{ VALID_BODY_MESH_BRIDGE_ENABLE[0] }}'"
            return (False, error_msg)
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

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_wireless_controller_wtp_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update wireless_controller/wtp.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_wireless_controller_wtp_put(payload)
    """
    # Step 1: Validate enum values
    if "admin" in payload:
        value = payload["admin"]
        if value not in VALID_BODY_ADMIN:
            return (
                False,
                f"Invalid value for 'admin'='{value}'. Must be one of: {', '.join(VALID_BODY_ADMIN)}",
            )
    if "firmware-provision-latest" in payload:
        value = payload["firmware-provision-latest"]
        if value not in VALID_BODY_FIRMWARE_PROVISION_LATEST:
            return (
                False,
                f"Invalid value for 'firmware-provision-latest'='{value}'. Must be one of: {', '.join(VALID_BODY_FIRMWARE_PROVISION_LATEST)}",
            )
    if "override-led-state" in payload:
        value = payload["override-led-state"]
        if value not in VALID_BODY_OVERRIDE_LED_STATE:
            return (
                False,
                f"Invalid value for 'override-led-state'='{value}'. Must be one of: {', '.join(VALID_BODY_OVERRIDE_LED_STATE)}",
            )
    if "led-state" in payload:
        value = payload["led-state"]
        if value not in VALID_BODY_LED_STATE:
            return (
                False,
                f"Invalid value for 'led-state'='{value}'. Must be one of: {', '.join(VALID_BODY_LED_STATE)}",
            )
    if "override-wan-port-mode" in payload:
        value = payload["override-wan-port-mode"]
        if value not in VALID_BODY_OVERRIDE_WAN_PORT_MODE:
            return (
                False,
                f"Invalid value for 'override-wan-port-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_OVERRIDE_WAN_PORT_MODE)}",
            )
    if "wan-port-mode" in payload:
        value = payload["wan-port-mode"]
        if value not in VALID_BODY_WAN_PORT_MODE:
            return (
                False,
                f"Invalid value for 'wan-port-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_WAN_PORT_MODE)}",
            )
    if "override-ip-fragment" in payload:
        value = payload["override-ip-fragment"]
        if value not in VALID_BODY_OVERRIDE_IP_FRAGMENT:
            return (
                False,
                f"Invalid value for 'override-ip-fragment'='{value}'. Must be one of: {', '.join(VALID_BODY_OVERRIDE_IP_FRAGMENT)}",
            )
    if "ip-fragment-preventing" in payload:
        value = payload["ip-fragment-preventing"]
        if value not in VALID_BODY_IP_FRAGMENT_PREVENTING:
            return (
                False,
                f"Invalid value for 'ip-fragment-preventing'='{value}'. Must be one of: {', '.join(VALID_BODY_IP_FRAGMENT_PREVENTING)}",
            )
    if "override-split-tunnel" in payload:
        value = payload["override-split-tunnel"]
        if value not in VALID_BODY_OVERRIDE_SPLIT_TUNNEL:
            return (
                False,
                f"Invalid value for 'override-split-tunnel'='{value}'. Must be one of: {', '.join(VALID_BODY_OVERRIDE_SPLIT_TUNNEL)}",
            )
    if "split-tunneling-acl-path" in payload:
        value = payload["split-tunneling-acl-path"]
        if value not in VALID_BODY_SPLIT_TUNNELING_ACL_PATH:
            return (
                False,
                f"Invalid value for 'split-tunneling-acl-path'='{value}'. Must be one of: {', '.join(VALID_BODY_SPLIT_TUNNELING_ACL_PATH)}",
            )
    if "split-tunneling-acl-local-ap-subnet" in payload:
        value = payload["split-tunneling-acl-local-ap-subnet"]
        if value not in VALID_BODY_SPLIT_TUNNELING_ACL_LOCAL_AP_SUBNET:
            return (
                False,
                f"Invalid value for 'split-tunneling-acl-local-ap-subnet'='{value}'. Must be one of: {', '.join(VALID_BODY_SPLIT_TUNNELING_ACL_LOCAL_AP_SUBNET)}",
            )
    if "override-lan" in payload:
        value = payload["override-lan"]
        if value not in VALID_BODY_OVERRIDE_LAN:
            return (
                False,
                f"Invalid value for 'override-lan'='{value}'. Must be one of: {', '.join(VALID_BODY_OVERRIDE_LAN)}",
            )
    if "override-allowaccess" in payload:
        value = payload["override-allowaccess"]
        if value not in VALID_BODY_OVERRIDE_ALLOWACCESS:
            return (
                False,
                f"Invalid value for 'override-allowaccess'='{value}'. Must be one of: {', '.join(VALID_BODY_OVERRIDE_ALLOWACCESS)}",
            )
    if "allowaccess" in payload:
        value = payload["allowaccess"]
        if value not in VALID_BODY_ALLOWACCESS:
            return (
                False,
                f"Invalid value for 'allowaccess'='{value}'. Must be one of: {', '.join(VALID_BODY_ALLOWACCESS)}",
            )
    if "override-login-passwd-change" in payload:
        value = payload["override-login-passwd-change"]
        if value not in VALID_BODY_OVERRIDE_LOGIN_PASSWD_CHANGE:
            return (
                False,
                f"Invalid value for 'override-login-passwd-change'='{value}'. Must be one of: {', '.join(VALID_BODY_OVERRIDE_LOGIN_PASSWD_CHANGE)}",
            )
    if "login-passwd-change" in payload:
        value = payload["login-passwd-change"]
        if value not in VALID_BODY_LOGIN_PASSWD_CHANGE:
            return (
                False,
                f"Invalid value for 'login-passwd-change'='{value}'. Must be one of: {', '.join(VALID_BODY_LOGIN_PASSWD_CHANGE)}",
            )
    if "override-default-mesh-root" in payload:
        value = payload["override-default-mesh-root"]
        if value not in VALID_BODY_OVERRIDE_DEFAULT_MESH_ROOT:
            return (
                False,
                f"Invalid value for 'override-default-mesh-root'='{value}'. Must be one of: {', '.join(VALID_BODY_OVERRIDE_DEFAULT_MESH_ROOT)}",
            )
    if "default-mesh-root" in payload:
        value = payload["default-mesh-root"]
        if value not in VALID_BODY_DEFAULT_MESH_ROOT:
            return (
                False,
                f"Invalid value for 'default-mesh-root'='{value}'. Must be one of: {', '.join(VALID_BODY_DEFAULT_MESH_ROOT)}",
            )
    if "image-download" in payload:
        value = payload["image-download"]
        if value not in VALID_BODY_IMAGE_DOWNLOAD:
            return (
                False,
                f"Invalid value for 'image-download'='{value}'. Must be one of: {', '.join(VALID_BODY_IMAGE_DOWNLOAD)}",
            )
    if "mesh-bridge-enable" in payload:
        value = payload["mesh-bridge-enable"]
        if value not in VALID_BODY_MESH_BRIDGE_ENABLE:
            return (
                False,
                f"Invalid value for 'mesh-bridge-enable'='{value}'. Must be one of: {', '.join(VALID_BODY_MESH_BRIDGE_ENABLE)}",
            )
    if "purdue-level" in payload:
        value = payload["purdue-level"]
        if value not in VALID_BODY_PURDUE_LEVEL:
            return (
                False,
                f"Invalid value for 'purdue-level'='{value}'. Must be one of: {', '.join(VALID_BODY_PURDUE_LEVEL)}",
            )

    return (True, None)


# ============================================================================
# Metadata Access Functions
# Provide programmatic access to field metadata for IDE autocomplete,
# documentation generation, and dynamic validation
# ============================================================================


def get_field_description(field_name: str) -> str | None:
    """
    Get description/help text for a field.

    Args:
        field_name: Name of the field

    Returns:
        Description text or None if field doesn't exist

    Example:
        >>> desc = get_field_description("name")
        >>> print(desc)
    """
    return FIELD_DESCRIPTIONS.get(field_name)


def get_field_type(field_name: str) -> str | None:
    """
    Get the type of a field.

    Args:
        field_name: Name of the field

    Returns:
        Field type (e.g., "string", "integer", "option") or None

    Example:
        >>> field_type = get_field_type("status")
        >>> print(field_type)  # "option"
    """
    return FIELD_TYPES.get(field_name)


def get_field_constraints(field_name: str) -> dict[str, Any] | None:
    """
    Get constraints for a field (min/max values, string length).

    Args:
        field_name: Name of the field

    Returns:
        Constraint dict or None

    Example:
        >>> constraints = get_field_constraints("port")
        >>> print(constraints)  # {"type": "integer", "min": 1, "max": 65535}
    """
    return FIELD_CONSTRAINTS.get(field_name)


def get_field_default(field_name: str) -> Any | None:
    """
    Get default value for a field.

    Args:
        field_name: Name of the field

    Returns:
        Default value or None if no default

    Example:
        >>> default = get_field_default("status")
        >>> print(default)  # "enable"
    """
    return FIELDS_WITH_DEFAULTS.get(field_name)


def get_field_options(field_name: str) -> list[str] | None:
    """
    Get valid enum options for a field.

    Args:
        field_name: Name of the field

    Returns:
        List of valid values or None if not an enum field

    Example:
        >>> options = get_field_options("status")
        >>> print(options)  # ["enable", "disable"]
    """
    # Construct the constant name from field name
    # Replace all non-alphanumeric characters with underscores for valid Python identifiers
    import re
    safe_name = re.sub(r'[^a-zA-Z0-9]', '_', field_name)
    constant_name = f"VALID_BODY_{safe_name.upper()}"
    return globals().get(constant_name)


def get_nested_schema(field_name: str) -> dict[str, Any] | None:
    """
    Get schema for nested table/list fields.

    Args:
        field_name: Name of the parent field

    Returns:
        Dict mapping child field names to their metadata

    Example:
        >>> nested = get_nested_schema("members")
        >>> if nested:
        ...     for child_field, child_meta in nested.items():
        ...         print(f"{child_field}: {child_meta['type']}")
    """
    return NESTED_SCHEMAS.get(field_name)


def get_all_fields() -> list[str]:
    """
    Get list of all field names.

    Returns:
        List of all field names in the schema

    Example:
        >>> fields = get_all_fields()
        >>> print(len(fields))
    """
    return list(FIELD_TYPES.keys())


def get_field_metadata(field_name: str) -> dict[str, Any] | None:
    """
    Get complete metadata for a field (type, description, constraints, defaults, options).

    Args:
        field_name: Name of the field

    Returns:
        Dict with all available metadata or None if field doesn't exist

    Example:
        >>> meta = get_field_metadata("status")
        >>> print(meta)
        >>> # {
        >>> #   "type": "option",
        >>> #   "description": "Enable/disable this feature",
        >>> #   "default": "enable",
        >>> #   "options": ["enable", "disable"]
        >>> # }
    """
    if field_name not in FIELD_TYPES:
        return None

    metadata = {
        "name": field_name,
        "type": FIELD_TYPES[field_name],
    }

    # Add description if available
    if field_name in FIELD_DESCRIPTIONS:
        metadata["description"] = FIELD_DESCRIPTIONS[field_name]

    # Add constraints if available
    if field_name in FIELD_CONSTRAINTS:
        metadata["constraints"] = FIELD_CONSTRAINTS[field_name]

    # Add default if available
    if field_name in FIELDS_WITH_DEFAULTS:
        metadata["default"] = FIELDS_WITH_DEFAULTS[field_name]

    # Add required flag
    metadata["required"] = field_name in REQUIRED_FIELDS

    # Add options if available
    options = get_field_options(field_name)
    if options:
        metadata["options"] = options

    # Add nested schema if available
    nested = get_nested_schema(field_name)
    if nested:
        metadata["nested_schema"] = nested

    return metadata


def validate_field_value(field_name: str, value: Any) -> tuple[bool, str | None]:
    """
    Validate a single field value against its constraints.

    Args:
        field_name: Name of the field
        value: Value to validate

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> is_valid, error = validate_field_value("status", "enable")
        >>> if not is_valid:
        ...     print(error)
    """
    # Get field metadata
    field_type = get_field_type(field_name)
    if field_type is None:
        return (False, f"Unknown field: '{field_name}' (not defined in schema)")

    # Get field description for better error context
    description = get_field_description(field_name)

    # Validate enum values
    options = get_field_options(field_name)
    if options and value not in options:
        error_msg = f"Invalid value for '{field_name}': {repr(value)}"
        if description:
            error_msg += f"\n  → Description: {description}"
        error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in options)}"
        if options:
            error_msg += f"\n  → Example: {field_name}={repr(options[0])}"
        return (False, error_msg)

    # Validate constraints
    constraints = get_field_constraints(field_name)
    if constraints:
        constraint_type = constraints.get("type")

        if constraint_type == "integer":
            if not isinstance(value, int):
                error_msg = f"Field '{field_name}' must be an integer"
                if description:
                    error_msg += f"\n  → Description: {description}"
                error_msg += f"\n  → You provided: {type(value).__name__} = {repr(value)}"
                return (False, error_msg)

            min_val = constraints.get("min")
            max_val = constraints.get("max")

            if min_val is not None and value < min_val:
                error_msg = f"Field '{field_name}' value {value} is below minimum {min_val}"
                if description:
                    error_msg += f"\n  → Description: {description}"
                if max_val is not None:
                    error_msg += f"\n  → Valid range: {min_val} to {max_val}"
                return (False, error_msg)

            if max_val is not None and value > max_val:
                error_msg = f"Field '{field_name}' value {value} exceeds maximum {max_val}"
                if description:
                    error_msg += f"\n  → Description: {description}"
                if min_val is not None:
                    error_msg += f"\n  → Valid range: {min_val} to {max_val}"
                return (False, error_msg)

        elif constraint_type == "string":
            if not isinstance(value, str):
                error_msg = f"Field '{field_name}' must be a string"
                if description:
                    error_msg += f"\n  → Description: {description}"
                error_msg += f"\n  → You provided: {type(value).__name__} = {repr(value)}"
                return (False, error_msg)

            max_length = constraints.get("max_length")
            if max_length and len(value) > max_length:
                error_msg = f"Field '{field_name}' length {len(value)} exceeds maximum {max_length}"
                if description:
                    error_msg += f"\n  → Description: {description}"
                error_msg += f"\n  → Your value: {repr(value[:50])}{'...' if len(value) > 50 else ''}"
                return (False, error_msg)

    return (True, None)


# ============================================================================
# Schema Information
# Metadata about this endpoint schema
# ============================================================================

SCHEMA_INFO = {
    "endpoint": "wireless_controller/wtp",
    "category": "cmdb",
    "api_path": "wireless-controller/wtp",
    "mkey": "wtp-id",
    "mkey_type": "string",
    "help": "Configure Wireless Termination Points (WTPs), that is, FortiAPs or APs to be managed by FortiGate.",
    "total_fields": 47,
    "required_fields_count": 2,
    "fields_with_defaults_count": 39,
}


def get_schema_info() -> dict[str, Any]:
    """
    Get information about this endpoint schema.

    Returns:
        Dict with schema metadata

    Example:
        >>> info = get_schema_info()
        >>> print(f"Endpoint: {info['endpoint']}")
        >>> print(f"Total fields: {info['total_fields']}")
    """
    return SCHEMA_INFO.copy()
