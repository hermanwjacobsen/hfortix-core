"""Validation helpers for wireless_controller/snmp - Auto-generated"""

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
    "engine-id": "",
    "contact-info": "",
    "trap-high-cpu-threshold": 80,
    "trap-high-mem-threshold": 80,
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
    "engine-id": "string",  # AC SNMP engineID string (maximum 24 characters).
    "contact-info": "string",  # Contact Information.
    "trap-high-cpu-threshold": "integer",  # CPU usage when trap is sent.
    "trap-high-mem-threshold": "integer",  # Memory usage when trap is sent.
    "community": "string",  # SNMP Community Configuration.
    "user": "string",  # SNMP User Configuration.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "engine-id": "AC SNMP engineID string (maximum 24 characters).",
    "contact-info": "Contact Information.",
    "trap-high-cpu-threshold": "CPU usage when trap is sent.",
    "trap-high-mem-threshold": "Memory usage when trap is sent.",
    "community": "SNMP Community Configuration.",
    "user": "SNMP User Configuration.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "engine-id": {"type": "string", "max_length": 23},
    "contact-info": {"type": "string", "max_length": 31},
    "trap-high-cpu-threshold": {"type": "integer", "min": 10, "max": 100},
    "trap-high-mem-threshold": {"type": "integer", "min": 10, "max": 100},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "community": {
        "id": {
            "type": "integer",
            "help": "Community ID.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "name": {
            "type": "string",
            "help": "Community name.",
            "required": True,
            "default": "",
            "max_length": 35,
        },
        "status": {
            "type": "option",
            "help": "Enable/disable this SNMP community.",
            "default": "enable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "query-v1-status": {
            "type": "option",
            "help": "Enable/disable SNMP v1 queries.",
            "default": "enable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "query-v2c-status": {
            "type": "option",
            "help": "Enable/disable SNMP v2c queries.",
            "default": "enable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "trap-v1-status": {
            "type": "option",
            "help": "Enable/disable SNMP v1 traps.",
            "default": "enable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "trap-v2c-status": {
            "type": "option",
            "help": "Enable/disable SNMP v2c traps.",
            "default": "enable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "hosts": {
            "type": "string",
            "help": "Configure IPv4 SNMP managers (hosts).",
        },
        "hosts6": {
            "type": "string",
            "help": "Configure IPv6 SNMP managers (hosts).",
        },
    },
    "user": {
        "name": {
            "type": "string",
            "help": "SNMP user name.",
            "required": True,
            "default": "",
            "max_length": 32,
        },
        "status": {
            "type": "option",
            "help": "SNMP user enable.",
            "default": "enable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "queries": {
            "type": "option",
            "help": "Enable/disable SNMP queries for this user.",
            "default": "enable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "trap-status": {
            "type": "option",
            "help": "Enable/disable traps for this SNMP user.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
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
            "default": "sha",
            "options": [{"help": "HMAC-MD5-96 authentication protocol.", "label": "Md5", "name": "md5"}, {"help": "HMAC-SHA-96 authentication protocol.", "label": "Sha", "name": "sha"}, {"help": "HMAC-SHA224 authentication protocol.", "label": "Sha224", "name": "sha224"}, {"help": "HMAC-SHA256 authentication protocol.", "label": "Sha256", "name": "sha256"}, {"help": "HMAC-SHA384 authentication protocol.", "label": "Sha384", "name": "sha384"}, {"help": "HMAC-SHA512 authentication protocol.", "label": "Sha512", "name": "sha512"}],
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
            "default": "aes",
            "options": [{"help": "CFB128-AES-128 symmetric encryption protocol.", "label": "Aes", "name": "aes"}, {"help": "CBC-DES symmetric encryption protocol.", "label": "Des", "name": "des"}, {"help": "CFB128-AES-256 symmetric encryption protocol.", "label": "Aes256", "name": "aes256"}, {"help": "CFB128-AES-256 symmetric encryption protocol compatible with CISCO.", "label": "Aes256Cisco", "name": "aes256cisco"}],
        },
        "priv-pwd": {
            "type": "password",
            "help": "Password for privacy (encryption) protocol.",
            "required": True,
            "max_length": 128,
        },
        "notify-hosts": {
            "type": "ipv4-address",
            "help": "Configure SNMP User Notify Hosts.",
            "default": "",
        },
        "notify-hosts6": {
            "type": "ipv6-address",
            "help": "Configure IPv6 SNMP User Notify Hosts.",
            "default": "",
        },
    },
}


# Valid enum values from API documentation
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_wireless_controller_snmp_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for wireless_controller/snmp."""
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
    """Validate required fields for wireless_controller/snmp."""
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


def validate_wireless_controller_snmp_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new wireless_controller/snmp object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_wireless_controller_snmp_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update wireless_controller/snmp."""
    # Step 1: Validate enum values

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
    "endpoint": "wireless_controller/snmp",
    "category": "cmdb",
    "api_path": "wireless-controller/snmp",
    "help": "Configure SNMP.",
    "total_fields": 6,
    "required_fields_count": 0,
    "fields_with_defaults_count": 4,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
