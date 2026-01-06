"""Validation helpers for system/automation_action - Auto-generated"""

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
    "email",  # Send notification email.
    "fortiexplorer-notification",  # Send push notification to FortiExplorer.
    "alert",  # Generate FortiOS dashboard alert.
    "disable-ssid",  # Disable interface.
    "system-actions",  # Perform immediate system operations on this FortiGate unit.
    "quarantine",  # Quarantine host.
    "quarantine-forticlient",  # Quarantine FortiClient by EMS.
    "quarantine-nsx",  # Quarantine NSX instance.
    "quarantine-fortinac",  # Quarantine host by FortiNAC.
    "ban-ip",  # Ban IP address.
    "aws-lambda",  # Send log data to integrated AWS service.
    "azure-function",  # Send log data to an Azure function.
    "google-cloud-function",  # Send log data to a Google Cloud function.
    "alicloud-function",  # Send log data to an AliCloud function.
    "webhook",  # Send an HTTP request.
    "cli-script",  # Run CLI script.
    "diagnose-script",  # Run diagnose script.
    "regular-expression",  # Match pattern on input text.
    "slack-notification",  # Send a notification message to a Slack incoming webhook.
    "microsoft-teams-notification",  # Send a notification message to a Microsoft Teams incoming webhook.
]
VALID_BODY_SYSTEM_ACTION = [
    "reboot",  # Reboot this FortiGate unit.
    "shutdown",  # Shutdown this FortiGate unit.
    "backup-config",  # Backup current configuration to the disk revisions.
]
VALID_BODY_FORTICARE_EMAIL = [
    "enable",  # Enable use of your FortiCare email address as the email-to address.
    "disable",  # Disable use of your FortiCare email address as the email-to address.
]
VALID_BODY_AZURE_FUNCTION_AUTHORIZATION = [
    "anonymous",  # Anonymous authorization level (No authorization required).
    "function",  # Function authorization level (Function or Host Key required).
    "admin",  # Admin authorization level (Master Host Key required).
]
VALID_BODY_ALICLOUD_FUNCTION_AUTHORIZATION = [
    "anonymous",  # Anonymous authorization (No authorization required).
    "function",  # Function authorization (Authorization required).
]
VALID_BODY_MESSAGE_TYPE = [
    "text",  # Plaintext.
    "json",  # Custom JSON.
    "form-data",  # Multipart/form-data
]
VALID_BODY_REPLACEMENT_MESSAGE = [
    "enable",  # Enable replacement message.
    "disable",  # Disable replacement message.
]
VALID_BODY_PROTOCOL = [
    "http",  # HTTP.
    "https",  # HTTPS.
]
VALID_BODY_METHOD = [
    "post",  # POST.
    "put",  # PUT.
    "get",  # GET.
    "patch",  # PATCH.
    "delete",  # DELETE.
]
VALID_BODY_VERIFY_HOST_CERT = [
    "enable",  # Enable verification of the remote host certificate.
    "disable",  # Disable verification of the remote host certificate.
]
VALID_BODY_FILE_ONLY = [
    "enable",  # The output of the diag CLI will only be files.
    "disable",  # The output of the diag CLI will be in raw text, output larger than 64KB will be in files.
]
VALID_BODY_EXECUTE_SECURITY_FABRIC = [
    "enable",  # CLI script executes on all FortiGate units in the Security Fabric.
    "disable",  # CLI script executes only on the FortiGate unit that the stitch is triggered.
]
VALID_BODY_LOG_DEBUG_PRINT = [
    "enable",  # Enable logging debug print output from diagnose action.
    "disable",  # Disable logging debug print output from diagnose action.
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
    """Validate GET request parameters for system/automation_action."""
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
    """Validate required fields for system/automation_action."""
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
    """Validate POST request to create new system/automation_action object."""
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
    """Validate PUT request to update system/automation_action."""
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
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
