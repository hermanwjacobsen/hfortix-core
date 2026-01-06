"""Validation helpers for log/disk/setting - Auto-generated"""

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
    "enable",  # Log to local disk.
    "disable",  # Do not log to local disk.
]
VALID_BODY_IPS_ARCHIVE = [
    "enable",  # Enable IPS packet archiving.
    "disable",  # Disable IPS packet archiving.
]
VALID_BODY_ROLL_SCHEDULE = [
    "daily",  # Check the log file once a day.
    "weekly",  # Check the log file once a week.
]
VALID_BODY_ROLL_DAY = [
    "sunday",  # Sunday
    "monday",  # Monday
    "tuesday",  # Tuesday
    "wednesday",  # Wednesday
    "thursday",  # Thursday
    "friday",  # Friday
    "saturday",  # Saturday
]
VALID_BODY_DISKFULL = [
    "overwrite",  # Overwrite the oldest logs when the log disk is full.
    "nolog",  # Stop logging when the log disk is full.
]
VALID_BODY_UPLOAD = [
    "enable",  # Enable uploading log files when they are rolled.
    "disable",  # Disable uploading log files when they are rolled.
]
VALID_BODY_UPLOAD_DESTINATION = [
    "ftp-server",  # Upload rolled log files to an FTP server.
]
VALID_BODY_UPLOADTYPE = [
    "traffic",  # Upload traffic log.
    "event",  # Upload event log.
    "virus",  # Upload anti-virus log.
    "webfilter",  # Upload web filter log.
    "IPS",  # Upload IPS log.
    "emailfilter",  # Upload spam filter log.
    "dlp-archive",  # Upload DLP archive.
    "anomaly",  # Upload anomaly log.
    "voip",  # Upload VoIP log.
    "dlp",  # Upload DLP log.
    "app-ctrl",  # Upload application control log.
    "waf",  # Upload web application firewall log.
    "gtp",  # Upload GTP log.
    "dns",  # Upload DNS log.
    "ssh",  # Upload SSH log.
    "ssl",  # Upload SSL log.
    "file-filter",  # Upload file-filter log.
    "icap",  # Upload ICAP log.
    "virtual-patch",  # Upload virtual-patch log.
    "debug",  # Upload debug log.
]
VALID_BODY_UPLOADSCHED = [
    "disable",  # Upload when rolling.
    "enable",  # Scheduled upload.
]
VALID_BODY_UPLOAD_DELETE_FILES = [
    "enable",  # Delete log files after uploading.
    "disable",  # Do not delete log files after uploading.
]
VALID_BODY_UPLOAD_SSL_CONN = [
    "default",  # FTPS with high and medium encryption algorithms.
    "high",  # FTPS with high encryption algorithms.
    "low",  # FTPS with low encryption algorithms.
    "disable",  # Disable FTPS communication.
]
VALID_BODY_INTERFACE_SELECT_METHOD = [
    "auto",  # Set outgoing interface automatically.
    "sdwan",  # Set outgoing interface by SD-WAN or policy routing rules.
    "specify",  # Set outgoing interface manually.
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
    """Validate GET request parameters for log/disk/setting."""
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
    """Validate required fields for log/disk/setting."""
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
    """Validate POST request to create new log/disk/setting object."""
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
    """Validate PUT request to update log/disk/setting."""
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
    "endpoint": "log/disk/setting",
    "category": "cmdb",
    "api_path": "log.disk/setting",
    "help": "Settings for local disk logging.",
    "total_fields": 31,
    "required_fields_count": 2,
    "fields_with_defaults_count": 30,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
