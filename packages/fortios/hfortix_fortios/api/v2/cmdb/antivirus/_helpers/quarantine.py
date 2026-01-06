"""
Validation helpers for antivirus/quarantine endpoint.

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
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "agelimit": 0,
    "maxfilesize": 0,
    "quarantine-quota": 0,
    "drop-infected": "",
    "store-infected": "imap smtp pop3 http ftp nntp imaps smtps pop3s https ftps mapi cifs ssh",
    "drop-machine-learning": "",
    "store-machine-learning": "imap smtp pop3 http ftp nntp imaps smtps pop3s https ftps mapi cifs ssh",
    "lowspace": "ovrw-old",
    "destination": "disk",
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
    "agelimit": "integer",  # Age limit for quarantined files (0 - 479 hours, 0 means fore
    "maxfilesize": "integer",  # Maximum file size to quarantine (0 - 500 Mbytes, 0 means unl
    "quarantine-quota": "integer",  # The amount of disk space to reserve for quarantining files (
    "drop-infected": "option",  # Do not quarantine infected files found in sessions using the
    "store-infected": "option",  # Quarantine infected files found in sessions using the select
    "drop-machine-learning": "option",  # Do not quarantine files detected by machine learning found i
    "store-machine-learning": "option",  # Quarantine files detected by machine learning found in sessi
    "lowspace": "option",  # Select the method for handling additional files when running
    "destination": "option",  # Choose whether to quarantine files to the FortiGate disk or 
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "agelimit": "Age limit for quarantined files (0 - 479 hours, 0 means forever).",
    "maxfilesize": "Maximum file size to quarantine (0 - 500 Mbytes, 0 means unlimited).",
    "quarantine-quota": "The amount of disk space to reserve for quarantining files (0 - 4294967295 Mbytes, 0 means unlimited and depends on disk space).",
    "drop-infected": "Do not quarantine infected files found in sessions using the selected protocols. Dropped files are deleted instead of being quarantined.",
    "store-infected": "Quarantine infected files found in sessions using the selected protocols.",
    "drop-machine-learning": "Do not quarantine files detected by machine learning found in sessions using the selected protocols. Dropped files are deleted instead of being quarantined.",
    "store-machine-learning": "Quarantine files detected by machine learning found in sessions using the selected protocols.",
    "lowspace": "Select the method for handling additional files when running low on disk space.",
    "destination": "Choose whether to quarantine files to the FortiGate disk or to FortiAnalyzer or to delete them instead of quarantining them.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "agelimit": {"type": "integer", "min": 0, "max": 479},
    "maxfilesize": {"type": "integer", "min": 0, "max": 500},
    "quarantine-quota": {"type": "integer", "min": 0, "max": 4294967295},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_DROP_INFECTED = [
    "imap",  # IMAP.
    "smtp",  # SMTP.
    "pop3",  # POP3.
    "http",  # HTTP.
    "ftp",  # FTP.
    "nntp",  # NNTP.
    "imaps",  # IMAPS.
    "smtps",  # SMTPS.
    "pop3s",  # POP3S.
    "https",  # HTTPS.
    "ftps",  # FTPS.
    "mapi",  # MAPI.
    "cifs",  # CIFS.
    "ssh",  # SSH.
]
VALID_BODY_STORE_INFECTED = [
    "imap",  # IMAP.
    "smtp",  # SMTP.
    "pop3",  # POP3.
    "http",  # HTTP.
    "ftp",  # FTP.
    "nntp",  # NNTP.
    "imaps",  # IMAPS.
    "smtps",  # SMTPS.
    "pop3s",  # POP3S.
    "https",  # HTTPS.
    "ftps",  # FTPS.
    "mapi",  # MAPI.
    "cifs",  # CIFS.
    "ssh",  # SSH.
]
VALID_BODY_DROP_MACHINE_LEARNING = [
    "imap",  # IMAP.
    "smtp",  # SMTP.
    "pop3",  # POP3.
    "http",  # HTTP.
    "ftp",  # FTP.
    "nntp",  # NNTP.
    "imaps",  # IMAPS.
    "smtps",  # SMTPS.
    "pop3s",  # POP3S.
    "https",  # HTTPS.
    "ftps",  # FTPS.
    "mapi",  # MAPI.
    "cifs",  # CIFS.
    "ssh",  # SSH.
]
VALID_BODY_STORE_MACHINE_LEARNING = [
    "imap",  # IMAP.
    "smtp",  # SMTP.
    "pop3",  # POP3.
    "http",  # HTTP.
    "ftp",  # FTP.
    "nntp",  # NNTP.
    "imaps",  # IMAPS.
    "smtps",  # SMTPS.
    "pop3s",  # POP3S.
    "https",  # HTTPS.
    "ftps",  # FTPS.
    "mapi",  # MAPI.
    "cifs",  # CIFS.
    "ssh",  # SSH.
]
VALID_BODY_LOWSPACE = [
    "drop-new",  # Drop (delete) the most recently quarantined files.
    "ovrw-old",  # Overwrite the oldest quarantined files. That is, the files that are closest to being deleted from the quarantine.
]
VALID_BODY_DESTINATION = [
    "NULL",  # Files that would be quarantined are deleted.
    "disk",  # Quarantine files to the FortiGate hard disk.
    "FortiAnalyzer",  # FortiAnalyzer
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_antivirus_quarantine_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for antivirus/quarantine.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_antivirus_quarantine_get()
        >>> assert is_valid == True
        
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_antivirus_quarantine_get(
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
    Validate required fields for antivirus/quarantine.

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


def validate_antivirus_quarantine_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new antivirus/quarantine object.

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
        ... }
        >>> is_valid, error = validate_antivirus_quarantine_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "drop-infected": "{'name': 'imap', 'help': 'IMAP.', 'label': 'Imap', 'description': 'IMAP'}",  # Valid enum value
        ... }
        >>> is_valid, error = validate_antivirus_quarantine_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["drop-infected"] = "invalid-value"
        >>> is_valid, error = validate_antivirus_quarantine_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_antivirus_quarantine_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "drop-infected" in payload:
        value = payload["drop-infected"]
        if value not in VALID_BODY_DROP_INFECTED:
            desc = FIELD_DESCRIPTIONS.get("drop-infected", "")
            error_msg = f"Invalid value for 'drop-infected': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DROP_INFECTED)}"
            error_msg += f"\n  → Example: drop-infected='{{ VALID_BODY_DROP_INFECTED[0] }}'"
            return (False, error_msg)
    if "store-infected" in payload:
        value = payload["store-infected"]
        if value not in VALID_BODY_STORE_INFECTED:
            desc = FIELD_DESCRIPTIONS.get("store-infected", "")
            error_msg = f"Invalid value for 'store-infected': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_STORE_INFECTED)}"
            error_msg += f"\n  → Example: store-infected='{{ VALID_BODY_STORE_INFECTED[0] }}'"
            return (False, error_msg)
    if "drop-machine-learning" in payload:
        value = payload["drop-machine-learning"]
        if value not in VALID_BODY_DROP_MACHINE_LEARNING:
            desc = FIELD_DESCRIPTIONS.get("drop-machine-learning", "")
            error_msg = f"Invalid value for 'drop-machine-learning': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DROP_MACHINE_LEARNING)}"
            error_msg += f"\n  → Example: drop-machine-learning='{{ VALID_BODY_DROP_MACHINE_LEARNING[0] }}'"
            return (False, error_msg)
    if "store-machine-learning" in payload:
        value = payload["store-machine-learning"]
        if value not in VALID_BODY_STORE_MACHINE_LEARNING:
            desc = FIELD_DESCRIPTIONS.get("store-machine-learning", "")
            error_msg = f"Invalid value for 'store-machine-learning': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_STORE_MACHINE_LEARNING)}"
            error_msg += f"\n  → Example: store-machine-learning='{{ VALID_BODY_STORE_MACHINE_LEARNING[0] }}'"
            return (False, error_msg)
    if "lowspace" in payload:
        value = payload["lowspace"]
        if value not in VALID_BODY_LOWSPACE:
            desc = FIELD_DESCRIPTIONS.get("lowspace", "")
            error_msg = f"Invalid value for 'lowspace': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOWSPACE)}"
            error_msg += f"\n  → Example: lowspace='{{ VALID_BODY_LOWSPACE[0] }}'"
            return (False, error_msg)
    if "destination" in payload:
        value = payload["destination"]
        if value not in VALID_BODY_DESTINATION:
            desc = FIELD_DESCRIPTIONS.get("destination", "")
            error_msg = f"Invalid value for 'destination': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DESTINATION)}"
            error_msg += f"\n  → Example: destination='{{ VALID_BODY_DESTINATION[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_antivirus_quarantine_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update antivirus/quarantine.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_antivirus_quarantine_put(payload)
    """
    # Step 1: Validate enum values
    if "drop-infected" in payload:
        value = payload["drop-infected"]
        if value not in VALID_BODY_DROP_INFECTED:
            return (
                False,
                f"Invalid value for 'drop-infected'='{value}'. Must be one of: {', '.join(VALID_BODY_DROP_INFECTED)}",
            )
    if "store-infected" in payload:
        value = payload["store-infected"]
        if value not in VALID_BODY_STORE_INFECTED:
            return (
                False,
                f"Invalid value for 'store-infected'='{value}'. Must be one of: {', '.join(VALID_BODY_STORE_INFECTED)}",
            )
    if "drop-machine-learning" in payload:
        value = payload["drop-machine-learning"]
        if value not in VALID_BODY_DROP_MACHINE_LEARNING:
            return (
                False,
                f"Invalid value for 'drop-machine-learning'='{value}'. Must be one of: {', '.join(VALID_BODY_DROP_MACHINE_LEARNING)}",
            )
    if "store-machine-learning" in payload:
        value = payload["store-machine-learning"]
        if value not in VALID_BODY_STORE_MACHINE_LEARNING:
            return (
                False,
                f"Invalid value for 'store-machine-learning'='{value}'. Must be one of: {', '.join(VALID_BODY_STORE_MACHINE_LEARNING)}",
            )
    if "lowspace" in payload:
        value = payload["lowspace"]
        if value not in VALID_BODY_LOWSPACE:
            return (
                False,
                f"Invalid value for 'lowspace'='{value}'. Must be one of: {', '.join(VALID_BODY_LOWSPACE)}",
            )
    if "destination" in payload:
        value = payload["destination"]
        if value not in VALID_BODY_DESTINATION:
            return (
                False,
                f"Invalid value for 'destination'='{value}'. Must be one of: {', '.join(VALID_BODY_DESTINATION)}",
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
    # Replace all non-alphanumeric characters with underscores for valid Python identifiers
    import re
    safe_name = re.sub(r'[^a-zA-Z0-9]', '_', field_name)
    constant_name = f"VALID_BODY_{safe_name.upper()}"
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
    "endpoint": "antivirus/quarantine",
    "category": "cmdb",
    "api_path": "antivirus/quarantine",
    "help": "Configure quarantine options.",
    "total_fields": 9,
    "required_fields_count": 0,
    "fields_with_defaults_count": 9,
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
