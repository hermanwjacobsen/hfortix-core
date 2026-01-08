"""Validation helpers for system/gre_tunnel - Auto-generated"""

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

# Import central validation functions (avoid duplication across 1,062 files)
from hfortix_fortios._helpers.validation import (
    validate_required_fields as _validate_required_fields,
    validate_enum_field as _validate_enum_field,
    validate_query_parameter as _validate_query_parameter,
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
    "name": "",
    "interface": "",
    "ip-version": "4",
    "remote-gw6": "::",
    "local-gw6": "::",
    "remote-gw": "0.0.0.0",
    "local-gw": "0.0.0.0",
    "use-sdwan": "disable",
    "sequence-number-transmission": "disable",
    "sequence-number-reception": "disable",
    "checksum-transmission": "disable",
    "checksum-reception": "disable",
    "key-outbound": 0,
    "key-inbound": 0,
    "dscp-copying": "disable",
    "diffservcode": "",
    "keepalive-interval": 0,
    "keepalive-failtimes": 10,
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
    "name": "string",  # Tunnel name.
    "interface": "string",  # Interface name.
    "ip-version": "option",  # IP version to use for VPN interface.
    "remote-gw6": "ipv6-address",  # IPv6 address of the remote gateway.
    "local-gw6": "ipv6-address",  # IPv6 address of the local gateway.
    "remote-gw": "ipv4-address",  # IP address of the remote gateway.
    "local-gw": "ipv4-address-any",  # IP address of the local gateway.
    "use-sdwan": "option",  # Enable/disable use of SD-WAN to reach remote gateway.
    "sequence-number-transmission": "option",  # Enable/disable including of sequence numbers in transmitted 
    "sequence-number-reception": "option",  # Enable/disable validating sequence numbers in received GRE p
    "checksum-transmission": "option",  # Enable/disable including checksums in transmitted GRE packet
    "checksum-reception": "option",  # Enable/disable validating checksums in received GRE packets.
    "key-outbound": "integer",  # Include this key in transmitted GRE packets (0 - 4294967295)
    "key-inbound": "integer",  # Require received GRE packets contain this key (0 - 429496729
    "dscp-copying": "option",  # Enable/disable DSCP copying.
    "diffservcode": "user",  # DiffServ setting to be applied to GRE tunnel outer IP header
    "keepalive-interval": "integer",  # Keepalive message interval (0 - 32767, 0 = disabled).
    "keepalive-failtimes": "integer",  # Number of consecutive unreturned keepalive messages before a
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Tunnel name.",
    "interface": "Interface name.",
    "ip-version": "IP version to use for VPN interface.",
    "remote-gw6": "IPv6 address of the remote gateway.",
    "local-gw6": "IPv6 address of the local gateway.",
    "remote-gw": "IP address of the remote gateway.",
    "local-gw": "IP address of the local gateway.",
    "use-sdwan": "Enable/disable use of SD-WAN to reach remote gateway.",
    "sequence-number-transmission": "Enable/disable including of sequence numbers in transmitted GRE packets.",
    "sequence-number-reception": "Enable/disable validating sequence numbers in received GRE packets.",
    "checksum-transmission": "Enable/disable including checksums in transmitted GRE packets.",
    "checksum-reception": "Enable/disable validating checksums in received GRE packets.",
    "key-outbound": "Include this key in transmitted GRE packets (0 - 4294967295).",
    "key-inbound": "Require received GRE packets contain this key (0 - 4294967295).",
    "dscp-copying": "Enable/disable DSCP copying.",
    "diffservcode": "DiffServ setting to be applied to GRE tunnel outer IP header.",
    "keepalive-interval": "Keepalive message interval (0 - 32767, 0 = disabled).",
    "keepalive-failtimes": "Number of consecutive unreturned keepalive messages before a GRE connection is considered down (1 - 255).",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 15},
    "interface": {"type": "string", "max_length": 15},
    "key-outbound": {"type": "integer", "min": 0, "max": 4294967295},
    "key-inbound": {"type": "integer", "min": 0, "max": 4294967295},
    "keepalive-interval": {"type": "integer", "min": 0, "max": 32767},
    "keepalive-failtimes": {"type": "integer", "min": 1, "max": 255},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_IP_VERSION = [
    "4",
    "6",
]
VALID_BODY_USE_SDWAN = [
    "disable",
    "enable",
]
VALID_BODY_SEQUENCE_NUMBER_TRANSMISSION = [
    "disable",
    "enable",
]
VALID_BODY_SEQUENCE_NUMBER_RECEPTION = [
    "disable",
    "enable",
]
VALID_BODY_CHECKSUM_TRANSMISSION = [
    "disable",
    "enable",
]
VALID_BODY_CHECKSUM_RECEPTION = [
    "disable",
    "enable",
]
VALID_BODY_DSCP_COPYING = [
    "disable",
    "enable",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_system_gre_tunnel_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for system/gre_tunnel."""
    # Validate query parameters using central function
    if "action" in params:
        is_valid, error = _validate_query_parameter(
            "action",
            params.get("action"),
            VALID_QUERY_ACTION
        )
        if not is_valid:
            return (False, error)

    return (True, None)


# ============================================================================
# POST Validation
# ============================================================================


def validate_system_gre_tunnel_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new system/gre_tunnel object."""
    # Step 1: Validate required fields using central function
    is_valid, error = _validate_required_fields(
        payload,
        REQUIRED_FIELDS,
        FIELD_DESCRIPTIONS
    )
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values using central function
    if "ip-version" in payload:
        is_valid, error = _validate_enum_field(
            "ip-version",
            payload["ip-version"],
            VALID_BODY_IP_VERSION,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "use-sdwan" in payload:
        is_valid, error = _validate_enum_field(
            "use-sdwan",
            payload["use-sdwan"],
            VALID_BODY_USE_SDWAN,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "sequence-number-transmission" in payload:
        is_valid, error = _validate_enum_field(
            "sequence-number-transmission",
            payload["sequence-number-transmission"],
            VALID_BODY_SEQUENCE_NUMBER_TRANSMISSION,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "sequence-number-reception" in payload:
        is_valid, error = _validate_enum_field(
            "sequence-number-reception",
            payload["sequence-number-reception"],
            VALID_BODY_SEQUENCE_NUMBER_RECEPTION,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "checksum-transmission" in payload:
        is_valid, error = _validate_enum_field(
            "checksum-transmission",
            payload["checksum-transmission"],
            VALID_BODY_CHECKSUM_TRANSMISSION,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "checksum-reception" in payload:
        is_valid, error = _validate_enum_field(
            "checksum-reception",
            payload["checksum-reception"],
            VALID_BODY_CHECKSUM_RECEPTION,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "dscp-copying" in payload:
        is_valid, error = _validate_enum_field(
            "dscp-copying",
            payload["dscp-copying"],
            VALID_BODY_DSCP_COPYING,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_system_gre_tunnel_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update system/gre_tunnel."""
    # Validate enum values using central function
    if "ip-version" in payload:
        is_valid, error = _validate_enum_field(
            "ip-version",
            payload["ip-version"],
            VALID_BODY_IP_VERSION,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "use-sdwan" in payload:
        is_valid, error = _validate_enum_field(
            "use-sdwan",
            payload["use-sdwan"],
            VALID_BODY_USE_SDWAN,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "sequence-number-transmission" in payload:
        is_valid, error = _validate_enum_field(
            "sequence-number-transmission",
            payload["sequence-number-transmission"],
            VALID_BODY_SEQUENCE_NUMBER_TRANSMISSION,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "sequence-number-reception" in payload:
        is_valid, error = _validate_enum_field(
            "sequence-number-reception",
            payload["sequence-number-reception"],
            VALID_BODY_SEQUENCE_NUMBER_RECEPTION,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "checksum-transmission" in payload:
        is_valid, error = _validate_enum_field(
            "checksum-transmission",
            payload["checksum-transmission"],
            VALID_BODY_CHECKSUM_TRANSMISSION,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "checksum-reception" in payload:
        is_valid, error = _validate_enum_field(
            "checksum-reception",
            payload["checksum-reception"],
            VALID_BODY_CHECKSUM_RECEPTION,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "dscp-copying" in payload:
        is_valid, error = _validate_enum_field(
            "dscp-copying",
            payload["dscp-copying"],
            VALID_BODY_DSCP_COPYING,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)

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
    "endpoint": "system/gre_tunnel",
    "category": "cmdb",
    "api_path": "system/gre-tunnel",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure GRE tunnel.",
    "total_fields": 18,
    "required_fields_count": 0,
    "fields_with_defaults_count": 18,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
