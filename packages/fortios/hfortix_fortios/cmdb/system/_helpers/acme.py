"""Validation helpers for system/acme - Auto-generated"""

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
    "use-ha-direct": "disable",
    "source-ip": "0.0.0.0",
    "source-ip6": "::",
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
    "interface": "string",  # Interface(s) on which the ACME client will listen for challe
    "use-ha-direct": "option",  # Enable the use of 'ha-mgmt' interface to connect to the ACME
    "source-ip": "ipv4-address",  # Source IPv4 address used to connect to the ACME server.
    "source-ip6": "ipv6-address",  # Source IPv6 address used to connect to the ACME server.
    "accounts": "string",  # ACME accounts list.
    "acc-details": "key",  # Print Account information and decrypted key.
    "status": "key",  # Print information about the current status of the acme clien
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "interface": "Interface(s) on which the ACME client will listen for challenges.",
    "use-ha-direct": "Enable the use of 'ha-mgmt' interface to connect to the ACME server when 'ha-direct' is enabled in HA configuration",
    "source-ip": "Source IPv4 address used to connect to the ACME server.",
    "source-ip6": "Source IPv6 address used to connect to the ACME server.",
    "accounts": "ACME accounts list.",
    "acc-details": "Print Account information and decrypted key.",
    "status": "Print information about the current status of the acme client.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "interface": {
        "interface-name": {
            "type": "string",
            "help": "Interface name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "accounts": {
        "id": {
            "type": "string",
            "help": "Account id.",
            "default": "",
            "max_length": 255,
        },
        "status": {
            "type": "string",
            "help": "Account status.",
            "required": True,
            "default": "",
            "max_length": 127,
        },
        "url": {
            "type": "string",
            "help": "Account url.",
            "required": True,
            "default": "",
            "max_length": 511,
        },
        "ca_url": {
            "type": "string",
            "help": "Account ca_url.",
            "required": True,
            "default": "",
            "max_length": 255,
        },
        "email": {
            "type": "string",
            "help": "Account email.",
            "required": True,
            "default": "",
            "max_length": 255,
        },
        "eab-key-id": {
            "type": "var-string",
            "help": "External Acccount Binding Key ID.",
            "max_length": 255,
        },
        "eab-key-hmac": {
            "type": "password",
            "help": "External Acccount Binding Key HMAC.",
            "max_length": 128,
        },
        "privatekey": {
            "type": "string",
            "help": "Account Private Key.",
            "required": True,
            "default": "",
            "max_length": 8191,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_USE_HA_DIRECT = [
    "enable",
    "disable",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_system_acme_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for system/acme."""
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


def validate_system_acme_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new system/acme object."""
    # Step 1: Validate required fields using central function
    is_valid, error = _validate_required_fields(
        payload,
        REQUIRED_FIELDS,
        FIELD_DESCRIPTIONS
    )
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values using central function
    if "use-ha-direct" in payload:
        is_valid, error = _validate_enum_field(
            "use-ha-direct",
            payload["use-ha-direct"],
            VALID_BODY_USE_HA_DIRECT,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_system_acme_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update system/acme."""
    # Validate enum values using central function
    if "use-ha-direct" in payload:
        is_valid, error = _validate_enum_field(
            "use-ha-direct",
            payload["use-ha-direct"],
            VALID_BODY_USE_HA_DIRECT,
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
    "endpoint": "system/acme",
    "category": "cmdb",
    "api_path": "system/acme",
    "help": "Configure ACME client.",
    "total_fields": 7,
    "required_fields_count": 0,
    "fields_with_defaults_count": 3,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
