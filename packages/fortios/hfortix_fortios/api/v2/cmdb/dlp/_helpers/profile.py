"""Validation helpers for dlp/profile - Auto-generated"""

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
    "name",  # Name of the DLP profile.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "feature-set": "flow",
    "replacemsg-group": "",
    "dlp-log": "enable",
    "extended-log": "disable",
    "nac-quar-log": "disable",
    "full-archive-proto": "",
    "summary-proto": "",
    "fortidata-error-action": "block",
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
    "name": "string",  # Name of the DLP profile.
    "comment": "var-string",  # Comment.
    "feature-set": "option",  # Flow/proxy feature set.
    "replacemsg-group": "string",  # Replacement message group used by this DLP profile.
    "rule": "string",  # Set up DLP rules for this profile.
    "dlp-log": "option",  # Enable/disable DLP logging.
    "extended-log": "option",  # Enable/disable extended logging for data loss prevention.
    "nac-quar-log": "option",  # Enable/disable NAC quarantine logging.
    "full-archive-proto": "option",  # Protocols to always content archive.
    "summary-proto": "option",  # Protocols to always log summary.
    "fortidata-error-action": "option",  # Action to take if FortiData query fails.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Name of the DLP profile.",
    "comment": "Comment.",
    "feature-set": "Flow/proxy feature set.",
    "replacemsg-group": "Replacement message group used by this DLP profile.",
    "rule": "Set up DLP rules for this profile.",
    "dlp-log": "Enable/disable DLP logging.",
    "extended-log": "Enable/disable extended logging for data loss prevention.",
    "nac-quar-log": "Enable/disable NAC quarantine logging.",
    "full-archive-proto": "Protocols to always content archive.",
    "summary-proto": "Protocols to always log summary.",
    "fortidata-error-action": "Action to take if FortiData query fails.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 47},
    "replacemsg-group": {"type": "string", "max_length": 35},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "rule": {
        "id": {
            "type": "integer",
            "help": "ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "name": {
            "type": "string",
            "help": "Filter name.",
            "default": "",
            "max_length": 35,
        },
        "severity": {
            "type": "option",
            "help": "Select the severity or threat level that matches this filter.",
            "default": "medium",
            "options": [{"help": "Informational.", "label": "Info", "name": "info"}, {"help": "Low.", "label": "Low", "name": "low"}, {"help": "Medium.", "label": "Medium", "name": "medium"}, {"help": "High.", "label": "High", "name": "high"}, {"help": "Critical.", "label": "Critical", "name": "critical"}],
        },
        "type": {
            "type": "option",
            "help": "Select whether to check the content of messages (an email message) or files (downloaded files or email attachments).",
            "default": "file",
            "options": [{"help": "Check the contents of downloaded or attached files.", "label": "File", "name": "file"}, {"help": "Check the contents of email messages, web pages, etc.", "label": "Message", "name": "message"}],
        },
        "proto": {
            "type": "option",
            "help": "Check messages or files over one or more of these protocols.",
            "default": "",
            "options": [{"help": "SMTP.", "label": "Smtp", "name": "smtp"}, {"help": "POP3.", "label": "Pop3", "name": "pop3"}, {"help": "IMAP.", "label": "Imap", "name": "imap"}, {"help": "HTTP GET.", "label": "Http Get", "name": "http-get"}, {"help": "HTTP POST.", "label": "Http Post", "name": "http-post"}, {"help": "FTP.", "label": "Ftp", "name": "ftp"}, {"help": "NNTP.", "label": "Nntp", "name": "nntp"}, {"help": "MAPI.", "label": "Mapi", "name": "mapi"}, {"help": "SFTP and SCP.", "label": "Ssh", "name": "ssh"}, {"help": "CIFS.", "label": "Cifs", "name": "cifs"}],
        },
        "filter-by": {
            "type": "option",
            "help": "Select the type of content to match.",
            "default": "none",
            "options": [{"help": "Use DLP sensors to match content.", "label": "Sensor", "name": "sensor"}, {"help": "Use DLP labels to match content.", "label": "Label", "name": "label"}, {"help": "Match against a fingerprint sensitivity.", "label": "Fingerprint", "name": "fingerprint"}, {"help": "Look for encrypted files.", "label": "Encrypted", "name": "encrypted"}, {"help": "No content scan.", "label": "None", "name": "none"}],
        },
        "file-size": {
            "type": "integer",
            "help": "Match files greater than or equal to this size (KB).",
            "default": 0,
            "min_value": 0,
            "max_value": 4193280,
        },
        "sensitivity": {
            "type": "string",
            "help": "Select a DLP file pattern sensitivity to match.",
            "required": True,
        },
        "match-percentage": {
            "type": "integer",
            "help": "Percentage of fingerprints in the fingerprint databases designated with the selected sensitivity to match.",
            "default": 10,
            "min_value": 1,
            "max_value": 100,
        },
        "file-type": {
            "type": "integer",
            "help": "Select the number of a DLP file pattern table to match.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "sensor": {
            "type": "string",
            "help": "Select DLP sensors.",
            "required": True,
        },
        "label": {
            "type": "string",
            "help": "Select DLP label.",
            "required": True,
            "default": "",
            "max_length": 35,
        },
        "archive": {
            "type": "option",
            "help": "Enable/disable DLP archiving.",
            "default": "disable",
            "options": [{"help": "No DLP archiving.", "label": "Disable", "name": "disable"}, {"help": "Enable full DLP archiving.", "label": "Enable", "name": "enable"}],
        },
        "action": {
            "type": "option",
            "help": "Action to take with content that this DLP profile matches.",
            "default": "allow",
            "options": [{"help": "Allow the content to pass through the FortiGate and do not create a log message.", "label": "Allow", "name": "allow"}, {"help": "Allow the content to pass through the FortiGate, but write a log message.", "label": "Log Only", "name": "log-only"}, {"help": "Block the content and write a log message.", "label": "Block", "name": "block"}, {"help": "Quarantine all traffic from the IP address and write a log message.", "label": "Quarantine Ip", "name": "quarantine-ip"}],
        },
        "expiry": {
            "type": "user",
            "help": "Quarantine duration in days, hours, minutes (format = dddhhmm).",
            "default": "5m",
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_FEATURE_SET = [
    "flow",  # Flow feature set.
    "proxy",  # Proxy feature set.
]
VALID_BODY_DLP_LOG = [
    "enable",  # Enable DLP logging.
    "disable",  # Disable DLP logging.
]
VALID_BODY_EXTENDED_LOG = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_NAC_QUAR_LOG = [
    "enable",  # Enable NAC quarantine logging.
    "disable",  # Disable NAC quarantine logging.
]
VALID_BODY_FULL_ARCHIVE_PROTO = [
    "smtp",  # SMTP.
    "pop3",  # POP3.
    "imap",  # IMAP.
    "http-get",  # HTTP GET.
    "http-post",  # HTTP POST.
    "ftp",  # FTP.
    "nntp",  # NNTP.
    "mapi",  # MAPI.
    "ssh",  # SFTP and SCP.
    "cifs",  # CIFS.
]
VALID_BODY_SUMMARY_PROTO = [
    "smtp",  # SMTP.
    "pop3",  # POP3.
    "imap",  # IMAP.
    "http-get",  # HTTP GET.
    "http-post",  # HTTP POST.
    "ftp",  # FTP.
    "nntp",  # NNTP.
    "mapi",  # MAPI.
    "ssh",  # SFTP and SCP.
    "cifs",  # CIFS.
]
VALID_BODY_FORTIDATA_ERROR_ACTION = [
    "log-only",  # Log failure, but allow the file.
    "block",  # Block the file.
    "ignore",  # Behave as if FortiData returned no match.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_dlp_profile_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for dlp/profile."""
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
    """Validate required fields for dlp/profile."""
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


def validate_dlp_profile_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new dlp/profile object."""
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
    if "dlp-log" in payload:
        value = payload["dlp-log"]
        if value not in VALID_BODY_DLP_LOG:
            desc = FIELD_DESCRIPTIONS.get("dlp-log", "")
            error_msg = f"Invalid value for 'dlp-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DLP_LOG)}"
            error_msg += f"\n  → Example: dlp-log='{{ VALID_BODY_DLP_LOG[0] }}'"
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
    if "nac-quar-log" in payload:
        value = payload["nac-quar-log"]
        if value not in VALID_BODY_NAC_QUAR_LOG:
            desc = FIELD_DESCRIPTIONS.get("nac-quar-log", "")
            error_msg = f"Invalid value for 'nac-quar-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_NAC_QUAR_LOG)}"
            error_msg += f"\n  → Example: nac-quar-log='{{ VALID_BODY_NAC_QUAR_LOG[0] }}'"
            return (False, error_msg)
    if "full-archive-proto" in payload:
        value = payload["full-archive-proto"]
        if value not in VALID_BODY_FULL_ARCHIVE_PROTO:
            desc = FIELD_DESCRIPTIONS.get("full-archive-proto", "")
            error_msg = f"Invalid value for 'full-archive-proto': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FULL_ARCHIVE_PROTO)}"
            error_msg += f"\n  → Example: full-archive-proto='{{ VALID_BODY_FULL_ARCHIVE_PROTO[0] }}'"
            return (False, error_msg)
    if "summary-proto" in payload:
        value = payload["summary-proto"]
        if value not in VALID_BODY_SUMMARY_PROTO:
            desc = FIELD_DESCRIPTIONS.get("summary-proto", "")
            error_msg = f"Invalid value for 'summary-proto': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SUMMARY_PROTO)}"
            error_msg += f"\n  → Example: summary-proto='{{ VALID_BODY_SUMMARY_PROTO[0] }}'"
            return (False, error_msg)
    if "fortidata-error-action" in payload:
        value = payload["fortidata-error-action"]
        if value not in VALID_BODY_FORTIDATA_ERROR_ACTION:
            desc = FIELD_DESCRIPTIONS.get("fortidata-error-action", "")
            error_msg = f"Invalid value for 'fortidata-error-action': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FORTIDATA_ERROR_ACTION)}"
            error_msg += f"\n  → Example: fortidata-error-action='{{ VALID_BODY_FORTIDATA_ERROR_ACTION[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_dlp_profile_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update dlp/profile."""
    # Step 1: Validate enum values
    if "feature-set" in payload:
        value = payload["feature-set"]
        if value not in VALID_BODY_FEATURE_SET:
            return (
                False,
                f"Invalid value for 'feature-set'='{value}'. Must be one of: {', '.join(VALID_BODY_FEATURE_SET)}",
            )
    if "dlp-log" in payload:
        value = payload["dlp-log"]
        if value not in VALID_BODY_DLP_LOG:
            return (
                False,
                f"Invalid value for 'dlp-log'='{value}'. Must be one of: {', '.join(VALID_BODY_DLP_LOG)}",
            )
    if "extended-log" in payload:
        value = payload["extended-log"]
        if value not in VALID_BODY_EXTENDED_LOG:
            return (
                False,
                f"Invalid value for 'extended-log'='{value}'. Must be one of: {', '.join(VALID_BODY_EXTENDED_LOG)}",
            )
    if "nac-quar-log" in payload:
        value = payload["nac-quar-log"]
        if value not in VALID_BODY_NAC_QUAR_LOG:
            return (
                False,
                f"Invalid value for 'nac-quar-log'='{value}'. Must be one of: {', '.join(VALID_BODY_NAC_QUAR_LOG)}",
            )
    if "full-archive-proto" in payload:
        value = payload["full-archive-proto"]
        if value not in VALID_BODY_FULL_ARCHIVE_PROTO:
            return (
                False,
                f"Invalid value for 'full-archive-proto'='{value}'. Must be one of: {', '.join(VALID_BODY_FULL_ARCHIVE_PROTO)}",
            )
    if "summary-proto" in payload:
        value = payload["summary-proto"]
        if value not in VALID_BODY_SUMMARY_PROTO:
            return (
                False,
                f"Invalid value for 'summary-proto'='{value}'. Must be one of: {', '.join(VALID_BODY_SUMMARY_PROTO)}",
            )
    if "fortidata-error-action" in payload:
        value = payload["fortidata-error-action"]
        if value not in VALID_BODY_FORTIDATA_ERROR_ACTION:
            return (
                False,
                f"Invalid value for 'fortidata-error-action'='{value}'. Must be one of: {', '.join(VALID_BODY_FORTIDATA_ERROR_ACTION)}",
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
    "endpoint": "dlp/profile",
    "category": "cmdb",
    "api_path": "dlp/profile",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure DLP profiles.",
    "total_fields": 11,
    "required_fields_count": 1,
    "fields_with_defaults_count": 9,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
