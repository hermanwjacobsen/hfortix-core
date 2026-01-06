"""
Validation helpers for application/list endpoint.

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
    "name",  # List name.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "replacemsg-group": "",
    "extended-log": "disable",
    "other-application-action": "pass",
    "app-replacemsg": "enable",
    "other-application-log": "disable",
    "enforce-default-app-port": "disable",
    "force-inclusion-ssl-di-sigs": "disable",
    "unknown-application-action": "pass",
    "unknown-application-log": "disable",
    "p2p-block-list": "",
    "deep-app-inspection": "enable",
    "options": "allow-dns",
    "control-default-network-services": "disable",
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
    "name": "string",  # List name.
    "comment": "var-string",  # Comments.
    "replacemsg-group": "string",  # Replacement message group.
    "extended-log": "option",  # Enable/disable extended logging.
    "other-application-action": "option",  # Action for other applications.
    "app-replacemsg": "option",  # Enable/disable replacement messages for blocked applications
    "other-application-log": "option",  # Enable/disable logging for other applications.
    "enforce-default-app-port": "option",  # Enable/disable default application port enforcement for allo
    "force-inclusion-ssl-di-sigs": "option",  # Enable/disable forced inclusion of SSL deep inspection signa
    "unknown-application-action": "option",  # Pass or block traffic from unknown applications.
    "unknown-application-log": "option",  # Enable/disable logging for unknown applications.
    "p2p-block-list": "option",  # P2P applications to be block listed.
    "deep-app-inspection": "option",  # Enable/disable deep application inspection.
    "options": "option",  # Basic application protocol signatures allowed by default.
    "entries": "string",  # Application list entries.
    "control-default-network-services": "option",  # Enable/disable enforcement of protocols over selected ports.
    "default-network-services": "string",  # Default network service entries.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "List name.",
    "comment": "Comments.",
    "replacemsg-group": "Replacement message group.",
    "extended-log": "Enable/disable extended logging.",
    "other-application-action": "Action for other applications.",
    "app-replacemsg": "Enable/disable replacement messages for blocked applications.",
    "other-application-log": "Enable/disable logging for other applications.",
    "enforce-default-app-port": "Enable/disable default application port enforcement for allowed applications.",
    "force-inclusion-ssl-di-sigs": "Enable/disable forced inclusion of SSL deep inspection signatures.",
    "unknown-application-action": "Pass or block traffic from unknown applications.",
    "unknown-application-log": "Enable/disable logging for unknown applications.",
    "p2p-block-list": "P2P applications to be block listed.",
    "deep-app-inspection": "Enable/disable deep application inspection.",
    "options": "Basic application protocol signatures allowed by default.",
    "entries": "Application list entries.",
    "control-default-network-services": "Enable/disable enforcement of protocols over selected ports.",
    "default-network-services": "Default network service entries.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 47},
    "replacemsg-group": {"type": "string", "max_length": 35},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "entries": {
        "id": {
            "type": "integer",
            "help": "Entry ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "risk": {
            "type": "string",
            "help": "Risk, or impact, of allowing traffic from this application to occur (1 - 5; Low, Elevated, Medium, High, and Critical).",
        },
        "category": {
            "type": "string",
            "help": "Category ID list.",
        },
        "application": {
            "type": "string",
            "help": "ID of allowed applications.",
        },
        "protocols": {
            "type": "user",
            "help": "Application protocol filter.",
            "default": "all",
        },
        "vendor": {
            "type": "user",
            "help": "Application vendor filter.",
            "default": "all",
        },
        "technology": {
            "type": "user",
            "help": "Application technology filter.",
            "default": "all",
        },
        "behavior": {
            "type": "user",
            "help": "Application behavior filter.",
            "default": "all",
        },
        "popularity": {
            "type": "option",
            "help": "Application popularity filter (1 - 5, from least to most popular).",
            "default": "1 2 3 4 5",
            "options": [{"help": "Popularity level 1.", "label": "1", "name": "1"}, {"help": "Popularity level 2.", "label": "2", "name": "2"}, {"help": "Popularity level 3.", "label": "3", "name": "3"}, {"help": "Popularity level 4.", "label": "4", "name": "4"}, {"help": "Popularity level 5.", "label": "5", "name": "5"}],
        },
        "exclusion": {
            "type": "string",
            "help": "ID of excluded applications.",
        },
        "parameters": {
            "type": "string",
            "help": "Application parameters.",
        },
        "action": {
            "type": "option",
            "help": "Pass or block traffic, or reset connection for traffic from this application.",
            "default": "block",
            "options": [{"help": "Pass or allow matching traffic.", "label": "Pass", "name": "pass"}, {"help": "Block or drop matching traffic.", "label": "Block", "name": "block"}, {"help": "Reset sessions for matching traffic.", "label": "Reset", "name": "reset"}],
        },
        "log": {
            "type": "option",
            "help": "Enable/disable logging for this application list.",
            "default": "enable",
            "options": [{"help": "Disable logging.", "label": "Disable", "name": "disable"}, {"help": "Enable logging.", "label": "Enable", "name": "enable"}],
        },
        "log-packet": {
            "type": "option",
            "help": "Enable/disable packet logging.",
            "default": "disable",
            "options": [{"help": "Disable packet logging.", "label": "Disable", "name": "disable"}, {"help": "Enable packet logging.", "label": "Enable", "name": "enable"}],
        },
        "rate-count": {
            "type": "integer",
            "help": "Count of the rate.",
            "default": 0,
            "min_value": 0,
            "max_value": 65535,
        },
        "rate-duration": {
            "type": "integer",
            "help": "Duration (sec) of the rate.",
            "default": 60,
            "min_value": 1,
            "max_value": 65535,
        },
        "rate-mode": {
            "type": "option",
            "help": "Rate limit mode.",
            "default": "continuous",
            "options": [{"help": "Allow configured number of packets every rate-duration.", "label": "Periodical", "name": "periodical"}, {"help": "Block packets once the rate is reached.", "label": "Continuous", "name": "continuous"}],
        },
        "rate-track": {
            "type": "option",
            "help": "Track the packet protocol field.",
            "default": "none",
            "options": [{"help": "none", "label": "None", "name": "none"}, {"help": "Source IP.", "label": "Src Ip", "name": "src-ip"}, {"help": "Destination IP.", "label": "Dest Ip", "name": "dest-ip"}, {"help": "DHCP client.", "label": "Dhcp Client Mac", "name": "dhcp-client-mac"}, {"help": "DNS domain.", "label": "Dns Domain", "name": "dns-domain"}],
        },
        "session-ttl": {
            "type": "integer",
            "help": "Session TTL (0 = default).",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "shaper": {
            "type": "string",
            "help": "Traffic shaper.",
            "default": "",
            "max_length": 35,
        },
        "shaper-reverse": {
            "type": "string",
            "help": "Reverse traffic shaper.",
            "default": "",
            "max_length": 35,
        },
        "per-ip-shaper": {
            "type": "string",
            "help": "Per-IP traffic shaper.",
            "default": "",
            "max_length": 35,
        },
        "quarantine": {
            "type": "option",
            "help": "Quarantine method.",
            "default": "none",
            "options": [{"help": "Quarantine is disabled.", "label": "None", "name": "none"}, {"help": "Block all traffic sent from attacker\u0027s IP address. The attacker\u0027s IP address is also added to the banned user list. The target\u0027s address is not affected.", "label": "Attacker", "name": "attacker"}],
        },
        "quarantine-expiry": {
            "type": "user",
            "help": "Duration of quarantine. (Format ###d##h##m, minimum 1m, maximum 364d23h59m, default = 5m). Requires quarantine set to attacker.",
            "default": "5m",
        },
        "quarantine-log": {
            "type": "option",
            "help": "Enable/disable quarantine logging.",
            "default": "enable",
            "options": [{"help": "Disable quarantine logging.", "label": "Disable", "name": "disable"}, {"help": "Enable quarantine logging.", "label": "Enable", "name": "enable"}],
        },
    },
    "default-network-services": {
        "id": {
            "type": "integer",
            "help": "Entry ID.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "port": {
            "type": "integer",
            "help": "Port number.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 65535,
        },
        "services": {
            "type": "option",
            "help": "Network protocols.",
            "default": "",
            "options": [{"help": "HTTP.", "label": "Http", "name": "http"}, {"help": "SSH.", "label": "Ssh", "name": "ssh"}, {"help": "TELNET.", "label": "Telnet", "name": "telnet"}, {"help": "FTP.", "label": "Ftp", "name": "ftp"}, {"help": "DNS.", "label": "Dns", "name": "dns"}, {"help": "SMTP.", "label": "Smtp", "name": "smtp"}, {"help": "POP3.", "label": "Pop3", "name": "pop3"}, {"help": "IMAP.", "label": "Imap", "name": "imap"}, {"help": "SNMP.", "label": "Snmp", "name": "snmp"}, {"help": "NNTP.", "label": "Nntp", "name": "nntp"}, {"help": "HTTPS.", "label": "Https", "name": "https"}],
        },
        "violation-action": {
            "type": "option",
            "help": "Action for protocols not in the allowlist for selected port.",
            "default": "block",
            "options": [{"help": "Allow protocols not in the allowlist for selected port.", "label": "Pass", "name": "pass"}, {"help": "Monitor protocols not in the allowlist for selected port.", "label": "Monitor", "name": "monitor"}, {"help": "Block protocols not in the allowlist for selected port.", "label": "Block", "name": "block"}],
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_EXTENDED_LOG = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_OTHER_APPLICATION_ACTION = [
    "pass",  # Allow sessions matching an application in this application list.
    "block",  # Block sessions matching an application in this application list.
]
VALID_BODY_APP_REPLACEMSG = [
    "disable",  # Disable replacement messages for blocked applications.
    "enable",  # Enable replacement messages for blocked applications.
]
VALID_BODY_OTHER_APPLICATION_LOG = [
    "disable",  # Disable logging for other applications.
    "enable",  # Enable logging for other applications.
]
VALID_BODY_ENFORCE_DEFAULT_APP_PORT = [
    "disable",  # Disable default application port enforcement.
    "enable",  # Enable default application port enforcement.
]
VALID_BODY_FORCE_INCLUSION_SSL_DI_SIGS = [
    "disable",  # Disable forced inclusion of signatures which normally require SSL deep inspection.
    "enable",  # Enable forced inclusion of signatures which normally require SSL deep inspection.
]
VALID_BODY_UNKNOWN_APPLICATION_ACTION = [
    "pass",  # Pass or allow unknown applications.
    "block",  # Drop or block unknown applications.
]
VALID_BODY_UNKNOWN_APPLICATION_LOG = [
    "disable",  # Disable logging for unknown applications.
    "enable",  # Enable logging for unknown applications.
]
VALID_BODY_P2P_BLOCK_LIST = [
    "skype",  # Skype.
    "edonkey",  # Edonkey.
    "bittorrent",  # Bit torrent.
]
VALID_BODY_DEEP_APP_INSPECTION = [
    "disable",  # Disable deep application inspection.
    "enable",  # Enable deep application inspection.
]
VALID_BODY_OPTIONS = [
    "allow-dns",  # Allow DNS.
    "allow-icmp",  # Allow ICMP.
    "allow-http",  # Allow generic HTTP web browsing.
    "allow-ssl",  # Allow generic SSL communication.
]
VALID_BODY_CONTROL_DEFAULT_NETWORK_SERVICES = [
    "disable",  # Disable protocol enforcement over selected ports.
    "enable",  # Enable protocol enforcement over selected ports.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_application_list_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for application/list.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_application_list_get()
        >>> assert is_valid == True
        
        >>> # Valid - Get specific item by name
        >>> is_valid, error = validate_application_list_get(name="test-item")
        >>> assert is_valid == True
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_application_list_get(
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
    Validate required fields for application/list.

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


def validate_application_list_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new application/list object.

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
        ...     "name": True,  # List name.
        ... }
        >>> is_valid, error = validate_application_list_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "name": True,
        ...     "extended-log": "{'name': 'enable', 'help': 'Enable setting.', 'label': 'Enable', 'description': 'Enable setting'}",  # Valid enum value
        ... }
        >>> is_valid, error = validate_application_list_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["extended-log"] = "invalid-value"
        >>> is_valid, error = validate_application_list_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_application_list_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
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
    if "other-application-action" in payload:
        value = payload["other-application-action"]
        if value not in VALID_BODY_OTHER_APPLICATION_ACTION:
            desc = FIELD_DESCRIPTIONS.get("other-application-action", "")
            error_msg = f"Invalid value for 'other-application-action': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OTHER_APPLICATION_ACTION)}"
            error_msg += f"\n  → Example: other-application-action='{{ VALID_BODY_OTHER_APPLICATION_ACTION[0] }}'"
            return (False, error_msg)
    if "app-replacemsg" in payload:
        value = payload["app-replacemsg"]
        if value not in VALID_BODY_APP_REPLACEMSG:
            desc = FIELD_DESCRIPTIONS.get("app-replacemsg", "")
            error_msg = f"Invalid value for 'app-replacemsg': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_APP_REPLACEMSG)}"
            error_msg += f"\n  → Example: app-replacemsg='{{ VALID_BODY_APP_REPLACEMSG[0] }}'"
            return (False, error_msg)
    if "other-application-log" in payload:
        value = payload["other-application-log"]
        if value not in VALID_BODY_OTHER_APPLICATION_LOG:
            desc = FIELD_DESCRIPTIONS.get("other-application-log", "")
            error_msg = f"Invalid value for 'other-application-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OTHER_APPLICATION_LOG)}"
            error_msg += f"\n  → Example: other-application-log='{{ VALID_BODY_OTHER_APPLICATION_LOG[0] }}'"
            return (False, error_msg)
    if "enforce-default-app-port" in payload:
        value = payload["enforce-default-app-port"]
        if value not in VALID_BODY_ENFORCE_DEFAULT_APP_PORT:
            desc = FIELD_DESCRIPTIONS.get("enforce-default-app-port", "")
            error_msg = f"Invalid value for 'enforce-default-app-port': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ENFORCE_DEFAULT_APP_PORT)}"
            error_msg += f"\n  → Example: enforce-default-app-port='{{ VALID_BODY_ENFORCE_DEFAULT_APP_PORT[0] }}'"
            return (False, error_msg)
    if "force-inclusion-ssl-di-sigs" in payload:
        value = payload["force-inclusion-ssl-di-sigs"]
        if value not in VALID_BODY_FORCE_INCLUSION_SSL_DI_SIGS:
            desc = FIELD_DESCRIPTIONS.get("force-inclusion-ssl-di-sigs", "")
            error_msg = f"Invalid value for 'force-inclusion-ssl-di-sigs': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FORCE_INCLUSION_SSL_DI_SIGS)}"
            error_msg += f"\n  → Example: force-inclusion-ssl-di-sigs='{{ VALID_BODY_FORCE_INCLUSION_SSL_DI_SIGS[0] }}'"
            return (False, error_msg)
    if "unknown-application-action" in payload:
        value = payload["unknown-application-action"]
        if value not in VALID_BODY_UNKNOWN_APPLICATION_ACTION:
            desc = FIELD_DESCRIPTIONS.get("unknown-application-action", "")
            error_msg = f"Invalid value for 'unknown-application-action': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_UNKNOWN_APPLICATION_ACTION)}"
            error_msg += f"\n  → Example: unknown-application-action='{{ VALID_BODY_UNKNOWN_APPLICATION_ACTION[0] }}'"
            return (False, error_msg)
    if "unknown-application-log" in payload:
        value = payload["unknown-application-log"]
        if value not in VALID_BODY_UNKNOWN_APPLICATION_LOG:
            desc = FIELD_DESCRIPTIONS.get("unknown-application-log", "")
            error_msg = f"Invalid value for 'unknown-application-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_UNKNOWN_APPLICATION_LOG)}"
            error_msg += f"\n  → Example: unknown-application-log='{{ VALID_BODY_UNKNOWN_APPLICATION_LOG[0] }}'"
            return (False, error_msg)
    if "p2p-block-list" in payload:
        value = payload["p2p-block-list"]
        if value not in VALID_BODY_P2P_BLOCK_LIST:
            desc = FIELD_DESCRIPTIONS.get("p2p-block-list", "")
            error_msg = f"Invalid value for 'p2p-block-list': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_P2P_BLOCK_LIST)}"
            error_msg += f"\n  → Example: p2p-block-list='{{ VALID_BODY_P2P_BLOCK_LIST[0] }}'"
            return (False, error_msg)
    if "deep-app-inspection" in payload:
        value = payload["deep-app-inspection"]
        if value not in VALID_BODY_DEEP_APP_INSPECTION:
            desc = FIELD_DESCRIPTIONS.get("deep-app-inspection", "")
            error_msg = f"Invalid value for 'deep-app-inspection': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DEEP_APP_INSPECTION)}"
            error_msg += f"\n  → Example: deep-app-inspection='{{ VALID_BODY_DEEP_APP_INSPECTION[0] }}'"
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
    if "control-default-network-services" in payload:
        value = payload["control-default-network-services"]
        if value not in VALID_BODY_CONTROL_DEFAULT_NETWORK_SERVICES:
            desc = FIELD_DESCRIPTIONS.get("control-default-network-services", "")
            error_msg = f"Invalid value for 'control-default-network-services': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CONTROL_DEFAULT_NETWORK_SERVICES)}"
            error_msg += f"\n  → Example: control-default-network-services='{{ VALID_BODY_CONTROL_DEFAULT_NETWORK_SERVICES[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_application_list_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update application/list.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_application_list_put(payload)
    """
    # Step 1: Validate enum values
    if "extended-log" in payload:
        value = payload["extended-log"]
        if value not in VALID_BODY_EXTENDED_LOG:
            return (
                False,
                f"Invalid value for 'extended-log'='{value}'. Must be one of: {', '.join(VALID_BODY_EXTENDED_LOG)}",
            )
    if "other-application-action" in payload:
        value = payload["other-application-action"]
        if value not in VALID_BODY_OTHER_APPLICATION_ACTION:
            return (
                False,
                f"Invalid value for 'other-application-action'='{value}'. Must be one of: {', '.join(VALID_BODY_OTHER_APPLICATION_ACTION)}",
            )
    if "app-replacemsg" in payload:
        value = payload["app-replacemsg"]
        if value not in VALID_BODY_APP_REPLACEMSG:
            return (
                False,
                f"Invalid value for 'app-replacemsg'='{value}'. Must be one of: {', '.join(VALID_BODY_APP_REPLACEMSG)}",
            )
    if "other-application-log" in payload:
        value = payload["other-application-log"]
        if value not in VALID_BODY_OTHER_APPLICATION_LOG:
            return (
                False,
                f"Invalid value for 'other-application-log'='{value}'. Must be one of: {', '.join(VALID_BODY_OTHER_APPLICATION_LOG)}",
            )
    if "enforce-default-app-port" in payload:
        value = payload["enforce-default-app-port"]
        if value not in VALID_BODY_ENFORCE_DEFAULT_APP_PORT:
            return (
                False,
                f"Invalid value for 'enforce-default-app-port'='{value}'. Must be one of: {', '.join(VALID_BODY_ENFORCE_DEFAULT_APP_PORT)}",
            )
    if "force-inclusion-ssl-di-sigs" in payload:
        value = payload["force-inclusion-ssl-di-sigs"]
        if value not in VALID_BODY_FORCE_INCLUSION_SSL_DI_SIGS:
            return (
                False,
                f"Invalid value for 'force-inclusion-ssl-di-sigs'='{value}'. Must be one of: {', '.join(VALID_BODY_FORCE_INCLUSION_SSL_DI_SIGS)}",
            )
    if "unknown-application-action" in payload:
        value = payload["unknown-application-action"]
        if value not in VALID_BODY_UNKNOWN_APPLICATION_ACTION:
            return (
                False,
                f"Invalid value for 'unknown-application-action'='{value}'. Must be one of: {', '.join(VALID_BODY_UNKNOWN_APPLICATION_ACTION)}",
            )
    if "unknown-application-log" in payload:
        value = payload["unknown-application-log"]
        if value not in VALID_BODY_UNKNOWN_APPLICATION_LOG:
            return (
                False,
                f"Invalid value for 'unknown-application-log'='{value}'. Must be one of: {', '.join(VALID_BODY_UNKNOWN_APPLICATION_LOG)}",
            )
    if "p2p-block-list" in payload:
        value = payload["p2p-block-list"]
        if value not in VALID_BODY_P2P_BLOCK_LIST:
            return (
                False,
                f"Invalid value for 'p2p-block-list'='{value}'. Must be one of: {', '.join(VALID_BODY_P2P_BLOCK_LIST)}",
            )
    if "deep-app-inspection" in payload:
        value = payload["deep-app-inspection"]
        if value not in VALID_BODY_DEEP_APP_INSPECTION:
            return (
                False,
                f"Invalid value for 'deep-app-inspection'='{value}'. Must be one of: {', '.join(VALID_BODY_DEEP_APP_INSPECTION)}",
            )
    if "options" in payload:
        value = payload["options"]
        if value not in VALID_BODY_OPTIONS:
            return (
                False,
                f"Invalid value for 'options'='{value}'. Must be one of: {', '.join(VALID_BODY_OPTIONS)}",
            )
    if "control-default-network-services" in payload:
        value = payload["control-default-network-services"]
        if value not in VALID_BODY_CONTROL_DEFAULT_NETWORK_SERVICES:
            return (
                False,
                f"Invalid value for 'control-default-network-services'='{value}'. Must be one of: {', '.join(VALID_BODY_CONTROL_DEFAULT_NETWORK_SERVICES)}",
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
    "endpoint": "application/list",
    "category": "cmdb",
    "api_path": "application/list",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure application control lists.",
    "total_fields": 17,
    "required_fields_count": 1,
    "fields_with_defaults_count": 14,
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
