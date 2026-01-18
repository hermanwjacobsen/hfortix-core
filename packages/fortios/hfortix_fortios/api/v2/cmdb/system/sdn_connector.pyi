""" - Type Stubs

Auto-generated stub file for type checking and IDE support.

Endpoint: system/sdn_connector
Category: cmdb
"""

from __future__ import annotations

from typing import (
    Any,
    ClassVar,
    Literal,
    TypedDict,
    overload,
)

from hfortix_fortios.models import (
    FortiObject,
    FortiObjectList,
)


# ================================================================
# TypedDict Payloads
# ================================================================

class SdnConnectorServerlistItem(TypedDict, total=False):
    """Nested item for server-list field."""
    ip: str


class SdnConnectorExternalaccountlistItem(TypedDict, total=False):
    """Nested item for external-account-list field."""
    role_arn: str
    external_id: str
    region_list: str | list[str]


class SdnConnectorNicItem(TypedDict, total=False):
    """Nested item for nic field."""
    name: str
    peer_nic: str
    ip: str | list[str]


class SdnConnectorRoutetableItem(TypedDict, total=False):
    """Nested item for route-table field."""
    name: str
    subscription_id: str
    resource_group: str
    route: str | list[str]


class SdnConnectorCompartmentlistItem(TypedDict, total=False):
    """Nested item for compartment-list field."""
    compartment_id: str


class SdnConnectorOciregionlistItem(TypedDict, total=False):
    """Nested item for oci-region-list field."""
    region: str


class SdnConnectorExternalipItem(TypedDict, total=False):
    """Nested item for external-ip field."""
    name: str


class SdnConnectorRouteItem(TypedDict, total=False):
    """Nested item for route field."""
    name: str


class SdnConnectorGcpprojectlistItem(TypedDict, total=False):
    """Nested item for gcp-project-list field."""
    id: str
    gcp_zone_list: str | list[str]


class SdnConnectorForwardingruleItem(TypedDict, total=False):
    """Nested item for forwarding-rule field."""
    rule_name: str
    target: str


class SdnConnectorPayload(TypedDict, total=False):
    """Payload type for SdnConnector operations."""
    name: str
    status: Literal["disable", "enable"]
    type: Literal["aci", "alicloud", "aws", "azure", "gcp", "nsx", "nuage", "oci", "openstack", "kubernetes", "vmware", "sepm", "aci-direct", "ibm", "nutanix", "sap"]
    proxy: str
    use_metadata_iam: Literal["disable", "enable"]
    microsoft_365: Literal["disable", "enable"]
    ha_status: Literal["disable", "enable"]
    verify_certificate: Literal["disable", "enable"]
    vdom: str
    server: str
    server_list: str | list[str] | list[SdnConnectorServerlistItem]
    server_port: int
    message_server_port: int
    username: str
    password: str
    vcenter_server: str
    vcenter_username: str
    vcenter_password: str
    access_key: str
    secret_key: str
    region: str
    vpc_id: str
    alt_resource_ip: Literal["disable", "enable"]
    external_account_list: str | list[str] | list[SdnConnectorExternalaccountlistItem]
    tenant_id: str
    client_id: str
    client_secret: str
    subscription_id: str
    resource_group: str
    login_endpoint: str
    resource_url: str
    azure_region: Literal["global", "china", "germany", "usgov", "local"]
    nic: str | list[str] | list[SdnConnectorNicItem]
    route_table: str | list[str] | list[SdnConnectorRoutetableItem]
    user_id: str
    compartment_list: str | list[str] | list[SdnConnectorCompartmentlistItem]
    oci_region_list: str | list[str] | list[SdnConnectorOciregionlistItem]
    oci_region_type: Literal["commercial", "government"]
    oci_cert: str
    oci_fingerprint: str
    external_ip: str | list[str] | list[SdnConnectorExternalipItem]
    route: str | list[str] | list[SdnConnectorRouteItem]
    gcp_project_list: str | list[str] | list[SdnConnectorGcpprojectlistItem]
    forwarding_rule: str | list[str] | list[SdnConnectorForwardingruleItem]
    service_account: str
    private_key: str
    secret_token: str
    domain: str
    group_name: str
    server_cert: str
    server_ca_cert: str
    api_key: str
    ibm_region: Literal["dallas", "washington-dc", "london", "frankfurt", "sydney", "tokyo", "osaka", "toronto", "sao-paulo", "madrid"]
    par_id: str
    update_interval: int


# ================================================================
# Response Types (TypedDict for dict-style access)
# ================================================================

class SdnConnectorResponse(TypedDict, total=False):
    """Response type for SdnConnector - use with .dict property for typed dict access."""
    name: str
    status: Literal["disable", "enable"]
    type: Literal["aci", "alicloud", "aws", "azure", "gcp", "nsx", "nuage", "oci", "openstack", "kubernetes", "vmware", "sepm", "aci-direct", "ibm", "nutanix", "sap"]
    proxy: str
    use_metadata_iam: Literal["disable", "enable"]
    microsoft_365: Literal["disable", "enable"]
    ha_status: Literal["disable", "enable"]
    verify_certificate: Literal["disable", "enable"]
    vdom: str
    server: str
    server_list: list[SdnConnectorServerlistItem]
    server_port: int
    message_server_port: int
    username: str
    password: str
    vcenter_server: str
    vcenter_username: str
    vcenter_password: str
    access_key: str
    secret_key: str
    region: str
    vpc_id: str
    alt_resource_ip: Literal["disable", "enable"]
    external_account_list: list[SdnConnectorExternalaccountlistItem]
    tenant_id: str
    client_id: str
    client_secret: str
    subscription_id: str
    resource_group: str
    login_endpoint: str
    resource_url: str
    azure_region: Literal["global", "china", "germany", "usgov", "local"]
    nic: list[SdnConnectorNicItem]
    route_table: list[SdnConnectorRoutetableItem]
    user_id: str
    compartment_list: list[SdnConnectorCompartmentlistItem]
    oci_region_list: list[SdnConnectorOciregionlistItem]
    oci_region_type: Literal["commercial", "government"]
    oci_cert: str
    oci_fingerprint: str
    external_ip: list[SdnConnectorExternalipItem]
    route: list[SdnConnectorRouteItem]
    gcp_project_list: list[SdnConnectorGcpprojectlistItem]
    forwarding_rule: list[SdnConnectorForwardingruleItem]
    service_account: str
    private_key: str
    secret_token: str
    domain: str
    group_name: str
    server_cert: str
    server_ca_cert: str
    api_key: str
    ibm_region: Literal["dallas", "washington-dc", "london", "frankfurt", "sydney", "tokyo", "osaka", "toronto", "sao-paulo", "madrid"]
    par_id: str
    update_interval: int


# ================================================================
# Response Types (Class for attribute access)
# ================================================================


class SdnConnectorObject(FortiObject):
    """Typed FortiObject for SdnConnector with field access."""
    name: str
    status: Literal["disable", "enable"]
    type: Literal["aci", "alicloud", "aws", "azure", "gcp", "nsx", "nuage", "oci", "openstack", "kubernetes", "vmware", "sepm", "aci-direct", "ibm", "nutanix", "sap"]
    proxy: str
    use_metadata_iam: Literal["disable", "enable"]
    microsoft_365: Literal["disable", "enable"]
    ha_status: Literal["disable", "enable"]
    verify_certificate: Literal["disable", "enable"]
    server: str
    server_list: list[SdnConnectorServerlistItem]
    server_port: int
    message_server_port: int
    username: str
    password: str
    vcenter_server: str
    vcenter_username: str
    vcenter_password: str
    access_key: str
    secret_key: str
    region: str
    vpc_id: str
    alt_resource_ip: Literal["disable", "enable"]
    external_account_list: list[SdnConnectorExternalaccountlistItem]
    tenant_id: str
    client_id: str
    client_secret: str
    subscription_id: str
    resource_group: str
    login_endpoint: str
    resource_url: str
    azure_region: Literal["global", "china", "germany", "usgov", "local"]
    nic: list[SdnConnectorNicItem]
    route_table: list[SdnConnectorRoutetableItem]
    user_id: str
    compartment_list: list[SdnConnectorCompartmentlistItem]
    oci_region_list: list[SdnConnectorOciregionlistItem]
    oci_region_type: Literal["commercial", "government"]
    oci_cert: str
    oci_fingerprint: str
    external_ip: list[SdnConnectorExternalipItem]
    route: list[SdnConnectorRouteItem]
    gcp_project_list: list[SdnConnectorGcpprojectlistItem]
    forwarding_rule: list[SdnConnectorForwardingruleItem]
    service_account: str
    private_key: str
    secret_token: str
    domain: str
    group_name: str
    server_cert: str
    server_ca_cert: str
    api_key: str
    ibm_region: Literal["dallas", "washington-dc", "london", "frankfurt", "sydney", "tokyo", "osaka", "toronto", "sao-paulo", "madrid"]
    par_id: str
    update_interval: int


# ================================================================
# Main Endpoint Class
# ================================================================

class SdnConnector:
    """
    
    Endpoint: system/sdn_connector
    Category: cmdb
    MKey: name
    """
    
    # Class attributes for introspection
    endpoint: ClassVar[str] = ...
    path: ClassVar[str] = ...
    category: ClassVar[str] = ...
    mkey: ClassVar[str] = ...
    capabilities: ClassVar[dict[str, Any]] = ...
    
    def __init__(self, client: Any) -> None:
        """Initialize endpoint with HTTP client."""
        ...
    
    # ================================================================
    # GET Methods
    # ================================================================
    
    # CMDB with mkey - overloads for single vs list returns
    @overload
    def get(
        self,
        name: str,
        *,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> SdnConnectorObject: ...
    
    @overload
    def get(
        self,
        *,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> FortiObjectList[SdnConnectorObject]: ...
    
    def get_schema(
        self,
        format: str = ...,
    ) -> FortiObject: ...

    # ================================================================
    # POST Method
    # ================================================================
    
    def post(
        self,
        payload_dict: SdnConnectorPayload | None = ...,
        name: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        type: Literal["aci", "alicloud", "aws", "azure", "gcp", "nsx", "nuage", "oci", "openstack", "kubernetes", "vmware", "sepm", "aci-direct", "ibm", "nutanix", "sap"] | None = ...,
        proxy: str | None = ...,
        use_metadata_iam: Literal["disable", "enable"] | None = ...,
        microsoft_365: Literal["disable", "enable"] | None = ...,
        ha_status: Literal["disable", "enable"] | None = ...,
        verify_certificate: Literal["disable", "enable"] | None = ...,
        server: str | None = ...,
        server_list: str | list[str] | list[SdnConnectorServerlistItem] | None = ...,
        server_port: int | None = ...,
        message_server_port: int | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        vcenter_server: str | None = ...,
        vcenter_username: str | None = ...,
        vcenter_password: str | None = ...,
        access_key: str | None = ...,
        secret_key: str | None = ...,
        region: str | None = ...,
        vpc_id: str | None = ...,
        alt_resource_ip: Literal["disable", "enable"] | None = ...,
        external_account_list: str | list[str] | list[SdnConnectorExternalaccountlistItem] | None = ...,
        tenant_id: str | None = ...,
        client_id: str | None = ...,
        client_secret: str | None = ...,
        subscription_id: str | None = ...,
        resource_group: str | None = ...,
        login_endpoint: str | None = ...,
        resource_url: str | None = ...,
        azure_region: Literal["global", "china", "germany", "usgov", "local"] | None = ...,
        nic: str | list[str] | list[SdnConnectorNicItem] | None = ...,
        route_table: str | list[str] | list[SdnConnectorRoutetableItem] | None = ...,
        user_id: str | None = ...,
        compartment_list: str | list[str] | list[SdnConnectorCompartmentlistItem] | None = ...,
        oci_region_list: str | list[str] | list[SdnConnectorOciregionlistItem] | None = ...,
        oci_region_type: Literal["commercial", "government"] | None = ...,
        oci_cert: str | None = ...,
        oci_fingerprint: str | None = ...,
        external_ip: str | list[str] | list[SdnConnectorExternalipItem] | None = ...,
        route: str | list[str] | list[SdnConnectorRouteItem] | None = ...,
        gcp_project_list: str | list[str] | list[SdnConnectorGcpprojectlistItem] | None = ...,
        forwarding_rule: str | list[str] | list[SdnConnectorForwardingruleItem] | None = ...,
        service_account: str | None = ...,
        private_key: str | None = ...,
        secret_token: str | None = ...,
        domain: str | None = ...,
        group_name: str | None = ...,
        server_cert: str | None = ...,
        server_ca_cert: str | None = ...,
        api_key: str | None = ...,
        ibm_region: Literal["dallas", "washington-dc", "london", "frankfurt", "sydney", "tokyo", "osaka", "toronto", "sao-paulo", "madrid"] | None = ...,
        par_id: str | None = ...,
        update_interval: int | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> SdnConnectorObject: ...

    # ================================================================
    # PUT Method
    # ================================================================
    
    def put(
        self,
        payload_dict: SdnConnectorPayload | None = ...,
        name: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        type: Literal["aci", "alicloud", "aws", "azure", "gcp", "nsx", "nuage", "oci", "openstack", "kubernetes", "vmware", "sepm", "aci-direct", "ibm", "nutanix", "sap"] | None = ...,
        proxy: str | None = ...,
        use_metadata_iam: Literal["disable", "enable"] | None = ...,
        microsoft_365: Literal["disable", "enable"] | None = ...,
        ha_status: Literal["disable", "enable"] | None = ...,
        verify_certificate: Literal["disable", "enable"] | None = ...,
        server: str | None = ...,
        server_list: str | list[str] | list[SdnConnectorServerlistItem] | None = ...,
        server_port: int | None = ...,
        message_server_port: int | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        vcenter_server: str | None = ...,
        vcenter_username: str | None = ...,
        vcenter_password: str | None = ...,
        access_key: str | None = ...,
        secret_key: str | None = ...,
        region: str | None = ...,
        vpc_id: str | None = ...,
        alt_resource_ip: Literal["disable", "enable"] | None = ...,
        external_account_list: str | list[str] | list[SdnConnectorExternalaccountlistItem] | None = ...,
        tenant_id: str | None = ...,
        client_id: str | None = ...,
        client_secret: str | None = ...,
        subscription_id: str | None = ...,
        resource_group: str | None = ...,
        login_endpoint: str | None = ...,
        resource_url: str | None = ...,
        azure_region: Literal["global", "china", "germany", "usgov", "local"] | None = ...,
        nic: str | list[str] | list[SdnConnectorNicItem] | None = ...,
        route_table: str | list[str] | list[SdnConnectorRoutetableItem] | None = ...,
        user_id: str | None = ...,
        compartment_list: str | list[str] | list[SdnConnectorCompartmentlistItem] | None = ...,
        oci_region_list: str | list[str] | list[SdnConnectorOciregionlistItem] | None = ...,
        oci_region_type: Literal["commercial", "government"] | None = ...,
        oci_cert: str | None = ...,
        oci_fingerprint: str | None = ...,
        external_ip: str | list[str] | list[SdnConnectorExternalipItem] | None = ...,
        route: str | list[str] | list[SdnConnectorRouteItem] | None = ...,
        gcp_project_list: str | list[str] | list[SdnConnectorGcpprojectlistItem] | None = ...,
        forwarding_rule: str | list[str] | list[SdnConnectorForwardingruleItem] | None = ...,
        service_account: str | None = ...,
        private_key: str | None = ...,
        secret_token: str | None = ...,
        domain: str | None = ...,
        group_name: str | None = ...,
        server_cert: str | None = ...,
        server_ca_cert: str | None = ...,
        api_key: str | None = ...,
        ibm_region: Literal["dallas", "washington-dc", "london", "frankfurt", "sydney", "tokyo", "osaka", "toronto", "sao-paulo", "madrid"] | None = ...,
        par_id: str | None = ...,
        update_interval: int | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> SdnConnectorObject: ...

    # ================================================================
    # DELETE Method
    # ================================================================
    
    def delete(
        self,
        name: str | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> FortiObject: ...

    # ================================================================
    # Utility Methods
    # ================================================================
    
    def exists(
        self,
        name: str,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: SdnConnectorPayload | None = ...,
        name: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        type: Literal["aci", "alicloud", "aws", "azure", "gcp", "nsx", "nuage", "oci", "openstack", "kubernetes", "vmware", "sepm", "aci-direct", "ibm", "nutanix", "sap"] | None = ...,
        proxy: str | None = ...,
        use_metadata_iam: Literal["disable", "enable"] | None = ...,
        microsoft_365: Literal["disable", "enable"] | None = ...,
        ha_status: Literal["disable", "enable"] | None = ...,
        verify_certificate: Literal["disable", "enable"] | None = ...,
        server: str | None = ...,
        server_list: str | list[str] | list[SdnConnectorServerlistItem] | None = ...,
        server_port: int | None = ...,
        message_server_port: int | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        vcenter_server: str | None = ...,
        vcenter_username: str | None = ...,
        vcenter_password: str | None = ...,
        access_key: str | None = ...,
        secret_key: str | None = ...,
        region: str | None = ...,
        vpc_id: str | None = ...,
        alt_resource_ip: Literal["disable", "enable"] | None = ...,
        external_account_list: str | list[str] | list[SdnConnectorExternalaccountlistItem] | None = ...,
        tenant_id: str | None = ...,
        client_id: str | None = ...,
        client_secret: str | None = ...,
        subscription_id: str | None = ...,
        resource_group: str | None = ...,
        login_endpoint: str | None = ...,
        resource_url: str | None = ...,
        azure_region: Literal["global", "china", "germany", "usgov", "local"] | None = ...,
        nic: str | list[str] | list[SdnConnectorNicItem] | None = ...,
        route_table: str | list[str] | list[SdnConnectorRoutetableItem] | None = ...,
        user_id: str | None = ...,
        compartment_list: str | list[str] | list[SdnConnectorCompartmentlistItem] | None = ...,
        oci_region_list: str | list[str] | list[SdnConnectorOciregionlistItem] | None = ...,
        oci_region_type: Literal["commercial", "government"] | None = ...,
        oci_cert: str | None = ...,
        oci_fingerprint: str | None = ...,
        external_ip: str | list[str] | list[SdnConnectorExternalipItem] | None = ...,
        route: str | list[str] | list[SdnConnectorRouteItem] | None = ...,
        gcp_project_list: str | list[str] | list[SdnConnectorGcpprojectlistItem] | None = ...,
        forwarding_rule: str | list[str] | list[SdnConnectorForwardingruleItem] | None = ...,
        service_account: str | None = ...,
        private_key: str | None = ...,
        secret_token: str | None = ...,
        domain: str | None = ...,
        group_name: str | None = ...,
        server_cert: str | None = ...,
        server_ca_cert: str | None = ...,
        api_key: str | None = ...,
        ibm_region: Literal["dallas", "washington-dc", "london", "frankfurt", "sydney", "tokyo", "osaka", "toronto", "sao-paulo", "madrid"] | None = ...,
        par_id: str | None = ...,
        update_interval: int | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> FortiObject: ...
    
    # Helper methods
    @staticmethod
    def help(field_name: str | None = ...) -> str: ...
    
    @staticmethod
    def fields(detailed: bool = ...) -> list[str] | list[dict[str, Any]]: ...
    
    @staticmethod
    def field_info(field_name: str) -> FortiObject: ...
    
    @staticmethod
    def validate_field(name: str, value: Any) -> bool: ...
    
    @staticmethod
    def required_fields() -> list[str]: ...
    
    @staticmethod
    def defaults() -> FortiObject: ...
    
    @staticmethod
    def schema() -> FortiObject: ...


__all__ = [
    "SdnConnector",
    "SdnConnectorPayload",
    "SdnConnectorResponse",
    "SdnConnectorObject",
]