from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class ShaperPerIpShaperPayload(TypedDict, total=False):
    """
    Type hints for firewall/shaper_per_ip_shaper payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: ShaperPerIpShaperPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Traffic shaper name.
    max_bandwidth: NotRequired[int]  # Upper bandwidth limit enforced by this shaper (0 - 80000000)
    bandwidth_unit: NotRequired[Literal["kbps", "mbps", "gbps"]]  # Unit of measurement for maximum bandwidth for this shaper (K
    max_concurrent_session: NotRequired[int]  # Maximum number of concurrent sessions allowed by this shaper
    max_concurrent_tcp_session: NotRequired[int]  # Maximum number of concurrent TCP sessions allowed by this sh
    max_concurrent_udp_session: NotRequired[int]  # Maximum number of concurrent UDP sessions allowed by this sh
    diffserv_forward: NotRequired[Literal["enable", "disable"]]  # Enable/disable changing the Forward (original) DiffServ sett
    diffserv_reverse: NotRequired[Literal["enable", "disable"]]  # Enable/disable changing the Reverse (reply) DiffServ setting
    diffservcode_forward: NotRequired[str]  # Forward (original) DiffServ setting to be applied to traffic
    diffservcode_rev: NotRequired[str]  # Reverse (reply) DiffServ setting to be applied to traffic ac


class ShaperPerIpShaper:
    """
    Configure per-IP traffic shaper.
    
    Path: firewall/shaper_per_ip_shaper
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
        payload_dict: ShaperPerIpShaperPayload | None = ...,
        name: str | None = ...,
        max_bandwidth: int | None = ...,
        bandwidth_unit: Literal["kbps", "mbps", "gbps"] | None = ...,
        max_concurrent_session: int | None = ...,
        max_concurrent_tcp_session: int | None = ...,
        max_concurrent_udp_session: int | None = ...,
        diffserv_forward: Literal["enable", "disable"] | None = ...,
        diffserv_reverse: Literal["enable", "disable"] | None = ...,
        diffservcode_forward: str | None = ...,
        diffservcode_rev: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: ShaperPerIpShaperPayload | None = ...,
        name: str | None = ...,
        max_bandwidth: int | None = ...,
        bandwidth_unit: Literal["kbps", "mbps", "gbps"] | None = ...,
        max_concurrent_session: int | None = ...,
        max_concurrent_tcp_session: int | None = ...,
        max_concurrent_udp_session: int | None = ...,
        diffserv_forward: Literal["enable", "disable"] | None = ...,
        diffserv_reverse: Literal["enable", "disable"] | None = ...,
        diffservcode_forward: str | None = ...,
        diffservcode_rev: str | None = ...,
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
        payload_dict: ShaperPerIpShaperPayload | None = ...,
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