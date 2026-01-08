from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class HsProfilePayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/hotspot20/hs_profile payload fields.
    
    Configure hotspot profile.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.wireless-controller.hotspot20.anqp-3gpp-cellular.Anqp3GppCellularEndpoint` (via: 3gpp-plmn)
        - :class:`~.wireless-controller.hotspot20.anqp-ip-address-type.AnqpIpAddressTypeEndpoint` (via: ip-addr-type)
        - :class:`~.wireless-controller.hotspot20.anqp-nai-realm.AnqpNaiRealmEndpoint` (via: nai-realm)
        - :class:`~.wireless-controller.hotspot20.anqp-network-auth-type.AnqpNetworkAuthTypeEndpoint` (via: network-auth)
        - :class:`~.wireless-controller.hotspot20.anqp-roaming-consortium.AnqpRoamingConsortiumEndpoint` (via: roaming-consortium)
        - :class:`~.wireless-controller.hotspot20.anqp-venue-name.AnqpVenueNameEndpoint` (via: venue-name)
        - :class:`~.wireless-controller.hotspot20.anqp-venue-url.AnqpVenueUrlEndpoint` (via: venue-url)
        - :class:`~.wireless-controller.hotspot20.h2qp-advice-of-charge.H2QpAdviceOfChargeEndpoint` (via: advice-of-charge)
        - :class:`~.wireless-controller.hotspot20.h2qp-conn-capability.H2QpConnCapabilityEndpoint` (via: conn-cap)
        - :class:`~.wireless-controller.hotspot20.h2qp-operator-name.H2QpOperatorNameEndpoint` (via: oper-friendly-name)
        - ... and 5 more dependencies

    **Usage:**
        payload: HsProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Hotspot profile name.
    release: NotRequired[int]  # Hotspot 2.0 Release number (1, 2, 3, default = 2).
    access_network_type: NotRequired[Literal["private-network", "private-network-with-guest-access", "chargeable-public-network", "free-public-network", "personal-device-network", "emergency-services-only-network", "test-or-experimental", "wildcard"]]  # Access network type.
    access_network_internet: NotRequired[Literal["enable", "disable"]]  # Enable/disable connectivity to the Internet.
    access_network_asra: NotRequired[Literal["enable", "disable"]]  # Enable/disable additional step required for access (ASRA).
    access_network_esr: NotRequired[Literal["enable", "disable"]]  # Enable/disable emergency services reachable (ESR).
    access_network_uesa: NotRequired[Literal["enable", "disable"]]  # Enable/disable unauthenticated emergency service accessible 
    venue_group: NotRequired[Literal["unspecified", "assembly", "business", "educational", "factory", "institutional", "mercantile", "residential", "storage", "utility", "vehicular", "outdoor"]]  # Venue group.
    venue_type: NotRequired[Literal["unspecified", "arena", "stadium", "passenger-terminal", "amphitheater", "amusement-park", "place-of-worship", "convention-center", "library", "museum", "restaurant", "theater", "bar", "coffee-shop", "zoo-or-aquarium", "emergency-center", "doctor-office", "bank", "fire-station", "police-station", "post-office", "professional-office", "research-facility", "attorney-office", "primary-school", "secondary-school", "university-or-college", "factory", "hospital", "long-term-care-facility", "rehab-center", "group-home", "prison-or-jail", "retail-store", "grocery-market", "auto-service-station", "shopping-mall", "gas-station", "private", "hotel-or-motel", "dormitory", "boarding-house", "automobile", "airplane", "bus", "ferry", "ship-or-boat", "train", "motor-bike", "muni-mesh-network", "city-park", "rest-area", "traffic-control", "bus-stop", "kiosk"]]  # Venue type.
    hessid: NotRequired[str]  # Homogeneous extended service set identifier (HESSID).
    proxy_arp: NotRequired[Literal["enable", "disable"]]  # Enable/disable Proxy ARP.
    l2tif: NotRequired[Literal["enable", "disable"]]  # Enable/disable Layer 2 traffic inspection and filtering.
    pame_bi: NotRequired[Literal["disable", "enable"]]  # Enable/disable Pre-Association Message Exchange BSSID Indepe
    anqp_domain_id: NotRequired[int]  # ANQP Domain ID (0-65535).
    domain_name: NotRequired[str]  # Domain name.
    osu_ssid: NotRequired[str]  # Online sign up (OSU) SSID.
    gas_comeback_delay: NotRequired[int]  # GAS comeback delay (0 or 100 - 10000 milliseconds, default =
    gas_fragmentation_limit: NotRequired[int]  # GAS fragmentation limit (512 - 4096, default = 1024).
    dgaf: NotRequired[Literal["enable", "disable"]]  # Enable/disable downstream group-addressed forwarding (DGAF).
    deauth_request_timeout: NotRequired[int]  # Deauthentication request timeout (in seconds).
    wnm_sleep_mode: NotRequired[Literal["enable", "disable"]]  # Enable/disable wireless network management (WNM) sleep mode.
    bss_transition: NotRequired[Literal["enable", "disable"]]  # Enable/disable basic service set (BSS) transition Support.
    venue_name: NotRequired[str]  # Venue name.
    venue_url: NotRequired[str]  # Venue name.
    roaming_consortium: NotRequired[str]  # Roaming consortium list name.
    nai_realm: NotRequired[str]  # NAI realm list name.
    oper_friendly_name: NotRequired[str]  # Operator friendly name.
    oper_icon: NotRequired[str]  # Operator icon.
    advice_of_charge: NotRequired[str]  # Advice of charge.
    osu_provider_nai: NotRequired[str]  # OSU Provider NAI.
    terms_and_conditions: NotRequired[str]  # Terms and conditions.
    osu_provider: NotRequired[list[dict[str, Any]]]  # Manually selected list of OSU provider(s).
    wan_metrics: NotRequired[str]  # WAN metric name.
    network_auth: NotRequired[str]  # Network authentication name.
    x3gpp_plmn: NotRequired[str]  # 3GPP PLMN name.
    conn_cap: NotRequired[str]  # Connection capability name.
    qos_map: NotRequired[str]  # QoS MAP set ID.
    ip_addr_type: NotRequired[str]  # IP address type name.
    wba_open_roaming: NotRequired[Literal["disable", "enable"]]  # Enable/disable WBA open roaming support.
    wba_financial_clearing_provider: NotRequired[str]  # WBA ID of financial clearing provider.
    wba_data_clearing_provider: NotRequired[str]  # WBA ID of data clearing provider.
    wba_charging_currency: NotRequired[str]  # Three letter currency code.
    wba_charging_rate: NotRequired[int]  # Number of currency units per kilobyte.


class HsProfileObject(FortiObject[HsProfilePayload]):
    """Typed FortiObject for wireless_controller/hotspot20/hs_profile with IDE autocomplete support."""
    
    # Hotspot profile name.
    name: str
    # Hotspot 2.0 Release number (1, 2, 3, default = 2).
    release: int
    # Access network type.
    access_network_type: Literal["private-network", "private-network-with-guest-access", "chargeable-public-network", "free-public-network", "personal-device-network", "emergency-services-only-network", "test-or-experimental", "wildcard"]
    # Enable/disable connectivity to the Internet.
    access_network_internet: Literal["enable", "disable"]
    # Enable/disable additional step required for access (ASRA).
    access_network_asra: Literal["enable", "disable"]
    # Enable/disable emergency services reachable (ESR).
    access_network_esr: Literal["enable", "disable"]
    # Enable/disable unauthenticated emergency service accessible (UESA).
    access_network_uesa: Literal["enable", "disable"]
    # Venue group.
    venue_group: Literal["unspecified", "assembly", "business", "educational", "factory", "institutional", "mercantile", "residential", "storage", "utility", "vehicular", "outdoor"]
    # Venue type.
    venue_type: Literal["unspecified", "arena", "stadium", "passenger-terminal", "amphitheater", "amusement-park", "place-of-worship", "convention-center", "library", "museum", "restaurant", "theater", "bar", "coffee-shop", "zoo-or-aquarium", "emergency-center", "doctor-office", "bank", "fire-station", "police-station", "post-office", "professional-office", "research-facility", "attorney-office", "primary-school", "secondary-school", "university-or-college", "factory", "hospital", "long-term-care-facility", "rehab-center", "group-home", "prison-or-jail", "retail-store", "grocery-market", "auto-service-station", "shopping-mall", "gas-station", "private", "hotel-or-motel", "dormitory", "boarding-house", "automobile", "airplane", "bus", "ferry", "ship-or-boat", "train", "motor-bike", "muni-mesh-network", "city-park", "rest-area", "traffic-control", "bus-stop", "kiosk"]
    # Homogeneous extended service set identifier (HESSID).
    hessid: str
    # Enable/disable Proxy ARP.
    proxy_arp: Literal["enable", "disable"]
    # Enable/disable Layer 2 traffic inspection and filtering.
    l2tif: Literal["enable", "disable"]
    # Enable/disable Pre-Association Message Exchange BSSID Independent (PAME-BI).
    pame_bi: Literal["disable", "enable"]
    # ANQP Domain ID (0-65535).
    anqp_domain_id: int
    # Domain name.
    domain_name: str
    # Online sign up (OSU) SSID.
    osu_ssid: str
    # GAS comeback delay (0 or 100 - 10000 milliseconds, default = 500).
    gas_comeback_delay: int
    # GAS fragmentation limit (512 - 4096, default = 1024).
    gas_fragmentation_limit: int
    # Enable/disable downstream group-addressed forwarding (DGAF).
    dgaf: Literal["enable", "disable"]
    # Deauthentication request timeout (in seconds).
    deauth_request_timeout: int
    # Enable/disable wireless network management (WNM) sleep mode.
    wnm_sleep_mode: Literal["enable", "disable"]
    # Enable/disable basic service set (BSS) transition Support.
    bss_transition: Literal["enable", "disable"]
    # Venue name.
    venue_name: str
    # Venue name.
    venue_url: str
    # Roaming consortium list name.
    roaming_consortium: str
    # NAI realm list name.
    nai_realm: str
    # Operator friendly name.
    oper_friendly_name: str
    # Operator icon.
    oper_icon: str
    # Advice of charge.
    advice_of_charge: str
    # OSU Provider NAI.
    osu_provider_nai: str
    # Terms and conditions.
    terms_and_conditions: str
    # Manually selected list of OSU provider(s).
    osu_provider: list[str]  # Auto-flattened from member_table
    # WAN metric name.
    wan_metrics: str
    # Network authentication name.
    network_auth: str
    # 3GPP PLMN name.
    x3gpp_plmn: str
    # Connection capability name.
    conn_cap: str
    # QoS MAP set ID.
    qos_map: str
    # IP address type name.
    ip_addr_type: str
    # Enable/disable WBA open roaming support.
    wba_open_roaming: Literal["disable", "enable"]
    # WBA ID of financial clearing provider.
    wba_financial_clearing_provider: str
    # WBA ID of data clearing provider.
    wba_data_clearing_provider: str
    # Three letter currency code.
    wba_charging_currency: str
    # Number of currency units per kilobyte.
    wba_charging_rate: int
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> HsProfilePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class HsProfile:
    """
    Configure hotspot profile.
    
    Path: wireless_controller/hotspot20/hs_profile
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
    ) -> HsProfileObject: ...
    
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
    ) -> list[HsProfileObject]: ...
    
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
    ) -> HsProfileObject | list[HsProfileObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: HsProfilePayload | None = ...,
        name: str | None = ...,
        release: int | None = ...,
        access_network_type: Literal["private-network", "private-network-with-guest-access", "chargeable-public-network", "free-public-network", "personal-device-network", "emergency-services-only-network", "test-or-experimental", "wildcard"] | None = ...,
        access_network_internet: Literal["enable", "disable"] | None = ...,
        access_network_asra: Literal["enable", "disable"] | None = ...,
        access_network_esr: Literal["enable", "disable"] | None = ...,
        access_network_uesa: Literal["enable", "disable"] | None = ...,
        venue_group: Literal["unspecified", "assembly", "business", "educational", "factory", "institutional", "mercantile", "residential", "storage", "utility", "vehicular", "outdoor"] | None = ...,
        venue_type: Literal["unspecified", "arena", "stadium", "passenger-terminal", "amphitheater", "amusement-park", "place-of-worship", "convention-center", "library", "museum", "restaurant", "theater", "bar", "coffee-shop", "zoo-or-aquarium", "emergency-center", "doctor-office", "bank", "fire-station", "police-station", "post-office", "professional-office", "research-facility", "attorney-office", "primary-school", "secondary-school", "university-or-college", "factory", "hospital", "long-term-care-facility", "rehab-center", "group-home", "prison-or-jail", "retail-store", "grocery-market", "auto-service-station", "shopping-mall", "gas-station", "private", "hotel-or-motel", "dormitory", "boarding-house", "automobile", "airplane", "bus", "ferry", "ship-or-boat", "train", "motor-bike", "muni-mesh-network", "city-park", "rest-area", "traffic-control", "bus-stop", "kiosk"] | None = ...,
        hessid: str | None = ...,
        proxy_arp: Literal["enable", "disable"] | None = ...,
        l2tif: Literal["enable", "disable"] | None = ...,
        pame_bi: Literal["disable", "enable"] | None = ...,
        anqp_domain_id: int | None = ...,
        domain_name: str | None = ...,
        osu_ssid: str | None = ...,
        gas_comeback_delay: int | None = ...,
        gas_fragmentation_limit: int | None = ...,
        dgaf: Literal["enable", "disable"] | None = ...,
        deauth_request_timeout: int | None = ...,
        wnm_sleep_mode: Literal["enable", "disable"] | None = ...,
        bss_transition: Literal["enable", "disable"] | None = ...,
        venue_name: str | None = ...,
        venue_url: str | None = ...,
        roaming_consortium: str | None = ...,
        nai_realm: str | None = ...,
        oper_friendly_name: str | None = ...,
        oper_icon: str | None = ...,
        advice_of_charge: str | None = ...,
        osu_provider_nai: str | None = ...,
        terms_and_conditions: str | None = ...,
        osu_provider: str | list[str] | list[dict[str, Any]] | None = ...,
        wan_metrics: str | None = ...,
        network_auth: str | None = ...,
        x3gpp_plmn: str | None = ...,
        conn_cap: str | None = ...,
        qos_map: str | None = ...,
        ip_addr_type: str | None = ...,
        wba_open_roaming: Literal["disable", "enable"] | None = ...,
        wba_financial_clearing_provider: str | None = ...,
        wba_data_clearing_provider: str | None = ...,
        wba_charging_currency: str | None = ...,
        wba_charging_rate: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> HsProfileObject: ...
    
    @overload
    def post(
        self,
        payload_dict: HsProfilePayload | None = ...,
        name: str | None = ...,
        release: int | None = ...,
        access_network_type: Literal["private-network", "private-network-with-guest-access", "chargeable-public-network", "free-public-network", "personal-device-network", "emergency-services-only-network", "test-or-experimental", "wildcard"] | None = ...,
        access_network_internet: Literal["enable", "disable"] | None = ...,
        access_network_asra: Literal["enable", "disable"] | None = ...,
        access_network_esr: Literal["enable", "disable"] | None = ...,
        access_network_uesa: Literal["enable", "disable"] | None = ...,
        venue_group: Literal["unspecified", "assembly", "business", "educational", "factory", "institutional", "mercantile", "residential", "storage", "utility", "vehicular", "outdoor"] | None = ...,
        venue_type: Literal["unspecified", "arena", "stadium", "passenger-terminal", "amphitheater", "amusement-park", "place-of-worship", "convention-center", "library", "museum", "restaurant", "theater", "bar", "coffee-shop", "zoo-or-aquarium", "emergency-center", "doctor-office", "bank", "fire-station", "police-station", "post-office", "professional-office", "research-facility", "attorney-office", "primary-school", "secondary-school", "university-or-college", "factory", "hospital", "long-term-care-facility", "rehab-center", "group-home", "prison-or-jail", "retail-store", "grocery-market", "auto-service-station", "shopping-mall", "gas-station", "private", "hotel-or-motel", "dormitory", "boarding-house", "automobile", "airplane", "bus", "ferry", "ship-or-boat", "train", "motor-bike", "muni-mesh-network", "city-park", "rest-area", "traffic-control", "bus-stop", "kiosk"] | None = ...,
        hessid: str | None = ...,
        proxy_arp: Literal["enable", "disable"] | None = ...,
        l2tif: Literal["enable", "disable"] | None = ...,
        pame_bi: Literal["disable", "enable"] | None = ...,
        anqp_domain_id: int | None = ...,
        domain_name: str | None = ...,
        osu_ssid: str | None = ...,
        gas_comeback_delay: int | None = ...,
        gas_fragmentation_limit: int | None = ...,
        dgaf: Literal["enable", "disable"] | None = ...,
        deauth_request_timeout: int | None = ...,
        wnm_sleep_mode: Literal["enable", "disable"] | None = ...,
        bss_transition: Literal["enable", "disable"] | None = ...,
        venue_name: str | None = ...,
        venue_url: str | None = ...,
        roaming_consortium: str | None = ...,
        nai_realm: str | None = ...,
        oper_friendly_name: str | None = ...,
        oper_icon: str | None = ...,
        advice_of_charge: str | None = ...,
        osu_provider_nai: str | None = ...,
        terms_and_conditions: str | None = ...,
        osu_provider: str | list[str] | list[dict[str, Any]] | None = ...,
        wan_metrics: str | None = ...,
        network_auth: str | None = ...,
        x3gpp_plmn: str | None = ...,
        conn_cap: str | None = ...,
        qos_map: str | None = ...,
        ip_addr_type: str | None = ...,
        wba_open_roaming: Literal["disable", "enable"] | None = ...,
        wba_financial_clearing_provider: str | None = ...,
        wba_data_clearing_provider: str | None = ...,
        wba_charging_currency: str | None = ...,
        wba_charging_rate: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: HsProfilePayload | None = ...,
        name: str | None = ...,
        release: int | None = ...,
        access_network_type: Literal["private-network", "private-network-with-guest-access", "chargeable-public-network", "free-public-network", "personal-device-network", "emergency-services-only-network", "test-or-experimental", "wildcard"] | None = ...,
        access_network_internet: Literal["enable", "disable"] | None = ...,
        access_network_asra: Literal["enable", "disable"] | None = ...,
        access_network_esr: Literal["enable", "disable"] | None = ...,
        access_network_uesa: Literal["enable", "disable"] | None = ...,
        venue_group: Literal["unspecified", "assembly", "business", "educational", "factory", "institutional", "mercantile", "residential", "storage", "utility", "vehicular", "outdoor"] | None = ...,
        venue_type: Literal["unspecified", "arena", "stadium", "passenger-terminal", "amphitheater", "amusement-park", "place-of-worship", "convention-center", "library", "museum", "restaurant", "theater", "bar", "coffee-shop", "zoo-or-aquarium", "emergency-center", "doctor-office", "bank", "fire-station", "police-station", "post-office", "professional-office", "research-facility", "attorney-office", "primary-school", "secondary-school", "university-or-college", "factory", "hospital", "long-term-care-facility", "rehab-center", "group-home", "prison-or-jail", "retail-store", "grocery-market", "auto-service-station", "shopping-mall", "gas-station", "private", "hotel-or-motel", "dormitory", "boarding-house", "automobile", "airplane", "bus", "ferry", "ship-or-boat", "train", "motor-bike", "muni-mesh-network", "city-park", "rest-area", "traffic-control", "bus-stop", "kiosk"] | None = ...,
        hessid: str | None = ...,
        proxy_arp: Literal["enable", "disable"] | None = ...,
        l2tif: Literal["enable", "disable"] | None = ...,
        pame_bi: Literal["disable", "enable"] | None = ...,
        anqp_domain_id: int | None = ...,
        domain_name: str | None = ...,
        osu_ssid: str | None = ...,
        gas_comeback_delay: int | None = ...,
        gas_fragmentation_limit: int | None = ...,
        dgaf: Literal["enable", "disable"] | None = ...,
        deauth_request_timeout: int | None = ...,
        wnm_sleep_mode: Literal["enable", "disable"] | None = ...,
        bss_transition: Literal["enable", "disable"] | None = ...,
        venue_name: str | None = ...,
        venue_url: str | None = ...,
        roaming_consortium: str | None = ...,
        nai_realm: str | None = ...,
        oper_friendly_name: str | None = ...,
        oper_icon: str | None = ...,
        advice_of_charge: str | None = ...,
        osu_provider_nai: str | None = ...,
        terms_and_conditions: str | None = ...,
        osu_provider: str | list[str] | list[dict[str, Any]] | None = ...,
        wan_metrics: str | None = ...,
        network_auth: str | None = ...,
        x3gpp_plmn: str | None = ...,
        conn_cap: str | None = ...,
        qos_map: str | None = ...,
        ip_addr_type: str | None = ...,
        wba_open_roaming: Literal["disable", "enable"] | None = ...,
        wba_financial_clearing_provider: str | None = ...,
        wba_data_clearing_provider: str | None = ...,
        wba_charging_currency: str | None = ...,
        wba_charging_rate: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: HsProfilePayload | None = ...,
        name: str | None = ...,
        release: int | None = ...,
        access_network_type: Literal["private-network", "private-network-with-guest-access", "chargeable-public-network", "free-public-network", "personal-device-network", "emergency-services-only-network", "test-or-experimental", "wildcard"] | None = ...,
        access_network_internet: Literal["enable", "disable"] | None = ...,
        access_network_asra: Literal["enable", "disable"] | None = ...,
        access_network_esr: Literal["enable", "disable"] | None = ...,
        access_network_uesa: Literal["enable", "disable"] | None = ...,
        venue_group: Literal["unspecified", "assembly", "business", "educational", "factory", "institutional", "mercantile", "residential", "storage", "utility", "vehicular", "outdoor"] | None = ...,
        venue_type: Literal["unspecified", "arena", "stadium", "passenger-terminal", "amphitheater", "amusement-park", "place-of-worship", "convention-center", "library", "museum", "restaurant", "theater", "bar", "coffee-shop", "zoo-or-aquarium", "emergency-center", "doctor-office", "bank", "fire-station", "police-station", "post-office", "professional-office", "research-facility", "attorney-office", "primary-school", "secondary-school", "university-or-college", "factory", "hospital", "long-term-care-facility", "rehab-center", "group-home", "prison-or-jail", "retail-store", "grocery-market", "auto-service-station", "shopping-mall", "gas-station", "private", "hotel-or-motel", "dormitory", "boarding-house", "automobile", "airplane", "bus", "ferry", "ship-or-boat", "train", "motor-bike", "muni-mesh-network", "city-park", "rest-area", "traffic-control", "bus-stop", "kiosk"] | None = ...,
        hessid: str | None = ...,
        proxy_arp: Literal["enable", "disable"] | None = ...,
        l2tif: Literal["enable", "disable"] | None = ...,
        pame_bi: Literal["disable", "enable"] | None = ...,
        anqp_domain_id: int | None = ...,
        domain_name: str | None = ...,
        osu_ssid: str | None = ...,
        gas_comeback_delay: int | None = ...,
        gas_fragmentation_limit: int | None = ...,
        dgaf: Literal["enable", "disable"] | None = ...,
        deauth_request_timeout: int | None = ...,
        wnm_sleep_mode: Literal["enable", "disable"] | None = ...,
        bss_transition: Literal["enable", "disable"] | None = ...,
        venue_name: str | None = ...,
        venue_url: str | None = ...,
        roaming_consortium: str | None = ...,
        nai_realm: str | None = ...,
        oper_friendly_name: str | None = ...,
        oper_icon: str | None = ...,
        advice_of_charge: str | None = ...,
        osu_provider_nai: str | None = ...,
        terms_and_conditions: str | None = ...,
        osu_provider: str | list[str] | list[dict[str, Any]] | None = ...,
        wan_metrics: str | None = ...,
        network_auth: str | None = ...,
        x3gpp_plmn: str | None = ...,
        conn_cap: str | None = ...,
        qos_map: str | None = ...,
        ip_addr_type: str | None = ...,
        wba_open_roaming: Literal["disable", "enable"] | None = ...,
        wba_financial_clearing_provider: str | None = ...,
        wba_data_clearing_provider: str | None = ...,
        wba_charging_currency: str | None = ...,
        wba_charging_rate: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: HsProfilePayload | None = ...,
        name: str | None = ...,
        release: int | None = ...,
        access_network_type: Literal["private-network", "private-network-with-guest-access", "chargeable-public-network", "free-public-network", "personal-device-network", "emergency-services-only-network", "test-or-experimental", "wildcard"] | None = ...,
        access_network_internet: Literal["enable", "disable"] | None = ...,
        access_network_asra: Literal["enable", "disable"] | None = ...,
        access_network_esr: Literal["enable", "disable"] | None = ...,
        access_network_uesa: Literal["enable", "disable"] | None = ...,
        venue_group: Literal["unspecified", "assembly", "business", "educational", "factory", "institutional", "mercantile", "residential", "storage", "utility", "vehicular", "outdoor"] | None = ...,
        venue_type: Literal["unspecified", "arena", "stadium", "passenger-terminal", "amphitheater", "amusement-park", "place-of-worship", "convention-center", "library", "museum", "restaurant", "theater", "bar", "coffee-shop", "zoo-or-aquarium", "emergency-center", "doctor-office", "bank", "fire-station", "police-station", "post-office", "professional-office", "research-facility", "attorney-office", "primary-school", "secondary-school", "university-or-college", "factory", "hospital", "long-term-care-facility", "rehab-center", "group-home", "prison-or-jail", "retail-store", "grocery-market", "auto-service-station", "shopping-mall", "gas-station", "private", "hotel-or-motel", "dormitory", "boarding-house", "automobile", "airplane", "bus", "ferry", "ship-or-boat", "train", "motor-bike", "muni-mesh-network", "city-park", "rest-area", "traffic-control", "bus-stop", "kiosk"] | None = ...,
        hessid: str | None = ...,
        proxy_arp: Literal["enable", "disable"] | None = ...,
        l2tif: Literal["enable", "disable"] | None = ...,
        pame_bi: Literal["disable", "enable"] | None = ...,
        anqp_domain_id: int | None = ...,
        domain_name: str | None = ...,
        osu_ssid: str | None = ...,
        gas_comeback_delay: int | None = ...,
        gas_fragmentation_limit: int | None = ...,
        dgaf: Literal["enable", "disable"] | None = ...,
        deauth_request_timeout: int | None = ...,
        wnm_sleep_mode: Literal["enable", "disable"] | None = ...,
        bss_transition: Literal["enable", "disable"] | None = ...,
        venue_name: str | None = ...,
        venue_url: str | None = ...,
        roaming_consortium: str | None = ...,
        nai_realm: str | None = ...,
        oper_friendly_name: str | None = ...,
        oper_icon: str | None = ...,
        advice_of_charge: str | None = ...,
        osu_provider_nai: str | None = ...,
        terms_and_conditions: str | None = ...,
        osu_provider: str | list[str] | list[dict[str, Any]] | None = ...,
        wan_metrics: str | None = ...,
        network_auth: str | None = ...,
        x3gpp_plmn: str | None = ...,
        conn_cap: str | None = ...,
        qos_map: str | None = ...,
        ip_addr_type: str | None = ...,
        wba_open_roaming: Literal["disable", "enable"] | None = ...,
        wba_financial_clearing_provider: str | None = ...,
        wba_data_clearing_provider: str | None = ...,
        wba_charging_currency: str | None = ...,
        wba_charging_rate: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> HsProfileObject: ...
    
    @overload
    def put(
        self,
        payload_dict: HsProfilePayload | None = ...,
        name: str | None = ...,
        release: int | None = ...,
        access_network_type: Literal["private-network", "private-network-with-guest-access", "chargeable-public-network", "free-public-network", "personal-device-network", "emergency-services-only-network", "test-or-experimental", "wildcard"] | None = ...,
        access_network_internet: Literal["enable", "disable"] | None = ...,
        access_network_asra: Literal["enable", "disable"] | None = ...,
        access_network_esr: Literal["enable", "disable"] | None = ...,
        access_network_uesa: Literal["enable", "disable"] | None = ...,
        venue_group: Literal["unspecified", "assembly", "business", "educational", "factory", "institutional", "mercantile", "residential", "storage", "utility", "vehicular", "outdoor"] | None = ...,
        venue_type: Literal["unspecified", "arena", "stadium", "passenger-terminal", "amphitheater", "amusement-park", "place-of-worship", "convention-center", "library", "museum", "restaurant", "theater", "bar", "coffee-shop", "zoo-or-aquarium", "emergency-center", "doctor-office", "bank", "fire-station", "police-station", "post-office", "professional-office", "research-facility", "attorney-office", "primary-school", "secondary-school", "university-or-college", "factory", "hospital", "long-term-care-facility", "rehab-center", "group-home", "prison-or-jail", "retail-store", "grocery-market", "auto-service-station", "shopping-mall", "gas-station", "private", "hotel-or-motel", "dormitory", "boarding-house", "automobile", "airplane", "bus", "ferry", "ship-or-boat", "train", "motor-bike", "muni-mesh-network", "city-park", "rest-area", "traffic-control", "bus-stop", "kiosk"] | None = ...,
        hessid: str | None = ...,
        proxy_arp: Literal["enable", "disable"] | None = ...,
        l2tif: Literal["enable", "disable"] | None = ...,
        pame_bi: Literal["disable", "enable"] | None = ...,
        anqp_domain_id: int | None = ...,
        domain_name: str | None = ...,
        osu_ssid: str | None = ...,
        gas_comeback_delay: int | None = ...,
        gas_fragmentation_limit: int | None = ...,
        dgaf: Literal["enable", "disable"] | None = ...,
        deauth_request_timeout: int | None = ...,
        wnm_sleep_mode: Literal["enable", "disable"] | None = ...,
        bss_transition: Literal["enable", "disable"] | None = ...,
        venue_name: str | None = ...,
        venue_url: str | None = ...,
        roaming_consortium: str | None = ...,
        nai_realm: str | None = ...,
        oper_friendly_name: str | None = ...,
        oper_icon: str | None = ...,
        advice_of_charge: str | None = ...,
        osu_provider_nai: str | None = ...,
        terms_and_conditions: str | None = ...,
        osu_provider: str | list[str] | list[dict[str, Any]] | None = ...,
        wan_metrics: str | None = ...,
        network_auth: str | None = ...,
        x3gpp_plmn: str | None = ...,
        conn_cap: str | None = ...,
        qos_map: str | None = ...,
        ip_addr_type: str | None = ...,
        wba_open_roaming: Literal["disable", "enable"] | None = ...,
        wba_financial_clearing_provider: str | None = ...,
        wba_data_clearing_provider: str | None = ...,
        wba_charging_currency: str | None = ...,
        wba_charging_rate: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: HsProfilePayload | None = ...,
        name: str | None = ...,
        release: int | None = ...,
        access_network_type: Literal["private-network", "private-network-with-guest-access", "chargeable-public-network", "free-public-network", "personal-device-network", "emergency-services-only-network", "test-or-experimental", "wildcard"] | None = ...,
        access_network_internet: Literal["enable", "disable"] | None = ...,
        access_network_asra: Literal["enable", "disable"] | None = ...,
        access_network_esr: Literal["enable", "disable"] | None = ...,
        access_network_uesa: Literal["enable", "disable"] | None = ...,
        venue_group: Literal["unspecified", "assembly", "business", "educational", "factory", "institutional", "mercantile", "residential", "storage", "utility", "vehicular", "outdoor"] | None = ...,
        venue_type: Literal["unspecified", "arena", "stadium", "passenger-terminal", "amphitheater", "amusement-park", "place-of-worship", "convention-center", "library", "museum", "restaurant", "theater", "bar", "coffee-shop", "zoo-or-aquarium", "emergency-center", "doctor-office", "bank", "fire-station", "police-station", "post-office", "professional-office", "research-facility", "attorney-office", "primary-school", "secondary-school", "university-or-college", "factory", "hospital", "long-term-care-facility", "rehab-center", "group-home", "prison-or-jail", "retail-store", "grocery-market", "auto-service-station", "shopping-mall", "gas-station", "private", "hotel-or-motel", "dormitory", "boarding-house", "automobile", "airplane", "bus", "ferry", "ship-or-boat", "train", "motor-bike", "muni-mesh-network", "city-park", "rest-area", "traffic-control", "bus-stop", "kiosk"] | None = ...,
        hessid: str | None = ...,
        proxy_arp: Literal["enable", "disable"] | None = ...,
        l2tif: Literal["enable", "disable"] | None = ...,
        pame_bi: Literal["disable", "enable"] | None = ...,
        anqp_domain_id: int | None = ...,
        domain_name: str | None = ...,
        osu_ssid: str | None = ...,
        gas_comeback_delay: int | None = ...,
        gas_fragmentation_limit: int | None = ...,
        dgaf: Literal["enable", "disable"] | None = ...,
        deauth_request_timeout: int | None = ...,
        wnm_sleep_mode: Literal["enable", "disable"] | None = ...,
        bss_transition: Literal["enable", "disable"] | None = ...,
        venue_name: str | None = ...,
        venue_url: str | None = ...,
        roaming_consortium: str | None = ...,
        nai_realm: str | None = ...,
        oper_friendly_name: str | None = ...,
        oper_icon: str | None = ...,
        advice_of_charge: str | None = ...,
        osu_provider_nai: str | None = ...,
        terms_and_conditions: str | None = ...,
        osu_provider: str | list[str] | list[dict[str, Any]] | None = ...,
        wan_metrics: str | None = ...,
        network_auth: str | None = ...,
        x3gpp_plmn: str | None = ...,
        conn_cap: str | None = ...,
        qos_map: str | None = ...,
        ip_addr_type: str | None = ...,
        wba_open_roaming: Literal["disable", "enable"] | None = ...,
        wba_financial_clearing_provider: str | None = ...,
        wba_data_clearing_provider: str | None = ...,
        wba_charging_currency: str | None = ...,
        wba_charging_rate: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: HsProfilePayload | None = ...,
        name: str | None = ...,
        release: int | None = ...,
        access_network_type: Literal["private-network", "private-network-with-guest-access", "chargeable-public-network", "free-public-network", "personal-device-network", "emergency-services-only-network", "test-or-experimental", "wildcard"] | None = ...,
        access_network_internet: Literal["enable", "disable"] | None = ...,
        access_network_asra: Literal["enable", "disable"] | None = ...,
        access_network_esr: Literal["enable", "disable"] | None = ...,
        access_network_uesa: Literal["enable", "disable"] | None = ...,
        venue_group: Literal["unspecified", "assembly", "business", "educational", "factory", "institutional", "mercantile", "residential", "storage", "utility", "vehicular", "outdoor"] | None = ...,
        venue_type: Literal["unspecified", "arena", "stadium", "passenger-terminal", "amphitheater", "amusement-park", "place-of-worship", "convention-center", "library", "museum", "restaurant", "theater", "bar", "coffee-shop", "zoo-or-aquarium", "emergency-center", "doctor-office", "bank", "fire-station", "police-station", "post-office", "professional-office", "research-facility", "attorney-office", "primary-school", "secondary-school", "university-or-college", "factory", "hospital", "long-term-care-facility", "rehab-center", "group-home", "prison-or-jail", "retail-store", "grocery-market", "auto-service-station", "shopping-mall", "gas-station", "private", "hotel-or-motel", "dormitory", "boarding-house", "automobile", "airplane", "bus", "ferry", "ship-or-boat", "train", "motor-bike", "muni-mesh-network", "city-park", "rest-area", "traffic-control", "bus-stop", "kiosk"] | None = ...,
        hessid: str | None = ...,
        proxy_arp: Literal["enable", "disable"] | None = ...,
        l2tif: Literal["enable", "disable"] | None = ...,
        pame_bi: Literal["disable", "enable"] | None = ...,
        anqp_domain_id: int | None = ...,
        domain_name: str | None = ...,
        osu_ssid: str | None = ...,
        gas_comeback_delay: int | None = ...,
        gas_fragmentation_limit: int | None = ...,
        dgaf: Literal["enable", "disable"] | None = ...,
        deauth_request_timeout: int | None = ...,
        wnm_sleep_mode: Literal["enable", "disable"] | None = ...,
        bss_transition: Literal["enable", "disable"] | None = ...,
        venue_name: str | None = ...,
        venue_url: str | None = ...,
        roaming_consortium: str | None = ...,
        nai_realm: str | None = ...,
        oper_friendly_name: str | None = ...,
        oper_icon: str | None = ...,
        advice_of_charge: str | None = ...,
        osu_provider_nai: str | None = ...,
        terms_and_conditions: str | None = ...,
        osu_provider: str | list[str] | list[dict[str, Any]] | None = ...,
        wan_metrics: str | None = ...,
        network_auth: str | None = ...,
        x3gpp_plmn: str | None = ...,
        conn_cap: str | None = ...,
        qos_map: str | None = ...,
        ip_addr_type: str | None = ...,
        wba_open_roaming: Literal["disable", "enable"] | None = ...,
        wba_financial_clearing_provider: str | None = ...,
        wba_data_clearing_provider: str | None = ...,
        wba_charging_currency: str | None = ...,
        wba_charging_rate: int | None = ...,
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
    ) -> HsProfileObject: ...
    
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
        payload_dict: HsProfilePayload | None = ...,
        name: str | None = ...,
        release: int | None = ...,
        access_network_type: Literal["private-network", "private-network-with-guest-access", "chargeable-public-network", "free-public-network", "personal-device-network", "emergency-services-only-network", "test-or-experimental", "wildcard"] | None = ...,
        access_network_internet: Literal["enable", "disable"] | None = ...,
        access_network_asra: Literal["enable", "disable"] | None = ...,
        access_network_esr: Literal["enable", "disable"] | None = ...,
        access_network_uesa: Literal["enable", "disable"] | None = ...,
        venue_group: Literal["unspecified", "assembly", "business", "educational", "factory", "institutional", "mercantile", "residential", "storage", "utility", "vehicular", "outdoor"] | None = ...,
        venue_type: Literal["unspecified", "arena", "stadium", "passenger-terminal", "amphitheater", "amusement-park", "place-of-worship", "convention-center", "library", "museum", "restaurant", "theater", "bar", "coffee-shop", "zoo-or-aquarium", "emergency-center", "doctor-office", "bank", "fire-station", "police-station", "post-office", "professional-office", "research-facility", "attorney-office", "primary-school", "secondary-school", "university-or-college", "factory", "hospital", "long-term-care-facility", "rehab-center", "group-home", "prison-or-jail", "retail-store", "grocery-market", "auto-service-station", "shopping-mall", "gas-station", "private", "hotel-or-motel", "dormitory", "boarding-house", "automobile", "airplane", "bus", "ferry", "ship-or-boat", "train", "motor-bike", "muni-mesh-network", "city-park", "rest-area", "traffic-control", "bus-stop", "kiosk"] | None = ...,
        hessid: str | None = ...,
        proxy_arp: Literal["enable", "disable"] | None = ...,
        l2tif: Literal["enable", "disable"] | None = ...,
        pame_bi: Literal["disable", "enable"] | None = ...,
        anqp_domain_id: int | None = ...,
        domain_name: str | None = ...,
        osu_ssid: str | None = ...,
        gas_comeback_delay: int | None = ...,
        gas_fragmentation_limit: int | None = ...,
        dgaf: Literal["enable", "disable"] | None = ...,
        deauth_request_timeout: int | None = ...,
        wnm_sleep_mode: Literal["enable", "disable"] | None = ...,
        bss_transition: Literal["enable", "disable"] | None = ...,
        venue_name: str | None = ...,
        venue_url: str | None = ...,
        roaming_consortium: str | None = ...,
        nai_realm: str | None = ...,
        oper_friendly_name: str | None = ...,
        oper_icon: str | None = ...,
        advice_of_charge: str | None = ...,
        osu_provider_nai: str | None = ...,
        terms_and_conditions: str | None = ...,
        osu_provider: str | list[str] | list[dict[str, Any]] | None = ...,
        wan_metrics: str | None = ...,
        network_auth: str | None = ...,
        x3gpp_plmn: str | None = ...,
        conn_cap: str | None = ...,
        qos_map: str | None = ...,
        ip_addr_type: str | None = ...,
        wba_open_roaming: Literal["disable", "enable"] | None = ...,
        wba_financial_clearing_provider: str | None = ...,
        wba_data_clearing_provider: str | None = ...,
        wba_charging_currency: str | None = ...,
        wba_charging_rate: int | None = ...,
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
    "HsProfile",
    "HsProfilePayload",
    "HsProfileObject",
]