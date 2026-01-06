"""
Validation helpers for voip/profile endpoint.

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
    "name",  # Profile name.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "feature-set": "voipd",
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
    "name": "string",  # Profile name.
    "feature-set": "option",  # IPS or voipd (SIP-ALG) inspection feature set.
    "comment": "var-string",  # Comment.
    "sip": "string",  # SIP.
    "sccp": "string",  # SCCP.
    "msrp": "string",  # MSRP.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Profile name.",
    "feature-set": "IPS or voipd (SIP-ALG) inspection feature set.",
    "comment": "Comment.",
    "sip": "SIP.",
    "sccp": "SCCP.",
    "msrp": "MSRP.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 47},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "sip": {
        "status": {
            "type": "option",
            "help": "Enable/disable SIP.",
            "default": "enable",
            "options": [{"help": "Disable status.", "label": "Disable", "name": "disable"}, {"help": "Enable status.", "label": "Enable", "name": "enable"}],
        },
        "rtp": {
            "type": "option",
            "help": "Enable/disable create pinholes for RTP traffic to traverse firewall.",
            "default": "enable",
            "options": [{"help": "Disable status.", "label": "Disable", "name": "disable"}, {"help": "Enable status.", "label": "Enable", "name": "enable"}],
        },
        "nat-port-range": {
            "type": "user",
            "help": "RTP NAT port range.",
            "default": "5117-65533",
        },
        "open-register-pinhole": {
            "type": "option",
            "help": "Enable/disable open pinhole for REGISTER Contact port.",
            "default": "enable",
            "options": [{"help": "Disable status.", "label": "Disable", "name": "disable"}, {"help": "Enable status.", "label": "Enable", "name": "enable"}],
        },
        "open-contact-pinhole": {
            "type": "option",
            "help": "Enable/disable open pinhole for non-REGISTER Contact port.",
            "default": "enable",
            "options": [{"help": "Disable status.", "label": "Disable", "name": "disable"}, {"help": "Enable status.", "label": "Enable", "name": "enable"}],
        },
        "strict-register": {
            "type": "option",
            "help": "Enable/disable only allow the registrar to connect.",
            "default": "enable",
            "options": [{"help": "Disable status.", "label": "Disable", "name": "disable"}, {"help": "Enable status.", "label": "Enable", "name": "enable"}],
        },
        "register-rate": {
            "type": "integer",
            "help": "REGISTER request rate limit (per second, per policy).",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "register-rate-track": {
            "type": "option",
            "help": "Track the packet protocol field.",
            "default": "none",
            "options": [{"help": "None.", "label": "None", "name": "none"}, {"help": "Source IP.", "label": "Src Ip", "name": "src-ip"}, {"help": "Destination IP.", "label": "Dest Ip", "name": "dest-ip"}],
        },
        "invite-rate": {
            "type": "integer",
            "help": "INVITE request rate limit (per second, per policy).",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "invite-rate-track": {
            "type": "option",
            "help": "Track the packet protocol field.",
            "default": "none",
            "options": [{"help": "None.", "label": "None", "name": "none"}, {"help": "Source IP.", "label": "Src Ip", "name": "src-ip"}, {"help": "Destination IP.", "label": "Dest Ip", "name": "dest-ip"}],
        },
        "max-dialogs": {
            "type": "integer",
            "help": "Maximum number of concurrent calls/dialogs (per policy).",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "max-line-length": {
            "type": "integer",
            "help": "Maximum SIP header line length (78-4096).",
            "default": 998,
            "min_value": 78,
            "max_value": 4096,
        },
        "block-long-lines": {
            "type": "option",
            "help": "Enable/disable block requests with headers exceeding max-line-length.",
            "default": "enable",
            "options": [{"help": "Disable status.", "label": "Disable", "name": "disable"}, {"help": "Enable status.", "label": "Enable", "name": "enable"}],
        },
        "block-unknown": {
            "type": "option",
            "help": "Block unrecognized SIP requests (enabled by default).",
            "default": "enable",
            "options": [{"help": "Disable status.", "label": "Disable", "name": "disable"}, {"help": "Enable status.", "label": "Enable", "name": "enable"}],
        },
        "call-keepalive": {
            "type": "integer",
            "help": "Continue tracking calls with no RTP for this many minutes.",
            "default": 0,
            "min_value": 0,
            "max_value": 10080,
        },
        "block-ack": {
            "type": "option",
            "help": "Enable/disable block ACK requests.",
            "default": "disable",
            "options": [{"help": "Disable status.", "label": "Disable", "name": "disable"}, {"help": "Enable status.", "label": "Enable", "name": "enable"}],
        },
        "block-bye": {
            "type": "option",
            "help": "Enable/disable block BYE requests.",
            "default": "disable",
            "options": [{"help": "Disable status.", "label": "Disable", "name": "disable"}, {"help": "Enable status.", "label": "Enable", "name": "enable"}],
        },
        "block-cancel": {
            "type": "option",
            "help": "Enable/disable block CANCEL requests.",
            "default": "disable",
            "options": [{"help": "Disable status.", "label": "Disable", "name": "disable"}, {"help": "Enable status.", "label": "Enable", "name": "enable"}],
        },
        "block-info": {
            "type": "option",
            "help": "Enable/disable block INFO requests.",
            "default": "disable",
            "options": [{"help": "Disable status.", "label": "Disable", "name": "disable"}, {"help": "Enable status.", "label": "Enable", "name": "enable"}],
        },
        "block-invite": {
            "type": "option",
            "help": "Enable/disable block INVITE requests.",
            "default": "disable",
            "options": [{"help": "Disable status.", "label": "Disable", "name": "disable"}, {"help": "Enable status.", "label": "Enable", "name": "enable"}],
        },
        "block-message": {
            "type": "option",
            "help": "Enable/disable block MESSAGE requests.",
            "default": "disable",
            "options": [{"help": "Disable status.", "label": "Disable", "name": "disable"}, {"help": "Enable status.", "label": "Enable", "name": "enable"}],
        },
        "block-notify": {
            "type": "option",
            "help": "Enable/disable block NOTIFY requests.",
            "default": "disable",
            "options": [{"help": "Disable status.", "label": "Disable", "name": "disable"}, {"help": "Enable status.", "label": "Enable", "name": "enable"}],
        },
        "block-options": {
            "type": "option",
            "help": "Enable/disable block OPTIONS requests and no OPTIONS as notifying message for redundancy either.",
            "default": "disable",
            "options": [{"help": "Disable status.", "label": "Disable", "name": "disable"}, {"help": "Enable status.", "label": "Enable", "name": "enable"}],
        },
        "block-prack": {
            "type": "option",
            "help": "Enable/disable block prack requests.",
            "default": "disable",
            "options": [{"help": "Disable status.", "label": "Disable", "name": "disable"}, {"help": "Enable status.", "label": "Enable", "name": "enable"}],
        },
        "block-publish": {
            "type": "option",
            "help": "Enable/disable block PUBLISH requests.",
            "default": "disable",
            "options": [{"help": "Disable status.", "label": "Disable", "name": "disable"}, {"help": "Enable status.", "label": "Enable", "name": "enable"}],
        },
        "block-refer": {
            "type": "option",
            "help": "Enable/disable block REFER requests.",
            "default": "disable",
            "options": [{"help": "Disable status.", "label": "Disable", "name": "disable"}, {"help": "Enable status.", "label": "Enable", "name": "enable"}],
        },
        "block-register": {
            "type": "option",
            "help": "Enable/disable block REGISTER requests.",
            "default": "disable",
            "options": [{"help": "Disable status.", "label": "Disable", "name": "disable"}, {"help": "Enable status.", "label": "Enable", "name": "enable"}],
        },
        "block-subscribe": {
            "type": "option",
            "help": "Enable/disable block SUBSCRIBE requests.",
            "default": "disable",
            "options": [{"help": "Disable status.", "label": "Disable", "name": "disable"}, {"help": "Enable status.", "label": "Enable", "name": "enable"}],
        },
        "block-update": {
            "type": "option",
            "help": "Enable/disable block UPDATE requests.",
            "default": "disable",
            "options": [{"help": "Disable status.", "label": "Disable", "name": "disable"}, {"help": "Enable status.", "label": "Enable", "name": "enable"}],
        },
        "register-contact-trace": {
            "type": "option",
            "help": "Enable/disable trace original IP/port within the contact header of REGISTER requests.",
            "default": "disable",
            "options": [{"help": "Disable status.", "label": "Disable", "name": "disable"}, {"help": "Enable status.", "label": "Enable", "name": "enable"}],
        },
        "open-via-pinhole": {
            "type": "option",
            "help": "Enable/disable open pinhole for Via port.",
            "default": "disable",
            "options": [{"help": "Disable status.", "label": "Disable", "name": "disable"}, {"help": "Enable status.", "label": "Enable", "name": "enable"}],
        },
        "open-record-route-pinhole": {
            "type": "option",
            "help": "Enable/disable open pinhole for Record-Route port.",
            "default": "enable",
            "options": [{"help": "Disable status.", "label": "Disable", "name": "disable"}, {"help": "Enable status.", "label": "Enable", "name": "enable"}],
        },
        "rfc2543-branch": {
            "type": "option",
            "help": "Enable/disable support via branch compliant with RFC 2543.",
            "default": "disable",
            "options": [{"help": "Disable status.", "label": "Disable", "name": "disable"}, {"help": "Enable status.", "label": "Enable", "name": "enable"}],
        },
        "log-violations": {
            "type": "option",
            "help": "Enable/disable logging of SIP violations.",
            "default": "disable",
            "options": [{"help": "Disable status.", "label": "Disable", "name": "disable"}, {"help": "Enable status.", "label": "Enable", "name": "enable"}],
        },
        "log-call-summary": {
            "type": "option",
            "help": "Enable/disable logging of SIP call summary.",
            "default": "enable",
            "options": [{"help": "Disable status.", "label": "Disable", "name": "disable"}, {"help": "Enable status.", "label": "Enable", "name": "enable"}],
        },
        "nat-trace": {
            "type": "option",
            "help": "Enable/disable preservation of original IP in SDP i line.",
            "default": "enable",
            "options": [{"help": "Disable status.", "label": "Disable", "name": "disable"}, {"help": "Enable status.", "label": "Enable", "name": "enable"}],
        },
        "subscribe-rate": {
            "type": "integer",
            "help": "SUBSCRIBE request rate limit (per second, per policy).",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "subscribe-rate-track": {
            "type": "option",
            "help": "Track the packet protocol field.",
            "default": "none",
            "options": [{"help": "None.", "label": "None", "name": "none"}, {"help": "Source IP.", "label": "Src Ip", "name": "src-ip"}, {"help": "Destination IP.", "label": "Dest Ip", "name": "dest-ip"}],
        },
        "message-rate": {
            "type": "integer",
            "help": "MESSAGE request rate limit (per second, per policy).",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "message-rate-track": {
            "type": "option",
            "help": "Track the packet protocol field.",
            "default": "none",
            "options": [{"help": "None.", "label": "None", "name": "none"}, {"help": "Source IP.", "label": "Src Ip", "name": "src-ip"}, {"help": "Destination IP.", "label": "Dest Ip", "name": "dest-ip"}],
        },
        "notify-rate": {
            "type": "integer",
            "help": "NOTIFY request rate limit (per second, per policy).",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "notify-rate-track": {
            "type": "option",
            "help": "Track the packet protocol field.",
            "default": "none",
            "options": [{"help": "None.", "label": "None", "name": "none"}, {"help": "Source IP.", "label": "Src Ip", "name": "src-ip"}, {"help": "Destination IP.", "label": "Dest Ip", "name": "dest-ip"}],
        },
        "refer-rate": {
            "type": "integer",
            "help": "REFER request rate limit (per second, per policy).",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "refer-rate-track": {
            "type": "option",
            "help": "Track the packet protocol field.",
            "default": "none",
            "options": [{"help": "None.", "label": "None", "name": "none"}, {"help": "Source IP.", "label": "Src Ip", "name": "src-ip"}, {"help": "Destination IP.", "label": "Dest Ip", "name": "dest-ip"}],
        },
        "update-rate": {
            "type": "integer",
            "help": "UPDATE request rate limit (per second, per policy).",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "update-rate-track": {
            "type": "option",
            "help": "Track the packet protocol field.",
            "default": "none",
            "options": [{"help": "None.", "label": "None", "name": "none"}, {"help": "Source IP.", "label": "Src Ip", "name": "src-ip"}, {"help": "Destination IP.", "label": "Dest Ip", "name": "dest-ip"}],
        },
        "options-rate": {
            "type": "integer",
            "help": "OPTIONS request rate limit (per second, per policy).",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "options-rate-track": {
            "type": "option",
            "help": "Track the packet protocol field.",
            "default": "none",
            "options": [{"help": "None.", "label": "None", "name": "none"}, {"help": "Source IP.", "label": "Src Ip", "name": "src-ip"}, {"help": "Destination IP.", "label": "Dest Ip", "name": "dest-ip"}],
        },
        "ack-rate": {
            "type": "integer",
            "help": "ACK request rate limit (per second, per policy).",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "ack-rate-track": {
            "type": "option",
            "help": "Track the packet protocol field.",
            "default": "none",
            "options": [{"help": "None.", "label": "None", "name": "none"}, {"help": "Source IP.", "label": "Src Ip", "name": "src-ip"}, {"help": "Destination IP.", "label": "Dest Ip", "name": "dest-ip"}],
        },
        "prack-rate": {
            "type": "integer",
            "help": "PRACK request rate limit (per second, per policy).",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "prack-rate-track": {
            "type": "option",
            "help": "Track the packet protocol field.",
            "default": "none",
            "options": [{"help": "None.", "label": "None", "name": "none"}, {"help": "Source IP.", "label": "Src Ip", "name": "src-ip"}, {"help": "Destination IP.", "label": "Dest Ip", "name": "dest-ip"}],
        },
        "info-rate": {
            "type": "integer",
            "help": "INFO request rate limit (per second, per policy).",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "info-rate-track": {
            "type": "option",
            "help": "Track the packet protocol field.",
            "default": "none",
            "options": [{"help": "None.", "label": "None", "name": "none"}, {"help": "Source IP.", "label": "Src Ip", "name": "src-ip"}, {"help": "Destination IP.", "label": "Dest Ip", "name": "dest-ip"}],
        },
        "publish-rate": {
            "type": "integer",
            "help": "PUBLISH request rate limit (per second, per policy).",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "publish-rate-track": {
            "type": "option",
            "help": "Track the packet protocol field.",
            "default": "none",
            "options": [{"help": "None.", "label": "None", "name": "none"}, {"help": "Source IP.", "label": "Src Ip", "name": "src-ip"}, {"help": "Destination IP.", "label": "Dest Ip", "name": "dest-ip"}],
        },
        "bye-rate": {
            "type": "integer",
            "help": "BYE request rate limit (per second, per policy).",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "bye-rate-track": {
            "type": "option",
            "help": "Track the packet protocol field.",
            "default": "none",
            "options": [{"help": "None.", "label": "None", "name": "none"}, {"help": "Source IP.", "label": "Src Ip", "name": "src-ip"}, {"help": "Destination IP.", "label": "Dest Ip", "name": "dest-ip"}],
        },
        "cancel-rate": {
            "type": "integer",
            "help": "CANCEL request rate limit (per second, per policy).",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "cancel-rate-track": {
            "type": "option",
            "help": "Track the packet protocol field.",
            "default": "none",
            "options": [{"help": "None.", "label": "None", "name": "none"}, {"help": "Source IP.", "label": "Src Ip", "name": "src-ip"}, {"help": "Destination IP.", "label": "Dest Ip", "name": "dest-ip"}],
        },
        "preserve-override": {
            "type": "option",
            "help": "Override i line to preserve original IPs (default: append).",
            "default": "disable",
            "options": [{"help": "Disable status.", "label": "Disable", "name": "disable"}, {"help": "Enable status.", "label": "Enable", "name": "enable"}],
        },
        "no-sdp-fixup": {
            "type": "option",
            "help": "Enable/disable no SDP fix-up.",
            "default": "disable",
            "options": [{"help": "Disable status.", "label": "Disable", "name": "disable"}, {"help": "Enable status.", "label": "Enable", "name": "enable"}],
        },
        "contact-fixup": {
            "type": "option",
            "help": "Fixup contact anyway even if contact's IP:port doesn't match session's IP:port.",
            "default": "enable",
            "options": [{"help": "Disable status.", "label": "Disable", "name": "disable"}, {"help": "Enable status.", "label": "Enable", "name": "enable"}],
        },
        "max-idle-dialogs": {
            "type": "integer",
            "help": "Maximum number established but idle dialogs to retain (per policy).",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "block-geo-red-options": {
            "type": "option",
            "help": "Enable/disable block OPTIONS requests, but OPTIONS requests still notify for redundancy.",
            "default": "disable",
            "options": [{"help": "Disable status.", "label": "Disable", "name": "disable"}, {"help": "Enable status.", "label": "Enable", "name": "enable"}],
        },
        "hosted-nat-traversal": {
            "type": "option",
            "help": "Hosted NAT Traversal (HNT).",
            "default": "disable",
            "options": [{"help": "Disable status.", "label": "Disable", "name": "disable"}, {"help": "Enable status.", "label": "Enable", "name": "enable"}],
        },
        "hnt-restrict-source-ip": {
            "type": "option",
            "help": "Enable/disable restrict RTP source IP to be the same as SIP source IP when HNT is enabled.",
            "default": "disable",
            "options": [{"help": "Disable status.", "label": "Disable", "name": "disable"}, {"help": "Enable status.", "label": "Enable", "name": "enable"}],
        },
        "call-id-regex": {
            "type": "var-string",
            "help": "Validate PCRE regular expression for Call-Id header value.",
            "max_length": 511,
        },
        "content-type-regex": {
            "type": "var-string",
            "help": "Validate PCRE regular expression for Content-Type header value.",
            "max_length": 511,
        },
        "max-body-length": {
            "type": "integer",
            "help": "Maximum SIP message body length (0 meaning no limit).",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "unknown-header": {
            "type": "option",
            "help": "Action for unknown SIP header.",
            "default": "pass",
            "options": [{"help": "Discard malformed messages.", "label": "Discard", "name": "discard"}, {"help": "Bypass malformed messages.", "label": "Pass", "name": "pass"}, {"help": "Respond with error code.", "label": "Respond", "name": "respond"}],
        },
        "malformed-request-line": {
            "type": "option",
            "help": "Action for malformed request line.",
            "default": "pass",
            "options": [{"help": "Discard malformed messages.", "label": "Discard", "name": "discard"}, {"help": "Bypass malformed messages.", "label": "Pass", "name": "pass"}, {"help": "Respond with error code.", "label": "Respond", "name": "respond"}],
        },
        "malformed-header-via": {
            "type": "option",
            "help": "Action for malformed VIA header.",
            "default": "pass",
            "options": [{"help": "Discard malformed messages.", "label": "Discard", "name": "discard"}, {"help": "Bypass malformed messages.", "label": "Pass", "name": "pass"}, {"help": "Respond with error code.", "label": "Respond", "name": "respond"}],
        },
        "malformed-header-from": {
            "type": "option",
            "help": "Action for malformed From header.",
            "default": "pass",
            "options": [{"help": "Discard malformed messages.", "label": "Discard", "name": "discard"}, {"help": "Bypass malformed messages.", "label": "Pass", "name": "pass"}, {"help": "Respond with error code.", "label": "Respond", "name": "respond"}],
        },
        "malformed-header-to": {
            "type": "option",
            "help": "Action for malformed To header.",
            "default": "pass",
            "options": [{"help": "Discard malformed messages.", "label": "Discard", "name": "discard"}, {"help": "Bypass malformed messages.", "label": "Pass", "name": "pass"}, {"help": "Respond with error code.", "label": "Respond", "name": "respond"}],
        },
        "malformed-header-call-id": {
            "type": "option",
            "help": "Action for malformed Call-ID header.",
            "default": "pass",
            "options": [{"help": "Discard malformed messages.", "label": "Discard", "name": "discard"}, {"help": "Bypass malformed messages.", "label": "Pass", "name": "pass"}, {"help": "Respond with error code.", "label": "Respond", "name": "respond"}],
        },
        "malformed-header-cseq": {
            "type": "option",
            "help": "Action for malformed CSeq header.",
            "default": "pass",
            "options": [{"help": "Discard malformed messages.", "label": "Discard", "name": "discard"}, {"help": "Bypass malformed messages.", "label": "Pass", "name": "pass"}, {"help": "Respond with error code.", "label": "Respond", "name": "respond"}],
        },
        "malformed-header-rack": {
            "type": "option",
            "help": "Action for malformed RAck header.",
            "default": "pass",
            "options": [{"help": "Discard malformed messages.", "label": "Discard", "name": "discard"}, {"help": "Bypass malformed messages.", "label": "Pass", "name": "pass"}, {"help": "Respond with error code.", "label": "Respond", "name": "respond"}],
        },
        "malformed-header-rseq": {
            "type": "option",
            "help": "Action for malformed RSeq header.",
            "default": "pass",
            "options": [{"help": "Discard malformed messages.", "label": "Discard", "name": "discard"}, {"help": "Bypass malformed messages.", "label": "Pass", "name": "pass"}, {"help": "Respond with error code.", "label": "Respond", "name": "respond"}],
        },
        "malformed-header-contact": {
            "type": "option",
            "help": "Action for malformed Contact header.",
            "default": "pass",
            "options": [{"help": "Discard malformed messages.", "label": "Discard", "name": "discard"}, {"help": "Bypass malformed messages.", "label": "Pass", "name": "pass"}, {"help": "Respond with error code.", "label": "Respond", "name": "respond"}],
        },
        "malformed-header-record-route": {
            "type": "option",
            "help": "Action for malformed Record-Route header.",
            "default": "pass",
            "options": [{"help": "Discard malformed messages.", "label": "Discard", "name": "discard"}, {"help": "Bypass malformed messages.", "label": "Pass", "name": "pass"}, {"help": "Respond with error code.", "label": "Respond", "name": "respond"}],
        },
        "malformed-header-route": {
            "type": "option",
            "help": "Action for malformed Route header.",
            "default": "pass",
            "options": [{"help": "Discard malformed messages.", "label": "Discard", "name": "discard"}, {"help": "Bypass malformed messages.", "label": "Pass", "name": "pass"}, {"help": "Respond with error code.", "label": "Respond", "name": "respond"}],
        },
        "malformed-header-expires": {
            "type": "option",
            "help": "Action for malformed Expires header.",
            "default": "pass",
            "options": [{"help": "Discard malformed messages.", "label": "Discard", "name": "discard"}, {"help": "Bypass malformed messages.", "label": "Pass", "name": "pass"}, {"help": "Respond with error code.", "label": "Respond", "name": "respond"}],
        },
        "malformed-header-content-type": {
            "type": "option",
            "help": "Action for malformed Content-Type header.",
            "default": "pass",
            "options": [{"help": "Discard malformed messages.", "label": "Discard", "name": "discard"}, {"help": "Bypass malformed messages.", "label": "Pass", "name": "pass"}, {"help": "Respond with error code.", "label": "Respond", "name": "respond"}],
        },
        "malformed-header-content-length": {
            "type": "option",
            "help": "Action for malformed Content-Length header.",
            "default": "pass",
            "options": [{"help": "Discard malformed messages.", "label": "Discard", "name": "discard"}, {"help": "Bypass malformed messages.", "label": "Pass", "name": "pass"}, {"help": "Respond with error code.", "label": "Respond", "name": "respond"}],
        },
        "malformed-header-max-forwards": {
            "type": "option",
            "help": "Action for malformed Max-Forwards header.",
            "default": "pass",
            "options": [{"help": "Discard malformed messages.", "label": "Discard", "name": "discard"}, {"help": "Bypass malformed messages.", "label": "Pass", "name": "pass"}, {"help": "Respond with error code.", "label": "Respond", "name": "respond"}],
        },
        "malformed-header-allow": {
            "type": "option",
            "help": "Action for malformed Allow header.",
            "default": "pass",
            "options": [{"help": "Discard malformed messages.", "label": "Discard", "name": "discard"}, {"help": "Bypass malformed messages.", "label": "Pass", "name": "pass"}, {"help": "Respond with error code.", "label": "Respond", "name": "respond"}],
        },
        "malformed-header-p-asserted-identity": {
            "type": "option",
            "help": "Action for malformed P-Asserted-Identity header.",
            "default": "pass",
            "options": [{"help": "Discard malformed messages.", "label": "Discard", "name": "discard"}, {"help": "Bypass malformed messages.", "label": "Pass", "name": "pass"}, {"help": "Respond with error code.", "label": "Respond", "name": "respond"}],
        },
        "malformed-header-no-require": {
            "type": "option",
            "help": "Action for malformed SIP messages without Require header.",
            "default": "pass",
            "options": [{"help": "Discard malformed messages.", "label": "Discard", "name": "discard"}, {"help": "Bypass malformed messages.", "label": "Pass", "name": "pass"}, {"help": "Respond with error code.", "label": "Respond", "name": "respond"}],
        },
        "malformed-header-no-proxy-require": {
            "type": "option",
            "help": "Action for malformed SIP messages without Proxy-Require header.",
            "default": "pass",
            "options": [{"help": "Discard malformed messages.", "label": "Discard", "name": "discard"}, {"help": "Bypass malformed messages.", "label": "Pass", "name": "pass"}, {"help": "Respond with error code.", "label": "Respond", "name": "respond"}],
        },
        "malformed-header-sdp-v": {
            "type": "option",
            "help": "Action for malformed SDP v line.",
            "default": "pass",
            "options": [{"help": "Discard malformed messages.", "label": "Discard", "name": "discard"}, {"help": "Bypass malformed messages.", "label": "Pass", "name": "pass"}, {"help": "Respond with error code.", "label": "Respond", "name": "respond"}],
        },
        "malformed-header-sdp-o": {
            "type": "option",
            "help": "Action for malformed SDP o line.",
            "default": "pass",
            "options": [{"help": "Discard malformed messages.", "label": "Discard", "name": "discard"}, {"help": "Bypass malformed messages.", "label": "Pass", "name": "pass"}, {"help": "Respond with error code.", "label": "Respond", "name": "respond"}],
        },
        "malformed-header-sdp-s": {
            "type": "option",
            "help": "Action for malformed SDP s line.",
            "default": "pass",
            "options": [{"help": "Discard malformed messages.", "label": "Discard", "name": "discard"}, {"help": "Bypass malformed messages.", "label": "Pass", "name": "pass"}, {"help": "Respond with error code.", "label": "Respond", "name": "respond"}],
        },
        "malformed-header-sdp-i": {
            "type": "option",
            "help": "Action for malformed SDP i line.",
            "default": "pass",
            "options": [{"help": "Discard malformed messages.", "label": "Discard", "name": "discard"}, {"help": "Bypass malformed messages.", "label": "Pass", "name": "pass"}, {"help": "Respond with error code.", "label": "Respond", "name": "respond"}],
        },
        "malformed-header-sdp-c": {
            "type": "option",
            "help": "Action for malformed SDP c line.",
            "default": "pass",
            "options": [{"help": "Discard malformed messages.", "label": "Discard", "name": "discard"}, {"help": "Bypass malformed messages.", "label": "Pass", "name": "pass"}, {"help": "Respond with error code.", "label": "Respond", "name": "respond"}],
        },
        "malformed-header-sdp-b": {
            "type": "option",
            "help": "Action for malformed SDP b line.",
            "default": "pass",
            "options": [{"help": "Discard malformed messages.", "label": "Discard", "name": "discard"}, {"help": "Bypass malformed messages.", "label": "Pass", "name": "pass"}, {"help": "Respond with error code.", "label": "Respond", "name": "respond"}],
        },
        "malformed-header-sdp-z": {
            "type": "option",
            "help": "Action for malformed SDP z line.",
            "default": "pass",
            "options": [{"help": "Discard malformed messages.", "label": "Discard", "name": "discard"}, {"help": "Bypass malformed messages.", "label": "Pass", "name": "pass"}, {"help": "Respond with error code.", "label": "Respond", "name": "respond"}],
        },
        "malformed-header-sdp-k": {
            "type": "option",
            "help": "Action for malformed SDP k line.",
            "default": "pass",
            "options": [{"help": "Discard malformed messages.", "label": "Discard", "name": "discard"}, {"help": "Bypass malformed messages.", "label": "Pass", "name": "pass"}, {"help": "Respond with error code.", "label": "Respond", "name": "respond"}],
        },
        "malformed-header-sdp-a": {
            "type": "option",
            "help": "Action for malformed SDP a line.",
            "default": "pass",
            "options": [{"help": "Discard malformed messages.", "label": "Discard", "name": "discard"}, {"help": "Bypass malformed messages.", "label": "Pass", "name": "pass"}, {"help": "Respond with error code.", "label": "Respond", "name": "respond"}],
        },
        "malformed-header-sdp-t": {
            "type": "option",
            "help": "Action for malformed SDP t line.",
            "default": "pass",
            "options": [{"help": "Discard malformed messages.", "label": "Discard", "name": "discard"}, {"help": "Bypass malformed messages.", "label": "Pass", "name": "pass"}, {"help": "Respond with error code.", "label": "Respond", "name": "respond"}],
        },
        "malformed-header-sdp-r": {
            "type": "option",
            "help": "Action for malformed SDP r line.",
            "default": "pass",
            "options": [{"help": "Discard malformed messages.", "label": "Discard", "name": "discard"}, {"help": "Bypass malformed messages.", "label": "Pass", "name": "pass"}, {"help": "Respond with error code.", "label": "Respond", "name": "respond"}],
        },
        "malformed-header-sdp-m": {
            "type": "option",
            "help": "Action for malformed SDP m line.",
            "default": "pass",
            "options": [{"help": "Discard malformed messages.", "label": "Discard", "name": "discard"}, {"help": "Bypass malformed messages.", "label": "Pass", "name": "pass"}, {"help": "Respond with error code.", "label": "Respond", "name": "respond"}],
        },
        "provisional-invite-expiry-time": {
            "type": "integer",
            "help": "Expiry time (10-3600, in seconds) for provisional INVITE.",
            "default": 210,
            "min_value": 10,
            "max_value": 3600,
        },
        "ips-rtp": {
            "type": "option",
            "help": "Enable/disable allow IPS on RTP.",
            "default": "enable",
            "options": [{"help": "Disable status.", "label": "Disable", "name": "disable"}, {"help": "Enable status.", "label": "Enable", "name": "enable"}],
        },
        "ssl-mode": {
            "type": "option",
            "help": "SSL/TLS mode for encryption & decryption of traffic.",
            "default": "off",
            "options": [{"help": "No SSL.", "label": "Off", "name": "off"}, {"help": "Client to FortiGate and FortiGate to Server SSL.", "label": "Full", "name": "full"}],
        },
        "ssl-send-empty-frags": {
            "type": "option",
            "help": "Send empty fragments to avoid attack on CBC IV (SSL 3.0 & TLS 1.0 only).",
            "default": "enable",
            "options": [{"help": "Send empty fragments.", "label": "Enable", "name": "enable"}, {"help": "Do not send empty fragments.", "label": "Disable", "name": "disable"}],
        },
        "ssl-client-renegotiation": {
            "type": "option",
            "help": "Allow/block client renegotiation by server.",
            "default": "allow",
            "options": [{"help": "Allow a SSL client to renegotiate.", "label": "Allow", "name": "allow"}, {"help": "Abort any SSL connection that attempts to renegotiate.", "label": "Deny", "name": "deny"}, {"help": "Reject any SSL connection that does not offer a RFC 5746 Secure Renegotiation Indication.", "label": "Secure", "name": "secure"}],
        },
        "ssl-algorithm": {
            "type": "option",
            "help": "Relative strength of encryption algorithms accepted in negotiation.",
            "default": "high",
            "options": [{"help": "High encryption. Allow only AES and ChaCha.", "label": "High", "name": "high"}, {"help": "Medium encryption. Allow AES, ChaCha, 3DES, and RC4.", "label": "Medium", "name": "medium"}, {"help": "Low encryption. Allow AES, ChaCha, 3DES, RC4, and DES.", "label": "Low", "name": "low"}],
        },
        "ssl-pfs": {
            "type": "option",
            "help": "SSL Perfect Forward Secrecy.",
            "default": "allow",
            "options": [{"help": "PFS mandatory.", "label": "Require", "name": "require"}, {"help": "PFS rejected.", "label": "Deny", "name": "deny"}, {"help": "PFS allowed.", "label": "Allow", "name": "allow"}],
        },
        "ssl-min-version": {
            "type": "option",
            "help": "Lowest SSL/TLS version to negotiate.",
            "default": "tls-1.1",
            "options": [{"help": "SSL 3.0.", "label": "Ssl 3.0", "name": "ssl-3.0"}, {"help": "TLS 1.0.", "label": "Tls 1.0", "name": "tls-1.0"}, {"help": "TLS 1.1.", "label": "Tls 1.1", "name": "tls-1.1"}, {"help": "TLS 1.2.", "label": "Tls 1.2", "name": "tls-1.2"}, {"help": "TLS 1.3.", "label": "Tls 1.3", "name": "tls-1.3"}],
        },
        "ssl-max-version": {
            "type": "option",
            "help": "Highest SSL/TLS version to negotiate.",
            "default": "tls-1.3",
            "options": [{"help": "SSL 3.0.", "label": "Ssl 3.0", "name": "ssl-3.0"}, {"help": "TLS 1.0.", "label": "Tls 1.0", "name": "tls-1.0"}, {"help": "TLS 1.1.", "label": "Tls 1.1", "name": "tls-1.1"}, {"help": "TLS 1.2.", "label": "Tls 1.2", "name": "tls-1.2"}, {"help": "TLS 1.3.", "label": "Tls 1.3", "name": "tls-1.3"}],
        },
        "ssl-client-certificate": {
            "type": "string",
            "help": "Name of Certificate to offer to server if requested.",
            "default": "",
            "max_length": 35,
        },
        "ssl-server-certificate": {
            "type": "string",
            "help": "Name of Certificate return to the client in every SSL connection.",
            "required": True,
            "default": "",
            "max_length": 35,
        },
        "ssl-auth-client": {
            "type": "string",
            "help": "Require a client certificate and authenticate it with the peer/peergrp.",
            "default": "",
            "max_length": 35,
        },
        "ssl-auth-server": {
            "type": "string",
            "help": "Authenticate the server's certificate with the peer/peergrp.",
            "default": "",
            "max_length": 35,
        },
    },
    "sccp": {
        "status": {
            "type": "option",
            "help": "Enable/disable SCCP.",
            "default": "enable",
            "options": [{"help": "Disable status.", "label": "Disable", "name": "disable"}, {"help": "Enable status.", "label": "Enable", "name": "enable"}],
        },
        "block-mcast": {
            "type": "option",
            "help": "Enable/disable block multicast RTP connections.",
            "default": "disable",
            "options": [{"help": "Disable status.", "label": "Disable", "name": "disable"}, {"help": "Enable status.", "label": "Enable", "name": "enable"}],
        },
        "verify-header": {
            "type": "option",
            "help": "Enable/disable verify SCCP header content.",
            "default": "disable",
            "options": [{"help": "Disable status.", "label": "Disable", "name": "disable"}, {"help": "Enable status.", "label": "Enable", "name": "enable"}],
        },
        "log-call-summary": {
            "type": "option",
            "help": "Enable/disable log summary of SCCP calls.",
            "default": "disable",
            "options": [{"help": "Disable status.", "label": "Disable", "name": "disable"}, {"help": "Enable status.", "label": "Enable", "name": "enable"}],
        },
        "log-violations": {
            "type": "option",
            "help": "Enable/disable logging of SCCP violations.",
            "default": "disable",
            "options": [{"help": "Disable status.", "label": "Disable", "name": "disable"}, {"help": "Enable status.", "label": "Enable", "name": "enable"}],
        },
        "max-calls": {
            "type": "integer",
            "help": "Maximum calls per minute per SCCP client (max 65535).",
            "default": 0,
            "min_value": 0,
            "max_value": 65535,
        },
    },
    "msrp": {
        "status": {
            "type": "option",
            "help": "Enable/disable MSRP.",
            "default": "enable",
            "options": [{"help": "Disable status.", "label": "Disable", "name": "disable"}, {"help": "Enable status.", "label": "Enable", "name": "enable"}],
        },
        "log-violations": {
            "type": "option",
            "help": "Enable/disable logging of MSRP violations.",
            "default": "enable",
            "options": [{"help": "Disable status.", "label": "Disable", "name": "disable"}, {"help": "Enable status.", "label": "Enable", "name": "enable"}],
        },
        "max-msg-size": {
            "type": "integer",
            "help": "Maximum allowable MSRP message size (1-65535).",
            "default": 0,
            "min_value": 0,
            "max_value": 65535,
        },
        "max-msg-size-action": {
            "type": "option",
            "help": "Action for violation of max-msg-size.",
            "default": "pass",
            "options": [{"help": "Pass or allow matching traffic.", "label": "Pass", "name": "pass"}, {"help": "Block or drop matching traffic.", "label": "Block", "name": "block"}, {"help": "Reset sessions for matching traffic.", "label": "Reset", "name": "reset"}, {"help": "Pass and log matching traffic.", "label": "Monitor", "name": "monitor"}],
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_FEATURE_SET = [
    "ips",  # IPS Engine feature set for ips-voip-filter.
    "voipd",  # SIP ALG feature set for voip-profile.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_voip_profile_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for voip/profile.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_voip_profile_get()
        >>> assert is_valid == True
        
        >>> # Valid - Get specific item by name
        >>> is_valid, error = validate_voip_profile_get(name="test-item")
        >>> assert is_valid == True
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_voip_profile_get(
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
    Validate required fields for voip/profile.

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


def validate_voip_profile_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new voip/profile object.

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
        ...     "name": True,  # Profile name.
        ... }
        >>> is_valid, error = validate_voip_profile_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "name": True,
        ...     "feature-set": "{'name': 'ips', 'help': 'IPS Engine feature set for ips-voip-filter.', 'label': 'Ips', 'description': 'IPS Engine feature set for ips-voip-filter'}",  # Valid enum value
        ... }
        >>> is_valid, error = validate_voip_profile_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["feature-set"] = "invalid-value"
        >>> is_valid, error = validate_voip_profile_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_voip_profile_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
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

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_voip_profile_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update voip/profile.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_voip_profile_put(payload)
    """
    # Step 1: Validate enum values
    if "feature-set" in payload:
        value = payload["feature-set"]
        if value not in VALID_BODY_FEATURE_SET:
            return (
                False,
                f"Invalid value for 'feature-set'='{value}'. Must be one of: {', '.join(VALID_BODY_FEATURE_SET)}",
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
    "endpoint": "voip/profile",
    "category": "cmdb",
    "api_path": "voip/profile",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure VoIP profiles.",
    "total_fields": 6,
    "required_fields_count": 1,
    "fields_with_defaults_count": 2,
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
