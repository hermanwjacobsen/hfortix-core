"""
Validation helpers for certificate/local endpoint.

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
    "name",  # Name.
    "private-key",  # PEM format key encrypted with a password.
    "acme-domain",  # A valid domain that resolves to this FortiGate unit.
    "acme-email",  # Contact email address that is required by some CAs like LetsEncrypt.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "comments": "",
    "private-key": "",
    "certificate": "",
    "csr": "",
    "state": "",
    "scep-url": "",
    "range": "global",
    "source": "user",
    "auto-regenerate-days": 0,
    "auto-regenerate-days-warning": 0,
    "ca-identifier": "",
    "name-encoding": "printable",
    "source-ip": "0.0.0.0",
    "ike-localid": "",
    "ike-localid-type": "asn1dn",
    "enroll-protocol": "none",
    "private-key-retain": "disable",
    "cmp-server": "",
    "cmp-path": "",
    "cmp-server-cert": "",
    "cmp-regeneration-method": "keyupate",
    "acme-ca-url": "https://acme-v02.api.letsencrypt.org/directory",
    "acme-domain": "",
    "acme-email": "",
    "acme-rsa-key-size": 2048,
    "acme-renew-window": 30,
    "est-server": "",
    "est-ca-id": "",
    "est-http-username": "",
    "est-client-cert": "",
    "est-server-cert": "",
    "est-srp-username": "",
    "est-regeneration-method": "create-new-key",
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
    "password": "password",  # Password as a PEM file.
    "comments": "string",  # Comment.
    "private-key": "user",  # PEM format key encrypted with a password.
    "certificate": "user",  # PEM format certificate.
    "csr": "user",  # Certificate Signing Request.
    "state": "user",  # Certificate Signing Request State.
    "scep-url": "string",  # SCEP server URL.
    "range": "option",  # Either a global or VDOM IP address range for the certificate
    "source": "option",  # Certificate source type.
    "auto-regenerate-days": "integer",  # Number of days to wait before expiry of an updated local cer
    "auto-regenerate-days-warning": "integer",  # Number of days to wait before an expiry warning message is g
    "scep-password": "password",  # SCEP server challenge password for auto-regeneration.
    "ca-identifier": "string",  # CA identifier of the CA server for signing via SCEP.
    "name-encoding": "option",  # Name encoding method for auto-regeneration.
    "source-ip": "ipv4-address",  # Source IP address for communications to the SCEP server.
    "ike-localid": "string",  # Local ID the FortiGate uses for authentication as a VPN clie
    "ike-localid-type": "option",  # IKE local ID type.
    "enroll-protocol": "option",  # Certificate enrollment protocol.
    "private-key-retain": "option",  # Enable/disable retention of private key during SCEP renewal 
    "cmp-server": "string",  # Address and port for CMP server (format = address:port).
    "cmp-path": "string",  # Path location inside CMP server.
    "cmp-server-cert": "string",  # CMP server certificate.
    "cmp-regeneration-method": "option",  # CMP auto-regeneration method.
    "acme-ca-url": "string",  # The URL for the ACME CA server (Let's Encrypt is the default
    "acme-domain": "string",  # A valid domain that resolves to this FortiGate unit.
    "acme-email": "string",  # Contact email address that is required by some CAs like Lets
    "acme-eab-key-id": "var-string",  # External Account Binding Key ID (optional setting).
    "acme-eab-key-hmac": "password",  # External Account Binding HMAC Key (URL-encoded base64).
    "acme-rsa-key-size": "integer",  # Length of the RSA private key of the generated cert (Minimum
    "acme-renew-window": "integer",  # Beginning of the renewal window (in days before certificate 
    "est-server": "string",  # Address and port for EST server (e.g. https://example.com:12
    "est-ca-id": "string",  # CA identifier of the CA server for signing via EST.
    "est-http-username": "string",  # HTTP Authentication username for signing via EST.
    "est-http-password": "password",  # HTTP Authentication password for signing via EST.
    "est-client-cert": "string",  # Certificate used to authenticate this FortiGate to EST serve
    "est-server-cert": "string",  # EST server's certificate must be verifiable by this certific
    "est-srp-username": "string",  # EST SRP authentication username.
    "est-srp-password": "password",  # EST SRP authentication password.
    "est-regeneration-method": "option",  # EST behavioral options during re-enrollment.
    "details": "key",  # Print local certificate detailed information.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Name.",
    "password": "Password as a PEM file.",
    "comments": "Comment.",
    "private-key": "PEM format key encrypted with a password.",
    "certificate": "PEM format certificate.",
    "csr": "Certificate Signing Request.",
    "state": "Certificate Signing Request State.",
    "scep-url": "SCEP server URL.",
    "range": "Either a global or VDOM IP address range for the certificate.",
    "source": "Certificate source type.",
    "auto-regenerate-days": "Number of days to wait before expiry of an updated local certificate is requested (0 = disabled).",
    "auto-regenerate-days-warning": "Number of days to wait before an expiry warning message is generated (0 = disabled).",
    "scep-password": "SCEP server challenge password for auto-regeneration.",
    "ca-identifier": "CA identifier of the CA server for signing via SCEP.",
    "name-encoding": "Name encoding method for auto-regeneration.",
    "source-ip": "Source IP address for communications to the SCEP server.",
    "ike-localid": "Local ID the FortiGate uses for authentication as a VPN client.",
    "ike-localid-type": "IKE local ID type.",
    "enroll-protocol": "Certificate enrollment protocol.",
    "private-key-retain": "Enable/disable retention of private key during SCEP renewal (default = disable).",
    "cmp-server": "Address and port for CMP server (format = address:port).",
    "cmp-path": "Path location inside CMP server.",
    "cmp-server-cert": "CMP server certificate.",
    "cmp-regeneration-method": "CMP auto-regeneration method.",
    "acme-ca-url": "The URL for the ACME CA server (Let's Encrypt is the default provider).",
    "acme-domain": "A valid domain that resolves to this FortiGate unit.",
    "acme-email": "Contact email address that is required by some CAs like LetsEncrypt.",
    "acme-eab-key-id": "External Account Binding Key ID (optional setting).",
    "acme-eab-key-hmac": "External Account Binding HMAC Key (URL-encoded base64).",
    "acme-rsa-key-size": "Length of the RSA private key of the generated cert (Minimum 2048 bits).",
    "acme-renew-window": "Beginning of the renewal window (in days before certificate expiration, 30 by default).",
    "est-server": "Address and port for EST server (e.g. https://example.com:1234).",
    "est-ca-id": "CA identifier of the CA server for signing via EST.",
    "est-http-username": "HTTP Authentication username for signing via EST.",
    "est-http-password": "HTTP Authentication password for signing via EST.",
    "est-client-cert": "Certificate used to authenticate this FortiGate to EST server.",
    "est-server-cert": "EST server's certificate must be verifiable by this certificate to be authenticated.",
    "est-srp-username": "EST SRP authentication username.",
    "est-srp-password": "EST SRP authentication password.",
    "est-regeneration-method": "EST behavioral options during re-enrollment.",
    "details": "Print local certificate detailed information.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 35},
    "comments": {"type": "string", "max_length": 511},
    "scep-url": {"type": "string", "max_length": 255},
    "auto-regenerate-days": {"type": "integer", "min": 0, "max": 4294967295},
    "auto-regenerate-days-warning": {"type": "integer", "min": 0, "max": 4294967295},
    "ca-identifier": {"type": "string", "max_length": 255},
    "ike-localid": {"type": "string", "max_length": 63},
    "cmp-server": {"type": "string", "max_length": 63},
    "cmp-path": {"type": "string", "max_length": 255},
    "cmp-server-cert": {"type": "string", "max_length": 79},
    "acme-ca-url": {"type": "string", "max_length": 255},
    "acme-domain": {"type": "string", "max_length": 255},
    "acme-email": {"type": "string", "max_length": 255},
    "acme-rsa-key-size": {"type": "integer", "min": 2048, "max": 4096},
    "acme-renew-window": {"type": "integer", "min": 1, "max": 60},
    "est-server": {"type": "string", "max_length": 255},
    "est-ca-id": {"type": "string", "max_length": 255},
    "est-http-username": {"type": "string", "max_length": 63},
    "est-client-cert": {"type": "string", "max_length": 79},
    "est-server-cert": {"type": "string", "max_length": 79},
    "est-srp-username": {"type": "string", "max_length": 63},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "details": {
        "<certficate name>": {
            "type": "value",
            "help": "Local certificate name.",
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_RANGE = [
    "global",
    "vdom",
]
VALID_BODY_SOURCE = [
    "factory",
    "user",
    "bundle",
]
VALID_BODY_NAME_ENCODING = [
    "printable",
    "utf8",
]
VALID_BODY_IKE_LOCALID_TYPE = [
    "asn1dn",
    "fqdn",
]
VALID_BODY_ENROLL_PROTOCOL = [
    "none",
    "scep",
    "cmpv2",
    "acme2",
    "est",
]
VALID_BODY_PRIVATE_KEY_RETAIN = [
    "enable",
    "disable",
]
VALID_BODY_CMP_REGENERATION_METHOD = [
    "keyupate",
    "renewal",
]
VALID_BODY_EST_REGENERATION_METHOD = [
    "create-new-key",
    "use-existing-key",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_certificate_local_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for certificate/local.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_certificate_local_get()
        >>> assert is_valid == True
        
        >>> # Valid - Get specific item by name
        >>> is_valid, error = validate_certificate_local_get(name="test-item")
        >>> assert is_valid == True
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_certificate_local_get(
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
    Validate required fields for certificate/local.

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


def validate_certificate_local_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new certificate/local object.

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
        ...     "name": True,  # Name.
        ...     "private-key": True,  # PEM format key encrypted with a password.
        ... }
        >>> is_valid, error = validate_certificate_local_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "name": True,
        ...     "range": "global",  # Valid enum value
        ... }
        >>> is_valid, error = validate_certificate_local_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["range"] = "invalid-value"
        >>> is_valid, error = validate_certificate_local_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_certificate_local_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "range" in payload:
        value = payload["range"]
        if value not in VALID_BODY_RANGE:
            desc = FIELD_DESCRIPTIONS.get("range", "")
            error_msg = f"Invalid value for 'range': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_RANGE)}"
            error_msg += f"\n  → Example: range='{{ VALID_BODY_RANGE[0] }}'"
            return (False, error_msg)
    if "source" in payload:
        value = payload["source"]
        if value not in VALID_BODY_SOURCE:
            desc = FIELD_DESCRIPTIONS.get("source", "")
            error_msg = f"Invalid value for 'source': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SOURCE)}"
            error_msg += f"\n  → Example: source='{{ VALID_BODY_SOURCE[0] }}'"
            return (False, error_msg)
    if "name-encoding" in payload:
        value = payload["name-encoding"]
        if value not in VALID_BODY_NAME_ENCODING:
            desc = FIELD_DESCRIPTIONS.get("name-encoding", "")
            error_msg = f"Invalid value for 'name-encoding': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_NAME_ENCODING)}"
            error_msg += f"\n  → Example: name-encoding='{{ VALID_BODY_NAME_ENCODING[0] }}'"
            return (False, error_msg)
    if "ike-localid-type" in payload:
        value = payload["ike-localid-type"]
        if value not in VALID_BODY_IKE_LOCALID_TYPE:
            desc = FIELD_DESCRIPTIONS.get("ike-localid-type", "")
            error_msg = f"Invalid value for 'ike-localid-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IKE_LOCALID_TYPE)}"
            error_msg += f"\n  → Example: ike-localid-type='{{ VALID_BODY_IKE_LOCALID_TYPE[0] }}'"
            return (False, error_msg)
    if "enroll-protocol" in payload:
        value = payload["enroll-protocol"]
        if value not in VALID_BODY_ENROLL_PROTOCOL:
            desc = FIELD_DESCRIPTIONS.get("enroll-protocol", "")
            error_msg = f"Invalid value for 'enroll-protocol': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ENROLL_PROTOCOL)}"
            error_msg += f"\n  → Example: enroll-protocol='{{ VALID_BODY_ENROLL_PROTOCOL[0] }}'"
            return (False, error_msg)
    if "private-key-retain" in payload:
        value = payload["private-key-retain"]
        if value not in VALID_BODY_PRIVATE_KEY_RETAIN:
            desc = FIELD_DESCRIPTIONS.get("private-key-retain", "")
            error_msg = f"Invalid value for 'private-key-retain': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PRIVATE_KEY_RETAIN)}"
            error_msg += f"\n  → Example: private-key-retain='{{ VALID_BODY_PRIVATE_KEY_RETAIN[0] }}'"
            return (False, error_msg)
    if "cmp-regeneration-method" in payload:
        value = payload["cmp-regeneration-method"]
        if value not in VALID_BODY_CMP_REGENERATION_METHOD:
            desc = FIELD_DESCRIPTIONS.get("cmp-regeneration-method", "")
            error_msg = f"Invalid value for 'cmp-regeneration-method': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CMP_REGENERATION_METHOD)}"
            error_msg += f"\n  → Example: cmp-regeneration-method='{{ VALID_BODY_CMP_REGENERATION_METHOD[0] }}'"
            return (False, error_msg)
    if "est-regeneration-method" in payload:
        value = payload["est-regeneration-method"]
        if value not in VALID_BODY_EST_REGENERATION_METHOD:
            desc = FIELD_DESCRIPTIONS.get("est-regeneration-method", "")
            error_msg = f"Invalid value for 'est-regeneration-method': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EST_REGENERATION_METHOD)}"
            error_msg += f"\n  → Example: est-regeneration-method='{{ VALID_BODY_EST_REGENERATION_METHOD[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_certificate_local_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update certificate/local.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_certificate_local_put(payload)
    """
    # Step 1: Validate enum values
    if "range" in payload:
        value = payload["range"]
        if value not in VALID_BODY_RANGE:
            return (
                False,
                f"Invalid value for 'range'='{value}'. Must be one of: {', '.join(VALID_BODY_RANGE)}",
            )
    if "source" in payload:
        value = payload["source"]
        if value not in VALID_BODY_SOURCE:
            return (
                False,
                f"Invalid value for 'source'='{value}'. Must be one of: {', '.join(VALID_BODY_SOURCE)}",
            )
    if "name-encoding" in payload:
        value = payload["name-encoding"]
        if value not in VALID_BODY_NAME_ENCODING:
            return (
                False,
                f"Invalid value for 'name-encoding'='{value}'. Must be one of: {', '.join(VALID_BODY_NAME_ENCODING)}",
            )
    if "ike-localid-type" in payload:
        value = payload["ike-localid-type"]
        if value not in VALID_BODY_IKE_LOCALID_TYPE:
            return (
                False,
                f"Invalid value for 'ike-localid-type'='{value}'. Must be one of: {', '.join(VALID_BODY_IKE_LOCALID_TYPE)}",
            )
    if "enroll-protocol" in payload:
        value = payload["enroll-protocol"]
        if value not in VALID_BODY_ENROLL_PROTOCOL:
            return (
                False,
                f"Invalid value for 'enroll-protocol'='{value}'. Must be one of: {', '.join(VALID_BODY_ENROLL_PROTOCOL)}",
            )
    if "private-key-retain" in payload:
        value = payload["private-key-retain"]
        if value not in VALID_BODY_PRIVATE_KEY_RETAIN:
            return (
                False,
                f"Invalid value for 'private-key-retain'='{value}'. Must be one of: {', '.join(VALID_BODY_PRIVATE_KEY_RETAIN)}",
            )
    if "cmp-regeneration-method" in payload:
        value = payload["cmp-regeneration-method"]
        if value not in VALID_BODY_CMP_REGENERATION_METHOD:
            return (
                False,
                f"Invalid value for 'cmp-regeneration-method'='{value}'. Must be one of: {', '.join(VALID_BODY_CMP_REGENERATION_METHOD)}",
            )
    if "est-regeneration-method" in payload:
        value = payload["est-regeneration-method"]
        if value not in VALID_BODY_EST_REGENERATION_METHOD:
            return (
                False,
                f"Invalid value for 'est-regeneration-method'='{value}'. Must be one of: {', '.join(VALID_BODY_EST_REGENERATION_METHOD)}",
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
    "endpoint": "certificate/local",
    "category": "cmdb",
    "api_path": "certificate/local",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Local keys and certificates.",
    "total_fields": 41,
    "required_fields_count": 4,
    "fields_with_defaults_count": 34,
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
