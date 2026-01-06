"""
Validation helpers for ztna/web_portal_bookmark endpoint.

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
    "name": "",
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
    "name": "string",  # Bookmark name.
    "users": "string",  # User name.
    "groups": "string",  # User groups.
    "bookmarks": "string",  # Bookmark table.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Bookmark name.",
    "users": "User name.",
    "groups": "User groups.",
    "bookmarks": "Bookmark table.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 35},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "users": {
        "name": {
            "type": "string",
            "help": "User name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "groups": {
        "name": {
            "type": "string",
            "help": "Group name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "bookmarks": {
        "name": {
            "type": "string",
            "help": "Bookmark name.",
            "default": "",
            "max_length": 35,
        },
        "apptype": {
            "type": "option",
            "help": "Application type.",
            "required": True,
            "default": "web",
            "options": [{"help": "FTP.", "label": "Ftp", "name": "ftp"}, {"help": "RDP.", "label": "Rdp", "name": "rdp"}, {"help": "SFTP.", "label": "Sftp", "name": "sftp"}, {"help": "SMB/CIFS.", "label": "Smb", "name": "smb"}, {"help": "SSH.", "label": "Ssh", "name": "ssh"}, {"help": "Telnet.", "label": "Telnet", "name": "telnet"}, {"help": "VNC.", "label": "Vnc", "name": "vnc"}, {"help": "HTTP/HTTPS.", "label": "Web", "name": "web"}],
        },
        "url": {
            "type": "var-string",
            "help": "URL parameter.",
            "required": True,
            "max_length": 128,
        },
        "host": {
            "type": "var-string",
            "help": "Host name/IP parameter.",
            "required": True,
            "max_length": 128,
        },
        "folder": {
            "type": "var-string",
            "help": "Network shared file folder parameter.",
            "required": True,
            "max_length": 128,
        },
        "domain": {
            "type": "var-string",
            "help": "Login domain.",
            "max_length": 128,
        },
        "description": {
            "type": "var-string",
            "help": "Description.",
            "max_length": 128,
        },
        "keyboard-layout": {
            "type": "option",
            "help": "Keyboard layout.",
            "default": "en-us",
            "options": [{"help": "Arabic (101).", "label": "Ar 101", "name": "ar-101"}, {"help": "Arabic (102).", "label": "Ar 102", "name": "ar-102"}, {"help": "Arabic (102) AZERTY.", "label": "Ar 102 Azerty", "name": "ar-102-azerty"}, {"help": "Canadian Multilingual Standard.", "label": "Can Mul", "name": "can-mul"}, {"help": "Czech.", "label": "Cz", "name": "cz"}, {"help": "Czech (QWERTY).", "label": "Cz Qwerty", "name": "cz-qwerty"}, {"help": "Czech Programmers.", "label": "Cz Pr", "name": "cz-pr"}, {"help": "Danish.", "label": "Da", "name": "da"}, {"help": "Dutch.", "label": "Nl", "name": "nl"}, {"help": "German.", "label": "De", "name": "de"}, {"help": "German, Switzerland.", "label": "De Ch", "name": "de-ch"}, {"help": "German (IBM).", "label": "De Ibm", "name": "de-ibm"}, {"help": "English, United Kingdom.", "label": "En Uk", "name": "en-uk"}, {"help": "English, United Kingdom Extended.", "label": "En Uk Ext", "name": "en-uk-ext"}, {"help": "English, United States.", "label": "En Us", "name": "en-us"}, {"help": "English, United States-Dvorak.", "label": "En Us Dvorak", "name": "en-us-dvorak"}, {"help": "Spanish.", "label": "Es", "name": "es"}, {"help": "Spanish Variation.", "label": "Es Var", "name": "es-var"}, {"help": "Finnish.", "label": "Fi", "name": "fi"}, {"help": "Finnish with Sami.", "label": "Fi Sami", "name": "fi-sami"}, {"help": "French.", "label": "Fr", "name": "fr"}, {"help": "French, Apple.", "label": "Fr Apple", "name": "fr-apple"}, {"help": "French, Canada.", "label": "Fr Ca", "name": "fr-ca"}, {"help": "French, Switzerland.", "label": "Fr Ch", "name": "fr-ch"}, {"help": "French, Belgium.", "label": "Fr Be", "name": "fr-be"}, {"help": "Croatian.", "label": "Hr", "name": "hr"}, {"help": "Hungarian.", "label": "Hu", "name": "hu"}, {"help": "Hungarian 101-Key.", "label": "Hu 101", "name": "hu-101"}, {"help": "Italian.", "label": "It", "name": "it"}, {"help": "Italian (142).", "label": "It 142", "name": "it-142"}, {"help": "Japanese.", "label": "Ja", "name": "ja"}, {"help": "Japanese 106/109 key.", "label": "Ja 106", "name": "ja-106"}, {"help": "Korean.", "label": "Ko", "name": "ko"}, {"help": "Latin American.", "label": "La Am", "name": "la-am"}, {"help": "Lithuanian.", "label": "Lt", "name": "lt"}, {"help": "Lithuanian IBM.", "label": "Lt Ibm", "name": "lt-ibm"}, {"help": "Lithuanian Standard.", "label": "Lt Std", "name": "lt-std"}, {"help": "Latvian (Standard).", "label": "Lav Std", "name": "lav-std"}, {"help": "Latvian (Legacy).", "label": "Lav Leg", "name": "lav-leg"}, {"help": "Macedonian (FYROM).", "label": "Mk", "name": "mk"}, {"help": "Macedonia (FYROM) - Standard.", "label": "Mk Std", "name": "mk-std"}, {"help": "Norwegian.", "label": "No", "name": "no"}, {"help": "Norwegian with Sami.", "label": "No Sami", "name": "no-sami"}, {"help": "Polish (214).", "label": "Pol 214", "name": "pol-214"}, {"help": "Polish (Programmers).", "label": "Pol Pr", "name": "pol-pr"}, {"help": "Portuguese.", "label": "Pt", "name": "pt"}, {"help": "Portuguese (Brazilian ABNT).", "label": "Pt Br", "name": "pt-br"}, {"help": "Portuguese (Brazilian ABNT2).", "label": "Pt Br Abnt2", "name": "pt-br-abnt2"}, {"help": "Russian.", "label": "Ru", "name": "ru"}, {"help": "Russian - Mnemonic.", "label": "Ru Mne", "name": "ru-mne"}, {"help": "Russian (Typewriter).", "label": "Ru T", "name": "ru-t"}, {"help": "Slovenian.", "label": "Sl", "name": "sl"}, {"help": "Swedish.", "label": "Sv", "name": "sv"}, {"help": "Swedish with Sami.", "label": "Sv Sami", "name": "sv-sami"}, {"help": "Turkmen.", "label": "Tuk", "name": "tuk"}, {"help": "Turkish F.", "label": "Tur F", "name": "tur-f"}, {"help": "Turkish Q.", "label": "Tur Q", "name": "tur-q"}, {"help": "Chinese (Simplified, Singapore) - US keyboard.", "label": "Zh Sym Sg Us", "name": "zh-sym-sg-us"}, {"help": "Chinese (Simplified) - US Keyboard.", "label": "Zh Sym Us", "name": "zh-sym-us"}, {"help": "Chinese (Traditional, Hong Kong S.A.R.).", "label": "Zh Tr Hk", "name": "zh-tr-hk"}, {"help": "Chinese (Traditional Macao S.A.R.) - US Keyboard.", "label": "Zh Tr Mo", "name": "zh-tr-mo"}, {"help": "Chinese (Traditional) - US keyboard.", "label": "Zh Tr Us", "name": "zh-tr-us"}],
        },
        "security": {
            "type": "option",
            "help": "Security mode for RDP connection (default = any).",
            "default": "any",
            "options": [{"help": "Allow the server to choose the type of security.", "label": "Any", "name": "any"}, {"help": "Standard RDP encryption.", "label": "Rdp", "name": "rdp"}, {"help": "Network Level Authentication.", "label": "Nla", "name": "nla"}, {"help": "TLS encryption.", "label": "Tls", "name": "tls"}],
        },
        "send-preconnection-id": {
            "type": "option",
            "help": "Enable/disable sending of preconnection ID.",
            "default": "disable",
            "options": [{"help": "Enable sending of preconnection ID.", "label": "Enable", "name": "enable"}, {"help": "Disable sending of preconnection ID.", "label": "Disable", "name": "disable"}],
        },
        "preconnection-id": {
            "type": "integer",
            "help": "The numeric ID of the RDP source (0-4294967295).",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "preconnection-blob": {
            "type": "var-string",
            "help": "An arbitrary string which identifies the RDP source.",
            "max_length": 511,
        },
        "load-balancing-info": {
            "type": "var-string",
            "help": "The load balancing information or cookie which should be provided to the connection broker.",
            "max_length": 511,
        },
        "restricted-admin": {
            "type": "option",
            "help": "Enable/disable restricted admin mode for RDP.",
            "default": "disable",
            "options": [{"help": "Enable restricted admin mode for RDP.", "label": "Enable", "name": "enable"}, {"help": "Disable restricted admin mode for RDP.", "label": "Disable", "name": "disable"}],
        },
        "port": {
            "type": "integer",
            "help": "Remote port.",
            "default": 0,
            "min_value": 0,
            "max_value": 65535,
        },
        "logon-user": {
            "type": "var-string",
            "help": "Logon user.",
            "max_length": 35,
        },
        "logon-password": {
            "type": "password",
            "help": "Logon password.",
            "max_length": 128,
        },
        "color-depth": {
            "type": "option",
            "help": "Color depth per pixel.",
            "default": "16",
            "options": [{"help": "32bits per pixel.", "label": "32", "name": "32"}, {"help": "16bits per pixel.", "label": "16", "name": "16"}, {"help": "8bits per pixel.", "label": "8", "name": "8"}],
        },
        "sso": {
            "type": "option",
            "help": "Single sign-on.",
            "default": "disable",
            "options": [{"help": "Disable SSO.", "label": "Disable", "name": "disable"}, {"help": "Enable SSO.", "label": "Enable", "name": "enable"}],
        },
        "width": {
            "type": "integer",
            "help": "Screen width (range from 0 - 65535, default = 0).",
            "default": 0,
            "min_value": 0,
            "max_value": 65535,
        },
        "height": {
            "type": "integer",
            "help": "Screen height (range from 0 - 65535, default = 0).",
            "default": 0,
            "min_value": 0,
            "max_value": 65535,
        },
        "vnc-keyboard-layout": {
            "type": "option",
            "help": "Keyboard layout.",
            "default": "default",
            "options": [{"help": "Default.", "label": "Default", "name": "default"}, {"help": "Danish.", "label": "Da", "name": "da"}, {"help": "Dutch.", "label": "Nl", "name": "nl"}, {"help": "English, United Kingdom.", "label": "En Uk", "name": "en-uk"}, {"help": "English, United Kingdom Extended.", "label": "En Uk Ext", "name": "en-uk-ext"}, {"help": "Finnish.", "label": "Fi", "name": "fi"}, {"help": "French.", "label": "Fr", "name": "fr"}, {"help": "French, Belgium.", "label": "Fr Be", "name": "fr-be"}, {"help": "French, Canadian Multilingual Std.", "label": "Fr Ca Mul", "name": "fr-ca-mul"}, {"help": "German.", "label": "De", "name": "de"}, {"help": "German, Switzerland.", "label": "De Ch", "name": "de-ch"}, {"help": "Italian.", "label": "It", "name": "it"}, {"help": "Italian (142).", "label": "It 142", "name": "it-142"}, {"help": "Portuguese.", "label": "Pt", "name": "pt"}, {"help": "Portuguese (Brazilian ABNT2).", "label": "Pt Br Abnt2", "name": "pt-br-abnt2"}, {"help": "Norwegian.", "label": "No", "name": "no"}, {"help": "Scottish Gaelic.", "label": "Gd", "name": "gd"}, {"help": "Spanish.", "label": "Es", "name": "es"}, {"help": "Swedish.", "label": "Sv", "name": "sv"}, {"help": "United States-International.", "label": "Us Intl", "name": "us-intl"}],
        },
    },
}


# Valid enum values from API documentation
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_ztna_web_portal_bookmark_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for ztna/web_portal_bookmark.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_ztna_web_portal_bookmark_get()
        >>> assert is_valid == True
        
        >>> # Valid - Get specific item by name
        >>> is_valid, error = validate_ztna_web_portal_bookmark_get(name="test-item")
        >>> assert is_valid == True
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_ztna_web_portal_bookmark_get(
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
    Validate required fields for ztna/web_portal_bookmark.

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


def validate_ztna_web_portal_bookmark_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new ztna/web_portal_bookmark object.

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
        >>> is_valid, error = validate_ztna_web_portal_bookmark_post(payload)
        >>> assert is_valid == True
        
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_ztna_web_portal_bookmark_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_ztna_web_portal_bookmark_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update ztna/web_portal_bookmark.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_ztna_web_portal_bookmark_put(payload)
    """
    # Step 1: Validate enum values

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
    "endpoint": "ztna/web_portal_bookmark",
    "category": "cmdb",
    "api_path": "ztna/web-portal-bookmark",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure ztna web-portal bookmark.",
    "total_fields": 4,
    "required_fields_count": 0,
    "fields_with_defaults_count": 1,
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
