from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class ProfilePayload(TypedDict, total=False):
    """
    Type hints for diameter_filter/profile payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: ProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Profile name.
    comment: NotRequired[str]  # Comment.
    monitor_all_messages: NotRequired[Literal["disable", "enable"]]  # Enable/disable logging for all User Name and Result Code AVP
    log_packet: NotRequired[Literal["disable", "enable"]]  # Enable/disable packet log for triggered diameter settings.
    track_requests_answers: NotRequired[Literal["disable", "enable"]]  # Enable/disable validation that each answer has a correspondi
    missing_request_action: NotRequired[Literal["allow", "block", "reset", "monitor"]]  # Action to be taken for answers without corresponding request
    protocol_version_invalid: NotRequired[Literal["allow", "block", "reset", "monitor"]]  # Action to be taken for invalid protocol version.
    message_length_invalid: NotRequired[Literal["allow", "block", "reset", "monitor"]]  # Action to be taken for invalid message length.
    request_error_flag_set: NotRequired[Literal["allow", "block", "reset", "monitor"]]  # Action to be taken for request messages with error flag set.
    cmd_flags_reserve_set: NotRequired[Literal["allow", "block", "reset", "monitor"]]  # Action to be taken for messages with cmd flag reserve bits s
    command_code_invalid: NotRequired[Literal["allow", "block", "reset", "monitor"]]  # Action to be taken for messages with invalid command code.
    command_code_range: NotRequired[str]  # Valid range for command codes (0-16777215).


class Profile:
    """
    Configure Diameter filter profiles.
    
    Path: diameter_filter/profile
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
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        monitor_all_messages: Literal["disable", "enable"] | None = ...,
        log_packet: Literal["disable", "enable"] | None = ...,
        track_requests_answers: Literal["disable", "enable"] | None = ...,
        missing_request_action: Literal["allow", "block", "reset", "monitor"] | None = ...,
        protocol_version_invalid: Literal["allow", "block", "reset", "monitor"] | None = ...,
        message_length_invalid: Literal["allow", "block", "reset", "monitor"] | None = ...,
        request_error_flag_set: Literal["allow", "block", "reset", "monitor"] | None = ...,
        cmd_flags_reserve_set: Literal["allow", "block", "reset", "monitor"] | None = ...,
        command_code_invalid: Literal["allow", "block", "reset", "monitor"] | None = ...,
        command_code_range: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        monitor_all_messages: Literal["disable", "enable"] | None = ...,
        log_packet: Literal["disable", "enable"] | None = ...,
        track_requests_answers: Literal["disable", "enable"] | None = ...,
        missing_request_action: Literal["allow", "block", "reset", "monitor"] | None = ...,
        protocol_version_invalid: Literal["allow", "block", "reset", "monitor"] | None = ...,
        message_length_invalid: Literal["allow", "block", "reset", "monitor"] | None = ...,
        request_error_flag_set: Literal["allow", "block", "reset", "monitor"] | None = ...,
        cmd_flags_reserve_set: Literal["allow", "block", "reset", "monitor"] | None = ...,
        command_code_invalid: Literal["allow", "block", "reset", "monitor"] | None = ...,
        command_code_range: str | None = ...,
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
        payload_dict: ProfilePayload | None = ...,
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