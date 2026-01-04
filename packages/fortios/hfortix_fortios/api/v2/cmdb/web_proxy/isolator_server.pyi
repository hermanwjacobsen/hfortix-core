from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class IsolatorServerPayload(TypedDict, total=False):
    """
    Type hints for web_proxy/isolator_server payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: IsolatorServerPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Server name.
    addr_type: NotRequired[Literal["ip", "ipv6", "fqdn"]]  # Address type of the forwarding proxy server: IP or FQDN.
    ip: NotRequired[str]  # Forward proxy server IP address.
    ipv6: NotRequired[str]  # Forward proxy server IPv6 address.
    fqdn: NotRequired[str]  # Forward server Fully Qualified Domain Name (FQDN).
    port: NotRequired[int]  # Port number that the forwarding server expects to receive HT
    interface_select_method: NotRequired[Literal["sdwan", "specify"]]  # Specify how to select outgoing interface to reach server.
    interface: str  # Specify outgoing interface to reach server.
    vrf_select: NotRequired[int]  # VRF ID used for connection to server.
    comment: NotRequired[str]  # Comment.
    masquerade: NotRequired[Literal["enable", "disable"]]  # Enable/disable use of the of the IP address of the outgoing 


class IsolatorServer:
    """
    Configure forward-server addresses.
    
    Path: web_proxy/isolator_server
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
        payload_dict: IsolatorServerPayload | None = ...,
        name: str | None = ...,
        addr_type: Literal["ip", "ipv6", "fqdn"] | None = ...,
        ip: str | None = ...,
        ipv6: str | None = ...,
        fqdn: str | None = ...,
        port: int | None = ...,
        interface_select_method: Literal["sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        comment: str | None = ...,
        masquerade: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: IsolatorServerPayload | None = ...,
        name: str | None = ...,
        addr_type: Literal["ip", "ipv6", "fqdn"] | None = ...,
        ip: str | None = ...,
        ipv6: str | None = ...,
        fqdn: str | None = ...,
        port: int | None = ...,
        interface_select_method: Literal["sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        comment: str | None = ...,
        masquerade: Literal["enable", "disable"] | None = ...,
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
        payload_dict: IsolatorServerPayload | None = ...,
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