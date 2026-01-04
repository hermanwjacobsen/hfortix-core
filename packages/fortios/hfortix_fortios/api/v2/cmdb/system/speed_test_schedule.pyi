from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class SpeedTestSchedulePayload(TypedDict, total=False):
    """
    Type hints for system/speed_test_schedule payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: SpeedTestSchedulePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    interface: NotRequired[str]  # Interface name.
    status: NotRequired[Literal["disable", "enable"]]  # Enable/disable scheduled speed test.
    diffserv: NotRequired[str]  # DSCP used for speed test.
    server_name: NotRequired[str]  # Speed test server name.
    mode: NotRequired[Literal["UDP", "TCP", "Auto"]]  # Protocol Auto(default), TCP or UDP used for speed test.
    schedules: list[dict[str, Any]]  # Schedules for the interface.
    dynamic_server: NotRequired[Literal["disable", "enable"]]  # Enable/disable dynamic server option.
    ctrl_port: NotRequired[int]  # Port of the controller to get access token.
    server_port: NotRequired[int]  # Port of the server to run speed test.
    update_shaper: NotRequired[Literal["disable", "local", "remote", "both"]]  # Set egress shaper based on the test result.
    update_inbandwidth: NotRequired[Literal["disable", "enable"]]  # Enable/disable bypassing interface's inbound bandwidth setti
    update_outbandwidth: NotRequired[Literal["disable", "enable"]]  # Enable/disable bypassing interface's outbound bandwidth sett
    update_inbandwidth_maximum: NotRequired[int]  # Maximum downloading bandwidth (kbps) to be used in a speed t
    update_inbandwidth_minimum: NotRequired[int]  # Minimum downloading bandwidth (kbps) to be considered effect
    update_outbandwidth_maximum: NotRequired[int]  # Maximum uploading bandwidth (kbps) to be used in a speed tes
    update_outbandwidth_minimum: NotRequired[int]  # Minimum uploading bandwidth (kbps) to be considered effectiv


class SpeedTestSchedule:
    """
    Speed test schedule for each interface.
    
    Path: system/speed_test_schedule
    Category: cmdb
    Primary Key: interface
    """
    
    def get(
        self,
        interface: str | None = ...,
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
        payload_dict: SpeedTestSchedulePayload | None = ...,
        interface: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        diffserv: str | None = ...,
        server_name: str | None = ...,
        mode: Literal["UDP", "TCP", "Auto"] | None = ...,
        schedules: list[dict[str, Any]] | None = ...,
        dynamic_server: Literal["disable", "enable"] | None = ...,
        ctrl_port: int | None = ...,
        server_port: int | None = ...,
        update_shaper: Literal["disable", "local", "remote", "both"] | None = ...,
        update_inbandwidth: Literal["disable", "enable"] | None = ...,
        update_outbandwidth: Literal["disable", "enable"] | None = ...,
        update_inbandwidth_maximum: int | None = ...,
        update_inbandwidth_minimum: int | None = ...,
        update_outbandwidth_maximum: int | None = ...,
        update_outbandwidth_minimum: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: SpeedTestSchedulePayload | None = ...,
        interface: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        diffserv: str | None = ...,
        server_name: str | None = ...,
        mode: Literal["UDP", "TCP", "Auto"] | None = ...,
        schedules: list[dict[str, Any]] | None = ...,
        dynamic_server: Literal["disable", "enable"] | None = ...,
        ctrl_port: int | None = ...,
        server_port: int | None = ...,
        update_shaper: Literal["disable", "local", "remote", "both"] | None = ...,
        update_inbandwidth: Literal["disable", "enable"] | None = ...,
        update_outbandwidth: Literal["disable", "enable"] | None = ...,
        update_inbandwidth_maximum: int | None = ...,
        update_inbandwidth_minimum: int | None = ...,
        update_outbandwidth_maximum: int | None = ...,
        update_outbandwidth_minimum: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def delete(
        self,
        interface: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def exists(
        self,
        interface: str,
        vdom: str | bool | None = ...,
    ) -> Union[bool, Coroutine[Any, Any, bool]]: ...
    
    def set(
        self,
        payload_dict: SpeedTestSchedulePayload | None = ...,
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