from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class StandaloneClusterPayload(TypedDict, total=False):
    """
    Type hints for system/standalone_cluster payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: StandaloneClusterPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    standalone_group_id: NotRequired[int]  # Cluster group ID (0 - 255). Must be the same for all members
    group_member_id: NotRequired[int]  # Cluster member ID (0 - 15).
    layer2_connection: NotRequired[Literal["available", "unavailable"]]  # Indicate whether layer 2 connections are present among FGSP 
    session_sync_dev: NotRequired[str]  # Offload session-sync process to kernel and sync sessions usi
    encryption: NotRequired[Literal["enable", "disable"]]  # Enable/disable encryption when synchronizing sessions.
    psksecret: str  # Pre-shared secret for session synchronization (ASCII string 
    asymmetric_traffic_control: NotRequired[Literal["cps-preferred", "strict-anti-replay"]]  # Asymmetric traffic control mode.
    cluster_peer: NotRequired[list[dict[str, Any]]]  # Configure FortiGate Session Life Support Protocol (FGSP) ses
    monitor_interface: NotRequired[list[dict[str, Any]]]  # Configure a list of interfaces on which to monitor itself. M
    pingsvr_monitor_interface: NotRequired[list[dict[str, Any]]]  # List of pingsvr monitor interface to check for remote IP mon
    monitor_prefix: NotRequired[list[dict[str, Any]]]  # Configure a list of routing prefixes to monitor.
    helper_traffic_bounce: NotRequired[Literal["enable", "disable"]]  # Enable/disable helper related traffic bounce.
    utm_traffic_bounce: NotRequired[Literal["enable", "disable"]]  # Enable/disable UTM related traffic bounce.


class StandaloneCluster:
    """
    Configure FortiGate Session Life Support Protocol (FGSP) cluster attributes.
    
    Path: system/standalone_cluster
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
        payload_dict: StandaloneClusterPayload | None = ...,
        standalone_group_id: int | None = ...,
        group_member_id: int | None = ...,
        layer2_connection: Literal["available", "unavailable"] | None = ...,
        session_sync_dev: str | None = ...,
        encryption: Literal["enable", "disable"] | None = ...,
        psksecret: str | None = ...,
        asymmetric_traffic_control: Literal["cps-preferred", "strict-anti-replay"] | None = ...,
        cluster_peer: list[dict[str, Any]] | None = ...,
        monitor_interface: list[dict[str, Any]] | None = ...,
        pingsvr_monitor_interface: list[dict[str, Any]] | None = ...,
        monitor_prefix: list[dict[str, Any]] | None = ...,
        helper_traffic_bounce: Literal["enable", "disable"] | None = ...,
        utm_traffic_bounce: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: StandaloneClusterPayload | None = ...,
        standalone_group_id: int | None = ...,
        group_member_id: int | None = ...,
        layer2_connection: Literal["available", "unavailable"] | None = ...,
        session_sync_dev: str | None = ...,
        encryption: Literal["enable", "disable"] | None = ...,
        psksecret: str | None = ...,
        asymmetric_traffic_control: Literal["cps-preferred", "strict-anti-replay"] | None = ...,
        cluster_peer: list[dict[str, Any]] | None = ...,
        monitor_interface: list[dict[str, Any]] | None = ...,
        pingsvr_monitor_interface: list[dict[str, Any]] | None = ...,
        monitor_prefix: list[dict[str, Any]] | None = ...,
        helper_traffic_bounce: Literal["enable", "disable"] | None = ...,
        utm_traffic_bounce: Literal["enable", "disable"] | None = ...,
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
        payload_dict: StandaloneClusterPayload | None = ...,
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