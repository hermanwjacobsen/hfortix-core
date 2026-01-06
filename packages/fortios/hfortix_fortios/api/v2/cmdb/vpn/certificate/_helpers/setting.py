"""Validation helpers for vpn/certificate/setting - Auto-generated"""

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
    "interface",  # Specify outgoing interface to reach server.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "ocsp-status": "disable",
    "ocsp-option": "server",
    "proxy": "",
    "proxy-port": 8080,
    "proxy-username": "",
    "source-ip": "",
    "ocsp-default-server": "",
    "interface-select-method": "auto",
    "interface": "",
    "vrf-select": 0,
    "check-ca-cert": "enable",
    "check-ca-chain": "disable",
    "subject-match": "substring",
    "subject-set": "subset",
    "cn-match": "substring",
    "cn-allow-multi": "enable",
    "strict-ocsp-check": "disable",
    "ssl-min-proto-version": "default",
    "cmp-save-extra-certs": "disable",
    "cmp-key-usage-checking": "enable",
    "cert-expire-warning": 14,
    "certname-rsa1024": "Fortinet_SSL_RSA1024",
    "certname-rsa2048": "Fortinet_SSL_RSA2048",
    "certname-rsa4096": "Fortinet_SSL_RSA4096",
    "certname-dsa1024": "Fortinet_SSL_DSA1024",
    "certname-dsa2048": "Fortinet_SSL_DSA2048",
    "certname-ecdsa256": "Fortinet_SSL_ECDSA256",
    "certname-ecdsa384": "Fortinet_SSL_ECDSA384",
    "certname-ecdsa521": "Fortinet_SSL_ECDSA521",
    "certname-ed25519": "Fortinet_SSL_ED25519",
    "certname-ed448": "Fortinet_SSL_ED448",
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
    "ocsp-status": "option",  # Enable/disable receiving certificates using the OCSP.
    "ocsp-option": "option",  # Specify whether the OCSP URL is from certificate or configur
    "proxy": "string",  # Proxy server FQDN or IP for OCSP/CA queries during certifica
    "proxy-port": "integer",  # Proxy server port (1 - 65535, default = 8080).
    "proxy-username": "string",  # Proxy server user name.
    "proxy-password": "password",  # Proxy server password.
    "source-ip": "string",  # Source IP address for dynamic AIA and OCSP queries.
    "ocsp-default-server": "string",  # Default OCSP server.
    "interface-select-method": "option",  # Specify how to select outgoing interface to reach server.
    "interface": "string",  # Specify outgoing interface to reach server.
    "vrf-select": "integer",  # VRF ID used for connection to server.
    "check-ca-cert": "option",  # Enable/disable verification of the user certificate and pass
    "check-ca-chain": "option",  # Enable/disable verification of the entire certificate chain 
    "subject-match": "option",  # When searching for a matching certificate, control how to do
    "subject-set": "option",  # When searching for a matching certificate, control how to do
    "cn-match": "option",  # When searching for a matching certificate, control how to do
    "cn-allow-multi": "option",  # When searching for a matching certificate, allow multiple CN
    "crl-verification": "string",  # CRL verification options.
    "strict-ocsp-check": "option",  # Enable/disable strict mode OCSP checking.
    "ssl-min-proto-version": "option",  # Minimum supported protocol version for SSL/TLS connections (
    "cmp-save-extra-certs": "option",  # Enable/disable saving extra certificates in CMP mode (defaul
    "cmp-key-usage-checking": "option",  # Enable/disable server certificate key usage checking in CMP 
    "cert-expire-warning": "integer",  # Number of days before a certificate expires to send a warnin
    "certname-rsa1024": "string",  # 1024 bit RSA key certificate for re-signing server certifica
    "certname-rsa2048": "string",  # 2048 bit RSA key certificate for re-signing server certifica
    "certname-rsa4096": "string",  # 4096 bit RSA key certificate for re-signing server certifica
    "certname-dsa1024": "string",  # 1024 bit DSA key certificate for re-signing server certifica
    "certname-dsa2048": "string",  # 2048 bit DSA key certificate for re-signing server certifica
    "certname-ecdsa256": "string",  # 256 bit ECDSA key certificate for re-signing server certific
    "certname-ecdsa384": "string",  # 384 bit ECDSA key certificate for re-signing server certific
    "certname-ecdsa521": "string",  # 521 bit ECDSA key certificate for re-signing server certific
    "certname-ed25519": "string",  # 253 bit EdDSA key certificate for re-signing server certific
    "certname-ed448": "string",  # 456 bit EdDSA key certificate for re-signing server certific
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "ocsp-status": "Enable/disable receiving certificates using the OCSP.",
    "ocsp-option": "Specify whether the OCSP URL is from certificate or configured OCSP server.",
    "proxy": "Proxy server FQDN or IP for OCSP/CA queries during certificate verification.",
    "proxy-port": "Proxy server port (1 - 65535, default = 8080).",
    "proxy-username": "Proxy server user name.",
    "proxy-password": "Proxy server password.",
    "source-ip": "Source IP address for dynamic AIA and OCSP queries.",
    "ocsp-default-server": "Default OCSP server.",
    "interface-select-method": "Specify how to select outgoing interface to reach server.",
    "interface": "Specify outgoing interface to reach server.",
    "vrf-select": "VRF ID used for connection to server.",
    "check-ca-cert": "Enable/disable verification of the user certificate and pass authentication if any CA in the chain is trusted (default = enable).",
    "check-ca-chain": "Enable/disable verification of the entire certificate chain and pass authentication only if the chain is complete and all of the CAs in the chain are trusted (default = disable).",
    "subject-match": "When searching for a matching certificate, control how to do RDN value matching with certificate subject name (default = substring).",
    "subject-set": "When searching for a matching certificate, control how to do RDN set matching with certificate subject name (default = subset).",
    "cn-match": "When searching for a matching certificate, control how to do CN value matching with certificate subject name (default = substring).",
    "cn-allow-multi": "When searching for a matching certificate, allow multiple CN fields in certificate subject name (default = enable).",
    "crl-verification": "CRL verification options.",
    "strict-ocsp-check": "Enable/disable strict mode OCSP checking.",
    "ssl-min-proto-version": "Minimum supported protocol version for SSL/TLS connections (default is to follow system global setting).",
    "cmp-save-extra-certs": "Enable/disable saving extra certificates in CMP mode (default = disable).",
    "cmp-key-usage-checking": "Enable/disable server certificate key usage checking in CMP mode (default = enable).",
    "cert-expire-warning": "Number of days before a certificate expires to send a warning. Set to 0 to disable sending of the warning (0 - 100, default = 14).",
    "certname-rsa1024": "1024 bit RSA key certificate for re-signing server certificates for SSL inspection.",
    "certname-rsa2048": "2048 bit RSA key certificate for re-signing server certificates for SSL inspection.",
    "certname-rsa4096": "4096 bit RSA key certificate for re-signing server certificates for SSL inspection.",
    "certname-dsa1024": "1024 bit DSA key certificate for re-signing server certificates for SSL inspection.",
    "certname-dsa2048": "2048 bit DSA key certificate for re-signing server certificates for SSL inspection.",
    "certname-ecdsa256": "256 bit ECDSA key certificate for re-signing server certificates for SSL inspection.",
    "certname-ecdsa384": "384 bit ECDSA key certificate for re-signing server certificates for SSL inspection.",
    "certname-ecdsa521": "521 bit ECDSA key certificate for re-signing server certificates for SSL inspection.",
    "certname-ed25519": "253 bit EdDSA key certificate for re-signing server certificates for SSL inspection.",
    "certname-ed448": "456 bit EdDSA key certificate for re-signing server certificates for SSL inspection.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "proxy": {"type": "string", "max_length": 127},
    "proxy-port": {"type": "integer", "min": 1, "max": 65535},
    "proxy-username": {"type": "string", "max_length": 63},
    "source-ip": {"type": "string", "max_length": 63},
    "ocsp-default-server": {"type": "string", "max_length": 35},
    "interface": {"type": "string", "max_length": 15},
    "vrf-select": {"type": "integer", "min": 0, "max": 511},
    "cert-expire-warning": {"type": "integer", "min": 0, "max": 100},
    "certname-rsa1024": {"type": "string", "max_length": 35},
    "certname-rsa2048": {"type": "string", "max_length": 35},
    "certname-rsa4096": {"type": "string", "max_length": 35},
    "certname-dsa1024": {"type": "string", "max_length": 35},
    "certname-dsa2048": {"type": "string", "max_length": 35},
    "certname-ecdsa256": {"type": "string", "max_length": 35},
    "certname-ecdsa384": {"type": "string", "max_length": 35},
    "certname-ecdsa521": {"type": "string", "max_length": 35},
    "certname-ed25519": {"type": "string", "max_length": 35},
    "certname-ed448": {"type": "string", "max_length": 35},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "crl-verification": {
        "expiry": {
            "type": "option",
            "help": "CRL verification option when CRL is expired (default = ignore).",
            "default": "ignore",
            "options": [{"help": "Certificate status will be verified even if CRL is expired.", "label": "Ignore", "name": "ignore"}, {"help": "Certificate will be revoked if CRL is expired.", "label": "Revoke", "name": "revoke"}],
        },
        "leaf-crl-absence": {
            "type": "option",
            "help": "CRL verification option when leaf CRL is absent (default = ignore).",
            "default": "ignore",
            "options": [{"help": "CRL verification against leaf certificate is ignored if CRL is absent.", "label": "Ignore", "name": "ignore"}, {"help": "Certificate will be revoked if CRL of leaf certificate is absent.", "label": "Revoke", "name": "revoke"}],
        },
        "chain-crl-absence": {
            "type": "option",
            "help": "CRL verification option when CRL of any certificate in chain is absent (default = ignore).",
            "default": "ignore",
            "options": [{"help": "CRL verification is ignored if CRL of any certificate in chain is absent.", "label": "Ignore", "name": "ignore"}, {"help": "Certificate will be revoked if CRL of any certificate in chain is absent.", "label": "Revoke", "name": "revoke"}],
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_OCSP_STATUS = [
    "enable",  # OCSP is performed if CRL is not checked.
    "mandatory",  # If cert is not revoked by CRL, OCSP is performed.
    "disable",  # OCSP is not performed.
]
VALID_BODY_OCSP_OPTION = [
    "certificate",  # Use URL from certificate.
    "server",  # Use URL from configured OCSP server.
]
VALID_BODY_INTERFACE_SELECT_METHOD = [
    "auto",  # Set outgoing interface automatically.
    "sdwan",  # Set outgoing interface by SD-WAN or policy routing rules.
    "specify",  # Set outgoing interface manually.
]
VALID_BODY_CHECK_CA_CERT = [
    "enable",  # Enable verification of the user certificate.
    "disable",  # Disable verification of the user certificate.
]
VALID_BODY_CHECK_CA_CHAIN = [
    "enable",  # Enable verification of the entire certificate chain.
    "disable",  # Disable verification of the entire certificate chain.
]
VALID_BODY_SUBJECT_MATCH = [
    "substring",  # Find a match if the name being searched for is a part or the same as a certificate subject RDN.
    "value",  # Find a match if the name being searched for is same as a certificate subject RDN.
]
VALID_BODY_SUBJECT_SET = [
    "subset",  # Find a match if the name being searched for is a subset of a certificate subject.
    "superset",  # Find a match if the name being searched for is a superset of a certificate subject.
]
VALID_BODY_CN_MATCH = [
    "substring",  # Find a match if the name being searched for is a part or the same as a certificate CN.
    "value",  # Find a match if the name being searched for is same as a certificate CN.
]
VALID_BODY_CN_ALLOW_MULTI = [
    "disable",  # Does not allow multiple CN entries in certificate matching.
    "enable",  # Allow multiple CN entries in certificate matching.
]
VALID_BODY_STRICT_OCSP_CHECK = [
    "enable",  # Enable strict mode OCSP checking.
    "disable",  # Disable strict mode OCSP checking.
]
VALID_BODY_SSL_MIN_PROTO_VERSION = [
    "default",  # Follow system global setting.
    "SSLv3",  # SSLv3.
    "TLSv1",  # TLSv1.
    "TLSv1-1",  # TLSv1.1.
    "TLSv1-2",  # TLSv1.2.
    "TLSv1-3",  # TLSv1.3.
]
VALID_BODY_CMP_SAVE_EXTRA_CERTS = [
    "enable",  # Enable saving extra certificates in CMP mode.
    "disable",  # Disable saving extra certificates in CMP mode.
]
VALID_BODY_CMP_KEY_USAGE_CHECKING = [
    "enable",  # Enable server certificate key usage checking in CMP mode.
    "disable",  # Disable server certificate key usage checking in CMP mode.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_vpn_certificate_setting_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for vpn/certificate/setting."""
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
    """Validate required fields for vpn/certificate/setting."""
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


def validate_vpn_certificate_setting_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new vpn/certificate/setting object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "ocsp-status" in payload:
        value = payload["ocsp-status"]
        if value not in VALID_BODY_OCSP_STATUS:
            desc = FIELD_DESCRIPTIONS.get("ocsp-status", "")
            error_msg = f"Invalid value for 'ocsp-status': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OCSP_STATUS)}"
            error_msg += f"\n  → Example: ocsp-status='{{ VALID_BODY_OCSP_STATUS[0] }}'"
            return (False, error_msg)
    if "ocsp-option" in payload:
        value = payload["ocsp-option"]
        if value not in VALID_BODY_OCSP_OPTION:
            desc = FIELD_DESCRIPTIONS.get("ocsp-option", "")
            error_msg = f"Invalid value for 'ocsp-option': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OCSP_OPTION)}"
            error_msg += f"\n  → Example: ocsp-option='{{ VALID_BODY_OCSP_OPTION[0] }}'"
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
    if "check-ca-cert" in payload:
        value = payload["check-ca-cert"]
        if value not in VALID_BODY_CHECK_CA_CERT:
            desc = FIELD_DESCRIPTIONS.get("check-ca-cert", "")
            error_msg = f"Invalid value for 'check-ca-cert': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CHECK_CA_CERT)}"
            error_msg += f"\n  → Example: check-ca-cert='{{ VALID_BODY_CHECK_CA_CERT[0] }}'"
            return (False, error_msg)
    if "check-ca-chain" in payload:
        value = payload["check-ca-chain"]
        if value not in VALID_BODY_CHECK_CA_CHAIN:
            desc = FIELD_DESCRIPTIONS.get("check-ca-chain", "")
            error_msg = f"Invalid value for 'check-ca-chain': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CHECK_CA_CHAIN)}"
            error_msg += f"\n  → Example: check-ca-chain='{{ VALID_BODY_CHECK_CA_CHAIN[0] }}'"
            return (False, error_msg)
    if "subject-match" in payload:
        value = payload["subject-match"]
        if value not in VALID_BODY_SUBJECT_MATCH:
            desc = FIELD_DESCRIPTIONS.get("subject-match", "")
            error_msg = f"Invalid value for 'subject-match': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SUBJECT_MATCH)}"
            error_msg += f"\n  → Example: subject-match='{{ VALID_BODY_SUBJECT_MATCH[0] }}'"
            return (False, error_msg)
    if "subject-set" in payload:
        value = payload["subject-set"]
        if value not in VALID_BODY_SUBJECT_SET:
            desc = FIELD_DESCRIPTIONS.get("subject-set", "")
            error_msg = f"Invalid value for 'subject-set': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SUBJECT_SET)}"
            error_msg += f"\n  → Example: subject-set='{{ VALID_BODY_SUBJECT_SET[0] }}'"
            return (False, error_msg)
    if "cn-match" in payload:
        value = payload["cn-match"]
        if value not in VALID_BODY_CN_MATCH:
            desc = FIELD_DESCRIPTIONS.get("cn-match", "")
            error_msg = f"Invalid value for 'cn-match': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CN_MATCH)}"
            error_msg += f"\n  → Example: cn-match='{{ VALID_BODY_CN_MATCH[0] }}'"
            return (False, error_msg)
    if "cn-allow-multi" in payload:
        value = payload["cn-allow-multi"]
        if value not in VALID_BODY_CN_ALLOW_MULTI:
            desc = FIELD_DESCRIPTIONS.get("cn-allow-multi", "")
            error_msg = f"Invalid value for 'cn-allow-multi': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CN_ALLOW_MULTI)}"
            error_msg += f"\n  → Example: cn-allow-multi='{{ VALID_BODY_CN_ALLOW_MULTI[0] }}'"
            return (False, error_msg)
    if "strict-ocsp-check" in payload:
        value = payload["strict-ocsp-check"]
        if value not in VALID_BODY_STRICT_OCSP_CHECK:
            desc = FIELD_DESCRIPTIONS.get("strict-ocsp-check", "")
            error_msg = f"Invalid value for 'strict-ocsp-check': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_STRICT_OCSP_CHECK)}"
            error_msg += f"\n  → Example: strict-ocsp-check='{{ VALID_BODY_STRICT_OCSP_CHECK[0] }}'"
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
    if "cmp-save-extra-certs" in payload:
        value = payload["cmp-save-extra-certs"]
        if value not in VALID_BODY_CMP_SAVE_EXTRA_CERTS:
            desc = FIELD_DESCRIPTIONS.get("cmp-save-extra-certs", "")
            error_msg = f"Invalid value for 'cmp-save-extra-certs': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CMP_SAVE_EXTRA_CERTS)}"
            error_msg += f"\n  → Example: cmp-save-extra-certs='{{ VALID_BODY_CMP_SAVE_EXTRA_CERTS[0] }}'"
            return (False, error_msg)
    if "cmp-key-usage-checking" in payload:
        value = payload["cmp-key-usage-checking"]
        if value not in VALID_BODY_CMP_KEY_USAGE_CHECKING:
            desc = FIELD_DESCRIPTIONS.get("cmp-key-usage-checking", "")
            error_msg = f"Invalid value for 'cmp-key-usage-checking': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CMP_KEY_USAGE_CHECKING)}"
            error_msg += f"\n  → Example: cmp-key-usage-checking='{{ VALID_BODY_CMP_KEY_USAGE_CHECKING[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_vpn_certificate_setting_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update vpn/certificate/setting."""
    # Step 1: Validate enum values
    if "ocsp-status" in payload:
        value = payload["ocsp-status"]
        if value not in VALID_BODY_OCSP_STATUS:
            return (
                False,
                f"Invalid value for 'ocsp-status'='{value}'. Must be one of: {', '.join(VALID_BODY_OCSP_STATUS)}",
            )
    if "ocsp-option" in payload:
        value = payload["ocsp-option"]
        if value not in VALID_BODY_OCSP_OPTION:
            return (
                False,
                f"Invalid value for 'ocsp-option'='{value}'. Must be one of: {', '.join(VALID_BODY_OCSP_OPTION)}",
            )
    if "interface-select-method" in payload:
        value = payload["interface-select-method"]
        if value not in VALID_BODY_INTERFACE_SELECT_METHOD:
            return (
                False,
                f"Invalid value for 'interface-select-method'='{value}'. Must be one of: {', '.join(VALID_BODY_INTERFACE_SELECT_METHOD)}",
            )
    if "check-ca-cert" in payload:
        value = payload["check-ca-cert"]
        if value not in VALID_BODY_CHECK_CA_CERT:
            return (
                False,
                f"Invalid value for 'check-ca-cert'='{value}'. Must be one of: {', '.join(VALID_BODY_CHECK_CA_CERT)}",
            )
    if "check-ca-chain" in payload:
        value = payload["check-ca-chain"]
        if value not in VALID_BODY_CHECK_CA_CHAIN:
            return (
                False,
                f"Invalid value for 'check-ca-chain'='{value}'. Must be one of: {', '.join(VALID_BODY_CHECK_CA_CHAIN)}",
            )
    if "subject-match" in payload:
        value = payload["subject-match"]
        if value not in VALID_BODY_SUBJECT_MATCH:
            return (
                False,
                f"Invalid value for 'subject-match'='{value}'. Must be one of: {', '.join(VALID_BODY_SUBJECT_MATCH)}",
            )
    if "subject-set" in payload:
        value = payload["subject-set"]
        if value not in VALID_BODY_SUBJECT_SET:
            return (
                False,
                f"Invalid value for 'subject-set'='{value}'. Must be one of: {', '.join(VALID_BODY_SUBJECT_SET)}",
            )
    if "cn-match" in payload:
        value = payload["cn-match"]
        if value not in VALID_BODY_CN_MATCH:
            return (
                False,
                f"Invalid value for 'cn-match'='{value}'. Must be one of: {', '.join(VALID_BODY_CN_MATCH)}",
            )
    if "cn-allow-multi" in payload:
        value = payload["cn-allow-multi"]
        if value not in VALID_BODY_CN_ALLOW_MULTI:
            return (
                False,
                f"Invalid value for 'cn-allow-multi'='{value}'. Must be one of: {', '.join(VALID_BODY_CN_ALLOW_MULTI)}",
            )
    if "strict-ocsp-check" in payload:
        value = payload["strict-ocsp-check"]
        if value not in VALID_BODY_STRICT_OCSP_CHECK:
            return (
                False,
                f"Invalid value for 'strict-ocsp-check'='{value}'. Must be one of: {', '.join(VALID_BODY_STRICT_OCSP_CHECK)}",
            )
    if "ssl-min-proto-version" in payload:
        value = payload["ssl-min-proto-version"]
        if value not in VALID_BODY_SSL_MIN_PROTO_VERSION:
            return (
                False,
                f"Invalid value for 'ssl-min-proto-version'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL_MIN_PROTO_VERSION)}",
            )
    if "cmp-save-extra-certs" in payload:
        value = payload["cmp-save-extra-certs"]
        if value not in VALID_BODY_CMP_SAVE_EXTRA_CERTS:
            return (
                False,
                f"Invalid value for 'cmp-save-extra-certs'='{value}'. Must be one of: {', '.join(VALID_BODY_CMP_SAVE_EXTRA_CERTS)}",
            )
    if "cmp-key-usage-checking" in payload:
        value = payload["cmp-key-usage-checking"]
        if value not in VALID_BODY_CMP_KEY_USAGE_CHECKING:
            return (
                False,
                f"Invalid value for 'cmp-key-usage-checking'='{value}'. Must be one of: {', '.join(VALID_BODY_CMP_KEY_USAGE_CHECKING)}",
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
    "endpoint": "vpn/certificate/setting",
    "category": "cmdb",
    "api_path": "vpn.certificate/setting",
    "help": "VPN certificate setting.",
    "total_fields": 33,
    "required_fields_count": 1,
    "fields_with_defaults_count": 31,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
