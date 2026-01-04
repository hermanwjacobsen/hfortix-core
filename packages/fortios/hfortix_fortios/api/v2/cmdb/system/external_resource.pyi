from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class ExternalResourcePayload(TypedDict, total=False):
    """
    Type hints for system/external_resource payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
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


class ExternalResource:
    """
    Configure external resource.
    
    Path: system/external_resource
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
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
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
        payload_dict: ExternalResourcePayload | None = ...,
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


__all__ = [
    "ExternalResource",
    "ExternalResourcePayload",
]