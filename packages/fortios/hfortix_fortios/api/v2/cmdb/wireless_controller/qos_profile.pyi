from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class QosProfilePayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/qos_profile payload fields.
    
    Configure WiFi quality of service (QoS) profiles.
    
    **Usage:**
        payload: QosProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # WiFi QoS profile name.
    comment: NotRequired[str]  # Comment.
    uplink: NotRequired[int]  # Maximum uplink bandwidth for Virtual Access Points (VAPs)
    downlink: NotRequired[int]  # Maximum downlink bandwidth for Virtual Access Points (VAPs)
    uplink_sta: NotRequired[int]  # Maximum uplink bandwidth for clients
    downlink_sta: NotRequired[int]  # Maximum downlink bandwidth for clients
    burst: NotRequired[Literal["enable", "disable"]]  # Enable/disable client rate burst.
    wmm: NotRequired[Literal["enable", "disable"]]  # Enable/disable WiFi multi-media (WMM) control.
    wmm_uapsd: NotRequired[Literal["enable", "disable"]]  # Enable/disable WMM Unscheduled Automatic Power Save Delivery
    call_admission_control: NotRequired[Literal["enable", "disable"]]  # Enable/disable WMM call admission control.
    call_capacity: NotRequired[int]  # Maximum number of Voice over WLAN (VoWLAN) phones allowed
    bandwidth_admission_control: NotRequired[Literal["enable", "disable"]]  # Enable/disable WMM bandwidth admission control.
    bandwidth_capacity: NotRequired[int]  # Maximum bandwidth capacity allowed
    dscp_wmm_mapping: NotRequired[Literal["enable", "disable"]]  # Enable/disable Differentiated Services Code Point (DSCP) map
    dscp_wmm_vo: NotRequired[list[dict[str, Any]]]  # DSCP mapping for voice access (default = 48 56).
    dscp_wmm_vi: NotRequired[list[dict[str, Any]]]  # DSCP mapping for video access (default = 32 40).
    dscp_wmm_be: NotRequired[list[dict[str, Any]]]  # DSCP mapping for best effort access (default = 0 24).
    dscp_wmm_bk: NotRequired[list[dict[str, Any]]]  # DSCP mapping for background access (default = 8 16).
    wmm_dscp_marking: NotRequired[Literal["enable", "disable"]]  # Enable/disable WMM Differentiated Services Code Point (DSCP)
    wmm_vo_dscp: NotRequired[int]  # DSCP marking for voice access (default = 48).
    wmm_vi_dscp: NotRequired[int]  # DSCP marking for video access (default = 32).
    wmm_be_dscp: NotRequired[int]  # DSCP marking for best effort access (default = 0).
    wmm_bk_dscp: NotRequired[int]  # DSCP marking for background access (default = 8).

# Nested classes for table field children

@final
class QosProfileDscpwmmvoObject:
    """Typed object for dscp-wmm-vo table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # DSCP WMM mapping numbers (0 - 63).
    id: int
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class QosProfileDscpwmmviObject:
    """Typed object for dscp-wmm-vi table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # DSCP WMM mapping numbers (0 - 63).
    id: int
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class QosProfileDscpwmmbeObject:
    """Typed object for dscp-wmm-be table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # DSCP WMM mapping numbers (0 - 63).
    id: int
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class QosProfileDscpwmmbkObject:
    """Typed object for dscp-wmm-bk table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # DSCP WMM mapping numbers (0 - 63).
    id: int
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class QosProfileResponse(TypedDict):
    """
    Type hints for wireless_controller/qos_profile API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    comment: str
    uplink: int
    downlink: int
    uplink_sta: int
    downlink_sta: int
    burst: Literal["enable", "disable"]
    wmm: Literal["enable", "disable"]
    wmm_uapsd: Literal["enable", "disable"]
    call_admission_control: Literal["enable", "disable"]
    call_capacity: int
    bandwidth_admission_control: Literal["enable", "disable"]
    bandwidth_capacity: int
    dscp_wmm_mapping: Literal["enable", "disable"]
    dscp_wmm_vo: list[dict[str, Any]]
    dscp_wmm_vi: list[dict[str, Any]]
    dscp_wmm_be: list[dict[str, Any]]
    dscp_wmm_bk: list[dict[str, Any]]
    wmm_dscp_marking: Literal["enable", "disable"]
    wmm_vo_dscp: int
    wmm_vi_dscp: int
    wmm_be_dscp: int
    wmm_bk_dscp: int


@final
class QosProfileObject:
    """Typed FortiObject for wireless_controller/qos_profile with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # WiFi QoS profile name.
    name: str
    # Comment.
    comment: str
    # Maximum uplink bandwidth for Virtual Access Points (VAPs)
    uplink: int
    # Maximum downlink bandwidth for Virtual Access Points (VAPs)
    downlink: int
    # Maximum uplink bandwidth for clients
    uplink_sta: int
    # Maximum downlink bandwidth for clients
    downlink_sta: int
    # Enable/disable client rate burst.
    burst: Literal["enable", "disable"]
    # Enable/disable WiFi multi-media (WMM) control.
    wmm: Literal["enable", "disable"]
    # Enable/disable WMM Unscheduled Automatic Power Save Delivery (U-APSD) power save
    wmm_uapsd: Literal["enable", "disable"]
    # Enable/disable WMM call admission control.
    call_admission_control: Literal["enable", "disable"]
    # Maximum number of Voice over WLAN (VoWLAN) phones allowed (0 - 60, default = 10)
    call_capacity: int
    # Enable/disable WMM bandwidth admission control.
    bandwidth_admission_control: Literal["enable", "disable"]
    # Maximum bandwidth capacity allowed (1 - 600000 Kbps, default = 2000).
    bandwidth_capacity: int
    # Enable/disable Differentiated Services Code Point (DSCP) mapping.
    dscp_wmm_mapping: Literal["enable", "disable"]
    # DSCP mapping for voice access (default = 48 56).
    dscp_wmm_vo: list[QosProfileDscpwmmvoObject]  # Table field - list of typed objects
    # DSCP mapping for video access (default = 32 40).
    dscp_wmm_vi: list[QosProfileDscpwmmviObject]  # Table field - list of typed objects
    # DSCP mapping for best effort access (default = 0 24).
    dscp_wmm_be: list[QosProfileDscpwmmbeObject]  # Table field - list of typed objects
    # DSCP mapping for background access (default = 8 16).
    dscp_wmm_bk: list[QosProfileDscpwmmbkObject]  # Table field - list of typed objects
    # Enable/disable WMM Differentiated Services Code Point (DSCP) marking.
    wmm_dscp_marking: Literal["enable", "disable"]
    # DSCP marking for voice access (default = 48).
    wmm_vo_dscp: int
    # DSCP marking for video access (default = 32).
    wmm_vi_dscp: int
    # DSCP marking for best effort access (default = 0).
    wmm_be_dscp: int
    # DSCP marking for background access (default = 8).
    wmm_bk_dscp: int
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> QosProfilePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class QosProfile:
    """
    Configure WiFi quality of service (QoS) profiles.
    
    Path: wireless_controller/qos_profile
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
    ) -> QosProfileObject: ...
    
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
    ) -> QosProfileObject: ...
    
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
    ) -> list[QosProfileObject]: ...
    
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
    ) -> QosProfileResponse: ...
    
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
    ) -> QosProfileResponse: ...
    
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
    ) -> list[QosProfileResponse]: ...
    
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
    ) -> QosProfileObject | list[QosProfileObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: QosProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        uplink: int | None = ...,
        downlink: int | None = ...,
        uplink_sta: int | None = ...,
        downlink_sta: int | None = ...,
        burst: Literal["enable", "disable"] | None = ...,
        wmm: Literal["enable", "disable"] | None = ...,
        wmm_uapsd: Literal["enable", "disable"] | None = ...,
        call_admission_control: Literal["enable", "disable"] | None = ...,
        call_capacity: int | None = ...,
        bandwidth_admission_control: Literal["enable", "disable"] | None = ...,
        bandwidth_capacity: int | None = ...,
        dscp_wmm_mapping: Literal["enable", "disable"] | None = ...,
        dscp_wmm_vo: str | list[str] | list[dict[str, Any]] | None = ...,
        dscp_wmm_vi: str | list[str] | list[dict[str, Any]] | None = ...,
        dscp_wmm_be: str | list[str] | list[dict[str, Any]] | None = ...,
        dscp_wmm_bk: str | list[str] | list[dict[str, Any]] | None = ...,
        wmm_dscp_marking: Literal["enable", "disable"] | None = ...,
        wmm_vo_dscp: int | None = ...,
        wmm_vi_dscp: int | None = ...,
        wmm_be_dscp: int | None = ...,
        wmm_bk_dscp: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> QosProfileObject: ...
    
    @overload
    def post(
        self,
        payload_dict: QosProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        uplink: int | None = ...,
        downlink: int | None = ...,
        uplink_sta: int | None = ...,
        downlink_sta: int | None = ...,
        burst: Literal["enable", "disable"] | None = ...,
        wmm: Literal["enable", "disable"] | None = ...,
        wmm_uapsd: Literal["enable", "disable"] | None = ...,
        call_admission_control: Literal["enable", "disable"] | None = ...,
        call_capacity: int | None = ...,
        bandwidth_admission_control: Literal["enable", "disable"] | None = ...,
        bandwidth_capacity: int | None = ...,
        dscp_wmm_mapping: Literal["enable", "disable"] | None = ...,
        dscp_wmm_vo: str | list[str] | list[dict[str, Any]] | None = ...,
        dscp_wmm_vi: str | list[str] | list[dict[str, Any]] | None = ...,
        dscp_wmm_be: str | list[str] | list[dict[str, Any]] | None = ...,
        dscp_wmm_bk: str | list[str] | list[dict[str, Any]] | None = ...,
        wmm_dscp_marking: Literal["enable", "disable"] | None = ...,
        wmm_vo_dscp: int | None = ...,
        wmm_vi_dscp: int | None = ...,
        wmm_be_dscp: int | None = ...,
        wmm_bk_dscp: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: QosProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        uplink: int | None = ...,
        downlink: int | None = ...,
        uplink_sta: int | None = ...,
        downlink_sta: int | None = ...,
        burst: Literal["enable", "disable"] | None = ...,
        wmm: Literal["enable", "disable"] | None = ...,
        wmm_uapsd: Literal["enable", "disable"] | None = ...,
        call_admission_control: Literal["enable", "disable"] | None = ...,
        call_capacity: int | None = ...,
        bandwidth_admission_control: Literal["enable", "disable"] | None = ...,
        bandwidth_capacity: int | None = ...,
        dscp_wmm_mapping: Literal["enable", "disable"] | None = ...,
        dscp_wmm_vo: str | list[str] | list[dict[str, Any]] | None = ...,
        dscp_wmm_vi: str | list[str] | list[dict[str, Any]] | None = ...,
        dscp_wmm_be: str | list[str] | list[dict[str, Any]] | None = ...,
        dscp_wmm_bk: str | list[str] | list[dict[str, Any]] | None = ...,
        wmm_dscp_marking: Literal["enable", "disable"] | None = ...,
        wmm_vo_dscp: int | None = ...,
        wmm_vi_dscp: int | None = ...,
        wmm_be_dscp: int | None = ...,
        wmm_bk_dscp: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: QosProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        uplink: int | None = ...,
        downlink: int | None = ...,
        uplink_sta: int | None = ...,
        downlink_sta: int | None = ...,
        burst: Literal["enable", "disable"] | None = ...,
        wmm: Literal["enable", "disable"] | None = ...,
        wmm_uapsd: Literal["enable", "disable"] | None = ...,
        call_admission_control: Literal["enable", "disable"] | None = ...,
        call_capacity: int | None = ...,
        bandwidth_admission_control: Literal["enable", "disable"] | None = ...,
        bandwidth_capacity: int | None = ...,
        dscp_wmm_mapping: Literal["enable", "disable"] | None = ...,
        dscp_wmm_vo: str | list[str] | list[dict[str, Any]] | None = ...,
        dscp_wmm_vi: str | list[str] | list[dict[str, Any]] | None = ...,
        dscp_wmm_be: str | list[str] | list[dict[str, Any]] | None = ...,
        dscp_wmm_bk: str | list[str] | list[dict[str, Any]] | None = ...,
        wmm_dscp_marking: Literal["enable", "disable"] | None = ...,
        wmm_vo_dscp: int | None = ...,
        wmm_vi_dscp: int | None = ...,
        wmm_be_dscp: int | None = ...,
        wmm_bk_dscp: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: QosProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        uplink: int | None = ...,
        downlink: int | None = ...,
        uplink_sta: int | None = ...,
        downlink_sta: int | None = ...,
        burst: Literal["enable", "disable"] | None = ...,
        wmm: Literal["enable", "disable"] | None = ...,
        wmm_uapsd: Literal["enable", "disable"] | None = ...,
        call_admission_control: Literal["enable", "disable"] | None = ...,
        call_capacity: int | None = ...,
        bandwidth_admission_control: Literal["enable", "disable"] | None = ...,
        bandwidth_capacity: int | None = ...,
        dscp_wmm_mapping: Literal["enable", "disable"] | None = ...,
        dscp_wmm_vo: str | list[str] | list[dict[str, Any]] | None = ...,
        dscp_wmm_vi: str | list[str] | list[dict[str, Any]] | None = ...,
        dscp_wmm_be: str | list[str] | list[dict[str, Any]] | None = ...,
        dscp_wmm_bk: str | list[str] | list[dict[str, Any]] | None = ...,
        wmm_dscp_marking: Literal["enable", "disable"] | None = ...,
        wmm_vo_dscp: int | None = ...,
        wmm_vi_dscp: int | None = ...,
        wmm_be_dscp: int | None = ...,
        wmm_bk_dscp: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> QosProfileObject: ...
    
    @overload
    def put(
        self,
        payload_dict: QosProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        uplink: int | None = ...,
        downlink: int | None = ...,
        uplink_sta: int | None = ...,
        downlink_sta: int | None = ...,
        burst: Literal["enable", "disable"] | None = ...,
        wmm: Literal["enable", "disable"] | None = ...,
        wmm_uapsd: Literal["enable", "disable"] | None = ...,
        call_admission_control: Literal["enable", "disable"] | None = ...,
        call_capacity: int | None = ...,
        bandwidth_admission_control: Literal["enable", "disable"] | None = ...,
        bandwidth_capacity: int | None = ...,
        dscp_wmm_mapping: Literal["enable", "disable"] | None = ...,
        dscp_wmm_vo: str | list[str] | list[dict[str, Any]] | None = ...,
        dscp_wmm_vi: str | list[str] | list[dict[str, Any]] | None = ...,
        dscp_wmm_be: str | list[str] | list[dict[str, Any]] | None = ...,
        dscp_wmm_bk: str | list[str] | list[dict[str, Any]] | None = ...,
        wmm_dscp_marking: Literal["enable", "disable"] | None = ...,
        wmm_vo_dscp: int | None = ...,
        wmm_vi_dscp: int | None = ...,
        wmm_be_dscp: int | None = ...,
        wmm_bk_dscp: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: QosProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        uplink: int | None = ...,
        downlink: int | None = ...,
        uplink_sta: int | None = ...,
        downlink_sta: int | None = ...,
        burst: Literal["enable", "disable"] | None = ...,
        wmm: Literal["enable", "disable"] | None = ...,
        wmm_uapsd: Literal["enable", "disable"] | None = ...,
        call_admission_control: Literal["enable", "disable"] | None = ...,
        call_capacity: int | None = ...,
        bandwidth_admission_control: Literal["enable", "disable"] | None = ...,
        bandwidth_capacity: int | None = ...,
        dscp_wmm_mapping: Literal["enable", "disable"] | None = ...,
        dscp_wmm_vo: str | list[str] | list[dict[str, Any]] | None = ...,
        dscp_wmm_vi: str | list[str] | list[dict[str, Any]] | None = ...,
        dscp_wmm_be: str | list[str] | list[dict[str, Any]] | None = ...,
        dscp_wmm_bk: str | list[str] | list[dict[str, Any]] | None = ...,
        wmm_dscp_marking: Literal["enable", "disable"] | None = ...,
        wmm_vo_dscp: int | None = ...,
        wmm_vi_dscp: int | None = ...,
        wmm_be_dscp: int | None = ...,
        wmm_bk_dscp: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: QosProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        uplink: int | None = ...,
        downlink: int | None = ...,
        uplink_sta: int | None = ...,
        downlink_sta: int | None = ...,
        burst: Literal["enable", "disable"] | None = ...,
        wmm: Literal["enable", "disable"] | None = ...,
        wmm_uapsd: Literal["enable", "disable"] | None = ...,
        call_admission_control: Literal["enable", "disable"] | None = ...,
        call_capacity: int | None = ...,
        bandwidth_admission_control: Literal["enable", "disable"] | None = ...,
        bandwidth_capacity: int | None = ...,
        dscp_wmm_mapping: Literal["enable", "disable"] | None = ...,
        dscp_wmm_vo: str | list[str] | list[dict[str, Any]] | None = ...,
        dscp_wmm_vi: str | list[str] | list[dict[str, Any]] | None = ...,
        dscp_wmm_be: str | list[str] | list[dict[str, Any]] | None = ...,
        dscp_wmm_bk: str | list[str] | list[dict[str, Any]] | None = ...,
        wmm_dscp_marking: Literal["enable", "disable"] | None = ...,
        wmm_vo_dscp: int | None = ...,
        wmm_vi_dscp: int | None = ...,
        wmm_be_dscp: int | None = ...,
        wmm_bk_dscp: int | None = ...,
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
    ) -> QosProfileObject: ...
    
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
        payload_dict: QosProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        uplink: int | None = ...,
        downlink: int | None = ...,
        uplink_sta: int | None = ...,
        downlink_sta: int | None = ...,
        burst: Literal["enable", "disable"] | None = ...,
        wmm: Literal["enable", "disable"] | None = ...,
        wmm_uapsd: Literal["enable", "disable"] | None = ...,
        call_admission_control: Literal["enable", "disable"] | None = ...,
        call_capacity: int | None = ...,
        bandwidth_admission_control: Literal["enable", "disable"] | None = ...,
        bandwidth_capacity: int | None = ...,
        dscp_wmm_mapping: Literal["enable", "disable"] | None = ...,
        dscp_wmm_vo: str | list[str] | list[dict[str, Any]] | None = ...,
        dscp_wmm_vi: str | list[str] | list[dict[str, Any]] | None = ...,
        dscp_wmm_be: str | list[str] | list[dict[str, Any]] | None = ...,
        dscp_wmm_bk: str | list[str] | list[dict[str, Any]] | None = ...,
        wmm_dscp_marking: Literal["enable", "disable"] | None = ...,
        wmm_vo_dscp: int | None = ...,
        wmm_vi_dscp: int | None = ...,
        wmm_be_dscp: int | None = ...,
        wmm_bk_dscp: int | None = ...,
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
    "QosProfile",
    "QosProfilePayload",
    "QosProfileObject",
]