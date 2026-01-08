from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class SnifferPayload(TypedDict, total=False):
    """
    Type hints for firewall/sniffer payload fields.
    
    Configure sniffer.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.antivirus.profile.ProfileEndpoint` (via: av-profile)
        - :class:`~.application.list.ListEndpoint` (via: application-list)
        - :class:`~.dlp.profile.ProfileEndpoint` (via: dlp-profile)
        - :class:`~.emailfilter.profile.ProfileEndpoint` (via: emailfilter-profile)
        - :class:`~.file-filter.profile.ProfileEndpoint` (via: file-filter-profile)
        - :class:`~.ips.sensor.SensorEndpoint` (via: ips-sensor)
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface)
        - :class:`~.webfilter.profile.ProfileEndpoint` (via: webfilter-profile)

    **Usage:**
        payload: SnifferPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    id: NotRequired[int]  # Sniffer ID (0 - 9999).
    uuid: NotRequired[str]  # Universally Unique Identifier
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable the active status of the sniffer.
    logtraffic: NotRequired[Literal["all", "utm", "disable"]]  # Either log all sessions, only sessions that have a security
    ipv6: NotRequired[Literal["enable", "disable"]]  # Enable/disable sniffing IPv6 packets.
    non_ip: NotRequired[Literal["enable", "disable"]]  # Enable/disable sniffing non-IP packets.
    interface: NotRequired[str]  # Interface name that traffic sniffing will take place on.
    host: NotRequired[str]  # Hosts to filter for in sniffer traffic
    port: NotRequired[str]  # Ports to sniff
    protocol: NotRequired[str]  # Integer value for the protocol type as defined by IANA
    vlan: NotRequired[str]  # List of VLANs to sniff.
    application_list_status: NotRequired[Literal["enable", "disable"]]  # Enable/disable application control profile.
    application_list: str  # Name of an existing application list.
    ips_sensor_status: NotRequired[Literal["enable", "disable"]]  # Enable/disable IPS sensor.
    ips_sensor: str  # Name of an existing IPS sensor.
    dsri: NotRequired[Literal["enable", "disable"]]  # Enable/disable DSRI.
    av_profile_status: NotRequired[Literal["enable", "disable"]]  # Enable/disable antivirus profile.
    av_profile: str  # Name of an existing antivirus profile.
    webfilter_profile_status: NotRequired[Literal["enable", "disable"]]  # Enable/disable web filter profile.
    webfilter_profile: str  # Name of an existing web filter profile.
    emailfilter_profile_status: NotRequired[Literal["enable", "disable"]]  # Enable/disable emailfilter.
    emailfilter_profile: str  # Name of an existing email filter profile.
    dlp_profile_status: NotRequired[Literal["enable", "disable"]]  # Enable/disable DLP profile.
    dlp_profile: str  # Name of an existing DLP profile.
    ip_threatfeed_status: NotRequired[Literal["enable", "disable"]]  # Enable/disable IP threat feed.
    ip_threatfeed: NotRequired[list[dict[str, Any]]]  # Name of an existing IP threat feed.
    file_filter_profile_status: NotRequired[Literal["enable", "disable"]]  # Enable/disable file filter.
    file_filter_profile: str  # Name of an existing file-filter profile.
    ips_dos_status: NotRequired[Literal["enable", "disable"]]  # Enable/disable IPS DoS anomaly detection.
    anomaly: NotRequired[list[dict[str, Any]]]  # Configuration method to edit Denial of Service (DoS) anomaly

# Nested classes for table field children

@final
class SnifferIpthreatfeedObject:
    """Typed object for ip-threatfeed table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Threat feed name.
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
class SnifferAnomalyObject:
    """Typed object for anomaly table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Anomaly name.
    name: str
    # Enable/disable this anomaly.
    status: Literal["disable", "enable"]
    # Enable/disable anomaly logging.
    log: Literal["enable", "disable"]
    # Action taken when the threshold is reached.
    action: Literal["pass", "block"]
    # Quarantine method.
    quarantine: Literal["none", "attacker"]
    # Duration of quarantine.
    quarantine_expiry: str
    # Enable/disable quarantine logging.
    quarantine_log: Literal["disable", "enable"]
    # Anomaly threshold. Number of detected instances
    threshold: int
    # Number of detected instances (packets per second or concurrent session number) w
    threshold(default): int
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class SnifferResponse(TypedDict):
    """
    Type hints for firewall/sniffer API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    id: int
    uuid: str
    status: Literal["enable", "disable"]
    logtraffic: Literal["all", "utm", "disable"]
    ipv6: Literal["enable", "disable"]
    non_ip: Literal["enable", "disable"]
    interface: str
    host: str
    port: str
    protocol: str
    vlan: str
    application_list_status: Literal["enable", "disable"]
    application_list: str
    ips_sensor_status: Literal["enable", "disable"]
    ips_sensor: str
    dsri: Literal["enable", "disable"]
    av_profile_status: Literal["enable", "disable"]
    av_profile: str
    webfilter_profile_status: Literal["enable", "disable"]
    webfilter_profile: str
    emailfilter_profile_status: Literal["enable", "disable"]
    emailfilter_profile: str
    dlp_profile_status: Literal["enable", "disable"]
    dlp_profile: str
    ip_threatfeed_status: Literal["enable", "disable"]
    ip_threatfeed: list[dict[str, Any]]
    file_filter_profile_status: Literal["enable", "disable"]
    file_filter_profile: str
    ips_dos_status: Literal["enable", "disable"]
    anomaly: list[dict[str, Any]]


@final
class SnifferObject:
    """Typed FortiObject for firewall/sniffer with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Sniffer ID (0 - 9999).
    id: int
    # Universally Unique Identifier
    uuid: str
    # Enable/disable the active status of the sniffer.
    status: Literal["enable", "disable"]
    # Either log all sessions, only sessions that have a security profile applied, or
    logtraffic: Literal["all", "utm", "disable"]
    # Enable/disable sniffing IPv6 packets.
    ipv6: Literal["enable", "disable"]
    # Enable/disable sniffing non-IP packets.
    non_ip: Literal["enable", "disable"]
    # Interface name that traffic sniffing will take place on.
    interface: str
    # Hosts to filter for in sniffer traffic
    host: str
    # Ports to sniff (Format examples: 10, :20, 30:40, 50-, 100-200).
    port: str
    # Integer value for the protocol type as defined by IANA (0 - 255).
    protocol: str
    # List of VLANs to sniff.
    vlan: str
    # Enable/disable application control profile.
    application_list_status: Literal["enable", "disable"]
    # Name of an existing application list.
    application_list: str
    # Enable/disable IPS sensor.
    ips_sensor_status: Literal["enable", "disable"]
    # Name of an existing IPS sensor.
    ips_sensor: str
    # Enable/disable DSRI.
    dsri: Literal["enable", "disable"]
    # Enable/disable antivirus profile.
    av_profile_status: Literal["enable", "disable"]
    # Name of an existing antivirus profile.
    av_profile: str
    # Enable/disable web filter profile.
    webfilter_profile_status: Literal["enable", "disable"]
    # Name of an existing web filter profile.
    webfilter_profile: str
    # Enable/disable emailfilter.
    emailfilter_profile_status: Literal["enable", "disable"]
    # Name of an existing email filter profile.
    emailfilter_profile: str
    # Enable/disable DLP profile.
    dlp_profile_status: Literal["enable", "disable"]
    # Name of an existing DLP profile.
    dlp_profile: str
    # Enable/disable IP threat feed.
    ip_threatfeed_status: Literal["enable", "disable"]
    # Name of an existing IP threat feed.
    ip_threatfeed: list[SnifferIpthreatfeedObject]  # Table field - list of typed objects
    # Enable/disable file filter.
    file_filter_profile_status: Literal["enable", "disable"]
    # Name of an existing file-filter profile.
    file_filter_profile: str
    # Enable/disable IPS DoS anomaly detection.
    ips_dos_status: Literal["enable", "disable"]
    # Configuration method to edit Denial of Service (DoS) anomaly settings.
    anomaly: list[SnifferAnomalyObject]  # Table field - list of typed objects
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> SnifferPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Sniffer:
    """
    Configure sniffer.
    
    Path: firewall/sniffer
    Category: cmdb
    Primary Key: id
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey/name provided as positional arg)
    @overload
    def get(
        self,
        id: int,
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
    ) -> SnifferObject: ...
    
    # Single object (mkey/name provided as keyword arg)
    @overload
    def get(
        self,
        *,
        id: int,
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
    ) -> SnifferObject: ...
    
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
    ) -> list[SnifferObject]: ...
    
    @overload
    def get(
        self,
        id: int | None = ...,
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
        id: int,
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
    ) -> SnifferResponse: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
        id: int,
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
    ) -> SnifferResponse: ...
    
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
    ) -> list[SnifferResponse]: ...
    
    # Default overload for dict mode
    @overload
    def get(
        self,
        id: int | None = ...,
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
        id: int | None = ...,
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
    ) -> SnifferObject | list[SnifferObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: SnifferPayload | None = ...,
        id: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        ipv6: Literal["enable", "disable"] | None = ...,
        non_ip: Literal["enable", "disable"] | None = ...,
        interface: str | None = ...,
        host: str | None = ...,
        port: str | None = ...,
        protocol: str | None = ...,
        vlan: str | None = ...,
        application_list_status: Literal["enable", "disable"] | None = ...,
        application_list: str | None = ...,
        ips_sensor_status: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        dsri: Literal["enable", "disable"] | None = ...,
        av_profile_status: Literal["enable", "disable"] | None = ...,
        av_profile: str | None = ...,
        webfilter_profile_status: Literal["enable", "disable"] | None = ...,
        webfilter_profile: str | None = ...,
        emailfilter_profile_status: Literal["enable", "disable"] | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile_status: Literal["enable", "disable"] | None = ...,
        dlp_profile: str | None = ...,
        ip_threatfeed_status: Literal["enable", "disable"] | None = ...,
        ip_threatfeed: str | list[str] | list[dict[str, Any]] | None = ...,
        file_filter_profile_status: Literal["enable", "disable"] | None = ...,
        file_filter_profile: str | None = ...,
        ips_dos_status: Literal["enable", "disable"] | None = ...,
        anomaly: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SnifferObject: ...
    
    @overload
    def post(
        self,
        payload_dict: SnifferPayload | None = ...,
        id: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        ipv6: Literal["enable", "disable"] | None = ...,
        non_ip: Literal["enable", "disable"] | None = ...,
        interface: str | None = ...,
        host: str | None = ...,
        port: str | None = ...,
        protocol: str | None = ...,
        vlan: str | None = ...,
        application_list_status: Literal["enable", "disable"] | None = ...,
        application_list: str | None = ...,
        ips_sensor_status: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        dsri: Literal["enable", "disable"] | None = ...,
        av_profile_status: Literal["enable", "disable"] | None = ...,
        av_profile: str | None = ...,
        webfilter_profile_status: Literal["enable", "disable"] | None = ...,
        webfilter_profile: str | None = ...,
        emailfilter_profile_status: Literal["enable", "disable"] | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile_status: Literal["enable", "disable"] | None = ...,
        dlp_profile: str | None = ...,
        ip_threatfeed_status: Literal["enable", "disable"] | None = ...,
        ip_threatfeed: str | list[str] | list[dict[str, Any]] | None = ...,
        file_filter_profile_status: Literal["enable", "disable"] | None = ...,
        file_filter_profile: str | None = ...,
        ips_dos_status: Literal["enable", "disable"] | None = ...,
        anomaly: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: SnifferPayload | None = ...,
        id: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        ipv6: Literal["enable", "disable"] | None = ...,
        non_ip: Literal["enable", "disable"] | None = ...,
        interface: str | None = ...,
        host: str | None = ...,
        port: str | None = ...,
        protocol: str | None = ...,
        vlan: str | None = ...,
        application_list_status: Literal["enable", "disable"] | None = ...,
        application_list: str | None = ...,
        ips_sensor_status: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        dsri: Literal["enable", "disable"] | None = ...,
        av_profile_status: Literal["enable", "disable"] | None = ...,
        av_profile: str | None = ...,
        webfilter_profile_status: Literal["enable", "disable"] | None = ...,
        webfilter_profile: str | None = ...,
        emailfilter_profile_status: Literal["enable", "disable"] | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile_status: Literal["enable", "disable"] | None = ...,
        dlp_profile: str | None = ...,
        ip_threatfeed_status: Literal["enable", "disable"] | None = ...,
        ip_threatfeed: str | list[str] | list[dict[str, Any]] | None = ...,
        file_filter_profile_status: Literal["enable", "disable"] | None = ...,
        file_filter_profile: str | None = ...,
        ips_dos_status: Literal["enable", "disable"] | None = ...,
        anomaly: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: SnifferPayload | None = ...,
        id: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        ipv6: Literal["enable", "disable"] | None = ...,
        non_ip: Literal["enable", "disable"] | None = ...,
        interface: str | None = ...,
        host: str | None = ...,
        port: str | None = ...,
        protocol: str | None = ...,
        vlan: str | None = ...,
        application_list_status: Literal["enable", "disable"] | None = ...,
        application_list: str | None = ...,
        ips_sensor_status: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        dsri: Literal["enable", "disable"] | None = ...,
        av_profile_status: Literal["enable", "disable"] | None = ...,
        av_profile: str | None = ...,
        webfilter_profile_status: Literal["enable", "disable"] | None = ...,
        webfilter_profile: str | None = ...,
        emailfilter_profile_status: Literal["enable", "disable"] | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile_status: Literal["enable", "disable"] | None = ...,
        dlp_profile: str | None = ...,
        ip_threatfeed_status: Literal["enable", "disable"] | None = ...,
        ip_threatfeed: str | list[str] | list[dict[str, Any]] | None = ...,
        file_filter_profile_status: Literal["enable", "disable"] | None = ...,
        file_filter_profile: str | None = ...,
        ips_dos_status: Literal["enable", "disable"] | None = ...,
        anomaly: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: SnifferPayload | None = ...,
        id: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        ipv6: Literal["enable", "disable"] | None = ...,
        non_ip: Literal["enable", "disable"] | None = ...,
        interface: str | None = ...,
        host: str | None = ...,
        port: str | None = ...,
        protocol: str | None = ...,
        vlan: str | None = ...,
        application_list_status: Literal["enable", "disable"] | None = ...,
        application_list: str | None = ...,
        ips_sensor_status: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        dsri: Literal["enable", "disable"] | None = ...,
        av_profile_status: Literal["enable", "disable"] | None = ...,
        av_profile: str | None = ...,
        webfilter_profile_status: Literal["enable", "disable"] | None = ...,
        webfilter_profile: str | None = ...,
        emailfilter_profile_status: Literal["enable", "disable"] | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile_status: Literal["enable", "disable"] | None = ...,
        dlp_profile: str | None = ...,
        ip_threatfeed_status: Literal["enable", "disable"] | None = ...,
        ip_threatfeed: str | list[str] | list[dict[str, Any]] | None = ...,
        file_filter_profile_status: Literal["enable", "disable"] | None = ...,
        file_filter_profile: str | None = ...,
        ips_dos_status: Literal["enable", "disable"] | None = ...,
        anomaly: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SnifferObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SnifferPayload | None = ...,
        id: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        ipv6: Literal["enable", "disable"] | None = ...,
        non_ip: Literal["enable", "disable"] | None = ...,
        interface: str | None = ...,
        host: str | None = ...,
        port: str | None = ...,
        protocol: str | None = ...,
        vlan: str | None = ...,
        application_list_status: Literal["enable", "disable"] | None = ...,
        application_list: str | None = ...,
        ips_sensor_status: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        dsri: Literal["enable", "disable"] | None = ...,
        av_profile_status: Literal["enable", "disable"] | None = ...,
        av_profile: str | None = ...,
        webfilter_profile_status: Literal["enable", "disable"] | None = ...,
        webfilter_profile: str | None = ...,
        emailfilter_profile_status: Literal["enable", "disable"] | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile_status: Literal["enable", "disable"] | None = ...,
        dlp_profile: str | None = ...,
        ip_threatfeed_status: Literal["enable", "disable"] | None = ...,
        ip_threatfeed: str | list[str] | list[dict[str, Any]] | None = ...,
        file_filter_profile_status: Literal["enable", "disable"] | None = ...,
        file_filter_profile: str | None = ...,
        ips_dos_status: Literal["enable", "disable"] | None = ...,
        anomaly: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: SnifferPayload | None = ...,
        id: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        ipv6: Literal["enable", "disable"] | None = ...,
        non_ip: Literal["enable", "disable"] | None = ...,
        interface: str | None = ...,
        host: str | None = ...,
        port: str | None = ...,
        protocol: str | None = ...,
        vlan: str | None = ...,
        application_list_status: Literal["enable", "disable"] | None = ...,
        application_list: str | None = ...,
        ips_sensor_status: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        dsri: Literal["enable", "disable"] | None = ...,
        av_profile_status: Literal["enable", "disable"] | None = ...,
        av_profile: str | None = ...,
        webfilter_profile_status: Literal["enable", "disable"] | None = ...,
        webfilter_profile: str | None = ...,
        emailfilter_profile_status: Literal["enable", "disable"] | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile_status: Literal["enable", "disable"] | None = ...,
        dlp_profile: str | None = ...,
        ip_threatfeed_status: Literal["enable", "disable"] | None = ...,
        ip_threatfeed: str | list[str] | list[dict[str, Any]] | None = ...,
        file_filter_profile_status: Literal["enable", "disable"] | None = ...,
        file_filter_profile: str | None = ...,
        ips_dos_status: Literal["enable", "disable"] | None = ...,
        anomaly: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: SnifferPayload | None = ...,
        id: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        ipv6: Literal["enable", "disable"] | None = ...,
        non_ip: Literal["enable", "disable"] | None = ...,
        interface: str | None = ...,
        host: str | None = ...,
        port: str | None = ...,
        protocol: str | None = ...,
        vlan: str | None = ...,
        application_list_status: Literal["enable", "disable"] | None = ...,
        application_list: str | None = ...,
        ips_sensor_status: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        dsri: Literal["enable", "disable"] | None = ...,
        av_profile_status: Literal["enable", "disable"] | None = ...,
        av_profile: str | None = ...,
        webfilter_profile_status: Literal["enable", "disable"] | None = ...,
        webfilter_profile: str | None = ...,
        emailfilter_profile_status: Literal["enable", "disable"] | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile_status: Literal["enable", "disable"] | None = ...,
        dlp_profile: str | None = ...,
        ip_threatfeed_status: Literal["enable", "disable"] | None = ...,
        ip_threatfeed: str | list[str] | list[dict[str, Any]] | None = ...,
        file_filter_profile_status: Literal["enable", "disable"] | None = ...,
        file_filter_profile: str | None = ...,
        ips_dos_status: Literal["enable", "disable"] | None = ...,
        anomaly: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SnifferObject: ...
    
    @overload
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        id: int,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: SnifferPayload | None = ...,
        id: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        ipv6: Literal["enable", "disable"] | None = ...,
        non_ip: Literal["enable", "disable"] | None = ...,
        interface: str | None = ...,
        host: str | None = ...,
        port: str | None = ...,
        protocol: str | None = ...,
        vlan: str | None = ...,
        application_list_status: Literal["enable", "disable"] | None = ...,
        application_list: str | None = ...,
        ips_sensor_status: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        dsri: Literal["enable", "disable"] | None = ...,
        av_profile_status: Literal["enable", "disable"] | None = ...,
        av_profile: str | None = ...,
        webfilter_profile_status: Literal["enable", "disable"] | None = ...,
        webfilter_profile: str | None = ...,
        emailfilter_profile_status: Literal["enable", "disable"] | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile_status: Literal["enable", "disable"] | None = ...,
        dlp_profile: str | None = ...,
        ip_threatfeed_status: Literal["enable", "disable"] | None = ...,
        ip_threatfeed: str | list[str] | list[dict[str, Any]] | None = ...,
        file_filter_profile_status: Literal["enable", "disable"] | None = ...,
        file_filter_profile: str | None = ...,
        ips_dos_status: Literal["enable", "disable"] | None = ...,
        anomaly: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "Sniffer",
    "SnifferPayload",
    "SnifferObject",
]