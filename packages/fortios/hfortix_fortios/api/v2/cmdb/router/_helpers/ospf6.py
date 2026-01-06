"""Validation helpers for router/ospf6 - Auto-generated"""

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
    "abr-type": "standard",
    "auto-cost-ref-bandwidth": 1000,
    "default-information-originate": "disable",
    "log-neighbour-changes": "enable",
    "default-information-metric": 10,
    "default-information-metric-type": "2",
    "default-information-route-map": "",
    "default-metric": 10,
    "router-id": "0.0.0.0",
    "spf-timers": "",
    "bfd": "disable",
    "restart-mode": "none",
    "restart-period": 120,
    "restart-on-topology-change": "disable",
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
    "abr-type": "option",  # Area border router type.
    "auto-cost-ref-bandwidth": "integer",  # Reference bandwidth in terms of megabits per second.
    "default-information-originate": "option",  # Enable/disable generation of default route.
    "log-neighbour-changes": "option",  # Log OSPFv3 neighbor changes.
    "default-information-metric": "integer",  # Default information metric.
    "default-information-metric-type": "option",  # Default information metric type.
    "default-information-route-map": "string",  # Default information route map.
    "default-metric": "integer",  # Default metric of redistribute routes.
    "router-id": "ipv4-address-any",  # A.B.C.D, in IPv4 address format.
    "spf-timers": "user",  # SPF calculation frequency.
    "bfd": "option",  # Enable/disable Bidirectional Forwarding Detection (BFD).
    "restart-mode": "option",  # OSPFv3 restart mode (graceful or none).
    "restart-period": "integer",  # Graceful restart period in seconds.
    "restart-on-topology-change": "option",  # Enable/disable continuing graceful restart upon topology cha
    "area": "string",  # OSPF6 area configuration.
    "ospf6-interface": "string",  # OSPF6 interface configuration.
    "redistribute": "string",  # Redistribute configuration.
    "passive-interface": "string",  # Passive interface configuration.
    "summary-address": "string",  # IPv6 address summary configuration.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "abr-type": "Area border router type.",
    "auto-cost-ref-bandwidth": "Reference bandwidth in terms of megabits per second.",
    "default-information-originate": "Enable/disable generation of default route.",
    "log-neighbour-changes": "Log OSPFv3 neighbor changes.",
    "default-information-metric": "Default information metric.",
    "default-information-metric-type": "Default information metric type.",
    "default-information-route-map": "Default information route map.",
    "default-metric": "Default metric of redistribute routes.",
    "router-id": "A.B.C.D, in IPv4 address format.",
    "spf-timers": "SPF calculation frequency.",
    "bfd": "Enable/disable Bidirectional Forwarding Detection (BFD).",
    "restart-mode": "OSPFv3 restart mode (graceful or none).",
    "restart-period": "Graceful restart period in seconds.",
    "restart-on-topology-change": "Enable/disable continuing graceful restart upon topology change.",
    "area": "OSPF6 area configuration.",
    "ospf6-interface": "OSPF6 interface configuration.",
    "redistribute": "Redistribute configuration.",
    "passive-interface": "Passive interface configuration.",
    "summary-address": "IPv6 address summary configuration.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "auto-cost-ref-bandwidth": {"type": "integer", "min": 1, "max": 1000000},
    "default-information-metric": {"type": "integer", "min": 1, "max": 16777214},
    "default-information-route-map": {"type": "string", "max_length": 35},
    "default-metric": {"type": "integer", "min": 1, "max": 16777214},
    "restart-period": {"type": "integer", "min": 1, "max": 3600},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "area": {
        "id": {
            "type": "ipv4-address-any",
            "help": "Area entry IP address.",
            "default": "0.0.0.0",
        },
        "default-cost": {
            "type": "integer",
            "help": "Summary default cost of stub or NSSA area.",
            "default": 10,
            "min_value": 0,
            "max_value": 16777215,
        },
        "nssa-translator-role": {
            "type": "option",
            "help": "NSSA translator role type.",
            "default": "candidate",
            "options": [{"help": "Candidate.", "label": "Candidate", "name": "candidate"}, {"help": "Never.", "label": "Never", "name": "never"}, {"help": "Always.", "label": "Always", "name": "always"}],
        },
        "stub-type": {
            "type": "option",
            "help": "Stub summary setting.",
            "default": "summary",
            "options": [{"help": "No summary.", "label": "No Summary", "name": "no-summary"}, {"help": "Summary.", "label": "Summary", "name": "summary"}],
        },
        "type": {
            "type": "option",
            "help": "Area type setting.",
            "default": "regular",
            "options": [{"help": "Regular.", "label": "Regular", "name": "regular"}, {"help": "NSSA.", "label": "Nssa", "name": "nssa"}, {"help": "Stub.", "label": "Stub", "name": "stub"}],
        },
        "nssa-default-information-originate": {
            "type": "option",
            "help": "Enable/disable originate type 7 default into NSSA area.",
            "default": "disable",
            "options": [{"help": "Enable originate type 7 default into NSSA area.", "label": "Enable", "name": "enable"}, {"help": "Disable originate type 7 default into NSSA area.", "label": "Disable", "name": "disable"}],
        },
        "nssa-default-information-originate-metric": {
            "type": "integer",
            "help": "OSPFv3 default metric.",
            "default": 10,
            "min_value": 0,
            "max_value": 16777214,
        },
        "nssa-default-information-originate-metric-type": {
            "type": "option",
            "help": "OSPFv3 metric type for default routes.",
            "default": "2",
            "options": [{"help": "Type 1.", "label": "1", "name": "1"}, {"help": "Type 2.", "label": "2", "name": "2"}],
        },
        "nssa-redistribution": {
            "type": "option",
            "help": "Enable/disable redistribute into NSSA area.",
            "default": "enable",
            "options": [{"help": "Enable redistribute into NSSA area.", "label": "Enable", "name": "enable"}, {"help": "Disable redistribute into NSSA area.", "label": "Disable", "name": "disable"}],
        },
        "authentication": {
            "type": "option",
            "help": "Authentication mode.",
            "default": "none",
            "options": [{"help": "Disable authentication.", "label": "None", "name": "none"}, {"help": "Authentication Header.", "label": "Ah", "name": "ah"}, {"help": "Encapsulating Security Payload.", "label": "Esp", "name": "esp"}],
        },
        "key-rollover-interval": {
            "type": "integer",
            "help": "Key roll-over interval.",
            "default": 300,
            "min_value": 300,
            "max_value": 216000,
        },
        "ipsec-auth-alg": {
            "type": "option",
            "help": "Authentication algorithm.",
            "default": "md5",
            "options": [{"help": "MD5.", "label": "Md5", "name": "md5"}, {"help": "SHA1.", "label": "Sha1", "name": "sha1"}, {"help": "SHA256.", "label": "Sha256", "name": "sha256"}, {"help": "SHA384.", "label": "Sha384", "name": "sha384"}, {"help": "SHA512.", "label": "Sha512", "name": "sha512"}],
        },
        "ipsec-enc-alg": {
            "type": "option",
            "help": "Encryption algorithm.",
            "default": "null",
            "options": [{"help": "No encryption.", "label": "Null", "name": "null"}, {"help": "DES.", "label": "Des", "name": "des"}, {"help": "3DES.", "label": "3Des", "name": "3des"}, {"help": "AES128.", "label": "Aes128", "name": "aes128"}, {"help": "AES192.", "label": "Aes192", "name": "aes192"}, {"help": "AES256.", "label": "Aes256", "name": "aes256"}],
        },
        "ipsec-keys": {
            "type": "string",
            "help": "IPsec authentication and encryption keys.",
        },
        "range": {
            "type": "string",
            "help": "OSPF6 area range configuration.",
        },
        "virtual-link": {
            "type": "string",
            "help": "OSPF6 virtual link configuration.",
        },
    },
    "ospf6-interface": {
        "name": {
            "type": "string",
            "help": "Interface entry name.",
            "default": "",
            "max_length": 35,
        },
        "area-id": {
            "type": "ipv4-address-any",
            "help": "A.B.C.D, in IPv4 address format.",
            "required": True,
            "default": "0.0.0.0",
        },
        "interface": {
            "type": "string",
            "help": "Configuration interface name.",
            "required": True,
            "default": "",
            "max_length": 15,
        },
        "retransmit-interval": {
            "type": "integer",
            "help": "Retransmit interval.",
            "default": 5,
            "min_value": 1,
            "max_value": 65535,
        },
        "transmit-delay": {
            "type": "integer",
            "help": "Transmit delay.",
            "default": 1,
            "min_value": 1,
            "max_value": 65535,
        },
        "cost": {
            "type": "integer",
            "help": "Cost of the interface, value range from 0 to 65535, 0 means auto-cost.",
            "default": 0,
            "min_value": 0,
            "max_value": 65535,
        },
        "priority": {
            "type": "integer",
            "help": "Priority.",
            "default": 1,
            "min_value": 0,
            "max_value": 255,
        },
        "dead-interval": {
            "type": "integer",
            "help": "Dead interval.",
            "default": 0,
            "min_value": 1,
            "max_value": 65535,
        },
        "hello-interval": {
            "type": "integer",
            "help": "Hello interval.",
            "default": 0,
            "min_value": 1,
            "max_value": 65535,
        },
        "status": {
            "type": "option",
            "help": "Enable/disable OSPF6 routing on this interface.",
            "default": "enable",
            "options": [{"help": "Disable OSPF6 routing.", "label": "Disable", "name": "disable"}, {"help": "Enable OSPF6 routing.", "label": "Enable", "name": "enable"}],
        },
        "network-type": {
            "type": "option",
            "help": "Network type.",
            "default": "broadcast",
            "options": [{"help": "broadcast", "label": "Broadcast", "name": "broadcast"}, {"help": "point-to-point", "label": "Point To Point", "name": "point-to-point"}, {"help": "non-broadcast", "label": "Non Broadcast", "name": "non-broadcast"}, {"help": "point-to-multipoint", "label": "Point To Multipoint", "name": "point-to-multipoint"}, {"help": "point-to-multipoint and non-broadcast.", "label": "Point To Multipoint Non Broadcast", "name": "point-to-multipoint-non-broadcast"}],
        },
        "bfd": {
            "type": "option",
            "help": "Enable/disable Bidirectional Forwarding Detection (BFD).",
            "default": "global",
            "options": [{"help": "Use global configuration of Bidirectional Forwarding Detection (BFD).", "label": "Global", "name": "global"}, {"help": "Enable Bidirectional Forwarding Detection (BFD) on this interface.", "label": "Enable", "name": "enable"}, {"help": "Disable Bidirectional Forwarding Detection (BFD) on this interface.", "label": "Disable", "name": "disable"}],
        },
        "mtu": {
            "type": "integer",
            "help": "MTU for OSPFv3 packets.",
            "default": 0,
            "min_value": 576,
            "max_value": 65535,
        },
        "mtu-ignore": {
            "type": "option",
            "help": "Enable/disable ignoring MTU field in DBD packets.",
            "default": "disable",
            "options": [{"help": "Ignore MTU field in DBD packets.", "label": "Enable", "name": "enable"}, {"help": "Do not ignore MTU field in DBD packets.", "label": "Disable", "name": "disable"}],
        },
        "authentication": {
            "type": "option",
            "help": "Authentication mode.",
            "default": "area",
            "options": [{"help": "Disable authentication.", "label": "None", "name": "none"}, {"help": "Authentication Header.", "label": "Ah", "name": "ah"}, {"help": "Encapsulating Security Payload.", "label": "Esp", "name": "esp"}, {"help": "Use the routing area\u0027s authentication configuration.", "label": "Area", "name": "area"}],
        },
        "key-rollover-interval": {
            "type": "integer",
            "help": "Key roll-over interval.",
            "default": 300,
            "min_value": 300,
            "max_value": 216000,
        },
        "ipsec-auth-alg": {
            "type": "option",
            "help": "Authentication algorithm.",
            "default": "md5",
            "options": [{"help": "MD5.", "label": "Md5", "name": "md5"}, {"help": "SHA1.", "label": "Sha1", "name": "sha1"}, {"help": "SHA256.", "label": "Sha256", "name": "sha256"}, {"help": "SHA384.", "label": "Sha384", "name": "sha384"}, {"help": "SHA512.", "label": "Sha512", "name": "sha512"}],
        },
        "ipsec-enc-alg": {
            "type": "option",
            "help": "Encryption algorithm.",
            "default": "null",
            "options": [{"help": "No encryption.", "label": "Null", "name": "null"}, {"help": "DES.", "label": "Des", "name": "des"}, {"help": "3DES.", "label": "3Des", "name": "3des"}, {"help": "AES128.", "label": "Aes128", "name": "aes128"}, {"help": "AES192.", "label": "Aes192", "name": "aes192"}, {"help": "AES256.", "label": "Aes256", "name": "aes256"}],
        },
        "ipsec-keys": {
            "type": "string",
            "help": "IPsec authentication and encryption keys.",
        },
        "neighbor": {
            "type": "string",
            "help": "OSPFv3 neighbors are used when OSPFv3 runs on non-broadcast media.",
        },
    },
    "redistribute": {
        "name": {
            "type": "string",
            "help": "Redistribute name.",
            "required": True,
            "default": "",
            "max_length": 35,
        },
        "status": {
            "type": "option",
            "help": "Status.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "metric": {
            "type": "integer",
            "help": "Redistribute metric setting.",
            "default": 0,
            "min_value": 0,
            "max_value": 16777214,
        },
        "routemap": {
            "type": "string",
            "help": "Route map name.",
            "default": "",
            "max_length": 35,
        },
        "metric-type": {
            "type": "option",
            "help": "Metric type.",
            "default": "2",
            "options": [{"help": "Type 1.", "label": "1", "name": "1"}, {"help": "Type 2.", "label": "2", "name": "2"}],
        },
    },
    "passive-interface": {
        "name": {
            "type": "string",
            "help": "Passive interface name.",
            "required": True,
            "default": "",
            "max_length": 79,
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
        "prefix6": {
            "type": "ipv6-network",
            "help": "IPv6 prefix.",
            "required": True,
            "default": "::/0",
        },
        "advertise": {
            "type": "option",
            "help": "Enable/disable advertise status.",
            "default": "enable",
            "options": [{"help": "disable", "label": "Disable", "name": "disable"}, {"help": "enable", "label": "Enable", "name": "enable"}],
        },
        "tag": {
            "type": "integer",
            "help": "Tag value.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_ABR_TYPE = [
    "cisco",  # Cisco.
    "ibm",  # IBM.
    "standard",  # Standard.
]
VALID_BODY_DEFAULT_INFORMATION_ORIGINATE = [
    "enable",  # Enable setting.
    "always",  # Always advertise the default router.
    "disable",  # Disable setting.
]
VALID_BODY_LOG_NEIGHBOUR_CHANGES = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_DEFAULT_INFORMATION_METRIC_TYPE = [
    "1",  # Type 1.
    "2",  # Type 2.
]
VALID_BODY_BFD = [
    "enable",  # Enable Bidirectional Forwarding Detection (BFD).
    "disable",  # Disable Bidirectional Forwarding Detection (BFD).
]
VALID_BODY_RESTART_MODE = [
    "none",  # Disable hitless restart.
    "graceful-restart",  # Enable graceful restart mode.
]
VALID_BODY_RESTART_ON_TOPOLOGY_CHANGE = [
    "enable",  # Continue graceful restart upon topology change.
    "disable",  # Exit graceful restart upon topology change.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_router_ospf6_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for router/ospf6."""
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
    """Validate required fields for router/ospf6."""
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


def validate_router_ospf6_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new router/ospf6 object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "abr-type" in payload:
        value = payload["abr-type"]
        if value not in VALID_BODY_ABR_TYPE:
            desc = FIELD_DESCRIPTIONS.get("abr-type", "")
            error_msg = f"Invalid value for 'abr-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ABR_TYPE)}"
            error_msg += f"\n  → Example: abr-type='{{ VALID_BODY_ABR_TYPE[0] }}'"
            return (False, error_msg)
    if "default-information-originate" in payload:
        value = payload["default-information-originate"]
        if value not in VALID_BODY_DEFAULT_INFORMATION_ORIGINATE:
            desc = FIELD_DESCRIPTIONS.get("default-information-originate", "")
            error_msg = f"Invalid value for 'default-information-originate': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DEFAULT_INFORMATION_ORIGINATE)}"
            error_msg += f"\n  → Example: default-information-originate='{{ VALID_BODY_DEFAULT_INFORMATION_ORIGINATE[0] }}'"
            return (False, error_msg)
    if "log-neighbour-changes" in payload:
        value = payload["log-neighbour-changes"]
        if value not in VALID_BODY_LOG_NEIGHBOUR_CHANGES:
            desc = FIELD_DESCRIPTIONS.get("log-neighbour-changes", "")
            error_msg = f"Invalid value for 'log-neighbour-changes': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOG_NEIGHBOUR_CHANGES)}"
            error_msg += f"\n  → Example: log-neighbour-changes='{{ VALID_BODY_LOG_NEIGHBOUR_CHANGES[0] }}'"
            return (False, error_msg)
    if "default-information-metric-type" in payload:
        value = payload["default-information-metric-type"]
        if value not in VALID_BODY_DEFAULT_INFORMATION_METRIC_TYPE:
            desc = FIELD_DESCRIPTIONS.get("default-information-metric-type", "")
            error_msg = f"Invalid value for 'default-information-metric-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DEFAULT_INFORMATION_METRIC_TYPE)}"
            error_msg += f"\n  → Example: default-information-metric-type='{{ VALID_BODY_DEFAULT_INFORMATION_METRIC_TYPE[0] }}'"
            return (False, error_msg)
    if "bfd" in payload:
        value = payload["bfd"]
        if value not in VALID_BODY_BFD:
            desc = FIELD_DESCRIPTIONS.get("bfd", "")
            error_msg = f"Invalid value for 'bfd': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_BFD)}"
            error_msg += f"\n  → Example: bfd='{{ VALID_BODY_BFD[0] }}'"
            return (False, error_msg)
    if "restart-mode" in payload:
        value = payload["restart-mode"]
        if value not in VALID_BODY_RESTART_MODE:
            desc = FIELD_DESCRIPTIONS.get("restart-mode", "")
            error_msg = f"Invalid value for 'restart-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_RESTART_MODE)}"
            error_msg += f"\n  → Example: restart-mode='{{ VALID_BODY_RESTART_MODE[0] }}'"
            return (False, error_msg)
    if "restart-on-topology-change" in payload:
        value = payload["restart-on-topology-change"]
        if value not in VALID_BODY_RESTART_ON_TOPOLOGY_CHANGE:
            desc = FIELD_DESCRIPTIONS.get("restart-on-topology-change", "")
            error_msg = f"Invalid value for 'restart-on-topology-change': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_RESTART_ON_TOPOLOGY_CHANGE)}"
            error_msg += f"\n  → Example: restart-on-topology-change='{{ VALID_BODY_RESTART_ON_TOPOLOGY_CHANGE[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_router_ospf6_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update router/ospf6."""
    # Step 1: Validate enum values
    if "abr-type" in payload:
        value = payload["abr-type"]
        if value not in VALID_BODY_ABR_TYPE:
            return (
                False,
                f"Invalid value for 'abr-type'='{value}'. Must be one of: {', '.join(VALID_BODY_ABR_TYPE)}",
            )
    if "default-information-originate" in payload:
        value = payload["default-information-originate"]
        if value not in VALID_BODY_DEFAULT_INFORMATION_ORIGINATE:
            return (
                False,
                f"Invalid value for 'default-information-originate'='{value}'. Must be one of: {', '.join(VALID_BODY_DEFAULT_INFORMATION_ORIGINATE)}",
            )
    if "log-neighbour-changes" in payload:
        value = payload["log-neighbour-changes"]
        if value not in VALID_BODY_LOG_NEIGHBOUR_CHANGES:
            return (
                False,
                f"Invalid value for 'log-neighbour-changes'='{value}'. Must be one of: {', '.join(VALID_BODY_LOG_NEIGHBOUR_CHANGES)}",
            )
    if "default-information-metric-type" in payload:
        value = payload["default-information-metric-type"]
        if value not in VALID_BODY_DEFAULT_INFORMATION_METRIC_TYPE:
            return (
                False,
                f"Invalid value for 'default-information-metric-type'='{value}'. Must be one of: {', '.join(VALID_BODY_DEFAULT_INFORMATION_METRIC_TYPE)}",
            )
    if "bfd" in payload:
        value = payload["bfd"]
        if value not in VALID_BODY_BFD:
            return (
                False,
                f"Invalid value for 'bfd'='{value}'. Must be one of: {', '.join(VALID_BODY_BFD)}",
            )
    if "restart-mode" in payload:
        value = payload["restart-mode"]
        if value not in VALID_BODY_RESTART_MODE:
            return (
                False,
                f"Invalid value for 'restart-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_RESTART_MODE)}",
            )
    if "restart-on-topology-change" in payload:
        value = payload["restart-on-topology-change"]
        if value not in VALID_BODY_RESTART_ON_TOPOLOGY_CHANGE:
            return (
                False,
                f"Invalid value for 'restart-on-topology-change'='{value}'. Must be one of: {', '.join(VALID_BODY_RESTART_ON_TOPOLOGY_CHANGE)}",
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
    "endpoint": "router/ospf6",
    "category": "cmdb",
    "api_path": "router/ospf6",
    "help": "Configure IPv6 OSPF.",
    "total_fields": 19,
    "required_fields_count": 0,
    "fields_with_defaults_count": 14,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
