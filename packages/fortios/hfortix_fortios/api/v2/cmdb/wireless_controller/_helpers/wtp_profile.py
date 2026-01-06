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
    "lw-profile": "",
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
    "apcfg-auto-cert": "disable",
    "apcfg-auto-cert-enroll-protocol": "none",
    "apcfg-auto-cert-crypto-algo": "ec-secp256r1",
    "apcfg-auto-cert-est-server": "",
    "apcfg-auto-cert-est-ca-id": "",
    "apcfg-auto-cert-est-http-username": "",
    "apcfg-auto-cert-est-subject": "CN=FortiAP,DC=local,DC=COM",
    "apcfg-auto-cert-est-subject-alt-name": "",
    "apcfg-auto-cert-auto-regen-days": 30,
    "apcfg-auto-cert-est-https-ca": "",
    "apcfg-auto-cert-scep-keytype": "rsa",
    "apcfg-auto-cert-scep-keysize": "2048",
    "apcfg-auto-cert-scep-ec-name": "secp256r1",
    "apcfg-auto-cert-scep-sub-fully-dn": "",
    "apcfg-auto-cert-scep-url": "",
    "apcfg-auto-cert-scep-ca-id": "",
    "apcfg-auto-cert-scep-subject-alt-name": "",
    "apcfg-auto-cert-scep-https-ca": "",
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
    "lw-profile": "string",  # LoRaWAN profile name.
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
    "apcfg-auto-cert": "option",  # Enable/disable AP local auto cert configuration (default = d
    "apcfg-auto-cert-enroll-protocol": "option",  # Certificate enrollment protocol (default = none)
    "apcfg-auto-cert-crypto-algo": "option",  # Cryptography algorithm: rsa-1024, rsa-1536, rsa-2048, rsa-40
    "apcfg-auto-cert-est-server": "string",  # Address and port for EST server (e.g. https://example.com:12
    "apcfg-auto-cert-est-ca-id": "string",  # CA identifier of the CA server for signing via EST.
    "apcfg-auto-cert-est-http-username": "string",  # HTTP Authentication username for signing via EST.
    "apcfg-auto-cert-est-http-password": "password",  # HTTP Authentication password for signing via EST.
    "apcfg-auto-cert-est-subject": "string",  # Subject e.g. "CN=User,DC=example,DC=COM" (default = CN=Forti
    "apcfg-auto-cert-est-subject-alt-name": "string",  # Subject alternative name (optional, e.g. "DNS:dns1.com,IP:19
    "apcfg-auto-cert-auto-regen-days": "integer",  # Number of days to wait before expiry of an updated local cer
    "apcfg-auto-cert-est-https-ca": "string",  # PEM format https CA Certificate.
    "apcfg-auto-cert-scep-keytype": "option",  # Key type (default = rsa)
    "apcfg-auto-cert-scep-keysize": "option",  # Key size: 1024, 1536, 2048, 4096 (default 2048).
    "apcfg-auto-cert-scep-ec-name": "option",  # Elliptic curve name: secp256r1, secp384r1 and secp521r1. (de
    "apcfg-auto-cert-scep-sub-fully-dn": "string",  # Full DN of the subject (e.g C=US,ST=CA,L=Sunnyvale,O=Fortine
    "apcfg-auto-cert-scep-url": "string",  # SCEP server URL.
    "apcfg-auto-cert-scep-password": "password",  # SCEP server challenge password for auto-regeneration.
    "apcfg-auto-cert-scep-ca-id": "string",  # CA identifier of the CA server for signing via SCEP.
    "apcfg-auto-cert-scep-subject-alt-name": "string",  # Subject alternative name (optional, e.g. "DNS:dns1.com,IP:19
    "apcfg-auto-cert-scep-https-ca": "string",  # PEM format https CA Certificate.
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
    "lw-profile": "LoRaWAN profile name.",
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
    "handoff-roaming": "Enable/disable client load balancing during roaming to avoid roaming delay (default = enable).",
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
    "apcfg-auto-cert": "Enable/disable AP local auto cert configuration (default = disable).",
    "apcfg-auto-cert-enroll-protocol": "Certificate enrollment protocol (default = none)",
    "apcfg-auto-cert-crypto-algo": "Cryptography algorithm: rsa-1024, rsa-1536, rsa-2048, rsa-4096, ec-secp256r1, ec-secp384r1, ec-secp521r1 (default = ec-secp256r1)",
    "apcfg-auto-cert-est-server": "Address and port for EST server (e.g. https://example.com:1234).",
    "apcfg-auto-cert-est-ca-id": "CA identifier of the CA server for signing via EST.",
    "apcfg-auto-cert-est-http-username": "HTTP Authentication username for signing via EST.",
    "apcfg-auto-cert-est-http-password": "HTTP Authentication password for signing via EST.",
    "apcfg-auto-cert-est-subject": "Subject e.g. \"CN=User,DC=example,DC=COM\" (default = CN=FortiAP,DC=local,DC=COM)",
    "apcfg-auto-cert-est-subject-alt-name": "Subject alternative name (optional, e.g. \"DNS:dns1.com,IP:192.168.1.99\")",
    "apcfg-auto-cert-auto-regen-days": "Number of days to wait before expiry of an updated local certificate is requested (0 = disabled) (default = 30).",
    "apcfg-auto-cert-est-https-ca": "PEM format https CA Certificate.",
    "apcfg-auto-cert-scep-keytype": "Key type (default = rsa)",
    "apcfg-auto-cert-scep-keysize": "Key size: 1024, 1536, 2048, 4096 (default 2048).",
    "apcfg-auto-cert-scep-ec-name": "Elliptic curve name: secp256r1, secp384r1 and secp521r1. (default secp256r1).",
    "apcfg-auto-cert-scep-sub-fully-dn": "Full DN of the subject (e.g C=US,ST=CA,L=Sunnyvale,O=Fortinet,OU=Dep1,emailAddress=test@example.com). There should be no space in between the attributes. Supported DN attributes (case-sensitive) are:C,ST,L,O,OU,emailAddress. The CN defaults to the device’s SN and cannot be changed.",
    "apcfg-auto-cert-scep-url": "SCEP server URL.",
    "apcfg-auto-cert-scep-password": "SCEP server challenge password for auto-regeneration.",
    "apcfg-auto-cert-scep-ca-id": "CA identifier of the CA server for signing via SCEP.",
    "apcfg-auto-cert-scep-subject-alt-name": "Subject alternative name (optional, e.g. \"DNS:dns1.com,IP:192.168.1.99\")",
    "apcfg-auto-cert-scep-https-ca": "PEM format https CA Certificate.",
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
    "lw-profile": {"type": "string", "max_length": 35},
    "syslog-profile": {"type": "string", "max_length": 35},
    "max-clients": {"type": "integer", "min": 0, "max": 4294967295},
    "handoff-rssi": {"type": "integer", "min": 20, "max": 30},
    "handoff-sta-thresh": {"type": "integer", "min": 5, "max": 60},
    "tun-mtu-uplink": {"type": "integer", "min": 576, "max": 1500},
    "tun-mtu-downlink": {"type": "integer", "min": 576, "max": 1500},
    "wan-port-auth-usrname": {"type": "string", "max_length": 63},
    "apcfg-auto-cert-est-server": {"type": "string", "max_length": 255},
    "apcfg-auto-cert-est-ca-id": {"type": "string", "max_length": 255},
    "apcfg-auto-cert-est-http-username": {"type": "string", "max_length": 63},
    "apcfg-auto-cert-est-subject": {"type": "string", "max_length": 127},
    "apcfg-auto-cert-est-subject-alt-name": {"type": "string", "max_length": 127},
    "apcfg-auto-cert-auto-regen-days": {"type": "integer", "min": 0, "max": 4294967295},
    "apcfg-auto-cert-est-https-ca": {"type": "string", "max_length": 79},
    "apcfg-auto-cert-scep-sub-fully-dn": {"type": "string", "max_length": 255},
    "apcfg-auto-cert-scep-url": {"type": "string", "max_length": 255},
    "apcfg-auto-cert-scep-ca-id": {"type": "string", "max_length": 255},
    "apcfg-auto-cert-scep-subject-alt-name": {"type": "string", "max_length": 127},
    "apcfg-auto-cert-scep-https-ca": {"type": "string", "max_length": 79},
    "admin-auth-tacacs+": {"type": "string", "max_length": 35},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "platform": {
        "type": {
            "type": "option",
            "help": "WTP, FortiAP or AP platform type. There are built-in WTP profiles for all supported FortiAP models. You can select a built-in profile and customize it or create a new profile.",
            "default": "221E",
            "options": [{"help": "Default 11n AP.", "label": "Ap 11N", "name": "AP-11N"}, {"help": "FAPC24JE.", "label": "C24Je", "name": "C24JE"}, {"help": "FAP421E.", "label": "421E", "name": "421E"}, {"help": "FAP423E.", "label": "423E", "name": "423E"}, {"help": "FAP221E.", "label": "221E", "name": "221E"}, {"help": "FAP222E.", "label": "222E", "name": "222E"}, {"help": "FAP223E.", "label": "223E", "name": "223E"}, {"help": "FAP224E.", "label": "224E", "name": "224E"}, {"help": "FAP231E.", "label": "231E", "name": "231E"}, {"help": "FAP321E.", "label": "321E", "name": "321E"}, {"help": "FAP431F.", "label": "431F", "name": "431F"}, {"help": "FAP431FL.", "label": "431Fl", "name": "431FL"}, {"help": "FAP432F.", "label": "432F", "name": "432F"}, {"help": "FAP432FR.", "label": "432Fr", "name": "432FR"}, {"help": "FAP433F.", "label": "433F", "name": "433F"}, {"help": "FAP433FL.", "label": "433Fl", "name": "433FL"}, {"help": "FAP231F.", "label": "231F", "name": "231F"}, {"help": "FAP231FL.", "label": "231Fl", "name": "231FL"}, {"help": "FAP234F.", "label": "234F", "name": "234F"}, {"help": "FAP23JF.", "label": "23Jf", "name": "23JF"}, {"help": "FAP831F.", "label": "831F", "name": "831F"}, {"help": "FAP231G.", "label": "231G", "name": "231G"}, {"help": "FAP233G.", "label": "233G", "name": "233G"}, {"help": "FAP234G.", "label": "234G", "name": "234G"}, {"help": "FAP431G.", "label": "431G", "name": "431G"}, {"help": "FAP432G.", "label": "432G", "name": "432G"}, {"help": "FAP433G.", "label": "433G", "name": "433G"}, {"help": "FAP231K.", "label": "231K", "name": "231K"}, {"help": "FAP231KD.", "label": "231Kd", "name": "231KD"}, {"help": "FAP23JK.", "label": "23Jk", "name": "23JK"}, {"help": "FAP222KL.", "label": "222Kl", "name": "222KL"}, {"help": "FAP241K.", "label": "241K", "name": "241K"}, {"help": "FAP243K.", "label": "243K", "name": "243K"}, {"help": "FAP244K.", "label": "244K", "name": "244K"}, {"help": "FAP441K.", "label": "441K", "name": "441K"}, {"help": "FAP432K.", "label": "432K", "name": "432K"}, {"help": "FAP443K.", "label": "443K", "name": "443K"}, {"help": "FAPU421EV.", "label": "U421E", "name": "U421E"}, {"help": "FAPU422EV.", "label": "U422Ev", "name": "U422EV"}, {"help": "FAPU423EV.", "label": "U423E", "name": "U423E"}, {"help": "FAPU221EV.", "label": "U221Ev", "name": "U221EV"}, {"help": "FAPU223EV.", "label": "U223Ev", "name": "U223EV"}, {"help": "FAPU24JEV.", "label": "U24Jev", "name": "U24JEV"}, {"help": "FAPU321EV.", "label": "U321Ev", "name": "U321EV"}, {"help": "FAPU323EV.", "label": "U323Ev", "name": "U323EV"}, {"help": "FAPU431F.", "label": "U431F", "name": "U431F"}, {"help": "FAPU433F.", "label": "U433F", "name": "U433F"}, {"help": "FAPU231F.", "label": "U231F", "name": "U231F"}, {"help": "FAPU234F.", "label": "U234F", "name": "U234F"}, {"help": "FAPU432F.", "label": "U432F", "name": "U432F"}, {"help": "FAPU231G.", "label": "U231G", "name": "U231G"}, {"help": "FAP MVP.", "label": "Mvp", "name": "MVP"}],
        },
        "mode": {
            "type": "option",
            "help": "Configure operation mode of 5G radios (default = single-5G).",
            "default": "single-5G",
            "options": [{"help": "Configure radios as one 5GHz band, one 2.4GHz band, and one dedicated monitor or sniffer.", "label": "Single 5G", "name": "single-5G"}, {"help": "Configure radios as one lower 5GHz band, one higher 5GHz band and one 2.4GHz band respectively.", "label": "Dual 5G", "name": "dual-5G"}],
        },
        "ddscan": {
            "type": "option",
            "help": "Enable/disable use of one radio for dedicated full-band scanning to detect RF characterization and wireless threat management.",
            "default": "disable",
            "options": [{"help": "Enable dedicated full-band scan mode.", "label": "Enable", "name": "enable"}, {"help": "Disable dedicated full-band scan mode.", "label": "Disable", "name": "disable"}],
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
            "options": [{"help": "Radio 1 is disabled.", "label": "Disabled", "name": "disabled"}, {"help": "Radio 1 operates as an access point that allows WiFi clients to connect to your network.", "label": "Ap", "name": "ap"}, {"help": "Radio 1 operates as a dedicated monitor. As a monitor, the radio scans for other WiFi access points and adds them to the Rogue AP monitor list.", "label": "Monitor", "name": "monitor"}, {"help": "Radio 1 operates as a sniffer capturing WiFi frames on air.", "label": "Sniffer", "name": "sniffer"}, {"help": "Radio 1 operates as a station that can connect to a neighboring AP for connectivity and health check.", "label": "Sam", "name": "sam"}],
        },
        "band": {
            "type": "option",
            "help": "WiFi band that Radio 1 operates on.",
            "default": "",
            "options": [{"help": "802.11a.", "label": "802.11A", "name": "802.11a"}, {"help": "802.11b.", "label": "802.11B", "name": "802.11b"}, {"help": "802.11g.", "label": "802.11G", "name": "802.11g"}, {"help": "802.11n (WiFi 4) at 2.4GHz.", "label": "802.11N 2G", "name": "802.11n-2G"}, {"help": "802.11n (WiFi 4) at 5GHz.", "label": "802.11N 5G", "name": "802.11n-5G"}, {"help": "802.11ac (WiFi 5) at 2.4GHz.", "label": "802.11Ac 2G", "name": "802.11ac-2G"}, {"help": "802.11ac (WiFi 5) at 5GHz.", "label": "802.11Ac 5G", "name": "802.11ac-5G"}, {"help": "802.11ax (WiFi 6) at 2.4GHz.", "label": "802.11Ax 2G", "name": "802.11ax-2G"}, {"help": "802.11ax (WiFi 6) at 5GHz.", "label": "802.11Ax 5G", "name": "802.11ax-5G"}, {"help": "802.11ax (WiFi 6) at 6GHz.", "label": "802.11Ax 6G", "name": "802.11ax-6G"}, {"help": "802.11be (WiFi 7) at 2.4GHz.", "label": "802.11Be 2G", "name": "802.11be-2G"}, {"help": "802.11be (WiFi 7) at 5GHz.", "label": "802.11Be 5G", "name": "802.11be-5G"}, {"help": "802.11be (WiFi 7) at 6GHz.", "label": "802.11Be 6G", "name": "802.11be-6G"}],
        },
        "band-5g-type": {
            "type": "option",
            "help": "WiFi 5G band type.",
            "default": "5g-full",
            "options": [{"help": "Full 5G band.", "label": "5G Full", "name": "5g-full"}, {"help": "High 5G band.", "label": "5G High", "name": "5g-high"}, {"help": "Low 5G band.", "label": "5G Low", "name": "5g-low"}],
        },
        "drma": {
            "type": "option",
            "help": "Enable/disable dynamic radio mode assignment (DRMA) (default = disable).",
            "default": "disable",
            "options": [{"help": "Disable dynamic radio mode assignment (DRMA).", "label": "Disable", "name": "disable"}, {"help": "Enable dynamic radio mode assignment (DRMA).", "label": "Enable", "name": "enable"}],
        },
        "drma-sensitivity": {
            "type": "option",
            "help": "Network Coverage Factor (NCF) percentage required to consider a radio as redundant (default = low).",
            "default": "low",
            "options": [{"help": "Consider a radio as redundant when its NCF is 100%.", "label": "Low", "name": "low"}, {"help": "Consider a radio as redundant when its NCF is 95%.", "label": "Medium", "name": "medium"}, {"help": "Consider a radio as redundant when its NCF is 90%.", "label": "High", "name": "high"}],
        },
        "airtime-fairness": {
            "type": "option",
            "help": "Enable/disable airtime fairness (default = disable).",
            "default": "disable",
            "options": [{"help": "Enable airtime fairness (ATF) support.", "label": "Enable", "name": "enable"}, {"help": "Disable airtime fairness (ATF) support.", "label": "Disable", "name": "disable"}],
        },
        "protection-mode": {
            "type": "option",
            "help": "Enable/disable 802.11g protection modes to support backwards compatibility with older clients (rtscts, ctsonly, disable).",
            "default": "disable",
            "options": [{"help": "Enable 802.11g protection RTS/CTS mode.", "label": "Rtscts", "name": "rtscts"}, {"help": "Enable 802.11g protection CTS only mode.", "label": "Ctsonly", "name": "ctsonly"}, {"help": "Disable 802.11g protection mode.", "label": "Disable", "name": "disable"}],
        },
        "powersave-optimize": {
            "type": "option",
            "help": "Enable client power-saving features such as TIM, AC VO, and OBSS etc.",
            "default": "",
            "options": [{"help": "TIM bit for client in power save mode.", "label": "Tim", "name": "tim"}, {"help": "Use AC VO priority to send out packets in the power save queue.", "label": "Ac Vo", "name": "ac-vo"}, {"help": "Do not put OBSS scan IE into beacon and probe response frames.", "label": "No Obss Scan", "name": "no-obss-scan"}, {"help": "Do not send frame using 11b data rate.", "label": "No 11B Rate", "name": "no-11b-rate"}, {"help": "Adapt transmitting PHY rate with receiving PHY rate from a client.", "label": "Client Rate Follow", "name": "client-rate-follow"}],
        },
        "transmit-optimize": {
            "type": "option",
            "help": "Packet transmission optimization options including power saving, aggregation limiting, retry limiting, etc. All are enabled by default.",
            "default": "power-save aggr-limit retry-limit send-bar",
            "options": [{"help": "Disable packet transmission optimization.", "label": "Disable", "name": "disable"}, {"help": "Tag client as operating in power save mode if excessive transmit retries occur.", "label": "Power Save", "name": "power-save"}, {"help": "Set aggregation limit to a lower value when data rate is low.", "label": "Aggr Limit", "name": "aggr-limit"}, {"help": "Set software retry limit to a lower value when data rate is low.", "label": "Retry Limit", "name": "retry-limit"}, {"help": "Limit transmission of BAR frames.", "label": "Send Bar", "name": "send-bar"}],
        },
        "amsdu": {
            "type": "option",
            "help": "Enable/disable 802.11n AMSDU support. AMSDU can improve performance if supported by your WiFi clients (default = enable).",
            "default": "enable",
            "options": [{"help": "Enable AMSDU support.", "label": "Enable", "name": "enable"}, {"help": "Disable AMSDU support.", "label": "Disable", "name": "disable"}],
        },
        "coexistence": {
            "type": "option",
            "help": "Enable/disable allowing both HT20 and HT40 on the same radio (default = enable).",
            "default": "enable",
            "options": [{"help": "Enable support for both HT20 and HT40 on the same radio.", "label": "Enable", "name": "enable"}, {"help": "Disable support for both HT20 and HT40 on the same radio.", "label": "Disable", "name": "disable"}],
        },
        "zero-wait-dfs": {
            "type": "option",
            "help": "Enable/disable zero wait DFS on radio (default = enable).",
            "default": "enable",
            "options": [{"help": "Enable zero wait DFS", "label": "Enable", "name": "enable"}, {"help": "Disable zero wait DFS", "label": "Disable", "name": "disable"}],
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
            "options": [{"help": "Automatically select BSS color value on AP.", "label": "Auto", "name": "auto"}, {"help": "Set BSS color value on this radio based on \u0027bss-color\u0027 CLI.", "label": "Static", "name": "static"}],
        },
        "short-guard-interval": {
            "type": "option",
            "help": "Use either the short guard interval (Short GI) of 400 ns or the long guard interval (Long GI) of 800 ns.",
            "default": "disable",
            "options": [{"help": "Select the 400 ns short guard interval (Short GI).", "label": "Enable", "name": "enable"}, {"help": "Select the 800 ns long guard interval (Long GI).", "label": "Disable", "name": "disable"}],
        },
        "mimo-mode": {
            "type": "option",
            "help": "Configure radio MIMO mode (default = default).",
            "default": "default",
            "options": [{"help": "Default radio MIMO mode.", "label": "Default", "name": "default"}, {"help": "1x1 radio MIMO mode.", "label": "1X1", "name": "1x1"}, {"help": "2x2 radio MIMO mode.", "label": "2X2", "name": "2x2"}, {"help": "3x3 radio MIMO mode.", "label": "3X3", "name": "3x3"}, {"help": "4x4 radio MIMO mode.", "label": "4X4", "name": "4x4"}, {"help": "8x8 radio MIMO mode.", "label": "8X8", "name": "8x8"}],
        },
        "channel-bonding": {
            "type": "option",
            "help": "Channel bandwidth: 320, 240, 160, 80, 40, or 20MHz. Channels may use both 20 and 40 by enabling coexistence.",
            "default": "20MHz",
            "options": [{"help": "320 MHz channel width.", "label": "320Mhz", "name": "320MHz"}, {"help": "240 MHz channel width.", "label": "240Mhz", "name": "240MHz"}, {"help": "160 MHz channel width.", "label": "160Mhz", "name": "160MHz"}, {"help": "80 MHz channel width.", "label": "80Mhz", "name": "80MHz"}, {"help": "40 MHz channel width.", "label": "40Mhz", "name": "40MHz"}, {"help": "20 MHz channel width.", "label": "20Mhz", "name": "20MHz"}],
        },
        "channel-bonding-ext": {
            "type": "option",
            "help": "Channel bandwidth extension: 320 MHz-1 and 320 MHz-2 (default = 320 MHz-2).",
            "default": "320MHz-2",
            "options": [{"help": "320 MHz channel with channel center frequency numbered 31, 95, and 159.", "label": "320Mhz 1", "name": "320MHz-1"}, {"help": "320 MHz channel with channel center frequency numbered 63, 127, and 191.", "label": "320Mhz 2", "name": "320MHz-2"}],
        },
        "optional-antenna": {
            "type": "option",
            "help": "Optional antenna used on FAP (default = none).",
            "default": "none",
            "options": [{"help": "None.", "label": "None", "name": "none"}, {"help": "Customize optional antenna gain.", "label": "Custom", "name": "custom"}, {"help": "6 dBi(2.4GHz) and 6 dBi(5GHz).", "label": "Fant 04Abgn 0606 O N", "name": "FANT-04ABGN-0606-O-N"}, {"help": "14 dBi(2.4GHz) and 14 dBi(5GHz).", "label": "Fant 04Abgn 1414 P N", "name": "FANT-04ABGN-1414-P-N"}, {"help": "8 dBi(2.4GHz) and 6.5 dBi(5GHz).", "label": "Fant 04Abgn 8065 P N", "name": "FANT-04ABGN-8065-P-N"}, {"help": "6 dBi(2.4GHz) and 6 dBi(5GHz).", "label": "Fant 04Abgn 0606 O R", "name": "FANT-04ABGN-0606-O-R"}, {"help": "6 dBi(2.4GHz) and 6 dBi(5GHz).", "label": "Fant 04Abgn 0606 P R", "name": "FANT-04ABGN-0606-P-R"}, {"help": "12 dBi(2.4GHz) and 13 dBi(5GHz).", "label": "Fant 10Acax 1213 D N", "name": "FANT-10ACAX-1213-D-N"}, {"help": "12 dBi(2.4GHz) and 13 dBi(5GHz).", "label": "Fant 08Abgn 1213 D R", "name": "FANT-08ABGN-1213-D-R"}, {"help": "6 dBi(2.4GHz), 6 dBi(5GHz) and 6 dBi(6GHz).", "label": "Fant 04Beax 0606 P R", "name": "FANT-04BEAX-0606-P-R"}],
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
            "options": [{"help": "Enable 802.11d countryie.", "label": "Enable", "name": "enable"}, {"help": "Disable 802.11d countryie.", "label": "Disable", "name": "disable"}],
        },
        "80211mc": {
            "type": "option",
            "help": "Enable/disable 802.11mc responder mode (default = disable).",
            "default": "disable",
            "options": [{"help": "Enable 802.11mc responder mode.", "label": "Enable", "name": "enable"}, {"help": "Disable 802.11mc responder mode.", "label": "Disable", "name": "disable"}],
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
            "options": [{"help": "320 MHz channel width.", "label": "320Mhz", "name": "320MHz"}, {"help": "240 MHz channel width.", "label": "240Mhz", "name": "240MHz"}, {"help": "160 MHz channel width.", "label": "160Mhz", "name": "160MHz"}, {"help": "80 MHz channel width.", "label": "80Mhz", "name": "80MHz"}, {"help": "40 MHz channel width.", "label": "40Mhz", "name": "40MHz"}, {"help": "20 MHz channel width.", "label": "20Mhz", "name": "20MHz"}],
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
            "options": [{"help": "Enable sniffer on WiFi management beacon frame.", "label": "Enable", "name": "enable"}, {"help": "Disable sniffer on WiFi management beacon frame.", "label": "Disable", "name": "disable"}],
        },
        "ap-sniffer-mgmt-probe": {
            "type": "option",
            "help": "Enable/disable sniffer on WiFi management probe frames (default = enable).",
            "default": "enable",
            "options": [{"help": "Enable sniffer on WiFi management probe frame.", "label": "Enable", "name": "enable"}, {"help": "Enable sniffer on WiFi management probe frame.", "label": "Disable", "name": "disable"}],
        },
        "ap-sniffer-mgmt-other": {
            "type": "option",
            "help": "Enable/disable sniffer on WiFi management other frames  (default = enable).",
            "default": "enable",
            "options": [{"help": "Enable sniffer on WiFi management other frame.", "label": "Enable", "name": "enable"}, {"help": "Disable sniffer on WiFi management other frame.", "label": "Disable", "name": "disable"}],
        },
        "ap-sniffer-ctl": {
            "type": "option",
            "help": "Enable/disable sniffer on WiFi control frame (default = enable).",
            "default": "enable",
            "options": [{"help": "Enable sniffer on WiFi control frame.", "label": "Enable", "name": "enable"}, {"help": "Disable sniffer on WiFi control frame.", "label": "Disable", "name": "disable"}],
        },
        "ap-sniffer-data": {
            "type": "option",
            "help": "Enable/disable sniffer on WiFi data frame (default = enable).",
            "default": "enable",
            "options": [{"help": "Enable sniffer on WiFi data frame", "label": "Enable", "name": "enable"}, {"help": "Disable sniffer on WiFi data frame", "label": "Disable", "name": "disable"}],
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
            "options": [{"help": "Open.", "label": "Open", "name": "open"}, {"help": "WPA/WPA2 personal.", "label": "Wpa Personal", "name": "wpa-personal"}, {"help": "WPA2/WPA3 enterprise.", "label": "Wpa Enterprise", "name": "wpa-enterprise"}, {"help": "WPA3 SAE.", "label": "Wpa3 Sae", "name": "wpa3-sae"}, {"help": "OWE.", "label": "Owe", "name": "owe"}],
        },
        "sam-captive-portal": {
            "type": "option",
            "help": "Enable/disable Captive Portal Authentication (default = disable).",
            "default": "disable",
            "options": [{"help": "Enable Captive Portal Authentication.", "label": "Enable", "name": "enable"}, {"help": "Disable Captive Portal Authentication.", "label": "Disable", "name": "disable"}],
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
            "options": [{"help": "EAP PEAP and TLS. (Not applicable in FIPS mode)", "label": "Both", "name": "both"}, {"help": "EAP TLS.", "label": "Tls", "name": "tls"}, {"help": "EAP PEAP. (Not applicable in FIPS mode)", "label": "Peap", "name": "peap"}],
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
            "options": [{"help": "PING test.", "label": "Ping", "name": "ping"}, {"help": "IPERF test.", "label": "Iperf", "name": "iperf"}],
        },
        "sam-server-type": {
            "type": "option",
            "help": "Select SAM server type (default = \"IP\").",
            "default": "ip",
            "options": [{"help": "IPv4 address.", "label": "Ip", "name": "ip"}, {"help": "Fully Qualified Domain Name address.", "label": "Fqdn", "name": "fqdn"}],
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
            "options": [{"help": "UDP.", "label": "Udp", "name": "udp"}, {"help": "TCP.", "label": "Tcp", "name": "tcp"}],
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
            "options": [{"help": "Enable measuring channel utilization.", "label": "Enable", "name": "enable"}, {"help": "Disable measuring channel utilization.", "label": "Disable", "name": "disable"}],
        },
        "wids-profile": {
            "type": "string",
            "help": "Wireless Intrusion Detection System (WIDS) profile name to assign to the radio.",
            "default": "",
            "max_length": 35,
        },
        "ai-darrp-support": {
            "type": "option",
            "help": "Enable/disable support for FortiAIOps to retrieve Distributed Automatic Radio Resource Provisioning (DARRP) data through REST API calls (default = disable).",
            "default": "disable",
            "options": [{"help": "Enable support for FortiAIOps REST API calls for DARRP data.", "label": "Enable", "name": "enable"}, {"help": "Disable support for FortiAIOps REST API calls for DARRP data.", "label": "Disable", "name": "disable"}],
        },
        "darrp": {
            "type": "option",
            "help": "Enable/disable Distributed Automatic Radio Resource Provisioning (DARRP) to make sure the radio is always using the most optimal channel (default = disable).",
            "default": "disable",
            "options": [{"help": "Enable distributed automatic radio resource provisioning.", "label": "Enable", "name": "enable"}, {"help": "Disable distributed automatic radio resource provisioning.", "label": "Disable", "name": "disable"}],
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
            "options": [{"help": "Automatically select tunnel SSIDs.", "label": "Tunnel", "name": "tunnel"}, {"help": "Automatically select local-bridging SSIDs.", "label": "Bridge", "name": "bridge"}, {"help": "Manually select SSIDs.", "label": "Manual", "name": "manual"}],
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
            "options": [{"help": "Enable WMM call admission control.", "label": "Enable", "name": "enable"}, {"help": "Disable WMM call admission control.", "label": "Disable", "name": "disable"}],
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
            "options": [{"help": "Enable WMM bandwidth admission control.", "label": "Enable", "name": "enable"}, {"help": "Disable WMM bandwidth admission control.", "label": "Disable", "name": "disable"}],
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
            "options": [{"help": "Radio 2 is disabled.", "label": "Disabled", "name": "disabled"}, {"help": "Radio 2 operates as an access point that allows WiFi clients to connect to your network.", "label": "Ap", "name": "ap"}, {"help": "Radio 2 operates as a dedicated monitor. As a monitor, the radio scans for other WiFi access points and adds them to the Rogue AP monitor list.", "label": "Monitor", "name": "monitor"}, {"help": "Radio 2 operates as a sniffer capturing WiFi frames on air.", "label": "Sniffer", "name": "sniffer"}, {"help": "Radio 2 operates as a station that can connect to a neighboring AP for connectivity and health check.", "label": "Sam", "name": "sam"}],
        },
        "band": {
            "type": "option",
            "help": "WiFi band that Radio 2 operates on.",
            "default": "",
            "options": [{"help": "802.11a.", "label": "802.11A", "name": "802.11a"}, {"help": "802.11b.", "label": "802.11B", "name": "802.11b"}, {"help": "802.11g.", "label": "802.11G", "name": "802.11g"}, {"help": "802.11n (WiFi 4) at 2.4GHz.", "label": "802.11N 2G", "name": "802.11n-2G"}, {"help": "802.11n (WiFi 4) at 5GHz.", "label": "802.11N 5G", "name": "802.11n-5G"}, {"help": "802.11ac (WiFi 5) at 2.4GHz.", "label": "802.11Ac 2G", "name": "802.11ac-2G"}, {"help": "802.11ac (WiFi 5) at 5GHz.", "label": "802.11Ac 5G", "name": "802.11ac-5G"}, {"help": "802.11ax (WiFi 6) at 2.4GHz.", "label": "802.11Ax 2G", "name": "802.11ax-2G"}, {"help": "802.11ax (WiFi 6) at 5GHz.", "label": "802.11Ax 5G", "name": "802.11ax-5G"}, {"help": "802.11ax (WiFi 6) at 6GHz.", "label": "802.11Ax 6G", "name": "802.11ax-6G"}, {"help": "802.11be (WiFi 7) at 2.4GHz.", "label": "802.11Be 2G", "name": "802.11be-2G"}, {"help": "802.11be (WiFi 7) at 5GHz.", "label": "802.11Be 5G", "name": "802.11be-5G"}, {"help": "802.11be (WiFi 7) at 6GHz.", "label": "802.11Be 6G", "name": "802.11be-6G"}],
        },
        "band-5g-type": {
            "type": "option",
            "help": "WiFi 5G band type.",
            "default": "5g-full",
            "options": [{"help": "Full 5G band.", "label": "5G Full", "name": "5g-full"}, {"help": "High 5G band.", "label": "5G High", "name": "5g-high"}, {"help": "Low 5G band.", "label": "5G Low", "name": "5g-low"}],
        },
        "drma": {
            "type": "option",
            "help": "Enable/disable dynamic radio mode assignment (DRMA) (default = disable).",
            "default": "disable",
            "options": [{"help": "Disable dynamic radio mode assignment (DRMA).", "label": "Disable", "name": "disable"}, {"help": "Enable dynamic radio mode assignment (DRMA).", "label": "Enable", "name": "enable"}],
        },
        "drma-sensitivity": {
            "type": "option",
            "help": "Network Coverage Factor (NCF) percentage required to consider a radio as redundant (default = low).",
            "default": "low",
            "options": [{"help": "Consider a radio as redundant when its NCF is 100%.", "label": "Low", "name": "low"}, {"help": "Consider a radio as redundant when its NCF is 95%.", "label": "Medium", "name": "medium"}, {"help": "Consider a radio as redundant when its NCF is 90%.", "label": "High", "name": "high"}],
        },
        "airtime-fairness": {
            "type": "option",
            "help": "Enable/disable airtime fairness (default = disable).",
            "default": "disable",
            "options": [{"help": "Enable airtime fairness (ATF) support.", "label": "Enable", "name": "enable"}, {"help": "Disable airtime fairness (ATF) support.", "label": "Disable", "name": "disable"}],
        },
        "protection-mode": {
            "type": "option",
            "help": "Enable/disable 802.11g protection modes to support backwards compatibility with older clients (rtscts, ctsonly, disable).",
            "default": "disable",
            "options": [{"help": "Enable 802.11g protection RTS/CTS mode.", "label": "Rtscts", "name": "rtscts"}, {"help": "Enable 802.11g protection CTS only mode.", "label": "Ctsonly", "name": "ctsonly"}, {"help": "Disable 802.11g protection mode.", "label": "Disable", "name": "disable"}],
        },
        "powersave-optimize": {
            "type": "option",
            "help": "Enable client power-saving features such as TIM, AC VO, and OBSS etc.",
            "default": "",
            "options": [{"help": "TIM bit for client in power save mode.", "label": "Tim", "name": "tim"}, {"help": "Use AC VO priority to send out packets in the power save queue.", "label": "Ac Vo", "name": "ac-vo"}, {"help": "Do not put OBSS scan IE into beacon and probe response frames.", "label": "No Obss Scan", "name": "no-obss-scan"}, {"help": "Do not send frame using 11b data rate.", "label": "No 11B Rate", "name": "no-11b-rate"}, {"help": "Adapt transmitting PHY rate with receiving PHY rate from a client.", "label": "Client Rate Follow", "name": "client-rate-follow"}],
        },
        "transmit-optimize": {
            "type": "option",
            "help": "Packet transmission optimization options including power saving, aggregation limiting, retry limiting, etc. All are enabled by default.",
            "default": "power-save aggr-limit retry-limit send-bar",
            "options": [{"help": "Disable packet transmission optimization.", "label": "Disable", "name": "disable"}, {"help": "Tag client as operating in power save mode if excessive transmit retries occur.", "label": "Power Save", "name": "power-save"}, {"help": "Set aggregation limit to a lower value when data rate is low.", "label": "Aggr Limit", "name": "aggr-limit"}, {"help": "Set software retry limit to a lower value when data rate is low.", "label": "Retry Limit", "name": "retry-limit"}, {"help": "Limit transmission of BAR frames.", "label": "Send Bar", "name": "send-bar"}],
        },
        "amsdu": {
            "type": "option",
            "help": "Enable/disable 802.11n AMSDU support. AMSDU can improve performance if supported by your WiFi clients (default = enable).",
            "default": "enable",
            "options": [{"help": "Enable AMSDU support.", "label": "Enable", "name": "enable"}, {"help": "Disable AMSDU support.", "label": "Disable", "name": "disable"}],
        },
        "coexistence": {
            "type": "option",
            "help": "Enable/disable allowing both HT20 and HT40 on the same radio (default = enable).",
            "default": "enable",
            "options": [{"help": "Enable support for both HT20 and HT40 on the same radio.", "label": "Enable", "name": "enable"}, {"help": "Disable support for both HT20 and HT40 on the same radio.", "label": "Disable", "name": "disable"}],
        },
        "zero-wait-dfs": {
            "type": "option",
            "help": "Enable/disable zero wait DFS on radio (default = enable).",
            "default": "enable",
            "options": [{"help": "Enable zero wait DFS", "label": "Enable", "name": "enable"}, {"help": "Disable zero wait DFS", "label": "Disable", "name": "disable"}],
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
            "options": [{"help": "Automatically select BSS color value on AP.", "label": "Auto", "name": "auto"}, {"help": "Set BSS color value on this radio based on \u0027bss-color\u0027 CLI.", "label": "Static", "name": "static"}],
        },
        "short-guard-interval": {
            "type": "option",
            "help": "Use either the short guard interval (Short GI) of 400 ns or the long guard interval (Long GI) of 800 ns.",
            "default": "disable",
            "options": [{"help": "Select the 400 ns short guard interval (Short GI).", "label": "Enable", "name": "enable"}, {"help": "Select the 800 ns long guard interval (Long GI).", "label": "Disable", "name": "disable"}],
        },
        "mimo-mode": {
            "type": "option",
            "help": "Configure radio MIMO mode (default = default).",
            "default": "default",
            "options": [{"help": "Default radio MIMO mode.", "label": "Default", "name": "default"}, {"help": "1x1 radio MIMO mode.", "label": "1X1", "name": "1x1"}, {"help": "2x2 radio MIMO mode.", "label": "2X2", "name": "2x2"}, {"help": "3x3 radio MIMO mode.", "label": "3X3", "name": "3x3"}, {"help": "4x4 radio MIMO mode.", "label": "4X4", "name": "4x4"}, {"help": "8x8 radio MIMO mode.", "label": "8X8", "name": "8x8"}],
        },
        "channel-bonding": {
            "type": "option",
            "help": "Channel bandwidth: 320, 240, 160, 80, 40, or 20MHz. Channels may use both 20 and 40 by enabling coexistence.",
            "default": "20MHz",
            "options": [{"help": "320 MHz channel width.", "label": "320Mhz", "name": "320MHz"}, {"help": "240 MHz channel width.", "label": "240Mhz", "name": "240MHz"}, {"help": "160 MHz channel width.", "label": "160Mhz", "name": "160MHz"}, {"help": "80 MHz channel width.", "label": "80Mhz", "name": "80MHz"}, {"help": "40 MHz channel width.", "label": "40Mhz", "name": "40MHz"}, {"help": "20 MHz channel width.", "label": "20Mhz", "name": "20MHz"}],
        },
        "channel-bonding-ext": {
            "type": "option",
            "help": "Channel bandwidth extension: 320 MHz-1 and 320 MHz-2 (default = 320 MHz-2).",
            "default": "320MHz-2",
            "options": [{"help": "320 MHz channel with channel center frequency numbered 31, 95, and 159.", "label": "320Mhz 1", "name": "320MHz-1"}, {"help": "320 MHz channel with channel center frequency numbered 63, 127, and 191.", "label": "320Mhz 2", "name": "320MHz-2"}],
        },
        "optional-antenna": {
            "type": "option",
            "help": "Optional antenna used on FAP (default = none).",
            "default": "none",
            "options": [{"help": "None.", "label": "None", "name": "none"}, {"help": "Customize optional antenna gain.", "label": "Custom", "name": "custom"}, {"help": "6 dBi(2.4GHz) and 6 dBi(5GHz).", "label": "Fant 04Abgn 0606 O N", "name": "FANT-04ABGN-0606-O-N"}, {"help": "14 dBi(2.4GHz) and 14 dBi(5GHz).", "label": "Fant 04Abgn 1414 P N", "name": "FANT-04ABGN-1414-P-N"}, {"help": "8 dBi(2.4GHz) and 6.5 dBi(5GHz).", "label": "Fant 04Abgn 8065 P N", "name": "FANT-04ABGN-8065-P-N"}, {"help": "6 dBi(2.4GHz) and 6 dBi(5GHz).", "label": "Fant 04Abgn 0606 O R", "name": "FANT-04ABGN-0606-O-R"}, {"help": "6 dBi(2.4GHz) and 6 dBi(5GHz).", "label": "Fant 04Abgn 0606 P R", "name": "FANT-04ABGN-0606-P-R"}, {"help": "12 dBi(2.4GHz) and 13 dBi(5GHz).", "label": "Fant 10Acax 1213 D N", "name": "FANT-10ACAX-1213-D-N"}, {"help": "12 dBi(2.4GHz) and 13 dBi(5GHz).", "label": "Fant 08Abgn 1213 D R", "name": "FANT-08ABGN-1213-D-R"}, {"help": "6 dBi(2.4GHz), 6 dBi(5GHz) and 6 dBi(6GHz).", "label": "Fant 04Beax 0606 P R", "name": "FANT-04BEAX-0606-P-R"}],
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
            "options": [{"help": "Enable 802.11d countryie.", "label": "Enable", "name": "enable"}, {"help": "Disable 802.11d countryie.", "label": "Disable", "name": "disable"}],
        },
        "80211mc": {
            "type": "option",
            "help": "Enable/disable 802.11mc responder mode (default = disable).",
            "default": "disable",
            "options": [{"help": "Enable 802.11mc responder mode.", "label": "Enable", "name": "enable"}, {"help": "Disable 802.11mc responder mode.", "label": "Disable", "name": "disable"}],
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
            "options": [{"help": "320 MHz channel width.", "label": "320Mhz", "name": "320MHz"}, {"help": "240 MHz channel width.", "label": "240Mhz", "name": "240MHz"}, {"help": "160 MHz channel width.", "label": "160Mhz", "name": "160MHz"}, {"help": "80 MHz channel width.", "label": "80Mhz", "name": "80MHz"}, {"help": "40 MHz channel width.", "label": "40Mhz", "name": "40MHz"}, {"help": "20 MHz channel width.", "label": "20Mhz", "name": "20MHz"}],
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
            "options": [{"help": "Enable sniffer on WiFi management beacon frame.", "label": "Enable", "name": "enable"}, {"help": "Disable sniffer on WiFi management beacon frame.", "label": "Disable", "name": "disable"}],
        },
        "ap-sniffer-mgmt-probe": {
            "type": "option",
            "help": "Enable/disable sniffer on WiFi management probe frames (default = enable).",
            "default": "enable",
            "options": [{"help": "Enable sniffer on WiFi management probe frame.", "label": "Enable", "name": "enable"}, {"help": "Enable sniffer on WiFi management probe frame.", "label": "Disable", "name": "disable"}],
        },
        "ap-sniffer-mgmt-other": {
            "type": "option",
            "help": "Enable/disable sniffer on WiFi management other frames  (default = enable).",
            "default": "enable",
            "options": [{"help": "Enable sniffer on WiFi management other frame.", "label": "Enable", "name": "enable"}, {"help": "Disable sniffer on WiFi management other frame.", "label": "Disable", "name": "disable"}],
        },
        "ap-sniffer-ctl": {
            "type": "option",
            "help": "Enable/disable sniffer on WiFi control frame (default = enable).",
            "default": "enable",
            "options": [{"help": "Enable sniffer on WiFi control frame.", "label": "Enable", "name": "enable"}, {"help": "Disable sniffer on WiFi control frame.", "label": "Disable", "name": "disable"}],
        },
        "ap-sniffer-data": {
            "type": "option",
            "help": "Enable/disable sniffer on WiFi data frame (default = enable).",
            "default": "enable",
            "options": [{"help": "Enable sniffer on WiFi data frame", "label": "Enable", "name": "enable"}, {"help": "Disable sniffer on WiFi data frame", "label": "Disable", "name": "disable"}],
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
            "options": [{"help": "Open.", "label": "Open", "name": "open"}, {"help": "WPA/WPA2 personal.", "label": "Wpa Personal", "name": "wpa-personal"}, {"help": "WPA2/WPA3 enterprise.", "label": "Wpa Enterprise", "name": "wpa-enterprise"}, {"help": "WPA3 SAE.", "label": "Wpa3 Sae", "name": "wpa3-sae"}, {"help": "OWE.", "label": "Owe", "name": "owe"}],
        },
        "sam-captive-portal": {
            "type": "option",
            "help": "Enable/disable Captive Portal Authentication (default = disable).",
            "default": "disable",
            "options": [{"help": "Enable Captive Portal Authentication.", "label": "Enable", "name": "enable"}, {"help": "Disable Captive Portal Authentication.", "label": "Disable", "name": "disable"}],
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
            "options": [{"help": "EAP PEAP and TLS. (Not applicable in FIPS mode)", "label": "Both", "name": "both"}, {"help": "EAP TLS.", "label": "Tls", "name": "tls"}, {"help": "EAP PEAP. (Not applicable in FIPS mode)", "label": "Peap", "name": "peap"}],
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
            "options": [{"help": "PING test.", "label": "Ping", "name": "ping"}, {"help": "IPERF test.", "label": "Iperf", "name": "iperf"}],
        },
        "sam-server-type": {
            "type": "option",
            "help": "Select SAM server type (default = \"IP\").",
            "default": "ip",
            "options": [{"help": "IPv4 address.", "label": "Ip", "name": "ip"}, {"help": "Fully Qualified Domain Name address.", "label": "Fqdn", "name": "fqdn"}],
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
            "options": [{"help": "UDP.", "label": "Udp", "name": "udp"}, {"help": "TCP.", "label": "Tcp", "name": "tcp"}],
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
            "options": [{"help": "Enable measuring channel utilization.", "label": "Enable", "name": "enable"}, {"help": "Disable measuring channel utilization.", "label": "Disable", "name": "disable"}],
        },
        "wids-profile": {
            "type": "string",
            "help": "Wireless Intrusion Detection System (WIDS) profile name to assign to the radio.",
            "default": "",
            "max_length": 35,
        },
        "ai-darrp-support": {
            "type": "option",
            "help": "Enable/disable support for FortiAIOps to retrieve Distributed Automatic Radio Resource Provisioning (DARRP) data through REST API calls (default = disable).",
            "default": "disable",
            "options": [{"help": "Enable support for FortiAIOps REST API calls for DARRP data.", "label": "Enable", "name": "enable"}, {"help": "Disable support for FortiAIOps REST API calls for DARRP data.", "label": "Disable", "name": "disable"}],
        },
        "darrp": {
            "type": "option",
            "help": "Enable/disable Distributed Automatic Radio Resource Provisioning (DARRP) to make sure the radio is always using the most optimal channel (default = disable).",
            "default": "disable",
            "options": [{"help": "Enable distributed automatic radio resource provisioning.", "label": "Enable", "name": "enable"}, {"help": "Disable distributed automatic radio resource provisioning.", "label": "Disable", "name": "disable"}],
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
            "options": [{"help": "Automatically select tunnel SSIDs.", "label": "Tunnel", "name": "tunnel"}, {"help": "Automatically select local-bridging SSIDs.", "label": "Bridge", "name": "bridge"}, {"help": "Manually select SSIDs.", "label": "Manual", "name": "manual"}],
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
            "options": [{"help": "Enable WMM call admission control.", "label": "Enable", "name": "enable"}, {"help": "Disable WMM call admission control.", "label": "Disable", "name": "disable"}],
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
            "options": [{"help": "Enable WMM bandwidth admission control.", "label": "Enable", "name": "enable"}, {"help": "Disable WMM bandwidth admission control.", "label": "Disable", "name": "disable"}],
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
            "options": [{"help": "Radio 3 is disabled.", "label": "Disabled", "name": "disabled"}, {"help": "Radio 3 operates as an access point that allows WiFi clients to connect to your network.", "label": "Ap", "name": "ap"}, {"help": "Radio 3 operates as a dedicated monitor. As a monitor, the radio scans for other WiFi access points and adds them to the Rogue AP monitor list.", "label": "Monitor", "name": "monitor"}, {"help": "Radio 3 operates as a sniffer capturing WiFi frames on air.", "label": "Sniffer", "name": "sniffer"}, {"help": "Radio 3 operates as a station that can connect to a neighboring AP for connectivity and health check.", "label": "Sam", "name": "sam"}],
        },
        "band": {
            "type": "option",
            "help": "WiFi band that Radio 3 operates on.",
            "default": "",
            "options": [{"help": "802.11a.", "label": "802.11A", "name": "802.11a"}, {"help": "802.11b.", "label": "802.11B", "name": "802.11b"}, {"help": "802.11g.", "label": "802.11G", "name": "802.11g"}, {"help": "802.11n (WiFi 4) at 2.4GHz.", "label": "802.11N 2G", "name": "802.11n-2G"}, {"help": "802.11n (WiFi 4) at 5GHz.", "label": "802.11N 5G", "name": "802.11n-5G"}, {"help": "802.11ac (WiFi 5) at 2.4GHz.", "label": "802.11Ac 2G", "name": "802.11ac-2G"}, {"help": "802.11ac (WiFi 5) at 5GHz.", "label": "802.11Ac 5G", "name": "802.11ac-5G"}, {"help": "802.11ax (WiFi 6) at 2.4GHz.", "label": "802.11Ax 2G", "name": "802.11ax-2G"}, {"help": "802.11ax (WiFi 6) at 5GHz.", "label": "802.11Ax 5G", "name": "802.11ax-5G"}, {"help": "802.11ax (WiFi 6) at 6GHz.", "label": "802.11Ax 6G", "name": "802.11ax-6G"}, {"help": "802.11be (WiFi 7) at 2.4GHz.", "label": "802.11Be 2G", "name": "802.11be-2G"}, {"help": "802.11be (WiFi 7) at 5GHz.", "label": "802.11Be 5G", "name": "802.11be-5G"}, {"help": "802.11be (WiFi 7) at 6GHz.", "label": "802.11Be 6G", "name": "802.11be-6G"}],
        },
        "band-5g-type": {
            "type": "option",
            "help": "WiFi 5G band type.",
            "default": "5g-full",
            "options": [{"help": "Full 5G band.", "label": "5G Full", "name": "5g-full"}, {"help": "High 5G band.", "label": "5G High", "name": "5g-high"}, {"help": "Low 5G band.", "label": "5G Low", "name": "5g-low"}],
        },
        "drma": {
            "type": "option",
            "help": "Enable/disable dynamic radio mode assignment (DRMA) (default = disable).",
            "default": "disable",
            "options": [{"help": "Disable dynamic radio mode assignment (DRMA).", "label": "Disable", "name": "disable"}, {"help": "Enable dynamic radio mode assignment (DRMA).", "label": "Enable", "name": "enable"}],
        },
        "drma-sensitivity": {
            "type": "option",
            "help": "Network Coverage Factor (NCF) percentage required to consider a radio as redundant (default = low).",
            "default": "low",
            "options": [{"help": "Consider a radio as redundant when its NCF is 100%.", "label": "Low", "name": "low"}, {"help": "Consider a radio as redundant when its NCF is 95%.", "label": "Medium", "name": "medium"}, {"help": "Consider a radio as redundant when its NCF is 90%.", "label": "High", "name": "high"}],
        },
        "airtime-fairness": {
            "type": "option",
            "help": "Enable/disable airtime fairness (default = disable).",
            "default": "disable",
            "options": [{"help": "Enable airtime fairness (ATF) support.", "label": "Enable", "name": "enable"}, {"help": "Disable airtime fairness (ATF) support.", "label": "Disable", "name": "disable"}],
        },
        "protection-mode": {
            "type": "option",
            "help": "Enable/disable 802.11g protection modes to support backwards compatibility with older clients (rtscts, ctsonly, disable).",
            "default": "disable",
            "options": [{"help": "Enable 802.11g protection RTS/CTS mode.", "label": "Rtscts", "name": "rtscts"}, {"help": "Enable 802.11g protection CTS only mode.", "label": "Ctsonly", "name": "ctsonly"}, {"help": "Disable 802.11g protection mode.", "label": "Disable", "name": "disable"}],
        },
        "powersave-optimize": {
            "type": "option",
            "help": "Enable client power-saving features such as TIM, AC VO, and OBSS etc.",
            "default": "",
            "options": [{"help": "TIM bit for client in power save mode.", "label": "Tim", "name": "tim"}, {"help": "Use AC VO priority to send out packets in the power save queue.", "label": "Ac Vo", "name": "ac-vo"}, {"help": "Do not put OBSS scan IE into beacon and probe response frames.", "label": "No Obss Scan", "name": "no-obss-scan"}, {"help": "Do not send frame using 11b data rate.", "label": "No 11B Rate", "name": "no-11b-rate"}, {"help": "Adapt transmitting PHY rate with receiving PHY rate from a client.", "label": "Client Rate Follow", "name": "client-rate-follow"}],
        },
        "transmit-optimize": {
            "type": "option",
            "help": "Packet transmission optimization options including power saving, aggregation limiting, retry limiting, etc. All are enabled by default.",
            "default": "power-save aggr-limit retry-limit send-bar",
            "options": [{"help": "Disable packet transmission optimization.", "label": "Disable", "name": "disable"}, {"help": "Tag client as operating in power save mode if excessive transmit retries occur.", "label": "Power Save", "name": "power-save"}, {"help": "Set aggregation limit to a lower value when data rate is low.", "label": "Aggr Limit", "name": "aggr-limit"}, {"help": "Set software retry limit to a lower value when data rate is low.", "label": "Retry Limit", "name": "retry-limit"}, {"help": "Limit transmission of BAR frames.", "label": "Send Bar", "name": "send-bar"}],
        },
        "amsdu": {
            "type": "option",
            "help": "Enable/disable 802.11n AMSDU support. AMSDU can improve performance if supported by your WiFi clients (default = enable).",
            "default": "enable",
            "options": [{"help": "Enable AMSDU support.", "label": "Enable", "name": "enable"}, {"help": "Disable AMSDU support.", "label": "Disable", "name": "disable"}],
        },
        "coexistence": {
            "type": "option",
            "help": "Enable/disable allowing both HT20 and HT40 on the same radio (default = enable).",
            "default": "enable",
            "options": [{"help": "Enable support for both HT20 and HT40 on the same radio.", "label": "Enable", "name": "enable"}, {"help": "Disable support for both HT20 and HT40 on the same radio.", "label": "Disable", "name": "disable"}],
        },
        "zero-wait-dfs": {
            "type": "option",
            "help": "Enable/disable zero wait DFS on radio (default = enable).",
            "default": "enable",
            "options": [{"help": "Enable zero wait DFS", "label": "Enable", "name": "enable"}, {"help": "Disable zero wait DFS", "label": "Disable", "name": "disable"}],
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
            "options": [{"help": "Automatically select BSS color value on AP.", "label": "Auto", "name": "auto"}, {"help": "Set BSS color value on this radio based on \u0027bss-color\u0027 CLI.", "label": "Static", "name": "static"}],
        },
        "short-guard-interval": {
            "type": "option",
            "help": "Use either the short guard interval (Short GI) of 400 ns or the long guard interval (Long GI) of 800 ns.",
            "default": "disable",
            "options": [{"help": "Select the 400 ns short guard interval (Short GI).", "label": "Enable", "name": "enable"}, {"help": "Select the 800 ns long guard interval (Long GI).", "label": "Disable", "name": "disable"}],
        },
        "mimo-mode": {
            "type": "option",
            "help": "Configure radio MIMO mode (default = default).",
            "default": "default",
            "options": [{"help": "Default radio MIMO mode.", "label": "Default", "name": "default"}, {"help": "1x1 radio MIMO mode.", "label": "1X1", "name": "1x1"}, {"help": "2x2 radio MIMO mode.", "label": "2X2", "name": "2x2"}, {"help": "3x3 radio MIMO mode.", "label": "3X3", "name": "3x3"}, {"help": "4x4 radio MIMO mode.", "label": "4X4", "name": "4x4"}, {"help": "8x8 radio MIMO mode.", "label": "8X8", "name": "8x8"}],
        },
        "channel-bonding": {
            "type": "option",
            "help": "Channel bandwidth: 320, 240, 160, 80, 40, or 20MHz. Channels may use both 20 and 40 by enabling coexistence.",
            "default": "20MHz",
            "options": [{"help": "320 MHz channel width.", "label": "320Mhz", "name": "320MHz"}, {"help": "240 MHz channel width.", "label": "240Mhz", "name": "240MHz"}, {"help": "160 MHz channel width.", "label": "160Mhz", "name": "160MHz"}, {"help": "80 MHz channel width.", "label": "80Mhz", "name": "80MHz"}, {"help": "40 MHz channel width.", "label": "40Mhz", "name": "40MHz"}, {"help": "20 MHz channel width.", "label": "20Mhz", "name": "20MHz"}],
        },
        "channel-bonding-ext": {
            "type": "option",
            "help": "Channel bandwidth extension: 320 MHz-1 and 320 MHz-2 (default = 320 MHz-2).",
            "default": "320MHz-2",
            "options": [{"help": "320 MHz channel with channel center frequency numbered 31, 95, and 159.", "label": "320Mhz 1", "name": "320MHz-1"}, {"help": "320 MHz channel with channel center frequency numbered 63, 127, and 191.", "label": "320Mhz 2", "name": "320MHz-2"}],
        },
        "optional-antenna": {
            "type": "option",
            "help": "Optional antenna used on FAP (default = none).",
            "default": "none",
            "options": [{"help": "None.", "label": "None", "name": "none"}, {"help": "Customize optional antenna gain.", "label": "Custom", "name": "custom"}, {"help": "6 dBi(2.4GHz) and 6 dBi(5GHz).", "label": "Fant 04Abgn 0606 O N", "name": "FANT-04ABGN-0606-O-N"}, {"help": "14 dBi(2.4GHz) and 14 dBi(5GHz).", "label": "Fant 04Abgn 1414 P N", "name": "FANT-04ABGN-1414-P-N"}, {"help": "8 dBi(2.4GHz) and 6.5 dBi(5GHz).", "label": "Fant 04Abgn 8065 P N", "name": "FANT-04ABGN-8065-P-N"}, {"help": "6 dBi(2.4GHz) and 6 dBi(5GHz).", "label": "Fant 04Abgn 0606 O R", "name": "FANT-04ABGN-0606-O-R"}, {"help": "6 dBi(2.4GHz) and 6 dBi(5GHz).", "label": "Fant 04Abgn 0606 P R", "name": "FANT-04ABGN-0606-P-R"}, {"help": "12 dBi(2.4GHz) and 13 dBi(5GHz).", "label": "Fant 10Acax 1213 D N", "name": "FANT-10ACAX-1213-D-N"}, {"help": "12 dBi(2.4GHz) and 13 dBi(5GHz).", "label": "Fant 08Abgn 1213 D R", "name": "FANT-08ABGN-1213-D-R"}, {"help": "6 dBi(2.4GHz), 6 dBi(5GHz) and 6 dBi(6GHz).", "label": "Fant 04Beax 0606 P R", "name": "FANT-04BEAX-0606-P-R"}],
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
            "options": [{"help": "Enable 802.11d countryie.", "label": "Enable", "name": "enable"}, {"help": "Disable 802.11d countryie.", "label": "Disable", "name": "disable"}],
        },
        "80211mc": {
            "type": "option",
            "help": "Enable/disable 802.11mc responder mode (default = disable).",
            "default": "disable",
            "options": [{"help": "Enable 802.11mc responder mode.", "label": "Enable", "name": "enable"}, {"help": "Disable 802.11mc responder mode.", "label": "Disable", "name": "disable"}],
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
            "options": [{"help": "320 MHz channel width.", "label": "320Mhz", "name": "320MHz"}, {"help": "240 MHz channel width.", "label": "240Mhz", "name": "240MHz"}, {"help": "160 MHz channel width.", "label": "160Mhz", "name": "160MHz"}, {"help": "80 MHz channel width.", "label": "80Mhz", "name": "80MHz"}, {"help": "40 MHz channel width.", "label": "40Mhz", "name": "40MHz"}, {"help": "20 MHz channel width.", "label": "20Mhz", "name": "20MHz"}],
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
            "options": [{"help": "Enable sniffer on WiFi management beacon frame.", "label": "Enable", "name": "enable"}, {"help": "Disable sniffer on WiFi management beacon frame.", "label": "Disable", "name": "disable"}],
        },
        "ap-sniffer-mgmt-probe": {
            "type": "option",
            "help": "Enable/disable sniffer on WiFi management probe frames (default = enable).",
            "default": "enable",
            "options": [{"help": "Enable sniffer on WiFi management probe frame.", "label": "Enable", "name": "enable"}, {"help": "Enable sniffer on WiFi management probe frame.", "label": "Disable", "name": "disable"}],
        },
        "ap-sniffer-mgmt-other": {
            "type": "option",
            "help": "Enable/disable sniffer on WiFi management other frames  (default = enable).",
            "default": "enable",
            "options": [{"help": "Enable sniffer on WiFi management other frame.", "label": "Enable", "name": "enable"}, {"help": "Disable sniffer on WiFi management other frame.", "label": "Disable", "name": "disable"}],
        },
        "ap-sniffer-ctl": {
            "type": "option",
            "help": "Enable/disable sniffer on WiFi control frame (default = enable).",
            "default": "enable",
            "options": [{"help": "Enable sniffer on WiFi control frame.", "label": "Enable", "name": "enable"}, {"help": "Disable sniffer on WiFi control frame.", "label": "Disable", "name": "disable"}],
        },
        "ap-sniffer-data": {
            "type": "option",
            "help": "Enable/disable sniffer on WiFi data frame (default = enable).",
            "default": "enable",
            "options": [{"help": "Enable sniffer on WiFi data frame", "label": "Enable", "name": "enable"}, {"help": "Disable sniffer on WiFi data frame", "label": "Disable", "name": "disable"}],
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
            "options": [{"help": "Open.", "label": "Open", "name": "open"}, {"help": "WPA/WPA2 personal.", "label": "Wpa Personal", "name": "wpa-personal"}, {"help": "WPA2/WPA3 enterprise.", "label": "Wpa Enterprise", "name": "wpa-enterprise"}, {"help": "WPA3 SAE.", "label": "Wpa3 Sae", "name": "wpa3-sae"}, {"help": "OWE.", "label": "Owe", "name": "owe"}],
        },
        "sam-captive-portal": {
            "type": "option",
            "help": "Enable/disable Captive Portal Authentication (default = disable).",
            "default": "disable",
            "options": [{"help": "Enable Captive Portal Authentication.", "label": "Enable", "name": "enable"}, {"help": "Disable Captive Portal Authentication.", "label": "Disable", "name": "disable"}],
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
            "options": [{"help": "EAP PEAP and TLS. (Not applicable in FIPS mode)", "label": "Both", "name": "both"}, {"help": "EAP TLS.", "label": "Tls", "name": "tls"}, {"help": "EAP PEAP. (Not applicable in FIPS mode)", "label": "Peap", "name": "peap"}],
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
            "options": [{"help": "PING test.", "label": "Ping", "name": "ping"}, {"help": "IPERF test.", "label": "Iperf", "name": "iperf"}],
        },
        "sam-server-type": {
            "type": "option",
            "help": "Select SAM server type (default = \"IP\").",
            "default": "ip",
            "options": [{"help": "IPv4 address.", "label": "Ip", "name": "ip"}, {"help": "Fully Qualified Domain Name address.", "label": "Fqdn", "name": "fqdn"}],
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
            "options": [{"help": "UDP.", "label": "Udp", "name": "udp"}, {"help": "TCP.", "label": "Tcp", "name": "tcp"}],
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
            "options": [{"help": "Enable measuring channel utilization.", "label": "Enable", "name": "enable"}, {"help": "Disable measuring channel utilization.", "label": "Disable", "name": "disable"}],
        },
        "wids-profile": {
            "type": "string",
            "help": "Wireless Intrusion Detection System (WIDS) profile name to assign to the radio.",
            "default": "",
            "max_length": 35,
        },
        "ai-darrp-support": {
            "type": "option",
            "help": "Enable/disable support for FortiAIOps to retrieve Distributed Automatic Radio Resource Provisioning (DARRP) data through REST API calls (default = disable).",
            "default": "disable",
            "options": [{"help": "Enable support for FortiAIOps REST API calls for DARRP data.", "label": "Enable", "name": "enable"}, {"help": "Disable support for FortiAIOps REST API calls for DARRP data.", "label": "Disable", "name": "disable"}],
        },
        "darrp": {
            "type": "option",
            "help": "Enable/disable Distributed Automatic Radio Resource Provisioning (DARRP) to make sure the radio is always using the most optimal channel (default = disable).",
            "default": "disable",
            "options": [{"help": "Enable distributed automatic radio resource provisioning.", "label": "Enable", "name": "enable"}, {"help": "Disable distributed automatic radio resource provisioning.", "label": "Disable", "name": "disable"}],
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
            "options": [{"help": "Automatically select tunnel SSIDs.", "label": "Tunnel", "name": "tunnel"}, {"help": "Automatically select local-bridging SSIDs.", "label": "Bridge", "name": "bridge"}, {"help": "Manually select SSIDs.", "label": "Manual", "name": "manual"}],
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
            "options": [{"help": "Enable WMM call admission control.", "label": "Enable", "name": "enable"}, {"help": "Disable WMM call admission control.", "label": "Disable", "name": "disable"}],
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
            "options": [{"help": "Enable WMM bandwidth admission control.", "label": "Enable", "name": "enable"}, {"help": "Disable WMM bandwidth admission control.", "label": "Disable", "name": "disable"}],
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
            "options": [{"help": "Radio 4 is disabled.", "label": "Disabled", "name": "disabled"}, {"help": "Radio 4 operates as an access point that allows WiFi clients to connect to your network.", "label": "Ap", "name": "ap"}, {"help": "Radio 4 operates as a dedicated monitor. As a monitor, the radio scans for other WiFi access points and adds them to the Rogue AP monitor list.", "label": "Monitor", "name": "monitor"}, {"help": "Radio 4 operates as a sniffer capturing WiFi frames on air.", "label": "Sniffer", "name": "sniffer"}, {"help": "Radio 4 operates as a station that can connect to a neighboring AP for connectivity and health check.", "label": "Sam", "name": "sam"}],
        },
        "band": {
            "type": "option",
            "help": "WiFi band that Radio 4 operates on.",
            "default": "",
            "options": [{"help": "802.11a.", "label": "802.11A", "name": "802.11a"}, {"help": "802.11b.", "label": "802.11B", "name": "802.11b"}, {"help": "802.11g.", "label": "802.11G", "name": "802.11g"}, {"help": "802.11n (WiFi 4) at 2.4GHz.", "label": "802.11N 2G", "name": "802.11n-2G"}, {"help": "802.11n (WiFi 4) at 5GHz.", "label": "802.11N 5G", "name": "802.11n-5G"}, {"help": "802.11ac (WiFi 5) at 2.4GHz.", "label": "802.11Ac 2G", "name": "802.11ac-2G"}, {"help": "802.11ac (WiFi 5) at 5GHz.", "label": "802.11Ac 5G", "name": "802.11ac-5G"}, {"help": "802.11ax (WiFi 6) at 2.4GHz.", "label": "802.11Ax 2G", "name": "802.11ax-2G"}, {"help": "802.11ax (WiFi 6) at 5GHz.", "label": "802.11Ax 5G", "name": "802.11ax-5G"}, {"help": "802.11ax (WiFi 6) at 6GHz.", "label": "802.11Ax 6G", "name": "802.11ax-6G"}, {"help": "802.11be (WiFi 7) at 2.4GHz.", "label": "802.11Be 2G", "name": "802.11be-2G"}, {"help": "802.11be (WiFi 7) at 5GHz.", "label": "802.11Be 5G", "name": "802.11be-5G"}, {"help": "802.11be (WiFi 7) at 6GHz.", "label": "802.11Be 6G", "name": "802.11be-6G"}],
        },
        "band-5g-type": {
            "type": "option",
            "help": "WiFi 5G band type.",
            "default": "5g-full",
            "options": [{"help": "Full 5G band.", "label": "5G Full", "name": "5g-full"}, {"help": "High 5G band.", "label": "5G High", "name": "5g-high"}, {"help": "Low 5G band.", "label": "5G Low", "name": "5g-low"}],
        },
        "drma": {
            "type": "option",
            "help": "Enable/disable dynamic radio mode assignment (DRMA) (default = disable).",
            "default": "disable",
            "options": [{"help": "Disable dynamic radio mode assignment (DRMA).", "label": "Disable", "name": "disable"}, {"help": "Enable dynamic radio mode assignment (DRMA).", "label": "Enable", "name": "enable"}],
        },
        "drma-sensitivity": {
            "type": "option",
            "help": "Network Coverage Factor (NCF) percentage required to consider a radio as redundant (default = low).",
            "default": "low",
            "options": [{"help": "Consider a radio as redundant when its NCF is 100%.", "label": "Low", "name": "low"}, {"help": "Consider a radio as redundant when its NCF is 95%.", "label": "Medium", "name": "medium"}, {"help": "Consider a radio as redundant when its NCF is 90%.", "label": "High", "name": "high"}],
        },
        "airtime-fairness": {
            "type": "option",
            "help": "Enable/disable airtime fairness (default = disable).",
            "default": "disable",
            "options": [{"help": "Enable airtime fairness (ATF) support.", "label": "Enable", "name": "enable"}, {"help": "Disable airtime fairness (ATF) support.", "label": "Disable", "name": "disable"}],
        },
        "protection-mode": {
            "type": "option",
            "help": "Enable/disable 802.11g protection modes to support backwards compatibility with older clients (rtscts, ctsonly, disable).",
            "default": "disable",
            "options": [{"help": "Enable 802.11g protection RTS/CTS mode.", "label": "Rtscts", "name": "rtscts"}, {"help": "Enable 802.11g protection CTS only mode.", "label": "Ctsonly", "name": "ctsonly"}, {"help": "Disable 802.11g protection mode.", "label": "Disable", "name": "disable"}],
        },
        "powersave-optimize": {
            "type": "option",
            "help": "Enable client power-saving features such as TIM, AC VO, and OBSS etc.",
            "default": "",
            "options": [{"help": "TIM bit for client in power save mode.", "label": "Tim", "name": "tim"}, {"help": "Use AC VO priority to send out packets in the power save queue.", "label": "Ac Vo", "name": "ac-vo"}, {"help": "Do not put OBSS scan IE into beacon and probe response frames.", "label": "No Obss Scan", "name": "no-obss-scan"}, {"help": "Do not send frame using 11b data rate.", "label": "No 11B Rate", "name": "no-11b-rate"}, {"help": "Adapt transmitting PHY rate with receiving PHY rate from a client.", "label": "Client Rate Follow", "name": "client-rate-follow"}],
        },
        "transmit-optimize": {
            "type": "option",
            "help": "Packet transmission optimization options including power saving, aggregation limiting, retry limiting, etc. All are enabled by default.",
            "default": "power-save aggr-limit retry-limit send-bar",
            "options": [{"help": "Disable packet transmission optimization.", "label": "Disable", "name": "disable"}, {"help": "Tag client as operating in power save mode if excessive transmit retries occur.", "label": "Power Save", "name": "power-save"}, {"help": "Set aggregation limit to a lower value when data rate is low.", "label": "Aggr Limit", "name": "aggr-limit"}, {"help": "Set software retry limit to a lower value when data rate is low.", "label": "Retry Limit", "name": "retry-limit"}, {"help": "Limit transmission of BAR frames.", "label": "Send Bar", "name": "send-bar"}],
        },
        "amsdu": {
            "type": "option",
            "help": "Enable/disable 802.11n AMSDU support. AMSDU can improve performance if supported by your WiFi clients (default = enable).",
            "default": "enable",
            "options": [{"help": "Enable AMSDU support.", "label": "Enable", "name": "enable"}, {"help": "Disable AMSDU support.", "label": "Disable", "name": "disable"}],
        },
        "coexistence": {
            "type": "option",
            "help": "Enable/disable allowing both HT20 and HT40 on the same radio (default = enable).",
            "default": "enable",
            "options": [{"help": "Enable support for both HT20 and HT40 on the same radio.", "label": "Enable", "name": "enable"}, {"help": "Disable support for both HT20 and HT40 on the same radio.", "label": "Disable", "name": "disable"}],
        },
        "zero-wait-dfs": {
            "type": "option",
            "help": "Enable/disable zero wait DFS on radio (default = enable).",
            "default": "enable",
            "options": [{"help": "Enable zero wait DFS", "label": "Enable", "name": "enable"}, {"help": "Disable zero wait DFS", "label": "Disable", "name": "disable"}],
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
            "options": [{"help": "Automatically select BSS color value on AP.", "label": "Auto", "name": "auto"}, {"help": "Set BSS color value on this radio based on \u0027bss-color\u0027 CLI.", "label": "Static", "name": "static"}],
        },
        "short-guard-interval": {
            "type": "option",
            "help": "Use either the short guard interval (Short GI) of 400 ns or the long guard interval (Long GI) of 800 ns.",
            "default": "disable",
            "options": [{"help": "Select the 400 ns short guard interval (Short GI).", "label": "Enable", "name": "enable"}, {"help": "Select the 800 ns long guard interval (Long GI).", "label": "Disable", "name": "disable"}],
        },
        "mimo-mode": {
            "type": "option",
            "help": "Configure radio MIMO mode (default = default).",
            "default": "default",
            "options": [{"help": "Default radio MIMO mode.", "label": "Default", "name": "default"}, {"help": "1x1 radio MIMO mode.", "label": "1X1", "name": "1x1"}, {"help": "2x2 radio MIMO mode.", "label": "2X2", "name": "2x2"}, {"help": "3x3 radio MIMO mode.", "label": "3X3", "name": "3x3"}, {"help": "4x4 radio MIMO mode.", "label": "4X4", "name": "4x4"}, {"help": "8x8 radio MIMO mode.", "label": "8X8", "name": "8x8"}],
        },
        "channel-bonding": {
            "type": "option",
            "help": "Channel bandwidth: 320, 240, 160, 80, 40, or 20MHz. Channels may use both 20 and 40 by enabling coexistence.",
            "default": "20MHz",
            "options": [{"help": "320 MHz channel width.", "label": "320Mhz", "name": "320MHz"}, {"help": "240 MHz channel width.", "label": "240Mhz", "name": "240MHz"}, {"help": "160 MHz channel width.", "label": "160Mhz", "name": "160MHz"}, {"help": "80 MHz channel width.", "label": "80Mhz", "name": "80MHz"}, {"help": "40 MHz channel width.", "label": "40Mhz", "name": "40MHz"}, {"help": "20 MHz channel width.", "label": "20Mhz", "name": "20MHz"}],
        },
        "channel-bonding-ext": {
            "type": "option",
            "help": "Channel bandwidth extension: 320 MHz-1 and 320 MHz-2 (default = 320 MHz-2).",
            "default": "320MHz-2",
            "options": [{"help": "320 MHz channel with channel center frequency numbered 31, 95, and 159.", "label": "320Mhz 1", "name": "320MHz-1"}, {"help": "320 MHz channel with channel center frequency numbered 63, 127, and 191.", "label": "320Mhz 2", "name": "320MHz-2"}],
        },
        "optional-antenna": {
            "type": "option",
            "help": "Optional antenna used on FAP (default = none).",
            "default": "none",
            "options": [{"help": "None.", "label": "None", "name": "none"}, {"help": "Customize optional antenna gain.", "label": "Custom", "name": "custom"}, {"help": "6 dBi(2.4GHz) and 6 dBi(5GHz).", "label": "Fant 04Abgn 0606 O N", "name": "FANT-04ABGN-0606-O-N"}, {"help": "14 dBi(2.4GHz) and 14 dBi(5GHz).", "label": "Fant 04Abgn 1414 P N", "name": "FANT-04ABGN-1414-P-N"}, {"help": "8 dBi(2.4GHz) and 6.5 dBi(5GHz).", "label": "Fant 04Abgn 8065 P N", "name": "FANT-04ABGN-8065-P-N"}, {"help": "6 dBi(2.4GHz) and 6 dBi(5GHz).", "label": "Fant 04Abgn 0606 O R", "name": "FANT-04ABGN-0606-O-R"}, {"help": "6 dBi(2.4GHz) and 6 dBi(5GHz).", "label": "Fant 04Abgn 0606 P R", "name": "FANT-04ABGN-0606-P-R"}, {"help": "12 dBi(2.4GHz) and 13 dBi(5GHz).", "label": "Fant 10Acax 1213 D N", "name": "FANT-10ACAX-1213-D-N"}, {"help": "12 dBi(2.4GHz) and 13 dBi(5GHz).", "label": "Fant 08Abgn 1213 D R", "name": "FANT-08ABGN-1213-D-R"}, {"help": "6 dBi(2.4GHz), 6 dBi(5GHz) and 6 dBi(6GHz).", "label": "Fant 04Beax 0606 P R", "name": "FANT-04BEAX-0606-P-R"}],
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
            "options": [{"help": "Enable 802.11d countryie.", "label": "Enable", "name": "enable"}, {"help": "Disable 802.11d countryie.", "label": "Disable", "name": "disable"}],
        },
        "80211mc": {
            "type": "option",
            "help": "Enable/disable 802.11mc responder mode (default = disable).",
            "default": "disable",
            "options": [{"help": "Enable 802.11mc responder mode.", "label": "Enable", "name": "enable"}, {"help": "Disable 802.11mc responder mode.", "label": "Disable", "name": "disable"}],
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
            "options": [{"help": "320 MHz channel width.", "label": "320Mhz", "name": "320MHz"}, {"help": "240 MHz channel width.", "label": "240Mhz", "name": "240MHz"}, {"help": "160 MHz channel width.", "label": "160Mhz", "name": "160MHz"}, {"help": "80 MHz channel width.", "label": "80Mhz", "name": "80MHz"}, {"help": "40 MHz channel width.", "label": "40Mhz", "name": "40MHz"}, {"help": "20 MHz channel width.", "label": "20Mhz", "name": "20MHz"}],
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
            "options": [{"help": "Enable sniffer on WiFi management beacon frame.", "label": "Enable", "name": "enable"}, {"help": "Disable sniffer on WiFi management beacon frame.", "label": "Disable", "name": "disable"}],
        },
        "ap-sniffer-mgmt-probe": {
            "type": "option",
            "help": "Enable/disable sniffer on WiFi management probe frames (default = enable).",
            "default": "enable",
            "options": [{"help": "Enable sniffer on WiFi management probe frame.", "label": "Enable", "name": "enable"}, {"help": "Enable sniffer on WiFi management probe frame.", "label": "Disable", "name": "disable"}],
        },
        "ap-sniffer-mgmt-other": {
            "type": "option",
            "help": "Enable/disable sniffer on WiFi management other frames  (default = enable).",
            "default": "enable",
            "options": [{"help": "Enable sniffer on WiFi management other frame.", "label": "Enable", "name": "enable"}, {"help": "Disable sniffer on WiFi management other frame.", "label": "Disable", "name": "disable"}],
        },
        "ap-sniffer-ctl": {
            "type": "option",
            "help": "Enable/disable sniffer on WiFi control frame (default = enable).",
            "default": "enable",
            "options": [{"help": "Enable sniffer on WiFi control frame.", "label": "Enable", "name": "enable"}, {"help": "Disable sniffer on WiFi control frame.", "label": "Disable", "name": "disable"}],
        },
        "ap-sniffer-data": {
            "type": "option",
            "help": "Enable/disable sniffer on WiFi data frame (default = enable).",
            "default": "enable",
            "options": [{"help": "Enable sniffer on WiFi data frame", "label": "Enable", "name": "enable"}, {"help": "Disable sniffer on WiFi data frame", "label": "Disable", "name": "disable"}],
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
            "options": [{"help": "Open.", "label": "Open", "name": "open"}, {"help": "WPA/WPA2 personal.", "label": "Wpa Personal", "name": "wpa-personal"}, {"help": "WPA2/WPA3 enterprise.", "label": "Wpa Enterprise", "name": "wpa-enterprise"}, {"help": "WPA3 SAE.", "label": "Wpa3 Sae", "name": "wpa3-sae"}, {"help": "OWE.", "label": "Owe", "name": "owe"}],
        },
        "sam-captive-portal": {
            "type": "option",
            "help": "Enable/disable Captive Portal Authentication (default = disable).",
            "default": "disable",
            "options": [{"help": "Enable Captive Portal Authentication.", "label": "Enable", "name": "enable"}, {"help": "Disable Captive Portal Authentication.", "label": "Disable", "name": "disable"}],
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
            "options": [{"help": "EAP PEAP and TLS. (Not applicable in FIPS mode)", "label": "Both", "name": "both"}, {"help": "EAP TLS.", "label": "Tls", "name": "tls"}, {"help": "EAP PEAP. (Not applicable in FIPS mode)", "label": "Peap", "name": "peap"}],
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
            "options": [{"help": "PING test.", "label": "Ping", "name": "ping"}, {"help": "IPERF test.", "label": "Iperf", "name": "iperf"}],
        },
        "sam-server-type": {
            "type": "option",
            "help": "Select SAM server type (default = \"IP\").",
            "default": "ip",
            "options": [{"help": "IPv4 address.", "label": "Ip", "name": "ip"}, {"help": "Fully Qualified Domain Name address.", "label": "Fqdn", "name": "fqdn"}],
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
            "options": [{"help": "UDP.", "label": "Udp", "name": "udp"}, {"help": "TCP.", "label": "Tcp", "name": "tcp"}],
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
            "options": [{"help": "Enable measuring channel utilization.", "label": "Enable", "name": "enable"}, {"help": "Disable measuring channel utilization.", "label": "Disable", "name": "disable"}],
        },
        "wids-profile": {
            "type": "string",
            "help": "Wireless Intrusion Detection System (WIDS) profile name to assign to the radio.",
            "default": "",
            "max_length": 35,
        },
        "ai-darrp-support": {
            "type": "option",
            "help": "Enable/disable support for FortiAIOps to retrieve Distributed Automatic Radio Resource Provisioning (DARRP) data through REST API calls (default = disable).",
            "default": "disable",
            "options": [{"help": "Enable support for FortiAIOps REST API calls for DARRP data.", "label": "Enable", "name": "enable"}, {"help": "Disable support for FortiAIOps REST API calls for DARRP data.", "label": "Disable", "name": "disable"}],
        },
        "darrp": {
            "type": "option",
            "help": "Enable/disable Distributed Automatic Radio Resource Provisioning (DARRP) to make sure the radio is always using the most optimal channel (default = disable).",
            "default": "disable",
            "options": [{"help": "Enable distributed automatic radio resource provisioning.", "label": "Enable", "name": "enable"}, {"help": "Disable distributed automatic radio resource provisioning.", "label": "Disable", "name": "disable"}],
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
            "options": [{"help": "Automatically select tunnel SSIDs.", "label": "Tunnel", "name": "tunnel"}, {"help": "Automatically select local-bridging SSIDs.", "label": "Bridge", "name": "bridge"}, {"help": "Manually select SSIDs.", "label": "Manual", "name": "manual"}],
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
            "options": [{"help": "Enable WMM call admission control.", "label": "Enable", "name": "enable"}, {"help": "Disable WMM call admission control.", "label": "Disable", "name": "disable"}],
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
            "options": [{"help": "Enable WMM bandwidth admission control.", "label": "Enable", "name": "enable"}, {"help": "Disable WMM bandwidth admission control.", "label": "Disable", "name": "disable"}],
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
            "options": [{"help": "Enable Ekahau blink mode.", "label": "Enable", "name": "enable"}, {"help": "Disable Ekahau blink mode.", "label": "Disable", "name": "disable"}],
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
            "options": [{"help": "Enable AeroScout support.", "label": "Enable", "name": "enable"}, {"help": "Disable AeroScout support.", "label": "Disable", "name": "disable"}],
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
            "options": [{"help": "Enable AeroScout MU mode support.", "label": "Enable", "name": "enable"}, {"help": "Disable AeroScout MU mode support.", "label": "Disable", "name": "disable"}],
        },
        "aeroscout-ap-mac": {
            "type": "option",
            "help": "Use BSSID or board MAC address as AP MAC address in AeroScout AP messages (default = bssid).",
            "default": "bssid",
            "options": [{"help": "Use BSSID as AP MAC address in AeroScout AP messages.", "label": "Bssid", "name": "bssid"}, {"help": "Use board MAC address as AP MAC address in AeroScout AP messages.", "label": "Board Mac", "name": "board-mac"}],
        },
        "aeroscout-mmu-report": {
            "type": "option",
            "help": "Enable/disable compounded AeroScout tag and MU report (default = enable).",
            "default": "enable",
            "options": [{"help": "Enable compounded AeroScout tag and MU report.", "label": "Enable", "name": "enable"}, {"help": "Disable compounded AeroScout tag and MU report.", "label": "Disable", "name": "disable"}],
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
            "options": [{"help": "FortiPresence monitors foreign channels only. Foreign channels mean all other available channels than the current operating channel of the WTP, AP, or FortiAP.", "label": "Foreign", "name": "foreign"}, {"help": "Enable FortiPresence on both foreign and home channels. Select this option to have FortiPresence monitor all WiFi channels.", "label": "Both", "name": "both"}, {"help": "Disable FortiPresence.", "label": "Disable", "name": "disable"}],
        },
        "fortipresence-server-addr-type": {
            "type": "option",
            "help": "FortiPresence server address type (default = ipv4).",
            "default": "ipv4",
            "options": [{"help": "IPv4 address.", "label": "Ipv4", "name": "ipv4"}, {"help": "Fully Qualified Domain Name address.", "label": "Fqdn", "name": "fqdn"}],
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
            "options": [{"help": "Enable FortiPresence finding and reporting rogue APs.", "label": "Enable", "name": "enable"}, {"help": "Disable FortiPresence finding and reporting rogue APs.", "label": "Disable", "name": "disable"}],
        },
        "fortipresence-unassoc": {
            "type": "option",
            "help": "Enable/disable FortiPresence finding and reporting unassociated stations.",
            "default": "enable",
            "options": [{"help": "Enable FortiPresence finding and reporting unassociated stations.", "label": "Enable", "name": "enable"}, {"help": "Disable FortiPresence finding and reporting unassociated stations.", "label": "Disable", "name": "disable"}],
        },
        "fortipresence-ble": {
            "type": "option",
            "help": "Enable/disable FortiPresence finding and reporting BLE devices.",
            "default": "enable",
            "options": [{"help": "Enable FortiPresence finding and reporting BLE devices.", "label": "Enable", "name": "enable"}, {"help": "Disable FortiPresence finding and reporting BLE devices.", "label": "Disable", "name": "disable"}],
        },
        "station-locate": {
            "type": "option",
            "help": "Enable/disable client station locating services for all clients, whether associated or not (default = disable).",
            "default": "disable",
            "options": [{"help": "Enable station locating service.", "label": "Enable", "name": "enable"}, {"help": "Disable station locating service.", "label": "Disable", "name": "disable"}],
        },
        "ble-rtls": {
            "type": "option",
            "help": "Set BLE Real Time Location Service (RTLS) support (default = none).",
            "default": "none",
            "options": [{"help": "Set BLE RTLS to none (default = none).", "label": "None", "name": "none"}, {"help": "Set BLE RTLS to PoleStar.", "label": "Polestar", "name": "polestar"}, {"help": "Set BLE RTLS to Evresys.", "label": "Evresys", "name": "evresys"}],
        },
        "ble-rtls-protocol": {
            "type": "option",
            "help": "Select the protocol to report Measurements, Advertising Data, or Location Data to Cloud Server (default = WSS).",
            "default": "WSS",
            "options": [{"help": "Use WebSocket protocol to report Measurements, Advertising Data, or Location Data to Cloud Server.", "label": "Wss", "name": "WSS"}],
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
            "options": [{"help": "Compliance Level 2 - Full Cloud Support, IoT and Fast-Response.", "label": "Compliance Level 2", "name": "compliance-level-2"}],
        },
        "scd-enable": {
            "type": "option",
            "help": "Enable/disable ESL SES-imagotag Serial Communication Daemon (SCD) (default = disable).",
            "default": "disable",
            "options": [{"help": "Enable ESL SES-imagotag SCD.", "label": "Enable", "name": "enable"}, {"help": "Disable ESL SES-imagotag SCD.", "label": "Disable", "name": "disable"}],
        },
        "esl-channel": {
            "type": "option",
            "help": "ESL SES-imagotag dongle channel (default = 127).",
            "default": "127",
            "options": [{"help": "No esl-channel is set.", "label": " 1", "name": "-1"}, {"help": "ESL channel 0.", "label": "0", "name": "0"}, {"help": "ESL channel 1.", "label": "1", "name": "1"}, {"help": "ESL channel 2.", "label": "2", "name": "2"}, {"help": "ESL channel 3.", "label": "3", "name": "3"}, {"help": "ESL channel 4.", "label": "4", "name": "4"}, {"help": "ESL channel 5.", "label": "5", "name": "5"}, {"help": "ESL channel 6.", "label": "6", "name": "6"}, {"help": "ESL channel 7.", "label": "7", "name": "7"}, {"help": "ESL channel 8.", "label": "8", "name": "8"}, {"help": "ESL channel 9.", "label": "9", "name": "9"}, {"help": "ESL channel 10.", "label": "10", "name": "10"}, {"help": "Managed channel enabled, indicates that the APC (server) is setting the esl-channel via the slot channel", "label": "127", "name": "127"}],
        },
        "output-power": {
            "type": "option",
            "help": "ESL SES-imagotag dongle output power (default = A).",
            "default": "a",
            "options": [{"help": "About 15mW.", "label": "A", "name": "a"}, {"help": "About 7mW.", "label": "B", "name": "b"}, {"help": "About 5mW.", "label": "C", "name": "c"}, {"help": "About 1mW.", "label": "D", "name": "d"}, {"help": "About 13mW.", "label": "E", "name": "e"}, {"help": "About 10mW.", "label": "F", "name": "f"}, {"help": "About 3mW.", "label": "G", "name": "g"}, {"help": "About 2mW.", "label": "H", "name": "h"}],
        },
        "apc-addr-type": {
            "type": "option",
            "help": "ESL SES-imagotag APC address type (default = fqdn).",
            "default": "fqdn",
            "options": [{"help": "Fully Qualified Domain Name address.", "label": "Fqdn", "name": "fqdn"}, {"help": "IPv4 address.", "label": "Ip", "name": "ip"}],
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
            "options": [{"help": "No support for coexistence of USB-Dongle with WiFi AP.", "label": "None", "name": "none"}],
        },
        "tls-cert-verification": {
            "type": "option",
            "help": "Enable/disable TLS certificate verification (default = enable).",
            "default": "enable",
            "options": [{"help": "Enable TLS Certificate verification.", "label": "Enable", "name": "enable"}, {"help": "Disable TLS Certificate verification.", "label": "Disable", "name": "disable"}],
        },
        "tls-fqdn-verification": {
            "type": "option",
            "help": "Enable/disable TLS FQDN verification (default = disable).",
            "default": "disable",
            "options": [{"help": "Enable TLS FQDN verification.", "label": "Enable", "name": "enable"}, {"help": "Disable TLS FQDN verification.", "label": "Disable", "name": "disable"}],
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_CONTROL_MESSAGE_OFFLOAD = [
    "ebp-frame",  # Ekahau blink protocol (EBP) frames.
    "aeroscout-tag",  # AeroScout tag.
    "ap-list",  # Rogue AP list.
    "sta-list",  # Rogue STA list.
    "sta-cap-list",  # STA capability list.
    "stats",  # WTP, radio, VAP, and STA statistics.
    "aeroscout-mu",  # AeroScout Mobile Unit (MU) report.
    "sta-health",  # STA health log.
    "spectral-analysis",  # Spectral analysis report.
]
VALID_BODY_APCFG_MESH = [
    "enable",  # Enable AP local mesh configuration.
    "disable",  # Disable AP local mesh configuration.
]
VALID_BODY_APCFG_MESH_AP_TYPE = [
    "ethernet",  # Use ethernet uplink.
    "mesh",  # Use mesh uplink.
    "auto",  # Ethernet with mesh backup support.
]
VALID_BODY_APCFG_MESH_ETH_BRIDGE = [
    "enable",  # Enable AP local mesh eth bridge configuration.
    "disable",  # Disable AP local mesh eth bridge configuration.
]
VALID_BODY_WAN_PORT_MODE = [
    "wan-lan",  # Enable using a WAN port as a LAN port.
    "wan-only",  # Disable using a WAN port as a LAN port.
]
VALID_BODY_ENERGY_EFFICIENT_ETHERNET = [
    "enable",  # Enable use of energy efficient Ethernet on WTP.
    "disable",  # Disable use of energy efficient Ethernet on WTP.
]
VALID_BODY_LED_STATE = [
    "enable",  # Enable use of LEDs on WTP.
    "disable",  # Disable use of LEDs on WTP.
]
VALID_BODY_DTLS_POLICY = [
    "clear-text",  # Clear Text Data Channel.
    "dtls-enabled",  # DTLS Enabled Data Channel.
    "ipsec-vpn",  # IPsec VPN Data Channel.
    "ipsec-sn-vpn",  # IPsec VPN Data Channel with FortiAP's SN in the first IKE messages.
]
VALID_BODY_DTLS_IN_KERNEL = [
    "enable",  # Enable data channel DTLS in kernel.
    "disable",  # Disable data channel DTLS in kernel.
]
VALID_BODY_HANDOFF_ROAMING = [
    "enable",  # Enable handoff roaming.
    "disable",  # Disable handoff roaming.
]
VALID_BODY_AP_COUNTRY = [
    "--",  # NO_COUNTRY_SET
    "AF",  # AFGHANISTAN
    "AL",  # ALBANIA
    "DZ",  # ALGERIA
    "AS",  # AMERICAN SAMOA
    "AO",  # ANGOLA
    "AR",  # ARGENTINA
    "AM",  # ARMENIA
    "AU",  # AUSTRALIA
    "AT",  # AUSTRIA
    "AZ",  # AZERBAIJAN
    "BS",  # BAHAMAS
    "BH",  # BAHRAIN
    "BD",  # BANGLADESH
    "BB",  # BARBADOS
    "BY",  # BELARUS
    "BE",  # BELGIUM
    "BZ",  # BELIZE
    "BJ",  # BENIN
    "BM",  # BERMUDA
    "BT",  # BHUTAN
    "BO",  # BOLIVIA
    "BA",  # BOSNIA AND HERZEGOVINA
    "BW",  # BOTSWANA
    "BR",  # BRAZIL
    "BN",  # BRUNEI DARUSSALAM
    "BG",  # BULGARIA
    "BF",  # BURKINA-FASO
    "KH",  # CAMBODIA
    "CM",  # CAMEROON
    "KY",  # CAYMAN ISLANDS
    "CF",  # CENTRAL AFRICA REPUBLIC
    "TD",  # CHAD  
    "CL",  # CHILE
    "CN",  # CHINA
    "CX",  # CHRISTMAS ISLAND
    "CO",  # COLOMBIA
    "CG",  # CONGO REPUBLIC
    "CD",  # DEMOCRATIC REPUBLIC OF CONGO
    "CR",  # COSTA RICA
    "HR",  # CROATIA
    "CY",  # CYPRUS
    "CZ",  # CZECH REPUBLIC
    "DK",  # DENMARK
    "DJ",  # DJIBOUTI
    "DM",  # DOMINICA
    "DO",  # DOMINICAN REPUBLIC
    "EC",  # ECUADOR
    "EG",  # EGYPT
    "SV",  # EL SALVADOR
    "ET",  # ETHIOPIA
    "EE",  # ESTONIA
    "GF",  # FRENCH GUIANA
    "PF",  # FRENCH POLYNESIA
    "FO",  # FAEROE ISLANDS
    "FJ",  # FIJI
    "FI",  # FINLAND
    "FR",  # FRANCE
    "GA",  # GABON
    "GE",  # GEORGIA
    "GM",  # GAMBIA
    "DE",  # GERMANY
    "GH",  # GHANA
    "GI",  # GIBRALTAR
    "GR",  # GREECE
    "GL",  # GREENLAND
    "GD",  # GRENADA
    "GP",  # GUADELOUPE
    "GU",  # GUAM
    "GT",  # GUATEMALA
    "GY",  # GUYANA
    "HT",  # HAITI
    "HN",  # HONDURAS
    "HK",  # HONG KONG
    "HU",  # HUNGARY
    "IS",  # ICELAND
    "IN",  # INDIA
    "ID",  # INDONESIA
    "IQ",  # IRAQ
    "IE",  # IRELAND
    "IM",  # ISLE OF MAN
    "IL",  # ISRAEL
    "IT",  # ITALY
    "CI",  # COTE_D_IVOIRE
    "JM",  # JAMAICA
    "JO",  # JORDAN
    "KZ",  # KAZAKHSTAN
    "KE",  # KENYA
    "KR",  # KOREA REPUBLIC
    "KW",  # KUWAIT
    "LA",  # LAOS
    "LV",  # LATVIA
    "LB",  # LEBANON
    "LS",  # LESOTHO
    "LR",  # LIBERIA
    "LY",  # LIBYA
    "LI",  # LIECHTENSTEIN
    "LT",  # LITHUANIA
    "LU",  # LUXEMBOURG
    "MO",  # MACAU SAR
    "MK",  # MACEDONIA, FYRO
    "MG",  # MADAGASCAR
    "MW",  # MALAWI
    "MY",  # MALAYSIA
    "MV",  # MALDIVES
    "ML",  # MALI
    "MT",  # MALTA
    "MH",  # MARSHALL ISLANDS
    "MQ",  # MARTINIQUE
    "MR",  # MAURITANIA
    "MU",  # MAURITIUS
    "YT",  # MAYOTTE
    "MX",  # MEXICO
    "FM",  # MICRONESIA
    "MD",  # REPUBLIC OF MOLDOVA
    "MC",  # MONACO
    "MN",  # MONGOLIA
    "MA",  # MOROCCO
    "MZ",  # MOZAMBIQUE
    "MM",  # MYANMAR
    "NA",  # NAMIBIA
    "NP",  # NEPAL
    "NL",  # NETHERLANDS
    "AN",  # NETHERLANDS ANTILLES
    "AW",  # ARUBA
    "NZ",  # NEW ZEALAND
    "NI",  # NICARAGUA
    "NE",  # NIGER
    "NG",  # NIGERIA
    "NO",  # NORWAY
    "MP",  # NORTHERN MARIANA ISLANDS
    "OM",  # OMAN
    "PK",  # PAKISTAN
    "PW",  # PALAU
    "PA",  # PANAMA
    "PG",  # PAPUA NEW GUINEA
    "PY",  # PARAGUAY
    "PE",  # PERU
    "PH",  # PHILIPPINES
    "PL",  # POLAND
    "PT",  # PORTUGAL
    "PR",  # PUERTO RICO
    "QA",  # QATAR
    "RE",  # REUNION
    "RO",  # ROMANIA
    "RU",  # RUSSIA
    "RW",  # RWANDA
    "BL",  # SAINT BARTHELEMY
    "KN",  # SAINT KITTS AND NEVIS
    "LC",  # SAINT LUCIA
    "MF",  # SAINT MARTIN
    "PM",  # SAINT PIERRE AND MIQUELON
    "VC",  # SAINT VINCENT AND GRENADIENS
    "SA",  # SAUDI ARABIA
    "SN",  # SENEGAL
    "RS",  # REPUBLIC OF SERBIA
    "ME",  # MONTENEGRO
    "SL",  # SIERRA LEONE
    "SG",  # SINGAPORE
    "SK",  # SLOVAKIA
    "SI",  # SLOVENIA
    "SO",  # SOMALIA
    "ZA",  # SOUTH AFRICA
    "ES",  # SPAIN
    "LK",  # SRI LANKA
    "SR",  # SURINAME
    "SZ",  # SWAZILAND
    "SE",  # SWEDEN
    "CH",  # SWITZERLAND
    "TW",  # TAIWAN
    "TZ",  # TANZANIA
    "TH",  # THAILAND
    "TL",  # TIMOR-LESTE
    "TG",  # TOGO
    "TT",  # TRINIDAD AND TOBAGO
    "TN",  # TUNISIA
    "TR",  # TURKEY
    "TM",  # TURKMENISTAN
    "AE",  # UNITED ARAB EMIRATES
    "TC",  # TURKS AND CAICOS
    "UG",  # UGANDA
    "UA",  # UKRAINE
    "GB",  # UNITED KINGDOM
    "US",  # UNITED STATES2
    "PS",  # UNITED STATES (PUBLIC SAFETY)
    "UY",  # URUGUAY
    "UZ",  # UZBEKISTAN
    "VU",  # VANUATU
    "VE",  # VENEZUELA
    "VN",  # VIET NAM
    "VI",  # VIRGIN ISLANDS
    "WF",  # WALLIS AND FUTUNA
    "YE",  # YEMEN
    "ZM",  # ZAMBIA
    "ZW",  # ZIMBABWE
    "JP",  # JAPAN14
    "CA",  # CANADA2
]
VALID_BODY_IP_FRAGMENT_PREVENTING = [
    "tcp-mss-adjust",  # TCP maximum segment size adjustment.
    "icmp-unreachable",  # Drop packet and send ICMP Destination Unreachable
]
VALID_BODY_SPLIT_TUNNELING_ACL_PATH = [
    "tunnel",  # Split tunneling ACL list traffic will be tunnel.
    "local",  # Split tunneling ACL list traffic will be local NATed.
]
VALID_BODY_SPLIT_TUNNELING_ACL_LOCAL_AP_SUBNET = [
    "enable",  # Enable automatically adding local subnetwork of FortiAP to split-tunneling ACL.
    "disable",  # Disable automatically adding local subnetwork of FortiAP to split-tunneling ACL.
]
VALID_BODY_ALLOWACCESS = [
    "https",  # HTTPS access.
    "ssh",  # SSH access.
    "snmp",  # SNMP access.
]
VALID_BODY_LOGIN_PASSWD_CHANGE = [
    "yes",  # Change the managed WTP, FortiAP or AP's administrator password. Use the login-password option to set the password.
    "default",  # Keep the managed WTP, FortiAP or AP's administrator password set to the factory default.
    "no",  # Do not change the managed WTP, FortiAP or AP's administrator password.
]
VALID_BODY_LLDP = [
    "enable",  # Enable LLDP.
    "disable",  # Disable LLDP.
]
VALID_BODY_POE_MODE = [
    "auto",  # Automatically detect the PoE mode.
    "8023af",  # Use 802.3af PoE mode.
    "8023at",  # Use 802.3at PoE mode.
    "power-adapter",  # Use the power adapter to control the PoE mode.
    "full",  # Use full power mode.
    "high",  # Use high power mode.
    "low",  # Use low power mode.
]
VALID_BODY_USB_PORT = [
    "enable",  # Enable USB port.
    "disable",  # Disable USB port.
]
VALID_BODY_FREQUENCY_HANDOFF = [
    "enable",  # Enable frequency handoff.
    "disable",  # Disable frequency handoff.
]
VALID_BODY_AP_HANDOFF = [
    "enable",  # Enable AP handoff.
    "disable",  # Disable AP handoff.
]
VALID_BODY_DEFAULT_MESH_ROOT = [
    "enable",  # Enable default mesh root SSID if it is not included by radio's SSID configuration.
    "disable",  # Do not enable default mesh root SSID if it is not included by radio's SSID configuration.
]
VALID_BODY_EXT_INFO_ENABLE = [
    "enable",  # Enable station/VAP/radio extension information.
    "disable",  # Disable station/VAP/radio extension information.
]
VALID_BODY_INDOOR_OUTDOOR_DEPLOYMENT = [
    "platform-determined",  # Set AP deployment type based on its platform.
    "outdoor",  # Set AP deployment type to outdoor.
    "indoor",  # Set AP deployment type to indoor.
]
VALID_BODY_CONSOLE_LOGIN = [
    "enable",  # Enable FAP console login access.
    "disable",  # Disable FAP console login access.
]
VALID_BODY_WAN_PORT_AUTH = [
    "none",  # Disable WAN port authentication.
    "802.1x",  # Enable WAN port 802.1x authentication.
]
VALID_BODY_WAN_PORT_AUTH_METHODS = [
    "all",  # Do not specify any EAP methods.
    "EAP-FAST",  # Enable EAP-FAST.
    "EAP-TLS",  # Enable EAP-TLS.
    "EAP-PEAP",  # Enable EAP-PEAP.
]
VALID_BODY_WAN_PORT_AUTH_MACSEC = [
    "enable",  # Enable WAN port 802.1x supplicant MACsec policy.
    "disable",  # Disable WAN port 802.1x supplicant MACsec policy.
]
VALID_BODY_APCFG_AUTO_CERT = [
    "enable",  # Enable AP local auto cert configuration.
    "disable",  # Disable AP local auto cert configuration.
]
VALID_BODY_APCFG_AUTO_CERT_ENROLL_PROTOCOL = [
    "none",  # None (default).
    "est",  # Enrollment over Secure Transport.
    "scep",  # Simple Certificate Enrollment Protocol.
]
VALID_BODY_APCFG_AUTO_CERT_CRYPTO_ALGO = [
    "rsa-1024",  # Cryptography algorithm rsa-1024.
    "rsa-1536",  # Cryptography algorithm rsa-1536.
    "rsa-2048",  # Cryptography algorithm rsa-2048.
    "rsa-4096",  # Cryptography algorithm rsa-4096.
    "ec-secp256r1",  # Cryptography algorithm ec-secp256r1.
    "ec-secp384r1",  # Cryptography algorithm ec-secp384r1.
    "ec-secp521r1",  # Cryptography algorithm ec-secp521r1.
]
VALID_BODY_APCFG_AUTO_CERT_SCEP_KEYTYPE = [
    "rsa",  # Generate a RSA certificate request.
    "ec",  # Generate an elliptic curve certificate request.
]
VALID_BODY_APCFG_AUTO_CERT_SCEP_KEYSIZE = [
    "1024",  # keysize 1024.
    "1536",  # keysize 1536.
    "2048",  # keysize 2048.
    "4096",  # keysize 4096.
]
VALID_BODY_APCFG_AUTO_CERT_SCEP_EC_NAME = [
    "secp256r1",  # Elliptic curve name secp256r1.
    "secp384r1",  # Elliptic curve name secp384r1.
    "secp521r1",  # Elliptic curve name secp521r1.
]
VALID_BODY_UNII_4_5GHZ_BAND = [
    "enable",  # Enable UNII-4 5Ghz band channels.
    "disable",  # Disable UNII-4 5Ghz band channels.
]
VALID_BODY_ADMIN_RESTRICT_LOCAL = [
    "enable",  # Enable local admin authentication restriction.
    "disable",  # Diable local admin authentication restriction.
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
        ...     "control-message-offload": "{'name': 'ebp-frame', 'help': 'Ekahau blink protocol (EBP) frames.', 'label': 'Ebp Frame', 'description': 'Ekahau blink protocol (EBP) frames'}",  # Valid enum value
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
    if "apcfg-auto-cert" in payload:
        value = payload["apcfg-auto-cert"]
        if value not in VALID_BODY_APCFG_AUTO_CERT:
            desc = FIELD_DESCRIPTIONS.get("apcfg-auto-cert", "")
            error_msg = f"Invalid value for 'apcfg-auto-cert': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_APCFG_AUTO_CERT)}"
            error_msg += f"\n  → Example: apcfg-auto-cert='{{ VALID_BODY_APCFG_AUTO_CERT[0] }}'"
            return (False, error_msg)
    if "apcfg-auto-cert-enroll-protocol" in payload:
        value = payload["apcfg-auto-cert-enroll-protocol"]
        if value not in VALID_BODY_APCFG_AUTO_CERT_ENROLL_PROTOCOL:
            desc = FIELD_DESCRIPTIONS.get("apcfg-auto-cert-enroll-protocol", "")
            error_msg = f"Invalid value for 'apcfg-auto-cert-enroll-protocol': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_APCFG_AUTO_CERT_ENROLL_PROTOCOL)}"
            error_msg += f"\n  → Example: apcfg-auto-cert-enroll-protocol='{{ VALID_BODY_APCFG_AUTO_CERT_ENROLL_PROTOCOL[0] }}'"
            return (False, error_msg)
    if "apcfg-auto-cert-crypto-algo" in payload:
        value = payload["apcfg-auto-cert-crypto-algo"]
        if value not in VALID_BODY_APCFG_AUTO_CERT_CRYPTO_ALGO:
            desc = FIELD_DESCRIPTIONS.get("apcfg-auto-cert-crypto-algo", "")
            error_msg = f"Invalid value for 'apcfg-auto-cert-crypto-algo': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_APCFG_AUTO_CERT_CRYPTO_ALGO)}"
            error_msg += f"\n  → Example: apcfg-auto-cert-crypto-algo='{{ VALID_BODY_APCFG_AUTO_CERT_CRYPTO_ALGO[0] }}'"
            return (False, error_msg)
    if "apcfg-auto-cert-scep-keytype" in payload:
        value = payload["apcfg-auto-cert-scep-keytype"]
        if value not in VALID_BODY_APCFG_AUTO_CERT_SCEP_KEYTYPE:
            desc = FIELD_DESCRIPTIONS.get("apcfg-auto-cert-scep-keytype", "")
            error_msg = f"Invalid value for 'apcfg-auto-cert-scep-keytype': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_APCFG_AUTO_CERT_SCEP_KEYTYPE)}"
            error_msg += f"\n  → Example: apcfg-auto-cert-scep-keytype='{{ VALID_BODY_APCFG_AUTO_CERT_SCEP_KEYTYPE[0] }}'"
            return (False, error_msg)
    if "apcfg-auto-cert-scep-keysize" in payload:
        value = payload["apcfg-auto-cert-scep-keysize"]
        if value not in VALID_BODY_APCFG_AUTO_CERT_SCEP_KEYSIZE:
            desc = FIELD_DESCRIPTIONS.get("apcfg-auto-cert-scep-keysize", "")
            error_msg = f"Invalid value for 'apcfg-auto-cert-scep-keysize': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_APCFG_AUTO_CERT_SCEP_KEYSIZE)}"
            error_msg += f"\n  → Example: apcfg-auto-cert-scep-keysize='{{ VALID_BODY_APCFG_AUTO_CERT_SCEP_KEYSIZE[0] }}'"
            return (False, error_msg)
    if "apcfg-auto-cert-scep-ec-name" in payload:
        value = payload["apcfg-auto-cert-scep-ec-name"]
        if value not in VALID_BODY_APCFG_AUTO_CERT_SCEP_EC_NAME:
            desc = FIELD_DESCRIPTIONS.get("apcfg-auto-cert-scep-ec-name", "")
            error_msg = f"Invalid value for 'apcfg-auto-cert-scep-ec-name': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_APCFG_AUTO_CERT_SCEP_EC_NAME)}"
            error_msg += f"\n  → Example: apcfg-auto-cert-scep-ec-name='{{ VALID_BODY_APCFG_AUTO_CERT_SCEP_EC_NAME[0] }}'"
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
    if "apcfg-auto-cert" in payload:
        value = payload["apcfg-auto-cert"]
        if value not in VALID_BODY_APCFG_AUTO_CERT:
            return (
                False,
                f"Invalid value for 'apcfg-auto-cert'='{value}'. Must be one of: {', '.join(VALID_BODY_APCFG_AUTO_CERT)}",
            )
    if "apcfg-auto-cert-enroll-protocol" in payload:
        value = payload["apcfg-auto-cert-enroll-protocol"]
        if value not in VALID_BODY_APCFG_AUTO_CERT_ENROLL_PROTOCOL:
            return (
                False,
                f"Invalid value for 'apcfg-auto-cert-enroll-protocol'='{value}'. Must be one of: {', '.join(VALID_BODY_APCFG_AUTO_CERT_ENROLL_PROTOCOL)}",
            )
    if "apcfg-auto-cert-crypto-algo" in payload:
        value = payload["apcfg-auto-cert-crypto-algo"]
        if value not in VALID_BODY_APCFG_AUTO_CERT_CRYPTO_ALGO:
            return (
                False,
                f"Invalid value for 'apcfg-auto-cert-crypto-algo'='{value}'. Must be one of: {', '.join(VALID_BODY_APCFG_AUTO_CERT_CRYPTO_ALGO)}",
            )
    if "apcfg-auto-cert-scep-keytype" in payload:
        value = payload["apcfg-auto-cert-scep-keytype"]
        if value not in VALID_BODY_APCFG_AUTO_CERT_SCEP_KEYTYPE:
            return (
                False,
                f"Invalid value for 'apcfg-auto-cert-scep-keytype'='{value}'. Must be one of: {', '.join(VALID_BODY_APCFG_AUTO_CERT_SCEP_KEYTYPE)}",
            )
    if "apcfg-auto-cert-scep-keysize" in payload:
        value = payload["apcfg-auto-cert-scep-keysize"]
        if value not in VALID_BODY_APCFG_AUTO_CERT_SCEP_KEYSIZE:
            return (
                False,
                f"Invalid value for 'apcfg-auto-cert-scep-keysize'='{value}'. Must be one of: {', '.join(VALID_BODY_APCFG_AUTO_CERT_SCEP_KEYSIZE)}",
            )
    if "apcfg-auto-cert-scep-ec-name" in payload:
        value = payload["apcfg-auto-cert-scep-ec-name"]
        if value not in VALID_BODY_APCFG_AUTO_CERT_SCEP_EC_NAME:
            return (
                False,
                f"Invalid value for 'apcfg-auto-cert-scep-ec-name'='{value}'. Must be one of: {', '.join(VALID_BODY_APCFG_AUTO_CERT_SCEP_EC_NAME)}",
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
    "endpoint": "wireless_controller/wtp_profile",
    "category": "cmdb",
    "api_path": "wireless-controller/wtp-profile",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure WTP profiles or FortiAP profiles that define radio settings for manageable FortiAP platforms.",
    "total_fields": 78,
    "required_fields_count": 0,
    "fields_with_defaults_count": 62,
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
