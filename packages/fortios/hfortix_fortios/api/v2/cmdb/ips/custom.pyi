from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class CustomPayload(TypedDict, total=False):
    """
    Type hints for ips/custom payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: CustomPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    tag: NotRequired[str]  # Signature tag.
    signature: NotRequired[str]  # Custom signature enclosed in single quotes.
    rule_id: NotRequired[int]  # Signature ID.
    severity: NotRequired[str]  # Relative severity of the signature, from info to critical. L
    location: NotRequired[str]  # Protect client or server traffic.
    os: NotRequired[str]  # Operating system(s) that the signature protects. Blank for a
    application: NotRequired[str]  # Applications to be protected. Blank for all applications.
    protocol: NotRequired[str]  # Protocol(s) that the signature scans. Blank for all protocol
    status: NotRequired[Literal["disable", "enable"]]  # Enable/disable this signature.
    log: NotRequired[Literal["disable", "enable"]]  # Enable/disable logging.
    log_packet: NotRequired[Literal["disable", "enable"]]  # Enable/disable packet logging.
    action: NotRequired[Literal["pass", "block"]]  # Default action (pass or block) for this signature.
    comment: NotRequired[str]  # Comment.


class Custom:
    """
    Configure IPS custom signature.
    
    Path: ips/custom
    Category: cmdb
    Primary Key: tag
    """
    
    def get(
        self,
        tag: str | None = ...,
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
        payload_dict: CustomPayload | None = ...,
        tag: str | None = ...,
        signature: str | None = ...,
        rule_id: int | None = ...,
        severity: str | None = ...,
        location: str | None = ...,
        os: str | None = ...,
        application: str | None = ...,
        protocol: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        log: Literal["disable", "enable"] | None = ...,
        log_packet: Literal["disable", "enable"] | None = ...,
        action: Literal["pass", "block"] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: CustomPayload | None = ...,
        tag: str | None = ...,
        signature: str | None = ...,
        rule_id: int | None = ...,
        severity: str | None = ...,
        location: str | None = ...,
        os: str | None = ...,
        application: str | None = ...,
        protocol: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        log: Literal["disable", "enable"] | None = ...,
        log_packet: Literal["disable", "enable"] | None = ...,
        action: Literal["pass", "block"] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def delete(
        self,
        tag: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def exists(
        self,
        tag: str,
        vdom: str | bool | None = ...,
    ) -> Union[bool, Coroutine[Any, Any, bool]]: ...
    
    def set(
        self,
        payload_dict: CustomPayload | None = ...,
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