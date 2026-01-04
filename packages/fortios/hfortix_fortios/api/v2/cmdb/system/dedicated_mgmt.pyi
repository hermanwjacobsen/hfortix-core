from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class DedicatedMgmtPayload(TypedDict, total=False):
    """
    Type hints for system/dedicated_mgmt payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: DedicatedMgmtPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable dedicated management.
    interface: NotRequired[str]  # Dedicated management interface.
    default_gateway: NotRequired[str]  # Default gateway for dedicated management interface.
    dhcp_server: NotRequired[Literal["enable", "disable"]]  # Enable/disable DHCP server on management interface.
    dhcp_netmask: NotRequired[str]  # DHCP netmask.
    dhcp_start_ip: NotRequired[str]  # DHCP start IP for dedicated management.
    dhcp_end_ip: NotRequired[str]  # DHCP end IP for dedicated management.


class DedicatedMgmt:
    """
    Configure dedicated management.
    
    Path: system/dedicated_mgmt
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
        payload_dict: DedicatedMgmtPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        interface: str | None = ...,
        default_gateway: str | None = ...,
        dhcp_server: Literal["enable", "disable"] | None = ...,
        dhcp_netmask: str | None = ...,
        dhcp_start_ip: str | None = ...,
        dhcp_end_ip: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: DedicatedMgmtPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        interface: str | None = ...,
        default_gateway: str | None = ...,
        dhcp_server: Literal["enable", "disable"] | None = ...,
        dhcp_netmask: str | None = ...,
        dhcp_start_ip: str | None = ...,
        dhcp_end_ip: str | None = ...,
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
        payload_dict: DedicatedMgmtPayload | None = ...,
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