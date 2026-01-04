"""
Validation helpers for log/disk_setting endpoint.

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
    "uploaduser",  # Username required to log into the FTP server to upload disk log files.
    "interface",  # Specify outgoing interface to reach server.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "status": "enable",
    "ips-archive": "enable",
    "max-log-file-size": 20,
    "max-policy-packet-capture-size": 100,
    "roll-schedule": "daily",
    "roll-day": "sunday",
    "roll-time": "",
    "diskfull": "overwrite",
    "log-quota": 0,
    "dlp-archive-quota": 0,
    "report-quota": 0,
    "maximum-log-age": 7,
    "upload": "disable",
    "upload-destination": "ftp-server",
    "uploadip": "0.0.0.0",
    "uploadport": 21,
    "source-ip": "0.0.0.0",
    "uploaduser": "",
    "uploaddir": "",
    "uploadtype": "traffic event virus webfilter IPS emailfilter dlp-archive anomaly voip dlp app-ctrl waf gtp dns ssh ssl",
    "uploadsched": "disable",
    "uploadtime": "",
    "upload-delete-files": "enable",
    "upload-ssl-conn": "default",
    "full-first-warning-threshold": 75,
    "full-second-warning-threshold": 90,
    "full-final-warning-threshold": 95,
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
    "status": "option",  # Enable/disable local disk logging.
    "ips-archive": "option",  # Enable/disable IPS packet archiving to the local disk.
    "max-log-file-size": "integer",  # Maximum log file size before rolling (1 - 100 Mbytes).
    "max-policy-packet-capture-size": "integer",  # Maximum size of policy sniffer in MB (0 means unlimited).
    "roll-schedule": "option",  # Frequency to check log file for rolling.
    "roll-day": "option",  # Day of week on which to roll log file.
    "roll-time": "user",  # Time of day to roll the log file (hh:mm).
    "diskfull": "option",  # Action to take when disk is full. The system can overwrite t
    "log-quota": "integer",  # Disk log quota (MB).
    "dlp-archive-quota": "integer",  # DLP archive quota (MB).
    "report-quota": "integer",  # Report db quota (MB).
    "maximum-log-age": "integer",  # Delete log files older than (days).
    "upload": "option",  # Enable/disable uploading log files when they are rolled.
    "upload-destination": "option",  # The type of server to upload log files to. Only FTP is curre
    "uploadip": "ipv4-address",  # IP address of the FTP server to upload log files to.
    "uploadport": "integer",  # TCP port to use for communicating with the FTP server (defau
    "source-ip": "ipv4-address",  # Source IP address to use for uploading disk log files.
    "uploaduser": "string",  # Username required to log into the FTP server to upload disk 
    "uploadpass": "password",  # Password required to log into the FTP server to upload disk 
    "uploaddir": "string",  # The remote directory on the FTP server to upload log files t
    "uploadtype": "option",  # Types of log files to upload. Separate multiple entries with
    "uploadsched": "option",  # Set the schedule for uploading log files to the FTP server (
    "uploadtime": "user",  # Time of day at which log files are uploaded if uploadsched i
    "upload-delete-files": "option",  # Delete log files after uploading (default = enable).
    "upload-ssl-conn": "option",  # Enable/disable encrypted FTPS communication to upload log fi
    "full-first-warning-threshold": "integer",  # Log full first warning threshold as a percent (1 - 98, defau
    "full-second-warning-threshold": "integer",  # Log full second warning threshold as a percent (2 - 99, defa
    "full-final-warning-threshold": "integer",  # Log full final warning threshold as a percent (3 - 100, defa
    "interface-select-method": "option",  # Specify how to select outgoing interface to reach server.
    "interface": "string",  # Specify outgoing interface to reach server.
    "vrf-select": "integer",  # VRF ID used for connection to server.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "status": "Enable/disable local disk logging.",
    "ips-archive": "Enable/disable IPS packet archiving to the local disk.",
    "max-log-file-size": "Maximum log file size before rolling (1 - 100 Mbytes).",
    "max-policy-packet-capture-size": "Maximum size of policy sniffer in MB (0 means unlimited).",
    "roll-schedule": "Frequency to check log file for rolling.",
    "roll-day": "Day of week on which to roll log file.",
    "roll-time": "Time of day to roll the log file (hh:mm).",
    "diskfull": "Action to take when disk is full. The system can overwrite the oldest log messages or stop logging when the disk is full (default = overwrite).",
    "log-quota": "Disk log quota (MB).",
    "dlp-archive-quota": "DLP archive quota (MB).",
    "report-quota": "Report db quota (MB).",
    "maximum-log-age": "Delete log files older than (days).",
    "upload": "Enable/disable uploading log files when they are rolled.",
    "upload-destination": "The type of server to upload log files to. Only FTP is currently supported.",
    "uploadip": "IP address of the FTP server to upload log files to.",
    "uploadport": "TCP port to use for communicating with the FTP server (default = 21).",
    "source-ip": "Source IP address to use for uploading disk log files.",
    "uploaduser": "Username required to log into the FTP server to upload disk log files.",
    "uploadpass": "Password required to log into the FTP server to upload disk log files.",
    "uploaddir": "The remote directory on the FTP server to upload log files to.",
    "uploadtype": "Types of log files to upload. Separate multiple entries with a space.",
    "uploadsched": "Set the schedule for uploading log files to the FTP server (default = disable = upload when rolling).",
    "uploadtime": "Time of day at which log files are uploaded if uploadsched is enabled (hh:mm or hh).",
    "upload-delete-files": "Delete log files after uploading (default = enable).",
    "upload-ssl-conn": "Enable/disable encrypted FTPS communication to upload log files.",
    "full-first-warning-threshold": "Log full first warning threshold as a percent (1 - 98, default = 75).",
    "full-second-warning-threshold": "Log full second warning threshold as a percent (2 - 99, default = 90).",
    "full-final-warning-threshold": "Log full final warning threshold as a percent (3 - 100, default = 95).",
    "interface-select-method": "Specify how to select outgoing interface to reach server.",
    "interface": "Specify outgoing interface to reach server.",
    "vrf-select": "VRF ID used for connection to server.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "max-log-file-size": {"type": "integer", "min": 1, "max": 100},
    "max-policy-packet-capture-size": {"type": "integer", "min": 0, "max": 4294967295},
    "log-quota": {"type": "integer", "min": 0, "max": 4294967295},
    "dlp-archive-quota": {"type": "integer", "min": 0, "max": 4294967295},
    "report-quota": {"type": "integer", "min": 0, "max": 4294967295},
    "maximum-log-age": {"type": "integer", "min": 0, "max": 3650},
    "uploadport": {"type": "integer", "min": 0, "max": 65535},
    "uploaduser": {"type": "string", "max_length": 35},
    "uploaddir": {"type": "string", "max_length": 63},
    "full-first-warning-threshold": {"type": "integer", "min": 1, "max": 98},
    "full-second-warning-threshold": {"type": "integer", "min": 2, "max": 99},
    "full-final-warning-threshold": {"type": "integer", "min": 3, "max": 100},
    "interface": {"type": "string", "max_length": 15},
    "vrf-select": {"type": "integer", "min": 0, "max": 511},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_STATUS = [
    "enable",
    "disable",
]
VALID_BODY_IPS_ARCHIVE = [
    "enable",
    "disable",
]
VALID_BODY_ROLL_SCHEDULE = [
    "daily",
    "weekly",
]
VALID_BODY_ROLL_DAY = [
    "sunday",
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
]
VALID_BODY_DISKFULL = [
    "overwrite",
    "nolog",
]
VALID_BODY_UPLOAD = [
    "enable",
    "disable",
]
VALID_BODY_UPLOAD_DESTINATION = [
    "ftp-server",
]
VALID_BODY_UPLOADTYPE = [
    "traffic",
    "event",
    "virus",
    "webfilter",
    "IPS",
    "emailfilter",
    "dlp-archive",
    "anomaly",
    "voip",
    "dlp",
    "app-ctrl",
    "waf",
    "gtp",
    "dns",
    "ssh",
    "ssl",
    "file-filter",
    "icap",
    "virtual-patch",
    "debug",
]
VALID_BODY_UPLOADSCHED = [
    "disable",
    "enable",
]
VALID_BODY_UPLOAD_DELETE_FILES = [
    "enable",
    "disable",
]
VALID_BODY_UPLOAD_SSL_CONN = [
    "default",
    "high",
    "low",
    "disable",
]
VALID_BODY_INTERFACE_SELECT_METHOD = [
    "auto",
    "sdwan",
    "specify",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_log_disk_setting_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for log/disk_setting.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_log_disk_setting_get()
        >>> assert is_valid == True
        
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_log_disk_setting_get(
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
    Validate required fields for log/disk_setting.

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


def validate_log_disk_setting_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new log/disk_setting object.

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
        ...     "uploaduser": True,  # Username required to log into the FTP server to up
        ...     "interface": True,  # Specify outgoing interface to reach server.
        ... }
        >>> is_valid, error = validate_log_disk_setting_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "uploaduser": True,
        ...     "status": "enable",  # Valid enum value
        ... }
        >>> is_valid, error = validate_log_disk_setting_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["status"] = "invalid-value"
        >>> is_valid, error = validate_log_disk_setting_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_log_disk_setting_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
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
    if "ips-archive" in payload:
        value = payload["ips-archive"]
        if value not in VALID_BODY_IPS_ARCHIVE:
            desc = FIELD_DESCRIPTIONS.get("ips-archive", "")
            error_msg = f"Invalid value for 'ips-archive': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IPS_ARCHIVE)}"
            error_msg += f"\n  → Example: ips-archive='{{ VALID_BODY_IPS_ARCHIVE[0] }}'"
            return (False, error_msg)
    if "roll-schedule" in payload:
        value = payload["roll-schedule"]
        if value not in VALID_BODY_ROLL_SCHEDULE:
            desc = FIELD_DESCRIPTIONS.get("roll-schedule", "")
            error_msg = f"Invalid value for 'roll-schedule': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ROLL_SCHEDULE)}"
            error_msg += f"\n  → Example: roll-schedule='{{ VALID_BODY_ROLL_SCHEDULE[0] }}'"
            return (False, error_msg)
    if "roll-day" in payload:
        value = payload["roll-day"]
        if value not in VALID_BODY_ROLL_DAY:
            desc = FIELD_DESCRIPTIONS.get("roll-day", "")
            error_msg = f"Invalid value for 'roll-day': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ROLL_DAY)}"
            error_msg += f"\n  → Example: roll-day='{{ VALID_BODY_ROLL_DAY[0] }}'"
            return (False, error_msg)
    if "diskfull" in payload:
        value = payload["diskfull"]
        if value not in VALID_BODY_DISKFULL:
            desc = FIELD_DESCRIPTIONS.get("diskfull", "")
            error_msg = f"Invalid value for 'diskfull': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DISKFULL)}"
            error_msg += f"\n  → Example: diskfull='{{ VALID_BODY_DISKFULL[0] }}'"
            return (False, error_msg)
    if "upload" in payload:
        value = payload["upload"]
        if value not in VALID_BODY_UPLOAD:
            desc = FIELD_DESCRIPTIONS.get("upload", "")
            error_msg = f"Invalid value for 'upload': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_UPLOAD)}"
            error_msg += f"\n  → Example: upload='{{ VALID_BODY_UPLOAD[0] }}'"
            return (False, error_msg)
    if "upload-destination" in payload:
        value = payload["upload-destination"]
        if value not in VALID_BODY_UPLOAD_DESTINATION:
            desc = FIELD_DESCRIPTIONS.get("upload-destination", "")
            error_msg = f"Invalid value for 'upload-destination': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_UPLOAD_DESTINATION)}"
            error_msg += f"\n  → Example: upload-destination='{{ VALID_BODY_UPLOAD_DESTINATION[0] }}'"
            return (False, error_msg)
    if "uploadtype" in payload:
        value = payload["uploadtype"]
        if value not in VALID_BODY_UPLOADTYPE:
            desc = FIELD_DESCRIPTIONS.get("uploadtype", "")
            error_msg = f"Invalid value for 'uploadtype': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_UPLOADTYPE)}"
            error_msg += f"\n  → Example: uploadtype='{{ VALID_BODY_UPLOADTYPE[0] }}'"
            return (False, error_msg)
    if "uploadsched" in payload:
        value = payload["uploadsched"]
        if value not in VALID_BODY_UPLOADSCHED:
            desc = FIELD_DESCRIPTIONS.get("uploadsched", "")
            error_msg = f"Invalid value for 'uploadsched': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_UPLOADSCHED)}"
            error_msg += f"\n  → Example: uploadsched='{{ VALID_BODY_UPLOADSCHED[0] }}'"
            return (False, error_msg)
    if "upload-delete-files" in payload:
        value = payload["upload-delete-files"]
        if value not in VALID_BODY_UPLOAD_DELETE_FILES:
            desc = FIELD_DESCRIPTIONS.get("upload-delete-files", "")
            error_msg = f"Invalid value for 'upload-delete-files': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_UPLOAD_DELETE_FILES)}"
            error_msg += f"\n  → Example: upload-delete-files='{{ VALID_BODY_UPLOAD_DELETE_FILES[0] }}'"
            return (False, error_msg)
    if "upload-ssl-conn" in payload:
        value = payload["upload-ssl-conn"]
        if value not in VALID_BODY_UPLOAD_SSL_CONN:
            desc = FIELD_DESCRIPTIONS.get("upload-ssl-conn", "")
            error_msg = f"Invalid value for 'upload-ssl-conn': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_UPLOAD_SSL_CONN)}"
            error_msg += f"\n  → Example: upload-ssl-conn='{{ VALID_BODY_UPLOAD_SSL_CONN[0] }}'"
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


def validate_log_disk_setting_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update log/disk_setting.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_log_disk_setting_put(payload)
    """
    # Step 1: Validate enum values
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid value for 'status'='{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )
    if "ips-archive" in payload:
        value = payload["ips-archive"]
        if value not in VALID_BODY_IPS_ARCHIVE:
            return (
                False,
                f"Invalid value for 'ips-archive'='{value}'. Must be one of: {', '.join(VALID_BODY_IPS_ARCHIVE)}",
            )
    if "roll-schedule" in payload:
        value = payload["roll-schedule"]
        if value not in VALID_BODY_ROLL_SCHEDULE:
            return (
                False,
                f"Invalid value for 'roll-schedule'='{value}'. Must be one of: {', '.join(VALID_BODY_ROLL_SCHEDULE)}",
            )
    if "roll-day" in payload:
        value = payload["roll-day"]
        if value not in VALID_BODY_ROLL_DAY:
            return (
                False,
                f"Invalid value for 'roll-day'='{value}'. Must be one of: {', '.join(VALID_BODY_ROLL_DAY)}",
            )
    if "diskfull" in payload:
        value = payload["diskfull"]
        if value not in VALID_BODY_DISKFULL:
            return (
                False,
                f"Invalid value for 'diskfull'='{value}'. Must be one of: {', '.join(VALID_BODY_DISKFULL)}",
            )
    if "upload" in payload:
        value = payload["upload"]
        if value not in VALID_BODY_UPLOAD:
            return (
                False,
                f"Invalid value for 'upload'='{value}'. Must be one of: {', '.join(VALID_BODY_UPLOAD)}",
            )
    if "upload-destination" in payload:
        value = payload["upload-destination"]
        if value not in VALID_BODY_UPLOAD_DESTINATION:
            return (
                False,
                f"Invalid value for 'upload-destination'='{value}'. Must be one of: {', '.join(VALID_BODY_UPLOAD_DESTINATION)}",
            )
    if "uploadtype" in payload:
        value = payload["uploadtype"]
        if value not in VALID_BODY_UPLOADTYPE:
            return (
                False,
                f"Invalid value for 'uploadtype'='{value}'. Must be one of: {', '.join(VALID_BODY_UPLOADTYPE)}",
            )
    if "uploadsched" in payload:
        value = payload["uploadsched"]
        if value not in VALID_BODY_UPLOADSCHED:
            return (
                False,
                f"Invalid value for 'uploadsched'='{value}'. Must be one of: {', '.join(VALID_BODY_UPLOADSCHED)}",
            )
    if "upload-delete-files" in payload:
        value = payload["upload-delete-files"]
        if value not in VALID_BODY_UPLOAD_DELETE_FILES:
            return (
                False,
                f"Invalid value for 'upload-delete-files'='{value}'. Must be one of: {', '.join(VALID_BODY_UPLOAD_DELETE_FILES)}",
            )
    if "upload-ssl-conn" in payload:
        value = payload["upload-ssl-conn"]
        if value not in VALID_BODY_UPLOAD_SSL_CONN:
            return (
                False,
                f"Invalid value for 'upload-ssl-conn'='{value}'. Must be one of: {', '.join(VALID_BODY_UPLOAD_SSL_CONN)}",
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
    constant_name = f"VALID_BODY_{field_name.replace('-', '_').upper()}"
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
    "endpoint": "log/disk_setting",
    "category": "cmdb",
    "api_path": "log.disk/setting",
    "help": "Settings for local disk logging.",
    "total_fields": 31,
    "required_fields_count": 2,
    "fields_with_defaults_count": 30,
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
