"""
Validation helpers for system/sdn_connector endpoint.

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
    "server",  # Server address of the remote SDN connector.
    "server-list",  # Server address list of the remote SDN connector.
    "username",  # Username of the remote SDN connector as login credentials.
    "password",  # Password of the remote SDN connector as login credentials.
    "access-key",  # AWS / ACS access key ID.
    "secret-key",  # AWS / ACS secret access key.
    "region",  # AWS / ACS region name.
    "service-account",  # GCP service account email.
    "private-key",  # Private key of GCP service account.
    "secret-token",  # Secret token of Kubernetes service account.
    "api-key",  # IBM cloud API key or service ID API key.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "status": "enable",
    "type": "aws",
    "proxy": "",
    "use-metadata-iam": "disable",
    "microsoft-365": "disable",
    "ha-status": "disable",
    "verify-certificate": "enable",
    "vdom": "",
    "server": "",
    "server-port": 0,
    "message-server-port": 0,
    "username": "",
    "vcenter-server": "",
    "vcenter-username": "",
    "access-key": "",
    "region": "",
    "vpc-id": "",
    "alt-resource-ip": "disable",
    "tenant-id": "",
    "client-id": "",
    "subscription-id": "",
    "resource-group": "",
    "login-endpoint": "",
    "resource-url": "",
    "azure-region": "global",
    "user-id": "",
    "oci-region-type": "commercial",
    "oci-cert": "",
    "oci-fingerprint": "",
    "service-account": "",
    "private-key": "",
    "secret-token": "",
    "domain": "",
    "group-name": "",
    "server-cert": "",
    "server-ca-cert": "",
    "ibm-region": "dallas",
    "update-interval": 60,
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
    "name": "string",  # SDN connector name.
    "status": "option",  # Enable/disable connection to the remote SDN connector.
    "type": "option",  # Type of SDN connector.
    "proxy": "string",  # SDN proxy.
    "use-metadata-iam": "option",  # Enable/disable use of IAM role from metadata to call API.
    "microsoft-365": "option",  # Enable to use as Microsoft 365 connector.
    "ha-status": "option",  # Enable/disable use for FortiGate HA service.
    "verify-certificate": "option",  # Enable/disable server certificate verification.
    "vdom": "string",  # Virtual domain name of the remote SDN connector.
    "server": "string",  # Server address of the remote SDN connector.
    "server-list": "string",  # Server address list of the remote SDN connector.
    "server-port": "integer",  # Port number of the remote SDN connector.
    "message-server-port": "integer",  # HTTP port number of the SAP message server.
    "username": "string",  # Username of the remote SDN connector as login credentials.
    "password": "password_aes256",  # Password of the remote SDN connector as login credentials.
    "vcenter-server": "string",  # vCenter server address for NSX quarantine.
    "vcenter-username": "string",  # vCenter server username for NSX quarantine.
    "vcenter-password": "password_aes256",  # vCenter server password for NSX quarantine.
    "access-key": "string",  # AWS / ACS access key ID.
    "secret-key": "password",  # AWS / ACS secret access key.
    "region": "string",  # AWS / ACS region name.
    "vpc-id": "string",  # AWS VPC ID.
    "alt-resource-ip": "option",  # Enable/disable AWS alternative resource IP.
    "external-account-list": "string",  # Configure AWS external account list.
    "tenant-id": "string",  # Tenant ID (directory ID).
    "client-id": "string",  # Azure client ID (application ID).
    "client-secret": "password",  # Azure client secret (application key).
    "subscription-id": "string",  # Azure subscription ID.
    "resource-group": "string",  # Azure resource group.
    "login-endpoint": "string",  # Azure Stack login endpoint.
    "resource-url": "string",  # Azure Stack resource URL.
    "azure-region": "option",  # Azure server region.
    "nic": "string",  # Configure Azure network interface.
    "route-table": "string",  # Configure Azure route table.
    "user-id": "string",  # User ID.
    "compartment-list": "string",  # Configure OCI compartment list.
    "oci-region-list": "string",  # Configure OCI region list.
    "oci-region-type": "option",  # OCI region type.
    "oci-cert": "string",  # OCI certificate.
    "oci-fingerprint": "string",  # OCI pubkey fingerprint.
    "external-ip": "string",  # Configure GCP external IP.
    "route": "string",  # Configure GCP route.
    "gcp-project-list": "string",  # Configure GCP project list.
    "forwarding-rule": "string",  # Configure GCP forwarding rule.
    "service-account": "string",  # GCP service account email.
    "private-key": "user",  # Private key of GCP service account.
    "secret-token": "user",  # Secret token of Kubernetes service account.
    "domain": "string",  # Domain name.
    "group-name": "string",  # Full path group name of computers.
    "server-cert": "string",  # Trust servers that contain this certificate only.
    "server-ca-cert": "string",  # Trust only those servers whose certificate is directly/indir
    "api-key": "password",  # IBM cloud API key or service ID API key.
    "ibm-region": "option",  # IBM cloud region name.
    "update-interval": "integer",  # Dynamic object update interval (30 - 3600 sec, default = 60,
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "SDN connector name.",
    "status": "Enable/disable connection to the remote SDN connector.",
    "type": "Type of SDN connector.",
    "proxy": "SDN proxy.",
    "use-metadata-iam": "Enable/disable use of IAM role from metadata to call API.",
    "microsoft-365": "Enable to use as Microsoft 365 connector.",
    "ha-status": "Enable/disable use for FortiGate HA service.",
    "verify-certificate": "Enable/disable server certificate verification.",
    "vdom": "Virtual domain name of the remote SDN connector.",
    "server": "Server address of the remote SDN connector.",
    "server-list": "Server address list of the remote SDN connector.",
    "server-port": "Port number of the remote SDN connector.",
    "message-server-port": "HTTP port number of the SAP message server.",
    "username": "Username of the remote SDN connector as login credentials.",
    "password": "Password of the remote SDN connector as login credentials.",
    "vcenter-server": "vCenter server address for NSX quarantine.",
    "vcenter-username": "vCenter server username for NSX quarantine.",
    "vcenter-password": "vCenter server password for NSX quarantine.",
    "access-key": "AWS / ACS access key ID.",
    "secret-key": "AWS / ACS secret access key.",
    "region": "AWS / ACS region name.",
    "vpc-id": "AWS VPC ID.",
    "alt-resource-ip": "Enable/disable AWS alternative resource IP.",
    "external-account-list": "Configure AWS external account list.",
    "tenant-id": "Tenant ID (directory ID).",
    "client-id": "Azure client ID (application ID).",
    "client-secret": "Azure client secret (application key).",
    "subscription-id": "Azure subscription ID.",
    "resource-group": "Azure resource group.",
    "login-endpoint": "Azure Stack login endpoint.",
    "resource-url": "Azure Stack resource URL.",
    "azure-region": "Azure server region.",
    "nic": "Configure Azure network interface.",
    "route-table": "Configure Azure route table.",
    "user-id": "User ID.",
    "compartment-list": "Configure OCI compartment list.",
    "oci-region-list": "Configure OCI region list.",
    "oci-region-type": "OCI region type.",
    "oci-cert": "OCI certificate.",
    "oci-fingerprint": "OCI pubkey fingerprint.",
    "external-ip": "Configure GCP external IP.",
    "route": "Configure GCP route.",
    "gcp-project-list": "Configure GCP project list.",
    "forwarding-rule": "Configure GCP forwarding rule.",
    "service-account": "GCP service account email.",
    "private-key": "Private key of GCP service account.",
    "secret-token": "Secret token of Kubernetes service account.",
    "domain": "Domain name.",
    "group-name": "Full path group name of computers.",
    "server-cert": "Trust servers that contain this certificate only.",
    "server-ca-cert": "Trust only those servers whose certificate is directly/indirectly signed by this certificate.",
    "api-key": "IBM cloud API key or service ID API key.",
    "ibm-region": "IBM cloud region name.",
    "update-interval": "Dynamic object update interval (30 - 3600 sec, default = 60, 0 = disabled).",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 35},
    "proxy": {"type": "string", "max_length": 35},
    "vdom": {"type": "string", "max_length": 31},
    "server": {"type": "string", "max_length": 127},
    "server-port": {"type": "integer", "min": 0, "max": 65535},
    "message-server-port": {"type": "integer", "min": 0, "max": 65535},
    "username": {"type": "string", "max_length": 64},
    "vcenter-server": {"type": "string", "max_length": 127},
    "vcenter-username": {"type": "string", "max_length": 64},
    "access-key": {"type": "string", "max_length": 31},
    "region": {"type": "string", "max_length": 31},
    "vpc-id": {"type": "string", "max_length": 31},
    "tenant-id": {"type": "string", "max_length": 127},
    "client-id": {"type": "string", "max_length": 63},
    "subscription-id": {"type": "string", "max_length": 63},
    "resource-group": {"type": "string", "max_length": 63},
    "login-endpoint": {"type": "string", "max_length": 127},
    "resource-url": {"type": "string", "max_length": 127},
    "user-id": {"type": "string", "max_length": 127},
    "oci-cert": {"type": "string", "max_length": 63},
    "oci-fingerprint": {"type": "string", "max_length": 63},
    "service-account": {"type": "string", "max_length": 127},
    "domain": {"type": "string", "max_length": 127},
    "group-name": {"type": "string", "max_length": 127},
    "server-cert": {"type": "string", "max_length": 127},
    "server-ca-cert": {"type": "string", "max_length": 127},
    "update-interval": {"type": "integer", "min": 0, "max": 3600},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "server-list": {
        "ip": {
            "type": "string",
            "help": "IPv4 address.",
            "required": True,
            "default": "",
            "max_length": 15,
        },
    },
    "external-account-list": {
        "role-arn": {
            "type": "string",
            "help": "AWS role ARN to assume.",
            "required": True,
            "default": "",
            "max_length": 2047,
        },
        "external-id": {
            "type": "string",
            "help": "AWS external ID.",
            "default": "",
            "max_length": 1399,
        },
        "region-list": {
            "type": "string",
            "help": "AWS region name list.",
            "required": True,
        },
    },
    "nic": {
        "name": {
            "type": "string",
            "help": "Network interface name.",
            "required": True,
            "default": "",
            "max_length": 63,
        },
        "peer-nic": {
            "type": "string",
            "help": "Peer network interface name.",
            "default": "",
            "max_length": 63,
        },
        "ip": {
            "type": "string",
            "help": "Configure IP configuration.",
        },
    },
    "route-table": {
        "name": {
            "type": "string",
            "help": "Route table name.",
            "required": True,
            "default": "",
            "max_length": 63,
        },
        "subscription-id": {
            "type": "string",
            "help": "Subscription ID of Azure route table.",
            "default": "",
            "max_length": 63,
        },
        "resource-group": {
            "type": "string",
            "help": "Resource group of Azure route table.",
            "default": "",
            "max_length": 63,
        },
        "route": {
            "type": "string",
            "help": "Configure Azure route.",
        },
    },
    "compartment-list": {
        "compartment-id": {
            "type": "string",
            "help": "OCI compartment ID.",
            "required": True,
            "default": "",
            "max_length": 127,
        },
    },
    "oci-region-list": {
        "region": {
            "type": "string",
            "help": "OCI region.",
            "required": True,
            "default": "",
            "max_length": 31,
        },
    },
    "external-ip": {
        "name": {
            "type": "string",
            "help": "External IP name.",
            "required": True,
            "default": "",
            "max_length": 63,
        },
    },
    "route": {
        "name": {
            "type": "string",
            "help": "Route name.",
            "required": True,
            "default": "",
            "max_length": 63,
        },
    },
    "gcp-project-list": {
        "id": {
            "type": "string",
            "help": "GCP project ID.",
            "required": True,
            "default": "",
            "max_length": 127,
        },
        "gcp-zone-list": {
            "type": "string",
            "help": "Configure GCP zone list.",
        },
    },
    "forwarding-rule": {
        "rule-name": {
            "type": "string",
            "help": "Forwarding rule name.",
            "required": True,
            "default": "",
            "max_length": 63,
        },
        "target": {
            "type": "string",
            "help": "Target instance name.",
            "required": True,
            "default": "",
            "max_length": 63,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_STATUS = [
    "disable",
    "enable",
]
VALID_BODY_TYPE = [
    "aci",
    "alicloud",
    "aws",
    "azure",
    "gcp",
    "nsx",
    "nuage",
    "oci",
    "openstack",
    "kubernetes",
    "vmware",
    "sepm",
    "aci-direct",
    "ibm",
    "nutanix",
    "sap",
]
VALID_BODY_USE_METADATA_IAM = [
    "disable",
    "enable",
]
VALID_BODY_MICROSOFT_365 = [
    "disable",
    "enable",
]
VALID_BODY_HA_STATUS = [
    "disable",
    "enable",
]
VALID_BODY_VERIFY_CERTIFICATE = [
    "disable",
    "enable",
]
VALID_BODY_ALT_RESOURCE_IP = [
    "disable",
    "enable",
]
VALID_BODY_AZURE_REGION = [
    "global",
    "china",
    "germany",
    "usgov",
    "local",
]
VALID_BODY_OCI_REGION_TYPE = [
    "commercial",
    "government",
]
VALID_BODY_IBM_REGION = [
    "dallas",
    "washington-dc",
    "london",
    "frankfurt",
    "sydney",
    "tokyo",
    "osaka",
    "toronto",
    "sao-paulo",
    "madrid",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_system_sdn_connector_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for system/sdn_connector.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_system_sdn_connector_get()
        >>> assert is_valid == True
        
        >>> # Valid - Get specific item by name
        >>> is_valid, error = validate_system_sdn_connector_get(name="test-item")
        >>> assert is_valid == True
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_system_sdn_connector_get(
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
    Validate required fields for system/sdn_connector.

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


def validate_system_sdn_connector_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new system/sdn_connector object.

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
        ...     "server": True,  # Server address of the remote SDN connector.
        ...     "server-list": True,  # Server address list of the remote SDN connector.
        ... }
        >>> is_valid, error = validate_system_sdn_connector_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "server": True,
        ...     "status": "disable",  # Valid enum value
        ... }
        >>> is_valid, error = validate_system_sdn_connector_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["status"] = "invalid-value"
        >>> is_valid, error = validate_system_sdn_connector_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_system_sdn_connector_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
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
    if "type" in payload:
        value = payload["type"]
        if value not in VALID_BODY_TYPE:
            desc = FIELD_DESCRIPTIONS.get("type", "")
            error_msg = f"Invalid value for 'type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TYPE)}"
            error_msg += f"\n  → Example: type='{{ VALID_BODY_TYPE[0] }}'"
            return (False, error_msg)
    if "use-metadata-iam" in payload:
        value = payload["use-metadata-iam"]
        if value not in VALID_BODY_USE_METADATA_IAM:
            desc = FIELD_DESCRIPTIONS.get("use-metadata-iam", "")
            error_msg = f"Invalid value for 'use-metadata-iam': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_USE_METADATA_IAM)}"
            error_msg += f"\n  → Example: use-metadata-iam='{{ VALID_BODY_USE_METADATA_IAM[0] }}'"
            return (False, error_msg)
    if "microsoft-365" in payload:
        value = payload["microsoft-365"]
        if value not in VALID_BODY_MICROSOFT_365:
            desc = FIELD_DESCRIPTIONS.get("microsoft-365", "")
            error_msg = f"Invalid value for 'microsoft-365': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MICROSOFT_365)}"
            error_msg += f"\n  → Example: microsoft-365='{{ VALID_BODY_MICROSOFT_365[0] }}'"
            return (False, error_msg)
    if "ha-status" in payload:
        value = payload["ha-status"]
        if value not in VALID_BODY_HA_STATUS:
            desc = FIELD_DESCRIPTIONS.get("ha-status", "")
            error_msg = f"Invalid value for 'ha-status': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_HA_STATUS)}"
            error_msg += f"\n  → Example: ha-status='{{ VALID_BODY_HA_STATUS[0] }}'"
            return (False, error_msg)
    if "verify-certificate" in payload:
        value = payload["verify-certificate"]
        if value not in VALID_BODY_VERIFY_CERTIFICATE:
            desc = FIELD_DESCRIPTIONS.get("verify-certificate", "")
            error_msg = f"Invalid value for 'verify-certificate': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_VERIFY_CERTIFICATE)}"
            error_msg += f"\n  → Example: verify-certificate='{{ VALID_BODY_VERIFY_CERTIFICATE[0] }}'"
            return (False, error_msg)
    if "alt-resource-ip" in payload:
        value = payload["alt-resource-ip"]
        if value not in VALID_BODY_ALT_RESOURCE_IP:
            desc = FIELD_DESCRIPTIONS.get("alt-resource-ip", "")
            error_msg = f"Invalid value for 'alt-resource-ip': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ALT_RESOURCE_IP)}"
            error_msg += f"\n  → Example: alt-resource-ip='{{ VALID_BODY_ALT_RESOURCE_IP[0] }}'"
            return (False, error_msg)
    if "azure-region" in payload:
        value = payload["azure-region"]
        if value not in VALID_BODY_AZURE_REGION:
            desc = FIELD_DESCRIPTIONS.get("azure-region", "")
            error_msg = f"Invalid value for 'azure-region': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AZURE_REGION)}"
            error_msg += f"\n  → Example: azure-region='{{ VALID_BODY_AZURE_REGION[0] }}'"
            return (False, error_msg)
    if "oci-region-type" in payload:
        value = payload["oci-region-type"]
        if value not in VALID_BODY_OCI_REGION_TYPE:
            desc = FIELD_DESCRIPTIONS.get("oci-region-type", "")
            error_msg = f"Invalid value for 'oci-region-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OCI_REGION_TYPE)}"
            error_msg += f"\n  → Example: oci-region-type='{{ VALID_BODY_OCI_REGION_TYPE[0] }}'"
            return (False, error_msg)
    if "ibm-region" in payload:
        value = payload["ibm-region"]
        if value not in VALID_BODY_IBM_REGION:
            desc = FIELD_DESCRIPTIONS.get("ibm-region", "")
            error_msg = f"Invalid value for 'ibm-region': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IBM_REGION)}"
            error_msg += f"\n  → Example: ibm-region='{{ VALID_BODY_IBM_REGION[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_system_sdn_connector_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update system/sdn_connector.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_system_sdn_connector_put(payload)
    """
    # Step 1: Validate enum values
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid value for 'status'='{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )
    if "type" in payload:
        value = payload["type"]
        if value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid value for 'type'='{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )
    if "use-metadata-iam" in payload:
        value = payload["use-metadata-iam"]
        if value not in VALID_BODY_USE_METADATA_IAM:
            return (
                False,
                f"Invalid value for 'use-metadata-iam'='{value}'. Must be one of: {', '.join(VALID_BODY_USE_METADATA_IAM)}",
            )
    if "microsoft-365" in payload:
        value = payload["microsoft-365"]
        if value not in VALID_BODY_MICROSOFT_365:
            return (
                False,
                f"Invalid value for 'microsoft-365'='{value}'. Must be one of: {', '.join(VALID_BODY_MICROSOFT_365)}",
            )
    if "ha-status" in payload:
        value = payload["ha-status"]
        if value not in VALID_BODY_HA_STATUS:
            return (
                False,
                f"Invalid value for 'ha-status'='{value}'. Must be one of: {', '.join(VALID_BODY_HA_STATUS)}",
            )
    if "verify-certificate" in payload:
        value = payload["verify-certificate"]
        if value not in VALID_BODY_VERIFY_CERTIFICATE:
            return (
                False,
                f"Invalid value for 'verify-certificate'='{value}'. Must be one of: {', '.join(VALID_BODY_VERIFY_CERTIFICATE)}",
            )
    if "alt-resource-ip" in payload:
        value = payload["alt-resource-ip"]
        if value not in VALID_BODY_ALT_RESOURCE_IP:
            return (
                False,
                f"Invalid value for 'alt-resource-ip'='{value}'. Must be one of: {', '.join(VALID_BODY_ALT_RESOURCE_IP)}",
            )
    if "azure-region" in payload:
        value = payload["azure-region"]
        if value not in VALID_BODY_AZURE_REGION:
            return (
                False,
                f"Invalid value for 'azure-region'='{value}'. Must be one of: {', '.join(VALID_BODY_AZURE_REGION)}",
            )
    if "oci-region-type" in payload:
        value = payload["oci-region-type"]
        if value not in VALID_BODY_OCI_REGION_TYPE:
            return (
                False,
                f"Invalid value for 'oci-region-type'='{value}'. Must be one of: {', '.join(VALID_BODY_OCI_REGION_TYPE)}",
            )
    if "ibm-region" in payload:
        value = payload["ibm-region"]
        if value not in VALID_BODY_IBM_REGION:
            return (
                False,
                f"Invalid value for 'ibm-region'='{value}'. Must be one of: {', '.join(VALID_BODY_IBM_REGION)}",
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
    "endpoint": "system/sdn_connector",
    "category": "cmdb",
    "api_path": "system/sdn-connector",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure connection to SDN Connector.",
    "total_fields": 54,
    "required_fields_count": 11,
    "fields_with_defaults_count": 39,
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
