"""Validation helpers for system/external_resource - Auto-generated"""

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
    "name",  # External resource name.
    "resource",  # URL of external resource.
    "interface",  # Specify outgoing interface to reach server.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "uuid": "00000000-0000-0000-0000-000000000000",
    "status": "enable",
    "type": "category",
    "namespace": "",
    "object-array-path": "$.addresses",
    "address-name-field": "$.name",
    "address-data-field": "$.value",
    "address-comment-field": "$.description",
    "update-method": "feed",
    "category": 0,
    "username": "",
    "client-cert-auth": "disable",
    "client-cert": "",
    "resource": "",
    "server-identity-check": "none",
    "refresh-rate": 5,
    "source-ip": "0.0.0.0",
    "source-ip-interface": "",
    "interface-select-method": "auto",
    "interface": "",
    "vrf-select": 0,
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
    "name": "string",  # External resource name.
    "uuid": "uuid",  # Universally Unique Identifier (UUID; automatically assigned 
    "status": "option",  # Enable/disable user resource.
    "type": "option",  # User resource type.
    "namespace": "string",  # Generic external connector address namespace.
    "object-array-path": "string",  # JSON Path to array of generic addresses in resource.
    "address-name-field": "string",  # JSON Path to address name in generic address entry.
    "address-data-field": "string",  # JSON Path to address data in generic address entry.
    "address-comment-field": "string",  # JSON Path to address description in generic address entry.
    "update-method": "option",  # External resource update method.
    "category": "integer",  # User resource category.
    "username": "string",  # HTTP basic authentication user name.
    "password": "varlen_password",  # HTTP basic authentication password.
    "client-cert-auth": "option",  # Enable/disable using client certificate for TLS authenticati
    "client-cert": "string",  # Client certificate name.
    "comments": "var-string",  # Comment.
    "resource": "string",  # URL of external resource.
    "user-agent": "var-string",  # HTTP User-Agent header (default = 'curl/7.58.0').
    "server-identity-check": "option",  # Certificate verification option.
    "refresh-rate": "integer",  # Time interval to refresh external resource (1 - 43200 min, d
    "source-ip": "ipv4-address",  # Source IPv4 address used to communicate with server.
    "source-ip-interface": "string",  # IPv4 Source interface for communication with the server.
    "interface-select-method": "option",  # Specify how to select outgoing interface to reach server.
    "interface": "string",  # Specify outgoing interface to reach server.
    "vrf-select": "integer",  # VRF ID used for connection to server.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "External resource name.",
    "uuid": "Universally Unique Identifier (UUID; automatically assigned but can be manually reset).",
    "status": "Enable/disable user resource.",
    "type": "User resource type.",
    "namespace": "Generic external connector address namespace.",
    "object-array-path": "JSON Path to array of generic addresses in resource.",
    "address-name-field": "JSON Path to address name in generic address entry.",
    "address-data-field": "JSON Path to address data in generic address entry.",
    "address-comment-field": "JSON Path to address description in generic address entry.",
    "update-method": "External resource update method.",
    "category": "User resource category.",
    "username": "HTTP basic authentication user name.",
    "password": "HTTP basic authentication password.",
    "client-cert-auth": "Enable/disable using client certificate for TLS authentication.",
    "client-cert": "Client certificate name.",
    "comments": "Comment.",
    "resource": "URL of external resource.",
    "user-agent": "HTTP User-Agent header (default = 'curl/7.58.0').",
    "server-identity-check": "Certificate verification option.",
    "refresh-rate": "Time interval to refresh external resource (1 - 43200 min, default = 5 min).",
    "source-ip": "Source IPv4 address used to communicate with server.",
    "source-ip-interface": "IPv4 Source interface for communication with the server.",
    "interface-select-method": "Specify how to select outgoing interface to reach server.",
    "interface": "Specify outgoing interface to reach server.",
    "vrf-select": "VRF ID used for connection to server.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 35},
    "namespace": {"type": "string", "max_length": 15},
    "object-array-path": {"type": "string", "max_length": 511},
    "address-name-field": {"type": "string", "max_length": 511},
    "address-data-field": {"type": "string", "max_length": 511},
    "address-comment-field": {"type": "string", "max_length": 511},
    "category": {"type": "integer", "min": 192, "max": 221},
    "username": {"type": "string", "max_length": 64},
    "client-cert": {"type": "string", "max_length": 79},
    "resource": {"type": "string", "max_length": 511},
    "refresh-rate": {"type": "integer", "min": 1, "max": 43200},
    "source-ip-interface": {"type": "string", "max_length": 15},
    "interface": {"type": "string", "max_length": 15},
    "vrf-select": {"type": "integer", "min": 0, "max": 511},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_STATUS = [
    "enable",  # Enable user resource.
    "disable",  # Disable user resource.
]
VALID_BODY_TYPE = [
    "category",  # FortiGuard category.
    "domain",  # Domain Name.
    "malware",  # Malware hash.
    "address",  # Firewall IP address.
    "mac-address",  # Firewall MAC address.
    "data",  # Data file.
    "generic-address",  # Generic addresses.
]
VALID_BODY_UPDATE_METHOD = [
    "feed",  # FortiGate unit will pull update from the external resource.
    "push",  # External Resource update is pushed to the FortiGate unit through the FortiGate unit's RESTAPI/CLI.
]
VALID_BODY_CLIENT_CERT_AUTH = [
    "enable",  # Enable using client certificate for TLS authentication.
    "disable",  # Disable using client certificate for TLS authentication.
]
VALID_BODY_SERVER_IDENTITY_CHECK = [
    "none",  # No certificate verification.
    "basic",  # Check server certifcate only.
    "full",  # Check server certificate and verify the domain matches in the server certificate.
]
VALID_BODY_INTERFACE_SELECT_METHOD = [
    "auto",  # Set outgoing interface automatically.
    "sdwan",  # Set outgoing interface by SD-WAN or policy routing rules.
    "specify",  # Set outgoing interface manually.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_system_external_resource_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for system/external_resource."""
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
    """Validate required fields for system/external_resource."""
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


def validate_system_external_resource_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new system/external_resource object."""
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
    if "type" in payload:
        value = payload["type"]
        if value not in VALID_BODY_TYPE:
            desc = FIELD_DESCRIPTIONS.get("type", "")
            error_msg = f"Invalid value for 'type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TYPE)}"
            error_msg += f"\n  → Example: type='{{ VALID_BODY_TYPE[0] }}'"
            return (False, error_msg)
    if "update-method" in payload:
        value = payload["update-method"]
        if value not in VALID_BODY_UPDATE_METHOD:
            desc = FIELD_DESCRIPTIONS.get("update-method", "")
            error_msg = f"Invalid value for 'update-method': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_UPDATE_METHOD)}"
            error_msg += f"\n  → Example: update-method='{{ VALID_BODY_UPDATE_METHOD[0] }}'"
            return (False, error_msg)
    if "client-cert-auth" in payload:
        value = payload["client-cert-auth"]
        if value not in VALID_BODY_CLIENT_CERT_AUTH:
            desc = FIELD_DESCRIPTIONS.get("client-cert-auth", "")
            error_msg = f"Invalid value for 'client-cert-auth': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CLIENT_CERT_AUTH)}"
            error_msg += f"\n  → Example: client-cert-auth='{{ VALID_BODY_CLIENT_CERT_AUTH[0] }}'"
            return (False, error_msg)
    if "server-identity-check" in payload:
        value = payload["server-identity-check"]
        if value not in VALID_BODY_SERVER_IDENTITY_CHECK:
            desc = FIELD_DESCRIPTIONS.get("server-identity-check", "")
            error_msg = f"Invalid value for 'server-identity-check': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SERVER_IDENTITY_CHECK)}"
            error_msg += f"\n  → Example: server-identity-check='{{ VALID_BODY_SERVER_IDENTITY_CHECK[0] }}'"
            return (False, error_msg)
    if "interface-select-method" in payload:
        value = payload["interface-select-method"]
        if value not in VALID_BODY_INTERFACE_SELECT_METHOD:
            desc = FIELD_DESCRIPTIONS.get("interface-select-method", "")
            error_msg = f"Invalid value for 'interface-select-method': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_INTERFACE_SELECT_METHOD)}"
            error_msg += f"\n  → Example: interface-select-method='{{ VALID_BODY_INTERFACE_SELECT_METHOD[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_system_external_resource_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update system/external_resource."""
    # Step 1: Validate enum values
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid value for 'status'='{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )
    if "type" in payload:
        value = payload["type"]
        if value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid value for 'type'='{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )
    if "update-method" in payload:
        value = payload["update-method"]
        if value not in VALID_BODY_UPDATE_METHOD:
            return (
                False,
                f"Invalid value for 'update-method'='{value}'. Must be one of: {', '.join(VALID_BODY_UPDATE_METHOD)}",
            )
    if "client-cert-auth" in payload:
        value = payload["client-cert-auth"]
        if value not in VALID_BODY_CLIENT_CERT_AUTH:
            return (
                False,
                f"Invalid value for 'client-cert-auth'='{value}'. Must be one of: {', '.join(VALID_BODY_CLIENT_CERT_AUTH)}",
            )
    if "server-identity-check" in payload:
        value = payload["server-identity-check"]
        if value not in VALID_BODY_SERVER_IDENTITY_CHECK:
            return (
                False,
                f"Invalid value for 'server-identity-check'='{value}'. Must be one of: {', '.join(VALID_BODY_SERVER_IDENTITY_CHECK)}",
            )
    if "interface-select-method" in payload:
        value = payload["interface-select-method"]
        if value not in VALID_BODY_INTERFACE_SELECT_METHOD:
            return (
                False,
                f"Invalid value for 'interface-select-method'='{value}'. Must be one of: {', '.join(VALID_BODY_INTERFACE_SELECT_METHOD)}",
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
    "endpoint": "system/external_resource",
    "category": "cmdb",
    "api_path": "system/external-resource",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure external resource.",
    "total_fields": 25,
    "required_fields_count": 3,
    "fields_with_defaults_count": 22,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
