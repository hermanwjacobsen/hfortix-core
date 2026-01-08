from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class ArrpProfilePayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/arrp_profile payload fields.
    
    Configure WiFi Automatic Radio Resource Provisioning (ARRP) profiles.
    
    **Usage:**
        payload: ArrpProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # WiFi ARRP profile name.
    comment: NotRequired[str]  # Comment.
    selection_period: NotRequired[int]  # Period in seconds to measure average channel load, noise flo
    monitor_period: NotRequired[int]  # Period in seconds to measure average transmit retries and re
    weight_managed_ap: NotRequired[int]  # Weight in DARRP channel score calculation for managed APs
    weight_rogue_ap: NotRequired[int]  # Weight in DARRP channel score calculation for rogue APs
    weight_noise_floor: NotRequired[int]  # Weight in DARRP channel score calculation for noise floor
    weight_channel_load: NotRequired[int]  # Weight in DARRP channel score calculation for channel load
    weight_spectral_rssi: NotRequired[int]  # Weight in DARRP channel score calculation for spectral RSSI
    weight_weather_channel: NotRequired[int]  # Weight in DARRP channel score calculation for weather channe
    weight_dfs_channel: NotRequired[int]  # Weight in DARRP channel score calculation for DFS channel
    threshold_ap: NotRequired[int]  # Threshold to reject channel in DARRP channel selection phase
    threshold_noise_floor: NotRequired[str]  # Threshold in dBm to reject channel in DARRP channel selectio
    threshold_channel_load: NotRequired[int]  # Threshold in percentage to reject channel in DARRP channel s
    threshold_spectral_rssi: NotRequired[str]  # Threshold in dBm to reject channel in DARRP channel selectio
    threshold_tx_retries: NotRequired[int]  # Threshold in percentage for transmit retries to trigger chan
    threshold_rx_errors: NotRequired[int]  # Threshold in percentage for receive errors to trigger channe
    include_weather_channel: NotRequired[Literal["enable", "disable"]]  # Enable/disable use of weather channel in DARRP channel selec
    include_dfs_channel: NotRequired[Literal["enable", "disable"]]  # Enable/disable use of DFS channel in DARRP channel selection
    override_darrp_optimize: NotRequired[Literal["enable", "disable"]]  # Enable to override setting darrp-optimize and darrp-optimize
    darrp_optimize: NotRequired[int]  # Time for running Distributed Automatic Radio Resource Provis
    darrp_optimize_schedules: NotRequired[list[dict[str, Any]]]  # Firewall schedules for DARRP running time. DARRP will run pe

# Nested classes for table field children

@final
class ArrpProfileDarrpoptimizeschedulesObject:
    """Typed object for darrp-optimize-schedules table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Schedule name.
    name: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class ArrpProfileResponse(TypedDict):
    """
    Type hints for wireless_controller/arrp_profile API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    comment: str
    selection_period: int
    monitor_period: int
    weight_managed_ap: int
    weight_rogue_ap: int
    weight_noise_floor: int
    weight_channel_load: int
    weight_spectral_rssi: int
    weight_weather_channel: int
    weight_dfs_channel: int
    threshold_ap: int
    threshold_noise_floor: str
    threshold_channel_load: int
    threshold_spectral_rssi: str
    threshold_tx_retries: int
    threshold_rx_errors: int
    include_weather_channel: Literal["enable", "disable"]
    include_dfs_channel: Literal["enable", "disable"]
    override_darrp_optimize: Literal["enable", "disable"]
    darrp_optimize: int
    darrp_optimize_schedules: list[dict[str, Any]]


@final
class ArrpProfileObject:
    """Typed FortiObject for wireless_controller/arrp_profile with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # WiFi ARRP profile name.
    name: str
    # Comment.
    comment: str
    # Period in seconds to measure average channel load, noise floor, spectral RSSI
    selection_period: int
    # Period in seconds to measure average transmit retries and receive errors
    monitor_period: int
    # Weight in DARRP channel score calculation for managed APs
    weight_managed_ap: int
    # Weight in DARRP channel score calculation for rogue APs (0 - 2000, default = 10)
    weight_rogue_ap: int
    # Weight in DARRP channel score calculation for noise floor
    weight_noise_floor: int
    # Weight in DARRP channel score calculation for channel load
    weight_channel_load: int
    # Weight in DARRP channel score calculation for spectral RSSI
    weight_spectral_rssi: int
    # Weight in DARRP channel score calculation for weather channel
    weight_weather_channel: int
    # Weight in DARRP channel score calculation for DFS channel
    weight_dfs_channel: int
    # Threshold to reject channel in DARRP channel selection phase 1 due to surroundin
    threshold_ap: int
    # Threshold in dBm to reject channel in DARRP channel selection phase 1 due to noi
    threshold_noise_floor: str
    # Threshold in percentage to reject channel in DARRP channel selection phase 1 due
    threshold_channel_load: int
    # Threshold in dBm to reject channel in DARRP channel selection phase 1 due to spe
    threshold_spectral_rssi: str
    # Threshold in percentage for transmit retries to trigger channel reselection in D
    threshold_tx_retries: int
    # Threshold in percentage for receive errors to trigger channel reselection in DAR
    threshold_rx_errors: int
    # Enable/disable use of weather channel in DARRP channel selection phase 1
    include_weather_channel: Literal["enable", "disable"]
    # Enable/disable use of DFS channel in DARRP channel selection phase 1
    include_dfs_channel: Literal["enable", "disable"]
    # Enable to override setting darrp-optimize and darrp-optimize-schedules
    override_darrp_optimize: Literal["enable", "disable"]
    # Time for running Distributed Automatic Radio Resource Provisioning (DARRP) optim
    darrp_optimize: int
    # Firewall schedules for DARRP running time. DARRP will run periodically based on
    darrp_optimize_schedules: list[ArrpProfileDarrpoptimizeschedulesObject]  # Table field - list of typed objects
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> ArrpProfilePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class ArrpProfile:
    """
    Configure WiFi Automatic Radio Resource Provisioning (ARRP) profiles.
    
    Path: wireless_controller/arrp_profile
    Category: cmdb
    Primary Key: name
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
    ) -> ArrpProfileObject: ...
    
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
    ) -> ArrpProfileObject: ...
    
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
    ) -> list[ArrpProfileObject]: ...
    
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
    ) -> ArrpProfileResponse: ...
    
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
    ) -> ArrpProfileResponse: ...
    
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
    ) -> list[ArrpProfileResponse]: ...
    
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
    ) -> ArrpProfileObject | list[ArrpProfileObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: ArrpProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        selection_period: int | None = ...,
        monitor_period: int | None = ...,
        weight_managed_ap: int | None = ...,
        weight_rogue_ap: int | None = ...,
        weight_noise_floor: int | None = ...,
        weight_channel_load: int | None = ...,
        weight_spectral_rssi: int | None = ...,
        weight_weather_channel: int | None = ...,
        weight_dfs_channel: int | None = ...,
        threshold_ap: int | None = ...,
        threshold_noise_floor: str | None = ...,
        threshold_channel_load: int | None = ...,
        threshold_spectral_rssi: str | None = ...,
        threshold_tx_retries: int | None = ...,
        threshold_rx_errors: int | None = ...,
        include_weather_channel: Literal["enable", "disable"] | None = ...,
        include_dfs_channel: Literal["enable", "disable"] | None = ...,
        override_darrp_optimize: Literal["enable", "disable"] | None = ...,
        darrp_optimize: int | None = ...,
        darrp_optimize_schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ArrpProfileObject: ...
    
    @overload
    def post(
        self,
        payload_dict: ArrpProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        selection_period: int | None = ...,
        monitor_period: int | None = ...,
        weight_managed_ap: int | None = ...,
        weight_rogue_ap: int | None = ...,
        weight_noise_floor: int | None = ...,
        weight_channel_load: int | None = ...,
        weight_spectral_rssi: int | None = ...,
        weight_weather_channel: int | None = ...,
        weight_dfs_channel: int | None = ...,
        threshold_ap: int | None = ...,
        threshold_noise_floor: str | None = ...,
        threshold_channel_load: int | None = ...,
        threshold_spectral_rssi: str | None = ...,
        threshold_tx_retries: int | None = ...,
        threshold_rx_errors: int | None = ...,
        include_weather_channel: Literal["enable", "disable"] | None = ...,
        include_dfs_channel: Literal["enable", "disable"] | None = ...,
        override_darrp_optimize: Literal["enable", "disable"] | None = ...,
        darrp_optimize: int | None = ...,
        darrp_optimize_schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: ArrpProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        selection_period: int | None = ...,
        monitor_period: int | None = ...,
        weight_managed_ap: int | None = ...,
        weight_rogue_ap: int | None = ...,
        weight_noise_floor: int | None = ...,
        weight_channel_load: int | None = ...,
        weight_spectral_rssi: int | None = ...,
        weight_weather_channel: int | None = ...,
        weight_dfs_channel: int | None = ...,
        threshold_ap: int | None = ...,
        threshold_noise_floor: str | None = ...,
        threshold_channel_load: int | None = ...,
        threshold_spectral_rssi: str | None = ...,
        threshold_tx_retries: int | None = ...,
        threshold_rx_errors: int | None = ...,
        include_weather_channel: Literal["enable", "disable"] | None = ...,
        include_dfs_channel: Literal["enable", "disable"] | None = ...,
        override_darrp_optimize: Literal["enable", "disable"] | None = ...,
        darrp_optimize: int | None = ...,
        darrp_optimize_schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: ArrpProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        selection_period: int | None = ...,
        monitor_period: int | None = ...,
        weight_managed_ap: int | None = ...,
        weight_rogue_ap: int | None = ...,
        weight_noise_floor: int | None = ...,
        weight_channel_load: int | None = ...,
        weight_spectral_rssi: int | None = ...,
        weight_weather_channel: int | None = ...,
        weight_dfs_channel: int | None = ...,
        threshold_ap: int | None = ...,
        threshold_noise_floor: str | None = ...,
        threshold_channel_load: int | None = ...,
        threshold_spectral_rssi: str | None = ...,
        threshold_tx_retries: int | None = ...,
        threshold_rx_errors: int | None = ...,
        include_weather_channel: Literal["enable", "disable"] | None = ...,
        include_dfs_channel: Literal["enable", "disable"] | None = ...,
        override_darrp_optimize: Literal["enable", "disable"] | None = ...,
        darrp_optimize: int | None = ...,
        darrp_optimize_schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ArrpProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        selection_period: int | None = ...,
        monitor_period: int | None = ...,
        weight_managed_ap: int | None = ...,
        weight_rogue_ap: int | None = ...,
        weight_noise_floor: int | None = ...,
        weight_channel_load: int | None = ...,
        weight_spectral_rssi: int | None = ...,
        weight_weather_channel: int | None = ...,
        weight_dfs_channel: int | None = ...,
        threshold_ap: int | None = ...,
        threshold_noise_floor: str | None = ...,
        threshold_channel_load: int | None = ...,
        threshold_spectral_rssi: str | None = ...,
        threshold_tx_retries: int | None = ...,
        threshold_rx_errors: int | None = ...,
        include_weather_channel: Literal["enable", "disable"] | None = ...,
        include_dfs_channel: Literal["enable", "disable"] | None = ...,
        override_darrp_optimize: Literal["enable", "disable"] | None = ...,
        darrp_optimize: int | None = ...,
        darrp_optimize_schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ArrpProfileObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ArrpProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        selection_period: int | None = ...,
        monitor_period: int | None = ...,
        weight_managed_ap: int | None = ...,
        weight_rogue_ap: int | None = ...,
        weight_noise_floor: int | None = ...,
        weight_channel_load: int | None = ...,
        weight_spectral_rssi: int | None = ...,
        weight_weather_channel: int | None = ...,
        weight_dfs_channel: int | None = ...,
        threshold_ap: int | None = ...,
        threshold_noise_floor: str | None = ...,
        threshold_channel_load: int | None = ...,
        threshold_spectral_rssi: str | None = ...,
        threshold_tx_retries: int | None = ...,
        threshold_rx_errors: int | None = ...,
        include_weather_channel: Literal["enable", "disable"] | None = ...,
        include_dfs_channel: Literal["enable", "disable"] | None = ...,
        override_darrp_optimize: Literal["enable", "disable"] | None = ...,
        darrp_optimize: int | None = ...,
        darrp_optimize_schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: ArrpProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        selection_period: int | None = ...,
        monitor_period: int | None = ...,
        weight_managed_ap: int | None = ...,
        weight_rogue_ap: int | None = ...,
        weight_noise_floor: int | None = ...,
        weight_channel_load: int | None = ...,
        weight_spectral_rssi: int | None = ...,
        weight_weather_channel: int | None = ...,
        weight_dfs_channel: int | None = ...,
        threshold_ap: int | None = ...,
        threshold_noise_floor: str | None = ...,
        threshold_channel_load: int | None = ...,
        threshold_spectral_rssi: str | None = ...,
        threshold_tx_retries: int | None = ...,
        threshold_rx_errors: int | None = ...,
        include_weather_channel: Literal["enable", "disable"] | None = ...,
        include_dfs_channel: Literal["enable", "disable"] | None = ...,
        override_darrp_optimize: Literal["enable", "disable"] | None = ...,
        darrp_optimize: int | None = ...,
        darrp_optimize_schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: ArrpProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        selection_period: int | None = ...,
        monitor_period: int | None = ...,
        weight_managed_ap: int | None = ...,
        weight_rogue_ap: int | None = ...,
        weight_noise_floor: int | None = ...,
        weight_channel_load: int | None = ...,
        weight_spectral_rssi: int | None = ...,
        weight_weather_channel: int | None = ...,
        weight_dfs_channel: int | None = ...,
        threshold_ap: int | None = ...,
        threshold_noise_floor: str | None = ...,
        threshold_channel_load: int | None = ...,
        threshold_spectral_rssi: str | None = ...,
        threshold_tx_retries: int | None = ...,
        threshold_rx_errors: int | None = ...,
        include_weather_channel: Literal["enable", "disable"] | None = ...,
        include_dfs_channel: Literal["enable", "disable"] | None = ...,
        override_darrp_optimize: Literal["enable", "disable"] | None = ...,
        darrp_optimize: int | None = ...,
        darrp_optimize_schedules: str | list[str] | list[dict[str, Any]] | None = ...,
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
    ) -> ArrpProfileObject: ...
    
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
        payload_dict: ArrpProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        selection_period: int | None = ...,
        monitor_period: int | None = ...,
        weight_managed_ap: int | None = ...,
        weight_rogue_ap: int | None = ...,
        weight_noise_floor: int | None = ...,
        weight_channel_load: int | None = ...,
        weight_spectral_rssi: int | None = ...,
        weight_weather_channel: int | None = ...,
        weight_dfs_channel: int | None = ...,
        threshold_ap: int | None = ...,
        threshold_noise_floor: str | None = ...,
        threshold_channel_load: int | None = ...,
        threshold_spectral_rssi: str | None = ...,
        threshold_tx_retries: int | None = ...,
        threshold_rx_errors: int | None = ...,
        include_weather_channel: Literal["enable", "disable"] | None = ...,
        include_dfs_channel: Literal["enable", "disable"] | None = ...,
        override_darrp_optimize: Literal["enable", "disable"] | None = ...,
        darrp_optimize: int | None = ...,
        darrp_optimize_schedules: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "ArrpProfile",
    "ArrpProfilePayload",
    "ArrpProfileObject",
]