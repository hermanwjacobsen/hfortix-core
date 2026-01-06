"""Validation helpers for icap/profile - Auto-generated"""

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
    "request-server",  # ICAP server to use for an HTTP request.
    "response-server",  # ICAP server to use for an HTTP response.
    "file-transfer-server",  # ICAP server to use for a file transfer.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "replacemsg-group": "",
    "name": "",
    "request": "disable",
    "response": "disable",
    "file-transfer": "",
    "streaming-content-bypass": "disable",
    "ocr-only": "disable",
    "204-size-limit": 1,
    "204-response": "disable",
    "preview": "disable",
    "preview-data-length": 0,
    "request-server": "",
    "response-server": "",
    "file-transfer-server": "",
    "request-failure": "error",
    "response-failure": "error",
    "file-transfer-failure": "error",
    "request-path": "",
    "response-path": "",
    "file-transfer-path": "",
    "methods": "delete get head options post put trace connect other",
    "response-req-hdr": "enable",
    "respmod-default-action": "forward",
    "icap-block-log": "disable",
    "chunk-encap": "disable",
    "extension-feature": "",
    "scan-progress-interval": 10,
    "timeout": 30,
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
    "replacemsg-group": "string",  # Replacement message group.
    "name": "string",  # ICAP profile name.
    "comment": "var-string",  # Comment.
    "request": "option",  # Enable/disable whether an HTTP request is passed to an ICAP 
    "response": "option",  # Enable/disable whether an HTTP response is passed to an ICAP
    "file-transfer": "option",  # Configure the file transfer protocols to pass transferred fi
    "streaming-content-bypass": "option",  # Enable/disable bypassing of ICAP server for streaming conten
    "ocr-only": "option",  # Enable/disable this FortiGate unit to submit only OCR intere
    "204-size-limit": "integer",  # 204 response size limit to be saved by ICAP client in megaby
    "204-response": "option",  # Enable/disable allowance of 204 response from ICAP server.
    "preview": "option",  # Enable/disable preview of data to ICAP server.
    "preview-data-length": "integer",  # Preview data length to be sent to ICAP server.
    "request-server": "string",  # ICAP server to use for an HTTP request.
    "response-server": "string",  # ICAP server to use for an HTTP response.
    "file-transfer-server": "string",  # ICAP server to use for a file transfer.
    "request-failure": "option",  # Action to take if the ICAP server cannot be contacted when p
    "response-failure": "option",  # Action to take if the ICAP server cannot be contacted when p
    "file-transfer-failure": "option",  # Action to take if the ICAP server cannot be contacted when p
    "request-path": "string",  # Path component of the ICAP URI that identifies the HTTP requ
    "response-path": "string",  # Path component of the ICAP URI that identifies the HTTP resp
    "file-transfer-path": "string",  # Path component of the ICAP URI that identifies the file tran
    "methods": "option",  # The allowed HTTP methods that will be sent to ICAP server fo
    "response-req-hdr": "option",  # Enable/disable addition of req-hdr for ICAP response modific
    "respmod-default-action": "option",  # Default action to ICAP response modification (respmod) proce
    "icap-block-log": "option",  # Enable/disable UTM log when infection found (default = disab
    "chunk-encap": "option",  # Enable/disable chunked encapsulation (default = disable).
    "extension-feature": "option",  # Enable/disable ICAP extension features.
    "scan-progress-interval": "integer",  # Scan progress interval value.
    "timeout": "integer",  # Time (in seconds) that ICAP client waits for the response fr
    "icap-headers": "string",  # Configure ICAP forwarded request headers.
    "respmod-forward-rules": "string",  # ICAP response mode forward rules.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "replacemsg-group": "Replacement message group.",
    "name": "ICAP profile name.",
    "comment": "Comment.",
    "request": "Enable/disable whether an HTTP request is passed to an ICAP server.",
    "response": "Enable/disable whether an HTTP response is passed to an ICAP server.",
    "file-transfer": "Configure the file transfer protocols to pass transferred files to an ICAP server as REQMOD.",
    "streaming-content-bypass": "Enable/disable bypassing of ICAP server for streaming content.",
    "ocr-only": "Enable/disable this FortiGate unit to submit only OCR interested content to the ICAP server.",
    "204-size-limit": "204 response size limit to be saved by ICAP client in megabytes (1 - 10, default = 1 MB).",
    "204-response": "Enable/disable allowance of 204 response from ICAP server.",
    "preview": "Enable/disable preview of data to ICAP server.",
    "preview-data-length": "Preview data length to be sent to ICAP server.",
    "request-server": "ICAP server to use for an HTTP request.",
    "response-server": "ICAP server to use for an HTTP response.",
    "file-transfer-server": "ICAP server to use for a file transfer.",
    "request-failure": "Action to take if the ICAP server cannot be contacted when processing an HTTP request.",
    "response-failure": "Action to take if the ICAP server cannot be contacted when processing an HTTP response.",
    "file-transfer-failure": "Action to take if the ICAP server cannot be contacted when processing a file transfer.",
    "request-path": "Path component of the ICAP URI that identifies the HTTP request processing service.",
    "response-path": "Path component of the ICAP URI that identifies the HTTP response processing service.",
    "file-transfer-path": "Path component of the ICAP URI that identifies the file transfer processing service.",
    "methods": "The allowed HTTP methods that will be sent to ICAP server for further processing.",
    "response-req-hdr": "Enable/disable addition of req-hdr for ICAP response modification (respmod) processing.",
    "respmod-default-action": "Default action to ICAP response modification (respmod) processing.",
    "icap-block-log": "Enable/disable UTM log when infection found (default = disable).",
    "chunk-encap": "Enable/disable chunked encapsulation (default = disable).",
    "extension-feature": "Enable/disable ICAP extension features.",
    "scan-progress-interval": "Scan progress interval value.",
    "timeout": "Time (in seconds) that ICAP client waits for the response from ICAP server.",
    "icap-headers": "Configure ICAP forwarded request headers.",
    "respmod-forward-rules": "ICAP response mode forward rules.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "replacemsg-group": {"type": "string", "max_length": 35},
    "name": {"type": "string", "max_length": 47},
    "204-size-limit": {"type": "integer", "min": 1, "max": 10},
    "preview-data-length": {"type": "integer", "min": 0, "max": 4096},
    "request-server": {"type": "string", "max_length": 63},
    "response-server": {"type": "string", "max_length": 63},
    "file-transfer-server": {"type": "string", "max_length": 63},
    "request-path": {"type": "string", "max_length": 127},
    "response-path": {"type": "string", "max_length": 127},
    "file-transfer-path": {"type": "string", "max_length": 127},
    "scan-progress-interval": {"type": "integer", "min": 5, "max": 30},
    "timeout": {"type": "integer", "min": 30, "max": 3600},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "icap-headers": {
        "id": {
            "type": "integer",
            "help": "HTTP forwarded header ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "name": {
            "type": "string",
            "help": "HTTP forwarded header name.",
            "default": "",
            "max_length": 79,
        },
        "content": {
            "type": "string",
            "help": "HTTP header content.",
            "default": "",
            "max_length": 255,
        },
        "base64-encoding": {
            "type": "option",
            "help": "Enable/disable use of base64 encoding of HTTP content.",
            "default": "disable",
            "options": [{"help": "Disable use of base64 encoding of HTTP content.", "label": "Disable", "name": "disable"}, {"help": "Enable use of base64 encoding of HTTP content.", "label": "Enable", "name": "enable"}],
        },
    },
    "respmod-forward-rules": {
        "name": {
            "type": "string",
            "help": "Address name.",
            "default": "",
            "max_length": 63,
        },
        "host": {
            "type": "string",
            "help": "Address object for the host.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
        "header-group": {
            "type": "string",
            "help": "HTTP header group.",
        },
        "action": {
            "type": "option",
            "help": "Action to be taken for ICAP server.",
            "default": "forward",
            "options": [{"help": "Forward request to ICAP server when this rule is matched.", "label": "Forward", "name": "forward"}, {"help": "Don\u0027t forward request to ICAP server when this rule is matched.", "label": "Bypass", "name": "bypass"}],
        },
        "http-resp-status-code": {
            "type": "string",
            "help": "HTTP response status code.",
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_REQUEST = [
    "disable",  # Disable HTTP request passing to ICAP server.
    "enable",  # Enable HTTP request passing to ICAP server.
]
VALID_BODY_RESPONSE = [
    "disable",  # Disable HTTP response passing to ICAP server.
    "enable",  # Enable HTTP response passing to ICAP server.
]
VALID_BODY_FILE_TRANSFER = [
    "ssh",  # Forward file transfer with SSH protocol to ICAP server for further processing.
    "ftp",  # Forward file transfer with FTP protocol to ICAP server for further processing.
]
VALID_BODY_STREAMING_CONTENT_BYPASS = [
    "disable",  # Disable bypassing of ICAP server for streaming content.
    "enable",  # Enable bypassing of ICAP server for streaming content.
]
VALID_BODY_OCR_ONLY = [
    "disable",  # Disable this FortiGate unit to submit only OCR interested content to the ICAP server.
    "enable",  # Enable this FortiGate unit to submit only OCR interested content to the ICAP server.
]
VALID_BODY_204_RESPONSE = [
    "disable",  # Disable allowance of 204 response from ICAP server.
    "enable",  # Enable allowance of 204 response from ICAP server.
]
VALID_BODY_PREVIEW = [
    "disable",  # Disable preview of data to ICAP server.
    "enable",  # Enable preview of data to ICAP server.
]
VALID_BODY_REQUEST_FAILURE = [
    "error",  # Error.
    "bypass",  # Bypass.
]
VALID_BODY_RESPONSE_FAILURE = [
    "error",  # Error.
    "bypass",  # Bypass.
]
VALID_BODY_FILE_TRANSFER_FAILURE = [
    "error",  # Error.
    "bypass",  # Bypass.
]
VALID_BODY_METHODS = [
    "delete",  # Forward HTTP request or response with DELETE method to ICAP server for further processing.
    "get",  # Forward HTTP request or response with GET method to ICAP server for further processing.
    "head",  # Forward HTTP request or response with HEAD method to ICAP server for further processing.
    "options",  # Forward HTTP request or response with OPTIONS method to ICAP server for further processing.
    "post",  # Forward HTTP request or response with POST method to ICAP server for further processing.
    "put",  # Forward HTTP request or response with PUT method to ICAP server for further processing.
    "trace",  # Forward HTTP request or response with TRACE method to ICAP server for further processing.
    "connect",  # Forward HTTP request or response with CONNECT method to ICAP server for further processing.
    "other",  # Forward HTTP request or response with All other methods to ICAP server for further processing.
]
VALID_BODY_RESPONSE_REQ_HDR = [
    "disable",  # Do not add req-hdr for response modification (respmod) processing.
    "enable",  # Add req-hdr for response modification (respmod) processing.
]
VALID_BODY_RESPMOD_DEFAULT_ACTION = [
    "forward",  # Forward response to ICAP server unless a rule specifies not to.
    "bypass",  # Don't forward request to ICAP server unless a rule specifies to forward the request.
]
VALID_BODY_ICAP_BLOCK_LOG = [
    "disable",  # Disable UTM log when infection found.
    "enable",  # Enable UTM log when infection found.
]
VALID_BODY_CHUNK_ENCAP = [
    "disable",  # Do not encapsulate chunked data.
    "enable",  # Encapsulate chunked data into a new chunk.
]
VALID_BODY_EXTENSION_FEATURE = [
    "scan-progress",  # Support X-Scan-Progress-Interval ICAP header.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_icap_profile_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for icap/profile."""
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
    """Validate required fields for icap/profile."""
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


def validate_icap_profile_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new icap/profile object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "request" in payload:
        value = payload["request"]
        if value not in VALID_BODY_REQUEST:
            desc = FIELD_DESCRIPTIONS.get("request", "")
            error_msg = f"Invalid value for 'request': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_REQUEST)}"
            error_msg += f"\n  → Example: request='{{ VALID_BODY_REQUEST[0] }}'"
            return (False, error_msg)
    if "response" in payload:
        value = payload["response"]
        if value not in VALID_BODY_RESPONSE:
            desc = FIELD_DESCRIPTIONS.get("response", "")
            error_msg = f"Invalid value for 'response': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_RESPONSE)}"
            error_msg += f"\n  → Example: response='{{ VALID_BODY_RESPONSE[0] }}'"
            return (False, error_msg)
    if "file-transfer" in payload:
        value = payload["file-transfer"]
        if value not in VALID_BODY_FILE_TRANSFER:
            desc = FIELD_DESCRIPTIONS.get("file-transfer", "")
            error_msg = f"Invalid value for 'file-transfer': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FILE_TRANSFER)}"
            error_msg += f"\n  → Example: file-transfer='{{ VALID_BODY_FILE_TRANSFER[0] }}'"
            return (False, error_msg)
    if "streaming-content-bypass" in payload:
        value = payload["streaming-content-bypass"]
        if value not in VALID_BODY_STREAMING_CONTENT_BYPASS:
            desc = FIELD_DESCRIPTIONS.get("streaming-content-bypass", "")
            error_msg = f"Invalid value for 'streaming-content-bypass': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_STREAMING_CONTENT_BYPASS)}"
            error_msg += f"\n  → Example: streaming-content-bypass='{{ VALID_BODY_STREAMING_CONTENT_BYPASS[0] }}'"
            return (False, error_msg)
    if "ocr-only" in payload:
        value = payload["ocr-only"]
        if value not in VALID_BODY_OCR_ONLY:
            desc = FIELD_DESCRIPTIONS.get("ocr-only", "")
            error_msg = f"Invalid value for 'ocr-only': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OCR_ONLY)}"
            error_msg += f"\n  → Example: ocr-only='{{ VALID_BODY_OCR_ONLY[0] }}'"
            return (False, error_msg)
    if "204-response" in payload:
        value = payload["204-response"]
        if value not in VALID_BODY_204_RESPONSE:
            desc = FIELD_DESCRIPTIONS.get("204-response", "")
            error_msg = f"Invalid value for '204-response': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_204_RESPONSE)}"
            error_msg += f"\n  → Example: 204-response='{{ VALID_BODY_204_RESPONSE[0] }}'"
            return (False, error_msg)
    if "preview" in payload:
        value = payload["preview"]
        if value not in VALID_BODY_PREVIEW:
            desc = FIELD_DESCRIPTIONS.get("preview", "")
            error_msg = f"Invalid value for 'preview': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PREVIEW)}"
            error_msg += f"\n  → Example: preview='{{ VALID_BODY_PREVIEW[0] }}'"
            return (False, error_msg)
    if "request-failure" in payload:
        value = payload["request-failure"]
        if value not in VALID_BODY_REQUEST_FAILURE:
            desc = FIELD_DESCRIPTIONS.get("request-failure", "")
            error_msg = f"Invalid value for 'request-failure': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_REQUEST_FAILURE)}"
            error_msg += f"\n  → Example: request-failure='{{ VALID_BODY_REQUEST_FAILURE[0] }}'"
            return (False, error_msg)
    if "response-failure" in payload:
        value = payload["response-failure"]
        if value not in VALID_BODY_RESPONSE_FAILURE:
            desc = FIELD_DESCRIPTIONS.get("response-failure", "")
            error_msg = f"Invalid value for 'response-failure': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_RESPONSE_FAILURE)}"
            error_msg += f"\n  → Example: response-failure='{{ VALID_BODY_RESPONSE_FAILURE[0] }}'"
            return (False, error_msg)
    if "file-transfer-failure" in payload:
        value = payload["file-transfer-failure"]
        if value not in VALID_BODY_FILE_TRANSFER_FAILURE:
            desc = FIELD_DESCRIPTIONS.get("file-transfer-failure", "")
            error_msg = f"Invalid value for 'file-transfer-failure': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FILE_TRANSFER_FAILURE)}"
            error_msg += f"\n  → Example: file-transfer-failure='{{ VALID_BODY_FILE_TRANSFER_FAILURE[0] }}'"
            return (False, error_msg)
    if "methods" in payload:
        value = payload["methods"]
        if value not in VALID_BODY_METHODS:
            desc = FIELD_DESCRIPTIONS.get("methods", "")
            error_msg = f"Invalid value for 'methods': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_METHODS)}"
            error_msg += f"\n  → Example: methods='{{ VALID_BODY_METHODS[0] }}'"
            return (False, error_msg)
    if "response-req-hdr" in payload:
        value = payload["response-req-hdr"]
        if value not in VALID_BODY_RESPONSE_REQ_HDR:
            desc = FIELD_DESCRIPTIONS.get("response-req-hdr", "")
            error_msg = f"Invalid value for 'response-req-hdr': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_RESPONSE_REQ_HDR)}"
            error_msg += f"\n  → Example: response-req-hdr='{{ VALID_BODY_RESPONSE_REQ_HDR[0] }}'"
            return (False, error_msg)
    if "respmod-default-action" in payload:
        value = payload["respmod-default-action"]
        if value not in VALID_BODY_RESPMOD_DEFAULT_ACTION:
            desc = FIELD_DESCRIPTIONS.get("respmod-default-action", "")
            error_msg = f"Invalid value for 'respmod-default-action': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_RESPMOD_DEFAULT_ACTION)}"
            error_msg += f"\n  → Example: respmod-default-action='{{ VALID_BODY_RESPMOD_DEFAULT_ACTION[0] }}'"
            return (False, error_msg)
    if "icap-block-log" in payload:
        value = payload["icap-block-log"]
        if value not in VALID_BODY_ICAP_BLOCK_LOG:
            desc = FIELD_DESCRIPTIONS.get("icap-block-log", "")
            error_msg = f"Invalid value for 'icap-block-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ICAP_BLOCK_LOG)}"
            error_msg += f"\n  → Example: icap-block-log='{{ VALID_BODY_ICAP_BLOCK_LOG[0] }}'"
            return (False, error_msg)
    if "chunk-encap" in payload:
        value = payload["chunk-encap"]
        if value not in VALID_BODY_CHUNK_ENCAP:
            desc = FIELD_DESCRIPTIONS.get("chunk-encap", "")
            error_msg = f"Invalid value for 'chunk-encap': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CHUNK_ENCAP)}"
            error_msg += f"\n  → Example: chunk-encap='{{ VALID_BODY_CHUNK_ENCAP[0] }}'"
            return (False, error_msg)
    if "extension-feature" in payload:
        value = payload["extension-feature"]
        if value not in VALID_BODY_EXTENSION_FEATURE:
            desc = FIELD_DESCRIPTIONS.get("extension-feature", "")
            error_msg = f"Invalid value for 'extension-feature': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EXTENSION_FEATURE)}"
            error_msg += f"\n  → Example: extension-feature='{{ VALID_BODY_EXTENSION_FEATURE[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_icap_profile_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update icap/profile."""
    # Step 1: Validate enum values
    if "request" in payload:
        value = payload["request"]
        if value not in VALID_BODY_REQUEST:
            return (
                False,
                f"Invalid value for 'request'='{value}'. Must be one of: {', '.join(VALID_BODY_REQUEST)}",
            )
    if "response" in payload:
        value = payload["response"]
        if value not in VALID_BODY_RESPONSE:
            return (
                False,
                f"Invalid value for 'response'='{value}'. Must be one of: {', '.join(VALID_BODY_RESPONSE)}",
            )
    if "file-transfer" in payload:
        value = payload["file-transfer"]
        if value not in VALID_BODY_FILE_TRANSFER:
            return (
                False,
                f"Invalid value for 'file-transfer'='{value}'. Must be one of: {', '.join(VALID_BODY_FILE_TRANSFER)}",
            )
    if "streaming-content-bypass" in payload:
        value = payload["streaming-content-bypass"]
        if value not in VALID_BODY_STREAMING_CONTENT_BYPASS:
            return (
                False,
                f"Invalid value for 'streaming-content-bypass'='{value}'. Must be one of: {', '.join(VALID_BODY_STREAMING_CONTENT_BYPASS)}",
            )
    if "ocr-only" in payload:
        value = payload["ocr-only"]
        if value not in VALID_BODY_OCR_ONLY:
            return (
                False,
                f"Invalid value for 'ocr-only'='{value}'. Must be one of: {', '.join(VALID_BODY_OCR_ONLY)}",
            )
    if "204-response" in payload:
        value = payload["204-response"]
        if value not in VALID_BODY_204_RESPONSE:
            return (
                False,
                f"Invalid value for '204-response'='{value}'. Must be one of: {', '.join(VALID_BODY_204_RESPONSE)}",
            )
    if "preview" in payload:
        value = payload["preview"]
        if value not in VALID_BODY_PREVIEW:
            return (
                False,
                f"Invalid value for 'preview'='{value}'. Must be one of: {', '.join(VALID_BODY_PREVIEW)}",
            )
    if "request-failure" in payload:
        value = payload["request-failure"]
        if value not in VALID_BODY_REQUEST_FAILURE:
            return (
                False,
                f"Invalid value for 'request-failure'='{value}'. Must be one of: {', '.join(VALID_BODY_REQUEST_FAILURE)}",
            )
    if "response-failure" in payload:
        value = payload["response-failure"]
        if value not in VALID_BODY_RESPONSE_FAILURE:
            return (
                False,
                f"Invalid value for 'response-failure'='{value}'. Must be one of: {', '.join(VALID_BODY_RESPONSE_FAILURE)}",
            )
    if "file-transfer-failure" in payload:
        value = payload["file-transfer-failure"]
        if value not in VALID_BODY_FILE_TRANSFER_FAILURE:
            return (
                False,
                f"Invalid value for 'file-transfer-failure'='{value}'. Must be one of: {', '.join(VALID_BODY_FILE_TRANSFER_FAILURE)}",
            )
    if "methods" in payload:
        value = payload["methods"]
        if value not in VALID_BODY_METHODS:
            return (
                False,
                f"Invalid value for 'methods'='{value}'. Must be one of: {', '.join(VALID_BODY_METHODS)}",
            )
    if "response-req-hdr" in payload:
        value = payload["response-req-hdr"]
        if value not in VALID_BODY_RESPONSE_REQ_HDR:
            return (
                False,
                f"Invalid value for 'response-req-hdr'='{value}'. Must be one of: {', '.join(VALID_BODY_RESPONSE_REQ_HDR)}",
            )
    if "respmod-default-action" in payload:
        value = payload["respmod-default-action"]
        if value not in VALID_BODY_RESPMOD_DEFAULT_ACTION:
            return (
                False,
                f"Invalid value for 'respmod-default-action'='{value}'. Must be one of: {', '.join(VALID_BODY_RESPMOD_DEFAULT_ACTION)}",
            )
    if "icap-block-log" in payload:
        value = payload["icap-block-log"]
        if value not in VALID_BODY_ICAP_BLOCK_LOG:
            return (
                False,
                f"Invalid value for 'icap-block-log'='{value}'. Must be one of: {', '.join(VALID_BODY_ICAP_BLOCK_LOG)}",
            )
    if "chunk-encap" in payload:
        value = payload["chunk-encap"]
        if value not in VALID_BODY_CHUNK_ENCAP:
            return (
                False,
                f"Invalid value for 'chunk-encap'='{value}'. Must be one of: {', '.join(VALID_BODY_CHUNK_ENCAP)}",
            )
    if "extension-feature" in payload:
        value = payload["extension-feature"]
        if value not in VALID_BODY_EXTENSION_FEATURE:
            return (
                False,
                f"Invalid value for 'extension-feature'='{value}'. Must be one of: {', '.join(VALID_BODY_EXTENSION_FEATURE)}",
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
    "endpoint": "icap/profile",
    "category": "cmdb",
    "api_path": "icap/profile",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure ICAP profiles.",
    "total_fields": 31,
    "required_fields_count": 3,
    "fields_with_defaults_count": 28,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
