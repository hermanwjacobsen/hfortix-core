"""
Validation helpers for system/automation_action endpoint.

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
    "system-action",  # System action type.
    "aws-api-key",  # AWS API Gateway API key.
    "alicloud-access-key-id",  # AliCloud AccessKey ID.
    "alicloud-access-key-secret",  # AliCloud AccessKey secret.
    "uri",  # Request API URI.
    "script",  # CLI script.
    "regular-expression",  # Regular expression string.
    "security-tag",  # NSX security tag.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "action-type": "alert",
    "system-action": "",
    "tls-certificate": "",
    "forticare-email": "disable",
    "minimum-interval": 0,
    "azure-function-authorization": "anonymous",
    "alicloud-function-authorization": "anonymous",
    "alicloud-access-key-id": "",
    "message-type": "text",
    "message": "Time: %%log.date%% %%log.time%%\nDevice: %%log.devid%% (%%log.vd%%)\nLevel: %%log.level%%\nEvent: %%log.logdesc%%\nRaw log:\n%%log%%",
    "replacement-message": "disable",
    "replacemsg-group": "",
    "protocol": "http",
    "method": "post",
    "port": 0,
    "verify-host-cert": "enable",
    "output-size": 10,
    "timeout": 0,
    "duration": 5,
    "output-interval": 0,
    "file-only": "disable",
    "execute-security-fabric": "disable",
    "accprofile": "",
    "log-debug-print": "disable",
    "security-tag": "",
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
    "name": "string",  # Name.
    "description": "var-string",  # Description.
    "action-type": "option",  # Action type.
    "system-action": "option",  # System action type.
    "tls-certificate": "string",  # Custom TLS certificate for API request.
    "forticare-email": "option",  # Enable/disable use of your FortiCare email address as the em
    "email-to": "string",  # Email addresses.
    "email-from": "var-string",  # Email sender name.
    "email-subject": "var-string",  # Email subject.
    "minimum-interval": "integer",  # Limit execution to no more than once in this interval (in se
    "aws-api-key": "password",  # AWS API Gateway API key.
    "azure-function-authorization": "option",  # Azure function authorization level.
    "azure-api-key": "password",  # Azure function API key.
    "alicloud-function-authorization": "option",  # AliCloud function authorization type.
    "alicloud-access-key-id": "string",  # AliCloud AccessKey ID.
    "alicloud-access-key-secret": "password",  # AliCloud AccessKey secret.
    "message-type": "option",  # Message type.
    "message": "string",  # Message content.
    "replacement-message": "option",  # Enable/disable replacement message.
    "replacemsg-group": "string",  # Replacement message group.
    "protocol": "option",  # Request protocol.
    "method": "option",  # Request method (POST, PUT, GET, PATCH or DELETE).
    "uri": "var-string",  # Request API URI.
    "http-body": "var-string",  # Request body (if necessary). Should be serialized json strin
    "port": "integer",  # Protocol port.
    "http-headers": "string",  # Request headers.
    "form-data": "string",  # Form data parts for content type multipart/form-data.
    "verify-host-cert": "option",  # Enable/disable verification of the remote host certificate.
    "script": "var-string",  # CLI script.
    "output-size": "integer",  # Number of megabytes to limit script output to (1 - 1024, def
    "timeout": "integer",  # Maximum running time for this script in seconds (0 = no time
    "duration": "integer",  # Maximum running time for this script in seconds.
    "output-interval": "integer",  # Collect the outputs for each output-interval in seconds (0 =
    "file-only": "option",  # Enable/disable the output in files only.
    "execute-security-fabric": "option",  # Enable/disable execution of CLI script on all or only one Fo
    "accprofile": "string",  # Access profile for CLI script action to access FortiGate fea
    "regular-expression": "var-string",  # Regular expression string.
    "log-debug-print": "option",  # Enable/disable logging debug print output from diagnose acti
    "security-tag": "string",  # NSX security tag.
    "sdn-connector": "string",  # NSX SDN connector names.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Name.",
    "description": "Description.",
    "action-type": "Action type.",
    "system-action": "System action type.",
    "tls-certificate": "Custom TLS certificate for API request.",
    "forticare-email": "Enable/disable use of your FortiCare email address as the email-to address.",
    "email-to": "Email addresses.",
    "email-from": "Email sender name.",
    "email-subject": "Email subject.",
    "minimum-interval": "Limit execution to no more than once in this interval (in seconds).",
    "aws-api-key": "AWS API Gateway API key.",
    "azure-function-authorization": "Azure function authorization level.",
    "azure-api-key": "Azure function API key.",
    "alicloud-function-authorization": "AliCloud function authorization type.",
    "alicloud-access-key-id": "AliCloud AccessKey ID.",
    "alicloud-access-key-secret": "AliCloud AccessKey secret.",
    "message-type": "Message type.",
    "message": "Message content.",
    "replacement-message": "Enable/disable replacement message.",
    "replacemsg-group": "Replacement message group.",
    "protocol": "Request protocol.",
    "method": "Request method (POST, PUT, GET, PATCH or DELETE).",
    "uri": "Request API URI.",
    "http-body": "Request body (if necessary). Should be serialized json string.",
    "port": "Protocol port.",
    "http-headers": "Request headers.",
    "form-data": "Form data parts for content type multipart/form-data.",
    "verify-host-cert": "Enable/disable verification of the remote host certificate.",
    "script": "CLI script.",
    "output-size": "Number of megabytes to limit script output to (1 - 1024, default = 10).",
    "timeout": "Maximum running time for this script in seconds (0 = no timeout).",
    "duration": "Maximum running time for this script in seconds.",
    "output-interval": "Collect the outputs for each output-interval in seconds (0 = no intermediate output).",
    "file-only": "Enable/disable the output in files only.",
    "execute-security-fabric": "Enable/disable execution of CLI script on all or only one FortiGate unit in the Security Fabric.",
    "accprofile": "Access profile for CLI script action to access FortiGate features.",
    "regular-expression": "Regular expression string.",
    "log-debug-print": "Enable/disable logging debug print output from diagnose action.",
    "security-tag": "NSX security tag.",
    "sdn-connector": "NSX SDN connector names.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 64},
    "tls-certificate": {"type": "string", "max_length": 35},
    "minimum-interval": {"type": "integer", "min": 0, "max": 2592000},
    "alicloud-access-key-id": {"type": "string", "max_length": 35},
    "message": {"type": "string", "max_length": 4095},
    "replacemsg-group": {"type": "string", "max_length": 35},
    "port": {"type": "integer", "min": 1, "max": 65535},
    "output-size": {"type": "integer", "min": 1, "max": 1024},
    "timeout": {"type": "integer", "min": 0, "max": 300},
    "duration": {"type": "integer", "min": 1, "max": 36000},
    "output-interval": {"type": "integer", "min": 0, "max": 36000},
    "accprofile": {"type": "string", "max_length": 35},
    "security-tag": {"type": "string", "max_length": 255},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "email-to": {
        "name": {
            "type": "string",
            "help": "Email address.",
            "required": True,
            "default": "",
            "max_length": 255,
        },
    },
    "http-headers": {
        "id": {
            "type": "integer",
            "help": "Entry ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "key": {
            "type": "var-string",
            "help": "Request header key.",
            "required": True,
            "max_length": 1023,
        },
        "value": {
            "type": "var-string",
            "help": "Request header value.",
            "required": True,
            "max_length": 4095,
        },
    },
    "form-data": {
        "id": {
            "type": "integer",
            "help": "Entry ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "key": {
            "type": "var-string",
            "help": "Key of the part of Multipart/form-data.",
            "required": True,
            "max_length": 1023,
        },
        "value": {
            "type": "var-string",
            "help": "Value of the part of Multipart/form-data.",
            "required": True,
            "max_length": 4095,
        },
    },
    "sdn-connector": {
        "name": {
            "type": "string",
            "help": "SDN connector name.",
            "default": "",
            "max_length": 79,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_ACTION_TYPE = [
    "email",
    "fortiexplorer-notification",
    "alert",
    "disable-ssid",
    "system-actions",
    "quarantine",
    "quarantine-forticlient",
    "quarantine-nsx",
    "quarantine-fortinac",
    "ban-ip",
    "aws-lambda",
    "azure-function",
    "google-cloud-function",
    "alicloud-function",
    "webhook",
    "cli-script",
    "diagnose-script",
    "regular-expression",
    "slack-notification",
    "microsoft-teams-notification",
]
VALID_BODY_SYSTEM_ACTION = [
    "reboot",
    "shutdown",
    "backup-config",
]
VALID_BODY_FORTICARE_EMAIL = [
    "enable",
    "disable",
]
VALID_BODY_AZURE_FUNCTION_AUTHORIZATION = [
    "anonymous",
    "function",
    "admin",
]
VALID_BODY_ALICLOUD_FUNCTION_AUTHORIZATION = [
    "anonymous",
    "function",
]
VALID_BODY_MESSAGE_TYPE = [
    "text",
    "json",
    "form-data",
]
VALID_BODY_REPLACEMENT_MESSAGE = [
    "enable",
    "disable",
]
VALID_BODY_PROTOCOL = [
    "http",
    "https",
]
VALID_BODY_METHOD = [
    "post",
    "put",
    "get",
    "patch",
    "delete",
]
VALID_BODY_VERIFY_HOST_CERT = [
    "enable",
    "disable",
]
VALID_BODY_FILE_ONLY = [
    "enable",
    "disable",
]
VALID_BODY_EXECUTE_SECURITY_FABRIC = [
    "enable",
    "disable",
]
VALID_BODY_LOG_DEBUG_PRINT = [
    "enable",
    "disable",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_system_automation_action_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for system/automation_action.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_system_automation_action_get()
        >>> assert is_valid == True
        
        >>> # Valid - Get specific item by name
        >>> is_valid, error = validate_system_automation_action_get(name="test-item")
        >>> assert is_valid == True
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_system_automation_action_get(
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
    Validate required fields for system/automation_action.

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


def validate_system_automation_action_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new system/automation_action object.

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
        ...     "system-action": True,  # System action type.
        ...     "aws-api-key": True,  # AWS API Gateway API key.
        ... }
        >>> is_valid, error = validate_system_automation_action_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "system-action": True,
        ...     "action-type": "email",  # Valid enum value
        ... }
        >>> is_valid, error = validate_system_automation_action_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["action-type"] = "invalid-value"
        >>> is_valid, error = validate_system_automation_action_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_system_automation_action_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "action-type" in payload:
        value = payload["action-type"]
        if value not in VALID_BODY_ACTION_TYPE:
            desc = FIELD_DESCRIPTIONS.get("action-type", "")
            error_msg = f"Invalid value for 'action-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ACTION_TYPE)}"
            error_msg += f"\n  → Example: action-type='{{ VALID_BODY_ACTION_TYPE[0] }}'"
            return (False, error_msg)
    if "system-action" in payload:
        value = payload["system-action"]
        if value not in VALID_BODY_SYSTEM_ACTION:
            desc = FIELD_DESCRIPTIONS.get("system-action", "")
            error_msg = f"Invalid value for 'system-action': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SYSTEM_ACTION)}"
            error_msg += f"\n  → Example: system-action='{{ VALID_BODY_SYSTEM_ACTION[0] }}'"
            return (False, error_msg)
    if "forticare-email" in payload:
        value = payload["forticare-email"]
        if value not in VALID_BODY_FORTICARE_EMAIL:
            desc = FIELD_DESCRIPTIONS.get("forticare-email", "")
            error_msg = f"Invalid value for 'forticare-email': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FORTICARE_EMAIL)}"
            error_msg += f"\n  → Example: forticare-email='{{ VALID_BODY_FORTICARE_EMAIL[0] }}'"
            return (False, error_msg)
    if "azure-function-authorization" in payload:
        value = payload["azure-function-authorization"]
        if value not in VALID_BODY_AZURE_FUNCTION_AUTHORIZATION:
            desc = FIELD_DESCRIPTIONS.get("azure-function-authorization", "")
            error_msg = f"Invalid value for 'azure-function-authorization': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AZURE_FUNCTION_AUTHORIZATION)}"
            error_msg += f"\n  → Example: azure-function-authorization='{{ VALID_BODY_AZURE_FUNCTION_AUTHORIZATION[0] }}'"
            return (False, error_msg)
    if "alicloud-function-authorization" in payload:
        value = payload["alicloud-function-authorization"]
        if value not in VALID_BODY_ALICLOUD_FUNCTION_AUTHORIZATION:
            desc = FIELD_DESCRIPTIONS.get("alicloud-function-authorization", "")
            error_msg = f"Invalid value for 'alicloud-function-authorization': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ALICLOUD_FUNCTION_AUTHORIZATION)}"
            error_msg += f"\n  → Example: alicloud-function-authorization='{{ VALID_BODY_ALICLOUD_FUNCTION_AUTHORIZATION[0] }}'"
            return (False, error_msg)
    if "message-type" in payload:
        value = payload["message-type"]
        if value not in VALID_BODY_MESSAGE_TYPE:
            desc = FIELD_DESCRIPTIONS.get("message-type", "")
            error_msg = f"Invalid value for 'message-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MESSAGE_TYPE)}"
            error_msg += f"\n  → Example: message-type='{{ VALID_BODY_MESSAGE_TYPE[0] }}'"
            return (False, error_msg)
    if "replacement-message" in payload:
        value = payload["replacement-message"]
        if value not in VALID_BODY_REPLACEMENT_MESSAGE:
            desc = FIELD_DESCRIPTIONS.get("replacement-message", "")
            error_msg = f"Invalid value for 'replacement-message': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_REPLACEMENT_MESSAGE)}"
            error_msg += f"\n  → Example: replacement-message='{{ VALID_BODY_REPLACEMENT_MESSAGE[0] }}'"
            return (False, error_msg)
    if "protocol" in payload:
        value = payload["protocol"]
        if value not in VALID_BODY_PROTOCOL:
            desc = FIELD_DESCRIPTIONS.get("protocol", "")
            error_msg = f"Invalid value for 'protocol': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PROTOCOL)}"
            error_msg += f"\n  → Example: protocol='{{ VALID_BODY_PROTOCOL[0] }}'"
            return (False, error_msg)
    if "method" in payload:
        value = payload["method"]
        if value not in VALID_BODY_METHOD:
            desc = FIELD_DESCRIPTIONS.get("method", "")
            error_msg = f"Invalid value for 'method': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_METHOD)}"
            error_msg += f"\n  → Example: method='{{ VALID_BODY_METHOD[0] }}'"
            return (False, error_msg)
    if "verify-host-cert" in payload:
        value = payload["verify-host-cert"]
        if value not in VALID_BODY_VERIFY_HOST_CERT:
            desc = FIELD_DESCRIPTIONS.get("verify-host-cert", "")
            error_msg = f"Invalid value for 'verify-host-cert': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_VERIFY_HOST_CERT)}"
            error_msg += f"\n  → Example: verify-host-cert='{{ VALID_BODY_VERIFY_HOST_CERT[0] }}'"
            return (False, error_msg)
    if "file-only" in payload:
        value = payload["file-only"]
        if value not in VALID_BODY_FILE_ONLY:
            desc = FIELD_DESCRIPTIONS.get("file-only", "")
            error_msg = f"Invalid value for 'file-only': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FILE_ONLY)}"
            error_msg += f"\n  → Example: file-only='{{ VALID_BODY_FILE_ONLY[0] }}'"
            return (False, error_msg)
    if "execute-security-fabric" in payload:
        value = payload["execute-security-fabric"]
        if value not in VALID_BODY_EXECUTE_SECURITY_FABRIC:
            desc = FIELD_DESCRIPTIONS.get("execute-security-fabric", "")
            error_msg = f"Invalid value for 'execute-security-fabric': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EXECUTE_SECURITY_FABRIC)}"
            error_msg += f"\n  → Example: execute-security-fabric='{{ VALID_BODY_EXECUTE_SECURITY_FABRIC[0] }}'"
            return (False, error_msg)
    if "log-debug-print" in payload:
        value = payload["log-debug-print"]
        if value not in VALID_BODY_LOG_DEBUG_PRINT:
            desc = FIELD_DESCRIPTIONS.get("log-debug-print", "")
            error_msg = f"Invalid value for 'log-debug-print': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOG_DEBUG_PRINT)}"
            error_msg += f"\n  → Example: log-debug-print='{{ VALID_BODY_LOG_DEBUG_PRINT[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_system_automation_action_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update system/automation_action.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_system_automation_action_put(payload)
    """
    # Step 1: Validate enum values
    if "action-type" in payload:
        value = payload["action-type"]
        if value not in VALID_BODY_ACTION_TYPE:
            return (
                False,
                f"Invalid value for 'action-type'='{value}'. Must be one of: {', '.join(VALID_BODY_ACTION_TYPE)}",
            )
    if "system-action" in payload:
        value = payload["system-action"]
        if value not in VALID_BODY_SYSTEM_ACTION:
            return (
                False,
                f"Invalid value for 'system-action'='{value}'. Must be one of: {', '.join(VALID_BODY_SYSTEM_ACTION)}",
            )
    if "forticare-email" in payload:
        value = payload["forticare-email"]
        if value not in VALID_BODY_FORTICARE_EMAIL:
            return (
                False,
                f"Invalid value for 'forticare-email'='{value}'. Must be one of: {', '.join(VALID_BODY_FORTICARE_EMAIL)}",
            )
    if "azure-function-authorization" in payload:
        value = payload["azure-function-authorization"]
        if value not in VALID_BODY_AZURE_FUNCTION_AUTHORIZATION:
            return (
                False,
                f"Invalid value for 'azure-function-authorization'='{value}'. Must be one of: {', '.join(VALID_BODY_AZURE_FUNCTION_AUTHORIZATION)}",
            )
    if "alicloud-function-authorization" in payload:
        value = payload["alicloud-function-authorization"]
        if value not in VALID_BODY_ALICLOUD_FUNCTION_AUTHORIZATION:
            return (
                False,
                f"Invalid value for 'alicloud-function-authorization'='{value}'. Must be one of: {', '.join(VALID_BODY_ALICLOUD_FUNCTION_AUTHORIZATION)}",
            )
    if "message-type" in payload:
        value = payload["message-type"]
        if value not in VALID_BODY_MESSAGE_TYPE:
            return (
                False,
                f"Invalid value for 'message-type'='{value}'. Must be one of: {', '.join(VALID_BODY_MESSAGE_TYPE)}",
            )
    if "replacement-message" in payload:
        value = payload["replacement-message"]
        if value not in VALID_BODY_REPLACEMENT_MESSAGE:
            return (
                False,
                f"Invalid value for 'replacement-message'='{value}'. Must be one of: {', '.join(VALID_BODY_REPLACEMENT_MESSAGE)}",
            )
    if "protocol" in payload:
        value = payload["protocol"]
        if value not in VALID_BODY_PROTOCOL:
            return (
                False,
                f"Invalid value for 'protocol'='{value}'. Must be one of: {', '.join(VALID_BODY_PROTOCOL)}",
            )
    if "method" in payload:
        value = payload["method"]
        if value not in VALID_BODY_METHOD:
            return (
                False,
                f"Invalid value for 'method'='{value}'. Must be one of: {', '.join(VALID_BODY_METHOD)}",
            )
    if "verify-host-cert" in payload:
        value = payload["verify-host-cert"]
        if value not in VALID_BODY_VERIFY_HOST_CERT:
            return (
                False,
                f"Invalid value for 'verify-host-cert'='{value}'. Must be one of: {', '.join(VALID_BODY_VERIFY_HOST_CERT)}",
            )
    if "file-only" in payload:
        value = payload["file-only"]
        if value not in VALID_BODY_FILE_ONLY:
            return (
                False,
                f"Invalid value for 'file-only'='{value}'. Must be one of: {', '.join(VALID_BODY_FILE_ONLY)}",
            )
    if "execute-security-fabric" in payload:
        value = payload["execute-security-fabric"]
        if value not in VALID_BODY_EXECUTE_SECURITY_FABRIC:
            return (
                False,
                f"Invalid value for 'execute-security-fabric'='{value}'. Must be one of: {', '.join(VALID_BODY_EXECUTE_SECURITY_FABRIC)}",
            )
    if "log-debug-print" in payload:
        value = payload["log-debug-print"]
        if value not in VALID_BODY_LOG_DEBUG_PRINT:
            return (
                False,
                f"Invalid value for 'log-debug-print'='{value}'. Must be one of: {', '.join(VALID_BODY_LOG_DEBUG_PRINT)}",
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
    "endpoint": "system/automation_action",
    "category": "cmdb",
    "api_path": "system/automation-action",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Action for automation stitches.",
    "total_fields": 40,
    "required_fields_count": 8,
    "fields_with_defaults_count": 26,
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
