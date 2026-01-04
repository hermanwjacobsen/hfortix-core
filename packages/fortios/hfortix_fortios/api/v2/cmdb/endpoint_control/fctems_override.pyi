from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class FctemsOverridePayload(TypedDict, total=False):
    """
    Type hints for endpoint_control/fctems_override payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: FctemsOverridePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    ems_id: NotRequired[int]  # EMS ID in order (1 - 7).
    status: NotRequired[Literal["enable", "disable"]]  # Enable or disable this EMS configuration.
    name: NotRequired[str]  # FortiClient Enterprise Management Server (EMS) name.
    dirty_reason: NotRequired[Literal["none", "mismatched-ems-sn"]]  # Dirty Reason for FortiClient EMS.
    fortinetone_cloud_authentication: NotRequired[Literal["enable", "disable"]]  # Enable/disable authentication of FortiClient EMS Cloud throu
    cloud_authentication_access_key: NotRequired[str]  # FortiClient EMS Cloud multitenancy access key
    server: NotRequired[str]  # FortiClient EMS FQDN or IPv4 address.
    https_port: NotRequired[int]  # FortiClient EMS HTTPS access port number. (1 - 65535, defaul
    serial_number: NotRequired[str]  # EMS Serial Number.
    tenant_id: NotRequired[str]  # EMS Tenant ID.
    source_ip: NotRequired[str]  # REST API call source IP.
    pull_sysinfo: NotRequired[Literal["enable", "disable"]]  # Enable/disable pulling SysInfo from EMS.
    pull_vulnerabilities: NotRequired[Literal["enable", "disable"]]  # Enable/disable pulling vulnerabilities from EMS.
    pull_tags: NotRequired[Literal["enable", "disable"]]  # Enable/disable pulling FortiClient user tags from EMS.
    pull_malware_hash: NotRequired[Literal["enable", "disable"]]  # Enable/disable pulling FortiClient malware hash from EMS.
    capabilities: NotRequired[Literal["fabric-auth", "silent-approval", "websocket", "websocket-malware", "push-ca-certs", "common-tags-api", "tenant-id", "client-avatars", "single-vdom-connector", "fgt-sysinfo-api", "ztna-server-info", "used-tags"]]  # List of EMS capabilities.
    call_timeout: NotRequired[int]  # FortiClient EMS call timeout in seconds (1 - 180 seconds, de
    out_of_sync_threshold: NotRequired[int]  # Outdated resource threshold in seconds (10 - 3600, default =
    send_tags_to_all_vdoms: NotRequired[Literal["enable", "disable"]]  # Relax restrictions on tags to send all EMS tags to all VDOMs
    websocket_override: NotRequired[Literal["enable", "disable"]]  # Enable/disable override behavior for how this FortiGate unit
    interface_select_method: NotRequired[Literal["auto", "sdwan", "specify"]]  # Specify how to select outgoing interface to reach server.
    interface: str  # Specify outgoing interface to reach server.
    trust_ca_cn: NotRequired[Literal["enable", "disable"]]  # Enable/disable trust of the EMS certificate issuer(CA) and c
    verifying_ca: NotRequired[str]  # Lowest CA cert on Fortigate in verified EMS cert chain.


class FctemsOverride:
    """
    Configure FortiClient Enterprise Management Server (EMS) entries.
    
    Path: endpoint_control/fctems_override
    Category: cmdb
    Primary Key: ems-id
    """
    
    def get(
        self,
        ems_id: int | None = ...,
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
        payload_dict: FctemsOverridePayload | None = ...,
        ems_id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        name: str | None = ...,
        dirty_reason: Literal["none", "mismatched-ems-sn"] | None = ...,
        fortinetone_cloud_authentication: Literal["enable", "disable"] | None = ...,
        cloud_authentication_access_key: str | None = ...,
        server: str | None = ...,
        https_port: int | None = ...,
        serial_number: str | None = ...,
        tenant_id: str | None = ...,
        source_ip: str | None = ...,
        pull_sysinfo: Literal["enable", "disable"] | None = ...,
        pull_vulnerabilities: Literal["enable", "disable"] | None = ...,
        pull_tags: Literal["enable", "disable"] | None = ...,
        pull_malware_hash: Literal["enable", "disable"] | None = ...,
        capabilities: Literal["fabric-auth", "silent-approval", "websocket", "websocket-malware", "push-ca-certs", "common-tags-api", "tenant-id", "client-avatars", "single-vdom-connector", "fgt-sysinfo-api", "ztna-server-info", "used-tags"] | None = ...,
        call_timeout: int | None = ...,
        out_of_sync_threshold: int | None = ...,
        send_tags_to_all_vdoms: Literal["enable", "disable"] | None = ...,
        websocket_override: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: FctemsOverridePayload | None = ...,
        ems_id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        name: str | None = ...,
        dirty_reason: Literal["none", "mismatched-ems-sn"] | None = ...,
        fortinetone_cloud_authentication: Literal["enable", "disable"] | None = ...,
        cloud_authentication_access_key: str | None = ...,
        server: str | None = ...,
        https_port: int | None = ...,
        serial_number: str | None = ...,
        tenant_id: str | None = ...,
        source_ip: str | None = ...,
        pull_sysinfo: Literal["enable", "disable"] | None = ...,
        pull_vulnerabilities: Literal["enable", "disable"] | None = ...,
        pull_tags: Literal["enable", "disable"] | None = ...,
        pull_malware_hash: Literal["enable", "disable"] | None = ...,
        capabilities: Literal["fabric-auth", "silent-approval", "websocket", "websocket-malware", "push-ca-certs", "common-tags-api", "tenant-id", "client-avatars", "single-vdom-connector", "fgt-sysinfo-api", "ztna-server-info", "used-tags"] | None = ...,
        call_timeout: int | None = ...,
        out_of_sync_threshold: int | None = ...,
        send_tags_to_all_vdoms: Literal["enable", "disable"] | None = ...,
        websocket_override: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def delete(
        self,
        ems_id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def exists(
        self,
        ems_id: int,
        vdom: str | bool | None = ...,
    ) -> Union[bool, Coroutine[Any, Any, bool]]: ...
    
    def set(
        self,
        payload_dict: FctemsOverridePayload | None = ...,
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