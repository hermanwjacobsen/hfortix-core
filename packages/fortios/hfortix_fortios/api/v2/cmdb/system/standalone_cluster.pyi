from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class StandaloneClusterPayload(TypedDict, total=False):
    """
    Type hints for system/standalone_cluster payload fields.
    
    Configure FortiGate Session Life Support Protocol (FGSP) cluster attributes.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: session-sync-dev)

    **Usage:**
        payload: StandaloneClusterPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    standalone_group_id: NotRequired[int]  # Cluster group ID (0 - 255). Must be the same for all members
    group_member_id: NotRequired[int]  # Cluster member ID (0 - 15).
    layer2_connection: NotRequired[Literal["available", "unavailable"]]  # Indicate whether layer 2 connections are present among FGSP
    session_sync_dev: NotRequired[list[dict[str, Any]]]  # Offload session-sync process to kernel and sync sessions usi
    encryption: NotRequired[Literal["enable", "disable"]]  # Enable/disable encryption when synchronizing sessions.
    psksecret: str  # Pre-shared secret for session synchronization
    asymmetric_traffic_control: NotRequired[Literal["cps-preferred", "strict-anti-replay"]]  # Asymmetric traffic control mode.
    cluster_peer: NotRequired[list[dict[str, Any]]]  # Configure FortiGate Session Life Support Protocol (FGSP) ses
    monitor_interface: NotRequired[list[dict[str, Any]]]  # Configure a list of interfaces on which to monitor itself. M
    pingsvr_monitor_interface: NotRequired[list[dict[str, Any]]]  # List of pingsvr monitor interface to check for remote IP mon
    monitor_prefix: NotRequired[list[dict[str, Any]]]  # Configure a list of routing prefixes to monitor.
    helper_traffic_bounce: NotRequired[Literal["enable", "disable"]]  # Enable/disable helper related traffic bounce.
    utm_traffic_bounce: NotRequired[Literal["enable", "disable"]]  # Enable/disable UTM related traffic bounce.

# Nested classes for table field children

@final
class StandaloneClusterClusterpeerObject:
    """Typed object for cluster-peer table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Sync ID.
    sync_id: int
    # VDOM that contains the session synchronization link interface on the peer unit.
    peervd: str
    # IP address of the interface on the peer unit that is used for the session synchr
    peerip: str
    # Sessions from these VDOMs are synchronized using this session synchronization co
    syncvd: str
    # List of interfaces to be turned down before session synchronization is complete.
    down_intfs_before_sess_sync: str
    # Heartbeat interval (1 - 20 (100*ms). Increase to reduce false positives.
    hb_interval: int
    # Lost heartbeat threshold (1 - 60). Increase to reduce false positives.
    hb_lost_threshold: int
    # Enable/disable IPsec tunnel synchronization.
    ipsec_tunnel_sync: Literal["enable", "disable"]
    # Enable/disable IKE route announcement on the backup unit.
    secondary_add_ipsec_routes: Literal["enable", "disable"]
    # Add one or more filters if you only want to synchronize some sessions. Use the f
    session_sync_filter: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class StandaloneClusterMonitorinterfaceObject:
    """Typed object for monitor-interface table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Interface name.
    name: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class StandaloneClusterPingsvrmonitorinterfaceObject:
    """Typed object for pingsvr-monitor-interface table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Interface name.
    name: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class StandaloneClusterMonitorprefixObject:
    """Typed object for monitor-prefix table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ID.
    id: int
    # VDOM name.
    vdom: str
    # VRF ID.
    vrf: int
    # Prefix.
    prefix: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class StandaloneClusterResponse(TypedDict):
    """
    Type hints for system/standalone_cluster API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    standalone_group_id: int
    group_member_id: int
    layer2_connection: Literal["available", "unavailable"]
    session_sync_dev: list[dict[str, Any]]
    encryption: Literal["enable", "disable"]
    psksecret: str
    asymmetric_traffic_control: Literal["cps-preferred", "strict-anti-replay"]
    cluster_peer: list[dict[str, Any]]
    monitor_interface: list[dict[str, Any]]
    pingsvr_monitor_interface: list[dict[str, Any]]
    monitor_prefix: list[dict[str, Any]]
    helper_traffic_bounce: Literal["enable", "disable"]
    utm_traffic_bounce: Literal["enable", "disable"]


@final
class StandaloneClusterObject:
    """Typed FortiObject for system/standalone_cluster with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Cluster group ID (0 - 255). Must be the same for all members.
    standalone_group_id: int
    # Cluster member ID (0 - 15).
    group_member_id: int
    # Indicate whether layer 2 connections are present among FGSP members.
    layer2_connection: Literal["available", "unavailable"]
    # Offload session-sync process to kernel and sync sessions using connected interfa
    session_sync_dev: list[dict[str, Any]]  # Multi-value field
    # Enable/disable encryption when synchronizing sessions.
    encryption: Literal["enable", "disable"]
    # Pre-shared secret for session synchronization
    psksecret: str
    # Asymmetric traffic control mode.
    asymmetric_traffic_control: Literal["cps-preferred", "strict-anti-replay"]
    # Configure FortiGate Session Life Support Protocol (FGSP) session synchronization
    cluster_peer: list[StandaloneClusterClusterpeerObject]  # Table field - list of typed objects
    # Configure a list of interfaces on which to monitor itself. Monitoring is perform
    monitor_interface: list[StandaloneClusterMonitorinterfaceObject]  # Table field - list of typed objects
    # List of pingsvr monitor interface to check for remote IP monitoring.
    pingsvr_monitor_interface: list[StandaloneClusterPingsvrmonitorinterfaceObject]  # Table field - list of typed objects
    # Configure a list of routing prefixes to monitor.
    monitor_prefix: list[StandaloneClusterMonitorprefixObject]  # Table field - list of typed objects
    # Enable/disable helper related traffic bounce.
    helper_traffic_bounce: Literal["enable", "disable"]
    # Enable/disable UTM related traffic bounce.
    utm_traffic_bounce: Literal["enable", "disable"]
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> StandaloneClusterPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class StandaloneCluster:
    """
    Configure FortiGate Session Life Support Protocol (FGSP) cluster attributes.
    
    Path: system/standalone_cluster
    Category: cmdb
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey/name provided as positional arg)
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
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> StandaloneClusterObject: ...
    
    # Single object (mkey/name provided as keyword arg)
    @overload
    def get(
        self,
        *,
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
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> StandaloneClusterObject: ...
    
    # List of objects (no mkey/name provided) - keyword-only signature
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
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> StandaloneClusterObject: ...
    
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
        raw_json: Literal[True] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Dict mode with mkey provided as positional arg (single dict)
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
    ) -> StandaloneClusterResponse: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
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
    ) -> StandaloneClusterResponse: ...
    
    # Dict mode - list of dicts (no mkey/name provided) - keyword-only signature
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
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> StandaloneClusterResponse: ...
    
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
    ) -> dict[str, Any]: ...
    
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
    ) -> StandaloneClusterObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: StandaloneClusterPayload | None = ...,
        standalone_group_id: int | None = ...,
        group_member_id: int | None = ...,
        layer2_connection: Literal["available", "unavailable"] | None = ...,
        session_sync_dev: str | list[str] | None = ...,
        encryption: Literal["enable", "disable"] | None = ...,
        psksecret: str | None = ...,
        asymmetric_traffic_control: Literal["cps-preferred", "strict-anti-replay"] | None = ...,
        cluster_peer: str | list[str] | list[dict[str, Any]] | None = ...,
        monitor_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        pingsvr_monitor_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        monitor_prefix: str | list[str] | list[dict[str, Any]] | None = ...,
        helper_traffic_bounce: Literal["enable", "disable"] | None = ...,
        utm_traffic_bounce: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> StandaloneClusterObject: ...
    
    @overload
    def put(
        self,
        payload_dict: StandaloneClusterPayload | None = ...,
        standalone_group_id: int | None = ...,
        group_member_id: int | None = ...,
        layer2_connection: Literal["available", "unavailable"] | None = ...,
        session_sync_dev: str | list[str] | None = ...,
        encryption: Literal["enable", "disable"] | None = ...,
        psksecret: str | None = ...,
        asymmetric_traffic_control: Literal["cps-preferred", "strict-anti-replay"] | None = ...,
        cluster_peer: str | list[str] | list[dict[str, Any]] | None = ...,
        monitor_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        pingsvr_monitor_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        monitor_prefix: str | list[str] | list[dict[str, Any]] | None = ...,
        helper_traffic_bounce: Literal["enable", "disable"] | None = ...,
        utm_traffic_bounce: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: StandaloneClusterPayload | None = ...,
        standalone_group_id: int | None = ...,
        group_member_id: int | None = ...,
        layer2_connection: Literal["available", "unavailable"] | None = ...,
        session_sync_dev: str | list[str] | None = ...,
        encryption: Literal["enable", "disable"] | None = ...,
        psksecret: str | None = ...,
        asymmetric_traffic_control: Literal["cps-preferred", "strict-anti-replay"] | None = ...,
        cluster_peer: str | list[str] | list[dict[str, Any]] | None = ...,
        monitor_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        pingsvr_monitor_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        monitor_prefix: str | list[str] | list[dict[str, Any]] | None = ...,
        helper_traffic_bounce: Literal["enable", "disable"] | None = ...,
        utm_traffic_bounce: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: StandaloneClusterPayload | None = ...,
        standalone_group_id: int | None = ...,
        group_member_id: int | None = ...,
        layer2_connection: Literal["available", "unavailable"] | None = ...,
        session_sync_dev: str | list[str] | None = ...,
        encryption: Literal["enable", "disable"] | None = ...,
        psksecret: str | None = ...,
        asymmetric_traffic_control: Literal["cps-preferred", "strict-anti-replay"] | None = ...,
        cluster_peer: str | list[str] | list[dict[str, Any]] | None = ...,
        monitor_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        pingsvr_monitor_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        monitor_prefix: str | list[str] | list[dict[str, Any]] | None = ...,
        helper_traffic_bounce: Literal["enable", "disable"] | None = ...,
        utm_traffic_bounce: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: StandaloneClusterPayload | None = ...,
        standalone_group_id: int | None = ...,
        group_member_id: int | None = ...,
        layer2_connection: Literal["available", "unavailable"] | None = ...,
        session_sync_dev: str | list[str] | None = ...,
        encryption: Literal["enable", "disable"] | None = ...,
        psksecret: str | None = ...,
        asymmetric_traffic_control: Literal["cps-preferred", "strict-anti-replay"] | None = ...,
        cluster_peer: str | list[str] | list[dict[str, Any]] | None = ...,
        monitor_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        pingsvr_monitor_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        monitor_prefix: str | list[str] | list[dict[str, Any]] | None = ...,
        helper_traffic_bounce: Literal["enable", "disable"] | None = ...,
        utm_traffic_bounce: Literal["enable", "disable"] | None = ...,
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
    "StandaloneCluster",
    "StandaloneClusterPayload",
    "StandaloneClusterObject",
]