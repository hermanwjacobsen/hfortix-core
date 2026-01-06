"""Validation helpers for antivirus/quarantine - Auto-generated"""

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
    """Validate GET request parameters for antivirus/quarantine."""
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
    """Validate required fields for antivirus/quarantine."""
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
    """Validate POST request to create new antivirus/quarantine object."""
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
    """Validate PUT request to update antivirus/quarantine."""
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
    "endpoint": "antivirus/quarantine",
    "category": "cmdb",
    "api_path": "antivirus/quarantine",
    "help": "Configure quarantine options.",
    "total_fields": 9,
    "required_fields_count": 0,
    "fields_with_defaults_count": 9,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
