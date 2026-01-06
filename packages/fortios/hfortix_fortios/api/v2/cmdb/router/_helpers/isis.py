"""Validation helpers for router/isis - Auto-generated"""

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
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "is-type": "level-1-2",
    "adv-passive-only": "disable",
    "adv-passive-only6": "disable",
    "auth-mode-l1": "password",
    "auth-mode-l2": "password",
    "auth-keychain-l1": "",
    "auth-keychain-l2": "",
    "auth-sendonly-l1": "disable",
    "auth-sendonly-l2": "disable",
    "ignore-lsp-errors": "disable",
    "lsp-gen-interval-l1": 30,
    "lsp-gen-interval-l2": 30,
    "lsp-refresh-interval": 900,
    "max-lsp-lifetime": 1200,
    "spf-interval-exp-l1": "",
    "spf-interval-exp-l2": "",
    "dynamic-hostname": "disable",
    "adjacency-check": "disable",
    "adjacency-check6": "disable",
    "overload-bit": "disable",
    "overload-bit-suppress": "",
    "overload-bit-on-startup": 0,
    "default-originate": "disable",
    "default-originate6": "disable",
    "metric-style": "narrow",
    "redistribute-l1": "disable",
    "redistribute-l1-list": "",
    "redistribute-l2": "disable",
    "redistribute-l2-list": "",
    "redistribute6-l1": "disable",
    "redistribute6-l1-list": "",
    "redistribute6-l2": "disable",
    "redistribute6-l2-list": "",
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
    "is-type": "option",  # IS type.
    "adv-passive-only": "option",  # Enable/disable IS-IS advertisement of passive interfaces onl
    "adv-passive-only6": "option",  # Enable/disable IPv6 IS-IS advertisement of passive interface
    "auth-mode-l1": "option",  # Level 1 authentication mode.
    "auth-mode-l2": "option",  # Level 2 authentication mode.
    "auth-password-l1": "password",  # Authentication password for level 1 PDUs.
    "auth-password-l2": "password",  # Authentication password for level 2 PDUs.
    "auth-keychain-l1": "string",  # Authentication key-chain for level 1 PDUs.
    "auth-keychain-l2": "string",  # Authentication key-chain for level 2 PDUs.
    "auth-sendonly-l1": "option",  # Enable/disable level 1 authentication send-only.
    "auth-sendonly-l2": "option",  # Enable/disable level 2 authentication send-only.
    "ignore-lsp-errors": "option",  # Enable/disable ignoring of LSP errors with bad checksums.
    "lsp-gen-interval-l1": "integer",  # Minimum interval for level 1 LSP regenerating.
    "lsp-gen-interval-l2": "integer",  # Minimum interval for level 2 LSP regenerating.
    "lsp-refresh-interval": "integer",  # LSP refresh time in seconds.
    "max-lsp-lifetime": "integer",  # Maximum LSP lifetime in seconds.
    "spf-interval-exp-l1": "user",  # Level 1 SPF calculation delay.
    "spf-interval-exp-l2": "user",  # Level 2 SPF calculation delay.
    "dynamic-hostname": "option",  # Enable/disable dynamic hostname.
    "adjacency-check": "option",  # Enable/disable adjacency check.
    "adjacency-check6": "option",  # Enable/disable IPv6 adjacency check.
    "overload-bit": "option",  # Enable/disable signal other routers not to use us in SPF.
    "overload-bit-suppress": "option",  # Suppress overload-bit for the specific prefixes.
    "overload-bit-on-startup": "integer",  # Overload-bit only temporarily after reboot.
    "default-originate": "option",  # Enable/disable distribution of default route information.
    "default-originate6": "option",  # Enable/disable distribution of default IPv6 route informatio
    "metric-style": "option",  # Use old-style (ISO 10589) or new-style packet formats.
    "redistribute-l1": "option",  # Enable/disable redistribution of level 1 routes into level 2
    "redistribute-l1-list": "string",  # Access-list for route redistribution from l1 to l2.
    "redistribute-l2": "option",  # Enable/disable redistribution of level 2 routes into level 1
    "redistribute-l2-list": "string",  # Access-list for route redistribution from l2 to l1.
    "redistribute6-l1": "option",  # Enable/disable redistribution of level 1 IPv6 routes into le
    "redistribute6-l1-list": "string",  # Access-list for IPv6 route redistribution from l1 to l2.
    "redistribute6-l2": "option",  # Enable/disable redistribution of level 2 IPv6 routes into le
    "redistribute6-l2-list": "string",  # Access-list for IPv6 route redistribution from l2 to l1.
    "isis-net": "string",  # IS-IS net configuration.
    "isis-interface": "string",  # IS-IS interface configuration.
    "summary-address": "string",  # IS-IS summary addresses.
    "summary-address6": "string",  # IS-IS IPv6 summary address.
    "redistribute": "string",  # IS-IS redistribute protocols.
    "redistribute6": "string",  # IS-IS IPv6 redistribution for routing protocols.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "is-type": "IS type.",
    "adv-passive-only": "Enable/disable IS-IS advertisement of passive interfaces only.",
    "adv-passive-only6": "Enable/disable IPv6 IS-IS advertisement of passive interfaces only.",
    "auth-mode-l1": "Level 1 authentication mode.",
    "auth-mode-l2": "Level 2 authentication mode.",
    "auth-password-l1": "Authentication password for level 1 PDUs.",
    "auth-password-l2": "Authentication password for level 2 PDUs.",
    "auth-keychain-l1": "Authentication key-chain for level 1 PDUs.",
    "auth-keychain-l2": "Authentication key-chain for level 2 PDUs.",
    "auth-sendonly-l1": "Enable/disable level 1 authentication send-only.",
    "auth-sendonly-l2": "Enable/disable level 2 authentication send-only.",
    "ignore-lsp-errors": "Enable/disable ignoring of LSP errors with bad checksums.",
    "lsp-gen-interval-l1": "Minimum interval for level 1 LSP regenerating.",
    "lsp-gen-interval-l2": "Minimum interval for level 2 LSP regenerating.",
    "lsp-refresh-interval": "LSP refresh time in seconds.",
    "max-lsp-lifetime": "Maximum LSP lifetime in seconds.",
    "spf-interval-exp-l1": "Level 1 SPF calculation delay.",
    "spf-interval-exp-l2": "Level 2 SPF calculation delay.",
    "dynamic-hostname": "Enable/disable dynamic hostname.",
    "adjacency-check": "Enable/disable adjacency check.",
    "adjacency-check6": "Enable/disable IPv6 adjacency check.",
    "overload-bit": "Enable/disable signal other routers not to use us in SPF.",
    "overload-bit-suppress": "Suppress overload-bit for the specific prefixes.",
    "overload-bit-on-startup": "Overload-bit only temporarily after reboot.",
    "default-originate": "Enable/disable distribution of default route information.",
    "default-originate6": "Enable/disable distribution of default IPv6 route information.",
    "metric-style": "Use old-style (ISO 10589) or new-style packet formats.",
    "redistribute-l1": "Enable/disable redistribution of level 1 routes into level 2.",
    "redistribute-l1-list": "Access-list for route redistribution from l1 to l2.",
    "redistribute-l2": "Enable/disable redistribution of level 2 routes into level 1.",
    "redistribute-l2-list": "Access-list for route redistribution from l2 to l1.",
    "redistribute6-l1": "Enable/disable redistribution of level 1 IPv6 routes into level 2.",
    "redistribute6-l1-list": "Access-list for IPv6 route redistribution from l1 to l2.",
    "redistribute6-l2": "Enable/disable redistribution of level 2 IPv6 routes into level 1.",
    "redistribute6-l2-list": "Access-list for IPv6 route redistribution from l2 to l1.",
    "isis-net": "IS-IS net configuration.",
    "isis-interface": "IS-IS interface configuration.",
    "summary-address": "IS-IS summary addresses.",
    "summary-address6": "IS-IS IPv6 summary address.",
    "redistribute": "IS-IS redistribute protocols.",
    "redistribute6": "IS-IS IPv6 redistribution for routing protocols.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "auth-keychain-l1": {"type": "string", "max_length": 35},
    "auth-keychain-l2": {"type": "string", "max_length": 35},
    "lsp-gen-interval-l1": {"type": "integer", "min": 1, "max": 120},
    "lsp-gen-interval-l2": {"type": "integer", "min": 1, "max": 120},
    "lsp-refresh-interval": {"type": "integer", "min": 1, "max": 65535},
    "max-lsp-lifetime": {"type": "integer", "min": 350, "max": 65535},
    "overload-bit-on-startup": {"type": "integer", "min": 5, "max": 86400},
    "redistribute-l1-list": {"type": "string", "max_length": 35},
    "redistribute-l2-list": {"type": "string", "max_length": 35},
    "redistribute6-l1-list": {"type": "string", "max_length": 35},
    "redistribute6-l2-list": {"type": "string", "max_length": 35},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "isis-net": {
        "id": {
            "type": "integer",
            "help": "ISIS network ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "net": {
            "type": "user",
            "help": "IS-IS networks (format = xx.xxxx.  .xxxx.xx.).",
            "default": "",
        },
    },
    "isis-interface": {
        "name": {
            "type": "string",
            "help": "IS-IS interface name.",
            "default": "",
            "max_length": 15,
        },
        "status": {
            "type": "option",
            "help": "Enable/disable interface for IS-IS.",
            "default": "disable",
            "options": [{"help": "Enable interface for IS-IS.", "label": "Enable", "name": "enable"}, {"help": "Disable interface for IS-IS.", "label": "Disable", "name": "disable"}],
        },
        "status6": {
            "type": "option",
            "help": "Enable/disable IPv6 interface for IS-IS.",
            "default": "disable",
            "options": [{"help": "Enable IPv6 interface for IS-IS.", "label": "Enable", "name": "enable"}, {"help": "Disable IPv6 interface for IS-IS.", "label": "Disable", "name": "disable"}],
        },
        "network-type": {
            "type": "option",
            "help": "IS-IS interface's network type.",
            "default": "",
            "options": [{"help": "Broadcast.", "label": "Broadcast", "name": "broadcast"}, {"help": "Point-to-point.", "label": "Point To Point", "name": "point-to-point"}, {"help": "Loopback.", "label": "Loopback", "name": "loopback"}],
        },
        "circuit-type": {
            "type": "option",
            "help": "IS-IS interface's circuit type.",
            "default": "level-1-2",
            "options": [{"help": "Level 1 and 2.", "label": "Level 1 2", "name": "level-1-2"}, {"help": "Level 1.", "label": "Level 1", "name": "level-1"}, {"help": "Level 2.", "label": "Level 2", "name": "level-2"}],
        },
        "csnp-interval-l1": {
            "type": "integer",
            "help": "Level 1 CSNP interval.",
            "default": 10,
            "min_value": 1,
            "max_value": 65535,
        },
        "csnp-interval-l2": {
            "type": "integer",
            "help": "Level 2 CSNP interval.",
            "default": 10,
            "min_value": 1,
            "max_value": 65535,
        },
        "hello-interval-l1": {
            "type": "integer",
            "help": "Level 1 hello interval.",
            "default": 10,
            "min_value": 0,
            "max_value": 65535,
        },
        "hello-interval-l2": {
            "type": "integer",
            "help": "Level 2 hello interval.",
            "default": 10,
            "min_value": 0,
            "max_value": 65535,
        },
        "hello-multiplier-l1": {
            "type": "integer",
            "help": "Level 1 multiplier for Hello holding time.",
            "default": 3,
            "min_value": 2,
            "max_value": 100,
        },
        "hello-multiplier-l2": {
            "type": "integer",
            "help": "Level 2 multiplier for Hello holding time.",
            "default": 3,
            "min_value": 2,
            "max_value": 100,
        },
        "hello-padding": {
            "type": "option",
            "help": "Enable/disable padding to IS-IS hello packets.",
            "default": "enable",
            "options": [{"help": "Enable padding to IS-IS hello packets.", "label": "Enable", "name": "enable"}, {"help": "Disable padding to IS-IS hello packets.", "label": "Disable", "name": "disable"}],
        },
        "lsp-interval": {
            "type": "integer",
            "help": "LSP transmission interval (milliseconds).",
            "default": 33,
            "min_value": 1,
            "max_value": 4294967295,
        },
        "lsp-retransmit-interval": {
            "type": "integer",
            "help": "LSP retransmission interval (sec).",
            "default": 5,
            "min_value": 1,
            "max_value": 65535,
        },
        "metric-l1": {
            "type": "integer",
            "help": "Level 1 metric for interface.",
            "default": 10,
            "min_value": 1,
            "max_value": 63,
        },
        "metric-l2": {
            "type": "integer",
            "help": "Level 2 metric for interface.",
            "default": 10,
            "min_value": 1,
            "max_value": 63,
        },
        "wide-metric-l1": {
            "type": "integer",
            "help": "Level 1 wide metric for interface.",
            "default": 10,
            "min_value": 1,
            "max_value": 16777214,
        },
        "wide-metric-l2": {
            "type": "integer",
            "help": "Level 2 wide metric for interface.",
            "default": 10,
            "min_value": 1,
            "max_value": 16777214,
        },
        "auth-password-l1": {
            "type": "password",
            "help": "Authentication password for level 1 PDUs.",
            "max_length": 128,
        },
        "auth-password-l2": {
            "type": "password",
            "help": "Authentication password for level 2 PDUs.",
            "max_length": 128,
        },
        "auth-keychain-l1": {
            "type": "string",
            "help": "Authentication key-chain for level 1 PDUs.",
            "default": "",
            "max_length": 35,
        },
        "auth-keychain-l2": {
            "type": "string",
            "help": "Authentication key-chain for level 2 PDUs.",
            "default": "",
            "max_length": 35,
        },
        "auth-send-only-l1": {
            "type": "option",
            "help": "Enable/disable authentication send-only for level 1 PDUs.",
            "default": "disable",
            "options": [{"help": "Enable authentication send-only for level 1 PDUs.", "label": "Enable", "name": "enable"}, {"help": "Disable authentication send-only for level 1 PDUs.", "label": "Disable", "name": "disable"}],
        },
        "auth-send-only-l2": {
            "type": "option",
            "help": "Enable/disable authentication send-only for level 2 PDUs.",
            "default": "disable",
            "options": [{"help": "Enable authentication send-only for level 2 PDUs.", "label": "Enable", "name": "enable"}, {"help": "Disable authentication send-only for level 2 PDUs.", "label": "Disable", "name": "disable"}],
        },
        "auth-mode-l1": {
            "type": "option",
            "help": "Level 1 authentication mode.",
            "default": "password",
            "options": [{"help": "MD5.", "label": "Md5", "name": "md5"}, {"help": "Password.", "label": "Password", "name": "password"}],
        },
        "auth-mode-l2": {
            "type": "option",
            "help": "Level 2 authentication mode.",
            "default": "password",
            "options": [{"help": "MD5.", "label": "Md5", "name": "md5"}, {"help": "Password.", "label": "Password", "name": "password"}],
        },
        "priority-l1": {
            "type": "integer",
            "help": "Level 1 priority.",
            "default": 64,
            "min_value": 0,
            "max_value": 127,
        },
        "priority-l2": {
            "type": "integer",
            "help": "Level 2 priority.",
            "default": 64,
            "min_value": 0,
            "max_value": 127,
        },
        "mesh-group": {
            "type": "option",
            "help": "Enable/disable IS-IS mesh group.",
            "default": "disable",
            "options": [{"help": "Enable IS-IS mesh group.", "label": "Enable", "name": "enable"}, {"help": "Disable IS-IS mesh group.", "label": "Disable", "name": "disable"}],
        },
        "mesh-group-id": {
            "type": "integer",
            "help": "Mesh group ID <0-4294967295>, 0: mesh-group blocked.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
    },
    "summary-address": {
        "id": {
            "type": "integer",
            "help": "Summary address entry ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "prefix": {
            "type": "ipv4-classnet-any",
            "help": "Prefix.",
            "required": True,
            "default": "0.0.0.0 0.0.0.0",
        },
        "level": {
            "type": "option",
            "help": "Level.",
            "default": "level-2",
            "options": [{"help": "Level 1 and 2.", "label": "Level 1 2", "name": "level-1-2"}, {"help": "Level 1.", "label": "Level 1", "name": "level-1"}, {"help": "Level 2.", "label": "Level 2", "name": "level-2"}],
        },
    },
    "summary-address6": {
        "id": {
            "type": "integer",
            "help": "Prefix entry ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "prefix6": {
            "type": "ipv6-prefix",
            "help": "IPv6 prefix.",
            "required": True,
            "default": "::/0",
        },
        "level": {
            "type": "option",
            "help": "Level.",
            "default": "level-2",
            "options": [{"help": "Level 1 and 2.", "label": "Level 1 2", "name": "level-1-2"}, {"help": "Level 1.", "label": "Level 1", "name": "level-1"}, {"help": "Level 2.", "label": "Level 2", "name": "level-2"}],
        },
    },
    "redistribute": {
        "protocol": {
            "type": "string",
            "help": "Protocol name.",
            "required": True,
            "default": "",
            "max_length": 35,
        },
        "status": {
            "type": "option",
            "help": "Status.",
            "default": "disable",
            "options": [{"help": "Enable.", "label": "Enable", "name": "enable"}, {"help": "Disable.", "label": "Disable", "name": "disable"}],
        },
        "metric": {
            "type": "integer",
            "help": "Metric.",
            "default": 0,
            "min_value": 0,
            "max_value": 4261412864,
        },
        "metric-type": {
            "type": "option",
            "help": "Metric type.",
            "default": "internal",
            "options": [{"help": "External.", "label": "External", "name": "external"}, {"help": "Internal.", "label": "Internal", "name": "internal"}],
        },
        "level": {
            "type": "option",
            "help": "Level.",
            "default": "level-2",
            "options": [{"help": "Level 1 and 2.", "label": "Level 1 2", "name": "level-1-2"}, {"help": "Level 1.", "label": "Level 1", "name": "level-1"}, {"help": "Level 2.", "label": "Level 2", "name": "level-2"}],
        },
        "routemap": {
            "type": "string",
            "help": "Route map name.",
            "default": "",
            "max_length": 35,
        },
    },
    "redistribute6": {
        "protocol": {
            "type": "string",
            "help": "Protocol name.",
            "required": True,
            "default": "",
            "max_length": 35,
        },
        "status": {
            "type": "option",
            "help": "Enable/disable redistribution.",
            "default": "disable",
            "options": [{"help": "Enable redistribution.", "label": "Enable", "name": "enable"}, {"help": "Disable redistribution.", "label": "Disable", "name": "disable"}],
        },
        "metric": {
            "type": "integer",
            "help": "Metric.",
            "default": 0,
            "min_value": 0,
            "max_value": 4261412864,
        },
        "metric-type": {
            "type": "option",
            "help": "Metric type.",
            "default": "internal",
            "options": [{"help": "External metric type.", "label": "External", "name": "external"}, {"help": "Internal metric type.", "label": "Internal", "name": "internal"}],
        },
        "level": {
            "type": "option",
            "help": "Level.",
            "default": "level-2",
            "options": [{"help": "Level 1 and 2.", "label": "Level 1 2", "name": "level-1-2"}, {"help": "Level 1.", "label": "Level 1", "name": "level-1"}, {"help": "Level 2.", "label": "Level 2", "name": "level-2"}],
        },
        "routemap": {
            "type": "string",
            "help": "Route map name.",
            "default": "",
            "max_length": 35,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_IS_TYPE = [
    "level-1-2",  # Level 1 and 2.
    "level-1",  # Level 1 only.
    "level-2-only",  # Level 2 only.
]
VALID_BODY_ADV_PASSIVE_ONLY = [
    "enable",  # Advertise passive interfaces only.
    "disable",  # Advertise all IS-IS enabled interfaces.
]
VALID_BODY_ADV_PASSIVE_ONLY6 = [
    "enable",  # Advertise passive interfaces only.
    "disable",  # Advertise all IS-IS enabled interfaces.
]
VALID_BODY_AUTH_MODE_L1 = [
    "password",  # Password.
    "md5",  # MD5.
]
VALID_BODY_AUTH_MODE_L2 = [
    "password",  # Password.
    "md5",  # MD5.
]
VALID_BODY_AUTH_SENDONLY_L1 = [
    "enable",  # Enable level 1 authentication send-only.
    "disable",  # Disable level 1 authentication send-only.
]
VALID_BODY_AUTH_SENDONLY_L2 = [
    "enable",  # Enable level 2 authentication send-only.
    "disable",  # Disable level 2 authentication send-only.
]
VALID_BODY_IGNORE_LSP_ERRORS = [
    "enable",  # Enable ignoring of LSP errors with bad checksums.
    "disable",  # Disable ignoring of LSP errors with bad checksums.
]
VALID_BODY_DYNAMIC_HOSTNAME = [
    "enable",  # Enable dynamic hostname.
    "disable",  # Disable dynamic hostname.
]
VALID_BODY_ADJACENCY_CHECK = [
    "enable",  # Enable adjacency check.
    "disable",  # Disable adjacency check.
]
VALID_BODY_ADJACENCY_CHECK6 = [
    "enable",  # Enable IPv6 adjacency check.
    "disable",  # Disable IPv6 adjacency check.
]
VALID_BODY_OVERLOAD_BIT = [
    "enable",  # Enable overload bit.
    "disable",  # Disable overload bit.
]
VALID_BODY_OVERLOAD_BIT_SUPPRESS = [
    "external",  # External.
    "interlevel",  # Inter-level.
]
VALID_BODY_DEFAULT_ORIGINATE = [
    "enable",  # Enable distribution of default route information.
    "disable",  # Disable distribution of default route information.
]
VALID_BODY_DEFAULT_ORIGINATE6 = [
    "enable",  # Enable distribution of default IPv6 route information.
    "disable",  # Disable distribution of default IPv6 route information.
]
VALID_BODY_METRIC_STYLE = [
    "narrow",  # Use old style of TLVs with narrow metric.
    "wide",  # Use new style of TLVs to carry wider metric.
    "transition",  # Send and accept both styles of TLVs during transition.
    "narrow-transition",  # Narrow and accept both styles of TLVs during transition.
    "narrow-transition-l1",  # Narrow-transition level-1 only.
    "narrow-transition-l2",  # Narrow-transition level-2 only.
    "wide-l1",  # Wide level-1 only.
    "wide-l2",  # Wide level-2 only.
    "wide-transition",  # Wide and accept both styles of TLVs during transition.
    "wide-transition-l1",  # Wide-transition level-1 only.
    "wide-transition-l2",  # Wide-transition level-2 only.
    "transition-l1",  # Transition level-1 only.
    "transition-l2",  # Transition level-2 only.
]
VALID_BODY_REDISTRIBUTE_L1 = [
    "enable",  # Enable redistribution of level 1 routes into level 2.
    "disable",  # Disable redistribution of level 1 routes into level 2.
]
VALID_BODY_REDISTRIBUTE_L2 = [
    "enable",  # Enable redistribution of level 2 routes into level 1.
    "disable",  # Disable redistribution of  level 2 routes into level 1.
]
VALID_BODY_REDISTRIBUTE6_L1 = [
    "enable",  # Enable redistribution of level 1 IPv6 routes into level 2.
    "disable",  # Disable redistribution of level 1 IPv6 routes into level 2.
]
VALID_BODY_REDISTRIBUTE6_L2 = [
    "enable",  # Enable redistribution of level 2 IPv6 routes into level 1.
    "disable",  # Disable redistribution of level 2 IPv6 routes into level 1.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_router_isis_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for router/isis."""
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
    """Validate required fields for router/isis."""
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


def validate_router_isis_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new router/isis object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "is-type" in payload:
        value = payload["is-type"]
        if value not in VALID_BODY_IS_TYPE:
            desc = FIELD_DESCRIPTIONS.get("is-type", "")
            error_msg = f"Invalid value for 'is-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IS_TYPE)}"
            error_msg += f"\n  → Example: is-type='{{ VALID_BODY_IS_TYPE[0] }}'"
            return (False, error_msg)
    if "adv-passive-only" in payload:
        value = payload["adv-passive-only"]
        if value not in VALID_BODY_ADV_PASSIVE_ONLY:
            desc = FIELD_DESCRIPTIONS.get("adv-passive-only", "")
            error_msg = f"Invalid value for 'adv-passive-only': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADV_PASSIVE_ONLY)}"
            error_msg += f"\n  → Example: adv-passive-only='{{ VALID_BODY_ADV_PASSIVE_ONLY[0] }}'"
            return (False, error_msg)
    if "adv-passive-only6" in payload:
        value = payload["adv-passive-only6"]
        if value not in VALID_BODY_ADV_PASSIVE_ONLY6:
            desc = FIELD_DESCRIPTIONS.get("adv-passive-only6", "")
            error_msg = f"Invalid value for 'adv-passive-only6': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADV_PASSIVE_ONLY6)}"
            error_msg += f"\n  → Example: adv-passive-only6='{{ VALID_BODY_ADV_PASSIVE_ONLY6[0] }}'"
            return (False, error_msg)
    if "auth-mode-l1" in payload:
        value = payload["auth-mode-l1"]
        if value not in VALID_BODY_AUTH_MODE_L1:
            desc = FIELD_DESCRIPTIONS.get("auth-mode-l1", "")
            error_msg = f"Invalid value for 'auth-mode-l1': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTH_MODE_L1)}"
            error_msg += f"\n  → Example: auth-mode-l1='{{ VALID_BODY_AUTH_MODE_L1[0] }}'"
            return (False, error_msg)
    if "auth-mode-l2" in payload:
        value = payload["auth-mode-l2"]
        if value not in VALID_BODY_AUTH_MODE_L2:
            desc = FIELD_DESCRIPTIONS.get("auth-mode-l2", "")
            error_msg = f"Invalid value for 'auth-mode-l2': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTH_MODE_L2)}"
            error_msg += f"\n  → Example: auth-mode-l2='{{ VALID_BODY_AUTH_MODE_L2[0] }}'"
            return (False, error_msg)
    if "auth-sendonly-l1" in payload:
        value = payload["auth-sendonly-l1"]
        if value not in VALID_BODY_AUTH_SENDONLY_L1:
            desc = FIELD_DESCRIPTIONS.get("auth-sendonly-l1", "")
            error_msg = f"Invalid value for 'auth-sendonly-l1': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTH_SENDONLY_L1)}"
            error_msg += f"\n  → Example: auth-sendonly-l1='{{ VALID_BODY_AUTH_SENDONLY_L1[0] }}'"
            return (False, error_msg)
    if "auth-sendonly-l2" in payload:
        value = payload["auth-sendonly-l2"]
        if value not in VALID_BODY_AUTH_SENDONLY_L2:
            desc = FIELD_DESCRIPTIONS.get("auth-sendonly-l2", "")
            error_msg = f"Invalid value for 'auth-sendonly-l2': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTH_SENDONLY_L2)}"
            error_msg += f"\n  → Example: auth-sendonly-l2='{{ VALID_BODY_AUTH_SENDONLY_L2[0] }}'"
            return (False, error_msg)
    if "ignore-lsp-errors" in payload:
        value = payload["ignore-lsp-errors"]
        if value not in VALID_BODY_IGNORE_LSP_ERRORS:
            desc = FIELD_DESCRIPTIONS.get("ignore-lsp-errors", "")
            error_msg = f"Invalid value for 'ignore-lsp-errors': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IGNORE_LSP_ERRORS)}"
            error_msg += f"\n  → Example: ignore-lsp-errors='{{ VALID_BODY_IGNORE_LSP_ERRORS[0] }}'"
            return (False, error_msg)
    if "dynamic-hostname" in payload:
        value = payload["dynamic-hostname"]
        if value not in VALID_BODY_DYNAMIC_HOSTNAME:
            desc = FIELD_DESCRIPTIONS.get("dynamic-hostname", "")
            error_msg = f"Invalid value for 'dynamic-hostname': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DYNAMIC_HOSTNAME)}"
            error_msg += f"\n  → Example: dynamic-hostname='{{ VALID_BODY_DYNAMIC_HOSTNAME[0] }}'"
            return (False, error_msg)
    if "adjacency-check" in payload:
        value = payload["adjacency-check"]
        if value not in VALID_BODY_ADJACENCY_CHECK:
            desc = FIELD_DESCRIPTIONS.get("adjacency-check", "")
            error_msg = f"Invalid value for 'adjacency-check': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADJACENCY_CHECK)}"
            error_msg += f"\n  → Example: adjacency-check='{{ VALID_BODY_ADJACENCY_CHECK[0] }}'"
            return (False, error_msg)
    if "adjacency-check6" in payload:
        value = payload["adjacency-check6"]
        if value not in VALID_BODY_ADJACENCY_CHECK6:
            desc = FIELD_DESCRIPTIONS.get("adjacency-check6", "")
            error_msg = f"Invalid value for 'adjacency-check6': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADJACENCY_CHECK6)}"
            error_msg += f"\n  → Example: adjacency-check6='{{ VALID_BODY_ADJACENCY_CHECK6[0] }}'"
            return (False, error_msg)
    if "overload-bit" in payload:
        value = payload["overload-bit"]
        if value not in VALID_BODY_OVERLOAD_BIT:
            desc = FIELD_DESCRIPTIONS.get("overload-bit", "")
            error_msg = f"Invalid value for 'overload-bit': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OVERLOAD_BIT)}"
            error_msg += f"\n  → Example: overload-bit='{{ VALID_BODY_OVERLOAD_BIT[0] }}'"
            return (False, error_msg)
    if "overload-bit-suppress" in payload:
        value = payload["overload-bit-suppress"]
        if value not in VALID_BODY_OVERLOAD_BIT_SUPPRESS:
            desc = FIELD_DESCRIPTIONS.get("overload-bit-suppress", "")
            error_msg = f"Invalid value for 'overload-bit-suppress': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OVERLOAD_BIT_SUPPRESS)}"
            error_msg += f"\n  → Example: overload-bit-suppress='{{ VALID_BODY_OVERLOAD_BIT_SUPPRESS[0] }}'"
            return (False, error_msg)
    if "default-originate" in payload:
        value = payload["default-originate"]
        if value not in VALID_BODY_DEFAULT_ORIGINATE:
            desc = FIELD_DESCRIPTIONS.get("default-originate", "")
            error_msg = f"Invalid value for 'default-originate': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DEFAULT_ORIGINATE)}"
            error_msg += f"\n  → Example: default-originate='{{ VALID_BODY_DEFAULT_ORIGINATE[0] }}'"
            return (False, error_msg)
    if "default-originate6" in payload:
        value = payload["default-originate6"]
        if value not in VALID_BODY_DEFAULT_ORIGINATE6:
            desc = FIELD_DESCRIPTIONS.get("default-originate6", "")
            error_msg = f"Invalid value for 'default-originate6': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DEFAULT_ORIGINATE6)}"
            error_msg += f"\n  → Example: default-originate6='{{ VALID_BODY_DEFAULT_ORIGINATE6[0] }}'"
            return (False, error_msg)
    if "metric-style" in payload:
        value = payload["metric-style"]
        if value not in VALID_BODY_METRIC_STYLE:
            desc = FIELD_DESCRIPTIONS.get("metric-style", "")
            error_msg = f"Invalid value for 'metric-style': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_METRIC_STYLE)}"
            error_msg += f"\n  → Example: metric-style='{{ VALID_BODY_METRIC_STYLE[0] }}'"
            return (False, error_msg)
    if "redistribute-l1" in payload:
        value = payload["redistribute-l1"]
        if value not in VALID_BODY_REDISTRIBUTE_L1:
            desc = FIELD_DESCRIPTIONS.get("redistribute-l1", "")
            error_msg = f"Invalid value for 'redistribute-l1': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_REDISTRIBUTE_L1)}"
            error_msg += f"\n  → Example: redistribute-l1='{{ VALID_BODY_REDISTRIBUTE_L1[0] }}'"
            return (False, error_msg)
    if "redistribute-l2" in payload:
        value = payload["redistribute-l2"]
        if value not in VALID_BODY_REDISTRIBUTE_L2:
            desc = FIELD_DESCRIPTIONS.get("redistribute-l2", "")
            error_msg = f"Invalid value for 'redistribute-l2': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_REDISTRIBUTE_L2)}"
            error_msg += f"\n  → Example: redistribute-l2='{{ VALID_BODY_REDISTRIBUTE_L2[0] }}'"
            return (False, error_msg)
    if "redistribute6-l1" in payload:
        value = payload["redistribute6-l1"]
        if value not in VALID_BODY_REDISTRIBUTE6_L1:
            desc = FIELD_DESCRIPTIONS.get("redistribute6-l1", "")
            error_msg = f"Invalid value for 'redistribute6-l1': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_REDISTRIBUTE6_L1)}"
            error_msg += f"\n  → Example: redistribute6-l1='{{ VALID_BODY_REDISTRIBUTE6_L1[0] }}'"
            return (False, error_msg)
    if "redistribute6-l2" in payload:
        value = payload["redistribute6-l2"]
        if value not in VALID_BODY_REDISTRIBUTE6_L2:
            desc = FIELD_DESCRIPTIONS.get("redistribute6-l2", "")
            error_msg = f"Invalid value for 'redistribute6-l2': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_REDISTRIBUTE6_L2)}"
            error_msg += f"\n  → Example: redistribute6-l2='{{ VALID_BODY_REDISTRIBUTE6_L2[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_router_isis_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update router/isis."""
    # Step 1: Validate enum values
    if "is-type" in payload:
        value = payload["is-type"]
        if value not in VALID_BODY_IS_TYPE:
            return (
                False,
                f"Invalid value for 'is-type'='{value}'. Must be one of: {', '.join(VALID_BODY_IS_TYPE)}",
            )
    if "adv-passive-only" in payload:
        value = payload["adv-passive-only"]
        if value not in VALID_BODY_ADV_PASSIVE_ONLY:
            return (
                False,
                f"Invalid value for 'adv-passive-only'='{value}'. Must be one of: {', '.join(VALID_BODY_ADV_PASSIVE_ONLY)}",
            )
    if "adv-passive-only6" in payload:
        value = payload["adv-passive-only6"]
        if value not in VALID_BODY_ADV_PASSIVE_ONLY6:
            return (
                False,
                f"Invalid value for 'adv-passive-only6'='{value}'. Must be one of: {', '.join(VALID_BODY_ADV_PASSIVE_ONLY6)}",
            )
    if "auth-mode-l1" in payload:
        value = payload["auth-mode-l1"]
        if value not in VALID_BODY_AUTH_MODE_L1:
            return (
                False,
                f"Invalid value for 'auth-mode-l1'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_MODE_L1)}",
            )
    if "auth-mode-l2" in payload:
        value = payload["auth-mode-l2"]
        if value not in VALID_BODY_AUTH_MODE_L2:
            return (
                False,
                f"Invalid value for 'auth-mode-l2'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_MODE_L2)}",
            )
    if "auth-sendonly-l1" in payload:
        value = payload["auth-sendonly-l1"]
        if value not in VALID_BODY_AUTH_SENDONLY_L1:
            return (
                False,
                f"Invalid value for 'auth-sendonly-l1'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_SENDONLY_L1)}",
            )
    if "auth-sendonly-l2" in payload:
        value = payload["auth-sendonly-l2"]
        if value not in VALID_BODY_AUTH_SENDONLY_L2:
            return (
                False,
                f"Invalid value for 'auth-sendonly-l2'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_SENDONLY_L2)}",
            )
    if "ignore-lsp-errors" in payload:
        value = payload["ignore-lsp-errors"]
        if value not in VALID_BODY_IGNORE_LSP_ERRORS:
            return (
                False,
                f"Invalid value for 'ignore-lsp-errors'='{value}'. Must be one of: {', '.join(VALID_BODY_IGNORE_LSP_ERRORS)}",
            )
    if "dynamic-hostname" in payload:
        value = payload["dynamic-hostname"]
        if value not in VALID_BODY_DYNAMIC_HOSTNAME:
            return (
                False,
                f"Invalid value for 'dynamic-hostname'='{value}'. Must be one of: {', '.join(VALID_BODY_DYNAMIC_HOSTNAME)}",
            )
    if "adjacency-check" in payload:
        value = payload["adjacency-check"]
        if value not in VALID_BODY_ADJACENCY_CHECK:
            return (
                False,
                f"Invalid value for 'adjacency-check'='{value}'. Must be one of: {', '.join(VALID_BODY_ADJACENCY_CHECK)}",
            )
    if "adjacency-check6" in payload:
        value = payload["adjacency-check6"]
        if value not in VALID_BODY_ADJACENCY_CHECK6:
            return (
                False,
                f"Invalid value for 'adjacency-check6'='{value}'. Must be one of: {', '.join(VALID_BODY_ADJACENCY_CHECK6)}",
            )
    if "overload-bit" in payload:
        value = payload["overload-bit"]
        if value not in VALID_BODY_OVERLOAD_BIT:
            return (
                False,
                f"Invalid value for 'overload-bit'='{value}'. Must be one of: {', '.join(VALID_BODY_OVERLOAD_BIT)}",
            )
    if "overload-bit-suppress" in payload:
        value = payload["overload-bit-suppress"]
        if value not in VALID_BODY_OVERLOAD_BIT_SUPPRESS:
            return (
                False,
                f"Invalid value for 'overload-bit-suppress'='{value}'. Must be one of: {', '.join(VALID_BODY_OVERLOAD_BIT_SUPPRESS)}",
            )
    if "default-originate" in payload:
        value = payload["default-originate"]
        if value not in VALID_BODY_DEFAULT_ORIGINATE:
            return (
                False,
                f"Invalid value for 'default-originate'='{value}'. Must be one of: {', '.join(VALID_BODY_DEFAULT_ORIGINATE)}",
            )
    if "default-originate6" in payload:
        value = payload["default-originate6"]
        if value not in VALID_BODY_DEFAULT_ORIGINATE6:
            return (
                False,
                f"Invalid value for 'default-originate6'='{value}'. Must be one of: {', '.join(VALID_BODY_DEFAULT_ORIGINATE6)}",
            )
    if "metric-style" in payload:
        value = payload["metric-style"]
        if value not in VALID_BODY_METRIC_STYLE:
            return (
                False,
                f"Invalid value for 'metric-style'='{value}'. Must be one of: {', '.join(VALID_BODY_METRIC_STYLE)}",
            )
    if "redistribute-l1" in payload:
        value = payload["redistribute-l1"]
        if value not in VALID_BODY_REDISTRIBUTE_L1:
            return (
                False,
                f"Invalid value for 'redistribute-l1'='{value}'. Must be one of: {', '.join(VALID_BODY_REDISTRIBUTE_L1)}",
            )
    if "redistribute-l2" in payload:
        value = payload["redistribute-l2"]
        if value not in VALID_BODY_REDISTRIBUTE_L2:
            return (
                False,
                f"Invalid value for 'redistribute-l2'='{value}'. Must be one of: {', '.join(VALID_BODY_REDISTRIBUTE_L2)}",
            )
    if "redistribute6-l1" in payload:
        value = payload["redistribute6-l1"]
        if value not in VALID_BODY_REDISTRIBUTE6_L1:
            return (
                False,
                f"Invalid value for 'redistribute6-l1'='{value}'. Must be one of: {', '.join(VALID_BODY_REDISTRIBUTE6_L1)}",
            )
    if "redistribute6-l2" in payload:
        value = payload["redistribute6-l2"]
        if value not in VALID_BODY_REDISTRIBUTE6_L2:
            return (
                False,
                f"Invalid value for 'redistribute6-l2'='{value}'. Must be one of: {', '.join(VALID_BODY_REDISTRIBUTE6_L2)}",
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
    "endpoint": "router/isis",
    "category": "cmdb",
    "api_path": "router/isis",
    "help": "Configure IS-IS.",
    "total_fields": 41,
    "required_fields_count": 0,
    "fields_with_defaults_count": 33,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
