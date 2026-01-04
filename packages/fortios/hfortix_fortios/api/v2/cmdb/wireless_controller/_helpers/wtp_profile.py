"""
Validation helpers for wireless_controller/wtp_profile endpoint.

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
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "control-message-offload": "ebp-frame aeroscout-tag ap-list sta-list sta-cap-list stats aeroscout-mu sta-health spectral-analysis",
    "bonjour-profile": "",
    "apcfg-profile": "",
    "apcfg-mesh": "disable",
    "apcfg-mesh-ap-type": "ethernet",
    "apcfg-mesh-ssid": "",
    "apcfg-mesh-eth-bridge": "disable",
    "ble-profile": "",
    "syslog-profile": "",
    "wan-port-mode": "wan-only",
    "energy-efficient-ethernet": "disable",
    "led-state": "enable",
    "dtls-policy": "clear-text",
    "dtls-in-kernel": "disable",
    "max-clients": 0,
    "handoff-rssi": 25,
    "handoff-sta-thresh": 0,
    "handoff-roaming": "enable",
    "ap-country": "--",
    "ip-fragment-preventing": "tcp-mss-adjust",
    "tun-mtu-uplink": 0,
    "tun-mtu-downlink": 0,
    "split-tunneling-acl-path": "local",
    "split-tunneling-acl-local-ap-subnet": "disable",
    "allowaccess": "",
    "login-passwd-change": "no",
    "lldp": "enable",
    "poe-mode": "auto",
    "usb-port": "enable",
    "frequency-handoff": "disable",
    "ap-handoff": "disable",
    "default-mesh-root": "disable",
    "ext-info-enable": "enable",
    "indoor-outdoor-deployment": "platform-determined",
    "console-login": "enable",
    "wan-port-auth": "none",
    "wan-port-auth-usrname": "",
    "wan-port-auth-methods": "all",
    "wan-port-auth-macsec": "disable",
    "unii-4-5ghz-band": "disable",
    "admin-auth-tacacs+": "",
    "admin-restrict-local": "disable",
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
    "name": "string",  # WTP (or FortiAP or AP) profile name.
    "comment": "var-string",  # Comment.
    "platform": "string",  # WTP, FortiAP, or AP platform.
    "control-message-offload": "option",  # Enable/disable CAPWAP control message data channel offload.
    "bonjour-profile": "string",  # Bonjour profile name.
    "apcfg-profile": "string",  # AP local configuration profile name.
    "apcfg-mesh": "option",  # Enable/disable AP local mesh configuration (default = disabl
    "apcfg-mesh-ap-type": "option",  # Mesh AP Type (default = ethernet).
    "apcfg-mesh-ssid": "string",  #  Mesh SSID (default = none).
    "apcfg-mesh-eth-bridge": "option",  # Enable/disable mesh ethernet bridge (default = disable).
    "ble-profile": "string",  # Bluetooth Low Energy profile name.
    "syslog-profile": "string",  # System log server configuration profile name.
    "wan-port-mode": "option",  # Enable/disable using a WAN port as a LAN port.
    "lan": "string",  # WTP LAN port mapping.
    "energy-efficient-ethernet": "option",  # Enable/disable use of energy efficient Ethernet on WTP.
    "led-state": "option",  # Enable/disable use of LEDs on WTP (default = enable).
    "led-schedules": "string",  # Recurring firewall schedules for illuminating LEDs on the Fo
    "dtls-policy": "option",  # WTP data channel DTLS policy (default = clear-text).
    "dtls-in-kernel": "option",  # Enable/disable data channel DTLS in kernel.
    "max-clients": "integer",  # Maximum number of stations (STAs) supported by the WTP (defa
    "handoff-rssi": "integer",  # Minimum received signal strength indicator (RSSI) value for 
    "handoff-sta-thresh": "integer",  # Threshold value for AP handoff.
    "handoff-roaming": "option",  # Enable/disable client load balancing during roaming to avoid
    "deny-mac-list": "string",  # List of MAC addresses that are denied access to this WTP, Fo
    "ap-country": "option",  # Country in which this WTP, FortiAP, or AP will operate (defa
    "ip-fragment-preventing": "option",  # Method(s) by which IP fragmentation is prevented for control
    "tun-mtu-uplink": "integer",  # The maximum transmission unit (MTU) of uplink CAPWAP tunnel 
    "tun-mtu-downlink": "integer",  # The MTU of downlink CAPWAP tunnel (576 - 1500 bytes or 0; 0 
    "split-tunneling-acl-path": "option",  # Split tunneling ACL path is local/tunnel.
    "split-tunneling-acl-local-ap-subnet": "option",  # Enable/disable automatically adding local subnetwork of Fort
    "split-tunneling-acl": "string",  # Split tunneling ACL filter list.
    "allowaccess": "option",  # Control management access to the managed WTP, FortiAP, or AP
    "login-passwd-change": "option",  # Change or reset the administrator password of a managed WTP,
    "login-passwd": "password",  # Set the managed WTP, FortiAP, or AP's administrator password
    "lldp": "option",  # Enable/disable Link Layer Discovery Protocol (LLDP) for the 
    "poe-mode": "option",  # Set the WTP, FortiAP, or AP's PoE mode.
    "usb-port": "option",  # Enable/disable USB port of the WTP (default = enable).
    "frequency-handoff": "option",  # Enable/disable frequency handoff of clients to other channel
    "ap-handoff": "option",  # Enable/disable AP handoff of clients to other APs (default =
    "default-mesh-root": "option",  # Configure default mesh root SSID when it is not included by 
    "radio-1": "string",  # Configuration options for radio 1.
    "radio-2": "string",  # Configuration options for radio 2.
    "radio-3": "string",  # Configuration options for radio 3.
    "radio-4": "string",  # Configuration options for radio 4.
    "lbs": "string",  # Set various location based service (LBS) options.
    "ext-info-enable": "option",  # Enable/disable station/VAP/radio extension information.
    "indoor-outdoor-deployment": "option",  # Set to allow indoor/outdoor-only channels under regulatory r
    "esl-ses-dongle": "string",  # ESL SES-imagotag dongle configuration.
    "console-login": "option",  # Enable/disable FortiAP console login access (default = enabl
    "wan-port-auth": "option",  # Set WAN port authentication mode (default = none).
    "wan-port-auth-usrname": "string",  # Set WAN port 802.1x supplicant user name.
    "wan-port-auth-password": "password",  # Set WAN port 802.1x supplicant password.
    "wan-port-auth-methods": "option",  # WAN port 802.1x supplicant EAP methods (default = all).
    "wan-port-auth-macsec": "option",  # Enable/disable WAN port 802.1x supplicant MACsec policy (def
    "unii-4-5ghz-band": "option",  # Enable/disable UNII-4 5Ghz band channels (default = disable)
    "admin-auth-tacacs+": "string",  # Remote authentication server for admin user.
    "admin-restrict-local": "option",  # Enable/disable local admin authentication restriction when r
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "WTP (or FortiAP or AP) profile name.",
    "comment": "Comment.",
    "platform": "WTP, FortiAP, or AP platform.",
    "control-message-offload": "Enable/disable CAPWAP control message data channel offload.",
    "bonjour-profile": "Bonjour profile name.",
    "apcfg-profile": "AP local configuration profile name.",
    "apcfg-mesh": "Enable/disable AP local mesh configuration (default = disable).",
    "apcfg-mesh-ap-type": "Mesh AP Type (default = ethernet).",
    "apcfg-mesh-ssid": " Mesh SSID (default = none).",
    "apcfg-mesh-eth-bridge": "Enable/disable mesh ethernet bridge (default = disable).",
    "ble-profile": "Bluetooth Low Energy profile name.",
    "syslog-profile": "System log server configuration profile name.",
    "wan-port-mode": "Enable/disable using a WAN port as a LAN port.",
    "lan": "WTP LAN port mapping.",
    "energy-efficient-ethernet": "Enable/disable use of energy efficient Ethernet on WTP.",
    "led-state": "Enable/disable use of LEDs on WTP (default = enable).",
    "led-schedules": "Recurring firewall schedules for illuminating LEDs on the FortiAP. If led-state is enabled, LEDs will be visible when at least one of the schedules is valid. Separate multiple schedule names with a space.",
    "dtls-policy": "WTP data channel DTLS policy (default = clear-text).",
    "dtls-in-kernel": "Enable/disable data channel DTLS in kernel.",
    "max-clients": "Maximum number of stations (STAs) supported by the WTP (default = 0, meaning no client limitation).",
    "handoff-rssi": "Minimum received signal strength indicator (RSSI) value for handoff (20 - 30, default = 25).",
    "handoff-sta-thresh": "Threshold value for AP handoff.",
    "handoff-roaming": "Enable/disable client load balancing during roaming to avoid roaming delay (default = disable).",
    "deny-mac-list": "List of MAC addresses that are denied access to this WTP, FortiAP, or AP.",
    "ap-country": "Country in which this WTP, FortiAP, or AP will operate (default = NA, automatically use the country configured for the current VDOM).",
    "ip-fragment-preventing": "Method(s) by which IP fragmentation is prevented for control and data packets through CAPWAP tunnel (default = tcp-mss-adjust).",
    "tun-mtu-uplink": "The maximum transmission unit (MTU) of uplink CAPWAP tunnel (576 - 1500 bytes or 0; 0 means the local MTU of FortiAP; default = 0).",
    "tun-mtu-downlink": "The MTU of downlink CAPWAP tunnel (576 - 1500 bytes or 0; 0 means the local MTU of FortiAP; default = 0).",
    "split-tunneling-acl-path": "Split tunneling ACL path is local/tunnel.",
    "split-tunneling-acl-local-ap-subnet": "Enable/disable automatically adding local subnetwork of FortiAP to split-tunneling ACL (default = disable).",
    "split-tunneling-acl": "Split tunneling ACL filter list.",
    "allowaccess": "Control management access to the managed WTP, FortiAP, or AP. Separate entries with a space.",
    "login-passwd-change": "Change or reset the administrator password of a managed WTP, FortiAP or AP (yes, default, or no, default = no).",
    "login-passwd": "Set the managed WTP, FortiAP, or AP's administrator password.",
    "lldp": "Enable/disable Link Layer Discovery Protocol (LLDP) for the WTP, FortiAP, or AP (default = enable).",
    "poe-mode": "Set the WTP, FortiAP, or AP's PoE mode.",
    "usb-port": "Enable/disable USB port of the WTP (default = enable).",
    "frequency-handoff": "Enable/disable frequency handoff of clients to other channels (default = disable).",
    "ap-handoff": "Enable/disable AP handoff of clients to other APs (default = disable).",
    "default-mesh-root": "Configure default mesh root SSID when it is not included by radio's SSID configuration.",
    "radio-1": "Configuration options for radio 1.",
    "radio-2": "Configuration options for radio 2.",
    "radio-3": "Configuration options for radio 3.",
    "radio-4": "Configuration options for radio 4.",
    "lbs": "Set various location based service (LBS) options.",
    "ext-info-enable": "Enable/disable station/VAP/radio extension information.",
    "indoor-outdoor-deployment": "Set to allow indoor/outdoor-only channels under regulatory rules (default = platform-determined).",
    "esl-ses-dongle": "ESL SES-imagotag dongle configuration.",
    "console-login": "Enable/disable FortiAP console login access (default = enable).",
    "wan-port-auth": "Set WAN port authentication mode (default = none).",
    "wan-port-auth-usrname": "Set WAN port 802.1x supplicant user name.",
    "wan-port-auth-password": "Set WAN port 802.1x supplicant password.",
    "wan-port-auth-methods": "WAN port 802.1x supplicant EAP methods (default = all).",
    "wan-port-auth-macsec": "Enable/disable WAN port 802.1x supplicant MACsec policy (default = disable).",
    "unii-4-5ghz-band": "Enable/disable UNII-4 5Ghz band channels (default = disable).",
    "admin-auth-tacacs+": "Remote authentication server for admin user.",
    "admin-restrict-local": "Enable/disable local admin authentication restriction when remote authenticator is up and running (default = disable).",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 35},
    "bonjour-profile": {"type": "string", "max_length": 35},
    "apcfg-profile": {"type": "string", "max_length": 35},
    "apcfg-mesh-ssid": {"type": "string", "max_length": 15},
    "ble-profile": {"type": "string", "max_length": 35},
    "syslog-profile": {"type": "string", "max_length": 35},
    "max-clients": {"type": "integer", "min": 0, "max": 4294967295},
    "handoff-rssi": {"type": "integer", "min": 20, "max": 30},
    "handoff-sta-thresh": {"type": "integer", "min": 5, "max": 60},
    "tun-mtu-uplink": {"type": "integer", "min": 576, "max": 1500},
    "tun-mtu-downlink": {"type": "integer", "min": 576, "max": 1500},
    "wan-port-auth-usrname": {"type": "string", "max_length": 63},
    "admin-auth-tacacs+": {"type": "string", "max_length": 35},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "platform": {
        "type": {
            "type": "option",
            "help": "WTP, FortiAP or AP platform type. There are built-in WTP profiles for all supported FortiAP models. You can select a built-in profile and customize it or create a new profile.",
            "default": "221E",
            "options": ["AP-11N", "C24JE", "421E", "423E", "221E", "222E", "223E", "224E", "231E", "321E", "431F", "431FL", "432F", "432FR", "433F", "433FL", "231F", "231FL", "234F", "23JF", "831F", "231G", "233G", "234G", "431G", "432G", "433G", "231K", "23JK", "222KL", "241K", "243K", "244K", "441K", "443K", "U421E", "U422EV", "U423E", "U221EV", "U223EV", "U24JEV", "U321EV", "U323EV", "U431F", "U433F", "U231F", "U234F", "U432F", "U231G"],
        },
        "mode": {
            "type": "option",
            "help": "Configure operation mode of 5G radios (default = single-5G).",
            "default": "single-5G",
            "options": ["single-5G", "dual-5G"],
        },
        "ddscan": {
            "type": "option",
            "help": "Enable/disable use of one radio for dedicated full-band scanning to detect RF characterization and wireless threat management.",
            "default": "disable",
            "options": ["enable", "disable"],
        },
    },
    "lan": {
        "port-mode": {
            "type": "option",
            "help": "LAN port mode.",
            "default": "offline",
            "options": ["offline", "nat-to-wan", "bridge-to-wan", "bridge-to-ssid"],
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
            "options": ["offline", "nat-to-wan", "bridge-to-wan", "bridge-to-ssid"],
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
            "options": ["offline", "nat-to-wan", "bridge-to-wan", "bridge-to-ssid"],
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
            "options": ["offline", "nat-to-wan", "bridge-to-wan", "bridge-to-ssid"],
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
            "options": ["offline", "nat-to-wan", "bridge-to-wan", "bridge-to-ssid"],
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
            "options": ["offline", "nat-to-wan", "bridge-to-wan", "bridge-to-ssid"],
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
            "options": ["offline", "nat-to-wan", "bridge-to-wan", "bridge-to-ssid"],
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
            "options": ["offline", "nat-to-wan", "bridge-to-wan", "bridge-to-ssid"],
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
            "options": ["offline", "nat-to-wan", "bridge-to-wan", "bridge-to-ssid"],
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
            "options": ["offline", "nat-to-wan", "bridge-to-wan", "bridge-to-ssid"],
        },
        "port-esl-ssid": {
            "type": "string",
            "help": "Bridge ESL port to SSID.",
            "default": "",
            "max_length": 15,
        },
    },
    "led-schedules": {
        "name": {
            "type": "string",
            "help": "Schedule name.",
            "required": True,
            "default": "",
            "max_length": 35,
        },
    },
    "deny-mac-list": {
        "id": {
            "type": "integer",
            "help": "ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "mac": {
            "type": "mac-address",
            "help": "A WiFi device with this MAC address is denied access to this WTP, FortiAP or AP.",
            "default": "00:00:00:00:00:00",
        },
    },
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
    "radio-1": {
        "mode": {
            "type": "option",
            "help": "Mode of radio 1. Radio 1 can be disabled, configured as an access point, a rogue AP monitor, a sniffer, or a station.",
            "default": "ap",
            "options": ["disabled", "ap", "monitor", "sniffer", "sam"],
        },
        "band": {
            "type": "option",
            "help": "WiFi band that Radio 1 operates on.",
            "default": "",
            "options": ["802.11a", "802.11b", "802.11g", "802.11n-2G", "802.11n-5G", "802.11ac-2G", "802.11ac-5G", "802.11ax-2G", "802.11ax-5G", "802.11ax-6G", "802.11be-2G", "802.11be-5G", "802.11be-6G"],
        },
        "band-5g-type": {
            "type": "option",
            "help": "WiFi 5G band type.",
            "default": "5g-full",
            "options": ["5g-full", "5g-high", "5g-low"],
        },
        "drma": {
            "type": "option",
            "help": "Enable/disable dynamic radio mode assignment (DRMA) (default = disable).",
            "default": "disable",
            "options": ["disable", "enable"],
        },
        "drma-sensitivity": {
            "type": "option",
            "help": "Network Coverage Factor (NCF) percentage required to consider a radio as redundant (default = low).",
            "default": "low",
            "options": ["low", "medium", "high"],
        },
        "airtime-fairness": {
            "type": "option",
            "help": "Enable/disable airtime fairness (default = disable).",
            "default": "disable",
            "options": ["enable", "disable"],
        },
        "protection-mode": {
            "type": "option",
            "help": "Enable/disable 802.11g protection modes to support backwards compatibility with older clients (rtscts, ctsonly, disable).",
            "default": "disable",
            "options": ["rtscts", "ctsonly", "disable"],
        },
        "powersave-optimize": {
            "type": "option",
            "help": "Enable client power-saving features such as TIM, AC VO, and OBSS etc.",
            "default": "",
            "options": ["tim", "ac-vo", "no-obss-scan", "no-11b-rate", "client-rate-follow"],
        },
        "transmit-optimize": {
            "type": "option",
            "help": "Packet transmission optimization options including power saving, aggregation limiting, retry limiting, etc. All are enabled by default.",
            "default": "power-save aggr-limit retry-limit send-bar",
            "options": ["disable", "power-save", "aggr-limit", "retry-limit", "send-bar"],
        },
        "amsdu": {
            "type": "option",
            "help": "Enable/disable 802.11n AMSDU support. AMSDU can improve performance if supported by your WiFi clients (default = enable).",
            "default": "enable",
            "options": ["enable", "disable"],
        },
        "coexistence": {
            "type": "option",
            "help": "Enable/disable allowing both HT20 and HT40 on the same radio (default = enable).",
            "default": "enable",
            "options": ["enable", "disable"],
        },
        "zero-wait-dfs": {
            "type": "option",
            "help": "Enable/disable zero wait DFS on radio (default = enable).",
            "default": "enable",
            "options": ["enable", "disable"],
        },
        "bss-color": {
            "type": "integer",
            "help": "BSS color value for this 11ax radio (0 - 63, disable = 0, default = 0).",
            "default": 0,
            "min_value": 0,
            "max_value": 63,
        },
        "bss-color-mode": {
            "type": "option",
            "help": "BSS color mode for this 11ax radio (default = auto).",
            "default": "auto",
            "options": ["auto", "static"],
        },
        "short-guard-interval": {
            "type": "option",
            "help": "Use either the short guard interval (Short GI) of 400 ns or the long guard interval (Long GI) of 800 ns.",
            "default": "disable",
            "options": ["enable", "disable"],
        },
        "mimo-mode": {
            "type": "option",
            "help": "Configure radio MIMO mode (default = default).",
            "default": "default",
            "options": ["default", "1x1", "2x2", "3x3", "4x4", "8x8"],
        },
        "channel-bonding": {
            "type": "option",
            "help": "Channel bandwidth: 320, 240, 160, 80, 40, or 20MHz. Channels may use both 20 and 40 by enabling coexistence.",
            "default": "20MHz",
            "options": ["320MHz", "240MHz", "160MHz", "80MHz", "40MHz", "20MHz"],
        },
        "channel-bonding-ext": {
            "type": "option",
            "help": "Channel bandwidth extension: 320 MHz-1 and 320 MHz-2 (default = 320 MHz-2).",
            "default": "320MHz-2",
            "options": ["320MHz-1", "320MHz-2"],
        },
        "optional-antenna": {
            "type": "option",
            "help": "Optional antenna used on FAP (default = none).",
            "default": "none",
            "options": ["none", "custom", "FANT-04ABGN-0606-O-N", "FANT-04ABGN-1414-P-N", "FANT-04ABGN-8065-P-N", "FANT-04ABGN-0606-O-R", "FANT-04ABGN-0606-P-R", "FANT-10ACAX-1213-D-N", "FANT-08ABGN-1213-D-R", "FANT-04BEAX-0606-P-R"],
        },
        "optional-antenna-gain": {
            "type": "string",
            "help": "Optional antenna gain in dBi (0 to 20, default = 0).",
            "default": "0",
            "max_length": 7,
        },
        "auto-power-level": {
            "type": "option",
            "help": "Enable/disable automatic power-level adjustment to prevent co-channel interference (default = disable).",
            "default": "disable",
            "options": ["enable", "disable"],
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
            "options": ["dBm", "percentage"],
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
        "dtim": {
            "type": "integer",
            "help": "Delivery Traffic Indication Map (DTIM) period (1 - 255, default = 1). Set higher to save battery life of WiFi client in power-save mode.",
            "default": 1,
            "min_value": 1,
            "max_value": 255,
        },
        "beacon-interval": {
            "type": "integer",
            "help": "Beacon interval. The time between beacon frames in milliseconds. Actual range of beacon interval depends on the AP platform type (default = 100).",
            "default": 100,
            "min_value": 0,
            "max_value": 65535,
        },
        "80211d": {
            "type": "option",
            "help": "Enable/disable 802.11d countryie(default = enable).",
            "default": "enable",
            "options": ["enable", "disable"],
        },
        "80211mc": {
            "type": "option",
            "help": "Enable/disable 802.11mc responder mode (default = disable).",
            "default": "disable",
            "options": ["enable", "disable"],
        },
        "rts-threshold": {
            "type": "integer",
            "help": "Maximum packet size for RTS transmissions, specifying the maximum size of a data packet before RTS/CTS (256 - 2346 bytes, default = 2346).",
            "default": 2346,
            "min_value": 256,
            "max_value": 2346,
        },
        "frag-threshold": {
            "type": "integer",
            "help": "Maximum packet size that can be sent without fragmentation (800 - 2346 bytes, default = 2346).",
            "default": 2346,
            "min_value": 800,
            "max_value": 2346,
        },
        "ap-sniffer-bufsize": {
            "type": "integer",
            "help": "Sniffer buffer size (1 - 32 MB, default = 16).",
            "default": 16,
            "min_value": 1,
            "max_value": 32,
        },
        "ap-sniffer-chan": {
            "type": "integer",
            "help": "Channel on which to operate the sniffer (default = 6).",
            "default": 36,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "ap-sniffer-chan-width": {
            "type": "option",
            "help": "Channel bandwidth for sniffer.",
            "default": "20MHz",
            "options": ["320MHz", "240MHz", "160MHz", "80MHz", "40MHz", "20MHz"],
        },
        "ap-sniffer-addr": {
            "type": "mac-address",
            "help": "MAC address to monitor.",
            "default": "00:00:00:00:00:00",
        },
        "ap-sniffer-mgmt-beacon": {
            "type": "option",
            "help": "Enable/disable sniffer on WiFi management Beacon frames (default = enable).",
            "default": "enable",
            "options": ["enable", "disable"],
        },
        "ap-sniffer-mgmt-probe": {
            "type": "option",
            "help": "Enable/disable sniffer on WiFi management probe frames (default = enable).",
            "default": "enable",
            "options": ["enable", "disable"],
        },
        "ap-sniffer-mgmt-other": {
            "type": "option",
            "help": "Enable/disable sniffer on WiFi management other frames  (default = enable).",
            "default": "enable",
            "options": ["enable", "disable"],
        },
        "ap-sniffer-ctl": {
            "type": "option",
            "help": "Enable/disable sniffer on WiFi control frame (default = enable).",
            "default": "enable",
            "options": ["enable", "disable"],
        },
        "ap-sniffer-data": {
            "type": "option",
            "help": "Enable/disable sniffer on WiFi data frame (default = enable).",
            "default": "enable",
            "options": ["enable", "disable"],
        },
        "sam-ssid": {
            "type": "string",
            "help": "SSID for WiFi network.",
            "default": "",
            "max_length": 32,
        },
        "sam-bssid": {
            "type": "mac-address",
            "help": "BSSID for WiFi network.",
            "default": "00:00:00:00:00:00",
        },
        "sam-security-type": {
            "type": "option",
            "help": "Select WiFi network security type (default = \"wpa-personal\" for 2.4/5G radio, \"wpa3-sae\" for 6G radio).",
            "default": "wpa-personal",
            "options": ["open", "wpa-personal", "wpa-enterprise", "wpa3-sae", "owe"],
        },
        "sam-captive-portal": {
            "type": "option",
            "help": "Enable/disable Captive Portal Authentication (default = disable).",
            "default": "disable",
            "options": ["enable", "disable"],
        },
        "sam-cwp-username": {
            "type": "string",
            "help": "Username for captive portal authentication.",
            "default": "",
            "max_length": 35,
        },
        "sam-cwp-password": {
            "type": "password",
            "help": "Password for captive portal authentication.",
            "max_length": 128,
        },
        "sam-cwp-test-url": {
            "type": "string",
            "help": "Website the client is trying to access.",
            "default": "",
            "max_length": 255,
        },
        "sam-cwp-match-string": {
            "type": "string",
            "help": "Identification string from the captive portal login form.",
            "default": "",
            "max_length": 64,
        },
        "sam-cwp-success-string": {
            "type": "string",
            "help": "Success identification on the page after a successful login.",
            "default": "",
            "max_length": 64,
        },
        "sam-cwp-failure-string": {
            "type": "string",
            "help": "Failure identification on the page after an incorrect login.",
            "default": "",
            "max_length": 64,
        },
        "sam-eap-method": {
            "type": "option",
            "help": "Select WPA2/WPA3-ENTERPRISE EAP Method (default = PEAP).",
            "default": "peap",
            "options": ["both", "tls", "peap"],
        },
        "sam-client-certificate": {
            "type": "string",
            "help": "Client certificate for WPA2/WPA3-ENTERPRISE.",
            "default": "",
            "max_length": 35,
        },
        "sam-private-key": {
            "type": "string",
            "help": "Private key for WPA2/WPA3-ENTERPRISE.",
            "default": "",
            "max_length": 35,
        },
        "sam-private-key-password": {
            "type": "password",
            "help": "Password for private key file for WPA2/WPA3-ENTERPRISE.",
            "max_length": 128,
        },
        "sam-ca-certificate": {
            "type": "string",
            "help": "CA certificate for WPA2/WPA3-ENTERPRISE.",
            "default": "",
            "max_length": 79,
        },
        "sam-username": {
            "type": "string",
            "help": "Username for WiFi network connection.",
            "default": "",
            "max_length": 35,
        },
        "sam-password": {
            "type": "password",
            "help": "Passphrase for WiFi network connection.",
            "max_length": 128,
        },
        "sam-test": {
            "type": "option",
            "help": "Select SAM test type (default = \"PING\").",
            "default": "ping",
            "options": ["ping", "iperf"],
        },
        "sam-server-type": {
            "type": "option",
            "help": "Select SAM server type (default = \"IP\").",
            "default": "ip",
            "options": ["ip", "fqdn"],
        },
        "sam-server-ip": {
            "type": "ipv4-address",
            "help": "SAM test server IP address.",
            "default": "0.0.0.0",
        },
        "sam-server-fqdn": {
            "type": "string",
            "help": "SAM test server domain name.",
            "default": "",
            "max_length": 255,
        },
        "iperf-server-port": {
            "type": "integer",
            "help": "Iperf service port number.",
            "default": 5001,
            "min_value": 0,
            "max_value": 65535,
        },
        "iperf-protocol": {
            "type": "option",
            "help": "Iperf test protocol (default = \"UDP\").",
            "default": "udp",
            "options": ["udp", "tcp"],
        },
        "sam-report-intv": {
            "type": "integer",
            "help": "SAM report interval (sec), 0 for a one-time report.",
            "default": 0,
            "min_value": 60,
            "max_value": 864000,
        },
        "channel-utilization": {
            "type": "option",
            "help": "Enable/disable measuring channel utilization.",
            "default": "enable",
            "options": ["enable", "disable"],
        },
        "wids-profile": {
            "type": "string",
            "help": "Wireless Intrusion Detection System (WIDS) profile name to assign to the radio.",
            "default": "",
            "max_length": 35,
        },
        "darrp": {
            "type": "option",
            "help": "Enable/disable Distributed Automatic Radio Resource Provisioning (DARRP) to make sure the radio is always using the most optimal channel (default = disable).",
            "default": "disable",
            "options": ["enable", "disable"],
        },
        "arrp-profile": {
            "type": "string",
            "help": "Distributed Automatic Radio Resource Provisioning (DARRP) profile name to assign to the radio.",
            "default": "",
            "max_length": 35,
        },
        "max-clients": {
            "type": "integer",
            "help": "Maximum number of stations (STAs) or WiFi clients supported by the radio. Range depends on the hardware.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "max-distance": {
            "type": "integer",
            "help": "Maximum expected distance between the AP and clients (0 - 54000 m, default = 0).",
            "default": 0,
            "min_value": 0,
            "max_value": 54000,
        },
        "vap-all": {
            "type": "option",
            "help": "Configure method for assigning SSIDs to this FortiAP (default = automatically assign tunnel SSIDs).",
            "default": "tunnel",
            "options": ["tunnel", "bridge", "manual"],
        },
        "vaps": {
            "type": "string",
            "help": "Manually selected list of Virtual Access Points (VAPs).",
        },
        "channel": {
            "type": "string",
            "help": "Selected list of wireless radio channels.",
        },
        "call-admission-control": {
            "type": "option",
            "help": "Enable/disable WiFi multimedia (WMM) call admission control to optimize WiFi bandwidth use for VoIP calls. New VoIP calls are only accepted if there is enough bandwidth available to support them.",
            "default": "disable",
            "options": ["enable", "disable"],
        },
        "call-capacity": {
            "type": "integer",
            "help": "Maximum number of Voice over WLAN (VoWLAN) phones supported by the radio (0 - 60, default = 10).",
            "default": 10,
            "min_value": 0,
            "max_value": 60,
        },
        "bandwidth-admission-control": {
            "type": "option",
            "help": "Enable/disable WiFi multimedia (WMM) bandwidth admission control to optimize WiFi bandwidth use. A request to join the wireless network is only allowed if the access point has enough bandwidth to support it.",
            "default": "disable",
            "options": ["enable", "disable"],
        },
        "bandwidth-capacity": {
            "type": "integer",
            "help": "Maximum bandwidth capacity allowed (1 - 600000 Kbps, default = 2000).",
            "default": 2000,
            "min_value": 1,
            "max_value": 600000,
        },
    },
    "radio-2": {
        "mode": {
            "type": "option",
            "help": "Mode of radio 2. Radio 2 can be disabled, configured as an access point, a rogue AP monitor, a sniffer, or a station.",
            "default": "ap",
            "options": ["disabled", "ap", "monitor", "sniffer", "sam"],
        },
        "band": {
            "type": "option",
            "help": "WiFi band that Radio 2 operates on.",
            "default": "",
            "options": ["802.11a", "802.11b", "802.11g", "802.11n-2G", "802.11n-5G", "802.11ac-2G", "802.11ac-5G", "802.11ax-2G", "802.11ax-5G", "802.11ax-6G", "802.11be-2G", "802.11be-5G", "802.11be-6G"],
        },
        "band-5g-type": {
            "type": "option",
            "help": "WiFi 5G band type.",
            "default": "5g-full",
            "options": ["5g-full", "5g-high", "5g-low"],
        },
        "drma": {
            "type": "option",
            "help": "Enable/disable dynamic radio mode assignment (DRMA) (default = disable).",
            "default": "disable",
            "options": ["disable", "enable"],
        },
        "drma-sensitivity": {
            "type": "option",
            "help": "Network Coverage Factor (NCF) percentage required to consider a radio as redundant (default = low).",
            "default": "low",
            "options": ["low", "medium", "high"],
        },
        "airtime-fairness": {
            "type": "option",
            "help": "Enable/disable airtime fairness (default = disable).",
            "default": "disable",
            "options": ["enable", "disable"],
        },
        "protection-mode": {
            "type": "option",
            "help": "Enable/disable 802.11g protection modes to support backwards compatibility with older clients (rtscts, ctsonly, disable).",
            "default": "disable",
            "options": ["rtscts", "ctsonly", "disable"],
        },
        "powersave-optimize": {
            "type": "option",
            "help": "Enable client power-saving features such as TIM, AC VO, and OBSS etc.",
            "default": "",
            "options": ["tim", "ac-vo", "no-obss-scan", "no-11b-rate", "client-rate-follow"],
        },
        "transmit-optimize": {
            "type": "option",
            "help": "Packet transmission optimization options including power saving, aggregation limiting, retry limiting, etc. All are enabled by default.",
            "default": "power-save aggr-limit retry-limit send-bar",
            "options": ["disable", "power-save", "aggr-limit", "retry-limit", "send-bar"],
        },
        "amsdu": {
            "type": "option",
            "help": "Enable/disable 802.11n AMSDU support. AMSDU can improve performance if supported by your WiFi clients (default = enable).",
            "default": "enable",
            "options": ["enable", "disable"],
        },
        "coexistence": {
            "type": "option",
            "help": "Enable/disable allowing both HT20 and HT40 on the same radio (default = enable).",
            "default": "enable",
            "options": ["enable", "disable"],
        },
        "zero-wait-dfs": {
            "type": "option",
            "help": "Enable/disable zero wait DFS on radio (default = enable).",
            "default": "enable",
            "options": ["enable", "disable"],
        },
        "bss-color": {
            "type": "integer",
            "help": "BSS color value for this 11ax radio (0 - 63, disable = 0, default = 0).",
            "default": 0,
            "min_value": 0,
            "max_value": 63,
        },
        "bss-color-mode": {
            "type": "option",
            "help": "BSS color mode for this 11ax radio (default = auto).",
            "default": "auto",
            "options": ["auto", "static"],
        },
        "short-guard-interval": {
            "type": "option",
            "help": "Use either the short guard interval (Short GI) of 400 ns or the long guard interval (Long GI) of 800 ns.",
            "default": "disable",
            "options": ["enable", "disable"],
        },
        "mimo-mode": {
            "type": "option",
            "help": "Configure radio MIMO mode (default = default).",
            "default": "default",
            "options": ["default", "1x1", "2x2", "3x3", "4x4", "8x8"],
        },
        "channel-bonding": {
            "type": "option",
            "help": "Channel bandwidth: 320, 240, 160, 80, 40, or 20MHz. Channels may use both 20 and 40 by enabling coexistence.",
            "default": "20MHz",
            "options": ["320MHz", "240MHz", "160MHz", "80MHz", "40MHz", "20MHz"],
        },
        "channel-bonding-ext": {
            "type": "option",
            "help": "Channel bandwidth extension: 320 MHz-1 and 320 MHz-2 (default = 320 MHz-2).",
            "default": "320MHz-2",
            "options": ["320MHz-1", "320MHz-2"],
        },
        "optional-antenna": {
            "type": "option",
            "help": "Optional antenna used on FAP (default = none).",
            "default": "none",
            "options": ["none", "custom", "FANT-04ABGN-0606-O-N", "FANT-04ABGN-1414-P-N", "FANT-04ABGN-8065-P-N", "FANT-04ABGN-0606-O-R", "FANT-04ABGN-0606-P-R", "FANT-10ACAX-1213-D-N", "FANT-08ABGN-1213-D-R", "FANT-04BEAX-0606-P-R"],
        },
        "optional-antenna-gain": {
            "type": "string",
            "help": "Optional antenna gain in dBi (0 to 20, default = 0).",
            "default": "0",
            "max_length": 7,
        },
        "auto-power-level": {
            "type": "option",
            "help": "Enable/disable automatic power-level adjustment to prevent co-channel interference (default = disable).",
            "default": "disable",
            "options": ["enable", "disable"],
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
            "options": ["dBm", "percentage"],
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
        "dtim": {
            "type": "integer",
            "help": "Delivery Traffic Indication Map (DTIM) period (1 - 255, default = 1). Set higher to save battery life of WiFi client in power-save mode.",
            "default": 1,
            "min_value": 1,
            "max_value": 255,
        },
        "beacon-interval": {
            "type": "integer",
            "help": "Beacon interval. The time between beacon frames in milliseconds. Actual range of beacon interval depends on the AP platform type (default = 100).",
            "default": 100,
            "min_value": 0,
            "max_value": 65535,
        },
        "80211d": {
            "type": "option",
            "help": "Enable/disable 802.11d countryie(default = enable).",
            "default": "enable",
            "options": ["enable", "disable"],
        },
        "80211mc": {
            "type": "option",
            "help": "Enable/disable 802.11mc responder mode (default = disable).",
            "default": "disable",
            "options": ["enable", "disable"],
        },
        "rts-threshold": {
            "type": "integer",
            "help": "Maximum packet size for RTS transmissions, specifying the maximum size of a data packet before RTS/CTS (256 - 2346 bytes, default = 2346).",
            "default": 2346,
            "min_value": 256,
            "max_value": 2346,
        },
        "frag-threshold": {
            "type": "integer",
            "help": "Maximum packet size that can be sent without fragmentation (800 - 2346 bytes, default = 2346).",
            "default": 2346,
            "min_value": 800,
            "max_value": 2346,
        },
        "ap-sniffer-bufsize": {
            "type": "integer",
            "help": "Sniffer buffer size (1 - 32 MB, default = 16).",
            "default": 16,
            "min_value": 1,
            "max_value": 32,
        },
        "ap-sniffer-chan": {
            "type": "integer",
            "help": "Channel on which to operate the sniffer (default = 6).",
            "default": 6,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "ap-sniffer-chan-width": {
            "type": "option",
            "help": "Channel bandwidth for sniffer.",
            "default": "20MHz",
            "options": ["320MHz", "240MHz", "160MHz", "80MHz", "40MHz", "20MHz"],
        },
        "ap-sniffer-addr": {
            "type": "mac-address",
            "help": "MAC address to monitor.",
            "default": "00:00:00:00:00:00",
        },
        "ap-sniffer-mgmt-beacon": {
            "type": "option",
            "help": "Enable/disable sniffer on WiFi management Beacon frames (default = enable).",
            "default": "enable",
            "options": ["enable", "disable"],
        },
        "ap-sniffer-mgmt-probe": {
            "type": "option",
            "help": "Enable/disable sniffer on WiFi management probe frames (default = enable).",
            "default": "enable",
            "options": ["enable", "disable"],
        },
        "ap-sniffer-mgmt-other": {
            "type": "option",
            "help": "Enable/disable sniffer on WiFi management other frames  (default = enable).",
            "default": "enable",
            "options": ["enable", "disable"],
        },
        "ap-sniffer-ctl": {
            "type": "option",
            "help": "Enable/disable sniffer on WiFi control frame (default = enable).",
            "default": "enable",
            "options": ["enable", "disable"],
        },
        "ap-sniffer-data": {
            "type": "option",
            "help": "Enable/disable sniffer on WiFi data frame (default = enable).",
            "default": "enable",
            "options": ["enable", "disable"],
        },
        "sam-ssid": {
            "type": "string",
            "help": "SSID for WiFi network.",
            "default": "",
            "max_length": 32,
        },
        "sam-bssid": {
            "type": "mac-address",
            "help": "BSSID for WiFi network.",
            "default": "00:00:00:00:00:00",
        },
        "sam-security-type": {
            "type": "option",
            "help": "Select WiFi network security type (default = \"wpa-personal\" for 2.4/5G radio, \"wpa3-sae\" for 6G radio).",
            "default": "wpa-personal",
            "options": ["open", "wpa-personal", "wpa-enterprise", "wpa3-sae", "owe"],
        },
        "sam-captive-portal": {
            "type": "option",
            "help": "Enable/disable Captive Portal Authentication (default = disable).",
            "default": "disable",
            "options": ["enable", "disable"],
        },
        "sam-cwp-username": {
            "type": "string",
            "help": "Username for captive portal authentication.",
            "default": "",
            "max_length": 35,
        },
        "sam-cwp-password": {
            "type": "password",
            "help": "Password for captive portal authentication.",
            "max_length": 128,
        },
        "sam-cwp-test-url": {
            "type": "string",
            "help": "Website the client is trying to access.",
            "default": "",
            "max_length": 255,
        },
        "sam-cwp-match-string": {
            "type": "string",
            "help": "Identification string from the captive portal login form.",
            "default": "",
            "max_length": 64,
        },
        "sam-cwp-success-string": {
            "type": "string",
            "help": "Success identification on the page after a successful login.",
            "default": "",
            "max_length": 64,
        },
        "sam-cwp-failure-string": {
            "type": "string",
            "help": "Failure identification on the page after an incorrect login.",
            "default": "",
            "max_length": 64,
        },
        "sam-eap-method": {
            "type": "option",
            "help": "Select WPA2/WPA3-ENTERPRISE EAP Method (default = PEAP).",
            "default": "peap",
            "options": ["both", "tls", "peap"],
        },
        "sam-client-certificate": {
            "type": "string",
            "help": "Client certificate for WPA2/WPA3-ENTERPRISE.",
            "default": "",
            "max_length": 35,
        },
        "sam-private-key": {
            "type": "string",
            "help": "Private key for WPA2/WPA3-ENTERPRISE.",
            "default": "",
            "max_length": 35,
        },
        "sam-private-key-password": {
            "type": "password",
            "help": "Password for private key file for WPA2/WPA3-ENTERPRISE.",
            "max_length": 128,
        },
        "sam-ca-certificate": {
            "type": "string",
            "help": "CA certificate for WPA2/WPA3-ENTERPRISE.",
            "default": "",
            "max_length": 79,
        },
        "sam-username": {
            "type": "string",
            "help": "Username for WiFi network connection.",
            "default": "",
            "max_length": 35,
        },
        "sam-password": {
            "type": "password",
            "help": "Passphrase for WiFi network connection.",
            "max_length": 128,
        },
        "sam-test": {
            "type": "option",
            "help": "Select SAM test type (default = \"PING\").",
            "default": "ping",
            "options": ["ping", "iperf"],
        },
        "sam-server-type": {
            "type": "option",
            "help": "Select SAM server type (default = \"IP\").",
            "default": "ip",
            "options": ["ip", "fqdn"],
        },
        "sam-server-ip": {
            "type": "ipv4-address",
            "help": "SAM test server IP address.",
            "default": "0.0.0.0",
        },
        "sam-server-fqdn": {
            "type": "string",
            "help": "SAM test server domain name.",
            "default": "",
            "max_length": 255,
        },
        "iperf-server-port": {
            "type": "integer",
            "help": "Iperf service port number.",
            "default": 5001,
            "min_value": 0,
            "max_value": 65535,
        },
        "iperf-protocol": {
            "type": "option",
            "help": "Iperf test protocol (default = \"UDP\").",
            "default": "udp",
            "options": ["udp", "tcp"],
        },
        "sam-report-intv": {
            "type": "integer",
            "help": "SAM report interval (sec), 0 for a one-time report.",
            "default": 0,
            "min_value": 60,
            "max_value": 864000,
        },
        "channel-utilization": {
            "type": "option",
            "help": "Enable/disable measuring channel utilization.",
            "default": "enable",
            "options": ["enable", "disable"],
        },
        "wids-profile": {
            "type": "string",
            "help": "Wireless Intrusion Detection System (WIDS) profile name to assign to the radio.",
            "default": "",
            "max_length": 35,
        },
        "darrp": {
            "type": "option",
            "help": "Enable/disable Distributed Automatic Radio Resource Provisioning (DARRP) to make sure the radio is always using the most optimal channel (default = disable).",
            "default": "disable",
            "options": ["enable", "disable"],
        },
        "arrp-profile": {
            "type": "string",
            "help": "Distributed Automatic Radio Resource Provisioning (DARRP) profile name to assign to the radio.",
            "default": "",
            "max_length": 35,
        },
        "max-clients": {
            "type": "integer",
            "help": "Maximum number of stations (STAs) or WiFi clients supported by the radio. Range depends on the hardware.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "max-distance": {
            "type": "integer",
            "help": "Maximum expected distance between the AP and clients (0 - 54000 m, default = 0).",
            "default": 0,
            "min_value": 0,
            "max_value": 54000,
        },
        "vap-all": {
            "type": "option",
            "help": "Configure method for assigning SSIDs to this FortiAP (default = automatically assign tunnel SSIDs).",
            "default": "tunnel",
            "options": ["tunnel", "bridge", "manual"],
        },
        "vaps": {
            "type": "string",
            "help": "Manually selected list of Virtual Access Points (VAPs).",
        },
        "channel": {
            "type": "string",
            "help": "Selected list of wireless radio channels.",
        },
        "call-admission-control": {
            "type": "option",
            "help": "Enable/disable WiFi multimedia (WMM) call admission control to optimize WiFi bandwidth use for VoIP calls. New VoIP calls are only accepted if there is enough bandwidth available to support them.",
            "default": "disable",
            "options": ["enable", "disable"],
        },
        "call-capacity": {
            "type": "integer",
            "help": "Maximum number of Voice over WLAN (VoWLAN) phones supported by the radio (0 - 60, default = 10).",
            "default": 10,
            "min_value": 0,
            "max_value": 60,
        },
        "bandwidth-admission-control": {
            "type": "option",
            "help": "Enable/disable WiFi multimedia (WMM) bandwidth admission control to optimize WiFi bandwidth use. A request to join the wireless network is only allowed if the access point has enough bandwidth to support it.",
            "default": "disable",
            "options": ["enable", "disable"],
        },
        "bandwidth-capacity": {
            "type": "integer",
            "help": "Maximum bandwidth capacity allowed (1 - 600000 Kbps, default = 2000).",
            "default": 2000,
            "min_value": 1,
            "max_value": 600000,
        },
    },
    "radio-3": {
        "mode": {
            "type": "option",
            "help": "Mode of radio 3. Radio 3 can be disabled, configured as an access point, a rogue AP monitor, a sniffer, or a station.",
            "default": "ap",
            "options": ["disabled", "ap", "monitor", "sniffer", "sam"],
        },
        "band": {
            "type": "option",
            "help": "WiFi band that Radio 3 operates on.",
            "default": "",
            "options": ["802.11a", "802.11b", "802.11g", "802.11n-2G", "802.11n-5G", "802.11ac-2G", "802.11ac-5G", "802.11ax-2G", "802.11ax-5G", "802.11ax-6G", "802.11be-2G", "802.11be-5G", "802.11be-6G"],
        },
        "band-5g-type": {
            "type": "option",
            "help": "WiFi 5G band type.",
            "default": "5g-full",
            "options": ["5g-full", "5g-high", "5g-low"],
        },
        "drma": {
            "type": "option",
            "help": "Enable/disable dynamic radio mode assignment (DRMA) (default = disable).",
            "default": "disable",
            "options": ["disable", "enable"],
        },
        "drma-sensitivity": {
            "type": "option",
            "help": "Network Coverage Factor (NCF) percentage required to consider a radio as redundant (default = low).",
            "default": "low",
            "options": ["low", "medium", "high"],
        },
        "airtime-fairness": {
            "type": "option",
            "help": "Enable/disable airtime fairness (default = disable).",
            "default": "disable",
            "options": ["enable", "disable"],
        },
        "protection-mode": {
            "type": "option",
            "help": "Enable/disable 802.11g protection modes to support backwards compatibility with older clients (rtscts, ctsonly, disable).",
            "default": "disable",
            "options": ["rtscts", "ctsonly", "disable"],
        },
        "powersave-optimize": {
            "type": "option",
            "help": "Enable client power-saving features such as TIM, AC VO, and OBSS etc.",
            "default": "",
            "options": ["tim", "ac-vo", "no-obss-scan", "no-11b-rate", "client-rate-follow"],
        },
        "transmit-optimize": {
            "type": "option",
            "help": "Packet transmission optimization options including power saving, aggregation limiting, retry limiting, etc. All are enabled by default.",
            "default": "power-save aggr-limit retry-limit send-bar",
            "options": ["disable", "power-save", "aggr-limit", "retry-limit", "send-bar"],
        },
        "amsdu": {
            "type": "option",
            "help": "Enable/disable 802.11n AMSDU support. AMSDU can improve performance if supported by your WiFi clients (default = enable).",
            "default": "enable",
            "options": ["enable", "disable"],
        },
        "coexistence": {
            "type": "option",
            "help": "Enable/disable allowing both HT20 and HT40 on the same radio (default = enable).",
            "default": "enable",
            "options": ["enable", "disable"],
        },
        "zero-wait-dfs": {
            "type": "option",
            "help": "Enable/disable zero wait DFS on radio (default = enable).",
            "default": "enable",
            "options": ["enable", "disable"],
        },
        "bss-color": {
            "type": "integer",
            "help": "BSS color value for this 11ax radio (0 - 63, disable = 0, default = 0).",
            "default": 0,
            "min_value": 0,
            "max_value": 63,
        },
        "bss-color-mode": {
            "type": "option",
            "help": "BSS color mode for this 11ax radio (default = auto).",
            "default": "auto",
            "options": ["auto", "static"],
        },
        "short-guard-interval": {
            "type": "option",
            "help": "Use either the short guard interval (Short GI) of 400 ns or the long guard interval (Long GI) of 800 ns.",
            "default": "disable",
            "options": ["enable", "disable"],
        },
        "mimo-mode": {
            "type": "option",
            "help": "Configure radio MIMO mode (default = default).",
            "default": "default",
            "options": ["default", "1x1", "2x2", "3x3", "4x4", "8x8"],
        },
        "channel-bonding": {
            "type": "option",
            "help": "Channel bandwidth: 320, 240, 160, 80, 40, or 20MHz. Channels may use both 20 and 40 by enabling coexistence.",
            "default": "20MHz",
            "options": ["320MHz", "240MHz", "160MHz", "80MHz", "40MHz", "20MHz"],
        },
        "channel-bonding-ext": {
            "type": "option",
            "help": "Channel bandwidth extension: 320 MHz-1 and 320 MHz-2 (default = 320 MHz-2).",
            "default": "320MHz-2",
            "options": ["320MHz-1", "320MHz-2"],
        },
        "optional-antenna": {
            "type": "option",
            "help": "Optional antenna used on FAP (default = none).",
            "default": "none",
            "options": ["none", "custom", "FANT-04ABGN-0606-O-N", "FANT-04ABGN-1414-P-N", "FANT-04ABGN-8065-P-N", "FANT-04ABGN-0606-O-R", "FANT-04ABGN-0606-P-R", "FANT-10ACAX-1213-D-N", "FANT-08ABGN-1213-D-R", "FANT-04BEAX-0606-P-R"],
        },
        "optional-antenna-gain": {
            "type": "string",
            "help": "Optional antenna gain in dBi (0 to 20, default = 0).",
            "default": "0",
            "max_length": 7,
        },
        "auto-power-level": {
            "type": "option",
            "help": "Enable/disable automatic power-level adjustment to prevent co-channel interference (default = disable).",
            "default": "disable",
            "options": ["enable", "disable"],
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
            "options": ["dBm", "percentage"],
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
        "dtim": {
            "type": "integer",
            "help": "Delivery Traffic Indication Map (DTIM) period (1 - 255, default = 1). Set higher to save battery life of WiFi client in power-save mode.",
            "default": 1,
            "min_value": 1,
            "max_value": 255,
        },
        "beacon-interval": {
            "type": "integer",
            "help": "Beacon interval. The time between beacon frames in milliseconds. Actual range of beacon interval depends on the AP platform type (default = 100).",
            "default": 100,
            "min_value": 0,
            "max_value": 65535,
        },
        "80211d": {
            "type": "option",
            "help": "Enable/disable 802.11d countryie(default = enable).",
            "default": "enable",
            "options": ["enable", "disable"],
        },
        "80211mc": {
            "type": "option",
            "help": "Enable/disable 802.11mc responder mode (default = disable).",
            "default": "disable",
            "options": ["enable", "disable"],
        },
        "rts-threshold": {
            "type": "integer",
            "help": "Maximum packet size for RTS transmissions, specifying the maximum size of a data packet before RTS/CTS (256 - 2346 bytes, default = 2346).",
            "default": 2346,
            "min_value": 256,
            "max_value": 2346,
        },
        "frag-threshold": {
            "type": "integer",
            "help": "Maximum packet size that can be sent without fragmentation (800 - 2346 bytes, default = 2346).",
            "default": 2346,
            "min_value": 800,
            "max_value": 2346,
        },
        "ap-sniffer-bufsize": {
            "type": "integer",
            "help": "Sniffer buffer size (1 - 32 MB, default = 16).",
            "default": 16,
            "min_value": 1,
            "max_value": 32,
        },
        "ap-sniffer-chan": {
            "type": "integer",
            "help": "Channel on which to operate the sniffer (default = 6).",
            "default": 37,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "ap-sniffer-chan-width": {
            "type": "option",
            "help": "Channel bandwidth for sniffer.",
            "default": "20MHz",
            "options": ["320MHz", "240MHz", "160MHz", "80MHz", "40MHz", "20MHz"],
        },
        "ap-sniffer-addr": {
            "type": "mac-address",
            "help": "MAC address to monitor.",
            "default": "00:00:00:00:00:00",
        },
        "ap-sniffer-mgmt-beacon": {
            "type": "option",
            "help": "Enable/disable sniffer on WiFi management Beacon frames (default = enable).",
            "default": "enable",
            "options": ["enable", "disable"],
        },
        "ap-sniffer-mgmt-probe": {
            "type": "option",
            "help": "Enable/disable sniffer on WiFi management probe frames (default = enable).",
            "default": "enable",
            "options": ["enable", "disable"],
        },
        "ap-sniffer-mgmt-other": {
            "type": "option",
            "help": "Enable/disable sniffer on WiFi management other frames  (default = enable).",
            "default": "enable",
            "options": ["enable", "disable"],
        },
        "ap-sniffer-ctl": {
            "type": "option",
            "help": "Enable/disable sniffer on WiFi control frame (default = enable).",
            "default": "enable",
            "options": ["enable", "disable"],
        },
        "ap-sniffer-data": {
            "type": "option",
            "help": "Enable/disable sniffer on WiFi data frame (default = enable).",
            "default": "enable",
            "options": ["enable", "disable"],
        },
        "sam-ssid": {
            "type": "string",
            "help": "SSID for WiFi network.",
            "default": "",
            "max_length": 32,
        },
        "sam-bssid": {
            "type": "mac-address",
            "help": "BSSID for WiFi network.",
            "default": "00:00:00:00:00:00",
        },
        "sam-security-type": {
            "type": "option",
            "help": "Select WiFi network security type (default = \"wpa-personal\" for 2.4/5G radio, \"wpa3-sae\" for 6G radio).",
            "default": "wpa-personal",
            "options": ["open", "wpa-personal", "wpa-enterprise", "wpa3-sae", "owe"],
        },
        "sam-captive-portal": {
            "type": "option",
            "help": "Enable/disable Captive Portal Authentication (default = disable).",
            "default": "disable",
            "options": ["enable", "disable"],
        },
        "sam-cwp-username": {
            "type": "string",
            "help": "Username for captive portal authentication.",
            "default": "",
            "max_length": 35,
        },
        "sam-cwp-password": {
            "type": "password",
            "help": "Password for captive portal authentication.",
            "max_length": 128,
        },
        "sam-cwp-test-url": {
            "type": "string",
            "help": "Website the client is trying to access.",
            "default": "",
            "max_length": 255,
        },
        "sam-cwp-match-string": {
            "type": "string",
            "help": "Identification string from the captive portal login form.",
            "default": "",
            "max_length": 64,
        },
        "sam-cwp-success-string": {
            "type": "string",
            "help": "Success identification on the page after a successful login.",
            "default": "",
            "max_length": 64,
        },
        "sam-cwp-failure-string": {
            "type": "string",
            "help": "Failure identification on the page after an incorrect login.",
            "default": "",
            "max_length": 64,
        },
        "sam-eap-method": {
            "type": "option",
            "help": "Select WPA2/WPA3-ENTERPRISE EAP Method (default = PEAP).",
            "default": "peap",
            "options": ["both", "tls", "peap"],
        },
        "sam-client-certificate": {
            "type": "string",
            "help": "Client certificate for WPA2/WPA3-ENTERPRISE.",
            "default": "",
            "max_length": 35,
        },
        "sam-private-key": {
            "type": "string",
            "help": "Private key for WPA2/WPA3-ENTERPRISE.",
            "default": "",
            "max_length": 35,
        },
        "sam-private-key-password": {
            "type": "password",
            "help": "Password for private key file for WPA2/WPA3-ENTERPRISE.",
            "max_length": 128,
        },
        "sam-ca-certificate": {
            "type": "string",
            "help": "CA certificate for WPA2/WPA3-ENTERPRISE.",
            "default": "",
            "max_length": 79,
        },
        "sam-username": {
            "type": "string",
            "help": "Username for WiFi network connection.",
            "default": "",
            "max_length": 35,
        },
        "sam-password": {
            "type": "password",
            "help": "Passphrase for WiFi network connection.",
            "max_length": 128,
        },
        "sam-test": {
            "type": "option",
            "help": "Select SAM test type (default = \"PING\").",
            "default": "ping",
            "options": ["ping", "iperf"],
        },
        "sam-server-type": {
            "type": "option",
            "help": "Select SAM server type (default = \"IP\").",
            "default": "ip",
            "options": ["ip", "fqdn"],
        },
        "sam-server-ip": {
            "type": "ipv4-address",
            "help": "SAM test server IP address.",
            "default": "0.0.0.0",
        },
        "sam-server-fqdn": {
            "type": "string",
            "help": "SAM test server domain name.",
            "default": "",
            "max_length": 255,
        },
        "iperf-server-port": {
            "type": "integer",
            "help": "Iperf service port number.",
            "default": 5001,
            "min_value": 0,
            "max_value": 65535,
        },
        "iperf-protocol": {
            "type": "option",
            "help": "Iperf test protocol (default = \"UDP\").",
            "default": "udp",
            "options": ["udp", "tcp"],
        },
        "sam-report-intv": {
            "type": "integer",
            "help": "SAM report interval (sec), 0 for a one-time report.",
            "default": 0,
            "min_value": 60,
            "max_value": 864000,
        },
        "channel-utilization": {
            "type": "option",
            "help": "Enable/disable measuring channel utilization.",
            "default": "enable",
            "options": ["enable", "disable"],
        },
        "wids-profile": {
            "type": "string",
            "help": "Wireless Intrusion Detection System (WIDS) profile name to assign to the radio.",
            "default": "",
            "max_length": 35,
        },
        "darrp": {
            "type": "option",
            "help": "Enable/disable Distributed Automatic Radio Resource Provisioning (DARRP) to make sure the radio is always using the most optimal channel (default = disable).",
            "default": "disable",
            "options": ["enable", "disable"],
        },
        "arrp-profile": {
            "type": "string",
            "help": "Distributed Automatic Radio Resource Provisioning (DARRP) profile name to assign to the radio.",
            "default": "",
            "max_length": 35,
        },
        "max-clients": {
            "type": "integer",
            "help": "Maximum number of stations (STAs) or WiFi clients supported by the radio. Range depends on the hardware.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "max-distance": {
            "type": "integer",
            "help": "Maximum expected distance between the AP and clients (0 - 54000 m, default = 0).",
            "default": 0,
            "min_value": 0,
            "max_value": 54000,
        },
        "vap-all": {
            "type": "option",
            "help": "Configure method for assigning SSIDs to this FortiAP (default = automatically assign tunnel SSIDs).",
            "default": "tunnel",
            "options": ["tunnel", "bridge", "manual"],
        },
        "vaps": {
            "type": "string",
            "help": "Manually selected list of Virtual Access Points (VAPs).",
        },
        "channel": {
            "type": "string",
            "help": "Selected list of wireless radio channels.",
        },
        "call-admission-control": {
            "type": "option",
            "help": "Enable/disable WiFi multimedia (WMM) call admission control to optimize WiFi bandwidth use for VoIP calls. New VoIP calls are only accepted if there is enough bandwidth available to support them.",
            "default": "disable",
            "options": ["enable", "disable"],
        },
        "call-capacity": {
            "type": "integer",
            "help": "Maximum number of Voice over WLAN (VoWLAN) phones supported by the radio (0 - 60, default = 10).",
            "default": 10,
            "min_value": 0,
            "max_value": 60,
        },
        "bandwidth-admission-control": {
            "type": "option",
            "help": "Enable/disable WiFi multimedia (WMM) bandwidth admission control to optimize WiFi bandwidth use. A request to join the wireless network is only allowed if the access point has enough bandwidth to support it.",
            "default": "disable",
            "options": ["enable", "disable"],
        },
        "bandwidth-capacity": {
            "type": "integer",
            "help": "Maximum bandwidth capacity allowed (1 - 600000 Kbps, default = 2000).",
            "default": 2000,
            "min_value": 1,
            "max_value": 600000,
        },
    },
    "radio-4": {
        "mode": {
            "type": "option",
            "help": "Mode of radio 4. Radio 4 can be disabled, configured as an access point, a rogue AP monitor, a sniffer, or a station.",
            "default": "ap",
            "options": ["disabled", "ap", "monitor", "sniffer", "sam"],
        },
        "band": {
            "type": "option",
            "help": "WiFi band that Radio 4 operates on.",
            "default": "",
            "options": ["802.11a", "802.11b", "802.11g", "802.11n-2G", "802.11n-5G", "802.11ac-2G", "802.11ac-5G", "802.11ax-2G", "802.11ax-5G", "802.11ax-6G", "802.11be-2G", "802.11be-5G", "802.11be-6G"],
        },
        "band-5g-type": {
            "type": "option",
            "help": "WiFi 5G band type.",
            "default": "5g-full",
            "options": ["5g-full", "5g-high", "5g-low"],
        },
        "drma": {
            "type": "option",
            "help": "Enable/disable dynamic radio mode assignment (DRMA) (default = disable).",
            "default": "disable",
            "options": ["disable", "enable"],
        },
        "drma-sensitivity": {
            "type": "option",
            "help": "Network Coverage Factor (NCF) percentage required to consider a radio as redundant (default = low).",
            "default": "low",
            "options": ["low", "medium", "high"],
        },
        "airtime-fairness": {
            "type": "option",
            "help": "Enable/disable airtime fairness (default = disable).",
            "default": "disable",
            "options": ["enable", "disable"],
        },
        "protection-mode": {
            "type": "option",
            "help": "Enable/disable 802.11g protection modes to support backwards compatibility with older clients (rtscts, ctsonly, disable).",
            "default": "disable",
            "options": ["rtscts", "ctsonly", "disable"],
        },
        "powersave-optimize": {
            "type": "option",
            "help": "Enable client power-saving features such as TIM, AC VO, and OBSS etc.",
            "default": "",
            "options": ["tim", "ac-vo", "no-obss-scan", "no-11b-rate", "client-rate-follow"],
        },
        "transmit-optimize": {
            "type": "option",
            "help": "Packet transmission optimization options including power saving, aggregation limiting, retry limiting, etc. All are enabled by default.",
            "default": "power-save aggr-limit retry-limit send-bar",
            "options": ["disable", "power-save", "aggr-limit", "retry-limit", "send-bar"],
        },
        "amsdu": {
            "type": "option",
            "help": "Enable/disable 802.11n AMSDU support. AMSDU can improve performance if supported by your WiFi clients (default = enable).",
            "default": "enable",
            "options": ["enable", "disable"],
        },
        "coexistence": {
            "type": "option",
            "help": "Enable/disable allowing both HT20 and HT40 on the same radio (default = enable).",
            "default": "enable",
            "options": ["enable", "disable"],
        },
        "zero-wait-dfs": {
            "type": "option",
            "help": "Enable/disable zero wait DFS on radio (default = enable).",
            "default": "enable",
            "options": ["enable", "disable"],
        },
        "bss-color": {
            "type": "integer",
            "help": "BSS color value for this 11ax radio (0 - 63, disable = 0, default = 0).",
            "default": 0,
            "min_value": 0,
            "max_value": 63,
        },
        "bss-color-mode": {
            "type": "option",
            "help": "BSS color mode for this 11ax radio (default = auto).",
            "default": "auto",
            "options": ["auto", "static"],
        },
        "short-guard-interval": {
            "type": "option",
            "help": "Use either the short guard interval (Short GI) of 400 ns or the long guard interval (Long GI) of 800 ns.",
            "default": "disable",
            "options": ["enable", "disable"],
        },
        "mimo-mode": {
            "type": "option",
            "help": "Configure radio MIMO mode (default = default).",
            "default": "default",
            "options": ["default", "1x1", "2x2", "3x3", "4x4", "8x8"],
        },
        "channel-bonding": {
            "type": "option",
            "help": "Channel bandwidth: 320, 240, 160, 80, 40, or 20MHz. Channels may use both 20 and 40 by enabling coexistence.",
            "default": "20MHz",
            "options": ["320MHz", "240MHz", "160MHz", "80MHz", "40MHz", "20MHz"],
        },
        "channel-bonding-ext": {
            "type": "option",
            "help": "Channel bandwidth extension: 320 MHz-1 and 320 MHz-2 (default = 320 MHz-2).",
            "default": "320MHz-2",
            "options": ["320MHz-1", "320MHz-2"],
        },
        "optional-antenna": {
            "type": "option",
            "help": "Optional antenna used on FAP (default = none).",
            "default": "none",
            "options": ["none", "custom", "FANT-04ABGN-0606-O-N", "FANT-04ABGN-1414-P-N", "FANT-04ABGN-8065-P-N", "FANT-04ABGN-0606-O-R", "FANT-04ABGN-0606-P-R", "FANT-10ACAX-1213-D-N", "FANT-08ABGN-1213-D-R", "FANT-04BEAX-0606-P-R"],
        },
        "optional-antenna-gain": {
            "type": "string",
            "help": "Optional antenna gain in dBi (0 to 20, default = 0).",
            "default": "0",
            "max_length": 7,
        },
        "auto-power-level": {
            "type": "option",
            "help": "Enable/disable automatic power-level adjustment to prevent co-channel interference (default = disable).",
            "default": "disable",
            "options": ["enable", "disable"],
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
            "options": ["dBm", "percentage"],
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
        "dtim": {
            "type": "integer",
            "help": "Delivery Traffic Indication Map (DTIM) period (1 - 255, default = 1). Set higher to save battery life of WiFi client in power-save mode.",
            "default": 1,
            "min_value": 1,
            "max_value": 255,
        },
        "beacon-interval": {
            "type": "integer",
            "help": "Beacon interval. The time between beacon frames in milliseconds. Actual range of beacon interval depends on the AP platform type (default = 100).",
            "default": 100,
            "min_value": 0,
            "max_value": 65535,
        },
        "80211d": {
            "type": "option",
            "help": "Enable/disable 802.11d countryie(default = enable).",
            "default": "enable",
            "options": ["enable", "disable"],
        },
        "80211mc": {
            "type": "option",
            "help": "Enable/disable 802.11mc responder mode (default = disable).",
            "default": "disable",
            "options": ["enable", "disable"],
        },
        "rts-threshold": {
            "type": "integer",
            "help": "Maximum packet size for RTS transmissions, specifying the maximum size of a data packet before RTS/CTS (256 - 2346 bytes, default = 2346).",
            "default": 2346,
            "min_value": 256,
            "max_value": 2346,
        },
        "frag-threshold": {
            "type": "integer",
            "help": "Maximum packet size that can be sent without fragmentation (800 - 2346 bytes, default = 2346).",
            "default": 2346,
            "min_value": 800,
            "max_value": 2346,
        },
        "ap-sniffer-bufsize": {
            "type": "integer",
            "help": "Sniffer buffer size (1 - 32 MB, default = 16).",
            "default": 16,
            "min_value": 1,
            "max_value": 32,
        },
        "ap-sniffer-chan": {
            "type": "integer",
            "help": "Channel on which to operate the sniffer (default = 6).",
            "default": 6,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "ap-sniffer-chan-width": {
            "type": "option",
            "help": "Channel bandwidth for sniffer.",
            "default": "20MHz",
            "options": ["320MHz", "240MHz", "160MHz", "80MHz", "40MHz", "20MHz"],
        },
        "ap-sniffer-addr": {
            "type": "mac-address",
            "help": "MAC address to monitor.",
            "default": "00:00:00:00:00:00",
        },
        "ap-sniffer-mgmt-beacon": {
            "type": "option",
            "help": "Enable/disable sniffer on WiFi management Beacon frames (default = enable).",
            "default": "enable",
            "options": ["enable", "disable"],
        },
        "ap-sniffer-mgmt-probe": {
            "type": "option",
            "help": "Enable/disable sniffer on WiFi management probe frames (default = enable).",
            "default": "enable",
            "options": ["enable", "disable"],
        },
        "ap-sniffer-mgmt-other": {
            "type": "option",
            "help": "Enable/disable sniffer on WiFi management other frames  (default = enable).",
            "default": "enable",
            "options": ["enable", "disable"],
        },
        "ap-sniffer-ctl": {
            "type": "option",
            "help": "Enable/disable sniffer on WiFi control frame (default = enable).",
            "default": "enable",
            "options": ["enable", "disable"],
        },
        "ap-sniffer-data": {
            "type": "option",
            "help": "Enable/disable sniffer on WiFi data frame (default = enable).",
            "default": "enable",
            "options": ["enable", "disable"],
        },
        "sam-ssid": {
            "type": "string",
            "help": "SSID for WiFi network.",
            "default": "",
            "max_length": 32,
        },
        "sam-bssid": {
            "type": "mac-address",
            "help": "BSSID for WiFi network.",
            "default": "00:00:00:00:00:00",
        },
        "sam-security-type": {
            "type": "option",
            "help": "Select WiFi network security type (default = \"wpa-personal\" for 2.4/5G radio, \"wpa3-sae\" for 6G radio).",
            "default": "wpa-personal",
            "options": ["open", "wpa-personal", "wpa-enterprise", "wpa3-sae", "owe"],
        },
        "sam-captive-portal": {
            "type": "option",
            "help": "Enable/disable Captive Portal Authentication (default = disable).",
            "default": "disable",
            "options": ["enable", "disable"],
        },
        "sam-cwp-username": {
            "type": "string",
            "help": "Username for captive portal authentication.",
            "default": "",
            "max_length": 35,
        },
        "sam-cwp-password": {
            "type": "password",
            "help": "Password for captive portal authentication.",
            "max_length": 128,
        },
        "sam-cwp-test-url": {
            "type": "string",
            "help": "Website the client is trying to access.",
            "default": "",
            "max_length": 255,
        },
        "sam-cwp-match-string": {
            "type": "string",
            "help": "Identification string from the captive portal login form.",
            "default": "",
            "max_length": 64,
        },
        "sam-cwp-success-string": {
            "type": "string",
            "help": "Success identification on the page after a successful login.",
            "default": "",
            "max_length": 64,
        },
        "sam-cwp-failure-string": {
            "type": "string",
            "help": "Failure identification on the page after an incorrect login.",
            "default": "",
            "max_length": 64,
        },
        "sam-eap-method": {
            "type": "option",
            "help": "Select WPA2/WPA3-ENTERPRISE EAP Method (default = PEAP).",
            "default": "peap",
            "options": ["both", "tls", "peap"],
        },
        "sam-client-certificate": {
            "type": "string",
            "help": "Client certificate for WPA2/WPA3-ENTERPRISE.",
            "default": "",
            "max_length": 35,
        },
        "sam-private-key": {
            "type": "string",
            "help": "Private key for WPA2/WPA3-ENTERPRISE.",
            "default": "",
            "max_length": 35,
        },
        "sam-private-key-password": {
            "type": "password",
            "help": "Password for private key file for WPA2/WPA3-ENTERPRISE.",
            "max_length": 128,
        },
        "sam-ca-certificate": {
            "type": "string",
            "help": "CA certificate for WPA2/WPA3-ENTERPRISE.",
            "default": "",
            "max_length": 79,
        },
        "sam-username": {
            "type": "string",
            "help": "Username for WiFi network connection.",
            "default": "",
            "max_length": 35,
        },
        "sam-password": {
            "type": "password",
            "help": "Passphrase for WiFi network connection.",
            "max_length": 128,
        },
        "sam-test": {
            "type": "option",
            "help": "Select SAM test type (default = \"PING\").",
            "default": "ping",
            "options": ["ping", "iperf"],
        },
        "sam-server-type": {
            "type": "option",
            "help": "Select SAM server type (default = \"IP\").",
            "default": "ip",
            "options": ["ip", "fqdn"],
        },
        "sam-server-ip": {
            "type": "ipv4-address",
            "help": "SAM test server IP address.",
            "default": "0.0.0.0",
        },
        "sam-server-fqdn": {
            "type": "string",
            "help": "SAM test server domain name.",
            "default": "",
            "max_length": 255,
        },
        "iperf-server-port": {
            "type": "integer",
            "help": "Iperf service port number.",
            "default": 5001,
            "min_value": 0,
            "max_value": 65535,
        },
        "iperf-protocol": {
            "type": "option",
            "help": "Iperf test protocol (default = \"UDP\").",
            "default": "udp",
            "options": ["udp", "tcp"],
        },
        "sam-report-intv": {
            "type": "integer",
            "help": "SAM report interval (sec), 0 for a one-time report.",
            "default": 0,
            "min_value": 60,
            "max_value": 864000,
        },
        "channel-utilization": {
            "type": "option",
            "help": "Enable/disable measuring channel utilization.",
            "default": "enable",
            "options": ["enable", "disable"],
        },
        "wids-profile": {
            "type": "string",
            "help": "Wireless Intrusion Detection System (WIDS) profile name to assign to the radio.",
            "default": "",
            "max_length": 35,
        },
        "darrp": {
            "type": "option",
            "help": "Enable/disable Distributed Automatic Radio Resource Provisioning (DARRP) to make sure the radio is always using the most optimal channel (default = disable).",
            "default": "disable",
            "options": ["enable", "disable"],
        },
        "arrp-profile": {
            "type": "string",
            "help": "Distributed Automatic Radio Resource Provisioning (DARRP) profile name to assign to the radio.",
            "default": "",
            "max_length": 35,
        },
        "max-clients": {
            "type": "integer",
            "help": "Maximum number of stations (STAs) or WiFi clients supported by the radio. Range depends on the hardware.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "max-distance": {
            "type": "integer",
            "help": "Maximum expected distance between the AP and clients (0 - 54000 m, default = 0).",
            "default": 0,
            "min_value": 0,
            "max_value": 54000,
        },
        "vap-all": {
            "type": "option",
            "help": "Configure method for assigning SSIDs to this FortiAP (default = automatically assign tunnel SSIDs).",
            "default": "tunnel",
            "options": ["tunnel", "bridge", "manual"],
        },
        "vaps": {
            "type": "string",
            "help": "Manually selected list of Virtual Access Points (VAPs).",
        },
        "channel": {
            "type": "string",
            "help": "Selected list of wireless radio channels.",
        },
        "call-admission-control": {
            "type": "option",
            "help": "Enable/disable WiFi multimedia (WMM) call admission control to optimize WiFi bandwidth use for VoIP calls. New VoIP calls are only accepted if there is enough bandwidth available to support them.",
            "default": "disable",
            "options": ["enable", "disable"],
        },
        "call-capacity": {
            "type": "integer",
            "help": "Maximum number of Voice over WLAN (VoWLAN) phones supported by the radio (0 - 60, default = 10).",
            "default": 10,
            "min_value": 0,
            "max_value": 60,
        },
        "bandwidth-admission-control": {
            "type": "option",
            "help": "Enable/disable WiFi multimedia (WMM) bandwidth admission control to optimize WiFi bandwidth use. A request to join the wireless network is only allowed if the access point has enough bandwidth to support it.",
            "default": "disable",
            "options": ["enable", "disable"],
        },
        "bandwidth-capacity": {
            "type": "integer",
            "help": "Maximum bandwidth capacity allowed (1 - 600000 Kbps, default = 2000).",
            "default": 2000,
            "min_value": 1,
            "max_value": 600000,
        },
    },
    "lbs": {
        "ekahau-blink-mode": {
            "type": "option",
            "help": "Enable/disable Ekahau blink mode (now known as AiRISTA Flow) to track and locate WiFi tags (default = disable).",
            "default": "disable",
            "options": ["enable", "disable"],
        },
        "ekahau-tag": {
            "type": "mac-address",
            "help": "WiFi frame MAC address or WiFi Tag.",
            "default": "01:18:8e:00:00:00",
        },
        "erc-server-ip": {
            "type": "ipv4-address-any",
            "help": "IP address of Ekahau RTLS Controller (ERC).",
            "default": "0.0.0.0",
        },
        "erc-server-port": {
            "type": "integer",
            "help": "Ekahau RTLS Controller (ERC) UDP listening port.",
            "default": 8569,
            "min_value": 1024,
            "max_value": 65535,
        },
        "aeroscout": {
            "type": "option",
            "help": "Enable/disable AeroScout Real Time Location Service (RTLS) support (default = disable).",
            "default": "disable",
            "options": ["enable", "disable"],
        },
        "aeroscout-server-ip": {
            "type": "ipv4-address-any",
            "help": "IP address of AeroScout server.",
            "default": "0.0.0.0",
        },
        "aeroscout-server-port": {
            "type": "integer",
            "help": "AeroScout server UDP listening port.",
            "default": 0,
            "min_value": 1024,
            "max_value": 65535,
        },
        "aeroscout-mu": {
            "type": "option",
            "help": "Enable/disable AeroScout Mobile Unit (MU) support (default = disable).",
            "default": "disable",
            "options": ["enable", "disable"],
        },
        "aeroscout-ap-mac": {
            "type": "option",
            "help": "Use BSSID or board MAC address as AP MAC address in AeroScout AP messages (default = bssid).",
            "default": "bssid",
            "options": ["bssid", "board-mac"],
        },
        "aeroscout-mmu-report": {
            "type": "option",
            "help": "Enable/disable compounded AeroScout tag and MU report (default = enable).",
            "default": "enable",
            "options": ["enable", "disable"],
        },
        "aeroscout-mu-factor": {
            "type": "integer",
            "help": "AeroScout MU mode dilution factor (default = 20).",
            "default": 20,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "aeroscout-mu-timeout": {
            "type": "integer",
            "help": "AeroScout MU mode timeout (0 - 65535 sec, default = 5).",
            "default": 5,
            "min_value": 0,
            "max_value": 65535,
        },
        "fortipresence": {
            "type": "option",
            "help": "Enable/disable FortiPresence to monitor the location and activity of WiFi clients even if they don't connect to this WiFi network (default = disable).",
            "default": "disable",
            "options": ["foreign", "both", "disable"],
        },
        "fortipresence-server-addr-type": {
            "type": "option",
            "help": "FortiPresence server address type (default = ipv4).",
            "default": "ipv4",
            "options": ["ipv4", "fqdn"],
        },
        "fortipresence-server": {
            "type": "ipv4-address-any",
            "help": "IP address of FortiPresence server.",
            "default": "0.0.0.0",
        },
        "fortipresence-server-fqdn": {
            "type": "string",
            "help": "FQDN of FortiPresence server.",
            "default": "",
            "max_length": 255,
        },
        "fortipresence-port": {
            "type": "integer",
            "help": "UDP listening port of FortiPresence server (default = 3000).",
            "default": 3000,
            "min_value": 300,
            "max_value": 65535,
        },
        "fortipresence-secret": {
            "type": "password",
            "help": "FortiPresence secret password (max. 16 characters).",
            "max_length": 123,
        },
        "fortipresence-project": {
            "type": "string",
            "help": "FortiPresence project name (max. 16 characters, default = fortipresence).",
            "default": "fortipresence",
            "max_length": 16,
        },
        "fortipresence-frequency": {
            "type": "integer",
            "help": "FortiPresence report transmit frequency (5 - 65535 sec, default = 30).",
            "default": 30,
            "min_value": 5,
            "max_value": 65535,
        },
        "fortipresence-rogue": {
            "type": "option",
            "help": "Enable/disable FortiPresence finding and reporting rogue APs.",
            "default": "disable",
            "options": ["enable", "disable"],
        },
        "fortipresence-unassoc": {
            "type": "option",
            "help": "Enable/disable FortiPresence finding and reporting unassociated stations.",
            "default": "enable",
            "options": ["enable", "disable"],
        },
        "fortipresence-ble": {
            "type": "option",
            "help": "Enable/disable FortiPresence finding and reporting BLE devices.",
            "default": "enable",
            "options": ["enable", "disable"],
        },
        "station-locate": {
            "type": "option",
            "help": "Enable/disable client station locating services for all clients, whether associated or not (default = disable).",
            "default": "disable",
            "options": ["enable", "disable"],
        },
        "ble-rtls": {
            "type": "option",
            "help": "Set BLE Real Time Location Service (RTLS) support (default = none).",
            "default": "none",
            "options": ["none", "polestar", "evresys"],
        },
        "ble-rtls-protocol": {
            "type": "option",
            "help": "Select the protocol to report Measurements, Advertising Data, or Location Data to Cloud Server (default = WSS).",
            "default": "WSS",
            "options": ["WSS"],
        },
        "ble-rtls-server-fqdn": {
            "type": "string",
            "help": "FQDN of BLE Real Time Location Service (RTLS) Server.",
            "default": "",
            "max_length": 255,
        },
        "ble-rtls-server-path": {
            "type": "string",
            "help": "Path of BLE Real Time Location Service (RTLS) Server.",
            "default": "",
            "max_length": 255,
        },
        "ble-rtls-server-token": {
            "type": "string",
            "help": "Access Token of BLE Real Time Location Service (RTLS) Server.",
            "default": "",
            "max_length": 31,
        },
        "ble-rtls-server-port": {
            "type": "integer",
            "help": "Port of BLE Real Time Location Service (RTLS) Server (default = 443).",
            "default": 443,
            "min_value": 1,
            "max_value": 65535,
        },
        "ble-rtls-accumulation-interval": {
            "type": "integer",
            "help": "Time that measurements should be accumulated in seconds (default = 2).",
            "default": 2,
            "min_value": 1,
            "max_value": 60,
        },
        "ble-rtls-reporting-interval": {
            "type": "integer",
            "help": "Time between reporting accumulated measurements in seconds (default = 2).",
            "default": 2,
            "min_value": 1,
            "max_value": 600,
        },
        "ble-rtls-asset-uuid-list1": {
            "type": "string",
            "help": "Tags and asset UUID list 1 to be reported (string in the format of 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX').",
            "default": "",
            "max_length": 36,
        },
        "ble-rtls-asset-uuid-list2": {
            "type": "string",
            "help": "Tags and asset UUID list 2 to be reported (string in the format of 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX').",
            "default": "",
            "max_length": 36,
        },
        "ble-rtls-asset-uuid-list3": {
            "type": "string",
            "help": "Tags and asset UUID list 3 to be reported (string in the format of 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX').",
            "default": "",
            "max_length": 36,
        },
        "ble-rtls-asset-uuid-list4": {
            "type": "string",
            "help": "Tags and asset UUID list 4 to be reported (string in the format of 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX').",
            "default": "",
            "max_length": 36,
        },
        "ble-rtls-asset-addrgrp-list": {
            "type": "string",
            "help": "Tags and asset addrgrp list to be reported.",
            "default": "",
            "max_length": 79,
        },
    },
    "esl-ses-dongle": {
        "compliance-level": {
            "type": "option",
            "help": "Compliance levels for the ESL solution integration (default = compliance-level-2).",
            "default": "compliance-level-2",
            "options": ["compliance-level-2"],
        },
        "scd-enable": {
            "type": "option",
            "help": "Enable/disable ESL SES-imagotag Serial Communication Daemon (SCD) (default = disable).",
            "default": "disable",
            "options": ["enable", "disable"],
        },
        "esl-channel": {
            "type": "option",
            "help": "ESL SES-imagotag dongle channel (default = 127).",
            "default": "127",
            "options": ["-1", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "127"],
        },
        "output-power": {
            "type": "option",
            "help": "ESL SES-imagotag dongle output power (default = A).",
            "default": "a",
            "options": ["a", "b", "c", "d", "e", "f", "g", "h"],
        },
        "apc-addr-type": {
            "type": "option",
            "help": "ESL SES-imagotag APC address type (default = fqdn).",
            "default": "fqdn",
            "options": ["fqdn", "ip"],
        },
        "apc-fqdn": {
            "type": "string",
            "help": "FQDN of ESL SES-imagotag Access Point Controller (APC).",
            "default": "",
            "max_length": 63,
        },
        "apc-ip": {
            "type": "ipv4-address",
            "help": "IP address of ESL SES-imagotag Access Point Controller (APC).",
            "default": "0.0.0.0",
        },
        "apc-port": {
            "type": "integer",
            "help": "Port of ESL SES-imagotag Access Point Controller (APC).",
            "default": 0,
            "min_value": 0,
            "max_value": 65535,
        },
        "coex-level": {
            "type": "option",
            "help": "ESL SES-imagotag dongle coexistence level (default = none).",
            "default": "none",
            "options": ["none"],
        },
        "tls-cert-verification": {
            "type": "option",
            "help": "Enable/disable TLS certificate verification (default = enable).",
            "default": "enable",
            "options": ["enable", "disable"],
        },
        "tls-fqdn-verification": {
            "type": "option",
            "help": "Enable/disable TLS FQDN verification (default = disable).",
            "default": "disable",
            "options": ["enable", "disable"],
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_CONTROL_MESSAGE_OFFLOAD = [
    "ebp-frame",
    "aeroscout-tag",
    "ap-list",
    "sta-list",
    "sta-cap-list",
    "stats",
    "aeroscout-mu",
    "sta-health",
    "spectral-analysis",
]
VALID_BODY_APCFG_MESH = [
    "enable",
    "disable",
]
VALID_BODY_APCFG_MESH_AP_TYPE = [
    "ethernet",
    "mesh",
    "auto",
]
VALID_BODY_APCFG_MESH_ETH_BRIDGE = [
    "enable",
    "disable",
]
VALID_BODY_WAN_PORT_MODE = [
    "wan-lan",
    "wan-only",
]
VALID_BODY_ENERGY_EFFICIENT_ETHERNET = [
    "enable",
    "disable",
]
VALID_BODY_LED_STATE = [
    "enable",
    "disable",
]
VALID_BODY_DTLS_POLICY = [
    "clear-text",
    "dtls-enabled",
    "ipsec-vpn",
    "ipsec-sn-vpn",
]
VALID_BODY_DTLS_IN_KERNEL = [
    "enable",
    "disable",
]
VALID_BODY_HANDOFF_ROAMING = [
    "enable",
    "disable",
]
VALID_BODY_AP_COUNTRY = [
    "--",
    "AF",
    "AL",
    "DZ",
    "AS",
    "AO",
    "AR",
    "AM",
    "AU",
    "AT",
    "AZ",
    "BS",
    "BH",
    "BD",
    "BB",
    "BY",
    "BE",
    "BZ",
    "BJ",
    "BM",
    "BT",
    "BO",
    "BA",
    "BW",
    "BR",
    "BN",
    "BG",
    "BF",
    "KH",
    "CM",
    "KY",
    "CF",
    "TD",
    "CL",
    "CN",
    "CX",
    "CO",
    "CG",
    "CD",
    "CR",
    "HR",
    "CY",
    "CZ",
    "DK",
    "DJ",
    "DM",
    "DO",
    "EC",
    "EG",
    "SV",
    "ET",
    "EE",
    "GF",
    "PF",
    "FO",
    "FJ",
    "FI",
    "FR",
    "GA",
    "GE",
    "GM",
    "DE",
    "GH",
    "GI",
    "GR",
    "GL",
    "GD",
    "GP",
    "GU",
    "GT",
    "GY",
    "HT",
    "HN",
    "HK",
    "HU",
    "IS",
    "IN",
    "ID",
    "IQ",
    "IE",
    "IM",
    "IL",
    "IT",
    "CI",
    "JM",
    "JO",
    "KZ",
    "KE",
    "KR",
    "KW",
    "LA",
    "LV",
    "LB",
    "LS",
    "LR",
    "LY",
    "LI",
    "LT",
    "LU",
    "MO",
    "MK",
    "MG",
    "MW",
    "MY",
    "MV",
    "ML",
    "MT",
    "MH",
    "MQ",
    "MR",
    "MU",
    "YT",
    "MX",
    "FM",
    "MD",
    "MC",
    "MN",
    "MA",
    "MZ",
    "MM",
    "NA",
    "NP",
    "NL",
    "AN",
    "AW",
    "NZ",
    "NI",
    "NE",
    "NG",
    "NO",
    "MP",
    "OM",
    "PK",
    "PW",
    "PA",
    "PG",
    "PY",
    "PE",
    "PH",
    "PL",
    "PT",
    "PR",
    "QA",
    "RE",
    "RO",
    "RU",
    "RW",
    "BL",
    "KN",
    "LC",
    "MF",
    "PM",
    "VC",
    "SA",
    "SN",
    "RS",
    "ME",
    "SL",
    "SG",
    "SK",
    "SI",
    "SO",
    "ZA",
    "ES",
    "LK",
    "SR",
    "SZ",
    "SE",
    "CH",
    "TW",
    "TZ",
    "TH",
    "TL",
    "TG",
    "TT",
    "TN",
    "TR",
    "TM",
    "AE",
    "TC",
    "UG",
    "UA",
    "GB",
    "US",
    "PS",
    "UY",
    "UZ",
    "VU",
    "VE",
    "VN",
    "VI",
    "WF",
    "YE",
    "ZM",
    "ZW",
    "JP",
    "CA",
]
VALID_BODY_IP_FRAGMENT_PREVENTING = [
    "tcp-mss-adjust",
    "icmp-unreachable",
]
VALID_BODY_SPLIT_TUNNELING_ACL_PATH = [
    "tunnel",
    "local",
]
VALID_BODY_SPLIT_TUNNELING_ACL_LOCAL_AP_SUBNET = [
    "enable",
    "disable",
]
VALID_BODY_ALLOWACCESS = [
    "https",
    "ssh",
    "snmp",
]
VALID_BODY_LOGIN_PASSWD_CHANGE = [
    "yes",
    "default",
    "no",
]
VALID_BODY_LLDP = [
    "enable",
    "disable",
]
VALID_BODY_POE_MODE = [
    "auto",
    "8023af",
    "8023at",
    "power-adapter",
    "full",
    "high",
    "low",
]
VALID_BODY_USB_PORT = [
    "enable",
    "disable",
]
VALID_BODY_FREQUENCY_HANDOFF = [
    "enable",
    "disable",
]
VALID_BODY_AP_HANDOFF = [
    "enable",
    "disable",
]
VALID_BODY_DEFAULT_MESH_ROOT = [
    "enable",
    "disable",
]
VALID_BODY_EXT_INFO_ENABLE = [
    "enable",
    "disable",
]
VALID_BODY_INDOOR_OUTDOOR_DEPLOYMENT = [
    "platform-determined",
    "outdoor",
    "indoor",
]
VALID_BODY_CONSOLE_LOGIN = [
    "enable",
    "disable",
]
VALID_BODY_WAN_PORT_AUTH = [
    "none",
    "802.1x",
]
VALID_BODY_WAN_PORT_AUTH_METHODS = [
    "all",
    "EAP-FAST",
    "EAP-TLS",
    "EAP-PEAP",
]
VALID_BODY_WAN_PORT_AUTH_MACSEC = [
    "enable",
    "disable",
]
VALID_BODY_UNII_4_5GHZ_BAND = [
    "enable",
    "disable",
]
VALID_BODY_ADMIN_RESTRICT_LOCAL = [
    "enable",
    "disable",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_wireless_controller_wtp_profile_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for wireless_controller/wtp_profile.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_wireless_controller_wtp_profile_get()
        >>> assert is_valid == True
        
        >>> # Valid - Get specific item by name
        >>> is_valid, error = validate_wireless_controller_wtp_profile_get(name="test-item")
        >>> assert is_valid == True
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_wireless_controller_wtp_profile_get(
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
    Validate required fields for wireless_controller/wtp_profile.

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


def validate_wireless_controller_wtp_profile_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new wireless_controller/wtp_profile object.

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
        ... }
        >>> is_valid, error = validate_wireless_controller_wtp_profile_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "control-message-offload": "ebp-frame",  # Valid enum value
        ... }
        >>> is_valid, error = validate_wireless_controller_wtp_profile_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["control-message-offload"] = "invalid-value"
        >>> is_valid, error = validate_wireless_controller_wtp_profile_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_wireless_controller_wtp_profile_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "control-message-offload" in payload:
        value = payload["control-message-offload"]
        if value not in VALID_BODY_CONTROL_MESSAGE_OFFLOAD:
            desc = FIELD_DESCRIPTIONS.get("control-message-offload", "")
            error_msg = f"Invalid value for 'control-message-offload': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CONTROL_MESSAGE_OFFLOAD)}"
            error_msg += f"\n  → Example: control-message-offload='{{ VALID_BODY_CONTROL_MESSAGE_OFFLOAD[0] }}'"
            return (False, error_msg)
    if "apcfg-mesh" in payload:
        value = payload["apcfg-mesh"]
        if value not in VALID_BODY_APCFG_MESH:
            desc = FIELD_DESCRIPTIONS.get("apcfg-mesh", "")
            error_msg = f"Invalid value for 'apcfg-mesh': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_APCFG_MESH)}"
            error_msg += f"\n  → Example: apcfg-mesh='{{ VALID_BODY_APCFG_MESH[0] }}'"
            return (False, error_msg)
    if "apcfg-mesh-ap-type" in payload:
        value = payload["apcfg-mesh-ap-type"]
        if value not in VALID_BODY_APCFG_MESH_AP_TYPE:
            desc = FIELD_DESCRIPTIONS.get("apcfg-mesh-ap-type", "")
            error_msg = f"Invalid value for 'apcfg-mesh-ap-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_APCFG_MESH_AP_TYPE)}"
            error_msg += f"\n  → Example: apcfg-mesh-ap-type='{{ VALID_BODY_APCFG_MESH_AP_TYPE[0] }}'"
            return (False, error_msg)
    if "apcfg-mesh-eth-bridge" in payload:
        value = payload["apcfg-mesh-eth-bridge"]
        if value not in VALID_BODY_APCFG_MESH_ETH_BRIDGE:
            desc = FIELD_DESCRIPTIONS.get("apcfg-mesh-eth-bridge", "")
            error_msg = f"Invalid value for 'apcfg-mesh-eth-bridge': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_APCFG_MESH_ETH_BRIDGE)}"
            error_msg += f"\n  → Example: apcfg-mesh-eth-bridge='{{ VALID_BODY_APCFG_MESH_ETH_BRIDGE[0] }}'"
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
    if "energy-efficient-ethernet" in payload:
        value = payload["energy-efficient-ethernet"]
        if value not in VALID_BODY_ENERGY_EFFICIENT_ETHERNET:
            desc = FIELD_DESCRIPTIONS.get("energy-efficient-ethernet", "")
            error_msg = f"Invalid value for 'energy-efficient-ethernet': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ENERGY_EFFICIENT_ETHERNET)}"
            error_msg += f"\n  → Example: energy-efficient-ethernet='{{ VALID_BODY_ENERGY_EFFICIENT_ETHERNET[0] }}'"
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
    if "dtls-policy" in payload:
        value = payload["dtls-policy"]
        if value not in VALID_BODY_DTLS_POLICY:
            desc = FIELD_DESCRIPTIONS.get("dtls-policy", "")
            error_msg = f"Invalid value for 'dtls-policy': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DTLS_POLICY)}"
            error_msg += f"\n  → Example: dtls-policy='{{ VALID_BODY_DTLS_POLICY[0] }}'"
            return (False, error_msg)
    if "dtls-in-kernel" in payload:
        value = payload["dtls-in-kernel"]
        if value not in VALID_BODY_DTLS_IN_KERNEL:
            desc = FIELD_DESCRIPTIONS.get("dtls-in-kernel", "")
            error_msg = f"Invalid value for 'dtls-in-kernel': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DTLS_IN_KERNEL)}"
            error_msg += f"\n  → Example: dtls-in-kernel='{{ VALID_BODY_DTLS_IN_KERNEL[0] }}'"
            return (False, error_msg)
    if "handoff-roaming" in payload:
        value = payload["handoff-roaming"]
        if value not in VALID_BODY_HANDOFF_ROAMING:
            desc = FIELD_DESCRIPTIONS.get("handoff-roaming", "")
            error_msg = f"Invalid value for 'handoff-roaming': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_HANDOFF_ROAMING)}"
            error_msg += f"\n  → Example: handoff-roaming='{{ VALID_BODY_HANDOFF_ROAMING[0] }}'"
            return (False, error_msg)
    if "ap-country" in payload:
        value = payload["ap-country"]
        if value not in VALID_BODY_AP_COUNTRY:
            desc = FIELD_DESCRIPTIONS.get("ap-country", "")
            error_msg = f"Invalid value for 'ap-country': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AP_COUNTRY)}"
            error_msg += f"\n  → Example: ap-country='{{ VALID_BODY_AP_COUNTRY[0] }}'"
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
    if "lldp" in payload:
        value = payload["lldp"]
        if value not in VALID_BODY_LLDP:
            desc = FIELD_DESCRIPTIONS.get("lldp", "")
            error_msg = f"Invalid value for 'lldp': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LLDP)}"
            error_msg += f"\n  → Example: lldp='{{ VALID_BODY_LLDP[0] }}'"
            return (False, error_msg)
    if "poe-mode" in payload:
        value = payload["poe-mode"]
        if value not in VALID_BODY_POE_MODE:
            desc = FIELD_DESCRIPTIONS.get("poe-mode", "")
            error_msg = f"Invalid value for 'poe-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_POE_MODE)}"
            error_msg += f"\n  → Example: poe-mode='{{ VALID_BODY_POE_MODE[0] }}'"
            return (False, error_msg)
    if "usb-port" in payload:
        value = payload["usb-port"]
        if value not in VALID_BODY_USB_PORT:
            desc = FIELD_DESCRIPTIONS.get("usb-port", "")
            error_msg = f"Invalid value for 'usb-port': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_USB_PORT)}"
            error_msg += f"\n  → Example: usb-port='{{ VALID_BODY_USB_PORT[0] }}'"
            return (False, error_msg)
    if "frequency-handoff" in payload:
        value = payload["frequency-handoff"]
        if value not in VALID_BODY_FREQUENCY_HANDOFF:
            desc = FIELD_DESCRIPTIONS.get("frequency-handoff", "")
            error_msg = f"Invalid value for 'frequency-handoff': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FREQUENCY_HANDOFF)}"
            error_msg += f"\n  → Example: frequency-handoff='{{ VALID_BODY_FREQUENCY_HANDOFF[0] }}'"
            return (False, error_msg)
    if "ap-handoff" in payload:
        value = payload["ap-handoff"]
        if value not in VALID_BODY_AP_HANDOFF:
            desc = FIELD_DESCRIPTIONS.get("ap-handoff", "")
            error_msg = f"Invalid value for 'ap-handoff': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AP_HANDOFF)}"
            error_msg += f"\n  → Example: ap-handoff='{{ VALID_BODY_AP_HANDOFF[0] }}'"
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
    if "ext-info-enable" in payload:
        value = payload["ext-info-enable"]
        if value not in VALID_BODY_EXT_INFO_ENABLE:
            desc = FIELD_DESCRIPTIONS.get("ext-info-enable", "")
            error_msg = f"Invalid value for 'ext-info-enable': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EXT_INFO_ENABLE)}"
            error_msg += f"\n  → Example: ext-info-enable='{{ VALID_BODY_EXT_INFO_ENABLE[0] }}'"
            return (False, error_msg)
    if "indoor-outdoor-deployment" in payload:
        value = payload["indoor-outdoor-deployment"]
        if value not in VALID_BODY_INDOOR_OUTDOOR_DEPLOYMENT:
            desc = FIELD_DESCRIPTIONS.get("indoor-outdoor-deployment", "")
            error_msg = f"Invalid value for 'indoor-outdoor-deployment': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_INDOOR_OUTDOOR_DEPLOYMENT)}"
            error_msg += f"\n  → Example: indoor-outdoor-deployment='{{ VALID_BODY_INDOOR_OUTDOOR_DEPLOYMENT[0] }}'"
            return (False, error_msg)
    if "console-login" in payload:
        value = payload["console-login"]
        if value not in VALID_BODY_CONSOLE_LOGIN:
            desc = FIELD_DESCRIPTIONS.get("console-login", "")
            error_msg = f"Invalid value for 'console-login': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CONSOLE_LOGIN)}"
            error_msg += f"\n  → Example: console-login='{{ VALID_BODY_CONSOLE_LOGIN[0] }}'"
            return (False, error_msg)
    if "wan-port-auth" in payload:
        value = payload["wan-port-auth"]
        if value not in VALID_BODY_WAN_PORT_AUTH:
            desc = FIELD_DESCRIPTIONS.get("wan-port-auth", "")
            error_msg = f"Invalid value for 'wan-port-auth': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WAN_PORT_AUTH)}"
            error_msg += f"\n  → Example: wan-port-auth='{{ VALID_BODY_WAN_PORT_AUTH[0] }}'"
            return (False, error_msg)
    if "wan-port-auth-methods" in payload:
        value = payload["wan-port-auth-methods"]
        if value not in VALID_BODY_WAN_PORT_AUTH_METHODS:
            desc = FIELD_DESCRIPTIONS.get("wan-port-auth-methods", "")
            error_msg = f"Invalid value for 'wan-port-auth-methods': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WAN_PORT_AUTH_METHODS)}"
            error_msg += f"\n  → Example: wan-port-auth-methods='{{ VALID_BODY_WAN_PORT_AUTH_METHODS[0] }}'"
            return (False, error_msg)
    if "wan-port-auth-macsec" in payload:
        value = payload["wan-port-auth-macsec"]
        if value not in VALID_BODY_WAN_PORT_AUTH_MACSEC:
            desc = FIELD_DESCRIPTIONS.get("wan-port-auth-macsec", "")
            error_msg = f"Invalid value for 'wan-port-auth-macsec': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WAN_PORT_AUTH_MACSEC)}"
            error_msg += f"\n  → Example: wan-port-auth-macsec='{{ VALID_BODY_WAN_PORT_AUTH_MACSEC[0] }}'"
            return (False, error_msg)
    if "unii-4-5ghz-band" in payload:
        value = payload["unii-4-5ghz-band"]
        if value not in VALID_BODY_UNII_4_5GHZ_BAND:
            desc = FIELD_DESCRIPTIONS.get("unii-4-5ghz-band", "")
            error_msg = f"Invalid value for 'unii-4-5ghz-band': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_UNII_4_5GHZ_BAND)}"
            error_msg += f"\n  → Example: unii-4-5ghz-band='{{ VALID_BODY_UNII_4_5GHZ_BAND[0] }}'"
            return (False, error_msg)
    if "admin-restrict-local" in payload:
        value = payload["admin-restrict-local"]
        if value not in VALID_BODY_ADMIN_RESTRICT_LOCAL:
            desc = FIELD_DESCRIPTIONS.get("admin-restrict-local", "")
            error_msg = f"Invalid value for 'admin-restrict-local': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADMIN_RESTRICT_LOCAL)}"
            error_msg += f"\n  → Example: admin-restrict-local='{{ VALID_BODY_ADMIN_RESTRICT_LOCAL[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_wireless_controller_wtp_profile_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update wireless_controller/wtp_profile.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_wireless_controller_wtp_profile_put(payload)
    """
    # Step 1: Validate enum values
    if "control-message-offload" in payload:
        value = payload["control-message-offload"]
        if value not in VALID_BODY_CONTROL_MESSAGE_OFFLOAD:
            return (
                False,
                f"Invalid value for 'control-message-offload'='{value}'. Must be one of: {', '.join(VALID_BODY_CONTROL_MESSAGE_OFFLOAD)}",
            )
    if "apcfg-mesh" in payload:
        value = payload["apcfg-mesh"]
        if value not in VALID_BODY_APCFG_MESH:
            return (
                False,
                f"Invalid value for 'apcfg-mesh'='{value}'. Must be one of: {', '.join(VALID_BODY_APCFG_MESH)}",
            )
    if "apcfg-mesh-ap-type" in payload:
        value = payload["apcfg-mesh-ap-type"]
        if value not in VALID_BODY_APCFG_MESH_AP_TYPE:
            return (
                False,
                f"Invalid value for 'apcfg-mesh-ap-type'='{value}'. Must be one of: {', '.join(VALID_BODY_APCFG_MESH_AP_TYPE)}",
            )
    if "apcfg-mesh-eth-bridge" in payload:
        value = payload["apcfg-mesh-eth-bridge"]
        if value not in VALID_BODY_APCFG_MESH_ETH_BRIDGE:
            return (
                False,
                f"Invalid value for 'apcfg-mesh-eth-bridge'='{value}'. Must be one of: {', '.join(VALID_BODY_APCFG_MESH_ETH_BRIDGE)}",
            )
    if "wan-port-mode" in payload:
        value = payload["wan-port-mode"]
        if value not in VALID_BODY_WAN_PORT_MODE:
            return (
                False,
                f"Invalid value for 'wan-port-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_WAN_PORT_MODE)}",
            )
    if "energy-efficient-ethernet" in payload:
        value = payload["energy-efficient-ethernet"]
        if value not in VALID_BODY_ENERGY_EFFICIENT_ETHERNET:
            return (
                False,
                f"Invalid value for 'energy-efficient-ethernet'='{value}'. Must be one of: {', '.join(VALID_BODY_ENERGY_EFFICIENT_ETHERNET)}",
            )
    if "led-state" in payload:
        value = payload["led-state"]
        if value not in VALID_BODY_LED_STATE:
            return (
                False,
                f"Invalid value for 'led-state'='{value}'. Must be one of: {', '.join(VALID_BODY_LED_STATE)}",
            )
    if "dtls-policy" in payload:
        value = payload["dtls-policy"]
        if value not in VALID_BODY_DTLS_POLICY:
            return (
                False,
                f"Invalid value for 'dtls-policy'='{value}'. Must be one of: {', '.join(VALID_BODY_DTLS_POLICY)}",
            )
    if "dtls-in-kernel" in payload:
        value = payload["dtls-in-kernel"]
        if value not in VALID_BODY_DTLS_IN_KERNEL:
            return (
                False,
                f"Invalid value for 'dtls-in-kernel'='{value}'. Must be one of: {', '.join(VALID_BODY_DTLS_IN_KERNEL)}",
            )
    if "handoff-roaming" in payload:
        value = payload["handoff-roaming"]
        if value not in VALID_BODY_HANDOFF_ROAMING:
            return (
                False,
                f"Invalid value for 'handoff-roaming'='{value}'. Must be one of: {', '.join(VALID_BODY_HANDOFF_ROAMING)}",
            )
    if "ap-country" in payload:
        value = payload["ap-country"]
        if value not in VALID_BODY_AP_COUNTRY:
            return (
                False,
                f"Invalid value for 'ap-country'='{value}'. Must be one of: {', '.join(VALID_BODY_AP_COUNTRY)}",
            )
    if "ip-fragment-preventing" in payload:
        value = payload["ip-fragment-preventing"]
        if value not in VALID_BODY_IP_FRAGMENT_PREVENTING:
            return (
                False,
                f"Invalid value for 'ip-fragment-preventing'='{value}'. Must be one of: {', '.join(VALID_BODY_IP_FRAGMENT_PREVENTING)}",
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
    if "allowaccess" in payload:
        value = payload["allowaccess"]
        if value not in VALID_BODY_ALLOWACCESS:
            return (
                False,
                f"Invalid value for 'allowaccess'='{value}'. Must be one of: {', '.join(VALID_BODY_ALLOWACCESS)}",
            )
    if "login-passwd-change" in payload:
        value = payload["login-passwd-change"]
        if value not in VALID_BODY_LOGIN_PASSWD_CHANGE:
            return (
                False,
                f"Invalid value for 'login-passwd-change'='{value}'. Must be one of: {', '.join(VALID_BODY_LOGIN_PASSWD_CHANGE)}",
            )
    if "lldp" in payload:
        value = payload["lldp"]
        if value not in VALID_BODY_LLDP:
            return (
                False,
                f"Invalid value for 'lldp'='{value}'. Must be one of: {', '.join(VALID_BODY_LLDP)}",
            )
    if "poe-mode" in payload:
        value = payload["poe-mode"]
        if value not in VALID_BODY_POE_MODE:
            return (
                False,
                f"Invalid value for 'poe-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_POE_MODE)}",
            )
    if "usb-port" in payload:
        value = payload["usb-port"]
        if value not in VALID_BODY_USB_PORT:
            return (
                False,
                f"Invalid value for 'usb-port'='{value}'. Must be one of: {', '.join(VALID_BODY_USB_PORT)}",
            )
    if "frequency-handoff" in payload:
        value = payload["frequency-handoff"]
        if value not in VALID_BODY_FREQUENCY_HANDOFF:
            return (
                False,
                f"Invalid value for 'frequency-handoff'='{value}'. Must be one of: {', '.join(VALID_BODY_FREQUENCY_HANDOFF)}",
            )
    if "ap-handoff" in payload:
        value = payload["ap-handoff"]
        if value not in VALID_BODY_AP_HANDOFF:
            return (
                False,
                f"Invalid value for 'ap-handoff'='{value}'. Must be one of: {', '.join(VALID_BODY_AP_HANDOFF)}",
            )
    if "default-mesh-root" in payload:
        value = payload["default-mesh-root"]
        if value not in VALID_BODY_DEFAULT_MESH_ROOT:
            return (
                False,
                f"Invalid value for 'default-mesh-root'='{value}'. Must be one of: {', '.join(VALID_BODY_DEFAULT_MESH_ROOT)}",
            )
    if "ext-info-enable" in payload:
        value = payload["ext-info-enable"]
        if value not in VALID_BODY_EXT_INFO_ENABLE:
            return (
                False,
                f"Invalid value for 'ext-info-enable'='{value}'. Must be one of: {', '.join(VALID_BODY_EXT_INFO_ENABLE)}",
            )
    if "indoor-outdoor-deployment" in payload:
        value = payload["indoor-outdoor-deployment"]
        if value not in VALID_BODY_INDOOR_OUTDOOR_DEPLOYMENT:
            return (
                False,
                f"Invalid value for 'indoor-outdoor-deployment'='{value}'. Must be one of: {', '.join(VALID_BODY_INDOOR_OUTDOOR_DEPLOYMENT)}",
            )
    if "console-login" in payload:
        value = payload["console-login"]
        if value not in VALID_BODY_CONSOLE_LOGIN:
            return (
                False,
                f"Invalid value for 'console-login'='{value}'. Must be one of: {', '.join(VALID_BODY_CONSOLE_LOGIN)}",
            )
    if "wan-port-auth" in payload:
        value = payload["wan-port-auth"]
        if value not in VALID_BODY_WAN_PORT_AUTH:
            return (
                False,
                f"Invalid value for 'wan-port-auth'='{value}'. Must be one of: {', '.join(VALID_BODY_WAN_PORT_AUTH)}",
            )
    if "wan-port-auth-methods" in payload:
        value = payload["wan-port-auth-methods"]
        if value not in VALID_BODY_WAN_PORT_AUTH_METHODS:
            return (
                False,
                f"Invalid value for 'wan-port-auth-methods'='{value}'. Must be one of: {', '.join(VALID_BODY_WAN_PORT_AUTH_METHODS)}",
            )
    if "wan-port-auth-macsec" in payload:
        value = payload["wan-port-auth-macsec"]
        if value not in VALID_BODY_WAN_PORT_AUTH_MACSEC:
            return (
                False,
                f"Invalid value for 'wan-port-auth-macsec'='{value}'. Must be one of: {', '.join(VALID_BODY_WAN_PORT_AUTH_MACSEC)}",
            )
    if "unii-4-5ghz-band" in payload:
        value = payload["unii-4-5ghz-band"]
        if value not in VALID_BODY_UNII_4_5GHZ_BAND:
            return (
                False,
                f"Invalid value for 'unii-4-5ghz-band'='{value}'. Must be one of: {', '.join(VALID_BODY_UNII_4_5GHZ_BAND)}",
            )
    if "admin-restrict-local" in payload:
        value = payload["admin-restrict-local"]
        if value not in VALID_BODY_ADMIN_RESTRICT_LOCAL:
            return (
                False,
                f"Invalid value for 'admin-restrict-local'='{value}'. Must be one of: {', '.join(VALID_BODY_ADMIN_RESTRICT_LOCAL)}",
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
    constant_name = f"VALID_BODY_{field_name.replace('-', '_').upper()}"
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
    "endpoint": "wireless_controller/wtp_profile",
    "category": "cmdb",
    "api_path": "wireless-controller/wtp-profile",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure WTP profiles or FortiAP profiles that define radio settings for manageable FortiAP platforms.",
    "total_fields": 57,
    "required_fields_count": 0,
    "fields_with_defaults_count": 43,
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
