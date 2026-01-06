"""Validation helpers for router/ospf - Auto-generated"""

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
    "distance-external": 110,
    "distance-inter-area": 110,
    "distance-intra-area": 110,
    "database-overflow": "disable",
    "database-overflow-max-lsas": 10000,
    "database-overflow-time-to-recover": 300,
    "default-information-originate": "disable",
    "default-information-metric": 10,
    "default-information-metric-type": "2",
    "default-information-route-map": "",
    "default-metric": 10,
    "distance": 110,
    "lsa-refresh-interval": 5,
    "rfc1583-compatible": "disable",
    "router-id": "0.0.0.0",
    "spf-timers": "",
    "bfd": "disable",
    "log-neighbour-changes": "enable",
    "distribute-list-in": "",
    "distribute-route-map-in": "",
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
    "distance-external": "integer",  # Administrative external distance.
    "distance-inter-area": "integer",  # Administrative inter-area distance.
    "distance-intra-area": "integer",  # Administrative intra-area distance.
    "database-overflow": "option",  # Enable/disable database overflow.
    "database-overflow-max-lsas": "integer",  # Database overflow maximum LSAs.
    "database-overflow-time-to-recover": "integer",  # Database overflow time to recover (sec).
    "default-information-originate": "option",  # Enable/disable generation of default route.
    "default-information-metric": "integer",  # Default information metric.
    "default-information-metric-type": "option",  # Default information metric type.
    "default-information-route-map": "string",  # Default information route map.
    "default-metric": "integer",  # Default metric of redistribute routes.
    "distance": "integer",  # Distance of the route.
    "lsa-refresh-interval": "integer",  # The minimal OSPF LSA update time interval
    "rfc1583-compatible": "option",  # Enable/disable RFC1583 compatibility.
    "router-id": "ipv4-address-any",  # Router ID.
    "spf-timers": "user",  # SPF calculation frequency.
    "bfd": "option",  # Bidirectional Forwarding Detection (BFD).
    "log-neighbour-changes": "option",  # Log of OSPF neighbor changes.
    "distribute-list-in": "string",  # Filter incoming routes.
    "distribute-route-map-in": "string",  # Filter incoming external routes by route-map.
    "restart-mode": "option",  # OSPF restart mode (graceful or LLS).
    "restart-period": "integer",  # Graceful restart period.
    "restart-on-topology-change": "option",  # Enable/disable continuing graceful restart upon topology cha
    "area": "string",  # OSPF area configuration.
    "ospf-interface": "string",  # OSPF interface configuration.
    "network": "string",  # OSPF network configuration.
    "neighbor": "string",  # OSPF neighbor configuration are used when OSPF runs on non-b
    "passive-interface": "string",  # Passive interface configuration.
    "summary-address": "string",  # IP address summary configuration.
    "distribute-list": "string",  # Distribute list configuration.
    "redistribute": "string",  # Redistribute configuration.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "abr-type": "Area border router type.",
    "auto-cost-ref-bandwidth": "Reference bandwidth in terms of megabits per second.",
    "distance-external": "Administrative external distance.",
    "distance-inter-area": "Administrative inter-area distance.",
    "distance-intra-area": "Administrative intra-area distance.",
    "database-overflow": "Enable/disable database overflow.",
    "database-overflow-max-lsas": "Database overflow maximum LSAs.",
    "database-overflow-time-to-recover": "Database overflow time to recover (sec).",
    "default-information-originate": "Enable/disable generation of default route.",
    "default-information-metric": "Default information metric.",
    "default-information-metric-type": "Default information metric type.",
    "default-information-route-map": "Default information route map.",
    "default-metric": "Default metric of redistribute routes.",
    "distance": "Distance of the route.",
    "lsa-refresh-interval": "The minimal OSPF LSA update time interval",
    "rfc1583-compatible": "Enable/disable RFC1583 compatibility.",
    "router-id": "Router ID.",
    "spf-timers": "SPF calculation frequency.",
    "bfd": "Bidirectional Forwarding Detection (BFD).",
    "log-neighbour-changes": "Log of OSPF neighbor changes.",
    "distribute-list-in": "Filter incoming routes.",
    "distribute-route-map-in": "Filter incoming external routes by route-map.",
    "restart-mode": "OSPF restart mode (graceful or LLS).",
    "restart-period": "Graceful restart period.",
    "restart-on-topology-change": "Enable/disable continuing graceful restart upon topology change.",
    "area": "OSPF area configuration.",
    "ospf-interface": "OSPF interface configuration.",
    "network": "OSPF network configuration.",
    "neighbor": "OSPF neighbor configuration are used when OSPF runs on non-broadcast media.",
    "passive-interface": "Passive interface configuration.",
    "summary-address": "IP address summary configuration.",
    "distribute-list": "Distribute list configuration.",
    "redistribute": "Redistribute configuration.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "auto-cost-ref-bandwidth": {"type": "integer", "min": 1, "max": 1000000},
    "distance-external": {"type": "integer", "min": 1, "max": 255},
    "distance-inter-area": {"type": "integer", "min": 1, "max": 255},
    "distance-intra-area": {"type": "integer", "min": 1, "max": 255},
    "database-overflow-max-lsas": {"type": "integer", "min": 0, "max": 4294967295},
    "database-overflow-time-to-recover": {"type": "integer", "min": 0, "max": 65535},
    "default-information-metric": {"type": "integer", "min": 1, "max": 16777214},
    "default-information-route-map": {"type": "string", "max_length": 35},
    "default-metric": {"type": "integer", "min": 1, "max": 16777214},
    "distance": {"type": "integer", "min": 1, "max": 255},
    "lsa-refresh-interval": {"type": "integer", "min": 0, "max": 5},
    "distribute-list-in": {"type": "string", "max_length": 35},
    "distribute-route-map-in": {"type": "string", "max_length": 35},
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
        "shortcut": {
            "type": "option",
            "help": "Enable/disable shortcut option.",
            "default": "disable",
            "options": [{"help": "Disable shortcut option.", "label": "Disable", "name": "disable"}, {"help": "Enable shortcut option.", "label": "Enable", "name": "enable"}, {"help": "Default shortcut option.", "label": "Default", "name": "default"}],
        },
        "authentication": {
            "type": "option",
            "help": "Authentication type.",
            "default": "none",
            "options": [{"help": "None.", "label": "None", "name": "none"}, {"help": "Text.", "label": "Text", "name": "text"}, {"help": "Message digest.", "label": "Message Digest", "name": "message-digest"}],
        },
        "default-cost": {
            "type": "integer",
            "help": "Summary default cost of stub or NSSA area.",
            "default": 10,
            "min_value": 0,
            "max_value": 4294967295,
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
            "help": "Redistribute, advertise, or do not originate Type-7 default route into NSSA area.",
            "default": "disable",
            "options": [{"help": "Redistribute Type-7 default route from routing table.", "label": "Enable", "name": "enable"}, {"help": "Advertise a self-originated Type-7 default route.", "label": "Always", "name": "always"}, {"help": "Do not advertise Type-7 default route.", "label": "Disable", "name": "disable"}],
        },
        "nssa-default-information-originate-metric": {
            "type": "integer",
            "help": "OSPF default metric.",
            "default": 10,
            "min_value": 0,
            "max_value": 16777214,
        },
        "nssa-default-information-originate-metric-type": {
            "type": "option",
            "help": "OSPF metric type for default routes.",
            "default": "2",
            "options": [{"help": "Type 1.", "label": "1", "name": "1"}, {"help": "Type 2.", "label": "2", "name": "2"}],
        },
        "nssa-redistribution": {
            "type": "option",
            "help": "Enable/disable redistribute into NSSA area.",
            "default": "enable",
            "options": [{"help": "Enable redistribute into NSSA area.", "label": "Enable", "name": "enable"}, {"help": "Disable redistribute into NSSA area.", "label": "Disable", "name": "disable"}],
        },
        "comments": {
            "type": "var-string",
            "help": "Comment.",
            "max_length": 255,
        },
        "range": {
            "type": "string",
            "help": "OSPF area range configuration.",
        },
        "virtual-link": {
            "type": "string",
            "help": "OSPF virtual link configuration.",
        },
        "filter-list": {
            "type": "string",
            "help": "OSPF area filter-list configuration.",
        },
    },
    "ospf-interface": {
        "name": {
            "type": "string",
            "help": "Interface entry name.",
            "default": "",
            "max_length": 35,
        },
        "comments": {
            "type": "var-string",
            "help": "Comment.",
            "max_length": 255,
        },
        "interface": {
            "type": "string",
            "help": "Configuration interface name.",
            "required": True,
            "default": "",
            "max_length": 15,
        },
        "ip": {
            "type": "ipv4-address",
            "help": "IP address.",
            "default": "0.0.0.0",
        },
        "linkdown-fast-failover": {
            "type": "option",
            "help": "Enable/disable fast link failover.",
            "default": "disable",
            "options": [{"help": "Enable fast failover for VLAN interfaces.", "label": "Enable", "name": "enable"}, {"help": "Disable fast failover for VLAN interfaces.", "label": "Disable", "name": "disable"}],
        },
        "authentication": {
            "type": "option",
            "help": "Authentication type.",
            "default": "none",
            "options": [{"help": "None.", "label": "None", "name": "none"}, {"help": "Text.", "label": "Text", "name": "text"}, {"help": "Message digest.", "label": "Message Digest", "name": "message-digest"}],
        },
        "authentication-key": {
            "type": "password",
            "help": "Authentication key.",
            "max_length": 8,
        },
        "keychain": {
            "type": "string",
            "help": "Message-digest key-chain name.",
            "default": "",
            "max_length": 35,
        },
        "prefix-length": {
            "type": "integer",
            "help": "Prefix length.",
            "default": 0,
            "min_value": 0,
            "max_value": 32,
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
            "min_value": 0,
            "max_value": 65535,
        },
        "hello-interval": {
            "type": "integer",
            "help": "Hello interval.",
            "default": 0,
            "min_value": 0,
            "max_value": 65535,
        },
        "hello-multiplier": {
            "type": "integer",
            "help": "Number of hello packets within dead interval.",
            "default": 0,
            "min_value": 3,
            "max_value": 10,
        },
        "database-filter-out": {
            "type": "option",
            "help": "Enable/disable control of flooding out LSAs.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "mtu": {
            "type": "integer",
            "help": "MTU for database description packets.",
            "default": 0,
            "min_value": 576,
            "max_value": 65535,
        },
        "mtu-ignore": {
            "type": "option",
            "help": "Enable/disable ignore MTU.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "network-type": {
            "type": "option",
            "help": "Network type.",
            "default": "broadcast",
            "options": [{"help": "Broadcast.", "label": "Broadcast", "name": "broadcast"}, {"help": "Non-broadcast.", "label": "Non Broadcast", "name": "non-broadcast"}, {"help": "Point-to-point.", "label": "Point To Point", "name": "point-to-point"}, {"help": "Point-to-multipoint.", "label": "Point To Multipoint", "name": "point-to-multipoint"}, {"help": "Point-to-multipoint and non-broadcast.", "label": "Point To Multipoint Non Broadcast", "name": "point-to-multipoint-non-broadcast"}],
        },
        "bfd": {
            "type": "option",
            "help": "Bidirectional Forwarding Detection (BFD).",
            "default": "global",
            "options": [{"help": "Follow global configuration.", "label": "Global", "name": "global"}, {"help": "Enable BFD on this interface.", "label": "Enable", "name": "enable"}, {"help": "Disable BFD on this interface.", "label": "Disable", "name": "disable"}],
        },
        "status": {
            "type": "option",
            "help": "Enable/disable status.",
            "default": "enable",
            "options": [{"help": "Disable status.", "label": "Disable", "name": "disable"}, {"help": "Enable status.", "label": "Enable", "name": "enable"}],
        },
        "resync-timeout": {
            "type": "integer",
            "help": "Graceful restart neighbor resynchronization timeout.",
            "default": 40,
            "min_value": 1,
            "max_value": 3600,
        },
        "md5-keys": {
            "type": "string",
            "help": "MD5 key.",
        },
    },
    "network": {
        "id": {
            "type": "integer",
            "help": "Network entry ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "prefix": {
            "type": "ipv4-classnet",
            "help": "Prefix.",
            "required": True,
            "default": "0.0.0.0 0.0.0.0",
        },
        "area": {
            "type": "ipv4-address-any",
            "help": "Attach the network to area.",
            "required": True,
            "default": "0.0.0.0",
        },
        "comments": {
            "type": "var-string",
            "help": "Comment.",
            "max_length": 255,
        },
    },
    "neighbor": {
        "id": {
            "type": "integer",
            "help": "Neighbor entry ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "ip": {
            "type": "ipv4-address",
            "help": "Interface IP address of the neighbor.",
            "required": True,
            "default": "0.0.0.0",
        },
        "poll-interval": {
            "type": "integer",
            "help": "Poll interval time in seconds.",
            "default": 10,
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
        "prefix": {
            "type": "ipv4-classnet",
            "help": "Prefix.",
            "required": True,
            "default": "0.0.0.0 0.0.0.0",
        },
        "tag": {
            "type": "integer",
            "help": "Tag value.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "advertise": {
            "type": "option",
            "help": "Enable/disable advertise status.",
            "default": "enable",
            "options": [{"help": "Disable advertise status.", "label": "Disable", "name": "disable"}, {"help": "Enable advertise status.", "label": "Enable", "name": "enable"}],
        },
    },
    "distribute-list": {
        "id": {
            "type": "integer",
            "help": "Distribute list entry ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "access-list": {
            "type": "string",
            "help": "Access list name.",
            "required": True,
            "default": "",
            "max_length": 35,
        },
        "protocol": {
            "type": "option",
            "help": "Protocol type.",
            "required": True,
            "default": "connected",
            "options": [{"help": "Connected type.", "label": "Connected", "name": "connected"}, {"help": "Static type.", "label": "Static", "name": "static"}, {"help": "RIP type.", "label": "Rip", "name": "rip"}],
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
    "shortcut",  # Shortcut.
    "standard",  # Standard.
]
VALID_BODY_DATABASE_OVERFLOW = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_DEFAULT_INFORMATION_ORIGINATE = [
    "enable",  # Enable setting.
    "always",  # Always advertise the default router.
    "disable",  # Disable setting.
]
VALID_BODY_DEFAULT_INFORMATION_METRIC_TYPE = [
    "1",  # Type 1.
    "2",  # Type 2.
]
VALID_BODY_RFC1583_COMPATIBLE = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_BFD = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_LOG_NEIGHBOUR_CHANGES = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_RESTART_MODE = [
    "none",  # Hitless restart disabled.
    "lls",  # LLS mode.
    "graceful-restart",  # Graceful Restart Mode.
]
VALID_BODY_RESTART_ON_TOPOLOGY_CHANGE = [
    "enable",  # Continue graceful restart upon topology change.
    "disable",  # Exit graceful restart upon topology change.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_router_ospf_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for router/ospf."""
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
    """Validate required fields for router/ospf."""
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


def validate_router_ospf_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new router/ospf object."""
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
    if "database-overflow" in payload:
        value = payload["database-overflow"]
        if value not in VALID_BODY_DATABASE_OVERFLOW:
            desc = FIELD_DESCRIPTIONS.get("database-overflow", "")
            error_msg = f"Invalid value for 'database-overflow': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DATABASE_OVERFLOW)}"
            error_msg += f"\n  → Example: database-overflow='{{ VALID_BODY_DATABASE_OVERFLOW[0] }}'"
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
    if "rfc1583-compatible" in payload:
        value = payload["rfc1583-compatible"]
        if value not in VALID_BODY_RFC1583_COMPATIBLE:
            desc = FIELD_DESCRIPTIONS.get("rfc1583-compatible", "")
            error_msg = f"Invalid value for 'rfc1583-compatible': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_RFC1583_COMPATIBLE)}"
            error_msg += f"\n  → Example: rfc1583-compatible='{{ VALID_BODY_RFC1583_COMPATIBLE[0] }}'"
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


def validate_router_ospf_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update router/ospf."""
    # Step 1: Validate enum values
    if "abr-type" in payload:
        value = payload["abr-type"]
        if value not in VALID_BODY_ABR_TYPE:
            return (
                False,
                f"Invalid value for 'abr-type'='{value}'. Must be one of: {', '.join(VALID_BODY_ABR_TYPE)}",
            )
    if "database-overflow" in payload:
        value = payload["database-overflow"]
        if value not in VALID_BODY_DATABASE_OVERFLOW:
            return (
                False,
                f"Invalid value for 'database-overflow'='{value}'. Must be one of: {', '.join(VALID_BODY_DATABASE_OVERFLOW)}",
            )
    if "default-information-originate" in payload:
        value = payload["default-information-originate"]
        if value not in VALID_BODY_DEFAULT_INFORMATION_ORIGINATE:
            return (
                False,
                f"Invalid value for 'default-information-originate'='{value}'. Must be one of: {', '.join(VALID_BODY_DEFAULT_INFORMATION_ORIGINATE)}",
            )
    if "default-information-metric-type" in payload:
        value = payload["default-information-metric-type"]
        if value not in VALID_BODY_DEFAULT_INFORMATION_METRIC_TYPE:
            return (
                False,
                f"Invalid value for 'default-information-metric-type'='{value}'. Must be one of: {', '.join(VALID_BODY_DEFAULT_INFORMATION_METRIC_TYPE)}",
            )
    if "rfc1583-compatible" in payload:
        value = payload["rfc1583-compatible"]
        if value not in VALID_BODY_RFC1583_COMPATIBLE:
            return (
                False,
                f"Invalid value for 'rfc1583-compatible'='{value}'. Must be one of: {', '.join(VALID_BODY_RFC1583_COMPATIBLE)}",
            )
    if "bfd" in payload:
        value = payload["bfd"]
        if value not in VALID_BODY_BFD:
            return (
                False,
                f"Invalid value for 'bfd'='{value}'. Must be one of: {', '.join(VALID_BODY_BFD)}",
            )
    if "log-neighbour-changes" in payload:
        value = payload["log-neighbour-changes"]
        if value not in VALID_BODY_LOG_NEIGHBOUR_CHANGES:
            return (
                False,
                f"Invalid value for 'log-neighbour-changes'='{value}'. Must be one of: {', '.join(VALID_BODY_LOG_NEIGHBOUR_CHANGES)}",
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
    "endpoint": "router/ospf",
    "category": "cmdb",
    "api_path": "router/ospf",
    "help": "Configure OSPF.",
    "total_fields": 33,
    "required_fields_count": 0,
    "fields_with_defaults_count": 25,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
