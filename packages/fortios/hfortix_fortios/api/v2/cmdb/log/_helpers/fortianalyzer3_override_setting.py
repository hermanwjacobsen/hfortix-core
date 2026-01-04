"""
Validation helpers for log/fortianalyzer3_override_setting endpoint.

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
    "server",  # The remote FortiAnalyzer.
    "interface",  # Specify outgoing interface to reach server.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "use-management-vdom": "disable",
    "status": "disable",
    "ips-archive": "enable",
    "server": "",
    "alt-server": "",
    "fallback-to-primary": "enable",
    "certificate-verification": "enable",
    "server-cert-ca": "",
    "preshared-key": "",
    "access-config": "enable",
    "hmac-algorithm": "sha256",
    "enc-algorithm": "high",
    "ssl-min-proto-version": "default",
    "conn-timeout": 10,
    "monitor-keepalive-period": 5,
    "monitor-failure-retry-period": 5,
    "certificate": "",
    "source-ip": "",
    "upload-option": "5-minute",
    "upload-interval": "daily",
    "upload-day": "",
    "upload-time": "",
    "reliable": "disable",
    "priority": "default",
    "max-log-rate": 0,
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
    "use-management-vdom": "option",  # Enable/disable use of management VDOM IP address as source I
    "status": "option",  # Enable/disable logging to FortiAnalyzer.
    "ips-archive": "option",  # Enable/disable IPS packet archive logging.
    "server": "string",  # The remote FortiAnalyzer.
    "alt-server": "string",  # Alternate FortiAnalyzer.
    "fallback-to-primary": "option",  # Enable/disable this FortiGate unit to fallback to the primar
    "certificate-verification": "option",  # Enable/disable identity verification of FortiAnalyzer by use
    "serial": "string",  # Serial numbers of the FortiAnalyzer.
    "server-cert-ca": "string",  # Mandatory CA on FortiGate in certificate chain of server.
    "preshared-key": "string",  # Preshared-key used for auto-authorization on FortiAnalyzer.
    "access-config": "option",  # Enable/disable FortiAnalyzer access to configuration and dat
    "hmac-algorithm": "option",  # OFTP login hash algorithm.
    "enc-algorithm": "option",  # Configure the level of SSL protection for secure communicati
    "ssl-min-proto-version": "option",  # Minimum supported protocol version for SSL/TLS connections (
    "conn-timeout": "integer",  # FortiAnalyzer connection time-out in seconds (for status and
    "monitor-keepalive-period": "integer",  # Time between OFTP keepalives in seconds (for status and log 
    "monitor-failure-retry-period": "integer",  # Time between FortiAnalyzer connection retries in seconds (fo
    "certificate": "string",  # Certificate used to communicate with FortiAnalyzer.
    "source-ip": "string",  # Source IPv4 or IPv6 address used to communicate with FortiAn
    "upload-option": "option",  # Enable/disable logging to hard disk and then uploading to Fo
    "upload-interval": "option",  # Frequency to upload log files to FortiAnalyzer.
    "upload-day": "user",  # Day of week (month) to upload logs.
    "upload-time": "user",  # Time to upload logs (hh:mm).
    "reliable": "option",  # Enable/disable reliable logging to FortiAnalyzer.
    "priority": "option",  # Set log transmission priority.
    "max-log-rate": "integer",  # FortiAnalyzer maximum log rate in MBps (0 = unlimited).
    "interface-select-method": "option",  # Specify how to select outgoing interface to reach server.
    "interface": "string",  # Specify outgoing interface to reach server.
    "vrf-select": "integer",  # VRF ID used for connection to server.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "use-management-vdom": "Enable/disable use of management VDOM IP address as source IP for logs sent to FortiAnalyzer.",
    "status": "Enable/disable logging to FortiAnalyzer.",
    "ips-archive": "Enable/disable IPS packet archive logging.",
    "server": "The remote FortiAnalyzer.",
    "alt-server": "Alternate FortiAnalyzer.",
    "fallback-to-primary": "Enable/disable this FortiGate unit to fallback to the primary FortiAnalyzer when it is available.",
    "certificate-verification": "Enable/disable identity verification of FortiAnalyzer by use of certificate.",
    "serial": "Serial numbers of the FortiAnalyzer.",
    "server-cert-ca": "Mandatory CA on FortiGate in certificate chain of server.",
    "preshared-key": "Preshared-key used for auto-authorization on FortiAnalyzer.",
    "access-config": "Enable/disable FortiAnalyzer access to configuration and data.",
    "hmac-algorithm": "OFTP login hash algorithm.",
    "enc-algorithm": "Configure the level of SSL protection for secure communication with FortiAnalyzer.",
    "ssl-min-proto-version": "Minimum supported protocol version for SSL/TLS connections (default is to follow system global setting).",
    "conn-timeout": "FortiAnalyzer connection time-out in seconds (for status and log buffer).",
    "monitor-keepalive-period": "Time between OFTP keepalives in seconds (for status and log buffer).",
    "monitor-failure-retry-period": "Time between FortiAnalyzer connection retries in seconds (for status and log buffer).",
    "certificate": "Certificate used to communicate with FortiAnalyzer.",
    "source-ip": "Source IPv4 or IPv6 address used to communicate with FortiAnalyzer.",
    "upload-option": "Enable/disable logging to hard disk and then uploading to FortiAnalyzer.",
    "upload-interval": "Frequency to upload log files to FortiAnalyzer.",
    "upload-day": "Day of week (month) to upload logs.",
    "upload-time": "Time to upload logs (hh:mm).",
    "reliable": "Enable/disable reliable logging to FortiAnalyzer.",
    "priority": "Set log transmission priority.",
    "max-log-rate": "FortiAnalyzer maximum log rate in MBps (0 = unlimited).",
    "interface-select-method": "Specify how to select outgoing interface to reach server.",
    "interface": "Specify outgoing interface to reach server.",
    "vrf-select": "VRF ID used for connection to server.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "server": {"type": "string", "max_length": 127},
    "alt-server": {"type": "string", "max_length": 127},
    "server-cert-ca": {"type": "string", "max_length": 79},
    "preshared-key": {"type": "string", "max_length": 63},
    "conn-timeout": {"type": "integer", "min": 1, "max": 3600},
    "monitor-keepalive-period": {"type": "integer", "min": 1, "max": 120},
    "monitor-failure-retry-period": {"type": "integer", "min": 1, "max": 86400},
    "certificate": {"type": "string", "max_length": 35},
    "source-ip": {"type": "string", "max_length": 63},
    "max-log-rate": {"type": "integer", "min": 0, "max": 100000},
    "interface": {"type": "string", "max_length": 15},
    "vrf-select": {"type": "integer", "min": 0, "max": 511},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "serial": {
        "name": {
            "type": "string",
            "help": "Serial Number.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_USE_MANAGEMENT_VDOM = [
    "enable",
    "disable",
]
VALID_BODY_STATUS = [
    "enable",
    "disable",
]
VALID_BODY_IPS_ARCHIVE = [
    "enable",
    "disable",
]
VALID_BODY_FALLBACK_TO_PRIMARY = [
    "enable",
    "disable",
]
VALID_BODY_CERTIFICATE_VERIFICATION = [
    "enable",
    "disable",
]
VALID_BODY_ACCESS_CONFIG = [
    "enable",
    "disable",
]
VALID_BODY_HMAC_ALGORITHM = [
    "sha256",
]
VALID_BODY_ENC_ALGORITHM = [
    "high-medium",
    "high",
    "low",
]
VALID_BODY_SSL_MIN_PROTO_VERSION = [
    "default",
    "SSLv3",
    "TLSv1",
    "TLSv1-1",
    "TLSv1-2",
    "TLSv1-3",
]
VALID_BODY_UPLOAD_OPTION = [
    "store-and-upload",
    "realtime",
    "1-minute",
    "5-minute",
]
VALID_BODY_UPLOAD_INTERVAL = [
    "daily",
    "weekly",
    "monthly",
]
VALID_BODY_RELIABLE = [
    "enable",
    "disable",
]
VALID_BODY_PRIORITY = [
    "default",
    "low",
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


def validate_log_fortianalyzer3_override_setting_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for log/fortianalyzer3_override_setting.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_log_fortianalyzer3_override_setting_get()
        >>> assert is_valid == True
        
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_log_fortianalyzer3_override_setting_get(
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
    Validate required fields for log/fortianalyzer3_override_setting.

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


def validate_log_fortianalyzer3_override_setting_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new log/fortianalyzer3_override_setting object.

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
        ...     "server": True,  # The remote FortiAnalyzer.
        ...     "interface": True,  # Specify outgoing interface to reach server.
        ... }
        >>> is_valid, error = validate_log_fortianalyzer3_override_setting_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "server": True,
        ...     "use-management-vdom": "enable",  # Valid enum value
        ... }
        >>> is_valid, error = validate_log_fortianalyzer3_override_setting_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["use-management-vdom"] = "invalid-value"
        >>> is_valid, error = validate_log_fortianalyzer3_override_setting_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_log_fortianalyzer3_override_setting_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "use-management-vdom" in payload:
        value = payload["use-management-vdom"]
        if value not in VALID_BODY_USE_MANAGEMENT_VDOM:
            desc = FIELD_DESCRIPTIONS.get("use-management-vdom", "")
            error_msg = f"Invalid value for 'use-management-vdom': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_USE_MANAGEMENT_VDOM)}"
            error_msg += f"\n  → Example: use-management-vdom='{{ VALID_BODY_USE_MANAGEMENT_VDOM[0] }}'"
            return (False, error_msg)
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
    if "fallback-to-primary" in payload:
        value = payload["fallback-to-primary"]
        if value not in VALID_BODY_FALLBACK_TO_PRIMARY:
            desc = FIELD_DESCRIPTIONS.get("fallback-to-primary", "")
            error_msg = f"Invalid value for 'fallback-to-primary': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FALLBACK_TO_PRIMARY)}"
            error_msg += f"\n  → Example: fallback-to-primary='{{ VALID_BODY_FALLBACK_TO_PRIMARY[0] }}'"
            return (False, error_msg)
    if "certificate-verification" in payload:
        value = payload["certificate-verification"]
        if value not in VALID_BODY_CERTIFICATE_VERIFICATION:
            desc = FIELD_DESCRIPTIONS.get("certificate-verification", "")
            error_msg = f"Invalid value for 'certificate-verification': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CERTIFICATE_VERIFICATION)}"
            error_msg += f"\n  → Example: certificate-verification='{{ VALID_BODY_CERTIFICATE_VERIFICATION[0] }}'"
            return (False, error_msg)
    if "access-config" in payload:
        value = payload["access-config"]
        if value not in VALID_BODY_ACCESS_CONFIG:
            desc = FIELD_DESCRIPTIONS.get("access-config", "")
            error_msg = f"Invalid value for 'access-config': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ACCESS_CONFIG)}"
            error_msg += f"\n  → Example: access-config='{{ VALID_BODY_ACCESS_CONFIG[0] }}'"
            return (False, error_msg)
    if "hmac-algorithm" in payload:
        value = payload["hmac-algorithm"]
        if value not in VALID_BODY_HMAC_ALGORITHM:
            desc = FIELD_DESCRIPTIONS.get("hmac-algorithm", "")
            error_msg = f"Invalid value for 'hmac-algorithm': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_HMAC_ALGORITHM)}"
            error_msg += f"\n  → Example: hmac-algorithm='{{ VALID_BODY_HMAC_ALGORITHM[0] }}'"
            return (False, error_msg)
    if "enc-algorithm" in payload:
        value = payload["enc-algorithm"]
        if value not in VALID_BODY_ENC_ALGORITHM:
            desc = FIELD_DESCRIPTIONS.get("enc-algorithm", "")
            error_msg = f"Invalid value for 'enc-algorithm': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ENC_ALGORITHM)}"
            error_msg += f"\n  → Example: enc-algorithm='{{ VALID_BODY_ENC_ALGORITHM[0] }}'"
            return (False, error_msg)
    if "ssl-min-proto-version" in payload:
        value = payload["ssl-min-proto-version"]
        if value not in VALID_BODY_SSL_MIN_PROTO_VERSION:
            desc = FIELD_DESCRIPTIONS.get("ssl-min-proto-version", "")
            error_msg = f"Invalid value for 'ssl-min-proto-version': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSL_MIN_PROTO_VERSION)}"
            error_msg += f"\n  → Example: ssl-min-proto-version='{{ VALID_BODY_SSL_MIN_PROTO_VERSION[0] }}'"
            return (False, error_msg)
    if "upload-option" in payload:
        value = payload["upload-option"]
        if value not in VALID_BODY_UPLOAD_OPTION:
            desc = FIELD_DESCRIPTIONS.get("upload-option", "")
            error_msg = f"Invalid value for 'upload-option': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_UPLOAD_OPTION)}"
            error_msg += f"\n  → Example: upload-option='{{ VALID_BODY_UPLOAD_OPTION[0] }}'"
            return (False, error_msg)
    if "upload-interval" in payload:
        value = payload["upload-interval"]
        if value not in VALID_BODY_UPLOAD_INTERVAL:
            desc = FIELD_DESCRIPTIONS.get("upload-interval", "")
            error_msg = f"Invalid value for 'upload-interval': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_UPLOAD_INTERVAL)}"
            error_msg += f"\n  → Example: upload-interval='{{ VALID_BODY_UPLOAD_INTERVAL[0] }}'"
            return (False, error_msg)
    if "reliable" in payload:
        value = payload["reliable"]
        if value not in VALID_BODY_RELIABLE:
            desc = FIELD_DESCRIPTIONS.get("reliable", "")
            error_msg = f"Invalid value for 'reliable': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_RELIABLE)}"
            error_msg += f"\n  → Example: reliable='{{ VALID_BODY_RELIABLE[0] }}'"
            return (False, error_msg)
    if "priority" in payload:
        value = payload["priority"]
        if value not in VALID_BODY_PRIORITY:
            desc = FIELD_DESCRIPTIONS.get("priority", "")
            error_msg = f"Invalid value for 'priority': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PRIORITY)}"
            error_msg += f"\n  → Example: priority='{{ VALID_BODY_PRIORITY[0] }}'"
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


def validate_log_fortianalyzer3_override_setting_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update log/fortianalyzer3_override_setting.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_log_fortianalyzer3_override_setting_put(payload)
    """
    # Step 1: Validate enum values
    if "use-management-vdom" in payload:
        value = payload["use-management-vdom"]
        if value not in VALID_BODY_USE_MANAGEMENT_VDOM:
            return (
                False,
                f"Invalid value for 'use-management-vdom'='{value}'. Must be one of: {', '.join(VALID_BODY_USE_MANAGEMENT_VDOM)}",
            )
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
    if "fallback-to-primary" in payload:
        value = payload["fallback-to-primary"]
        if value not in VALID_BODY_FALLBACK_TO_PRIMARY:
            return (
                False,
                f"Invalid value for 'fallback-to-primary'='{value}'. Must be one of: {', '.join(VALID_BODY_FALLBACK_TO_PRIMARY)}",
            )
    if "certificate-verification" in payload:
        value = payload["certificate-verification"]
        if value not in VALID_BODY_CERTIFICATE_VERIFICATION:
            return (
                False,
                f"Invalid value for 'certificate-verification'='{value}'. Must be one of: {', '.join(VALID_BODY_CERTIFICATE_VERIFICATION)}",
            )
    if "access-config" in payload:
        value = payload["access-config"]
        if value not in VALID_BODY_ACCESS_CONFIG:
            return (
                False,
                f"Invalid value for 'access-config'='{value}'. Must be one of: {', '.join(VALID_BODY_ACCESS_CONFIG)}",
            )
    if "hmac-algorithm" in payload:
        value = payload["hmac-algorithm"]
        if value not in VALID_BODY_HMAC_ALGORITHM:
            return (
                False,
                f"Invalid value for 'hmac-algorithm'='{value}'. Must be one of: {', '.join(VALID_BODY_HMAC_ALGORITHM)}",
            )
    if "enc-algorithm" in payload:
        value = payload["enc-algorithm"]
        if value not in VALID_BODY_ENC_ALGORITHM:
            return (
                False,
                f"Invalid value for 'enc-algorithm'='{value}'. Must be one of: {', '.join(VALID_BODY_ENC_ALGORITHM)}",
            )
    if "ssl-min-proto-version" in payload:
        value = payload["ssl-min-proto-version"]
        if value not in VALID_BODY_SSL_MIN_PROTO_VERSION:
            return (
                False,
                f"Invalid value for 'ssl-min-proto-version'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL_MIN_PROTO_VERSION)}",
            )
    if "upload-option" in payload:
        value = payload["upload-option"]
        if value not in VALID_BODY_UPLOAD_OPTION:
            return (
                False,
                f"Invalid value for 'upload-option'='{value}'. Must be one of: {', '.join(VALID_BODY_UPLOAD_OPTION)}",
            )
    if "upload-interval" in payload:
        value = payload["upload-interval"]
        if value not in VALID_BODY_UPLOAD_INTERVAL:
            return (
                False,
                f"Invalid value for 'upload-interval'='{value}'. Must be one of: {', '.join(VALID_BODY_UPLOAD_INTERVAL)}",
            )
    if "reliable" in payload:
        value = payload["reliable"]
        if value not in VALID_BODY_RELIABLE:
            return (
                False,
                f"Invalid value for 'reliable'='{value}'. Must be one of: {', '.join(VALID_BODY_RELIABLE)}",
            )
    if "priority" in payload:
        value = payload["priority"]
        if value not in VALID_BODY_PRIORITY:
            return (
                False,
                f"Invalid value for 'priority'='{value}'. Must be one of: {', '.join(VALID_BODY_PRIORITY)}",
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
    "endpoint": "log/fortianalyzer3_override_setting",
    "category": "cmdb",
    "api_path": "log.fortianalyzer3/override-setting",
    "help": "Override FortiAnalyzer settings.",
    "total_fields": 29,
    "required_fields_count": 2,
    "fields_with_defaults_count": 28,
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
