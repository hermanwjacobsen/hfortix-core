from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class CustomPayload(TypedDict, total=False):
    """
    Type hints for ips/custom payload fields.
    
    Configure IPS custom signature.
    
    **Usage:**
        payload: CustomPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    tag: NotRequired[str]  # Signature tag.
    signature: NotRequired[str]  # Custom signature enclosed in single quotes.
    rule_id: NotRequired[int]  # Signature ID.
    severity: NotRequired[str]  # Relative severity of the signature, from info to critical. L
    location: NotRequired[list[dict[str, Any]]]  # Protect client or server traffic.
    os: NotRequired[list[dict[str, Any]]]  # Operating system(s) that the signature protects. Blank for a
    application: NotRequired[list[dict[str, Any]]]  # Applications to be protected. Blank for all applications.
    protocol: NotRequired[str]  # Protocol(s) that the signature scans. Blank for all protocol
    status: NotRequired[Literal["disable", "enable"]]  # Enable/disable this signature.
    log: NotRequired[Literal["disable", "enable"]]  # Enable/disable logging.
    log_packet: NotRequired[Literal["disable", "enable"]]  # Enable/disable packet logging.
    action: NotRequired[Literal["pass", "block"]]  # Default action (pass or block) for this signature.
    comment: NotRequired[str]  # Comment.

# Nested classes for table field children


# Response TypedDict for GET returns (all fields present in API response)
class CustomResponse(TypedDict):
    """
    Type hints for ips/custom API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    tag: str
    signature: str
    rule_id: int
    severity: str
    location: list[dict[str, Any]]
    os: list[dict[str, Any]]
    application: list[dict[str, Any]]
    protocol: str
    status: Literal["disable", "enable"]
    log: Literal["disable", "enable"]
    log_packet: Literal["disable", "enable"]
    action: Literal["pass", "block"]
    comment: str


@final
class CustomObject:
    """Typed FortiObject for ips/custom with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Signature tag.
    tag: str
    # Custom signature enclosed in single quotes.
    signature: str
    # Signature ID.
    rule_id: int
    # Relative severity of the signature, from info to critical. Log messages generate
    severity: str
    # Protect client or server traffic.
    location: list[dict[str, Any]]  # Multi-value field
    # Operating system(s) that the signature protects. Blank for all operating systems
    os: list[dict[str, Any]]  # Multi-value field
    # Applications to be protected. Blank for all applications.
    application: list[dict[str, Any]]  # Multi-value field
    # Protocol(s) that the signature scans. Blank for all protocols.
    protocol: str
    # Enable/disable this signature.
    status: Literal["disable", "enable"]
    # Enable/disable logging.
    log: Literal["disable", "enable"]
    # Enable/disable packet logging.
    log_packet: Literal["disable", "enable"]
    # Default action (pass or block) for this signature.
    action: Literal["pass", "block"]
    # Comment.
    comment: str
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> CustomPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Custom:
    """
    Configure IPS custom signature.
    
    Path: ips/custom
    Category: cmdb
    Primary Key: tag
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey/name provided as positional arg)
    @overload
    def get(
        self,
        tag: str,
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
    ) -> CustomObject: ...
    
    # Single object (mkey/name provided as keyword arg)
    @overload
    def get(
        self,
        *,
        tag: str,
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
    ) -> CustomObject: ...
    
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
    ) -> list[CustomObject]: ...
    
    @overload
    def get(
        self,
        tag: str | None = ...,
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
        tag: str,
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
    ) -> CustomResponse: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
        tag: str,
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
    ) -> CustomResponse: ...
    
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
    ) -> list[CustomResponse]: ...
    
    # Default overload for dict mode
    @overload
    def get(
        self,
        tag: str | None = ...,
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
        tag: str | None = ...,
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
    ) -> CustomObject | list[CustomObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: CustomPayload | None = ...,
        tag: str | None = ...,
        signature: str | None = ...,
        rule_id: int | None = ...,
        severity: str | None = ...,
        location: str | list[str] | None = ...,
        os: str | list[str] | None = ...,
        application: str | list[str] | None = ...,
        protocol: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        log: Literal["disable", "enable"] | None = ...,
        log_packet: Literal["disable", "enable"] | None = ...,
        action: Literal["pass", "block"] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> CustomObject: ...
    
    @overload
    def post(
        self,
        payload_dict: CustomPayload | None = ...,
        tag: str | None = ...,
        signature: str | None = ...,
        rule_id: int | None = ...,
        severity: str | None = ...,
        location: str | list[str] | None = ...,
        os: str | list[str] | None = ...,
        application: str | list[str] | None = ...,
        protocol: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        log: Literal["disable", "enable"] | None = ...,
        log_packet: Literal["disable", "enable"] | None = ...,
        action: Literal["pass", "block"] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: CustomPayload | None = ...,
        tag: str | None = ...,
        signature: str | None = ...,
        rule_id: int | None = ...,
        severity: str | None = ...,
        location: str | list[str] | None = ...,
        os: str | list[str] | None = ...,
        application: str | list[str] | None = ...,
        protocol: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        log: Literal["disable", "enable"] | None = ...,
        log_packet: Literal["disable", "enable"] | None = ...,
        action: Literal["pass", "block"] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: CustomPayload | None = ...,
        tag: str | None = ...,
        signature: str | None = ...,
        rule_id: int | None = ...,
        severity: str | None = ...,
        location: str | list[str] | None = ...,
        os: str | list[str] | None = ...,
        application: str | list[str] | None = ...,
        protocol: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        log: Literal["disable", "enable"] | None = ...,
        log_packet: Literal["disable", "enable"] | None = ...,
        action: Literal["pass", "block"] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: CustomPayload | None = ...,
        tag: str | None = ...,
        signature: str | None = ...,
        rule_id: int | None = ...,
        severity: str | None = ...,
        location: str | list[str] | None = ...,
        os: str | list[str] | None = ...,
        application: str | list[str] | None = ...,
        protocol: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        log: Literal["disable", "enable"] | None = ...,
        log_packet: Literal["disable", "enable"] | None = ...,
        action: Literal["pass", "block"] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> CustomObject: ...
    
    @overload
    def put(
        self,
        payload_dict: CustomPayload | None = ...,
        tag: str | None = ...,
        signature: str | None = ...,
        rule_id: int | None = ...,
        severity: str | None = ...,
        location: str | list[str] | None = ...,
        os: str | list[str] | None = ...,
        application: str | list[str] | None = ...,
        protocol: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        log: Literal["disable", "enable"] | None = ...,
        log_packet: Literal["disable", "enable"] | None = ...,
        action: Literal["pass", "block"] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: CustomPayload | None = ...,
        tag: str | None = ...,
        signature: str | None = ...,
        rule_id: int | None = ...,
        severity: str | None = ...,
        location: str | list[str] | None = ...,
        os: str | list[str] | None = ...,
        application: str | list[str] | None = ...,
        protocol: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        log: Literal["disable", "enable"] | None = ...,
        log_packet: Literal["disable", "enable"] | None = ...,
        action: Literal["pass", "block"] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: CustomPayload | None = ...,
        tag: str | None = ...,
        signature: str | None = ...,
        rule_id: int | None = ...,
        severity: str | None = ...,
        location: str | list[str] | None = ...,
        os: str | list[str] | None = ...,
        application: str | list[str] | None = ...,
        protocol: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        log: Literal["disable", "enable"] | None = ...,
        log_packet: Literal["disable", "enable"] | None = ...,
        action: Literal["pass", "block"] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        tag: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> CustomObject: ...
    
    @overload
    def delete(
        self,
        tag: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def delete(
        self,
        tag: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def delete(
        self,
        tag: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        tag: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: CustomPayload | None = ...,
        tag: str | None = ...,
        signature: str | None = ...,
        rule_id: int | None = ...,
        severity: str | None = ...,
        location: str | list[str] | None = ...,
        os: str | list[str] | None = ...,
        application: str | list[str] | None = ...,
        protocol: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        log: Literal["disable", "enable"] | None = ...,
        log_packet: Literal["disable", "enable"] | None = ...,
        action: Literal["pass", "block"] | None = ...,
        comment: str | None = ...,
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
    "Custom",
    "CustomPayload",
    "CustomObject",
]