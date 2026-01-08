from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class SdnConnectorPayload(TypedDict, total=False):
    """
    Type hints for system/sdn_connector payload fields.
    
    Configure connection to SDN Connector.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.certificate.ca.CaEndpoint` (via: server-ca-cert)
        - :class:`~.certificate.local.LocalEndpoint` (via: oci-cert)
        - :class:`~.certificate.remote.RemoteEndpoint` (via: server-ca-cert, server-cert)
        - :class:`~.system.sdn-proxy.SdnProxyEndpoint` (via: proxy)
        - :class:`~.system.vdom.VdomEndpoint` (via: vdom)

    **Usage:**
        payload: SdnConnectorPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # SDN connector name.
    status: Literal["disable", "enable"]  # Enable/disable connection to the remote SDN connector.
    type: Literal["aci", "alicloud", "aws", "azure", "gcp", "nsx", "nuage", "oci", "openstack", "kubernetes", "vmware", "sepm", "aci-direct", "ibm", "nutanix", "sap"]  # Type of SDN connector.
    proxy: NotRequired[str]  # SDN proxy.
    use_metadata_iam: Literal["disable", "enable"]  # Enable/disable use of IAM role from metadata to call API.
    microsoft_365: Literal["disable", "enable"]  # Enable to use as Microsoft 365 connector.
    ha_status: Literal["disable", "enable"]  # Enable/disable use for FortiGate HA service.
    verify_certificate: Literal["disable", "enable"]  # Enable/disable server certificate verification.
    vdom: NotRequired[str]  # Virtual domain name of the remote SDN connector.
    server: str  # Server address of the remote SDN connector.
    server_list: list[dict[str, Any]]  # Server address list of the remote SDN connector.
    server_port: NotRequired[int]  # Port number of the remote SDN connector.
    message_server_port: NotRequired[int]  # HTTP port number of the SAP message server.
    username: str  # Username of the remote SDN connector as login credentials.
    password: str  # Password of the remote SDN connector as login credentials.
    vcenter_server: NotRequired[str]  # vCenter server address for NSX quarantine.
    vcenter_username: NotRequired[str]  # vCenter server username for NSX quarantine.
    vcenter_password: NotRequired[str]  # vCenter server password for NSX quarantine.
    access_key: str  # AWS / ACS access key ID.
    secret_key: str  # AWS / ACS secret access key.
    region: str  # AWS / ACS region name.
    vpc_id: NotRequired[str]  # AWS VPC ID.
    alt_resource_ip: NotRequired[Literal["disable", "enable"]]  # Enable/disable AWS alternative resource IP.
    external_account_list: NotRequired[list[dict[str, Any]]]  # Configure AWS external account list.
    tenant_id: NotRequired[str]  # Tenant ID (directory ID).
    client_id: NotRequired[str]  # Azure client ID (application ID).
    client_secret: NotRequired[str]  # Azure client secret (application key).
    subscription_id: NotRequired[str]  # Azure subscription ID.
    resource_group: NotRequired[str]  # Azure resource group.
    login_endpoint: NotRequired[str]  # Azure Stack login endpoint.
    resource_url: NotRequired[str]  # Azure Stack resource URL.
    azure_region: NotRequired[Literal["global", "china", "germany", "usgov", "local"]]  # Azure server region.
    nic: NotRequired[list[dict[str, Any]]]  # Configure Azure network interface.
    route_table: NotRequired[list[dict[str, Any]]]  # Configure Azure route table.
    user_id: NotRequired[str]  # User ID.
    compartment_list: NotRequired[list[dict[str, Any]]]  # Configure OCI compartment list.
    oci_region_list: NotRequired[list[dict[str, Any]]]  # Configure OCI region list.
    oci_region_type: Literal["commercial", "government"]  # OCI region type.
    oci_cert: NotRequired[str]  # OCI certificate.
    oci_fingerprint: NotRequired[str]  # OCI pubkey fingerprint.
    external_ip: NotRequired[list[dict[str, Any]]]  # Configure GCP external IP.
    route: NotRequired[list[dict[str, Any]]]  # Configure GCP route.
    gcp_project_list: NotRequired[list[dict[str, Any]]]  # Configure GCP project list.
    forwarding_rule: NotRequired[list[dict[str, Any]]]  # Configure GCP forwarding rule.
    service_account: str  # GCP service account email.
    private_key: str  # Private key of GCP service account.
    secret_token: str  # Secret token of Kubernetes service account.
    domain: NotRequired[str]  # Domain name.
    group_name: NotRequired[str]  # Full path group name of computers.
    server_cert: NotRequired[str]  # Trust servers that contain this certificate only.
    server_ca_cert: NotRequired[str]  # Trust only those servers whose certificate is directly/indir
    api_key: str  # IBM cloud API key or service ID API key.
    ibm_region: Literal["dallas", "washington-dc", "london", "frankfurt", "sydney", "tokyo", "osaka", "toronto", "sao-paulo", "madrid"]  # IBM cloud region name.
    par_id: NotRequired[str]  # Public address range ID.
    update_interval: NotRequired[int]  # Dynamic object update interval

# Nested classes for table field children

@final
class SdnConnectorServerlistObject:
    """Typed object for server-list table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # IPv4 address.
    ip: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class SdnConnectorExternalaccountlistObject:
    """Typed object for external-account-list table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # AWS role ARN to assume.
    role_arn: str
    # AWS external ID.
    external_id: str
    # AWS region name list.
    region_list: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class SdnConnectorNicObject:
    """Typed object for nic table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Network interface name.
    name: str
    # Peer network interface name.
    peer_nic: str
    # Configure IP configuration.
    ip: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class SdnConnectorRoutetableObject:
    """Typed object for route-table table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Route table name.
    name: str
    # Subscription ID of Azure route table.
    subscription_id: str
    # Resource group of Azure route table.
    resource_group: str
    # Configure Azure route.
    route: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class SdnConnectorCompartmentlistObject:
    """Typed object for compartment-list table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # OCI compartment ID.
    compartment_id: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class SdnConnectorOciregionlistObject:
    """Typed object for oci-region-list table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # OCI region.
    region: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class SdnConnectorExternalipObject:
    """Typed object for external-ip table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # External IP name.
    name: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class SdnConnectorRouteObject:
    """Typed object for route table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Route name.
    name: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class SdnConnectorGcpprojectlistObject:
    """Typed object for gcp-project-list table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # GCP project ID.
    id: str
    # Configure GCP zone list.
    gcp_zone_list: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class SdnConnectorForwardingruleObject:
    """Typed object for forwarding-rule table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Forwarding rule name.
    rule_name: str
    # Target instance name.
    target: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class SdnConnectorResponse(TypedDict):
    """
    Type hints for system/sdn_connector API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
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
    server_list: list[dict[str, Any]]
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
    external_account_list: list[dict[str, Any]]
    tenant_id: str
    client_id: str
    client_secret: str
    subscription_id: str
    resource_group: str
    login_endpoint: str
    resource_url: str
    azure_region: Literal["global", "china", "germany", "usgov", "local"]
    nic: list[dict[str, Any]]
    route_table: list[dict[str, Any]]
    user_id: str
    compartment_list: list[dict[str, Any]]
    oci_region_list: list[dict[str, Any]]
    oci_region_type: Literal["commercial", "government"]
    oci_cert: str
    oci_fingerprint: str
    external_ip: list[dict[str, Any]]
    route: list[dict[str, Any]]
    gcp_project_list: list[dict[str, Any]]
    forwarding_rule: list[dict[str, Any]]
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


@final
class SdnConnectorObject:
    """Typed FortiObject for system/sdn_connector with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # SDN connector name.
    name: str
    # Enable/disable connection to the remote SDN connector.
    status: Literal["disable", "enable"]
    # Type of SDN connector.
    type: Literal["aci", "alicloud", "aws", "azure", "gcp", "nsx", "nuage", "oci", "openstack", "kubernetes", "vmware", "sepm", "aci-direct", "ibm", "nutanix", "sap"]
    # SDN proxy.
    proxy: str
    # Enable/disable use of IAM role from metadata to call API.
    use_metadata_iam: Literal["disable", "enable"]
    # Enable to use as Microsoft 365 connector.
    microsoft_365: Literal["disable", "enable"]
    # Enable/disable use for FortiGate HA service.
    ha_status: Literal["disable", "enable"]
    # Enable/disable server certificate verification.
    verify_certificate: Literal["disable", "enable"]
    # Virtual domain name of the remote SDN connector.
    vdom: str
    # Server address of the remote SDN connector.
    server: str
    # Server address list of the remote SDN connector.
    server_list: list[SdnConnectorServerlistObject]  # Table field - list of typed objects
    # Port number of the remote SDN connector.
    server_port: int
    # HTTP port number of the SAP message server.
    message_server_port: int
    # Username of the remote SDN connector as login credentials.
    username: str
    # Password of the remote SDN connector as login credentials.
    password: str
    # vCenter server address for NSX quarantine.
    vcenter_server: str
    # vCenter server username for NSX quarantine.
    vcenter_username: str
    # vCenter server password for NSX quarantine.
    vcenter_password: str
    # AWS / ACS access key ID.
    access_key: str
    # AWS / ACS secret access key.
    secret_key: str
    # AWS / ACS region name.
    region: str
    # AWS VPC ID.
    vpc_id: str
    # Enable/disable AWS alternative resource IP.
    alt_resource_ip: Literal["disable", "enable"]
    # Configure AWS external account list.
    external_account_list: list[SdnConnectorExternalaccountlistObject]  # Table field - list of typed objects
    # Tenant ID (directory ID).
    tenant_id: str
    # Azure client ID (application ID).
    client_id: str
    # Azure client secret (application key).
    client_secret: str
    # Azure subscription ID.
    subscription_id: str
    # Azure resource group.
    resource_group: str
    # Azure Stack login endpoint.
    login_endpoint: str
    # Azure Stack resource URL.
    resource_url: str
    # Azure server region.
    azure_region: Literal["global", "china", "germany", "usgov", "local"]
    # Configure Azure network interface.
    nic: list[SdnConnectorNicObject]  # Table field - list of typed objects
    # Configure Azure route table.
    route_table: list[SdnConnectorRoutetableObject]  # Table field - list of typed objects
    # User ID.
    user_id: str
    # Configure OCI compartment list.
    compartment_list: list[SdnConnectorCompartmentlistObject]  # Table field - list of typed objects
    # Configure OCI region list.
    oci_region_list: list[SdnConnectorOciregionlistObject]  # Table field - list of typed objects
    # OCI region type.
    oci_region_type: Literal["commercial", "government"]
    # OCI certificate.
    oci_cert: str
    # OCI pubkey fingerprint.
    oci_fingerprint: str
    # Configure GCP external IP.
    external_ip: list[SdnConnectorExternalipObject]  # Table field - list of typed objects
    # Configure GCP route.
    route: list[SdnConnectorRouteObject]  # Table field - list of typed objects
    # Configure GCP project list.
    gcp_project_list: list[SdnConnectorGcpprojectlistObject]  # Table field - list of typed objects
    # Configure GCP forwarding rule.
    forwarding_rule: list[SdnConnectorForwardingruleObject]  # Table field - list of typed objects
    # GCP service account email.
    service_account: str
    # Private key of GCP service account.
    private_key: str
    # Secret token of Kubernetes service account.
    secret_token: str
    # Domain name.
    domain: str
    # Full path group name of computers.
    group_name: str
    # Trust servers that contain this certificate only.
    server_cert: str
    # Trust only those servers whose certificate is directly/indirectly signed by this
    server_ca_cert: str
    # IBM cloud API key or service ID API key.
    api_key: str
    # IBM cloud region name.
    ibm_region: Literal["dallas", "washington-dc", "london", "frankfurt", "sydney", "tokyo", "osaka", "toronto", "sao-paulo", "madrid"]
    # Public address range ID.
    par_id: str
    # Dynamic object update interval (30 - 3600 sec, default = 60, 0 = disabled).
    update_interval: int
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> SdnConnectorPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class SdnConnector:
    """
    Configure connection to SDN Connector.
    
    Path: system/sdn_connector
    Category: cmdb
    Primary Key: name
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey/name provided as positional arg)
    @overload
    def get(
        self,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SdnConnectorObject: ...
    
    # Single object (mkey/name provided as keyword arg)
    @overload
    def get(
        self,
        *,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SdnConnectorObject: ...
    
    # List of objects (no mkey/name provided) - keyword-only signature
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
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> list[SdnConnectorObject]: ...
    
    @overload
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Dict mode with mkey provided as positional arg (single dict)
    @overload
    def get(
        self,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> SdnConnectorResponse: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> SdnConnectorResponse: ...
    
    # Dict mode - list of dicts (no mkey/name provided) - keyword-only signature
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
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> list[SdnConnectorResponse]: ...
    
    # Default overload for dict mode
    @overload
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], list[dict[str, Any]]]: ...
    
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: str | None = ...,
        **kwargs: Any,
    ) -> SdnConnectorObject | list[SdnConnectorObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
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
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
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
        external_account_list: str | list[str] | list[dict[str, Any]] | None = ...,
        tenant_id: str | None = ...,
        client_id: str | None = ...,
        client_secret: str | None = ...,
        subscription_id: str | None = ...,
        resource_group: str | None = ...,
        login_endpoint: str | None = ...,
        resource_url: str | None = ...,
        azure_region: Literal["global", "china", "germany", "usgov", "local"] | None = ...,
        nic: str | list[str] | list[dict[str, Any]] | None = ...,
        route_table: str | list[str] | list[dict[str, Any]] | None = ...,
        user_id: str | None = ...,
        compartment_list: str | list[str] | list[dict[str, Any]] | None = ...,
        oci_region_list: str | list[str] | list[dict[str, Any]] | None = ...,
        oci_region_type: Literal["commercial", "government"] | None = ...,
        oci_cert: str | None = ...,
        oci_fingerprint: str | None = ...,
        external_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        route: str | list[str] | list[dict[str, Any]] | None = ...,
        gcp_project_list: str | list[str] | list[dict[str, Any]] | None = ...,
        forwarding_rule: str | list[str] | list[dict[str, Any]] | None = ...,
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
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SdnConnectorObject: ...
    
    @overload
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
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
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
        external_account_list: str | list[str] | list[dict[str, Any]] | None = ...,
        tenant_id: str | None = ...,
        client_id: str | None = ...,
        client_secret: str | None = ...,
        subscription_id: str | None = ...,
        resource_group: str | None = ...,
        login_endpoint: str | None = ...,
        resource_url: str | None = ...,
        azure_region: Literal["global", "china", "germany", "usgov", "local"] | None = ...,
        nic: str | list[str] | list[dict[str, Any]] | None = ...,
        route_table: str | list[str] | list[dict[str, Any]] | None = ...,
        user_id: str | None = ...,
        compartment_list: str | list[str] | list[dict[str, Any]] | None = ...,
        oci_region_list: str | list[str] | list[dict[str, Any]] | None = ...,
        oci_region_type: Literal["commercial", "government"] | None = ...,
        oci_cert: str | None = ...,
        oci_fingerprint: str | None = ...,
        external_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        route: str | list[str] | list[dict[str, Any]] | None = ...,
        gcp_project_list: str | list[str] | list[dict[str, Any]] | None = ...,
        forwarding_rule: str | list[str] | list[dict[str, Any]] | None = ...,
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
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
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
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
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
        external_account_list: str | list[str] | list[dict[str, Any]] | None = ...,
        tenant_id: str | None = ...,
        client_id: str | None = ...,
        client_secret: str | None = ...,
        subscription_id: str | None = ...,
        resource_group: str | None = ...,
        login_endpoint: str | None = ...,
        resource_url: str | None = ...,
        azure_region: Literal["global", "china", "germany", "usgov", "local"] | None = ...,
        nic: str | list[str] | list[dict[str, Any]] | None = ...,
        route_table: str | list[str] | list[dict[str, Any]] | None = ...,
        user_id: str | None = ...,
        compartment_list: str | list[str] | list[dict[str, Any]] | None = ...,
        oci_region_list: str | list[str] | list[dict[str, Any]] | None = ...,
        oci_region_type: Literal["commercial", "government"] | None = ...,
        oci_cert: str | None = ...,
        oci_fingerprint: str | None = ...,
        external_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        route: str | list[str] | list[dict[str, Any]] | None = ...,
        gcp_project_list: str | list[str] | list[dict[str, Any]] | None = ...,
        forwarding_rule: str | list[str] | list[dict[str, Any]] | None = ...,
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
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
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
        external_account_list: str | list[str] | list[dict[str, Any]] | None = ...,
        tenant_id: str | None = ...,
        client_id: str | None = ...,
        client_secret: str | None = ...,
        subscription_id: str | None = ...,
        resource_group: str | None = ...,
        login_endpoint: str | None = ...,
        resource_url: str | None = ...,
        azure_region: Literal["global", "china", "germany", "usgov", "local"] | None = ...,
        nic: str | list[str] | list[dict[str, Any]] | None = ...,
        route_table: str | list[str] | list[dict[str, Any]] | None = ...,
        user_id: str | None = ...,
        compartment_list: str | list[str] | list[dict[str, Any]] | None = ...,
        oci_region_list: str | list[str] | list[dict[str, Any]] | None = ...,
        oci_region_type: Literal["commercial", "government"] | None = ...,
        oci_cert: str | None = ...,
        oci_fingerprint: str | None = ...,
        external_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        route: str | list[str] | list[dict[str, Any]] | None = ...,
        gcp_project_list: str | list[str] | list[dict[str, Any]] | None = ...,
        forwarding_rule: str | list[str] | list[dict[str, Any]] | None = ...,
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
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
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
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
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
        external_account_list: str | list[str] | list[dict[str, Any]] | None = ...,
        tenant_id: str | None = ...,
        client_id: str | None = ...,
        client_secret: str | None = ...,
        subscription_id: str | None = ...,
        resource_group: str | None = ...,
        login_endpoint: str | None = ...,
        resource_url: str | None = ...,
        azure_region: Literal["global", "china", "germany", "usgov", "local"] | None = ...,
        nic: str | list[str] | list[dict[str, Any]] | None = ...,
        route_table: str | list[str] | list[dict[str, Any]] | None = ...,
        user_id: str | None = ...,
        compartment_list: str | list[str] | list[dict[str, Any]] | None = ...,
        oci_region_list: str | list[str] | list[dict[str, Any]] | None = ...,
        oci_region_type: Literal["commercial", "government"] | None = ...,
        oci_cert: str | None = ...,
        oci_fingerprint: str | None = ...,
        external_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        route: str | list[str] | list[dict[str, Any]] | None = ...,
        gcp_project_list: str | list[str] | list[dict[str, Any]] | None = ...,
        forwarding_rule: str | list[str] | list[dict[str, Any]] | None = ...,
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
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SdnConnectorObject: ...
    
    @overload
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
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
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
        external_account_list: str | list[str] | list[dict[str, Any]] | None = ...,
        tenant_id: str | None = ...,
        client_id: str | None = ...,
        client_secret: str | None = ...,
        subscription_id: str | None = ...,
        resource_group: str | None = ...,
        login_endpoint: str | None = ...,
        resource_url: str | None = ...,
        azure_region: Literal["global", "china", "germany", "usgov", "local"] | None = ...,
        nic: str | list[str] | list[dict[str, Any]] | None = ...,
        route_table: str | list[str] | list[dict[str, Any]] | None = ...,
        user_id: str | None = ...,
        compartment_list: str | list[str] | list[dict[str, Any]] | None = ...,
        oci_region_list: str | list[str] | list[dict[str, Any]] | None = ...,
        oci_region_type: Literal["commercial", "government"] | None = ...,
        oci_cert: str | None = ...,
        oci_fingerprint: str | None = ...,
        external_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        route: str | list[str] | list[dict[str, Any]] | None = ...,
        gcp_project_list: str | list[str] | list[dict[str, Any]] | None = ...,
        forwarding_rule: str | list[str] | list[dict[str, Any]] | None = ...,
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
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
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
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
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
        external_account_list: str | list[str] | list[dict[str, Any]] | None = ...,
        tenant_id: str | None = ...,
        client_id: str | None = ...,
        client_secret: str | None = ...,
        subscription_id: str | None = ...,
        resource_group: str | None = ...,
        login_endpoint: str | None = ...,
        resource_url: str | None = ...,
        azure_region: Literal["global", "china", "germany", "usgov", "local"] | None = ...,
        nic: str | list[str] | list[dict[str, Any]] | None = ...,
        route_table: str | list[str] | list[dict[str, Any]] | None = ...,
        user_id: str | None = ...,
        compartment_list: str | list[str] | list[dict[str, Any]] | None = ...,
        oci_region_list: str | list[str] | list[dict[str, Any]] | None = ...,
        oci_region_type: Literal["commercial", "government"] | None = ...,
        oci_cert: str | None = ...,
        oci_fingerprint: str | None = ...,
        external_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        route: str | list[str] | list[dict[str, Any]] | None = ...,
        gcp_project_list: str | list[str] | list[dict[str, Any]] | None = ...,
        forwarding_rule: str | list[str] | list[dict[str, Any]] | None = ...,
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
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
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
        external_account_list: str | list[str] | list[dict[str, Any]] | None = ...,
        tenant_id: str | None = ...,
        client_id: str | None = ...,
        client_secret: str | None = ...,
        subscription_id: str | None = ...,
        resource_group: str | None = ...,
        login_endpoint: str | None = ...,
        resource_url: str | None = ...,
        azure_region: Literal["global", "china", "germany", "usgov", "local"] | None = ...,
        nic: str | list[str] | list[dict[str, Any]] | None = ...,
        route_table: str | list[str] | list[dict[str, Any]] | None = ...,
        user_id: str | None = ...,
        compartment_list: str | list[str] | list[dict[str, Any]] | None = ...,
        oci_region_list: str | list[str] | list[dict[str, Any]] | None = ...,
        oci_region_type: Literal["commercial", "government"] | None = ...,
        oci_cert: str | None = ...,
        oci_fingerprint: str | None = ...,
        external_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        route: str | list[str] | list[dict[str, Any]] | None = ...,
        gcp_project_list: str | list[str] | list[dict[str, Any]] | None = ...,
        forwarding_rule: str | list[str] | list[dict[str, Any]] | None = ...,
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
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SdnConnectorObject: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
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
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
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
        external_account_list: str | list[str] | list[dict[str, Any]] | None = ...,
        tenant_id: str | None = ...,
        client_id: str | None = ...,
        client_secret: str | None = ...,
        subscription_id: str | None = ...,
        resource_group: str | None = ...,
        login_endpoint: str | None = ...,
        resource_url: str | None = ...,
        azure_region: Literal["global", "china", "germany", "usgov", "local"] | None = ...,
        nic: str | list[str] | list[dict[str, Any]] | None = ...,
        route_table: str | list[str] | list[dict[str, Any]] | None = ...,
        user_id: str | None = ...,
        compartment_list: str | list[str] | list[dict[str, Any]] | None = ...,
        oci_region_list: str | list[str] | list[dict[str, Any]] | None = ...,
        oci_region_type: Literal["commercial", "government"] | None = ...,
        oci_cert: str | None = ...,
        oci_fingerprint: str | None = ...,
        external_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        route: str | list[str] | list[dict[str, Any]] | None = ...,
        gcp_project_list: str | list[str] | list[dict[str, Any]] | None = ...,
        forwarding_rule: str | list[str] | list[dict[str, Any]] | None = ...,
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
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Helper methods
    @staticmethod
    def help(field_name: str | None = ...) -> str: ...
    
    @staticmethod
    def fields(detailed: bool = ...) -> Union[list[str], list[dict[str, Any]]]: ...
    
    @staticmethod
    def field_info(field_name: str) -> dict[str, Any]: ...
    
    @staticmethod
    def validate_field(name: str, value: Any) -> bool: ...
    
    @staticmethod
    def required_fields() -> list[str]: ...
    
    @staticmethod
    def defaults() -> dict[str, Any]: ...
    
    @staticmethod
    def schema() -> dict[str, Any]: ...


__all__ = [
    "SdnConnector",
    "SdnConnectorPayload",
    "SdnConnectorObject",
]