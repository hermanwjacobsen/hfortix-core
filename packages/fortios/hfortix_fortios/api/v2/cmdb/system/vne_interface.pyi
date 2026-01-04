from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class VneInterfacePayload(TypedDict, total=False):
    """
    Type hints for system/vne_interface payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: VneInterfacePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # VNE tunnel name.
    interface: str  # Interface name.
    ssl_certificate: str  # Name of local certificate for SSL connections.
    bmr_hostname: str  # BMR hostname.
    auto_asic_offload: Literal["enable", "disable"]  # Enable/disable tunnel ASIC offloading.
    ipv4_address: NotRequired[str]  # Tunnel IPv4 address and netmask.
    br: str  # IPv6 address or FQDN of the border relay.
    update_url: str  # URL of provisioning server.
    mode: Literal["map-e", "fixed-ip", "ds-lite"]  # VNE tunnel mode.
    http_username: NotRequired[str]  # HTTP authentication user name.
    http_password: NotRequired[str]  # HTTP authentication password.


class VneInterface:
    """
    Configure virtual network enabler tunnels.
    
    Path: system/vne_interface
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
        payload_dict: VneInterfacePayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ssl_certificate: str | None = ...,
        bmr_hostname: str | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        ipv4_address: str | None = ...,
        br: str | None = ...,
        update_url: str | None = ...,
        mode: Literal["map-e", "fixed-ip", "ds-lite"] | None = ...,
        http_username: str | None = ...,
        http_password: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: VneInterfacePayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ssl_certificate: str | None = ...,
        bmr_hostname: str | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        ipv4_address: str | None = ...,
        br: str | None = ...,
        update_url: str | None = ...,
        mode: Literal["map-e", "fixed-ip", "ds-lite"] | None = ...,
        http_username: str | None = ...,
        http_password: str | None = ...,
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
        payload_dict: VneInterfacePayload | None = ...,
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