from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class SpeedTestSchedulePayload(TypedDict, total=False):
    """
    Type hints for system/speed_test_schedule payload fields.
    
    Speed test schedule for each interface.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface)
        - :class:`~.system.speed-test-server.SpeedTestServerEndpoint` (via: server-name)

    **Usage:**
        payload: SpeedTestSchedulePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    interface: NotRequired[str]  # Interface name.
    status: NotRequired[Literal["disable", "enable"]]  # Enable/disable scheduled speed test.
    diffserv: NotRequired[str]  # DSCP used for speed test.
    server_name: NotRequired[str]  # Speed test server name in system.speed-test-server list or l
    mode: NotRequired[Literal["UDP", "TCP", "Auto"]]  # Protocol Auto(default), TCP or UDP used for speed test.
    schedules: list[dict[str, Any]]  # Schedules for the interface.
    dynamic_server: NotRequired[Literal["disable", "enable"]]  # Enable/disable dynamic server option.
    ctrl_port: NotRequired[int]  # Port of the controller to get access token.
    server_port: NotRequired[int]  # Port of the server to run speed test.
    update_shaper: NotRequired[Literal["disable", "local", "remote", "both"]]  # Set egress shaper based on the test result.
    update_inbandwidth: NotRequired[Literal["disable", "enable"]]  # Enable/disable bypassing interface's inbound bandwidth setti
    update_outbandwidth: NotRequired[Literal["disable", "enable"]]  # Enable/disable bypassing interface's outbound bandwidth sett
    update_interface_shaping: NotRequired[Literal["disable", "enable"]]  # Enable/disable using the speedtest results as reference for 
    update_inbandwidth_maximum: NotRequired[int]  # Maximum downloading bandwidth (kbps) to be used in a speed t
    update_inbandwidth_minimum: NotRequired[int]  # Minimum downloading bandwidth (kbps) to be considered effect
    update_outbandwidth_maximum: NotRequired[int]  # Maximum uploading bandwidth (kbps) to be used in a speed tes
    update_outbandwidth_minimum: NotRequired[int]  # Minimum uploading bandwidth (kbps) to be considered effectiv
    expected_inbandwidth_minimum: NotRequired[int]  # Set the minimum inbandwidth threshold for applying speedtest
    expected_inbandwidth_maximum: NotRequired[int]  # Set the maximum inbandwidth threshold for applying speedtest
    expected_outbandwidth_minimum: NotRequired[int]  # Set the minimum outbandwidth threshold for applying speedtes
    expected_outbandwidth_maximum: NotRequired[int]  # Set the maximum outbandwidth threshold for applying speedtes
    retries: NotRequired[int]  # Maximum number of times the FortiGate unit will attempt to c
    retry_pause: NotRequired[int]  # Number of seconds the FortiGate pauses between successive sp


class SpeedTestScheduleObject(FortiObject[SpeedTestSchedulePayload]):
    """Typed FortiObject for system/speed_test_schedule with IDE autocomplete support."""
    
    # Interface name.
    interface: str
    # Enable/disable scheduled speed test.
    status: Literal["disable", "enable"]
    # DSCP used for speed test.
    diffserv: str
    # Speed test server name in system.speed-test-server list or leave it as empty to 
    server_name: str
    # Protocol Auto(default), TCP or UDP used for speed test.
    mode: Literal["UDP", "TCP", "Auto"]
    # Schedules for the interface.
    schedules: list[str]  # Auto-flattened from member_table
    # Enable/disable dynamic server option.
    dynamic_server: Literal["disable", "enable"]
    # Port of the controller to get access token.
    ctrl_port: int
    # Port of the server to run speed test.
    server_port: int
    # Set egress shaper based on the test result.
    update_shaper: Literal["disable", "local", "remote", "both"]
    # Enable/disable bypassing interface's inbound bandwidth setting.
    update_inbandwidth: Literal["disable", "enable"]
    # Enable/disable bypassing interface's outbound bandwidth setting.
    update_outbandwidth: Literal["disable", "enable"]
    # Enable/disable using the speedtest results as reference for interface shaping (o
    update_interface_shaping: Literal["disable", "enable"]
    # Maximum downloading bandwidth (kbps) to be used in a speed test.
    update_inbandwidth_maximum: int
    # Minimum downloading bandwidth (kbps) to be considered effective.
    update_inbandwidth_minimum: int
    # Maximum uploading bandwidth (kbps) to be used in a speed test.
    update_outbandwidth_maximum: int
    # Minimum uploading bandwidth (kbps) to be considered effective.
    update_outbandwidth_minimum: int
    # Set the minimum inbandwidth threshold for applying speedtest results on shaping-
    expected_inbandwidth_minimum: int
    # Set the maximum inbandwidth threshold for applying speedtest results on shaping-
    expected_inbandwidth_maximum: int
    # Set the minimum outbandwidth threshold for applying speedtest results on shaping
    expected_outbandwidth_minimum: int
    # Set the maximum outbandwidth threshold for applying speedtest results on shaping
    expected_outbandwidth_maximum: int
    # Maximum number of times the FortiGate unit will attempt to contact the same serv
    retries: int
    # Number of seconds the FortiGate pauses between successive speed tests before try
    retry_pause: int
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> SpeedTestSchedulePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class SpeedTestSchedule:
    """
    Speed test schedule for each interface.
    
    Path: system/speed_test_schedule
    Category: cmdb
    Primary Key: interface
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey provided)
    @overload
    def get(
        self,
        interface: str,
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
    ) -> SpeedTestScheduleObject: ...
    
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
    ) -> list[SpeedTestScheduleObject]: ...
    
    @overload
    def get(
        self,
        interface: str | None = ...,
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
        interface: str,
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
        interface: None = None,
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
        interface: str | None = ...,
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
        interface: str | None = ...,
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
    ) -> SpeedTestScheduleObject | list[SpeedTestScheduleObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: SpeedTestSchedulePayload | None = ...,
        interface: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        diffserv: str | None = ...,
        server_name: str | None = ...,
        mode: Literal["UDP", "TCP", "Auto"] | None = ...,
        schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        dynamic_server: Literal["disable", "enable"] | None = ...,
        ctrl_port: int | None = ...,
        server_port: int | None = ...,
        update_shaper: Literal["disable", "local", "remote", "both"] | None = ...,
        update_inbandwidth: Literal["disable", "enable"] | None = ...,
        update_outbandwidth: Literal["disable", "enable"] | None = ...,
        update_interface_shaping: Literal["disable", "enable"] | None = ...,
        update_inbandwidth_maximum: int | None = ...,
        update_inbandwidth_minimum: int | None = ...,
        update_outbandwidth_maximum: int | None = ...,
        update_outbandwidth_minimum: int | None = ...,
        expected_inbandwidth_minimum: int | None = ...,
        expected_inbandwidth_maximum: int | None = ...,
        expected_outbandwidth_minimum: int | None = ...,
        expected_outbandwidth_maximum: int | None = ...,
        retries: int | None = ...,
        retry_pause: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SpeedTestScheduleObject: ...
    
    @overload
    def post(
        self,
        payload_dict: SpeedTestSchedulePayload | None = ...,
        interface: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        diffserv: str | None = ...,
        server_name: str | None = ...,
        mode: Literal["UDP", "TCP", "Auto"] | None = ...,
        schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        dynamic_server: Literal["disable", "enable"] | None = ...,
        ctrl_port: int | None = ...,
        server_port: int | None = ...,
        update_shaper: Literal["disable", "local", "remote", "both"] | None = ...,
        update_inbandwidth: Literal["disable", "enable"] | None = ...,
        update_outbandwidth: Literal["disable", "enable"] | None = ...,
        update_interface_shaping: Literal["disable", "enable"] | None = ...,
        update_inbandwidth_maximum: int | None = ...,
        update_inbandwidth_minimum: int | None = ...,
        update_outbandwidth_maximum: int | None = ...,
        update_outbandwidth_minimum: int | None = ...,
        expected_inbandwidth_minimum: int | None = ...,
        expected_inbandwidth_maximum: int | None = ...,
        expected_outbandwidth_minimum: int | None = ...,
        expected_outbandwidth_maximum: int | None = ...,
        retries: int | None = ...,
        retry_pause: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: SpeedTestSchedulePayload | None = ...,
        interface: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        diffserv: str | None = ...,
        server_name: str | None = ...,
        mode: Literal["UDP", "TCP", "Auto"] | None = ...,
        schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        dynamic_server: Literal["disable", "enable"] | None = ...,
        ctrl_port: int | None = ...,
        server_port: int | None = ...,
        update_shaper: Literal["disable", "local", "remote", "both"] | None = ...,
        update_inbandwidth: Literal["disable", "enable"] | None = ...,
        update_outbandwidth: Literal["disable", "enable"] | None = ...,
        update_interface_shaping: Literal["disable", "enable"] | None = ...,
        update_inbandwidth_maximum: int | None = ...,
        update_inbandwidth_minimum: int | None = ...,
        update_outbandwidth_maximum: int | None = ...,
        update_outbandwidth_minimum: int | None = ...,
        expected_inbandwidth_minimum: int | None = ...,
        expected_inbandwidth_maximum: int | None = ...,
        expected_outbandwidth_minimum: int | None = ...,
        expected_outbandwidth_maximum: int | None = ...,
        retries: int | None = ...,
        retry_pause: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: SpeedTestSchedulePayload | None = ...,
        interface: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        diffserv: str | None = ...,
        server_name: str | None = ...,
        mode: Literal["UDP", "TCP", "Auto"] | None = ...,
        schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        dynamic_server: Literal["disable", "enable"] | None = ...,
        ctrl_port: int | None = ...,
        server_port: int | None = ...,
        update_shaper: Literal["disable", "local", "remote", "both"] | None = ...,
        update_inbandwidth: Literal["disable", "enable"] | None = ...,
        update_outbandwidth: Literal["disable", "enable"] | None = ...,
        update_interface_shaping: Literal["disable", "enable"] | None = ...,
        update_inbandwidth_maximum: int | None = ...,
        update_inbandwidth_minimum: int | None = ...,
        update_outbandwidth_maximum: int | None = ...,
        update_outbandwidth_minimum: int | None = ...,
        expected_inbandwidth_minimum: int | None = ...,
        expected_inbandwidth_maximum: int | None = ...,
        expected_outbandwidth_minimum: int | None = ...,
        expected_outbandwidth_maximum: int | None = ...,
        retries: int | None = ...,
        retry_pause: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: SpeedTestSchedulePayload | None = ...,
        interface: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        diffserv: str | None = ...,
        server_name: str | None = ...,
        mode: Literal["UDP", "TCP", "Auto"] | None = ...,
        schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        dynamic_server: Literal["disable", "enable"] | None = ...,
        ctrl_port: int | None = ...,
        server_port: int | None = ...,
        update_shaper: Literal["disable", "local", "remote", "both"] | None = ...,
        update_inbandwidth: Literal["disable", "enable"] | None = ...,
        update_outbandwidth: Literal["disable", "enable"] | None = ...,
        update_interface_shaping: Literal["disable", "enable"] | None = ...,
        update_inbandwidth_maximum: int | None = ...,
        update_inbandwidth_minimum: int | None = ...,
        update_outbandwidth_maximum: int | None = ...,
        update_outbandwidth_minimum: int | None = ...,
        expected_inbandwidth_minimum: int | None = ...,
        expected_inbandwidth_maximum: int | None = ...,
        expected_outbandwidth_minimum: int | None = ...,
        expected_outbandwidth_maximum: int | None = ...,
        retries: int | None = ...,
        retry_pause: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SpeedTestScheduleObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SpeedTestSchedulePayload | None = ...,
        interface: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        diffserv: str | None = ...,
        server_name: str | None = ...,
        mode: Literal["UDP", "TCP", "Auto"] | None = ...,
        schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        dynamic_server: Literal["disable", "enable"] | None = ...,
        ctrl_port: int | None = ...,
        server_port: int | None = ...,
        update_shaper: Literal["disable", "local", "remote", "both"] | None = ...,
        update_inbandwidth: Literal["disable", "enable"] | None = ...,
        update_outbandwidth: Literal["disable", "enable"] | None = ...,
        update_interface_shaping: Literal["disable", "enable"] | None = ...,
        update_inbandwidth_maximum: int | None = ...,
        update_inbandwidth_minimum: int | None = ...,
        update_outbandwidth_maximum: int | None = ...,
        update_outbandwidth_minimum: int | None = ...,
        expected_inbandwidth_minimum: int | None = ...,
        expected_inbandwidth_maximum: int | None = ...,
        expected_outbandwidth_minimum: int | None = ...,
        expected_outbandwidth_maximum: int | None = ...,
        retries: int | None = ...,
        retry_pause: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: SpeedTestSchedulePayload | None = ...,
        interface: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        diffserv: str | None = ...,
        server_name: str | None = ...,
        mode: Literal["UDP", "TCP", "Auto"] | None = ...,
        schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        dynamic_server: Literal["disable", "enable"] | None = ...,
        ctrl_port: int | None = ...,
        server_port: int | None = ...,
        update_shaper: Literal["disable", "local", "remote", "both"] | None = ...,
        update_inbandwidth: Literal["disable", "enable"] | None = ...,
        update_outbandwidth: Literal["disable", "enable"] | None = ...,
        update_interface_shaping: Literal["disable", "enable"] | None = ...,
        update_inbandwidth_maximum: int | None = ...,
        update_inbandwidth_minimum: int | None = ...,
        update_outbandwidth_maximum: int | None = ...,
        update_outbandwidth_minimum: int | None = ...,
        expected_inbandwidth_minimum: int | None = ...,
        expected_inbandwidth_maximum: int | None = ...,
        expected_outbandwidth_minimum: int | None = ...,
        expected_outbandwidth_maximum: int | None = ...,
        retries: int | None = ...,
        retry_pause: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: SpeedTestSchedulePayload | None = ...,
        interface: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        diffserv: str | None = ...,
        server_name: str | None = ...,
        mode: Literal["UDP", "TCP", "Auto"] | None = ...,
        schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        dynamic_server: Literal["disable", "enable"] | None = ...,
        ctrl_port: int | None = ...,
        server_port: int | None = ...,
        update_shaper: Literal["disable", "local", "remote", "both"] | None = ...,
        update_inbandwidth: Literal["disable", "enable"] | None = ...,
        update_outbandwidth: Literal["disable", "enable"] | None = ...,
        update_interface_shaping: Literal["disable", "enable"] | None = ...,
        update_inbandwidth_maximum: int | None = ...,
        update_inbandwidth_minimum: int | None = ...,
        update_outbandwidth_maximum: int | None = ...,
        update_outbandwidth_minimum: int | None = ...,
        expected_inbandwidth_minimum: int | None = ...,
        expected_inbandwidth_maximum: int | None = ...,
        expected_outbandwidth_minimum: int | None = ...,
        expected_outbandwidth_maximum: int | None = ...,
        retries: int | None = ...,
        retry_pause: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        interface: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SpeedTestScheduleObject: ...
    
    @overload
    def delete(
        self,
        interface: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def delete(
        self,
        interface: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def delete(
        self,
        interface: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        interface: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: SpeedTestSchedulePayload | None = ...,
        interface: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        diffserv: str | None = ...,
        server_name: str | None = ...,
        mode: Literal["UDP", "TCP", "Auto"] | None = ...,
        schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        dynamic_server: Literal["disable", "enable"] | None = ...,
        ctrl_port: int | None = ...,
        server_port: int | None = ...,
        update_shaper: Literal["disable", "local", "remote", "both"] | None = ...,
        update_inbandwidth: Literal["disable", "enable"] | None = ...,
        update_outbandwidth: Literal["disable", "enable"] | None = ...,
        update_interface_shaping: Literal["disable", "enable"] | None = ...,
        update_inbandwidth_maximum: int | None = ...,
        update_inbandwidth_minimum: int | None = ...,
        update_outbandwidth_maximum: int | None = ...,
        update_outbandwidth_minimum: int | None = ...,
        expected_inbandwidth_minimum: int | None = ...,
        expected_inbandwidth_maximum: int | None = ...,
        expected_outbandwidth_minimum: int | None = ...,
        expected_outbandwidth_maximum: int | None = ...,
        retries: int | None = ...,
        retry_pause: int | None = ...,
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
    "SpeedTestSchedule",
    "SpeedTestSchedulePayload",
    "SpeedTestScheduleObject",
]