from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class ProfilePayload(TypedDict, total=False):
    """
    Type hints for switch_controller/ptp/profile payload fields.
    
    Global PTP profile.
    
    **Usage:**
        payload: ProfilePayload = {
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


class ProfileObject(FortiObject[ProfilePayload]):
    """Typed FortiObject for switch_controller/ptp/profile with IDE autocomplete support."""
    
    # Profile name.
    name: str
    # Description.
    description: str
    # Select PTP mode.
    mode: Literal["transparent-e2e", "transparent-p2p"]
    # Configure PTP power profile.
    ptp_profile: Literal["C37.238-2017"]
    # Configure PTP transport mode.
    transport: Literal["l2-mcast"]
    # Configure PTP domain value (0 - 255, default = 254).
    domain: int
    # Configure PTP peer delay request interval.
    pdelay_req_interval: Literal["1sec", "2sec", "4sec", "8sec", "16sec", "32sec"]
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> ProfilePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Profile:
    """
    Global PTP profile.
    
    Path: switch_controller/ptp/profile
    Category: cmdb
    Primary Key: name
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey provided)
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
        *,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> ProfileObject: ...
    
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
        raw_json: Literal[True],
        *,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Dict mode with mkey provided (single dict)
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
    ) -> dict[str, Any]: ...
    
    # Dict mode without mkey (returns dict with results array)
    @overload
    def get(
        self,
        name: None = None,
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
        description: str | None = ...,
        mode: Literal["transparent-e2e", "transparent-p2p"] | None = ...,
        ptp_profile: Literal["C37.238-2017"] | None = ...,
        transport: Literal["l2-mcast"] | None = ...,
        domain: int | None = ...,
        pdelay_req_interval: Literal["1sec", "2sec", "4sec", "8sec", "16sec", "32sec"] | None = ...,
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
        description: str | None = ...,
        mode: Literal["transparent-e2e", "transparent-p2p"] | None = ...,
        ptp_profile: Literal["C37.238-2017"] | None = ...,
        transport: Literal["l2-mcast"] | None = ...,
        domain: int | None = ...,
        pdelay_req_interval: Literal["1sec", "2sec", "4sec", "8sec", "16sec", "32sec"] | None = ...,
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
        description: str | None = ...,
        mode: Literal["transparent-e2e", "transparent-p2p"] | None = ...,
        ptp_profile: Literal["C37.238-2017"] | None = ...,
        transport: Literal["l2-mcast"] | None = ...,
        domain: int | None = ...,
        pdelay_req_interval: Literal["1sec", "2sec", "4sec", "8sec", "16sec", "32sec"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        mode: Literal["transparent-e2e", "transparent-p2p"] | None = ...,
        ptp_profile: Literal["C37.238-2017"] | None = ...,
        transport: Literal["l2-mcast"] | None = ...,
        domain: int | None = ...,
        pdelay_req_interval: Literal["1sec", "2sec", "4sec", "8sec", "16sec", "32sec"] | None = ...,
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
        description: str | None = ...,
        mode: Literal["transparent-e2e", "transparent-p2p"] | None = ...,
        ptp_profile: Literal["C37.238-2017"] | None = ...,
        transport: Literal["l2-mcast"] | None = ...,
        domain: int | None = ...,
        pdelay_req_interval: Literal["1sec", "2sec", "4sec", "8sec", "16sec", "32sec"] | None = ...,
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
        description: str | None = ...,
        mode: Literal["transparent-e2e", "transparent-p2p"] | None = ...,
        ptp_profile: Literal["C37.238-2017"] | None = ...,
        transport: Literal["l2-mcast"] | None = ...,
        domain: int | None = ...,
        pdelay_req_interval: Literal["1sec", "2sec", "4sec", "8sec", "16sec", "32sec"] | None = ...,
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
        description: str | None = ...,
        mode: Literal["transparent-e2e", "transparent-p2p"] | None = ...,
        ptp_profile: Literal["C37.238-2017"] | None = ...,
        transport: Literal["l2-mcast"] | None = ...,
        domain: int | None = ...,
        pdelay_req_interval: Literal["1sec", "2sec", "4sec", "8sec", "16sec", "32sec"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        mode: Literal["transparent-e2e", "transparent-p2p"] | None = ...,
        ptp_profile: Literal["C37.238-2017"] | None = ...,
        transport: Literal["l2-mcast"] | None = ...,
        domain: int | None = ...,
        pdelay_req_interval: Literal["1sec", "2sec", "4sec", "8sec", "16sec", "32sec"] | None = ...,
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
        description: str | None = ...,
        mode: Literal["transparent-e2e", "transparent-p2p"] | None = ...,
        ptp_profile: Literal["C37.238-2017"] | None = ...,
        transport: Literal["l2-mcast"] | None = ...,
        domain: int | None = ...,
        pdelay_req_interval: Literal["1sec", "2sec", "4sec", "8sec", "16sec", "32sec"] | None = ...,
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