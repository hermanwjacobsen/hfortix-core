"""Validation helpers for system/standalone_cluster - Auto-generated"""

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
    "psksecret",  # Pre-shared secret for session synchronization (ASCII string or hexadecimal encoded with a leading 0x).
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "standalone-group-id": 0,
    "group-member-id": 0,
    "layer2-connection": "unavailable",
    "session-sync-dev": "",
    "encryption": "disable",
    "asymmetric-traffic-control": "cps-preferred",
    "helper-traffic-bounce": "enable",
    "utm-traffic-bounce": "enable",
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
    "standalone-group-id": "integer",  # Cluster group ID (0 - 255). Must be the same for all members
    "group-member-id": "integer",  # Cluster member ID (0 - 15).
    "layer2-connection": "option",  # Indicate whether layer 2 connections are present among FGSP 
    "session-sync-dev": "user",  # Offload session-sync process to kernel and sync sessions usi
    "encryption": "option",  # Enable/disable encryption when synchronizing sessions.
    "psksecret": "password-3",  # Pre-shared secret for session synchronization (ASCII string 
    "asymmetric-traffic-control": "option",  # Asymmetric traffic control mode.
    "cluster-peer": "string",  # Configure FortiGate Session Life Support Protocol (FGSP) ses
    "monitor-interface": "string",  # Configure a list of interfaces on which to monitor itself. M
    "pingsvr-monitor-interface": "string",  # List of pingsvr monitor interface to check for remote IP mon
    "monitor-prefix": "string",  # Configure a list of routing prefixes to monitor.
    "helper-traffic-bounce": "option",  # Enable/disable helper related traffic bounce.
    "utm-traffic-bounce": "option",  # Enable/disable UTM related traffic bounce.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "standalone-group-id": "Cluster group ID (0 - 255). Must be the same for all members.",
    "group-member-id": "Cluster member ID (0 - 15).",
    "layer2-connection": "Indicate whether layer 2 connections are present among FGSP members.",
    "session-sync-dev": "Offload session-sync process to kernel and sync sessions using connected interface(s) directly.",
    "encryption": "Enable/disable encryption when synchronizing sessions.",
    "psksecret": "Pre-shared secret for session synchronization (ASCII string or hexadecimal encoded with a leading 0x).",
    "asymmetric-traffic-control": "Asymmetric traffic control mode.",
    "cluster-peer": "Configure FortiGate Session Life Support Protocol (FGSP) session synchronization.",
    "monitor-interface": "Configure a list of interfaces on which to monitor itself. Monitoring is performed on the status of the interface.",
    "pingsvr-monitor-interface": "List of pingsvr monitor interface to check for remote IP monitoring.",
    "monitor-prefix": "Configure a list of routing prefixes to monitor.",
    "helper-traffic-bounce": "Enable/disable helper related traffic bounce.",
    "utm-traffic-bounce": "Enable/disable UTM related traffic bounce.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "standalone-group-id": {"type": "integer", "min": 0, "max": 255},
    "group-member-id": {"type": "integer", "min": 0, "max": 15},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "cluster-peer": {
        "sync-id": {
            "type": "integer",
            "help": "Sync ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "peervd": {
            "type": "string",
            "help": "VDOM that contains the session synchronization link interface on the peer unit. Usually both peers would have the same peervd.",
            "default": "root",
            "max_length": 31,
        },
        "peerip": {
            "type": "ipv4-address",
            "help": "IP address of the interface on the peer unit that is used for the session synchronization link.",
            "default": "0.0.0.0",
        },
        "syncvd": {
            "type": "string",
            "help": "Sessions from these VDOMs are synchronized using this session synchronization configuration.",
        },
        "down-intfs-before-sess-sync": {
            "type": "string",
            "help": "List of interfaces to be turned down before session synchronization is complete.",
        },
        "hb-interval": {
            "type": "integer",
            "help": "Heartbeat interval (1 - 20 (100*ms). Increase to reduce false positives.",
            "default": 2,
            "min_value": 1,
            "max_value": 20,
        },
        "hb-lost-threshold": {
            "type": "integer",
            "help": "Lost heartbeat threshold (1 - 60). Increase to reduce false positives.",
            "default": 10,
            "min_value": 1,
            "max_value": 60,
        },
        "ipsec-tunnel-sync": {
            "type": "option",
            "help": "Enable/disable IPsec tunnel synchronization.",
            "default": "enable",
            "options": [{"help": "Enable IPsec tunnel synchronization.", "label": "Enable", "name": "enable"}, {"help": "Disable IPsec tunnel synchronization.", "label": "Disable", "name": "disable"}],
        },
        "secondary-add-ipsec-routes": {
            "type": "option",
            "help": "Enable/disable IKE route announcement on the backup unit.",
            "default": "enable",
            "options": [{"help": "Add IKE routes to the backup unit.", "label": "Enable", "name": "enable"}, {"help": "Do not add IKE routes to the backup unit.", "label": "Disable", "name": "disable"}],
        },
        "session-sync-filter": {
            "type": "string",
            "help": "Add one or more filters if you only want to synchronize some sessions. Use the filter to configure the types of sessions to synchronize.",
        },
    },
    "monitor-interface": {
        "name": {
            "type": "string",
            "help": "Interface name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "pingsvr-monitor-interface": {
        "name": {
            "type": "string",
            "help": "Interface name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "monitor-prefix": {
        "id": {
            "type": "integer",
            "help": "ID.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "vdom": {
            "type": "string",
            "help": "VDOM name.",
            "required": True,
            "default": "",
            "max_length": 31,
        },
        "vrf": {
            "type": "integer",
            "help": "VRF ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 511,
        },
        "prefix": {
            "type": "ipv4-classnet-any",
            "help": "Prefix.",
            "default": "0.0.0.0 0.0.0.0",
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_LAYER2_CONNECTION = [
    "available",  # There exist layer 2 connections among FGSP members.
    "unavailable",  # There does not exist layer 2 connection among FGSP members.
]
VALID_BODY_ENCRYPTION = [
    "enable",  # Enable encryption when synchronizing sessions.
    "disable",  # Disable encryption when synchronizing sessions.
]
VALID_BODY_ASYMMETRIC_TRAFFIC_CONTROL = [
    "cps-preferred",  # Connection per second (CPS) preferred.
    "strict-anti-replay",  # Strict anti-replay check.
]
VALID_BODY_HELPER_TRAFFIC_BOUNCE = [
    "enable",  # Enable helper related traffic bounce.
    "disable",  # Disable helper related traffic bounce.
]
VALID_BODY_UTM_TRAFFIC_BOUNCE = [
    "enable",  # Enable UTM related traffic bounce.
    "disable",  # Disable UTM related traffic bounce.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_system_standalone_cluster_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for system/standalone_cluster."""
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
    """Validate required fields for system/standalone_cluster."""
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


def validate_system_standalone_cluster_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new system/standalone_cluster object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "layer2-connection" in payload:
        value = payload["layer2-connection"]
        if value not in VALID_BODY_LAYER2_CONNECTION:
            desc = FIELD_DESCRIPTIONS.get("layer2-connection", "")
            error_msg = f"Invalid value for 'layer2-connection': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LAYER2_CONNECTION)}"
            error_msg += f"\n  → Example: layer2-connection='{{ VALID_BODY_LAYER2_CONNECTION[0] }}'"
            return (False, error_msg)
    if "encryption" in payload:
        value = payload["encryption"]
        if value not in VALID_BODY_ENCRYPTION:
            desc = FIELD_DESCRIPTIONS.get("encryption", "")
            error_msg = f"Invalid value for 'encryption': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ENCRYPTION)}"
            error_msg += f"\n  → Example: encryption='{{ VALID_BODY_ENCRYPTION[0] }}'"
            return (False, error_msg)
    if "asymmetric-traffic-control" in payload:
        value = payload["asymmetric-traffic-control"]
        if value not in VALID_BODY_ASYMMETRIC_TRAFFIC_CONTROL:
            desc = FIELD_DESCRIPTIONS.get("asymmetric-traffic-control", "")
            error_msg = f"Invalid value for 'asymmetric-traffic-control': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ASYMMETRIC_TRAFFIC_CONTROL)}"
            error_msg += f"\n  → Example: asymmetric-traffic-control='{{ VALID_BODY_ASYMMETRIC_TRAFFIC_CONTROL[0] }}'"
            return (False, error_msg)
    if "helper-traffic-bounce" in payload:
        value = payload["helper-traffic-bounce"]
        if value not in VALID_BODY_HELPER_TRAFFIC_BOUNCE:
            desc = FIELD_DESCRIPTIONS.get("helper-traffic-bounce", "")
            error_msg = f"Invalid value for 'helper-traffic-bounce': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_HELPER_TRAFFIC_BOUNCE)}"
            error_msg += f"\n  → Example: helper-traffic-bounce='{{ VALID_BODY_HELPER_TRAFFIC_BOUNCE[0] }}'"
            return (False, error_msg)
    if "utm-traffic-bounce" in payload:
        value = payload["utm-traffic-bounce"]
        if value not in VALID_BODY_UTM_TRAFFIC_BOUNCE:
            desc = FIELD_DESCRIPTIONS.get("utm-traffic-bounce", "")
            error_msg = f"Invalid value for 'utm-traffic-bounce': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_UTM_TRAFFIC_BOUNCE)}"
            error_msg += f"\n  → Example: utm-traffic-bounce='{{ VALID_BODY_UTM_TRAFFIC_BOUNCE[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_system_standalone_cluster_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update system/standalone_cluster."""
    # Step 1: Validate enum values
    if "layer2-connection" in payload:
        value = payload["layer2-connection"]
        if value not in VALID_BODY_LAYER2_CONNECTION:
            return (
                False,
                f"Invalid value for 'layer2-connection'='{value}'. Must be one of: {', '.join(VALID_BODY_LAYER2_CONNECTION)}",
            )
    if "encryption" in payload:
        value = payload["encryption"]
        if value not in VALID_BODY_ENCRYPTION:
            return (
                False,
                f"Invalid value for 'encryption'='{value}'. Must be one of: {', '.join(VALID_BODY_ENCRYPTION)}",
            )
    if "asymmetric-traffic-control" in payload:
        value = payload["asymmetric-traffic-control"]
        if value not in VALID_BODY_ASYMMETRIC_TRAFFIC_CONTROL:
            return (
                False,
                f"Invalid value for 'asymmetric-traffic-control'='{value}'. Must be one of: {', '.join(VALID_BODY_ASYMMETRIC_TRAFFIC_CONTROL)}",
            )
    if "helper-traffic-bounce" in payload:
        value = payload["helper-traffic-bounce"]
        if value not in VALID_BODY_HELPER_TRAFFIC_BOUNCE:
            return (
                False,
                f"Invalid value for 'helper-traffic-bounce'='{value}'. Must be one of: {', '.join(VALID_BODY_HELPER_TRAFFIC_BOUNCE)}",
            )
    if "utm-traffic-bounce" in payload:
        value = payload["utm-traffic-bounce"]
        if value not in VALID_BODY_UTM_TRAFFIC_BOUNCE:
            return (
                False,
                f"Invalid value for 'utm-traffic-bounce'='{value}'. Must be one of: {', '.join(VALID_BODY_UTM_TRAFFIC_BOUNCE)}",
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
    "endpoint": "system/standalone_cluster",
    "category": "cmdb",
    "api_path": "system/standalone-cluster",
    "help": "Configure FortiGate Session Life Support Protocol (FGSP) cluster attributes.",
    "total_fields": 13,
    "required_fields_count": 1,
    "fields_with_defaults_count": 8,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
