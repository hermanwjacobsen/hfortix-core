from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class IpamPayload(TypedDict, total=False):
    """
    Type hints for system/ipam payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: IpamPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable IP address management services.
    server_type: NotRequired[Literal["fabric-root"]]  # Configure the type of IPAM server to use.
    automatic_conflict_resolution: NotRequired[Literal["disable", "enable"]]  # Enable/disable automatic conflict resolution.
    require_subnet_size_match: NotRequired[Literal["disable", "enable"]]  # Enable/disable reassignment of subnets to make requested and
    manage_lan_addresses: NotRequired[Literal["disable", "enable"]]  # Enable/disable default management of LAN interface addresses
    manage_lan_extension_addresses: NotRequired[Literal["disable", "enable"]]  # Enable/disable default management of FortiExtender LAN exten
    manage_ssid_addresses: NotRequired[Literal["disable", "enable"]]  # Enable/disable default management of FortiAP SSID addresses.
    pools: NotRequired[list[dict[str, Any]]]  # Configure IPAM pools.
    rules: NotRequired[list[dict[str, Any]]]  # Configure IPAM allocation rules.


class Ipam:
    """
    Configure IP address management services.
    
    Path: system/ipam
    Category: cmdb
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
        payload_dict: IpamPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        server_type: Literal["fabric-root"] | None = ...,
        automatic_conflict_resolution: Literal["disable", "enable"] | None = ...,
        require_subnet_size_match: Literal["disable", "enable"] | None = ...,
        manage_lan_addresses: Literal["disable", "enable"] | None = ...,
        manage_lan_extension_addresses: Literal["disable", "enable"] | None = ...,
        manage_ssid_addresses: Literal["disable", "enable"] | None = ...,
        pools: list[dict[str, Any]] | None = ...,
        rules: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: IpamPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        server_type: Literal["fabric-root"] | None = ...,
        automatic_conflict_resolution: Literal["disable", "enable"] | None = ...,
        require_subnet_size_match: Literal["disable", "enable"] | None = ...,
        manage_lan_addresses: Literal["disable", "enable"] | None = ...,
        manage_lan_extension_addresses: Literal["disable", "enable"] | None = ...,
        manage_ssid_addresses: Literal["disable", "enable"] | None = ...,
        pools: list[dict[str, Any]] | None = ...,
        rules: list[dict[str, Any]] | None = ...,
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
        payload_dict: IpamPayload | None = ...,
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