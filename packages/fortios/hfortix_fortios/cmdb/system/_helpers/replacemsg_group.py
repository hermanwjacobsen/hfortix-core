"""Validation helpers for system/replacemsg_group - Auto-generated"""

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
    "group-type": "default",
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
    "name": "string",  # Group name.
    "comment": "var-string",  # Comment.
    "group-type": "option",  # Group type.
    "mail": "string",  # Replacement message table entries.
    "http": "string",  # Replacement message table entries.
    "webproxy": "string",  # Replacement message table entries.
    "ftp": "string",  # Replacement message table entries.
    "fortiguard-wf": "string",  # Replacement message table entries.
    "spam": "string",  # Replacement message table entries.
    "alertmail": "string",  # Replacement message table entries.
    "admin": "string",  # Replacement message table entries.
    "auth": "string",  # Replacement message table entries.
    "sslvpn": "string",  # Replacement message table entries.
    "nac-quar": "string",  # Replacement message table entries.
    "traffic-quota": "string",  # Replacement message table entries.
    "utm": "string",  # Replacement message table entries.
    "custom-message": "string",  # Replacement message table entries.
    "icap": "string",  # Replacement message table entries.
    "automation": "string",  # Replacement message table entries.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Group name.",
    "comment": "Comment.",
    "group-type": "Group type.",
    "mail": "Replacement message table entries.",
    "http": "Replacement message table entries.",
    "webproxy": "Replacement message table entries.",
    "ftp": "Replacement message table entries.",
    "fortiguard-wf": "Replacement message table entries.",
    "spam": "Replacement message table entries.",
    "alertmail": "Replacement message table entries.",
    "admin": "Replacement message table entries.",
    "auth": "Replacement message table entries.",
    "sslvpn": "Replacement message table entries.",
    "nac-quar": "Replacement message table entries.",
    "traffic-quota": "Replacement message table entries.",
    "utm": "Replacement message table entries.",
    "custom-message": "Replacement message table entries.",
    "icap": "Replacement message table entries.",
    "automation": "Replacement message table entries.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 35},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "mail": {
        "msg-type": {
            "type": "string",
            "help": "Message type.",
            "required": True,
            "default": "",
            "max_length": 28,
        },
        "buffer": {
            "type": "var-string",
            "help": "Message string.",
            "max_length": 32768,
        },
        "header": {
            "type": "option",
            "help": "Header flag.",
            "default": "none",
            "options": ["none", "http", "8bit"],
        },
        "format": {
            "type": "option",
            "help": "Format flag.",
            "default": "none",
            "options": ["none", "text", "html"],
        },
    },
    "http": {
        "msg-type": {
            "type": "string",
            "help": "Message type.",
            "required": True,
            "default": "",
            "max_length": 28,
        },
        "buffer": {
            "type": "var-string",
            "help": "Message string.",
            "max_length": 32768,
        },
        "header": {
            "type": "option",
            "help": "Header flag.",
            "default": "none",
            "options": ["none", "http", "8bit"],
        },
        "format": {
            "type": "option",
            "help": "Format flag.",
            "default": "none",
            "options": ["none", "text", "html"],
        },
    },
    "webproxy": {
        "msg-type": {
            "type": "string",
            "help": "Message type.",
            "required": True,
            "default": "",
            "max_length": 28,
        },
        "buffer": {
            "type": "var-string",
            "help": "Message string.",
            "max_length": 32768,
        },
        "header": {
            "type": "option",
            "help": "Header flag.",
            "default": "none",
            "options": ["none", "http", "8bit"],
        },
        "format": {
            "type": "option",
            "help": "Format flag.",
            "default": "none",
            "options": ["none", "text", "html"],
        },
    },
    "ftp": {
        "msg-type": {
            "type": "string",
            "help": "Message type.",
            "required": True,
            "default": "",
            "max_length": 28,
        },
        "buffer": {
            "type": "var-string",
            "help": "Message string.",
            "max_length": 32768,
        },
        "header": {
            "type": "option",
            "help": "Header flag.",
            "default": "none",
            "options": ["none", "http", "8bit"],
        },
        "format": {
            "type": "option",
            "help": "Format flag.",
            "default": "none",
            "options": ["none", "text", "html"],
        },
    },
    "fortiguard-wf": {
        "msg-type": {
            "type": "string",
            "help": "Message type.",
            "required": True,
            "default": "",
            "max_length": 28,
        },
        "buffer": {
            "type": "var-string",
            "help": "Message string.",
            "max_length": 32768,
        },
        "header": {
            "type": "option",
            "help": "Header flag.",
            "default": "none",
            "options": ["none", "http", "8bit"],
        },
        "format": {
            "type": "option",
            "help": "Format flag.",
            "default": "none",
            "options": ["none", "text", "html"],
        },
    },
    "spam": {
        "msg-type": {
            "type": "string",
            "help": "Message type.",
            "required": True,
            "default": "",
            "max_length": 28,
        },
        "buffer": {
            "type": "var-string",
            "help": "Message string.",
            "max_length": 32768,
        },
        "header": {
            "type": "option",
            "help": "Header flag.",
            "default": "none",
            "options": ["none", "http", "8bit"],
        },
        "format": {
            "type": "option",
            "help": "Format flag.",
            "default": "none",
            "options": ["none", "text", "html"],
        },
    },
    "alertmail": {
        "msg-type": {
            "type": "string",
            "help": "Message type.",
            "required": True,
            "default": "",
            "max_length": 28,
        },
        "buffer": {
            "type": "var-string",
            "help": "Message string.",
            "max_length": 32768,
        },
        "header": {
            "type": "option",
            "help": "Header flag.",
            "default": "none",
            "options": ["none", "http", "8bit"],
        },
        "format": {
            "type": "option",
            "help": "Format flag.",
            "default": "none",
            "options": ["none", "text", "html"],
        },
    },
    "admin": {
        "msg-type": {
            "type": "string",
            "help": "Message type.",
            "required": True,
            "default": "",
            "max_length": 28,
        },
        "buffer": {
            "type": "var-string",
            "help": "Message string.",
            "max_length": 32768,
        },
        "header": {
            "type": "option",
            "help": "Header flag.",
            "default": "none",
            "options": ["none", "http", "8bit"],
        },
        "format": {
            "type": "option",
            "help": "Format flag.",
            "default": "none",
            "options": ["none", "text", "html"],
        },
    },
    "auth": {
        "msg-type": {
            "type": "string",
            "help": "Message type.",
            "required": True,
            "default": "",
            "max_length": 28,
        },
        "buffer": {
            "type": "var-string",
            "help": "Message string.",
            "max_length": 32768,
        },
        "header": {
            "type": "option",
            "help": "Header flag.",
            "default": "none",
            "options": ["none", "http", "8bit"],
        },
        "format": {
            "type": "option",
            "help": "Format flag.",
            "default": "none",
            "options": ["none", "text", "html"],
        },
    },
    "sslvpn": {
        "msg-type": {
            "type": "string",
            "help": "Message type.",
            "required": True,
            "default": "",
            "max_length": 28,
        },
        "buffer": {
            "type": "var-string",
            "help": "Message string.",
            "max_length": 32768,
        },
        "header": {
            "type": "option",
            "help": "Header flag.",
            "default": "none",
            "options": ["none", "http", "8bit"],
        },
        "format": {
            "type": "option",
            "help": "Format flag.",
            "default": "none",
            "options": ["none", "text", "html"],
        },
    },
    "nac-quar": {
        "msg-type": {
            "type": "string",
            "help": "Message type.",
            "required": True,
            "default": "",
            "max_length": 28,
        },
        "buffer": {
            "type": "var-string",
            "help": "Message string.",
            "max_length": 32768,
        },
        "header": {
            "type": "option",
            "help": "Header flag.",
            "default": "none",
            "options": ["none", "http", "8bit"],
        },
        "format": {
            "type": "option",
            "help": "Format flag.",
            "default": "none",
            "options": ["none", "text", "html"],
        },
    },
    "traffic-quota": {
        "msg-type": {
            "type": "string",
            "help": "Message type.",
            "required": True,
            "default": "",
            "max_length": 28,
        },
        "buffer": {
            "type": "var-string",
            "help": "Message string.",
            "max_length": 32768,
        },
        "header": {
            "type": "option",
            "help": "Header flag.",
            "default": "none",
            "options": ["none", "http", "8bit"],
        },
        "format": {
            "type": "option",
            "help": "Format flag.",
            "default": "none",
            "options": ["none", "text", "html"],
        },
    },
    "utm": {
        "msg-type": {
            "type": "string",
            "help": "Message type.",
            "required": True,
            "default": "",
            "max_length": 28,
        },
        "buffer": {
            "type": "var-string",
            "help": "Message string.",
            "max_length": 32768,
        },
        "header": {
            "type": "option",
            "help": "Header flag.",
            "default": "none",
            "options": ["none", "http", "8bit"],
        },
        "format": {
            "type": "option",
            "help": "Format flag.",
            "default": "none",
            "options": ["none", "text", "html"],
        },
    },
    "custom-message": {
        "msg-type": {
            "type": "string",
            "help": "Message type.",
            "required": True,
            "default": "",
            "max_length": 28,
        },
        "buffer": {
            "type": "var-string",
            "help": "Message string.",
            "max_length": 32768,
        },
        "header": {
            "type": "option",
            "help": "Header flag.",
            "default": "none",
            "options": ["none", "http", "8bit"],
        },
        "format": {
            "type": "option",
            "help": "Format flag.",
            "default": "none",
            "options": ["none", "text", "html"],
        },
    },
    "icap": {
        "msg-type": {
            "type": "string",
            "help": "Message type.",
            "required": True,
            "default": "",
            "max_length": 28,
        },
        "buffer": {
            "type": "var-string",
            "help": "Message string.",
            "max_length": 32768,
        },
        "header": {
            "type": "option",
            "help": "Header flag.",
            "default": "none",
            "options": ["none", "http", "8bit"],
        },
        "format": {
            "type": "option",
            "help": "Format flag.",
            "default": "none",
            "options": ["none", "text", "html"],
        },
    },
    "automation": {
        "msg-type": {
            "type": "string",
            "help": "Message type.",
            "required": True,
            "default": "",
            "max_length": 28,
        },
        "buffer": {
            "type": "var-string",
            "help": "Message string.",
            "max_length": 32768,
        },
        "header": {
            "type": "option",
            "help": "Header flag.",
            "default": "none",
            "options": ["none", "http", "8bit"],
        },
        "format": {
            "type": "option",
            "help": "Format flag.",
            "default": "none",
            "options": ["none", "text", "html"],
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_GROUP_TYPE = [
    "default",
    "utm",
    "auth",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_system_replacemsg_group_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for system/replacemsg_group."""
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


def validate_system_replacemsg_group_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new system/replacemsg_group object."""
    # Step 1: Validate required fields using central function
    is_valid, error = _validate_required_fields(
        payload,
        REQUIRED_FIELDS,
        FIELD_DESCRIPTIONS
    )
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values using central function
    if "group-type" in payload:
        is_valid, error = _validate_enum_field(
            "group-type",
            payload["group-type"],
            VALID_BODY_GROUP_TYPE,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_system_replacemsg_group_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update system/replacemsg_group."""
    # Validate enum values using central function
    if "group-type" in payload:
        is_valid, error = _validate_enum_field(
            "group-type",
            payload["group-type"],
            VALID_BODY_GROUP_TYPE,
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
    "endpoint": "system/replacemsg_group",
    "category": "cmdb",
    "api_path": "system/replacemsg-group",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure replacement message groups.",
    "total_fields": 19,
    "required_fields_count": 0,
    "fields_with_defaults_count": 2,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
