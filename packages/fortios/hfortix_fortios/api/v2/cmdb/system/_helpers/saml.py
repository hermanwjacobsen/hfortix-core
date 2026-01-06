"""Validation helpers for system/saml - Auto-generated"""

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
    "require-signed-resp-and-asrt": "disable",
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
    "require-signed-resp-and-asrt": "option",  # Require both response and assertion from IDP to be signed wh
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
    "require-signed-resp-and-asrt": "Require both response and assertion from IDP to be signed when FGT acts as SP (default = disable).",
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
            "options": [{"help": "HTTP POST binding.", "label": "Post", "name": "post"}, {"help": "HTTP Redirect binding.", "label": "Redirect", "name": "redirect"}],
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
    "enable",  # Enable SAML authentication.
    "disable",  # Disable SAML authentication.
]
VALID_BODY_ROLE = [
    "identity-provider",  # Identity Provider.
    "service-provider",  # Service Provider.
]
VALID_BODY_DEFAULT_LOGIN_PAGE = [
    "normal",  # Use local login page as default.
    "sso",  # Use IdP's Single Sign-On page as default.
]
VALID_BODY_BINDING_PROTOCOL = [
    "post",  # HTTP POST binding.
    "redirect",  # HTTP Redirect binding.
]
VALID_BODY_REQUIRE_SIGNED_RESP_AND_ASRT = [
    "enable",  # Both response and assertion must be signed and valid.
    "disable",  # At least one of response or assertion must be signed and valid.
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
    """Validate GET request parameters for system/saml."""
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
    """Validate required fields for system/saml."""
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
    """Validate POST request to create new system/saml object."""
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
    if "require-signed-resp-and-asrt" in payload:
        value = payload["require-signed-resp-and-asrt"]
        if value not in VALID_BODY_REQUIRE_SIGNED_RESP_AND_ASRT:
            desc = FIELD_DESCRIPTIONS.get("require-signed-resp-and-asrt", "")
            error_msg = f"Invalid value for 'require-signed-resp-and-asrt': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_REQUIRE_SIGNED_RESP_AND_ASRT)}"
            error_msg += f"\n  → Example: require-signed-resp-and-asrt='{{ VALID_BODY_REQUIRE_SIGNED_RESP_AND_ASRT[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_system_saml_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update system/saml."""
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
    if "require-signed-resp-and-asrt" in payload:
        value = payload["require-signed-resp-and-asrt"]
        if value not in VALID_BODY_REQUIRE_SIGNED_RESP_AND_ASRT:
            return (
                False,
                f"Invalid value for 'require-signed-resp-and-asrt'='{value}'. Must be one of: {', '.join(VALID_BODY_REQUIRE_SIGNED_RESP_AND_ASRT)}",
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
    "endpoint": "system/saml",
    "category": "cmdb",
    "api_path": "system/saml",
    "help": "Global settings for SAML authentication.",
    "total_fields": 19,
    "required_fields_count": 4,
    "fields_with_defaults_count": 18,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
