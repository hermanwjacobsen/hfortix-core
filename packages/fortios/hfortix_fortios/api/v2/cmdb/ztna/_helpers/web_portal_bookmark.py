"""Validation helpers for ztna/web_portal_bookmark - Auto-generated"""

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
    """Validate GET request parameters for ztna/web_portal_bookmark."""
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
    """Validate required fields for ztna/web_portal_bookmark."""
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
    """Validate POST request to create new ztna/web_portal_bookmark object."""
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
    """Validate PUT request to update ztna/web_portal_bookmark."""
    # Step 1: Validate enum values

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
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
