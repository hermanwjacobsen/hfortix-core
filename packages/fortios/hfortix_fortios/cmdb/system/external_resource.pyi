from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class ExternalResourcePayload(TypedDict, total=False):
    """
    Type hints for system/external_resource payload fields.
    
    Configure external resource.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface, source-ip-interface)
        - :class:`~.vpn.certificate.local.LocalEndpoint` (via: client-cert)

    **Usage:**
        payload: ExternalResourcePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # External resource name.
    uuid: NotRequired[str]  # Universally Unique Identifier (UUID; automatically assigned 
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable user resource.
    type: NotRequired[Literal["category", "domain", "malware", "address", "mac-address", "data", "generic-address"]]  # User resource type.
    namespace: NotRequired[str]  # Generic external connector address namespace.
    object_array_path: NotRequired[str]  # JSON Path to array of generic addresses in resource.
    address_name_field: NotRequired[str]  # JSON Path to address name in generic address entry.
    address_data_field: NotRequired[str]  # JSON Path to address data in generic address entry.
    address_comment_field: NotRequired[str]  # JSON Path to address description in generic address entry.
    update_method: NotRequired[Literal["feed", "push"]]  # External resource update method.
    category: NotRequired[int]  # User resource category.
    username: NotRequired[str]  # HTTP basic authentication user name.
    password: NotRequired[str]  # HTTP basic authentication password.
    client_cert_auth: NotRequired[Literal["enable", "disable"]]  # Enable/disable using client certificate for TLS authenticati
    client_cert: NotRequired[str]  # Client certificate name.
    comments: NotRequired[str]  # Comment.
    resource: str  # URL of external resource.
    user_agent: NotRequired[str]  # HTTP User-Agent header (default = 'curl/7.58.0').
    server_identity_check: NotRequired[Literal["none", "basic", "full"]]  # Certificate verification option.
    refresh_rate: int  # Time interval to refresh external resource (1 - 43200 min, d
    source_ip: NotRequired[str]  # Source IPv4 address used to communicate with server.
    source_ip_interface: NotRequired[str]  # IPv4 Source interface for communication with the server.
    interface_select_method: NotRequired[Literal["auto", "sdwan", "specify"]]  # Specify how to select outgoing interface to reach server.
    interface: str  # Specify outgoing interface to reach server.
    vrf_select: NotRequired[int]  # VRF ID used for connection to server.


class ExternalResourceObject(FortiObject[ExternalResourcePayload]):
    """Typed FortiObject for system/external_resource with IDE autocomplete support."""
    
    # External resource name.
    name: str
    # Universally Unique Identifier (UUID; automatically assigned but can be manually 
    uuid: str
    # Enable/disable user resource.
    status: Literal["enable", "disable"]
    # User resource type.
    type: Literal["category", "domain", "malware", "address", "mac-address", "data", "generic-address"]
    # Generic external connector address namespace.
    namespace: str
    # JSON Path to array of generic addresses in resource.
    object_array_path: str
    # JSON Path to address name in generic address entry.
    address_name_field: str
    # JSON Path to address data in generic address entry.
    address_data_field: str
    # JSON Path to address description in generic address entry.
    address_comment_field: str
    # External resource update method.
    update_method: Literal["feed", "push"]
    # User resource category.
    category: int
    # HTTP basic authentication user name.
    username: str
    # HTTP basic authentication password.
    password: str
    # Enable/disable using client certificate for TLS authentication.
    client_cert_auth: Literal["enable", "disable"]
    # Client certificate name.
    client_cert: str
    # Comment.
    comments: str
    # URL of external resource.
    resource: str
    # HTTP User-Agent header (default = 'curl/7.58.0').
    user_agent: str
    # Certificate verification option.
    server_identity_check: Literal["none", "basic", "full"]
    # Time interval to refresh external resource (1 - 43200 min, default = 5 min).
    refresh_rate: int
    # Source IPv4 address used to communicate with server.
    source_ip: str
    # IPv4 Source interface for communication with the server.
    source_ip_interface: str
    # Specify how to select outgoing interface to reach server.
    interface_select_method: Literal["auto", "sdwan", "specify"]
    # Specify outgoing interface to reach server.
    interface: str
    # VRF ID used for connection to server.
    vrf_select: int
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> ExternalResourcePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class ExternalResource:
    """
    Configure external resource.
    
    Path: system/external_resource
    Category: cmdb
    Primary Key: name
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey provided)
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
        *,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> ExternalResourceObject: ...
    
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
    ) -> list[ExternalResourceObject]: ...
    
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
        raw_json: Literal[True],
        *,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Dict mode with mkey provided (single dict)
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
    ) -> dict[str, Any]: ...
    
    # Dict mode without mkey (returns dict with results array)
    @overload
    def get(
        self,
        name: None = None,
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
    ) -> ExternalResourceObject | list[ExternalResourceObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: ExternalResourcePayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["category", "domain", "malware", "address", "mac-address", "data", "generic-address"] | None = ...,
        namespace: str | None = ...,
        object_array_path: str | None = ...,
        address_name_field: str | None = ...,
        address_data_field: str | None = ...,
        address_comment_field: str | None = ...,
        update_method: Literal["feed", "push"] | None = ...,
        category: int | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        client_cert_auth: Literal["enable", "disable"] | None = ...,
        client_cert: str | None = ...,
        comments: str | None = ...,
        resource: str | None = ...,
        user_agent: str | None = ...,
        server_identity_check: Literal["none", "basic", "full"] | None = ...,
        refresh_rate: int | None = ...,
        source_ip: str | None = ...,
        source_ip_interface: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ExternalResourceObject: ...
    
    @overload
    def post(
        self,
        payload_dict: ExternalResourcePayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["category", "domain", "malware", "address", "mac-address", "data", "generic-address"] | None = ...,
        namespace: str | None = ...,
        object_array_path: str | None = ...,
        address_name_field: str | None = ...,
        address_data_field: str | None = ...,
        address_comment_field: str | None = ...,
        update_method: Literal["feed", "push"] | None = ...,
        category: int | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        client_cert_auth: Literal["enable", "disable"] | None = ...,
        client_cert: str | None = ...,
        comments: str | None = ...,
        resource: str | None = ...,
        user_agent: str | None = ...,
        server_identity_check: Literal["none", "basic", "full"] | None = ...,
        refresh_rate: int | None = ...,
        source_ip: str | None = ...,
        source_ip_interface: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: ExternalResourcePayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["category", "domain", "malware", "address", "mac-address", "data", "generic-address"] | None = ...,
        namespace: str | None = ...,
        object_array_path: str | None = ...,
        address_name_field: str | None = ...,
        address_data_field: str | None = ...,
        address_comment_field: str | None = ...,
        update_method: Literal["feed", "push"] | None = ...,
        category: int | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        client_cert_auth: Literal["enable", "disable"] | None = ...,
        client_cert: str | None = ...,
        comments: str | None = ...,
        resource: str | None = ...,
        user_agent: str | None = ...,
        server_identity_check: Literal["none", "basic", "full"] | None = ...,
        refresh_rate: int | None = ...,
        source_ip: str | None = ...,
        source_ip_interface: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: ExternalResourcePayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["category", "domain", "malware", "address", "mac-address", "data", "generic-address"] | None = ...,
        namespace: str | None = ...,
        object_array_path: str | None = ...,
        address_name_field: str | None = ...,
        address_data_field: str | None = ...,
        address_comment_field: str | None = ...,
        update_method: Literal["feed", "push"] | None = ...,
        category: int | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        client_cert_auth: Literal["enable", "disable"] | None = ...,
        client_cert: str | None = ...,
        comments: str | None = ...,
        resource: str | None = ...,
        user_agent: str | None = ...,
        server_identity_check: Literal["none", "basic", "full"] | None = ...,
        refresh_rate: int | None = ...,
        source_ip: str | None = ...,
        source_ip_interface: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ExternalResourcePayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["category", "domain", "malware", "address", "mac-address", "data", "generic-address"] | None = ...,
        namespace: str | None = ...,
        object_array_path: str | None = ...,
        address_name_field: str | None = ...,
        address_data_field: str | None = ...,
        address_comment_field: str | None = ...,
        update_method: Literal["feed", "push"] | None = ...,
        category: int | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        client_cert_auth: Literal["enable", "disable"] | None = ...,
        client_cert: str | None = ...,
        comments: str | None = ...,
        resource: str | None = ...,
        user_agent: str | None = ...,
        server_identity_check: Literal["none", "basic", "full"] | None = ...,
        refresh_rate: int | None = ...,
        source_ip: str | None = ...,
        source_ip_interface: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ExternalResourceObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ExternalResourcePayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["category", "domain", "malware", "address", "mac-address", "data", "generic-address"] | None = ...,
        namespace: str | None = ...,
        object_array_path: str | None = ...,
        address_name_field: str | None = ...,
        address_data_field: str | None = ...,
        address_comment_field: str | None = ...,
        update_method: Literal["feed", "push"] | None = ...,
        category: int | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        client_cert_auth: Literal["enable", "disable"] | None = ...,
        client_cert: str | None = ...,
        comments: str | None = ...,
        resource: str | None = ...,
        user_agent: str | None = ...,
        server_identity_check: Literal["none", "basic", "full"] | None = ...,
        refresh_rate: int | None = ...,
        source_ip: str | None = ...,
        source_ip_interface: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: ExternalResourcePayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["category", "domain", "malware", "address", "mac-address", "data", "generic-address"] | None = ...,
        namespace: str | None = ...,
        object_array_path: str | None = ...,
        address_name_field: str | None = ...,
        address_data_field: str | None = ...,
        address_comment_field: str | None = ...,
        update_method: Literal["feed", "push"] | None = ...,
        category: int | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        client_cert_auth: Literal["enable", "disable"] | None = ...,
        client_cert: str | None = ...,
        comments: str | None = ...,
        resource: str | None = ...,
        user_agent: str | None = ...,
        server_identity_check: Literal["none", "basic", "full"] | None = ...,
        refresh_rate: int | None = ...,
        source_ip: str | None = ...,
        source_ip_interface: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: ExternalResourcePayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["category", "domain", "malware", "address", "mac-address", "data", "generic-address"] | None = ...,
        namespace: str | None = ...,
        object_array_path: str | None = ...,
        address_name_field: str | None = ...,
        address_data_field: str | None = ...,
        address_comment_field: str | None = ...,
        update_method: Literal["feed", "push"] | None = ...,
        category: int | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        client_cert_auth: Literal["enable", "disable"] | None = ...,
        client_cert: str | None = ...,
        comments: str | None = ...,
        resource: str | None = ...,
        user_agent: str | None = ...,
        server_identity_check: Literal["none", "basic", "full"] | None = ...,
        refresh_rate: int | None = ...,
        source_ip: str | None = ...,
        source_ip_interface: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
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
    ) -> ExternalResourceObject: ...
    
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
        payload_dict: ExternalResourcePayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["category", "domain", "malware", "address", "mac-address", "data", "generic-address"] | None = ...,
        namespace: str | None = ...,
        object_array_path: str | None = ...,
        address_name_field: str | None = ...,
        address_data_field: str | None = ...,
        address_comment_field: str | None = ...,
        update_method: Literal["feed", "push"] | None = ...,
        category: int | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        client_cert_auth: Literal["enable", "disable"] | None = ...,
        client_cert: str | None = ...,
        comments: str | None = ...,
        resource: str | None = ...,
        user_agent: str | None = ...,
        server_identity_check: Literal["none", "basic", "full"] | None = ...,
        refresh_rate: int | None = ...,
        source_ip: str | None = ...,
        source_ip_interface: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
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
    "ExternalResource",
    "ExternalResourcePayload",
    "ExternalResourceObject",
]