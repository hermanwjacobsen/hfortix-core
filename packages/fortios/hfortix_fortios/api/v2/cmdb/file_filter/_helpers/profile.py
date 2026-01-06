"""Validation helpers for file_filter/profile - Auto-generated"""

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
    "name",  # Profile name.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "feature-set": "flow",
    "replacemsg-group": "",
    "log": "enable",
    "extended-log": "disable",
    "scan-archive-contents": "enable",
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
    "name": "string",  # Profile name.
    "comment": "var-string",  # Comment.
    "feature-set": "option",  # Flow/proxy feature set.
    "replacemsg-group": "string",  # Replacement message group.
    "log": "option",  # Enable/disable file-filter logging.
    "extended-log": "option",  # Enable/disable file-filter extended logging.
    "scan-archive-contents": "option",  # Enable/disable archive contents scan.
    "rules": "string",  # File filter rules.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Profile name.",
    "comment": "Comment.",
    "feature-set": "Flow/proxy feature set.",
    "replacemsg-group": "Replacement message group.",
    "log": "Enable/disable file-filter logging.",
    "extended-log": "Enable/disable file-filter extended logging.",
    "scan-archive-contents": "Enable/disable archive contents scan.",
    "rules": "File filter rules.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 47},
    "replacemsg-group": {"type": "string", "max_length": 35},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "rules": {
        "name": {
            "type": "string",
            "help": "File-filter rule name.",
            "required": True,
            "default": "",
            "max_length": 35,
        },
        "comment": {
            "type": "var-string",
            "help": "Comment.",
            "max_length": 255,
        },
        "protocol": {
            "type": "option",
            "help": "Protocols to apply rule to.",
            "default": "http ftp smtp imap pop3 mapi cifs ssh",
            "options": [{"help": "Filter on HTTP.", "label": "Http", "name": "http"}, {"help": "Filter on FTP.", "label": "Ftp", "name": "ftp"}, {"help": "Filter on SMTP.", "label": "Smtp", "name": "smtp"}, {"help": "Filter on IMAP.", "label": "Imap", "name": "imap"}, {"help": "Filter on POP3.", "label": "Pop3", "name": "pop3"}, {"help": "Filter on MAPI. (Proxy mode only.)", "label": "Mapi", "name": "mapi"}, {"help": "Filter on CIFS.", "label": "Cifs", "name": "cifs"}, {"help": "Filter on SFTP and SCP. (Proxy mode only.)", "label": "Ssh", "name": "ssh"}],
        },
        "action": {
            "type": "option",
            "help": "Action taken for matched file.",
            "default": "log-only",
            "options": [{"help": "Allow the content and write a log message.", "label": "Log Only", "name": "log-only"}, {"help": "Block the content and write a log message.", "label": "Block", "name": "block"}],
        },
        "direction": {
            "type": "option",
            "help": "Traffic direction (HTTP, FTP, SSH, CIFS, and MAPI only).",
            "default": "any",
            "options": [{"help": "Match files transmitted in the session\u0027s reply direction.", "label": "Incoming", "name": "incoming"}, {"help": "Match files transmitted in the session\u0027s originating direction.", "label": "Outgoing", "name": "outgoing"}, {"help": "Match files transmitted in the session\u0027s originating and reply directions.", "label": "Any", "name": "any"}],
        },
        "password-protected": {
            "type": "option",
            "help": "Match password-protected files.",
            "default": "any",
            "options": [{"help": "Match only password-protected files.", "label": "Yes", "name": "yes"}, {"help": "Match any file.", "label": "Any", "name": "any"}],
        },
        "file-type": {
            "type": "string",
            "help": "Select file type.",
            "required": True,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_FEATURE_SET = [
    "flow",  # Flow feature set.
    "proxy",  # Proxy feature set.
]
VALID_BODY_LOG = [
    "disable",  # Disable logging.
    "enable",  # Enable logging.
]
VALID_BODY_EXTENDED_LOG = [
    "disable",  # Disable extended logging.
    "enable",  # Enable extended logging.
]
VALID_BODY_SCAN_ARCHIVE_CONTENTS = [
    "disable",  # Disable scanning archive contents.
    "enable",  # Enable scanning archive contents.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_file_filter_profile_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for file_filter/profile."""
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
    """Validate required fields for file_filter/profile."""
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


def validate_file_filter_profile_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new file_filter/profile object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "feature-set" in payload:
        value = payload["feature-set"]
        if value not in VALID_BODY_FEATURE_SET:
            desc = FIELD_DESCRIPTIONS.get("feature-set", "")
            error_msg = f"Invalid value for 'feature-set': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FEATURE_SET)}"
            error_msg += f"\n  → Example: feature-set='{{ VALID_BODY_FEATURE_SET[0] }}'"
            return (False, error_msg)
    if "log" in payload:
        value = payload["log"]
        if value not in VALID_BODY_LOG:
            desc = FIELD_DESCRIPTIONS.get("log", "")
            error_msg = f"Invalid value for 'log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOG)}"
            error_msg += f"\n  → Example: log='{{ VALID_BODY_LOG[0] }}'"
            return (False, error_msg)
    if "extended-log" in payload:
        value = payload["extended-log"]
        if value not in VALID_BODY_EXTENDED_LOG:
            desc = FIELD_DESCRIPTIONS.get("extended-log", "")
            error_msg = f"Invalid value for 'extended-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EXTENDED_LOG)}"
            error_msg += f"\n  → Example: extended-log='{{ VALID_BODY_EXTENDED_LOG[0] }}'"
            return (False, error_msg)
    if "scan-archive-contents" in payload:
        value = payload["scan-archive-contents"]
        if value not in VALID_BODY_SCAN_ARCHIVE_CONTENTS:
            desc = FIELD_DESCRIPTIONS.get("scan-archive-contents", "")
            error_msg = f"Invalid value for 'scan-archive-contents': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SCAN_ARCHIVE_CONTENTS)}"
            error_msg += f"\n  → Example: scan-archive-contents='{{ VALID_BODY_SCAN_ARCHIVE_CONTENTS[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_file_filter_profile_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update file_filter/profile."""
    # Step 1: Validate enum values
    if "feature-set" in payload:
        value = payload["feature-set"]
        if value not in VALID_BODY_FEATURE_SET:
            return (
                False,
                f"Invalid value for 'feature-set'='{value}'. Must be one of: {', '.join(VALID_BODY_FEATURE_SET)}",
            )
    if "log" in payload:
        value = payload["log"]
        if value not in VALID_BODY_LOG:
            return (
                False,
                f"Invalid value for 'log'='{value}'. Must be one of: {', '.join(VALID_BODY_LOG)}",
            )
    if "extended-log" in payload:
        value = payload["extended-log"]
        if value not in VALID_BODY_EXTENDED_LOG:
            return (
                False,
                f"Invalid value for 'extended-log'='{value}'. Must be one of: {', '.join(VALID_BODY_EXTENDED_LOG)}",
            )
    if "scan-archive-contents" in payload:
        value = payload["scan-archive-contents"]
        if value not in VALID_BODY_SCAN_ARCHIVE_CONTENTS:
            return (
                False,
                f"Invalid value for 'scan-archive-contents'='{value}'. Must be one of: {', '.join(VALID_BODY_SCAN_ARCHIVE_CONTENTS)}",
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
    "endpoint": "file_filter/profile",
    "category": "cmdb",
    "api_path": "file-filter/profile",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure file-filter profiles.",
    "total_fields": 8,
    "required_fields_count": 1,
    "fields_with_defaults_count": 6,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
