"""Validation helpers for extension_controller/extender - Auto-generated"""

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
    "name",  # FortiExtender entry name.
    "id",  # FortiExtender serial number.
    "extension-type",  # Extension type for this FortiExtender.
    "login-password",  # Set the managed extender's administrator password.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "id": "",
    "authorized": "discovered",
    "ext-name": "",
    "description": "",
    "vdom": 1,
    "device-id": 1026,
    "extension-type": "",
    "profile": "",
    "override-allowaccess": "disable",
    "allowaccess": "",
    "override-login-password-change": "disable",
    "login-password-change": "no",
    "override-enforce-bandwidth": "disable",
    "enforce-bandwidth": "disable",
    "bandwidth-limit": 1024,
    "firmware-provision-latest": "disable",
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
    "name": "string",  # FortiExtender entry name.
    "id": "string",  # FortiExtender serial number.
    "authorized": "option",  # FortiExtender Administration (enable or disable).
    "ext-name": "string",  # FortiExtender name.
    "description": "string",  # Description.
    "vdom": "integer",  # VDOM.
    "device-id": "integer",  # Device ID.
    "extension-type": "option",  # Extension type for this FortiExtender.
    "profile": "string",  # FortiExtender profile configuration.
    "override-allowaccess": "option",  # Enable to override the extender profile management access co
    "allowaccess": "option",  # Control management access to the managed extender. Separate 
    "override-login-password-change": "option",  # Enable to override the extender profile login-password (admi
    "login-password-change": "option",  # Change or reset the administrator password of a managed exte
    "login-password": "password",  # Set the managed extender's administrator password.
    "override-enforce-bandwidth": "option",  # Enable to override the extender profile enforce-bandwidth se
    "enforce-bandwidth": "option",  # Enable/disable enforcement of bandwidth on LAN extension int
    "bandwidth-limit": "integer",  # FortiExtender LAN extension bandwidth limit (Mbps).
    "wan-extension": "string",  # FortiExtender wan extension configuration.
    "firmware-provision-latest": "option",  # Enable/disable one-time automatic provisioning of the latest
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "FortiExtender entry name.",
    "id": "FortiExtender serial number.",
    "authorized": "FortiExtender Administration (enable or disable).",
    "ext-name": "FortiExtender name.",
    "description": "Description.",
    "vdom": "VDOM.",
    "device-id": "Device ID.",
    "extension-type": "Extension type for this FortiExtender.",
    "profile": "FortiExtender profile configuration.",
    "override-allowaccess": "Enable to override the extender profile management access configuration.",
    "allowaccess": "Control management access to the managed extender. Separate entries with a space.",
    "override-login-password-change": "Enable to override the extender profile login-password (administrator password) setting.",
    "login-password-change": "Change or reset the administrator password of a managed extender (yes, default, or no, default = no).",
    "login-password": "Set the managed extender's administrator password.",
    "override-enforce-bandwidth": "Enable to override the extender profile enforce-bandwidth setting.",
    "enforce-bandwidth": "Enable/disable enforcement of bandwidth on LAN extension interface.",
    "bandwidth-limit": "FortiExtender LAN extension bandwidth limit (Mbps).",
    "wan-extension": "FortiExtender wan extension configuration.",
    "firmware-provision-latest": "Enable/disable one-time automatic provisioning of the latest firmware version.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 19},
    "id": {"type": "string", "max_length": 19},
    "ext-name": {"type": "string", "max_length": 31},
    "description": {"type": "string", "max_length": 255},
    "vdom": {"type": "integer", "min": 0, "max": 4294967295},
    "device-id": {"type": "integer", "min": 0, "max": 4294967295},
    "profile": {"type": "string", "max_length": 31},
    "bandwidth-limit": {"type": "integer", "min": 1, "max": 16776000},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "wan-extension": {
        "modem1-extension": {
            "type": "string",
            "help": "FortiExtender interface name.",
            "default": "",
            "max_length": 31,
        },
        "modem2-extension": {
            "type": "string",
            "help": "FortiExtender interface name.",
            "default": "",
            "max_length": 31,
        },
        "modem1-pdn1-interface": {
            "type": "string",
            "help": "FortiExtender interface name.",
            "default": "",
            "max_length": 31,
        },
        "modem1-pdn2-interface": {
            "type": "string",
            "help": "FortiExtender interface name.",
            "default": "",
            "max_length": 31,
        },
        "modem1-pdn3-interface": {
            "type": "string",
            "help": "FortiExtender interface name.",
            "default": "",
            "max_length": 31,
        },
        "modem1-pdn4-interface": {
            "type": "string",
            "help": "FortiExtender interface name.",
            "default": "",
            "max_length": 31,
        },
        "modem2-pdn1-interface": {
            "type": "string",
            "help": "FortiExtender interface name.",
            "default": "",
            "max_length": 31,
        },
        "modem2-pdn2-interface": {
            "type": "string",
            "help": "FortiExtender interface name.",
            "default": "",
            "max_length": 31,
        },
        "modem2-pdn3-interface": {
            "type": "string",
            "help": "FortiExtender interface name.",
            "default": "",
            "max_length": 31,
        },
        "modem2-pdn4-interface": {
            "type": "string",
            "help": "FortiExtender interface name.",
            "default": "",
            "max_length": 31,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_AUTHORIZED = [
    "discovered",  # Controller discovered this FortiExtender.
    "disable",  # Controller is configured to not provide service to this FortiExtender.
    "enable",  # Controller is configured to provide service to this FortiExtender.
]
VALID_BODY_EXTENSION_TYPE = [
    "wan-extension",  # FortiExtender WAN extension mode.
    "lan-extension",  # FortiExtender LAN extension mode.
]
VALID_BODY_OVERRIDE_ALLOWACCESS = [
    "enable",  # Override the extender profile management access configuration.
    "disable",  # Use the extender profile management access configuration.
]
VALID_BODY_ALLOWACCESS = [
    "ping",  # PING access.
    "telnet",  # TELNET access.
    "http",  # HTTP access.
    "https",  # HTTPS access.
    "ssh",  # SSH access.
    "snmp",  # SNMP access.
]
VALID_BODY_OVERRIDE_LOGIN_PASSWORD_CHANGE = [
    "enable",  # Override the WTP profile login-password (administrator password) setting.
    "disable",  # Use the the WTP profile login-password (administrator password) setting.
]
VALID_BODY_LOGIN_PASSWORD_CHANGE = [
    "yes",  # Change the managed extender's administrator password. Use the login-password option to set the password.
    "default",  # Keep the managed extender's administrator password set to the factory default.
    "no",  # Do not change the managed extender's administrator password.
]
VALID_BODY_OVERRIDE_ENFORCE_BANDWIDTH = [
    "enable",  # Enable override of FortiExtender profile bandwidth setting.
    "disable",  # Disable override of FortiExtender profile bandwidth setting.
]
VALID_BODY_ENFORCE_BANDWIDTH = [
    "enable",  # Enable to enforce bandwidth limit on LAN extension interface.
    "disable",  # Disable to enforce bandwidth limit on LAN extension interface.
]
VALID_BODY_FIRMWARE_PROVISION_LATEST = [
    "disable",  # Do not automatically provision the latest available firmware.
    "once",  # Automatically attempt a one-time upgrade to the latest available firmware version.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_extension_controller_extender_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for extension_controller/extender."""
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
    """Validate required fields for extension_controller/extender."""
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


def validate_extension_controller_extender_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new extension_controller/extender object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "authorized" in payload:
        value = payload["authorized"]
        if value not in VALID_BODY_AUTHORIZED:
            desc = FIELD_DESCRIPTIONS.get("authorized", "")
            error_msg = f"Invalid value for 'authorized': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTHORIZED)}"
            error_msg += f"\n  → Example: authorized='{{ VALID_BODY_AUTHORIZED[0] }}'"
            return (False, error_msg)
    if "extension-type" in payload:
        value = payload["extension-type"]
        if value not in VALID_BODY_EXTENSION_TYPE:
            desc = FIELD_DESCRIPTIONS.get("extension-type", "")
            error_msg = f"Invalid value for 'extension-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EXTENSION_TYPE)}"
            error_msg += f"\n  → Example: extension-type='{{ VALID_BODY_EXTENSION_TYPE[0] }}'"
            return (False, error_msg)
    if "override-allowaccess" in payload:
        value = payload["override-allowaccess"]
        if value not in VALID_BODY_OVERRIDE_ALLOWACCESS:
            desc = FIELD_DESCRIPTIONS.get("override-allowaccess", "")
            error_msg = f"Invalid value for 'override-allowaccess': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OVERRIDE_ALLOWACCESS)}"
            error_msg += f"\n  → Example: override-allowaccess='{{ VALID_BODY_OVERRIDE_ALLOWACCESS[0] }}'"
            return (False, error_msg)
    if "allowaccess" in payload:
        value = payload["allowaccess"]
        if value not in VALID_BODY_ALLOWACCESS:
            desc = FIELD_DESCRIPTIONS.get("allowaccess", "")
            error_msg = f"Invalid value for 'allowaccess': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ALLOWACCESS)}"
            error_msg += f"\n  → Example: allowaccess='{{ VALID_BODY_ALLOWACCESS[0] }}'"
            return (False, error_msg)
    if "override-login-password-change" in payload:
        value = payload["override-login-password-change"]
        if value not in VALID_BODY_OVERRIDE_LOGIN_PASSWORD_CHANGE:
            desc = FIELD_DESCRIPTIONS.get("override-login-password-change", "")
            error_msg = f"Invalid value for 'override-login-password-change': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OVERRIDE_LOGIN_PASSWORD_CHANGE)}"
            error_msg += f"\n  → Example: override-login-password-change='{{ VALID_BODY_OVERRIDE_LOGIN_PASSWORD_CHANGE[0] }}'"
            return (False, error_msg)
    if "login-password-change" in payload:
        value = payload["login-password-change"]
        if value not in VALID_BODY_LOGIN_PASSWORD_CHANGE:
            desc = FIELD_DESCRIPTIONS.get("login-password-change", "")
            error_msg = f"Invalid value for 'login-password-change': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOGIN_PASSWORD_CHANGE)}"
            error_msg += f"\n  → Example: login-password-change='{{ VALID_BODY_LOGIN_PASSWORD_CHANGE[0] }}'"
            return (False, error_msg)
    if "override-enforce-bandwidth" in payload:
        value = payload["override-enforce-bandwidth"]
        if value not in VALID_BODY_OVERRIDE_ENFORCE_BANDWIDTH:
            desc = FIELD_DESCRIPTIONS.get("override-enforce-bandwidth", "")
            error_msg = f"Invalid value for 'override-enforce-bandwidth': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OVERRIDE_ENFORCE_BANDWIDTH)}"
            error_msg += f"\n  → Example: override-enforce-bandwidth='{{ VALID_BODY_OVERRIDE_ENFORCE_BANDWIDTH[0] }}'"
            return (False, error_msg)
    if "enforce-bandwidth" in payload:
        value = payload["enforce-bandwidth"]
        if value not in VALID_BODY_ENFORCE_BANDWIDTH:
            desc = FIELD_DESCRIPTIONS.get("enforce-bandwidth", "")
            error_msg = f"Invalid value for 'enforce-bandwidth': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ENFORCE_BANDWIDTH)}"
            error_msg += f"\n  → Example: enforce-bandwidth='{{ VALID_BODY_ENFORCE_BANDWIDTH[0] }}'"
            return (False, error_msg)
    if "firmware-provision-latest" in payload:
        value = payload["firmware-provision-latest"]
        if value not in VALID_BODY_FIRMWARE_PROVISION_LATEST:
            desc = FIELD_DESCRIPTIONS.get("firmware-provision-latest", "")
            error_msg = f"Invalid value for 'firmware-provision-latest': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FIRMWARE_PROVISION_LATEST)}"
            error_msg += f"\n  → Example: firmware-provision-latest='{{ VALID_BODY_FIRMWARE_PROVISION_LATEST[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_extension_controller_extender_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update extension_controller/extender."""
    # Step 1: Validate enum values
    if "authorized" in payload:
        value = payload["authorized"]
        if value not in VALID_BODY_AUTHORIZED:
            return (
                False,
                f"Invalid value for 'authorized'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTHORIZED)}",
            )
    if "extension-type" in payload:
        value = payload["extension-type"]
        if value not in VALID_BODY_EXTENSION_TYPE:
            return (
                False,
                f"Invalid value for 'extension-type'='{value}'. Must be one of: {', '.join(VALID_BODY_EXTENSION_TYPE)}",
            )
    if "override-allowaccess" in payload:
        value = payload["override-allowaccess"]
        if value not in VALID_BODY_OVERRIDE_ALLOWACCESS:
            return (
                False,
                f"Invalid value for 'override-allowaccess'='{value}'. Must be one of: {', '.join(VALID_BODY_OVERRIDE_ALLOWACCESS)}",
            )
    if "allowaccess" in payload:
        value = payload["allowaccess"]
        if value not in VALID_BODY_ALLOWACCESS:
            return (
                False,
                f"Invalid value for 'allowaccess'='{value}'. Must be one of: {', '.join(VALID_BODY_ALLOWACCESS)}",
            )
    if "override-login-password-change" in payload:
        value = payload["override-login-password-change"]
        if value not in VALID_BODY_OVERRIDE_LOGIN_PASSWORD_CHANGE:
            return (
                False,
                f"Invalid value for 'override-login-password-change'='{value}'. Must be one of: {', '.join(VALID_BODY_OVERRIDE_LOGIN_PASSWORD_CHANGE)}",
            )
    if "login-password-change" in payload:
        value = payload["login-password-change"]
        if value not in VALID_BODY_LOGIN_PASSWORD_CHANGE:
            return (
                False,
                f"Invalid value for 'login-password-change'='{value}'. Must be one of: {', '.join(VALID_BODY_LOGIN_PASSWORD_CHANGE)}",
            )
    if "override-enforce-bandwidth" in payload:
        value = payload["override-enforce-bandwidth"]
        if value not in VALID_BODY_OVERRIDE_ENFORCE_BANDWIDTH:
            return (
                False,
                f"Invalid value for 'override-enforce-bandwidth'='{value}'. Must be one of: {', '.join(VALID_BODY_OVERRIDE_ENFORCE_BANDWIDTH)}",
            )
    if "enforce-bandwidth" in payload:
        value = payload["enforce-bandwidth"]
        if value not in VALID_BODY_ENFORCE_BANDWIDTH:
            return (
                False,
                f"Invalid value for 'enforce-bandwidth'='{value}'. Must be one of: {', '.join(VALID_BODY_ENFORCE_BANDWIDTH)}",
            )
    if "firmware-provision-latest" in payload:
        value = payload["firmware-provision-latest"]
        if value not in VALID_BODY_FIRMWARE_PROVISION_LATEST:
            return (
                False,
                f"Invalid value for 'firmware-provision-latest'='{value}'. Must be one of: {', '.join(VALID_BODY_FIRMWARE_PROVISION_LATEST)}",
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
    "endpoint": "extension_controller/extender",
    "category": "cmdb",
    "api_path": "extension-controller/extender",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Extender controller configuration.",
    "total_fields": 19,
    "required_fields_count": 4,
    "fields_with_defaults_count": 17,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
