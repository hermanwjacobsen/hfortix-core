from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class SdnConnectorPayload(TypedDict, total=False):
    """
    Type hints for system/sdn_connector payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
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
    update_interval: NotRequired[int]  # Dynamic object update interval (30 - 3600 sec, default = 60,


class SdnConnector:
    """
    Configure connection to SDN Connector.
    
    Path: system/sdn_connector
    Category: cmdb
    Primary Key: name
    """
    
    def get(
        self,
        name: str | None = ...,
        filter: str | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
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
        server_list: list[dict[str, Any]] | None = ...,
        server_port: int | None = ...,
        message_server_port: int | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        vcenter_server: str | None = ...,
        vcenter_username: str | None = ...,
        vcenter_password: str | None = ...,
        access_key: str | None = ...,
        secret_key: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
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
        server_list: list[dict[str, Any]] | None = ...,
        server_port: int | None = ...,
        message_server_port: int | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        vcenter_server: str | None = ...,
        vcenter_username: str | None = ...,
        vcenter_password: str | None = ...,
        access_key: str | None = ...,
        secret_key: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> Union[bool, Coroutine[Any, Any, bool]]: ...
    
    def set(
        self,
        payload_dict: SdnConnectorPayload | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
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