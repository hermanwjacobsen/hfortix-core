"""Validation helpers for wireless_controller/bonjour_profile - Auto-generated"""

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
    "name": "",
    "comment": "",
    "micro-location": "disable",
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
    "name": "string",  # Bonjour profile name.
    "comment": "string",  # Comment.
    "micro-location": "option",  # Enable/disable Micro location for Bonjour profile (default =
    "policy-list": "string",  # Bonjour policy list.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Bonjour profile name.",
    "comment": "Comment.",
    "micro-location": "Enable/disable Micro location for Bonjour profile (default = disable).",
    "policy-list": "Bonjour policy list.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 35},
    "comment": {"type": "string", "max_length": 63},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "policy-list": {
        "policy-id": {
            "type": "integer",
            "help": "Policy ID.",
            "default": 0,
            "min_value": 1,
            "max_value": 65535,
        },
        "description": {
            "type": "string",
            "help": "Description.",
            "default": "",
            "max_length": 63,
        },
        "from-vlan": {
            "type": "string",
            "help": "VLAN ID from which the Bonjour service is advertised (0 - 4094, default = 0).",
            "default": "0",
            "max_length": 63,
        },
        "to-vlan": {
            "type": "string",
            "help": "VLAN ID to which the Bonjour service is made available (0 - 4094, default = all).",
            "default": "all",
            "max_length": 63,
        },
        "services": {
            "type": "option",
            "help": "Bonjour services for the VLAN connecting to the Bonjour network.",
            "default": "all",
            "options": [{"help": "All services.", "label": "All", "name": "all"}, {"help": "AirPlay.", "label": "Airplay", "name": "airplay"}, {"help": "AFP (Apple File Sharing).", "label": "Afp", "name": "afp"}, {"help": "BitTorrent.", "label": "Bit Torrent", "name": "bit-torrent"}, {"help": "FTP.", "label": "Ftp", "name": "ftp"}, {"help": "iChat.", "label": "Ichat", "name": "ichat"}, {"help": "iTunes.", "label": "Itunes", "name": "itunes"}, {"help": "Printers.", "label": "Printers", "name": "printers"}, {"help": "Samba.", "label": "Samba", "name": "samba"}, {"help": "Scanners.", "label": "Scanners", "name": "scanners"}, {"help": "SSH.", "label": "Ssh", "name": "ssh"}, {"help": "ChromeCast.", "label": "Chromecast", "name": "chromecast"}, {"help": "Miracast.", "label": "Miracast", "name": "miracast"}],
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_MICRO_LOCATION = [
    "enable",  # Enable Micro location.
    "disable",  # Disable Micro location.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_wireless_controller_bonjour_profile_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for wireless_controller/bonjour_profile."""
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
    """Validate required fields for wireless_controller/bonjour_profile."""
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


def validate_wireless_controller_bonjour_profile_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new wireless_controller/bonjour_profile object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "micro-location" in payload:
        value = payload["micro-location"]
        if value not in VALID_BODY_MICRO_LOCATION:
            desc = FIELD_DESCRIPTIONS.get("micro-location", "")
            error_msg = f"Invalid value for 'micro-location': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MICRO_LOCATION)}"
            error_msg += f"\n  → Example: micro-location='{{ VALID_BODY_MICRO_LOCATION[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_wireless_controller_bonjour_profile_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update wireless_controller/bonjour_profile."""
    # Step 1: Validate enum values
    if "micro-location" in payload:
        value = payload["micro-location"]
        if value not in VALID_BODY_MICRO_LOCATION:
            return (
                False,
                f"Invalid value for 'micro-location'='{value}'. Must be one of: {', '.join(VALID_BODY_MICRO_LOCATION)}",
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
    "endpoint": "wireless_controller/bonjour_profile",
    "category": "cmdb",
    "api_path": "wireless-controller/bonjour-profile",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure Bonjour profiles. Bonjour is Apple's zero configuration networking protocol. Bonjour profiles allow APs and FortiAPs to connect to networks using Bonjour.",
    "total_fields": 4,
    "required_fields_count": 0,
    "fields_with_defaults_count": 3,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
