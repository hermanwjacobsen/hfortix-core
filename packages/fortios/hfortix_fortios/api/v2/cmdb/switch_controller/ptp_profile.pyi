from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class PtpProfilePayload(TypedDict, total=False):
    """
    Type hints for switch-controller/ptp_profile payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: PtpProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Profile name.
    description: NotRequired[str]  # Description.
    mode: NotRequired[Literal["transparent-e2e", "transparent-p2p"]]  # Select PTP mode.
    ptp_profile: NotRequired[Literal["C37.238-2017"]]  # Configure PTP power profile.
    transport: NotRequired[Literal["l2-mcast"]]  # Configure PTP transport mode.
    domain: NotRequired[int]  # Configure PTP domain value (0 - 255, default = 254).
    pdelay_req_interval: NotRequired[Literal["1sec", "2sec", "4sec", "8sec", "16sec", "32sec"]]  # Configure PTP peer delay request interval.


class PtpProfile:
    """
    Global PTP profile.
    
    Path: switch-controller/ptp_profile
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
        payload_dict: PtpProfilePayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        mode: Literal["transparent-e2e", "transparent-p2p"] | None = ...,
        ptp_profile: Literal["C37.238-2017"] | None = ...,
        transport: Literal["l2-mcast"] | None = ...,
        domain: int | None = ...,
        pdelay_req_interval: Literal["1sec", "2sec", "4sec", "8sec", "16sec", "32sec"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: PtpProfilePayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        mode: Literal["transparent-e2e", "transparent-p2p"] | None = ...,
        ptp_profile: Literal["C37.238-2017"] | None = ...,
        transport: Literal["l2-mcast"] | None = ...,
        domain: int | None = ...,
        pdelay_req_interval: Literal["1sec", "2sec", "4sec", "8sec", "16sec", "32sec"] | None = ...,
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
        payload_dict: PtpProfilePayload | None = ...,
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