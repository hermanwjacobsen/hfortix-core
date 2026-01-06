"""Validation helpers for log/threat_weight - Auto-generated"""

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
    "status": "enable",
    "blocked-connection": "high",
    "failed-connection": "low",
    "url-block-detected": "high",
    "botnet-connection-detected": "critical",
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
    "status": "option",  # Enable/disable the threat weight feature.
    "level": "string",  # Score mapping for threat weight levels.
    "blocked-connection": "option",  # Threat weight score for blocked connections.
    "failed-connection": "option",  # Threat weight score for failed connections.
    "url-block-detected": "option",  # Threat weight score for URL blocking.
    "botnet-connection-detected": "option",  # Threat weight score for detected botnet connections.
    "malware": "string",  # Anti-virus malware threat weight settings.
    "ips": "string",  # IPS threat weight settings.
    "web": "string",  # Web filtering threat weight settings.
    "geolocation": "string",  # Geolocation-based threat weight settings.
    "application": "string",  # Application-control threat weight settings.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "status": "Enable/disable the threat weight feature.",
    "level": "Score mapping for threat weight levels.",
    "blocked-connection": "Threat weight score for blocked connections.",
    "failed-connection": "Threat weight score for failed connections.",
    "url-block-detected": "Threat weight score for URL blocking.",
    "botnet-connection-detected": "Threat weight score for detected botnet connections.",
    "malware": "Anti-virus malware threat weight settings.",
    "ips": "IPS threat weight settings.",
    "web": "Web filtering threat weight settings.",
    "geolocation": "Geolocation-based threat weight settings.",
    "application": "Application-control threat weight settings.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "level": {
        "low": {
            "type": "integer",
            "help": "Low level score value (1 - 100).",
            "default": 5,
            "min_value": 1,
            "max_value": 100,
        },
        "medium": {
            "type": "integer",
            "help": "Medium level score value (1 - 100).",
            "default": 10,
            "min_value": 1,
            "max_value": 100,
        },
        "high": {
            "type": "integer",
            "help": "High level score value (1 - 100).",
            "default": 30,
            "min_value": 1,
            "max_value": 100,
        },
        "critical": {
            "type": "integer",
            "help": "Critical level score value (1 - 100).",
            "default": 50,
            "min_value": 1,
            "max_value": 100,
        },
    },
    "malware": {
        "virus-infected": {
            "type": "option",
            "help": "Threat weight score for virus (infected) detected.",
            "default": "critical",
            "options": [{"help": "Disable threat weight scoring for virus (infected) detected.", "label": "Disable", "name": "disable"}, {"help": "Use the low level score for virus (infected) detected.", "label": "Low", "name": "low"}, {"help": "Use the medium level score for virus (infected) detected.", "label": "Medium", "name": "medium"}, {"help": "Use the high level score for virus (infected) detected.", "label": "High", "name": "high"}, {"help": "Use the critical level score for virus (infected) detected.", "label": "Critical", "name": "critical"}],
        },
        "inline-block": {
            "type": "option",
            "help": "Threat weight score for malware detected by inline block.",
            "default": "critical",
            "options": [{"help": "Disable threat weight scoring for virus detected by inline block.", "label": "Disable", "name": "disable"}, {"help": "Use the low level score for virus detected by inline block.", "label": "Low", "name": "low"}, {"help": "Use the medium level score for virus detected by inline block.", "label": "Medium", "name": "medium"}, {"help": "Use the high level score for virus detected by inline block.", "label": "High", "name": "high"}, {"help": "Use the critical level score for virus detected by inline block.", "label": "Critical", "name": "critical"}],
        },
        "file-blocked": {
            "type": "option",
            "help": "Threat weight score for blocked file detected.",
            "default": "low",
            "options": [{"help": "Disable threat weight scoring for blocked file detected.", "label": "Disable", "name": "disable"}, {"help": "Use the low level score for blocked file detected.", "label": "Low", "name": "low"}, {"help": "Use the medium level score for blocked file detected.", "label": "Medium", "name": "medium"}, {"help": "Use the high level score for blocked file detected.", "label": "High", "name": "high"}, {"help": "Use the critical level score for blocked file detected.", "label": "Critical", "name": "critical"}],
        },
        "command-blocked": {
            "type": "option",
            "help": "Threat weight score for blocked command detected.",
            "default": "disable",
            "options": [{"help": "Disable threat weight scoring for blocked command detected.", "label": "Disable", "name": "disable"}, {"help": "Use the low level score for blocked command detected.", "label": "Low", "name": "low"}, {"help": "Use the medium level score for blocked command detected.", "label": "Medium", "name": "medium"}, {"help": "Use the high level score for blocked command detected.", "label": "High", "name": "high"}, {"help": "Use the critical level score for blocked command detected.", "label": "Critical", "name": "critical"}],
        },
        "oversized": {
            "type": "option",
            "help": "Threat weight score for oversized file detected.",
            "default": "disable",
            "options": [{"help": "Disable threat weight scoring for oversized file detected.", "label": "Disable", "name": "disable"}, {"help": "Use the low level score for oversized file detected.", "label": "Low", "name": "low"}, {"help": "Use the medium level score for oversized file detected.", "label": "Medium", "name": "medium"}, {"help": "Use the high level score for oversized file detected.", "label": "High", "name": "high"}, {"help": "Use the critical level score for oversized file detected.", "label": "Critical", "name": "critical"}],
        },
        "virus-scan-error": {
            "type": "option",
            "help": "Threat weight score for virus (scan error) detected.",
            "default": "high",
            "options": [{"help": "Disable threat weight scoring for virus (scan error) detected.", "label": "Disable", "name": "disable"}, {"help": "Use the low level score for virus (scan error) detected.", "label": "Low", "name": "low"}, {"help": "Use the medium level score for virus (scan error) detected.", "label": "Medium", "name": "medium"}, {"help": "Use the high level score for virus (scan error) detected.", "label": "High", "name": "high"}, {"help": "Use the critical level score for virus (scan error) detected.", "label": "Critical", "name": "critical"}],
        },
        "switch-proto": {
            "type": "option",
            "help": "Threat weight score for switch proto detected.",
            "default": "disable",
            "options": [{"help": "Disable threat weight scoring for switch proto detected.", "label": "Disable", "name": "disable"}, {"help": "Use the low level score for switch proto detected.", "label": "Low", "name": "low"}, {"help": "Use the medium level score for switch proto detected.", "label": "Medium", "name": "medium"}, {"help": "Use the high level score for switch proto detected.", "label": "High", "name": "high"}, {"help": "Use the critical level score for switch proto detected.", "label": "Critical", "name": "critical"}],
        },
        "mimefragmented": {
            "type": "option",
            "help": "Threat weight score for mimefragmented detected.",
            "default": "disable",
            "options": [{"help": "Disable threat weight scoring for mimefragmented detected.", "label": "Disable", "name": "disable"}, {"help": "Use the low level score for mimefragmented detected.", "label": "Low", "name": "low"}, {"help": "Use the medium level score for mimefragmented detected.", "label": "Medium", "name": "medium"}, {"help": "Use the high level score for mimefragmented detected.", "label": "High", "name": "high"}, {"help": "Use the critical level score for mimefragmented detected.", "label": "Critical", "name": "critical"}],
        },
        "virus-file-type-executable": {
            "type": "option",
            "help": "Threat weight score for virus (file type executable) detected.",
            "default": "medium",
            "options": [{"help": "Disable threat weight scoring for virus (filetype executable) detected.", "label": "Disable", "name": "disable"}, {"help": "Use the low level score for virus (filetype executable) detected.", "label": "Low", "name": "low"}, {"help": "Use the medium level score for virus (filetype executable) detected.", "label": "Medium", "name": "medium"}, {"help": "Use the high level score for virus (filetype executable) detected.", "label": "High", "name": "high"}, {"help": "Use the critical level score for virus (filetype executable) detected.", "label": "Critical", "name": "critical"}],
        },
        "virus-outbreak-prevention": {
            "type": "option",
            "help": "Threat weight score for virus (outbreak prevention) event.",
            "default": "critical",
            "options": [{"help": "Disable threat weight scoring for virus (outbreak prevention) event.", "label": "Disable", "name": "disable"}, {"help": "Use the low level score for virus (outbreak prevention) event.", "label": "Low", "name": "low"}, {"help": "Use the medium level score for virus (outbreak prevention) event.", "label": "Medium", "name": "medium"}, {"help": "Use the high level score for virus (outbreak prevention) event.", "label": "High", "name": "high"}, {"help": "Use the critical level score for virus (outbreak prevention) event.", "label": "Critical", "name": "critical"}],
        },
        "content-disarm": {
            "type": "option",
            "help": "Threat weight score for virus (content disarm) detected.",
            "default": "medium",
            "options": [{"help": "Disable threat weight scoring for virus (content disarm) detected.", "label": "Disable", "name": "disable"}, {"help": "Use the low level score for virus (content disarm) detected.", "label": "Low", "name": "low"}, {"help": "Use the medium level score for virus (content disarm) detected.", "label": "Medium", "name": "medium"}, {"help": "Use the high level score for virus (content disarm) detected.", "label": "High", "name": "high"}, {"help": "Use the critical level score for virus (content disarm) detected.", "label": "Critical", "name": "critical"}],
        },
        "malware-list": {
            "type": "option",
            "help": "Threat weight score for virus (malware list) detected.",
            "default": "medium",
            "options": [{"help": "Disable threat weight scoring for virus (malware list) detected.", "label": "Disable", "name": "disable"}, {"help": "Use the low level score for virus (malware list) detected.", "label": "Low", "name": "low"}, {"help": "Use the medium level score for virus (malware list) detected.", "label": "Medium", "name": "medium"}, {"help": "Use the high level score for virus (malware list) detected.", "label": "High", "name": "high"}, {"help": "Use the critical level score for virus (malware list) detected.", "label": "Critical", "name": "critical"}],
        },
        "ems-threat-feed": {
            "type": "option",
            "help": "Threat weight score for virus (EMS threat feed) detected.",
            "default": "medium",
            "options": [{"help": "Disable threat weight scoring for virus (EMS threat feed) detected.", "label": "Disable", "name": "disable"}, {"help": "Use the low level score for virus (EMS threat feed) detected.", "label": "Low", "name": "low"}, {"help": "Use the medium level score for virus (EMS threat feed) detected.", "label": "Medium", "name": "medium"}, {"help": "Use the high level score for virus (EMS threat feed) detected.", "label": "High", "name": "high"}, {"help": "Use the critical level score for virus (EMS threat feed) detected.", "label": "Critical", "name": "critical"}],
        },
        "fsa-malicious": {
            "type": "option",
            "help": "Threat weight score for FortiSandbox malicious malware detected.",
            "default": "critical",
            "options": [{"help": "Disable threat weight scoring for FortiSandbox malicious malware detected.", "label": "Disable", "name": "disable"}, {"help": "Use the low level score for FortiSandbox malicious malware detected.", "label": "Low", "name": "low"}, {"help": "Use the medium level score for FortiSandbox malicious malware detected.", "label": "Medium", "name": "medium"}, {"help": "Use the high level score for FortiSandbox malicious malware detected.", "label": "High", "name": "high"}, {"help": "Use the critical level score for FortiSandbox malicious malware detected.", "label": "Critical", "name": "critical"}],
        },
        "fsa-high-risk": {
            "type": "option",
            "help": "Threat weight score for FortiSandbox high risk malware detected.",
            "default": "high",
            "options": [{"help": "Disable threat weight scoring for FortiSandbox high risk malware detected.", "label": "Disable", "name": "disable"}, {"help": "Use the low level score for FortiSandbox high risk malware detected.", "label": "Low", "name": "low"}, {"help": "Use the medium level score for FortiSandbox high risk malware detected.", "label": "Medium", "name": "medium"}, {"help": "Use the high level score for FortiSandbox high risk malware detected.", "label": "High", "name": "high"}, {"help": "Use the critical level score for FortiSandbox high risk malware detected.", "label": "Critical", "name": "critical"}],
        },
        "fsa-medium-risk": {
            "type": "option",
            "help": "Threat weight score for FortiSandbox medium risk malware detected.",
            "default": "medium",
            "options": [{"help": "Disable threat weight scoring for FortiSandbox medium risk malware detected.", "label": "Disable", "name": "disable"}, {"help": "Use the low level score for FortiSandbox medium risk malware detected.", "label": "Low", "name": "low"}, {"help": "Use the medium level score for FortiSandbox medium risk malware detected.", "label": "Medium", "name": "medium"}, {"help": "Use the high level score for FortiSandbox medium risk malware detected.", "label": "High", "name": "high"}, {"help": "Use the critical level score for FortiSandbox medium risk malware detected.", "label": "Critical", "name": "critical"}],
        },
    },
    "ips": {
        "info-severity": {
            "type": "option",
            "help": "Threat weight score for IPS info severity events.",
            "default": "disable",
            "options": [{"help": "Disable threat weight scoring for IPS info severity events.", "label": "Disable", "name": "disable"}, {"help": "Use the low level score for IPS info severity events.", "label": "Low", "name": "low"}, {"help": "Use the medium level score for IPS info severity events.", "label": "Medium", "name": "medium"}, {"help": "Use the high level score for IPS info severity events.", "label": "High", "name": "high"}, {"help": "Use the critical level score for IPS info severity events.", "label": "Critical", "name": "critical"}],
        },
        "low-severity": {
            "type": "option",
            "help": "Threat weight score for IPS low severity events.",
            "default": "low",
            "options": [{"help": "Disable threat weight scoring for IPS low severity events.", "label": "Disable", "name": "disable"}, {"help": "Use the low level score for IPS low severity events.", "label": "Low", "name": "low"}, {"help": "Use the medium level score for IPS low severity events.", "label": "Medium", "name": "medium"}, {"help": "Use the high level score for IPS low severity events.", "label": "High", "name": "high"}, {"help": "Use the critical level score for IPS low severity events.", "label": "Critical", "name": "critical"}],
        },
        "medium-severity": {
            "type": "option",
            "help": "Threat weight score for IPS medium severity events.",
            "default": "medium",
            "options": [{"help": "Disable threat weight scoring for IPS medium severity events.", "label": "Disable", "name": "disable"}, {"help": "Use the low level score for IPS medium severity events.", "label": "Low", "name": "low"}, {"help": "Use the medium level score for IPS medium severity events.", "label": "Medium", "name": "medium"}, {"help": "Use the high level score for IPS medium severity events.", "label": "High", "name": "high"}, {"help": "Use the critical level score for IPS medium severity events.", "label": "Critical", "name": "critical"}],
        },
        "high-severity": {
            "type": "option",
            "help": "Threat weight score for IPS high severity events.",
            "default": "high",
            "options": [{"help": "Disable threat weight scoring for IPS high severity events.", "label": "Disable", "name": "disable"}, {"help": "Use the low level score for IPS high severity events.", "label": "Low", "name": "low"}, {"help": "Use the medium level score for IPS high severity events.", "label": "Medium", "name": "medium"}, {"help": "Use the high level score for IPS high severity events.", "label": "High", "name": "high"}, {"help": "Use the critical level score for IPS high severity events.", "label": "Critical", "name": "critical"}],
        },
        "critical-severity": {
            "type": "option",
            "help": "Threat weight score for IPS critical severity events.",
            "default": "critical",
            "options": [{"help": "Disable threat weight scoring for IPS critical severity events.", "label": "Disable", "name": "disable"}, {"help": "Use the low level score for IPS critical severity events.", "label": "Low", "name": "low"}, {"help": "Use the medium level score for IPS critical severity events.", "label": "Medium", "name": "medium"}, {"help": "Use the high level score for IPS critical severity events.", "label": "High", "name": "high"}, {"help": "Use the critical level score for IPS critical severity events.", "label": "Critical", "name": "critical"}],
        },
    },
    "web": {
        "id": {
            "type": "integer",
            "help": "Entry ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 255,
        },
        "category": {
            "type": "integer",
            "help": "Threat weight score for web category filtering matches.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 255,
        },
        "level": {
            "type": "option",
            "help": "Threat weight score for web category filtering matches.",
            "default": "low",
            "options": [{"help": "Disable threat weight scoring for web category filtering matches.", "label": "Disable", "name": "disable"}, {"help": "Use the low level score for web category filtering matches.", "label": "Low", "name": "low"}, {"help": "Use the medium level score for web category filtering matches.", "label": "Medium", "name": "medium"}, {"help": "Use the high level score for web category filtering matches.", "label": "High", "name": "high"}, {"help": "Use the critical level score for web category filtering matches.", "label": "Critical", "name": "critical"}],
        },
    },
    "geolocation": {
        "id": {
            "type": "integer",
            "help": "Entry ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 255,
        },
        "country": {
            "type": "string",
            "help": "Country code.",
            "required": True,
            "default": "",
            "max_length": 2,
        },
        "level": {
            "type": "option",
            "help": "Threat weight score for Geolocation-based events.",
            "default": "low",
            "options": [{"help": "Disable threat weight scoring for Geolocation-based events.", "label": "Disable", "name": "disable"}, {"help": "Use the low level score for Geolocation-based events.", "label": "Low", "name": "low"}, {"help": "Use the medium level score for Geolocation-based events.", "label": "Medium", "name": "medium"}, {"help": "Use the high level score for Geolocation-based events.", "label": "High", "name": "high"}, {"help": "Use the critical level score for Geolocation-based events.", "label": "Critical", "name": "critical"}],
        },
    },
    "application": {
        "id": {
            "type": "integer",
            "help": "Entry ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 255,
        },
        "category": {
            "type": "integer",
            "help": "Application category.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 65535,
        },
        "level": {
            "type": "option",
            "help": "Threat weight score for Application events.",
            "default": "low",
            "options": [{"help": "Disable threat weight scoring for Application events.", "label": "Disable", "name": "disable"}, {"help": "Use the low level score for Application events.", "label": "Low", "name": "low"}, {"help": "Use the medium level score for Application events.", "label": "Medium", "name": "medium"}, {"help": "Use the high level score for Application events.", "label": "High", "name": "high"}, {"help": "Use the critical level score for Application events.", "label": "Critical", "name": "critical"}],
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_STATUS = [
    "enable",  # Enable the threat weight feature.
    "disable",  # Disable the threat weight feature.
]
VALID_BODY_BLOCKED_CONNECTION = [
    "disable",  # Disable threat weight scoring for blocked connections.
    "low",  # Use the low level score for blocked connections.
    "medium",  # Use the medium level score for blocked connections.
    "high",  # Use the high level score for blocked connections.
    "critical",  # Use the critical level score for blocked connections.
]
VALID_BODY_FAILED_CONNECTION = [
    "disable",  # Disable threat weight scoring for failed connections.
    "low",  # Use the low level score for failed connections.
    "medium",  # Use the medium level score for failed connections.
    "high",  # Use the high level score for failed connections.
    "critical",  # Use the critical level score for failed connections.
]
VALID_BODY_URL_BLOCK_DETECTED = [
    "disable",  # Disable threat weight scoring for URL blocking.
    "low",  # Use the low level score for URL blocking.
    "medium",  # Use the medium level score for URL blocking.
    "high",  # Use the high level score for URL blocking.
    "critical",  # Use the critical level score for URL blocking.
]
VALID_BODY_BOTNET_CONNECTION_DETECTED = [
    "disable",  # Disable threat weight scoring for detected botnet connections.
    "low",  # Use the low level score for detected botnet connections.
    "medium",  # Use the medium level score for detected botnet connections.
    "high",  # Use the high level score for detected botnet connections.
    "critical",  # Use the critical level score for detected botnet connections.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_log_threat_weight_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for log/threat_weight."""
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
    """Validate required fields for log/threat_weight."""
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


def validate_log_threat_weight_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new log/threat_weight object."""
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
    if "blocked-connection" in payload:
        value = payload["blocked-connection"]
        if value not in VALID_BODY_BLOCKED_CONNECTION:
            desc = FIELD_DESCRIPTIONS.get("blocked-connection", "")
            error_msg = f"Invalid value for 'blocked-connection': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_BLOCKED_CONNECTION)}"
            error_msg += f"\n  → Example: blocked-connection='{{ VALID_BODY_BLOCKED_CONNECTION[0] }}'"
            return (False, error_msg)
    if "failed-connection" in payload:
        value = payload["failed-connection"]
        if value not in VALID_BODY_FAILED_CONNECTION:
            desc = FIELD_DESCRIPTIONS.get("failed-connection", "")
            error_msg = f"Invalid value for 'failed-connection': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FAILED_CONNECTION)}"
            error_msg += f"\n  → Example: failed-connection='{{ VALID_BODY_FAILED_CONNECTION[0] }}'"
            return (False, error_msg)
    if "url-block-detected" in payload:
        value = payload["url-block-detected"]
        if value not in VALID_BODY_URL_BLOCK_DETECTED:
            desc = FIELD_DESCRIPTIONS.get("url-block-detected", "")
            error_msg = f"Invalid value for 'url-block-detected': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_URL_BLOCK_DETECTED)}"
            error_msg += f"\n  → Example: url-block-detected='{{ VALID_BODY_URL_BLOCK_DETECTED[0] }}'"
            return (False, error_msg)
    if "botnet-connection-detected" in payload:
        value = payload["botnet-connection-detected"]
        if value not in VALID_BODY_BOTNET_CONNECTION_DETECTED:
            desc = FIELD_DESCRIPTIONS.get("botnet-connection-detected", "")
            error_msg = f"Invalid value for 'botnet-connection-detected': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_BOTNET_CONNECTION_DETECTED)}"
            error_msg += f"\n  → Example: botnet-connection-detected='{{ VALID_BODY_BOTNET_CONNECTION_DETECTED[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_log_threat_weight_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update log/threat_weight."""
    # Step 1: Validate enum values
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid value for 'status'='{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )
    if "blocked-connection" in payload:
        value = payload["blocked-connection"]
        if value not in VALID_BODY_BLOCKED_CONNECTION:
            return (
                False,
                f"Invalid value for 'blocked-connection'='{value}'. Must be one of: {', '.join(VALID_BODY_BLOCKED_CONNECTION)}",
            )
    if "failed-connection" in payload:
        value = payload["failed-connection"]
        if value not in VALID_BODY_FAILED_CONNECTION:
            return (
                False,
                f"Invalid value for 'failed-connection'='{value}'. Must be one of: {', '.join(VALID_BODY_FAILED_CONNECTION)}",
            )
    if "url-block-detected" in payload:
        value = payload["url-block-detected"]
        if value not in VALID_BODY_URL_BLOCK_DETECTED:
            return (
                False,
                f"Invalid value for 'url-block-detected'='{value}'. Must be one of: {', '.join(VALID_BODY_URL_BLOCK_DETECTED)}",
            )
    if "botnet-connection-detected" in payload:
        value = payload["botnet-connection-detected"]
        if value not in VALID_BODY_BOTNET_CONNECTION_DETECTED:
            return (
                False,
                f"Invalid value for 'botnet-connection-detected'='{value}'. Must be one of: {', '.join(VALID_BODY_BOTNET_CONNECTION_DETECTED)}",
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
    "endpoint": "log/threat_weight",
    "category": "cmdb",
    "api_path": "log/threat-weight",
    "help": "Configure threat weight settings.",
    "total_fields": 11,
    "required_fields_count": 0,
    "fields_with_defaults_count": 5,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
