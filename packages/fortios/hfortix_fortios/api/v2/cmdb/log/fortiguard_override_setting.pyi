from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class FortiguardOverrideSettingPayload(TypedDict, total=False):
    """
    Type hints for log/fortiguard_override_setting payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: FortiguardOverrideSettingPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    override: NotRequired[Literal["enable", "disable"]]  # Overriding FortiCloud settings for this VDOM or use global s
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable logging to FortiCloud.
    upload_option: NotRequired[Literal["store-and-upload", "realtime", "1-minute", "5-minute"]]  # Configure how log messages are sent to FortiCloud.
    upload_interval: NotRequired[Literal["daily", "weekly", "monthly"]]  # Frequency of uploading log files to FortiCloud.
    upload_day: NotRequired[str]  # Day of week to roll logs.
    upload_time: NotRequired[str]  # Time of day to roll logs (hh:mm).
    priority: NotRequired[Literal["default", "low"]]  # Set log transmission priority.
    max_log_rate: NotRequired[int]  # FortiCloud maximum log rate in MBps (0 = unlimited).
    access_config: NotRequired[Literal["enable", "disable"]]  # Enable/disable FortiCloud access to configuration and data.


class FortiguardOverrideSetting:
    """
    Override global FortiCloud logging settings for this VDOM.
    
    Path: log/fortiguard_override_setting
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
        payload_dict: FortiguardOverrideSettingPayload | None = ...,
        override: Literal["enable", "disable"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        upload_option: Literal["store-and-upload", "realtime", "1-minute", "5-minute"] | None = ...,
        upload_interval: Literal["daily", "weekly", "monthly"] | None = ...,
        upload_day: str | None = ...,
        upload_time: str | None = ...,
        priority: Literal["default", "low"] | None = ...,
        max_log_rate: int | None = ...,
        access_config: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: FortiguardOverrideSettingPayload | None = ...,
        override: Literal["enable", "disable"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        upload_option: Literal["store-and-upload", "realtime", "1-minute", "5-minute"] | None = ...,
        upload_interval: Literal["daily", "weekly", "monthly"] | None = ...,
        upload_day: str | None = ...,
        upload_time: str | None = ...,
        priority: Literal["default", "low"] | None = ...,
        max_log_rate: int | None = ...,
        access_config: Literal["enable", "disable"] | None = ...,
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
        payload_dict: FortiguardOverrideSettingPayload | None = ...,
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