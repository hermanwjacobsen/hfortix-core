from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class InterfacePolicy6Payload(TypedDict, total=False):
    """
    Type hints for firewall/interface_policy6 payload fields.
    
    Configure IPv6 interface policies.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.antivirus.profile.ProfileEndpoint` (via: av-profile)
        - :class:`~.application.list.ListEndpoint` (via: application-list)
        - :class:`~.casb.profile.ProfileEndpoint` (via: casb-profile)
        - :class:`~.dlp.profile.ProfileEndpoint` (via: dlp-profile)
        - :class:`~.emailfilter.profile.ProfileEndpoint` (via: emailfilter-profile)
        - :class:`~.ips.sensor.SensorEndpoint` (via: ips-sensor)
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface)
        - :class:`~.system.sdwan.zone.ZoneEndpoint` (via: interface)
        - :class:`~.system.zone.ZoneEndpoint` (via: interface)
        - :class:`~.webfilter.profile.ProfileEndpoint` (via: webfilter-profile)

    **Usage:**
        payload: InterfacePolicy6Payload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    policyid: NotRequired[int]  # Policy ID (0 - 4294967295).
    uuid: NotRequired[str]  # Universally Unique Identifier
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable this policy.
    comments: NotRequired[str]  # Comments.
    logtraffic: NotRequired[Literal["all", "utm", "disable"]]  # Logging type to be used in this policy
    interface: str  # Monitored interface name from available interfaces.
    srcaddr6: list[dict[str, Any]]  # IPv6 address object to limit traffic monitoring to network t
    dstaddr6: list[dict[str, Any]]  # IPv6 address object to limit traffic monitoring to network t
    service6: NotRequired[list[dict[str, Any]]]  # Service name.
    application_list_status: NotRequired[Literal["enable", "disable"]]  # Enable/disable application control.
    application_list: str  # Application list name.
    ips_sensor_status: NotRequired[Literal["enable", "disable"]]  # Enable/disable IPS.
    ips_sensor: str  # IPS sensor name.
    dsri: NotRequired[Literal["enable", "disable"]]  # Enable/disable DSRI.
    av_profile_status: NotRequired[Literal["enable", "disable"]]  # Enable/disable antivirus.
    av_profile: str  # Antivirus profile.
    webfilter_profile_status: NotRequired[Literal["enable", "disable"]]  # Enable/disable web filtering.
    webfilter_profile: str  # Web filter profile.
    casb_profile_status: NotRequired[Literal["enable", "disable"]]  # Enable/disable CASB.
    casb_profile: str  # CASB profile.
    emailfilter_profile_status: NotRequired[Literal["enable", "disable"]]  # Enable/disable email filter.
    emailfilter_profile: str  # Email filter profile.
    dlp_profile_status: NotRequired[Literal["enable", "disable"]]  # Enable/disable DLP.
    dlp_profile: str  # DLP profile name.

# Nested classes for table field children

@final
class InterfacePolicy6Srcaddr6Object:
    """Typed object for srcaddr6 table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Address name.
    name: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class InterfacePolicy6Dstaddr6Object:
    """Typed object for dstaddr6 table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Address name.
    name: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class InterfacePolicy6Service6Object:
    """Typed object for service6 table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Service name.
    name: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class InterfacePolicy6Response(TypedDict):
    """
    Type hints for firewall/interface_policy6 API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    policyid: int
    uuid: str
    status: Literal["enable", "disable"]
    comments: str
    logtraffic: Literal["all", "utm", "disable"]
    interface: str
    srcaddr6: list[dict[str, Any]]
    dstaddr6: list[dict[str, Any]]
    service6: list[dict[str, Any]]
    application_list_status: Literal["enable", "disable"]
    application_list: str
    ips_sensor_status: Literal["enable", "disable"]
    ips_sensor: str
    dsri: Literal["enable", "disable"]
    av_profile_status: Literal["enable", "disable"]
    av_profile: str
    webfilter_profile_status: Literal["enable", "disable"]
    webfilter_profile: str
    casb_profile_status: Literal["enable", "disable"]
    casb_profile: str
    emailfilter_profile_status: Literal["enable", "disable"]
    emailfilter_profile: str
    dlp_profile_status: Literal["enable", "disable"]
    dlp_profile: str


@final
class InterfacePolicy6Object:
    """Typed FortiObject for firewall/interface_policy6 with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Policy ID (0 - 4294967295).
    policyid: int
    # Universally Unique Identifier
    uuid: str
    # Enable/disable this policy.
    status: Literal["enable", "disable"]
    # Comments.
    comments: str
    # Logging type to be used in this policy
    logtraffic: Literal["all", "utm", "disable"]
    # Monitored interface name from available interfaces.
    interface: str
    # IPv6 address object to limit traffic monitoring to network traffic sent from the
    srcaddr6: list[InterfacePolicy6Srcaddr6Object]  # Table field - list of typed objects
    # IPv6 address object to limit traffic monitoring to network traffic sent to the s
    dstaddr6: list[InterfacePolicy6Dstaddr6Object]  # Table field - list of typed objects
    # Service name.
    service6: list[InterfacePolicy6Service6Object]  # Table field - list of typed objects
    # Enable/disable application control.
    application_list_status: Literal["enable", "disable"]
    # Application list name.
    application_list: str
    # Enable/disable IPS.
    ips_sensor_status: Literal["enable", "disable"]
    # IPS sensor name.
    ips_sensor: str
    # Enable/disable DSRI.
    dsri: Literal["enable", "disable"]
    # Enable/disable antivirus.
    av_profile_status: Literal["enable", "disable"]
    # Antivirus profile.
    av_profile: str
    # Enable/disable web filtering.
    webfilter_profile_status: Literal["enable", "disable"]
    # Web filter profile.
    webfilter_profile: str
    # Enable/disable CASB.
    casb_profile_status: Literal["enable", "disable"]
    # CASB profile.
    casb_profile: str
    # Enable/disable email filter.
    emailfilter_profile_status: Literal["enable", "disable"]
    # Email filter profile.
    emailfilter_profile: str
    # Enable/disable DLP.
    dlp_profile_status: Literal["enable", "disable"]
    # DLP profile name.
    dlp_profile: str
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> InterfacePolicy6Payload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class InterfacePolicy6:
    """
    Configure IPv6 interface policies.
    
    Path: firewall/interface_policy6
    Category: cmdb
    Primary Key: policyid
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey/name provided as positional arg)
    @overload
    def get(
        self,
        policyid: int,
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
    ) -> InterfacePolicy6Object: ...
    
    # Single object (mkey/name provided as keyword arg)
    @overload
    def get(
        self,
        *,
        policyid: int,
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
    ) -> InterfacePolicy6Object: ...
    
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
    ) -> list[InterfacePolicy6Object]: ...
    
    @overload
    def get(
        self,
        policyid: int | None = ...,
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
        policyid: int,
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
    ) -> InterfacePolicy6Response: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
        policyid: int,
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
    ) -> InterfacePolicy6Response: ...
    
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
    ) -> list[InterfacePolicy6Response]: ...
    
    # Default overload for dict mode
    @overload
    def get(
        self,
        policyid: int | None = ...,
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
        policyid: int | None = ...,
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
    ) -> InterfacePolicy6Object | list[InterfacePolicy6Object] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: InterfacePolicy6Payload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        interface: str | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        service6: str | list[str] | list[dict[str, Any]] | None = ...,
        application_list_status: Literal["enable", "disable"] | None = ...,
        application_list: str | None = ...,
        ips_sensor_status: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        dsri: Literal["enable", "disable"] | None = ...,
        av_profile_status: Literal["enable", "disable"] | None = ...,
        av_profile: str | None = ...,
        webfilter_profile_status: Literal["enable", "disable"] | None = ...,
        webfilter_profile: str | None = ...,
        casb_profile_status: Literal["enable", "disable"] | None = ...,
        casb_profile: str | None = ...,
        emailfilter_profile_status: Literal["enable", "disable"] | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile_status: Literal["enable", "disable"] | None = ...,
        dlp_profile: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> InterfacePolicy6Object: ...
    
    @overload
    def post(
        self,
        payload_dict: InterfacePolicy6Payload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        interface: str | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        service6: str | list[str] | list[dict[str, Any]] | None = ...,
        application_list_status: Literal["enable", "disable"] | None = ...,
        application_list: str | None = ...,
        ips_sensor_status: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        dsri: Literal["enable", "disable"] | None = ...,
        av_profile_status: Literal["enable", "disable"] | None = ...,
        av_profile: str | None = ...,
        webfilter_profile_status: Literal["enable", "disable"] | None = ...,
        webfilter_profile: str | None = ...,
        casb_profile_status: Literal["enable", "disable"] | None = ...,
        casb_profile: str | None = ...,
        emailfilter_profile_status: Literal["enable", "disable"] | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile_status: Literal["enable", "disable"] | None = ...,
        dlp_profile: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: InterfacePolicy6Payload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        interface: str | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        service6: str | list[str] | list[dict[str, Any]] | None = ...,
        application_list_status: Literal["enable", "disable"] | None = ...,
        application_list: str | None = ...,
        ips_sensor_status: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        dsri: Literal["enable", "disable"] | None = ...,
        av_profile_status: Literal["enable", "disable"] | None = ...,
        av_profile: str | None = ...,
        webfilter_profile_status: Literal["enable", "disable"] | None = ...,
        webfilter_profile: str | None = ...,
        casb_profile_status: Literal["enable", "disable"] | None = ...,
        casb_profile: str | None = ...,
        emailfilter_profile_status: Literal["enable", "disable"] | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile_status: Literal["enable", "disable"] | None = ...,
        dlp_profile: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: InterfacePolicy6Payload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        interface: str | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        service6: str | list[str] | list[dict[str, Any]] | None = ...,
        application_list_status: Literal["enable", "disable"] | None = ...,
        application_list: str | None = ...,
        ips_sensor_status: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        dsri: Literal["enable", "disable"] | None = ...,
        av_profile_status: Literal["enable", "disable"] | None = ...,
        av_profile: str | None = ...,
        webfilter_profile_status: Literal["enable", "disable"] | None = ...,
        webfilter_profile: str | None = ...,
        casb_profile_status: Literal["enable", "disable"] | None = ...,
        casb_profile: str | None = ...,
        emailfilter_profile_status: Literal["enable", "disable"] | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile_status: Literal["enable", "disable"] | None = ...,
        dlp_profile: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: InterfacePolicy6Payload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        interface: str | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        service6: str | list[str] | list[dict[str, Any]] | None = ...,
        application_list_status: Literal["enable", "disable"] | None = ...,
        application_list: str | None = ...,
        ips_sensor_status: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        dsri: Literal["enable", "disable"] | None = ...,
        av_profile_status: Literal["enable", "disable"] | None = ...,
        av_profile: str | None = ...,
        webfilter_profile_status: Literal["enable", "disable"] | None = ...,
        webfilter_profile: str | None = ...,
        casb_profile_status: Literal["enable", "disable"] | None = ...,
        casb_profile: str | None = ...,
        emailfilter_profile_status: Literal["enable", "disable"] | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile_status: Literal["enable", "disable"] | None = ...,
        dlp_profile: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> InterfacePolicy6Object: ...
    
    @overload
    def put(
        self,
        payload_dict: InterfacePolicy6Payload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        interface: str | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        service6: str | list[str] | list[dict[str, Any]] | None = ...,
        application_list_status: Literal["enable", "disable"] | None = ...,
        application_list: str | None = ...,
        ips_sensor_status: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        dsri: Literal["enable", "disable"] | None = ...,
        av_profile_status: Literal["enable", "disable"] | None = ...,
        av_profile: str | None = ...,
        webfilter_profile_status: Literal["enable", "disable"] | None = ...,
        webfilter_profile: str | None = ...,
        casb_profile_status: Literal["enable", "disable"] | None = ...,
        casb_profile: str | None = ...,
        emailfilter_profile_status: Literal["enable", "disable"] | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile_status: Literal["enable", "disable"] | None = ...,
        dlp_profile: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: InterfacePolicy6Payload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        interface: str | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        service6: str | list[str] | list[dict[str, Any]] | None = ...,
        application_list_status: Literal["enable", "disable"] | None = ...,
        application_list: str | None = ...,
        ips_sensor_status: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        dsri: Literal["enable", "disable"] | None = ...,
        av_profile_status: Literal["enable", "disable"] | None = ...,
        av_profile: str | None = ...,
        webfilter_profile_status: Literal["enable", "disable"] | None = ...,
        webfilter_profile: str | None = ...,
        casb_profile_status: Literal["enable", "disable"] | None = ...,
        casb_profile: str | None = ...,
        emailfilter_profile_status: Literal["enable", "disable"] | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile_status: Literal["enable", "disable"] | None = ...,
        dlp_profile: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: InterfacePolicy6Payload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        interface: str | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        service6: str | list[str] | list[dict[str, Any]] | None = ...,
        application_list_status: Literal["enable", "disable"] | None = ...,
        application_list: str | None = ...,
        ips_sensor_status: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        dsri: Literal["enable", "disable"] | None = ...,
        av_profile_status: Literal["enable", "disable"] | None = ...,
        av_profile: str | None = ...,
        webfilter_profile_status: Literal["enable", "disable"] | None = ...,
        webfilter_profile: str | None = ...,
        casb_profile_status: Literal["enable", "disable"] | None = ...,
        casb_profile: str | None = ...,
        emailfilter_profile_status: Literal["enable", "disable"] | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile_status: Literal["enable", "disable"] | None = ...,
        dlp_profile: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> InterfacePolicy6Object: ...
    
    @overload
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        policyid: int,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: InterfacePolicy6Payload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        interface: str | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        service6: str | list[str] | list[dict[str, Any]] | None = ...,
        application_list_status: Literal["enable", "disable"] | None = ...,
        application_list: str | None = ...,
        ips_sensor_status: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        dsri: Literal["enable", "disable"] | None = ...,
        av_profile_status: Literal["enable", "disable"] | None = ...,
        av_profile: str | None = ...,
        webfilter_profile_status: Literal["enable", "disable"] | None = ...,
        webfilter_profile: str | None = ...,
        casb_profile_status: Literal["enable", "disable"] | None = ...,
        casb_profile: str | None = ...,
        emailfilter_profile_status: Literal["enable", "disable"] | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile_status: Literal["enable", "disable"] | None = ...,
        dlp_profile: str | None = ...,
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
    "InterfacePolicy6",
    "InterfacePolicy6Payload",
    "InterfacePolicy6Object",
]