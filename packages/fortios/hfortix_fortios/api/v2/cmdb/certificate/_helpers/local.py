"""Validation helpers for certificate/local - Auto-generated"""

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
    "global",  # Global range.
    "vdom",  # VDOM IP address range.
]
VALID_BODY_SOURCE = [
    "factory",  # Factory installed certificate.
    "user",  # User generated certificate.
    "bundle",  # Bundle file certificate.
]
VALID_BODY_NAME_ENCODING = [
    "printable",  # Printable encoding (default).
    "utf8",  # UTF-8 encoding.
]
VALID_BODY_IKE_LOCALID_TYPE = [
    "asn1dn",  # ASN.1 distinguished name.
    "fqdn",  # Fully qualified domain name.
]
VALID_BODY_ENROLL_PROTOCOL = [
    "none",  # None (default).
    "scep",  # Simple Certificate Enrollment Protocol.
    "cmpv2",  # Certificate Management Protocol Version 2.
    "acme2",  # Automated Certificate Management Environment Version 2.
    "est",  # Enrollment over Secure Transport.
]
VALID_BODY_PRIVATE_KEY_RETAIN = [
    "enable",  # Keep the existing private key during SCEP renewal.
    "disable",  # Generate a new private key during SCEP renewal.
]
VALID_BODY_CMP_REGENERATION_METHOD = [
    "keyupate",  # Key Update.
    "renewal",  # Renewal.
]
VALID_BODY_EST_REGENERATION_METHOD = [
    "create-new-key",  # Create new private key during re-enrollment.
    "use-existing-key",  # Reuse existing private key during re-enrollment.
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
    """Validate GET request parameters for certificate/local."""
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
    """Validate required fields for certificate/local."""
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
    """Validate POST request to create new certificate/local object."""
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
    """Validate PUT request to update certificate/local."""
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
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
