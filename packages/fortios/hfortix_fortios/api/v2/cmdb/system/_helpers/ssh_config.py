"""Validation helpers for system/ssh_config - Auto-generated"""

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
    "ssh-hsk",  # Config SSH host key.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "ssh-kex-algo": "diffie-hellman-group14-sha256 diffie-hellman-group16-sha512 diffie-hellman-group18-sha512 diffie-hellman-group-exchange-sha256 curve25519-sha256@libssh.org ecdh-sha2-nistp256 ecdh-sha2-nistp384 ecdh-sha2-nistp521",
    "ssh-enc-algo": "aes256-ctr aes256-gcm@openssh.com",
    "ssh-mac-algo": "hmac-sha2-256 hmac-sha2-256-etm@openssh.com hmac-sha2-512 hmac-sha2-512-etm@openssh.com",
    "ssh-hsk-algo": "ecdsa-sha2-nistp521 ecdsa-sha2-nistp384 ecdsa-sha2-nistp256 rsa-sha2-256 rsa-sha2-512 ssh-ed25519",
    "ssh-hsk-override": "disable",
    "ssh-hsk": "",
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
    "ssh-kex-algo": "option",  # Select one or more SSH kex algorithms.
    "ssh-enc-algo": "option",  # Select one or more SSH ciphers.
    "ssh-mac-algo": "option",  # Select one or more SSH MAC algorithms.
    "ssh-hsk-algo": "option",  # Select one or more SSH hostkey algorithms.
    "ssh-hsk-override": "option",  # Enable/disable SSH host key override in SSH daemon.
    "ssh-hsk-password": "password",  # Password for ssh-hostkey.
    "ssh-hsk": "user",  # Config SSH host key.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "ssh-kex-algo": "Select one or more SSH kex algorithms.",
    "ssh-enc-algo": "Select one or more SSH ciphers.",
    "ssh-mac-algo": "Select one or more SSH MAC algorithms.",
    "ssh-hsk-algo": "Select one or more SSH hostkey algorithms.",
    "ssh-hsk-override": "Enable/disable SSH host key override in SSH daemon.",
    "ssh-hsk-password": "Password for ssh-hostkey.",
    "ssh-hsk": "Config SSH host key.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_SSH_KEX_ALGO = [
    "diffie-hellman-group1-sha1",  # diffie-hellman-group1-sha1
    "diffie-hellman-group14-sha1",  # diffie-hellman-group14-sha1
    "diffie-hellman-group14-sha256",  # diffie-hellman-group14-sha256
    "diffie-hellman-group16-sha512",  # diffie-hellman-group16-sha512
    "diffie-hellman-group18-sha512",  # diffie-hellman-group18-sha512
    "diffie-hellman-group-exchange-sha1",  # diffie-hellman-group-exchange-sha1
    "diffie-hellman-group-exchange-sha256",  # diffie-hellman-group-exchange-sha256
    "curve25519-sha256@libssh.org",  # curve25519-sha256@libssh.org
    "ecdh-sha2-nistp256",  # ecdh-sha2-nistp256
    "ecdh-sha2-nistp384",  # ecdh-sha2-nistp384
    "ecdh-sha2-nistp521",  # ecdh-sha2-nistp521
]
VALID_BODY_SSH_ENC_ALGO = [
    "chacha20-poly1305@openssh.com",  # chacha20-poly1305@openssh.com
    "aes128-ctr",  # aes128-ctr
    "aes192-ctr",  # aes192-ctr
    "aes256-ctr",  # aes256-ctr
    "arcfour256",  # arcfour256
    "arcfour128",  # arcfour128
    "aes128-cbc",  # aes128-cbc
    "3des-cbc",  # 3des-cbc
    "blowfish-cbc",  # blowfish-cbc
    "cast128-cbc",  # cast128-cbc
    "aes192-cbc",  # aes192-cbc
    "aes256-cbc",  # aes256-cbc
    "arcfour",  # arcfour
    "rijndael-cbc@lysator.liu.se",  # rijndael-cbc@lysator.liu.se
    "aes128-gcm@openssh.com",  # aes128-gcm@openssh.com
    "aes256-gcm@openssh.com",  # aes256-gcm@openssh.com
]
VALID_BODY_SSH_MAC_ALGO = [
    "hmac-md5",  # hmac-md5
    "hmac-md5-etm@openssh.com",  # hmac-md5-etm@openssh.com
    "hmac-md5-96",  # hmac-md5-96
    "hmac-md5-96-etm@openssh.com",  # hmac-md5-96-etm@openssh.com
    "hmac-sha1",  # hmac-sha1
    "hmac-sha1-etm@openssh.com",  # hmac-sha1-etm@openssh.com
    "hmac-sha2-256",  # hmac-sha2-256
    "hmac-sha2-256-etm@openssh.com",  # hmac-sha2-256-etm@openssh.com
    "hmac-sha2-512",  # hmac-sha2-512
    "hmac-sha2-512-etm@openssh.com",  # hmac-sha2-512-etm@openssh.com
    "hmac-ripemd160",  # hmac-ripemd160
    "hmac-ripemd160@openssh.com",  # hmac-ripemd160@openssh.com
    "hmac-ripemd160-etm@openssh.com",  # hmac-ripemd160-etm@openssh.com
    "umac-64@openssh.com",  # umac-64@openssh.com
    "umac-128@openssh.com",  # umac-128@openssh.com
    "umac-64-etm@openssh.com",  # umac-64-etm@openssh.com
    "umac-128-etm@openssh.com",  # umac-128-etm@openssh.com
]
VALID_BODY_SSH_HSK_ALGO = [
    "ssh-rsa",  # ssh-rsa
    "ecdsa-sha2-nistp521",  # ecdsa-sha2-nistp521
    "ecdsa-sha2-nistp384",  # ecdsa-sha2-nistp384
    "ecdsa-sha2-nistp256",  # ecdsa-sha2-nistp256
    "rsa-sha2-256",  # rsa-sha2-256
    "rsa-sha2-512",  # rsa-sha2-512
    "ssh-ed25519",  # ssh-ed25519
]
VALID_BODY_SSH_HSK_OVERRIDE = [
    "disable",  # Disable SSH host key override in SSH daemon.
    "enable",  # Enable SSH host key override in SSH daemon.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_system_ssh_config_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for system/ssh_config."""
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
    """Validate required fields for system/ssh_config."""
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


def validate_system_ssh_config_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new system/ssh_config object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "ssh-kex-algo" in payload:
        value = payload["ssh-kex-algo"]
        if value not in VALID_BODY_SSH_KEX_ALGO:
            desc = FIELD_DESCRIPTIONS.get("ssh-kex-algo", "")
            error_msg = f"Invalid value for 'ssh-kex-algo': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSH_KEX_ALGO)}"
            error_msg += f"\n  → Example: ssh-kex-algo='{{ VALID_BODY_SSH_KEX_ALGO[0] }}'"
            return (False, error_msg)
    if "ssh-enc-algo" in payload:
        value = payload["ssh-enc-algo"]
        if value not in VALID_BODY_SSH_ENC_ALGO:
            desc = FIELD_DESCRIPTIONS.get("ssh-enc-algo", "")
            error_msg = f"Invalid value for 'ssh-enc-algo': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSH_ENC_ALGO)}"
            error_msg += f"\n  → Example: ssh-enc-algo='{{ VALID_BODY_SSH_ENC_ALGO[0] }}'"
            return (False, error_msg)
    if "ssh-mac-algo" in payload:
        value = payload["ssh-mac-algo"]
        if value not in VALID_BODY_SSH_MAC_ALGO:
            desc = FIELD_DESCRIPTIONS.get("ssh-mac-algo", "")
            error_msg = f"Invalid value for 'ssh-mac-algo': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSH_MAC_ALGO)}"
            error_msg += f"\n  → Example: ssh-mac-algo='{{ VALID_BODY_SSH_MAC_ALGO[0] }}'"
            return (False, error_msg)
    if "ssh-hsk-algo" in payload:
        value = payload["ssh-hsk-algo"]
        if value not in VALID_BODY_SSH_HSK_ALGO:
            desc = FIELD_DESCRIPTIONS.get("ssh-hsk-algo", "")
            error_msg = f"Invalid value for 'ssh-hsk-algo': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSH_HSK_ALGO)}"
            error_msg += f"\n  → Example: ssh-hsk-algo='{{ VALID_BODY_SSH_HSK_ALGO[0] }}'"
            return (False, error_msg)
    if "ssh-hsk-override" in payload:
        value = payload["ssh-hsk-override"]
        if value not in VALID_BODY_SSH_HSK_OVERRIDE:
            desc = FIELD_DESCRIPTIONS.get("ssh-hsk-override", "")
            error_msg = f"Invalid value for 'ssh-hsk-override': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSH_HSK_OVERRIDE)}"
            error_msg += f"\n  → Example: ssh-hsk-override='{{ VALID_BODY_SSH_HSK_OVERRIDE[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_system_ssh_config_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update system/ssh_config."""
    # Step 1: Validate enum values
    if "ssh-kex-algo" in payload:
        value = payload["ssh-kex-algo"]
        if value not in VALID_BODY_SSH_KEX_ALGO:
            return (
                False,
                f"Invalid value for 'ssh-kex-algo'='{value}'. Must be one of: {', '.join(VALID_BODY_SSH_KEX_ALGO)}",
            )
    if "ssh-enc-algo" in payload:
        value = payload["ssh-enc-algo"]
        if value not in VALID_BODY_SSH_ENC_ALGO:
            return (
                False,
                f"Invalid value for 'ssh-enc-algo'='{value}'. Must be one of: {', '.join(VALID_BODY_SSH_ENC_ALGO)}",
            )
    if "ssh-mac-algo" in payload:
        value = payload["ssh-mac-algo"]
        if value not in VALID_BODY_SSH_MAC_ALGO:
            return (
                False,
                f"Invalid value for 'ssh-mac-algo'='{value}'. Must be one of: {', '.join(VALID_BODY_SSH_MAC_ALGO)}",
            )
    if "ssh-hsk-algo" in payload:
        value = payload["ssh-hsk-algo"]
        if value not in VALID_BODY_SSH_HSK_ALGO:
            return (
                False,
                f"Invalid value for 'ssh-hsk-algo'='{value}'. Must be one of: {', '.join(VALID_BODY_SSH_HSK_ALGO)}",
            )
    if "ssh-hsk-override" in payload:
        value = payload["ssh-hsk-override"]
        if value not in VALID_BODY_SSH_HSK_OVERRIDE:
            return (
                False,
                f"Invalid value for 'ssh-hsk-override'='{value}'. Must be one of: {', '.join(VALID_BODY_SSH_HSK_OVERRIDE)}",
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
    "endpoint": "system/ssh_config",
    "category": "cmdb",
    "api_path": "system/ssh-config",
    "help": "Configure SSH config.",
    "total_fields": 7,
    "required_fields_count": 1,
    "fields_with_defaults_count": 6,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
