"""Validation helpers for system/sdn_connector - Auto-generated"""

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
    "par-id": "",
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
    "par-id": "string",  # Public address range ID.
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
    "par-id": "Public address range ID.",
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
    "par-id": {"type": "string", "max_length": 63},
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
    "disable",  # Disable connection to this SDN Connector.
    "enable",  # Enable connection to this SDN Connector.
]
VALID_BODY_TYPE = [
    "aci",  # Application Centric Infrastructure (ACI).
    "alicloud",  # AliCloud Service (ACS).
    "aws",  # Amazon Web Services (AWS).
    "azure",  # Microsoft Azure.
    "gcp",  # Google Cloud Platform (GCP).
    "nsx",  # VMware NSX.
    "nuage",  # Nuage VSP.
    "oci",  # Oracle Cloud Infrastructure.
    "openstack",  # OpenStack.
    "kubernetes",  # Kubernetes.
    "vmware",  # VMware vSphere (vCenter & ESXi).
    "sepm",  # Symantec Endpoint Protection Manager.
    "aci-direct",  # Application Centric Infrastructure (ACI Direct Connection).
    "ibm",  # IBM Cloud Infrastructure.
    "nutanix",  # Nutanix Prism Central.
    "sap",  # SAP Control.
]
VALID_BODY_USE_METADATA_IAM = [
    "disable",  # Disable using IAM role to call API.
    "enable",  # Enable using IAM role to call API.
]
VALID_BODY_MICROSOFT_365 = [
    "disable",  # Azure SDN connector
    "enable",  # Microsoft 365 SDN connector
]
VALID_BODY_HA_STATUS = [
    "disable",  # Disable use for FortiGate HA service.
    "enable",  # Enable use for FortiGate HA service.
]
VALID_BODY_VERIFY_CERTIFICATE = [
    "disable",  # Disable server certificate verification.
    "enable",  # Enable server certificate verification.
]
VALID_BODY_ALT_RESOURCE_IP = [
    "disable",  # Disable AWS alternative resource IP.
    "enable",  # Enable AWS alternative resource IP.
]
VALID_BODY_AZURE_REGION = [
    "global",  # Global Azure Server.
    "china",  # China Azure Server.
    "germany",  # Germany Azure Server.
    "usgov",  # US Government Azure Server.
    "local",  # Azure Stack Local Server.
]
VALID_BODY_OCI_REGION_TYPE = [
    "commercial",  # Commercial region.
    "government",  # Government region.
]
VALID_BODY_IBM_REGION = [
    "dallas",  # US South (Dallas) Public Endpoint.
    "washington-dc",  # US East (Washington DC) Public Endpoint.
    "london",  # United Kingdom (London) Public Endpoint.
    "frankfurt",  # Germany (Frankfurt) Public Endpoint.
    "sydney",  # Australia (Sydney) Public Endpoint.
    "tokyo",  # Japan (Tokyo) Public Endpoint.
    "osaka",  # Japan (Osaka) Public Endpoint.
    "toronto",  # Canada (Toronto) Public Endpoint.
    "sao-paulo",  # Brazil (Sao Paulo) Public Endpoint.
    "madrid",  # Spain (Madrid) Public Endpoint.
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
    """Validate GET request parameters for system/sdn_connector."""
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
    """Validate required fields for system/sdn_connector."""
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
    """Validate POST request to create new system/sdn_connector object."""
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
    """Validate PUT request to update system/sdn_connector."""
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
    "endpoint": "system/sdn_connector",
    "category": "cmdb",
    "api_path": "system/sdn-connector",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure connection to SDN Connector.",
    "total_fields": 55,
    "required_fields_count": 11,
    "fields_with_defaults_count": 40,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
