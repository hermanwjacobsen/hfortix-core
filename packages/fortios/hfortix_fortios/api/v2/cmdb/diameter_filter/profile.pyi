from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class ProfilePayload(TypedDict, total=False):
    """
    Type hints for diameter_filter/profile payload fields.
    
    Configure Diameter filter profiles.
    
    **Usage:**
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

# Nested classes for table field children


# Response TypedDict for GET returns (all fields present in API response)
class ProfileResponse(TypedDict):
    """
    Type hints for diameter_filter/profile API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    comment: str
    monitor_all_messages: Literal["disable", "enable"]
    log_packet: Literal["disable", "enable"]
    track_requests_answers: Literal["disable", "enable"]
    missing_request_action: Literal["allow", "block", "reset", "monitor"]
    protocol_version_invalid: Literal["allow", "block", "reset", "monitor"]
    message_length_invalid: Literal["allow", "block", "reset", "monitor"]
    request_error_flag_set: Literal["allow", "block", "reset", "monitor"]
    cmd_flags_reserve_set: Literal["allow", "block", "reset", "monitor"]
    command_code_invalid: Literal["allow", "block", "reset", "monitor"]
    command_code_range: str


@final
class ProfileObject:
    """Typed FortiObject for diameter_filter/profile with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Profile name.
    name: str
    # Comment.
    comment: str
    # Enable/disable logging for all User Name and Result Code AVP messages.
    monitor_all_messages: Literal["disable", "enable"]
    # Enable/disable packet log for triggered diameter settings.
    log_packet: Literal["disable", "enable"]
    # Enable/disable validation that each answer has a corresponding request.
    track_requests_answers: Literal["disable", "enable"]
    # Action to be taken for answers without corresponding request.
    missing_request_action: Literal["allow", "block", "reset", "monitor"]
    # Action to be taken for invalid protocol version.
    protocol_version_invalid: Literal["allow", "block", "reset", "monitor"]
    # Action to be taken for invalid message length.
    message_length_invalid: Literal["allow", "block", "reset", "monitor"]
    # Action to be taken for request messages with error flag set.
    request_error_flag_set: Literal["allow", "block", "reset", "monitor"]
    # Action to be taken for messages with cmd flag reserve bits set.
    cmd_flags_reserve_set: Literal["allow", "block", "reset", "monitor"]
    # Action to be taken for messages with invalid command code.
    command_code_invalid: Literal["allow", "block", "reset", "monitor"]
    # Valid range for command codes (0-16777215).
    command_code_range: str
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> ProfilePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Profile:
    """
    Configure Diameter filter profiles.
    
    Path: diameter_filter/profile
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
    ) -> ProfileObject: ...
    
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
    ) -> ProfileObject: ...
    
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
    ) -> list[ProfileObject]: ...
    
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
    ) -> ProfileResponse: ...
    
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
    ) -> ProfileResponse: ...
    
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
    ) -> list[ProfileResponse]: ...
    
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
    ) -> ProfileObject | list[ProfileObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ProfileObject: ...
    
    @overload
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
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
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ProfileObject: ...
    
    @overload
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
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
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
    ) -> ProfileObject: ...
    
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
    "Profile",
    "ProfilePayload",
    "ProfileObject",
]