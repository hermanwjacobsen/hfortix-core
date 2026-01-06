"""Validation helpers for ztna/web_portal - Auto-generated"""

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
    "name": "",
    "vip": "",
    "host": "",
    "decrypted-traffic-mirror": "",
    "log-blocked-traffic": "enable",
    "auth-portal": "disable",
    "auth-virtual-host": "",
    "vip6": "",
    "auth-rule": "",
    "display-bookmark": "enable",
    "focus-bookmark": "disable",
    "display-status": "enable",
    "display-history": "disable",
    "policy-auth-sso": "enable",
    "heading": "ZTNA Portal",
    "theme": "security-fabric",
    "clipboard": "enable",
    "default-window-width": 1024,
    "default-window-height": 768,
    "cookie-age": 60,
    "forticlient-download": "enable",
    "customize-forticlient-download-url": "disable",
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
    "name": "string",  # ZTNA proxy name.
    "vip": "string",  # Virtual IP name.
    "host": "string",  # Virtual or real host name.
    "decrypted-traffic-mirror": "string",  # Decrypted traffic mirror.
    "log-blocked-traffic": "option",  # Enable/disable logging of blocked traffic.
    "auth-portal": "option",  # Enable/disable authentication portal.
    "auth-virtual-host": "string",  # Virtual host for authentication portal.
    "vip6": "string",  # Virtual IPv6 name.
    "auth-rule": "string",  # Authentication Rule.
    "display-bookmark": "option",  # Enable to display the web portal bookmark widget.
    "focus-bookmark": "option",  # Enable to prioritize the placement of the bookmark section o
    "display-status": "option",  # Enable to display the web portal status widget.
    "display-history": "option",  # Enable to display the web portal user login history widget.
    "policy-auth-sso": "option",  # Enable policy sso authentication.
    "heading": "string",  # Web portal heading message.
    "theme": "option",  # Web portal color scheme.
    "clipboard": "option",  # Enable to support RDP/VPC clipboard functionality.
    "default-window-width": "integer",  # Screen width (range from 0 - 65535, default = 1024).
    "default-window-height": "integer",  # Screen height (range from 0 - 65535, default = 768).
    "cookie-age": "integer",  # Time in minutes that client web browsers should keep a cooki
    "forticlient-download": "option",  # Enable/disable download option for FortiClient.
    "customize-forticlient-download-url": "option",  # Enable support of customized download URL for FortiClient.
    "windows-forticlient-download-url": "var-string",  # Download URL for Windows FortiClient.
    "macos-forticlient-download-url": "var-string",  # Download URL for Mac FortiClient.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "ZTNA proxy name.",
    "vip": "Virtual IP name.",
    "host": "Virtual or real host name.",
    "decrypted-traffic-mirror": "Decrypted traffic mirror.",
    "log-blocked-traffic": "Enable/disable logging of blocked traffic.",
    "auth-portal": "Enable/disable authentication portal.",
    "auth-virtual-host": "Virtual host for authentication portal.",
    "vip6": "Virtual IPv6 name.",
    "auth-rule": "Authentication Rule.",
    "display-bookmark": "Enable to display the web portal bookmark widget.",
    "focus-bookmark": "Enable to prioritize the placement of the bookmark section over the quick-connection section in the ztna web-portal.",
    "display-status": "Enable to display the web portal status widget.",
    "display-history": "Enable to display the web portal user login history widget.",
    "policy-auth-sso": "Enable policy sso authentication.",
    "heading": "Web portal heading message.",
    "theme": "Web portal color scheme.",
    "clipboard": "Enable to support RDP/VPC clipboard functionality.",
    "default-window-width": "Screen width (range from 0 - 65535, default = 1024).",
    "default-window-height": "Screen height (range from 0 - 65535, default = 768).",
    "cookie-age": "Time in minutes that client web browsers should keep a cookie. Default is 60 minutes. 0 = no time limit.",
    "forticlient-download": "Enable/disable download option for FortiClient.",
    "customize-forticlient-download-url": "Enable support of customized download URL for FortiClient.",
    "windows-forticlient-download-url": "Download URL for Windows FortiClient.",
    "macos-forticlient-download-url": "Download URL for Mac FortiClient.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 79},
    "vip": {"type": "string", "max_length": 79},
    "host": {"type": "string", "max_length": 79},
    "decrypted-traffic-mirror": {"type": "string", "max_length": 35},
    "auth-virtual-host": {"type": "string", "max_length": 79},
    "vip6": {"type": "string", "max_length": 79},
    "auth-rule": {"type": "string", "max_length": 35},
    "heading": {"type": "string", "max_length": 31},
    "default-window-width": {"type": "integer", "min": 0, "max": 65535},
    "default-window-height": {"type": "integer", "min": 0, "max": 65535},
    "cookie-age": {"type": "integer", "min": 0, "max": 525600},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_LOG_BLOCKED_TRAFFIC = [
    "disable",  # Do not log all traffic denied by this ZTNA web-proxy.
    "enable",  # Log all traffic denied by this ZTNA web-proxy.
]
VALID_BODY_AUTH_PORTAL = [
    "disable",  # Disable authentication portal.
    "enable",  # Enable authentication portal.
]
VALID_BODY_DISPLAY_BOOKMARK = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_FOCUS_BOOKMARK = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_DISPLAY_STATUS = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_DISPLAY_HISTORY = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_POLICY_AUTH_SSO = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_THEME = [
    "jade",  # Jade theme.
    "neutrino",  # Neutrino theme.
    "mariner",  # Mariner theme.
    "graphite",  # Graphite theme.
    "melongene",  # Melongene theme.
    "jet-stream",  # Jet Stream theme.
    "security-fabric",  # Security Fabric theme.
    "dark-matter",  # Dark Matter theme.
    "onyx",  # Onyx theme.
    "eclipse",  # Eclipse theme.
]
VALID_BODY_CLIPBOARD = [
    "enable",  # Enable support of RDP/VNC clipboard.
    "disable",  # Disable support of RDP/VNC clipboard.
]
VALID_BODY_FORTICLIENT_DOWNLOAD = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_CUSTOMIZE_FORTICLIENT_DOWNLOAD_URL = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_ztna_web_portal_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for ztna/web_portal."""
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
    """Validate required fields for ztna/web_portal."""
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


def validate_ztna_web_portal_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new ztna/web_portal object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "log-blocked-traffic" in payload:
        value = payload["log-blocked-traffic"]
        if value not in VALID_BODY_LOG_BLOCKED_TRAFFIC:
            desc = FIELD_DESCRIPTIONS.get("log-blocked-traffic", "")
            error_msg = f"Invalid value for 'log-blocked-traffic': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOG_BLOCKED_TRAFFIC)}"
            error_msg += f"\n  → Example: log-blocked-traffic='{{ VALID_BODY_LOG_BLOCKED_TRAFFIC[0] }}'"
            return (False, error_msg)
    if "auth-portal" in payload:
        value = payload["auth-portal"]
        if value not in VALID_BODY_AUTH_PORTAL:
            desc = FIELD_DESCRIPTIONS.get("auth-portal", "")
            error_msg = f"Invalid value for 'auth-portal': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTH_PORTAL)}"
            error_msg += f"\n  → Example: auth-portal='{{ VALID_BODY_AUTH_PORTAL[0] }}'"
            return (False, error_msg)
    if "display-bookmark" in payload:
        value = payload["display-bookmark"]
        if value not in VALID_BODY_DISPLAY_BOOKMARK:
            desc = FIELD_DESCRIPTIONS.get("display-bookmark", "")
            error_msg = f"Invalid value for 'display-bookmark': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DISPLAY_BOOKMARK)}"
            error_msg += f"\n  → Example: display-bookmark='{{ VALID_BODY_DISPLAY_BOOKMARK[0] }}'"
            return (False, error_msg)
    if "focus-bookmark" in payload:
        value = payload["focus-bookmark"]
        if value not in VALID_BODY_FOCUS_BOOKMARK:
            desc = FIELD_DESCRIPTIONS.get("focus-bookmark", "")
            error_msg = f"Invalid value for 'focus-bookmark': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FOCUS_BOOKMARK)}"
            error_msg += f"\n  → Example: focus-bookmark='{{ VALID_BODY_FOCUS_BOOKMARK[0] }}'"
            return (False, error_msg)
    if "display-status" in payload:
        value = payload["display-status"]
        if value not in VALID_BODY_DISPLAY_STATUS:
            desc = FIELD_DESCRIPTIONS.get("display-status", "")
            error_msg = f"Invalid value for 'display-status': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DISPLAY_STATUS)}"
            error_msg += f"\n  → Example: display-status='{{ VALID_BODY_DISPLAY_STATUS[0] }}'"
            return (False, error_msg)
    if "display-history" in payload:
        value = payload["display-history"]
        if value not in VALID_BODY_DISPLAY_HISTORY:
            desc = FIELD_DESCRIPTIONS.get("display-history", "")
            error_msg = f"Invalid value for 'display-history': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DISPLAY_HISTORY)}"
            error_msg += f"\n  → Example: display-history='{{ VALID_BODY_DISPLAY_HISTORY[0] }}'"
            return (False, error_msg)
    if "policy-auth-sso" in payload:
        value = payload["policy-auth-sso"]
        if value not in VALID_BODY_POLICY_AUTH_SSO:
            desc = FIELD_DESCRIPTIONS.get("policy-auth-sso", "")
            error_msg = f"Invalid value for 'policy-auth-sso': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_POLICY_AUTH_SSO)}"
            error_msg += f"\n  → Example: policy-auth-sso='{{ VALID_BODY_POLICY_AUTH_SSO[0] }}'"
            return (False, error_msg)
    if "theme" in payload:
        value = payload["theme"]
        if value not in VALID_BODY_THEME:
            desc = FIELD_DESCRIPTIONS.get("theme", "")
            error_msg = f"Invalid value for 'theme': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_THEME)}"
            error_msg += f"\n  → Example: theme='{{ VALID_BODY_THEME[0] }}'"
            return (False, error_msg)
    if "clipboard" in payload:
        value = payload["clipboard"]
        if value not in VALID_BODY_CLIPBOARD:
            desc = FIELD_DESCRIPTIONS.get("clipboard", "")
            error_msg = f"Invalid value for 'clipboard': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CLIPBOARD)}"
            error_msg += f"\n  → Example: clipboard='{{ VALID_BODY_CLIPBOARD[0] }}'"
            return (False, error_msg)
    if "forticlient-download" in payload:
        value = payload["forticlient-download"]
        if value not in VALID_BODY_FORTICLIENT_DOWNLOAD:
            desc = FIELD_DESCRIPTIONS.get("forticlient-download", "")
            error_msg = f"Invalid value for 'forticlient-download': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FORTICLIENT_DOWNLOAD)}"
            error_msg += f"\n  → Example: forticlient-download='{{ VALID_BODY_FORTICLIENT_DOWNLOAD[0] }}'"
            return (False, error_msg)
    if "customize-forticlient-download-url" in payload:
        value = payload["customize-forticlient-download-url"]
        if value not in VALID_BODY_CUSTOMIZE_FORTICLIENT_DOWNLOAD_URL:
            desc = FIELD_DESCRIPTIONS.get("customize-forticlient-download-url", "")
            error_msg = f"Invalid value for 'customize-forticlient-download-url': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CUSTOMIZE_FORTICLIENT_DOWNLOAD_URL)}"
            error_msg += f"\n  → Example: customize-forticlient-download-url='{{ VALID_BODY_CUSTOMIZE_FORTICLIENT_DOWNLOAD_URL[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_ztna_web_portal_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update ztna/web_portal."""
    # Step 1: Validate enum values
    if "log-blocked-traffic" in payload:
        value = payload["log-blocked-traffic"]
        if value not in VALID_BODY_LOG_BLOCKED_TRAFFIC:
            return (
                False,
                f"Invalid value for 'log-blocked-traffic'='{value}'. Must be one of: {', '.join(VALID_BODY_LOG_BLOCKED_TRAFFIC)}",
            )
    if "auth-portal" in payload:
        value = payload["auth-portal"]
        if value not in VALID_BODY_AUTH_PORTAL:
            return (
                False,
                f"Invalid value for 'auth-portal'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_PORTAL)}",
            )
    if "display-bookmark" in payload:
        value = payload["display-bookmark"]
        if value not in VALID_BODY_DISPLAY_BOOKMARK:
            return (
                False,
                f"Invalid value for 'display-bookmark'='{value}'. Must be one of: {', '.join(VALID_BODY_DISPLAY_BOOKMARK)}",
            )
    if "focus-bookmark" in payload:
        value = payload["focus-bookmark"]
        if value not in VALID_BODY_FOCUS_BOOKMARK:
            return (
                False,
                f"Invalid value for 'focus-bookmark'='{value}'. Must be one of: {', '.join(VALID_BODY_FOCUS_BOOKMARK)}",
            )
    if "display-status" in payload:
        value = payload["display-status"]
        if value not in VALID_BODY_DISPLAY_STATUS:
            return (
                False,
                f"Invalid value for 'display-status'='{value}'. Must be one of: {', '.join(VALID_BODY_DISPLAY_STATUS)}",
            )
    if "display-history" in payload:
        value = payload["display-history"]
        if value not in VALID_BODY_DISPLAY_HISTORY:
            return (
                False,
                f"Invalid value for 'display-history'='{value}'. Must be one of: {', '.join(VALID_BODY_DISPLAY_HISTORY)}",
            )
    if "policy-auth-sso" in payload:
        value = payload["policy-auth-sso"]
        if value not in VALID_BODY_POLICY_AUTH_SSO:
            return (
                False,
                f"Invalid value for 'policy-auth-sso'='{value}'. Must be one of: {', '.join(VALID_BODY_POLICY_AUTH_SSO)}",
            )
    if "theme" in payload:
        value = payload["theme"]
        if value not in VALID_BODY_THEME:
            return (
                False,
                f"Invalid value for 'theme'='{value}'. Must be one of: {', '.join(VALID_BODY_THEME)}",
            )
    if "clipboard" in payload:
        value = payload["clipboard"]
        if value not in VALID_BODY_CLIPBOARD:
            return (
                False,
                f"Invalid value for 'clipboard'='{value}'. Must be one of: {', '.join(VALID_BODY_CLIPBOARD)}",
            )
    if "forticlient-download" in payload:
        value = payload["forticlient-download"]
        if value not in VALID_BODY_FORTICLIENT_DOWNLOAD:
            return (
                False,
                f"Invalid value for 'forticlient-download'='{value}'. Must be one of: {', '.join(VALID_BODY_FORTICLIENT_DOWNLOAD)}",
            )
    if "customize-forticlient-download-url" in payload:
        value = payload["customize-forticlient-download-url"]
        if value not in VALID_BODY_CUSTOMIZE_FORTICLIENT_DOWNLOAD_URL:
            return (
                False,
                f"Invalid value for 'customize-forticlient-download-url'='{value}'. Must be one of: {', '.join(VALID_BODY_CUSTOMIZE_FORTICLIENT_DOWNLOAD_URL)}",
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
    "endpoint": "ztna/web_portal",
    "category": "cmdb",
    "api_path": "ztna/web-portal",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure ztna web-portal.",
    "total_fields": 24,
    "required_fields_count": 0,
    "fields_with_defaults_count": 22,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
