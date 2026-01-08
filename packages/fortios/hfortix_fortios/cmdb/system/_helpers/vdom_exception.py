"""Validation helpers for system/vdom_exception - Auto-generated"""

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
    "object",  # Name of the configuration object that can be configured independently for all VDOMs.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "id": 0,
    "object": "",
    "scope": "all",
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
    "id": "integer",  # Index (1 - 4096).
    "object": "option",  # Name of the configuration object that can be configured inde
    "scope": "option",  # Determine whether the configuration object can be configured
    "vdom": "string",  # Names of the VDOMs.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "id": "Index (1 - 4096).",
    "object": "Name of the configuration object that can be configured independently for all VDOMs.",
    "scope": "Determine whether the configuration object can be configured separately for all VDOMs or if some VDOMs share the same configuration.",
    "vdom": "Names of the VDOMs.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "id": {"type": "integer", "min": 1, "max": 4096},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "vdom": {
        "name": {
            "type": "string",
            "help": "VDOM name.",
            "default": "",
            "max_length": 79,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_OBJECT = [
    "log.fortianalyzer.setting",
    "log.fortianalyzer.override-setting",
    "log.fortianalyzer2.setting",
    "log.fortianalyzer2.override-setting",
    "log.fortianalyzer3.setting",
    "log.fortianalyzer3.override-setting",
    "log.fortianalyzer-cloud.setting",
    "log.fortianalyzer-cloud.override-setting",
    "log.syslogd.setting",
    "log.syslogd.override-setting",
    "log.syslogd2.setting",
    "log.syslogd2.override-setting",
    "log.syslogd3.setting",
    "log.syslogd3.override-setting",
    "log.syslogd4.setting",
    "log.syslogd4.override-setting",
    "system.gre-tunnel",
    "system.central-management",
    "system.csf",
    "user.radius",
    "system.interface",
    "vpn.ipsec.phase1-interface",
    "vpn.ipsec.phase2-interface",
    "router.bgp",
    "router.route-map",
    "router.prefix-list",
    "firewall.ippool",
    "firewall.ippool6",
    "router.static",
    "router.static6",
    "firewall.vip",
    "firewall.vip6",
    "system.sdwan",
    "system.saml",
    "router.policy",
    "router.policy6",
    "log.syslogd.setting",
    "log.syslogd.override-setting",
    "firewall.address",
]
VALID_BODY_SCOPE = [
    "all",
    "inclusive",
    "exclusive",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_system_vdom_exception_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for system/vdom_exception."""
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


def validate_system_vdom_exception_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new system/vdom_exception object."""
    # Step 1: Validate required fields using central function
    is_valid, error = _validate_required_fields(
        payload,
        REQUIRED_FIELDS,
        FIELD_DESCRIPTIONS
    )
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values using central function
    if "object" in payload:
        is_valid, error = _validate_enum_field(
            "object",
            payload["object"],
            VALID_BODY_OBJECT,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "scope" in payload:
        is_valid, error = _validate_enum_field(
            "scope",
            payload["scope"],
            VALID_BODY_SCOPE,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_system_vdom_exception_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update system/vdom_exception."""
    # Validate enum values using central function
    if "object" in payload:
        is_valid, error = _validate_enum_field(
            "object",
            payload["object"],
            VALID_BODY_OBJECT,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "scope" in payload:
        is_valid, error = _validate_enum_field(
            "scope",
            payload["scope"],
            VALID_BODY_SCOPE,
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
    "endpoint": "system/vdom_exception",
    "category": "cmdb",
    "api_path": "system/vdom-exception",
    "mkey": "id",
    "mkey_type": "integer",
    "help": "Global configuration objects that can be configured independently across different ha peers for all VDOMs or for the defined VDOM scope.",
    "total_fields": 4,
    "required_fields_count": 1,
    "fields_with_defaults_count": 3,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
