"""Validation helpers for emailfilter/profile - Auto-generated"""

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
    "spam-log": "enable",
    "spam-log-fortiguard-response": "disable",
    "spam-filtering": "disable",
    "external": "disable",
    "options": "",
    "spam-bword-threshold": 10,
    "spam-bword-table": 0,
    "spam-bal-table": 0,
    "spam-mheader-table": 0,
    "spam-rbl-table": 0,
    "spam-iptrust-table": 0,
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
    "spam-log": "option",  # Enable/disable spam logging for email filtering.
    "spam-log-fortiguard-response": "option",  # Enable/disable logging FortiGuard spam response.
    "spam-filtering": "option",  # Enable/disable spam filtering.
    "external": "option",  # Enable/disable external Email inspection.
    "options": "option",  # Options.
    "imap": "string",  # IMAP.
    "pop3": "string",  # POP3.
    "smtp": "string",  # SMTP.
    "mapi": "string",  # MAPI.
    "msn-hotmail": "string",  # MSN Hotmail.
    "yahoo-mail": "string",  # Yahoo! Mail.
    "gmail": "string",  # Gmail.
    "other-webmails": "string",  # Other supported webmails.
    "spam-bword-threshold": "integer",  # Spam banned word threshold.
    "spam-bword-table": "integer",  # Anti-spam banned word table ID.
    "spam-bal-table": "integer",  # Anti-spam block/allow list table ID.
    "spam-mheader-table": "integer",  # Anti-spam MIME header table ID.
    "spam-rbl-table": "integer",  # Anti-spam DNSBL table ID.
    "spam-iptrust-table": "integer",  # Anti-spam IP trust table ID.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Profile name.",
    "comment": "Comment.",
    "feature-set": "Flow/proxy feature set.",
    "replacemsg-group": "Replacement message group.",
    "spam-log": "Enable/disable spam logging for email filtering.",
    "spam-log-fortiguard-response": "Enable/disable logging FortiGuard spam response.",
    "spam-filtering": "Enable/disable spam filtering.",
    "external": "Enable/disable external Email inspection.",
    "options": "Options.",
    "imap": "IMAP.",
    "pop3": "POP3.",
    "smtp": "SMTP.",
    "mapi": "MAPI.",
    "msn-hotmail": "MSN Hotmail.",
    "yahoo-mail": "Yahoo! Mail.",
    "gmail": "Gmail.",
    "other-webmails": "Other supported webmails.",
    "spam-bword-threshold": "Spam banned word threshold.",
    "spam-bword-table": "Anti-spam banned word table ID.",
    "spam-bal-table": "Anti-spam block/allow list table ID.",
    "spam-mheader-table": "Anti-spam MIME header table ID.",
    "spam-rbl-table": "Anti-spam DNSBL table ID.",
    "spam-iptrust-table": "Anti-spam IP trust table ID.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 47},
    "replacemsg-group": {"type": "string", "max_length": 35},
    "spam-bword-threshold": {"type": "integer", "min": 0, "max": 2147483647},
    "spam-bword-table": {"type": "integer", "min": 0, "max": 4294967295},
    "spam-bal-table": {"type": "integer", "min": 0, "max": 4294967295},
    "spam-mheader-table": {"type": "integer", "min": 0, "max": 4294967295},
    "spam-rbl-table": {"type": "integer", "min": 0, "max": 4294967295},
    "spam-iptrust-table": {"type": "integer", "min": 0, "max": 4294967295},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "imap": {
        "log-all": {
            "type": "option",
            "help": "Enable/disable logging of all email traffic.",
            "default": "disable",
            "options": [{"help": "Disable logging of all email traffic.", "label": "Disable", "name": "disable"}, {"help": "Enable logging of all email traffic.", "label": "Enable", "name": "enable"}],
        },
        "action": {
            "type": "option",
            "help": "Action for spam email.",
            "default": "tag",
            "options": [{"help": "Allow spam email to pass through.", "label": "Pass", "name": "pass"}, {"help": "Tag spam email with configured text in subject or header.", "label": "Tag", "name": "tag"}],
        },
        "tag-type": {
            "type": "option",
            "help": "Tag subject or header for spam email.",
            "default": "subject spaminfo",
            "options": [{"help": "Prepend text to spam email subject.", "label": "Subject", "name": "subject"}, {"help": "Append a user defined mime header to spam email.", "label": "Header", "name": "header"}, {"help": "Append spam info to spam email header.", "label": "Spaminfo", "name": "spaminfo"}],
        },
        "tag-msg": {
            "type": "string",
            "help": "Subject text or header added to spam email.",
            "default": "Spam",
            "max_length": 63,
        },
    },
    "pop3": {
        "log-all": {
            "type": "option",
            "help": "Enable/disable logging of all email traffic.",
            "default": "disable",
            "options": [{"help": "Disable logging of all email traffic.", "label": "Disable", "name": "disable"}, {"help": "Enable logging of all email traffic.", "label": "Enable", "name": "enable"}],
        },
        "action": {
            "type": "option",
            "help": "Action for spam email.",
            "default": "tag",
            "options": [{"help": "Allow spam email to pass through.", "label": "Pass", "name": "pass"}, {"help": "Tag spam email with configured text in subject or header.", "label": "Tag", "name": "tag"}],
        },
        "tag-type": {
            "type": "option",
            "help": "Tag subject or header for spam email.",
            "default": "subject spaminfo",
            "options": [{"help": "Prepend text to spam email subject.", "label": "Subject", "name": "subject"}, {"help": "Append a user defined mime header to spam email.", "label": "Header", "name": "header"}, {"help": "Append spam info to spam email header.", "label": "Spaminfo", "name": "spaminfo"}],
        },
        "tag-msg": {
            "type": "string",
            "help": "Subject text or header added to spam email.",
            "default": "Spam",
            "max_length": 63,
        },
    },
    "smtp": {
        "log-all": {
            "type": "option",
            "help": "Enable/disable logging of all email traffic.",
            "default": "disable",
            "options": [{"help": "Disable logging of all email traffic.", "label": "Disable", "name": "disable"}, {"help": "Enable logging of all email traffic.", "label": "Enable", "name": "enable"}],
        },
        "action": {
            "type": "option",
            "help": "Action for spam email.",
            "default": "discard",
            "options": [{"help": "Allow spam email to pass through.", "label": "Pass", "name": "pass"}, {"help": "Tag spam email with configured text in subject or header.", "label": "Tag", "name": "tag"}, {"help": "Discard (block) spam email.", "label": "Discard", "name": "discard"}],
        },
        "tag-type": {
            "type": "option",
            "help": "Tag subject or header for spam email.",
            "default": "subject spaminfo",
            "options": [{"help": "Prepend text to spam email subject.", "label": "Subject", "name": "subject"}, {"help": "Append a user defined mime header to spam email.", "label": "Header", "name": "header"}, {"help": "Append spam info to spam email header.", "label": "Spaminfo", "name": "spaminfo"}],
        },
        "tag-msg": {
            "type": "string",
            "help": "Subject text or header added to spam email.",
            "default": "Spam",
            "max_length": 63,
        },
        "hdrip": {
            "type": "option",
            "help": "Enable/disable SMTP email header IP checks for spamfsip, spamrbl, and spambal filters.",
            "default": "disable",
            "options": [{"help": "Disable SMTP email header IP checks for spamfsip, spamrbl, and spambal filters.", "label": "Disable", "name": "disable"}, {"help": "Enable SMTP email header IP checks for spamfsip, spamrbl, and spambal filters.", "label": "Enable", "name": "enable"}],
        },
        "local-override": {
            "type": "option",
            "help": "Enable/disable local filter to override SMTP remote check result.",
            "default": "disable",
            "options": [{"help": "Disable local filter to override SMTP remote check result.", "label": "Disable", "name": "disable"}, {"help": "Enable local filter to override SMTP remote check result.", "label": "Enable", "name": "enable"}],
        },
    },
    "mapi": {
        "log-all": {
            "type": "option",
            "help": "Enable/disable logging of all email traffic.",
            "default": "disable",
            "options": [{"help": "Disable logging of all email traffic.", "label": "Disable", "name": "disable"}, {"help": "Enable logging of all email traffic.", "label": "Enable", "name": "enable"}],
        },
        "action": {
            "type": "option",
            "help": "Action for spam email.",
            "default": "pass",
            "options": [{"help": "Allow spam email to pass through.", "label": "Pass", "name": "pass"}, {"help": "Discard (block) spam email.", "label": "Discard", "name": "discard"}],
        },
    },
    "msn-hotmail": {
        "log-all": {
            "type": "option",
            "help": "Enable/disable logging of all email traffic.",
            "default": "disable",
            "options": [{"help": "Disable logging of all email traffic.", "label": "Disable", "name": "disable"}, {"help": "Enable logging of all email traffic.", "label": "Enable", "name": "enable"}],
        },
    },
    "yahoo-mail": {
        "log-all": {
            "type": "option",
            "help": "Enable/disable logging of all email traffic.",
            "default": "disable",
            "options": [{"help": "Disable logging of all email traffic.", "label": "Disable", "name": "disable"}, {"help": "Enable logging of all email traffic.", "label": "Enable", "name": "enable"}],
        },
    },
    "gmail": {
        "log-all": {
            "type": "option",
            "help": "Enable/disable logging of all email traffic.",
            "default": "disable",
            "options": [{"help": "Disable logging of all email traffic.", "label": "Disable", "name": "disable"}, {"help": "Enable logging of all email traffic.", "label": "Enable", "name": "enable"}],
        },
    },
    "other-webmails": {
        "log-all": {
            "type": "option",
            "help": "Enable/disable logging of all email traffic.",
            "default": "disable",
            "options": [{"help": "Disable logging of all email traffic.", "label": "Disable", "name": "disable"}, {"help": "Enable logging of all email traffic.", "label": "Enable", "name": "enable"}],
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_FEATURE_SET = [
    "flow",  # Flow feature set.
    "proxy",  # Proxy feature set.
]
VALID_BODY_SPAM_LOG = [
    "disable",  # Disable spam logging for email filtering.
    "enable",  # Enable spam logging for email filtering.
]
VALID_BODY_SPAM_LOG_FORTIGUARD_RESPONSE = [
    "disable",  # Disable logging FortiGuard spam response.
    "enable",  # Enable logging FortiGuard spam response.
]
VALID_BODY_SPAM_FILTERING = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_EXTERNAL = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_OPTIONS = [
    "bannedword",  # Content block.
    "spambal",  # Block/allow list.
    "spamfsip",  # Email IP address FortiGuard AntiSpam block list check.
    "spamfssubmit",  # Add FortiGuard AntiSpam spam submission text.
    "spamfschksum",  # Email checksum FortiGuard AntiSpam check.
    "spamfsurl",  # Email content URL FortiGuard AntiSpam check.
    "spamhelodns",  # Email helo/ehlo domain DNS check.
    "spamraddrdns",  # Email return address DNS check.
    "spamrbl",  # Email DNSBL & ORBL check.
    "spamhdrcheck",  # Email mime header check.
    "spamfsphish",  # Email content phishing URL FortiGuard AntiSpam check.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_emailfilter_profile_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for emailfilter/profile."""
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
    """Validate required fields for emailfilter/profile."""
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


def validate_emailfilter_profile_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new emailfilter/profile object."""
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
    if "spam-log" in payload:
        value = payload["spam-log"]
        if value not in VALID_BODY_SPAM_LOG:
            desc = FIELD_DESCRIPTIONS.get("spam-log", "")
            error_msg = f"Invalid value for 'spam-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SPAM_LOG)}"
            error_msg += f"\n  → Example: spam-log='{{ VALID_BODY_SPAM_LOG[0] }}'"
            return (False, error_msg)
    if "spam-log-fortiguard-response" in payload:
        value = payload["spam-log-fortiguard-response"]
        if value not in VALID_BODY_SPAM_LOG_FORTIGUARD_RESPONSE:
            desc = FIELD_DESCRIPTIONS.get("spam-log-fortiguard-response", "")
            error_msg = f"Invalid value for 'spam-log-fortiguard-response': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SPAM_LOG_FORTIGUARD_RESPONSE)}"
            error_msg += f"\n  → Example: spam-log-fortiguard-response='{{ VALID_BODY_SPAM_LOG_FORTIGUARD_RESPONSE[0] }}'"
            return (False, error_msg)
    if "spam-filtering" in payload:
        value = payload["spam-filtering"]
        if value not in VALID_BODY_SPAM_FILTERING:
            desc = FIELD_DESCRIPTIONS.get("spam-filtering", "")
            error_msg = f"Invalid value for 'spam-filtering': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SPAM_FILTERING)}"
            error_msg += f"\n  → Example: spam-filtering='{{ VALID_BODY_SPAM_FILTERING[0] }}'"
            return (False, error_msg)
    if "external" in payload:
        value = payload["external"]
        if value not in VALID_BODY_EXTERNAL:
            desc = FIELD_DESCRIPTIONS.get("external", "")
            error_msg = f"Invalid value for 'external': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EXTERNAL)}"
            error_msg += f"\n  → Example: external='{{ VALID_BODY_EXTERNAL[0] }}'"
            return (False, error_msg)
    if "options" in payload:
        value = payload["options"]
        if value not in VALID_BODY_OPTIONS:
            desc = FIELD_DESCRIPTIONS.get("options", "")
            error_msg = f"Invalid value for 'options': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OPTIONS)}"
            error_msg += f"\n  → Example: options='{{ VALID_BODY_OPTIONS[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_emailfilter_profile_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update emailfilter/profile."""
    # Step 1: Validate enum values
    if "feature-set" in payload:
        value = payload["feature-set"]
        if value not in VALID_BODY_FEATURE_SET:
            return (
                False,
                f"Invalid value for 'feature-set'='{value}'. Must be one of: {', '.join(VALID_BODY_FEATURE_SET)}",
            )
    if "spam-log" in payload:
        value = payload["spam-log"]
        if value not in VALID_BODY_SPAM_LOG:
            return (
                False,
                f"Invalid value for 'spam-log'='{value}'. Must be one of: {', '.join(VALID_BODY_SPAM_LOG)}",
            )
    if "spam-log-fortiguard-response" in payload:
        value = payload["spam-log-fortiguard-response"]
        if value not in VALID_BODY_SPAM_LOG_FORTIGUARD_RESPONSE:
            return (
                False,
                f"Invalid value for 'spam-log-fortiguard-response'='{value}'. Must be one of: {', '.join(VALID_BODY_SPAM_LOG_FORTIGUARD_RESPONSE)}",
            )
    if "spam-filtering" in payload:
        value = payload["spam-filtering"]
        if value not in VALID_BODY_SPAM_FILTERING:
            return (
                False,
                f"Invalid value for 'spam-filtering'='{value}'. Must be one of: {', '.join(VALID_BODY_SPAM_FILTERING)}",
            )
    if "external" in payload:
        value = payload["external"]
        if value not in VALID_BODY_EXTERNAL:
            return (
                False,
                f"Invalid value for 'external'='{value}'. Must be one of: {', '.join(VALID_BODY_EXTERNAL)}",
            )
    if "options" in payload:
        value = payload["options"]
        if value not in VALID_BODY_OPTIONS:
            return (
                False,
                f"Invalid value for 'options'='{value}'. Must be one of: {', '.join(VALID_BODY_OPTIONS)}",
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
    "endpoint": "emailfilter/profile",
    "category": "cmdb",
    "api_path": "emailfilter/profile",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure Email Filter profiles.",
    "total_fields": 23,
    "required_fields_count": 1,
    "fields_with_defaults_count": 14,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
