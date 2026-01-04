"""
Validation helpers for system/saml endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification
Customize as needed for endpoint-specific business logic.
"""

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
#
# 1. FALSE POSITIVES: Some fields marked "required" have default values,
#    meaning they're optional (filtered out by generator)
#
# 2. CONDITIONAL REQUIREMENTS: Many endpoints require EITHER field A OR field B:
#    - firewall.policy: requires (srcaddr + dstaddr) OR (srcaddr6 + dstaddr6)
#    - These conditional requirements cannot be expressed in a simple list
#
# 3. SPECIALIZED FEATURES: Fields for WAN optimization, VPN, NAT64, etc.
#    are marked "required" but only apply when using those features
#
# The REQUIRED_FIELDS list below is INFORMATIONAL ONLY and shows fields that:
# - Are marked required in the schema
# - Don't have non-empty default values
# - Aren't specialized feature fields
#
# Do NOT use this list for strict validation - test with the actual FortiOS API!

# Fields marked as required (after filtering false positives)
REQUIRED_FIELDS = [
    "default-profile",  # Default profile for new SSO admin.
    "entity-id",  # SP entity ID.
    "idp-cert",  # IDP certificate name.
    "server-address",  # Server address.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "status": "disable",
    "role": "service-provider",
    "default-login-page": "normal",
    "default-profile": "",
    "cert": "",
    "binding-protocol": "redirect",
    "portal-url": "",
    "entity-id": "",
    "single-sign-on-url": "",
    "single-logout-url": "",
    "idp-entity-id": "",
    "idp-single-sign-on-url": "",
    "idp-single-logout-url": "",
    "idp-cert": "",
    "server-address": "",
    "tolerance": 5,
    "life": 30,
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
    "status": "option",  # Enable/disable SAML authentication (default = disable).
    "role": "option",  # SAML role.
    "default-login-page": "option",  # Choose default login page.
    "default-profile": "string",  # Default profile for new SSO admin.
    "cert": "string",  # Certificate to sign SAML messages.
    "binding-protocol": "option",  # IdP Binding protocol.
    "portal-url": "string",  # SP portal URL.
    "entity-id": "string",  # SP entity ID.
    "single-sign-on-url": "string",  # SP single sign-on URL.
    "single-logout-url": "string",  # SP single logout URL.
    "idp-entity-id": "string",  # IDP entity ID.
    "idp-single-sign-on-url": "string",  # IDP single sign-on URL.
    "idp-single-logout-url": "string",  # IDP single logout URL.
    "idp-cert": "string",  # IDP certificate name.
    "server-address": "string",  # Server address.
    "tolerance": "integer",  # Tolerance to the range of time when the assertion is valid (
    "life": "integer",  # Length of the range of time when the assertion is valid (in 
    "service-providers": "string",  # Authorized service providers.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "status": "Enable/disable SAML authentication (default = disable).",
    "role": "SAML role.",
    "default-login-page": "Choose default login page.",
    "default-profile": "Default profile for new SSO admin.",
    "cert": "Certificate to sign SAML messages.",
    "binding-protocol": "IdP Binding protocol.",
    "portal-url": "SP portal URL.",
    "entity-id": "SP entity ID.",
    "single-sign-on-url": "SP single sign-on URL.",
    "single-logout-url": "SP single logout URL.",
    "idp-entity-id": "IDP entity ID.",
    "idp-single-sign-on-url": "IDP single sign-on URL.",
    "idp-single-logout-url": "IDP single logout URL.",
    "idp-cert": "IDP certificate name.",
    "server-address": "Server address.",
    "tolerance": "Tolerance to the range of time when the assertion is valid (in minutes).",
    "life": "Length of the range of time when the assertion is valid (in minutes).",
    "service-providers": "Authorized service providers.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "default-profile": {"type": "string", "max_length": 35},
    "cert": {"type": "string", "max_length": 35},
    "portal-url": {"type": "string", "max_length": 255},
    "entity-id": {"type": "string", "max_length": 255},
    "single-sign-on-url": {"type": "string", "max_length": 255},
    "single-logout-url": {"type": "string", "max_length": 255},
    "idp-entity-id": {"type": "string", "max_length": 255},
    "idp-single-sign-on-url": {"type": "string", "max_length": 255},
    "idp-single-logout-url": {"type": "string", "max_length": 255},
    "idp-cert": {"type": "string", "max_length": 35},
    "server-address": {"type": "string", "max_length": 63},
    "tolerance": {"type": "integer", "min": 0, "max": 4294967295},
    "life": {"type": "integer", "min": 0, "max": 4294967295},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "service-providers": {
        "name": {
            "type": "string",
            "help": "Name.",
            "required": True,
            "default": "",
            "max_length": 35,
        },
        "prefix": {
            "type": "string",
            "help": "Prefix.",
            "required": True,
            "default": "",
            "max_length": 35,
        },
        "sp-binding-protocol": {
            "type": "option",
            "help": "SP binding protocol.",
            "default": "post",
            "options": ["post", "redirect"],
        },
        "sp-cert": {
            "type": "string",
            "help": "SP certificate name.",
            "default": "",
            "max_length": 35,
        },
        "sp-entity-id": {
            "type": "string",
            "help": "SP entity ID.",
            "required": True,
            "default": "",
            "max_length": 255,
        },
        "sp-single-sign-on-url": {
            "type": "string",
            "help": "SP single sign-on URL.",
            "required": True,
            "default": "",
            "max_length": 255,
        },
        "sp-single-logout-url": {
            "type": "string",
            "help": "SP single logout URL.",
            "default": "",
            "max_length": 255,
        },
        "sp-portal-url": {
            "type": "string",
            "help": "SP portal URL.",
            "default": "",
            "max_length": 255,
        },
        "idp-entity-id": {
            "type": "string",
            "help": "IDP entity ID.",
            "default": "",
            "max_length": 255,
        },
        "idp-single-sign-on-url": {
            "type": "string",
            "help": "IDP single sign-on URL.",
            "default": "",
            "max_length": 255,
        },
        "idp-single-logout-url": {
            "type": "string",
            "help": "IDP single logout URL.",
            "default": "",
            "max_length": 255,
        },
        "assertion-attributes": {
            "type": "string",
            "help": "Customized SAML attributes to send along with assertion.",
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_STATUS = [
    "enable",
    "disable",
]
VALID_BODY_ROLE = [
    "identity-provider",
    "service-provider",
]
VALID_BODY_DEFAULT_LOGIN_PAGE = [
    "normal",
    "sso",
]
VALID_BODY_BINDING_PROTOCOL = [
    "post",
    "redirect",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_system_saml_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for system/saml.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_system_saml_get()
        >>> assert is_valid == True
        
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_system_saml_get(
        ...     filters={"format": "name|type"}
        ... )
        >>> assert is_valid == True
    """
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
    """
    Validate required fields for system/saml.

    This validator checks:
    1. Always-required fields are present
    2. Mutually exclusive groups have at least one field

    Args:
        payload: The request payload to validate

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "test"}
        >>> is_valid, error = validate_required_fields(payload)
    """
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


def validate_system_saml_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new system/saml object.

    This validator performs two-stage validation:
    1. Required fields check (schema-based)
    2. Field value validation (enums, ranges, formats)

    Args:
        payload: Request body data with configuration
        **params: Query parameters (vdom, etc.)

    Returns:
        Tuple of (is_valid, error_message)
        - is_valid: True if payload is valid, False otherwise
        - error_message: None if valid, detailed error string if invalid

    Examples:
        >>> # ✅ Valid - Minimal required fields
        >>> payload = {
        ...     "default-profile": True,  # Default profile for new SSO admin.
        ...     "entity-id": True,  # SP entity ID.
        ... }
        >>> is_valid, error = validate_system_saml_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "default-profile": True,
        ...     "status": "enable",  # Valid enum value
        ... }
        >>> is_valid, error = validate_system_saml_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["status"] = "invalid-value"
        >>> is_valid, error = validate_system_saml_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_system_saml_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            desc = FIELD_DESCRIPTIONS.get("status", "")
            error_msg = f"Invalid value for 'status': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_STATUS)}"
            error_msg += f"\n  → Example: status='{{ VALID_BODY_STATUS[0] }}'"
            return (False, error_msg)
    if "role" in payload:
        value = payload["role"]
        if value not in VALID_BODY_ROLE:
            desc = FIELD_DESCRIPTIONS.get("role", "")
            error_msg = f"Invalid value for 'role': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ROLE)}"
            error_msg += f"\n  → Example: role='{{ VALID_BODY_ROLE[0] }}'"
            return (False, error_msg)
    if "default-login-page" in payload:
        value = payload["default-login-page"]
        if value not in VALID_BODY_DEFAULT_LOGIN_PAGE:
            desc = FIELD_DESCRIPTIONS.get("default-login-page", "")
            error_msg = f"Invalid value for 'default-login-page': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DEFAULT_LOGIN_PAGE)}"
            error_msg += f"\n  → Example: default-login-page='{{ VALID_BODY_DEFAULT_LOGIN_PAGE[0] }}'"
            return (False, error_msg)
    if "binding-protocol" in payload:
        value = payload["binding-protocol"]
        if value not in VALID_BODY_BINDING_PROTOCOL:
            desc = FIELD_DESCRIPTIONS.get("binding-protocol", "")
            error_msg = f"Invalid value for 'binding-protocol': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_BINDING_PROTOCOL)}"
            error_msg += f"\n  → Example: binding-protocol='{{ VALID_BODY_BINDING_PROTOCOL[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_system_saml_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update system/saml.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_system_saml_put(payload)
    """
    # Step 1: Validate enum values
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid value for 'status'='{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )
    if "role" in payload:
        value = payload["role"]
        if value not in VALID_BODY_ROLE:
            return (
                False,
                f"Invalid value for 'role'='{value}'. Must be one of: {', '.join(VALID_BODY_ROLE)}",
            )
    if "default-login-page" in payload:
        value = payload["default-login-page"]
        if value not in VALID_BODY_DEFAULT_LOGIN_PAGE:
            return (
                False,
                f"Invalid value for 'default-login-page'='{value}'. Must be one of: {', '.join(VALID_BODY_DEFAULT_LOGIN_PAGE)}",
            )
    if "binding-protocol" in payload:
        value = payload["binding-protocol"]
        if value not in VALID_BODY_BINDING_PROTOCOL:
            return (
                False,
                f"Invalid value for 'binding-protocol'='{value}'. Must be one of: {', '.join(VALID_BODY_BINDING_PROTOCOL)}",
            )

    return (True, None)


# ============================================================================
# Metadata Access Functions
# Provide programmatic access to field metadata for IDE autocomplete,
# documentation generation, and dynamic validation
# ============================================================================


def get_field_description(field_name: str) -> str | None:
    """
    Get description/help text for a field.

    Args:
        field_name: Name of the field

    Returns:
        Description text or None if field doesn't exist

    Example:
        >>> desc = get_field_description("name")
        >>> print(desc)
    """
    return FIELD_DESCRIPTIONS.get(field_name)


def get_field_type(field_name: str) -> str | None:
    """
    Get the type of a field.

    Args:
        field_name: Name of the field

    Returns:
        Field type (e.g., "string", "integer", "option") or None

    Example:
        >>> field_type = get_field_type("status")
        >>> print(field_type)  # "option"
    """
    return FIELD_TYPES.get(field_name)


def get_field_constraints(field_name: str) -> dict[str, Any] | None:
    """
    Get constraints for a field (min/max values, string length).

    Args:
        field_name: Name of the field

    Returns:
        Constraint dict or None

    Example:
        >>> constraints = get_field_constraints("port")
        >>> print(constraints)  # {"type": "integer", "min": 1, "max": 65535}
    """
    return FIELD_CONSTRAINTS.get(field_name)


def get_field_default(field_name: str) -> Any | None:
    """
    Get default value for a field.

    Args:
        field_name: Name of the field

    Returns:
        Default value or None if no default

    Example:
        >>> default = get_field_default("status")
        >>> print(default)  # "enable"
    """
    return FIELDS_WITH_DEFAULTS.get(field_name)


def get_field_options(field_name: str) -> list[str] | None:
    """
    Get valid enum options for a field.

    Args:
        field_name: Name of the field

    Returns:
        List of valid values or None if not an enum field

    Example:
        >>> options = get_field_options("status")
        >>> print(options)  # ["enable", "disable"]
    """
    # Construct the constant name from field name
    constant_name = f"VALID_BODY_{field_name.replace('-', '_').upper()}"
    return globals().get(constant_name)


def get_nested_schema(field_name: str) -> dict[str, Any] | None:
    """
    Get schema for nested table/list fields.

    Args:
        field_name: Name of the parent field

    Returns:
        Dict mapping child field names to their metadata

    Example:
        >>> nested = get_nested_schema("members")
        >>> if nested:
        ...     for child_field, child_meta in nested.items():
        ...         print(f"{child_field}: {child_meta['type']}")
    """
    return NESTED_SCHEMAS.get(field_name)


def get_all_fields() -> list[str]:
    """
    Get list of all field names.

    Returns:
        List of all field names in the schema

    Example:
        >>> fields = get_all_fields()
        >>> print(len(fields))
    """
    return list(FIELD_TYPES.keys())


def get_field_metadata(field_name: str) -> dict[str, Any] | None:
    """
    Get complete metadata for a field (type, description, constraints, defaults, options).

    Args:
        field_name: Name of the field

    Returns:
        Dict with all available metadata or None if field doesn't exist

    Example:
        >>> meta = get_field_metadata("status")
        >>> print(meta)
        >>> # {
        >>> #   "type": "option",
        >>> #   "description": "Enable/disable this feature",
        >>> #   "default": "enable",
        >>> #   "options": ["enable", "disable"]
        >>> # }
    """
    if field_name not in FIELD_TYPES:
        return None

    metadata = {
        "name": field_name,
        "type": FIELD_TYPES[field_name],
    }

    # Add description if available
    if field_name in FIELD_DESCRIPTIONS:
        metadata["description"] = FIELD_DESCRIPTIONS[field_name]

    # Add constraints if available
    if field_name in FIELD_CONSTRAINTS:
        metadata["constraints"] = FIELD_CONSTRAINTS[field_name]

    # Add default if available
    if field_name in FIELDS_WITH_DEFAULTS:
        metadata["default"] = FIELDS_WITH_DEFAULTS[field_name]

    # Add required flag
    metadata["required"] = field_name in REQUIRED_FIELDS

    # Add options if available
    options = get_field_options(field_name)
    if options:
        metadata["options"] = options

    # Add nested schema if available
    nested = get_nested_schema(field_name)
    if nested:
        metadata["nested_schema"] = nested

    return metadata


def validate_field_value(field_name: str, value: Any) -> tuple[bool, str | None]:
    """
    Validate a single field value against its constraints.

    Args:
        field_name: Name of the field
        value: Value to validate

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> is_valid, error = validate_field_value("status", "enable")
        >>> if not is_valid:
        ...     print(error)
    """
    # Get field metadata
    field_type = get_field_type(field_name)
    if field_type is None:
        return (False, f"Unknown field: '{field_name}' (not defined in schema)")

    # Get field description for better error context
    description = get_field_description(field_name)

    # Validate enum values
    options = get_field_options(field_name)
    if options and value not in options:
        error_msg = f"Invalid value for '{field_name}': {repr(value)}"
        if description:
            error_msg += f"\n  → Description: {description}"
        error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in options)}"
        if options:
            error_msg += f"\n  → Example: {field_name}={repr(options[0])}"
        return (False, error_msg)

    # Validate constraints
    constraints = get_field_constraints(field_name)
    if constraints:
        constraint_type = constraints.get("type")

        if constraint_type == "integer":
            if not isinstance(value, int):
                error_msg = f"Field '{field_name}' must be an integer"
                if description:
                    error_msg += f"\n  → Description: {description}"
                error_msg += f"\n  → You provided: {type(value).__name__} = {repr(value)}"
                return (False, error_msg)

            min_val = constraints.get("min")
            max_val = constraints.get("max")

            if min_val is not None and value < min_val:
                error_msg = f"Field '{field_name}' value {value} is below minimum {min_val}"
                if description:
                    error_msg += f"\n  → Description: {description}"
                if max_val is not None:
                    error_msg += f"\n  → Valid range: {min_val} to {max_val}"
                return (False, error_msg)

            if max_val is not None and value > max_val:
                error_msg = f"Field '{field_name}' value {value} exceeds maximum {max_val}"
                if description:
                    error_msg += f"\n  → Description: {description}"
                if min_val is not None:
                    error_msg += f"\n  → Valid range: {min_val} to {max_val}"
                return (False, error_msg)

        elif constraint_type == "string":
            if not isinstance(value, str):
                error_msg = f"Field '{field_name}' must be a string"
                if description:
                    error_msg += f"\n  → Description: {description}"
                error_msg += f"\n  → You provided: {type(value).__name__} = {repr(value)}"
                return (False, error_msg)

            max_length = constraints.get("max_length")
            if max_length and len(value) > max_length:
                error_msg = f"Field '{field_name}' length {len(value)} exceeds maximum {max_length}"
                if description:
                    error_msg += f"\n  → Description: {description}"
                error_msg += f"\n  → Your value: {repr(value[:50])}{'...' if len(value) > 50 else ''}"
                return (False, error_msg)

    return (True, None)


# ============================================================================
# Schema Information
# Metadata about this endpoint schema
# ============================================================================

SCHEMA_INFO = {
    "endpoint": "system/saml",
    "category": "cmdb",
    "api_path": "system/saml",
    "help": "Global settings for SAML authentication.",
    "total_fields": 18,
    "required_fields_count": 4,
    "fields_with_defaults_count": 17,
}


def get_schema_info() -> dict[str, Any]:
    """
    Get information about this endpoint schema.

    Returns:
        Dict with schema metadata

    Example:
        >>> info = get_schema_info()
        >>> print(f"Endpoint: {info['endpoint']}")
        >>> print(f"Total fields: {info['total_fields']}")
    """
    return SCHEMA_INFO.copy()
