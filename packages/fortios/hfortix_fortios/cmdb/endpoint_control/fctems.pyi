from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class FctemsPayload(TypedDict, total=False):
    """
    Type hints for endpoint_control/fctems payload fields.
    
    Configure FortiClient Enterprise Management Server (EMS) entries.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.certificate.ca.CaEndpoint` (via: verifying-ca)
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface)
        - :class:`~.vpn.certificate.ca.CaEndpoint` (via: verifying-ca)

    **Usage:**
        payload: FctemsPayload = {
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


class FctemsObject(FortiObject[FctemsPayload]):
    """Typed FortiObject for endpoint_control/fctems with IDE autocomplete support."""
    
    # EMS ID in order (1 - 7).
    ems_id: int
    # Enable or disable this EMS configuration.
    status: Literal["enable", "disable"]
    # FortiClient Enterprise Management Server (EMS) name.
    name: str
    # Dirty Reason for FortiClient EMS.
    dirty_reason: Literal["none", "mismatched-ems-sn"]
    # Enable/disable authentication of FortiClient EMS Cloud through FortiCloud accoun
    fortinetone_cloud_authentication: Literal["enable", "disable"]
    # FortiClient EMS Cloud multitenancy access key
    cloud_authentication_access_key: str
    # FortiClient EMS FQDN or IPv4 address.
    server: str
    # FortiClient EMS HTTPS access port number. (1 - 65535, default: 443).
    https_port: int
    # EMS Serial Number.
    serial_number: str
    # EMS Tenant ID.
    tenant_id: str
    # REST API call source IP.
    source_ip: str
    # Enable/disable pulling SysInfo from EMS.
    pull_sysinfo: Literal["enable", "disable"]
    # Enable/disable pulling vulnerabilities from EMS.
    pull_vulnerabilities: Literal["enable", "disable"]
    # Enable/disable pulling FortiClient user tags from EMS.
    pull_tags: Literal["enable", "disable"]
    # Enable/disable pulling FortiClient malware hash from EMS.
    pull_malware_hash: Literal["enable", "disable"]
    # List of EMS capabilities.
    capabilities: Literal["fabric-auth", "silent-approval", "websocket", "websocket-malware", "push-ca-certs", "common-tags-api", "tenant-id", "client-avatars", "single-vdom-connector", "fgt-sysinfo-api", "ztna-server-info", "used-tags"]
    # FortiClient EMS call timeout in seconds (1 - 180 seconds, default = 30).
    call_timeout: int
    # Outdated resource threshold in seconds (10 - 3600, default = 180).
    out_of_sync_threshold: int
    # Relax restrictions on tags to send all EMS tags to all VDOMs
    send_tags_to_all_vdoms: Literal["enable", "disable"]
    # Enable/disable override behavior for how this FortiGate unit connects to EMS usi
    websocket_override: Literal["enable", "disable"]
    # Specify how to select outgoing interface to reach server.
    interface_select_method: Literal["auto", "sdwan", "specify"]
    # Specify outgoing interface to reach server.
    interface: str
    # Enable/disable trust of the EMS certificate issuer(CA) and common name(CN) for c
    trust_ca_cn: Literal["enable", "disable"]
    # Lowest CA cert on Fortigate in verified EMS cert chain.
    verifying_ca: str
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FctemsPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Fctems:
    """
    Configure FortiClient Enterprise Management Server (EMS) entries.
    
    Path: endpoint_control/fctems
    Category: cmdb
    Primary Key: ems-id
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey provided)
    @overload
    def get(
        self,
        ems_id: int,
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
        *,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> FctemsObject: ...
    
    # List of objects (no mkey provided - most specific for list returns)
    # For singleton endpoints (no mkey), returns single object; for table endpoints, returns list
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
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> list[FctemsObject]: ...
    
    @overload
    def get(
        self,
        ems_id: int | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True],
        *,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Dict mode with mkey provided (single dict)
    @overload
    def get(
        self,
        ems_id: int,
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
    ) -> dict[str, Any]: ...
    
    # Dict mode without mkey (returns dict with results array)
    @overload
    def get(
        self,
        ems_id: None = None,
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
    ) -> dict[str, Any]: ...
    
    # Default overload for dict mode
    @overload
    def get(
        self,
        ems_id: int | None = ...,
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
        ems_id: int | None = ...,
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
    ) -> FctemsObject | list[FctemsObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: FctemsPayload | None = ...,
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
        capabilities: Literal["fabric-auth", "silent-approval", "websocket", "websocket-malware", "push-ca-certs", "common-tags-api", "tenant-id", "client-avatars", "single-vdom-connector", "fgt-sysinfo-api", "ztna-server-info", "used-tags"] | list[str] | list[dict[str, Any]] | None = ...,
        call_timeout: int | None = ...,
        out_of_sync_threshold: int | None = ...,
        send_tags_to_all_vdoms: Literal["enable", "disable"] | None = ...,
        websocket_override: Literal["enable", "disable"] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        trust_ca_cn: Literal["enable", "disable"] | None = ...,
        verifying_ca: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> FctemsObject: ...
    
    @overload
    def post(
        self,
        payload_dict: FctemsPayload | None = ...,
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
        capabilities: Literal["fabric-auth", "silent-approval", "websocket", "websocket-malware", "push-ca-certs", "common-tags-api", "tenant-id", "client-avatars", "single-vdom-connector", "fgt-sysinfo-api", "ztna-server-info", "used-tags"] | list[str] | list[dict[str, Any]] | None = ...,
        call_timeout: int | None = ...,
        out_of_sync_threshold: int | None = ...,
        send_tags_to_all_vdoms: Literal["enable", "disable"] | None = ...,
        websocket_override: Literal["enable", "disable"] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        trust_ca_cn: Literal["enable", "disable"] | None = ...,
        verifying_ca: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: FctemsPayload | None = ...,
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
        capabilities: Literal["fabric-auth", "silent-approval", "websocket", "websocket-malware", "push-ca-certs", "common-tags-api", "tenant-id", "client-avatars", "single-vdom-connector", "fgt-sysinfo-api", "ztna-server-info", "used-tags"] | list[str] | list[dict[str, Any]] | None = ...,
        call_timeout: int | None = ...,
        out_of_sync_threshold: int | None = ...,
        send_tags_to_all_vdoms: Literal["enable", "disable"] | None = ...,
        websocket_override: Literal["enable", "disable"] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        trust_ca_cn: Literal["enable", "disable"] | None = ...,
        verifying_ca: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: FctemsPayload | None = ...,
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
        capabilities: Literal["fabric-auth", "silent-approval", "websocket", "websocket-malware", "push-ca-certs", "common-tags-api", "tenant-id", "client-avatars", "single-vdom-connector", "fgt-sysinfo-api", "ztna-server-info", "used-tags"] | list[str] | list[dict[str, Any]] | None = ...,
        call_timeout: int | None = ...,
        out_of_sync_threshold: int | None = ...,
        send_tags_to_all_vdoms: Literal["enable", "disable"] | None = ...,
        websocket_override: Literal["enable", "disable"] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        trust_ca_cn: Literal["enable", "disable"] | None = ...,
        verifying_ca: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: FctemsPayload | None = ...,
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
        capabilities: Literal["fabric-auth", "silent-approval", "websocket", "websocket-malware", "push-ca-certs", "common-tags-api", "tenant-id", "client-avatars", "single-vdom-connector", "fgt-sysinfo-api", "ztna-server-info", "used-tags"] | list[str] | list[dict[str, Any]] | None = ...,
        call_timeout: int | None = ...,
        out_of_sync_threshold: int | None = ...,
        send_tags_to_all_vdoms: Literal["enable", "disable"] | None = ...,
        websocket_override: Literal["enable", "disable"] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        trust_ca_cn: Literal["enable", "disable"] | None = ...,
        verifying_ca: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> FctemsObject: ...
    
    @overload
    def put(
        self,
        payload_dict: FctemsPayload | None = ...,
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
        capabilities: Literal["fabric-auth", "silent-approval", "websocket", "websocket-malware", "push-ca-certs", "common-tags-api", "tenant-id", "client-avatars", "single-vdom-connector", "fgt-sysinfo-api", "ztna-server-info", "used-tags"] | list[str] | list[dict[str, Any]] | None = ...,
        call_timeout: int | None = ...,
        out_of_sync_threshold: int | None = ...,
        send_tags_to_all_vdoms: Literal["enable", "disable"] | None = ...,
        websocket_override: Literal["enable", "disable"] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        trust_ca_cn: Literal["enable", "disable"] | None = ...,
        verifying_ca: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: FctemsPayload | None = ...,
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
        capabilities: Literal["fabric-auth", "silent-approval", "websocket", "websocket-malware", "push-ca-certs", "common-tags-api", "tenant-id", "client-avatars", "single-vdom-connector", "fgt-sysinfo-api", "ztna-server-info", "used-tags"] | list[str] | list[dict[str, Any]] | None = ...,
        call_timeout: int | None = ...,
        out_of_sync_threshold: int | None = ...,
        send_tags_to_all_vdoms: Literal["enable", "disable"] | None = ...,
        websocket_override: Literal["enable", "disable"] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        trust_ca_cn: Literal["enable", "disable"] | None = ...,
        verifying_ca: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: FctemsPayload | None = ...,
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
        capabilities: Literal["fabric-auth", "silent-approval", "websocket", "websocket-malware", "push-ca-certs", "common-tags-api", "tenant-id", "client-avatars", "single-vdom-connector", "fgt-sysinfo-api", "ztna-server-info", "used-tags"] | list[str] | list[dict[str, Any]] | None = ...,
        call_timeout: int | None = ...,
        out_of_sync_threshold: int | None = ...,
        send_tags_to_all_vdoms: Literal["enable", "disable"] | None = ...,
        websocket_override: Literal["enable", "disable"] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        trust_ca_cn: Literal["enable", "disable"] | None = ...,
        verifying_ca: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        ems_id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> FctemsObject: ...
    
    @overload
    def delete(
        self,
        ems_id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def delete(
        self,
        ems_id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def delete(
        self,
        ems_id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        ems_id: int,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: FctemsPayload | None = ...,
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
        capabilities: Literal["fabric-auth", "silent-approval", "websocket", "websocket-malware", "push-ca-certs", "common-tags-api", "tenant-id", "client-avatars", "single-vdom-connector", "fgt-sysinfo-api", "ztna-server-info", "used-tags"] | list[str] | list[dict[str, Any]] | None = ...,
        call_timeout: int | None = ...,
        out_of_sync_threshold: int | None = ...,
        send_tags_to_all_vdoms: Literal["enable", "disable"] | None = ...,
        websocket_override: Literal["enable", "disable"] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        trust_ca_cn: Literal["enable", "disable"] | None = ...,
        verifying_ca: str | None = ...,
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
    "Fctems",
    "FctemsPayload",
    "FctemsObject",
]