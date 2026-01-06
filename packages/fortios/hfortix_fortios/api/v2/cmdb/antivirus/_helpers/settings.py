"""Validation helpers for antivirus/settings - Auto-generated"""

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
    "machine-learning-detection": "enable",
    "use-extreme-db": "disable",
    "grayware": "disable",
    "override-timeout": 0,
    "cache-infected-result": "enable",
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
    "machine-learning-detection": "option",  # Use machine learning based malware detection.
    "use-extreme-db": "option",  # Enable/disable the use of Extreme AVDB.
    "grayware": "option",  # Enable/disable grayware detection when an AntiVirus profile 
    "override-timeout": "integer",  # Override the large file scan timeout value in seconds (30 - 
    "cache-infected-result": "option",  # Enable/disable cache of infected scan results (default = ena
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "machine-learning-detection": "Use machine learning based malware detection.",
    "use-extreme-db": "Enable/disable the use of Extreme AVDB.",
    "grayware": "Enable/disable grayware detection when an AntiVirus profile is applied to traffic.",
    "override-timeout": "Override the large file scan timeout value in seconds (30 - 3600). Zero is the default value and is used to disable this command. When disabled, the daemon adjusts the large file scan timeout based on the file size.",
    "cache-infected-result": "Enable/disable cache of infected scan results (default = enable).",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "override-timeout": {"type": "integer", "min": 30, "max": 3600},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_MACHINE_LEARNING_DETECTION = [
    "enable",  # Enable machine learning based malware detection.
    "monitor",  # Enable machine learning based malware detection for monitoring only.
    "disable",  # Disable machine learning based malware detection.
]
VALID_BODY_USE_EXTREME_DB = [
    "enable",  # Enable extreme AVDB.
    "disable",  # Disable extreme AVDB.
]
VALID_BODY_GRAYWARE = [
    "enable",  # Enable grayware detection.
    "disable",  # Disable grayware detection.
]
VALID_BODY_CACHE_INFECTED_RESULT = [
    "enable",  # Enable cache of infected scan results.
    "disable",  # Disable cache of infected scan results.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_antivirus_settings_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for antivirus/settings."""
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
    """Validate required fields for antivirus/settings."""
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


def validate_antivirus_settings_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new antivirus/settings object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "machine-learning-detection" in payload:
        value = payload["machine-learning-detection"]
        if value not in VALID_BODY_MACHINE_LEARNING_DETECTION:
            desc = FIELD_DESCRIPTIONS.get("machine-learning-detection", "")
            error_msg = f"Invalid value for 'machine-learning-detection': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MACHINE_LEARNING_DETECTION)}"
            error_msg += f"\n  → Example: machine-learning-detection='{{ VALID_BODY_MACHINE_LEARNING_DETECTION[0] }}'"
            return (False, error_msg)
    if "use-extreme-db" in payload:
        value = payload["use-extreme-db"]
        if value not in VALID_BODY_USE_EXTREME_DB:
            desc = FIELD_DESCRIPTIONS.get("use-extreme-db", "")
            error_msg = f"Invalid value for 'use-extreme-db': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_USE_EXTREME_DB)}"
            error_msg += f"\n  → Example: use-extreme-db='{{ VALID_BODY_USE_EXTREME_DB[0] }}'"
            return (False, error_msg)
    if "grayware" in payload:
        value = payload["grayware"]
        if value not in VALID_BODY_GRAYWARE:
            desc = FIELD_DESCRIPTIONS.get("grayware", "")
            error_msg = f"Invalid value for 'grayware': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GRAYWARE)}"
            error_msg += f"\n  → Example: grayware='{{ VALID_BODY_GRAYWARE[0] }}'"
            return (False, error_msg)
    if "cache-infected-result" in payload:
        value = payload["cache-infected-result"]
        if value not in VALID_BODY_CACHE_INFECTED_RESULT:
            desc = FIELD_DESCRIPTIONS.get("cache-infected-result", "")
            error_msg = f"Invalid value for 'cache-infected-result': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CACHE_INFECTED_RESULT)}"
            error_msg += f"\n  → Example: cache-infected-result='{{ VALID_BODY_CACHE_INFECTED_RESULT[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_antivirus_settings_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update antivirus/settings."""
    # Step 1: Validate enum values
    if "machine-learning-detection" in payload:
        value = payload["machine-learning-detection"]
        if value not in VALID_BODY_MACHINE_LEARNING_DETECTION:
            return (
                False,
                f"Invalid value for 'machine-learning-detection'='{value}'. Must be one of: {', '.join(VALID_BODY_MACHINE_LEARNING_DETECTION)}",
            )
    if "use-extreme-db" in payload:
        value = payload["use-extreme-db"]
        if value not in VALID_BODY_USE_EXTREME_DB:
            return (
                False,
                f"Invalid value for 'use-extreme-db'='{value}'. Must be one of: {', '.join(VALID_BODY_USE_EXTREME_DB)}",
            )
    if "grayware" in payload:
        value = payload["grayware"]
        if value not in VALID_BODY_GRAYWARE:
            return (
                False,
                f"Invalid value for 'grayware'='{value}'. Must be one of: {', '.join(VALID_BODY_GRAYWARE)}",
            )
    if "cache-infected-result" in payload:
        value = payload["cache-infected-result"]
        if value not in VALID_BODY_CACHE_INFECTED_RESULT:
            return (
                False,
                f"Invalid value for 'cache-infected-result'='{value}'. Must be one of: {', '.join(VALID_BODY_CACHE_INFECTED_RESULT)}",
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
    "endpoint": "antivirus/settings",
    "category": "cmdb",
    "api_path": "antivirus/settings",
    "help": "Configure AntiVirus settings.",
    "total_fields": 5,
    "required_fields_count": 0,
    "fields_with_defaults_count": 5,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
