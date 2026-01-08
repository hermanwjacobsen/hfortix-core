from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class WtpPayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/wtp payload fields.
    
    Configure Wireless Termination Points (WTPs), that is, FortiAPs or APs to be managed by FortiGate.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.wireless-controller.apcfg-profile.ApcfgProfileEndpoint` (via: apcfg-profile)
        - :class:`~.wireless-controller.bonjour-profile.BonjourProfileEndpoint` (via: bonjour-profile)
        - :class:`~.wireless-controller.region.RegionEndpoint` (via: region)
        - :class:`~.wireless-controller.wtp-profile.WtpProfileEndpoint` (via: wtp-profile)

    **Usage:**
        payload: WtpPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    wtp_id: str  # WTP ID.
    index: NotRequired[int]  # Index (0 - 4294967295).
    uuid: NotRequired[str]  # Universally Unique Identifier
    admin: NotRequired[Literal["discovered", "disable", "enable"]]  # Configure how the FortiGate operating as a wireless controll
    name: NotRequired[str]  # WTP, AP or FortiAP configuration name.
    location: NotRequired[str]  # Field for describing the physical location of the WTP, AP or
    comment: NotRequired[str]  # Comment.
    region: NotRequired[str]  # Region name WTP is associated with.
    region_x: NotRequired[str]  # Relative horizontal region coordinate (between 0 and 1).
    region_y: NotRequired[str]  # Relative vertical region coordinate (between 0 and 1).
    firmware_provision: NotRequired[str]  # Firmware version to provision to this FortiAP on bootup
    firmware_provision_latest: NotRequired[Literal["disable", "once"]]  # Enable/disable one-time automatic provisioning of the latest
    wtp_profile: str  # WTP profile name to apply to this WTP, AP or FortiAP.
    apcfg_profile: NotRequired[str]  # AP local configuration profile name.
    bonjour_profile: NotRequired[str]  # Bonjour profile name.
    ble_major_id: NotRequired[int]  # Override BLE Major ID.
    ble_minor_id: NotRequired[int]  # Override BLE Minor ID.
    override_led_state: NotRequired[Literal["enable", "disable"]]  # Enable to override the profile LED state setting for this Fo
    led_state: NotRequired[Literal["enable", "disable"]]  # Enable to allow the FortiAPs LEDs to light. Disable to keep
    override_wan_port_mode: NotRequired[Literal["enable", "disable"]]  # Enable/disable overriding the wan-port-mode in the WTP profi
    wan_port_mode: NotRequired[Literal["wan-lan", "wan-only"]]  # Enable/disable using the FortiAP WAN port as a LAN port.
    override_ip_fragment: NotRequired[Literal["enable", "disable"]]  # Enable/disable overriding the WTP profile IP fragment preven
    ip_fragment_preventing: NotRequired[Literal["tcp-mss-adjust", "icmp-unreachable"]]  # Method(s) by which IP fragmentation is prevented for control
    tun_mtu_uplink: NotRequired[int]  # The maximum transmission unit (MTU) of uplink CAPWAP tunnel
    tun_mtu_downlink: NotRequired[int]  # The MTU of downlink CAPWAP tunnel
    override_split_tunnel: NotRequired[Literal["enable", "disable"]]  # Enable/disable overriding the WTP profile split tunneling se
    split_tunneling_acl_path: NotRequired[Literal["tunnel", "local"]]  # Split tunneling ACL path is local/tunnel.
    split_tunneling_acl_local_ap_subnet: NotRequired[Literal["enable", "disable"]]  # Enable/disable automatically adding local subnetwork of Fort
    split_tunneling_acl: NotRequired[list[dict[str, Any]]]  # Split tunneling ACL filter list.
    override_lan: NotRequired[Literal["enable", "disable"]]  # Enable to override the WTP profile LAN port setting.
    lan: NotRequired[str]  # WTP LAN port mapping.
    override_allowaccess: NotRequired[Literal["enable", "disable"]]  # Enable to override the WTP profile management access configu
    allowaccess: NotRequired[Literal["https", "ssh", "snmp"]]  # Control management access to the managed WTP, FortiAP, or AP
    override_login_passwd_change: NotRequired[Literal["enable", "disable"]]  # Enable to override the WTP profile login-password
    login_passwd_change: NotRequired[Literal["yes", "default", "no"]]  # Change or reset the administrator password of a managed WTP,
    login_passwd: NotRequired[str]  # Set the managed WTP, FortiAP, or AP's administrator password
    override_default_mesh_root: NotRequired[Literal["enable", "disable"]]  # Enable to override the WTP profile default mesh root SSID se
    default_mesh_root: NotRequired[Literal["enable", "disable"]]  # Configure default mesh root SSID when it is not included by
    radio_1: NotRequired[str]  # Configuration options for radio 1.
    radio_2: NotRequired[str]  # Configuration options for radio 2.
    radio_3: NotRequired[str]  # Configuration options for radio 3.
    radio_4: NotRequired[str]  # Configuration options for radio 4.
    image_download: NotRequired[Literal["enable", "disable"]]  # Enable/disable WTP image download.
    mesh_bridge_enable: NotRequired[Literal["default", "enable", "disable"]]  # Enable/disable mesh Ethernet bridge when WTP is configured a
    purdue_level: NotRequired[Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"]]  # Purdue Level of this WTP.
    coordinate_latitude: NotRequired[str]  # WTP latitude coordinate.
    coordinate_longitude: NotRequired[str]  # WTP longitude coordinate.

# Nested classes for table field children

@final
class WtpSplittunnelingaclObject:
    """Typed object for split-tunneling-acl table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ID.
    id: int
    # Destination IP and mask for the split-tunneling subnet.
    dest_ip: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class WtpResponse(TypedDict):
    """
    Type hints for wireless_controller/wtp API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    wtp_id: str
    index: int
    uuid: str
    admin: Literal["discovered", "disable", "enable"]
    name: str
    location: str
    comment: str
    region: str
    region_x: str
    region_y: str
    firmware_provision: str
    firmware_provision_latest: Literal["disable", "once"]
    wtp_profile: str
    apcfg_profile: str
    bonjour_profile: str
    ble_major_id: int
    ble_minor_id: int
    override_led_state: Literal["enable", "disable"]
    led_state: Literal["enable", "disable"]
    override_wan_port_mode: Literal["enable", "disable"]
    wan_port_mode: Literal["wan-lan", "wan-only"]
    override_ip_fragment: Literal["enable", "disable"]
    ip_fragment_preventing: Literal["tcp-mss-adjust", "icmp-unreachable"]
    tun_mtu_uplink: int
    tun_mtu_downlink: int
    override_split_tunnel: Literal["enable", "disable"]
    split_tunneling_acl_path: Literal["tunnel", "local"]
    split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"]
    split_tunneling_acl: list[dict[str, Any]]
    override_lan: Literal["enable", "disable"]
    lan: str
    override_allowaccess: Literal["enable", "disable"]
    allowaccess: Literal["https", "ssh", "snmp"]
    override_login_passwd_change: Literal["enable", "disable"]
    login_passwd_change: Literal["yes", "default", "no"]
    login_passwd: str
    override_default_mesh_root: Literal["enable", "disable"]
    default_mesh_root: Literal["enable", "disable"]
    radio_1: str
    radio_2: str
    radio_3: str
    radio_4: str
    image_download: Literal["enable", "disable"]
    mesh_bridge_enable: Literal["default", "enable", "disable"]
    purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"]
    coordinate_latitude: str
    coordinate_longitude: str


@final
class WtpObject:
    """Typed FortiObject for wireless_controller/wtp with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # WTP ID.
    wtp_id: str
    # Index (0 - 4294967295).
    index: int
    # Universally Unique Identifier
    uuid: str
    # Configure how the FortiGate operating as a wireless controller discovers and man
    admin: Literal["discovered", "disable", "enable"]
    # WTP, AP or FortiAP configuration name.
    name: str
    # Field for describing the physical location of the WTP, AP or FortiAP.
    location: str
    # Comment.
    comment: str
    # Region name WTP is associated with.
    region: str
    # Relative horizontal region coordinate (between 0 and 1).
    region_x: str
    # Relative vertical region coordinate (between 0 and 1).
    region_y: str
    # Firmware version to provision to this FortiAP on bootup
    firmware_provision: str
    # Enable/disable one-time automatic provisioning of the latest firmware version.
    firmware_provision_latest: Literal["disable", "once"]
    # WTP profile name to apply to this WTP, AP or FortiAP.
    wtp_profile: str
    # AP local configuration profile name.
    apcfg_profile: str
    # Bonjour profile name.
    bonjour_profile: str
    # Override BLE Major ID.
    ble_major_id: int
    # Override BLE Minor ID.
    ble_minor_id: int
    # Enable to override the profile LED state setting for this FortiAP. You must enab
    override_led_state: Literal["enable", "disable"]
    # Enable to allow the FortiAPs LEDs to light. Disable to keep the LEDs off. You ma
    led_state: Literal["enable", "disable"]
    # Enable/disable overriding the wan-port-mode in the WTP profile.
    override_wan_port_mode: Literal["enable", "disable"]
    # Enable/disable using the FortiAP WAN port as a LAN port.
    wan_port_mode: Literal["wan-lan", "wan-only"]
    # Enable/disable overriding the WTP profile IP fragment prevention setting.
    override_ip_fragment: Literal["enable", "disable"]
    # Method(s) by which IP fragmentation is prevented for control and data packets th
    ip_fragment_preventing: Literal["tcp-mss-adjust", "icmp-unreachable"]
    # The maximum transmission unit (MTU) of uplink CAPWAP tunnel
    tun_mtu_uplink: int
    # The MTU of downlink CAPWAP tunnel
    tun_mtu_downlink: int
    # Enable/disable overriding the WTP profile split tunneling setting.
    override_split_tunnel: Literal["enable", "disable"]
    # Split tunneling ACL path is local/tunnel.
    split_tunneling_acl_path: Literal["tunnel", "local"]
    # Enable/disable automatically adding local subnetwork of FortiAP to split-tunneli
    split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"]
    # Split tunneling ACL filter list.
    split_tunneling_acl: list[WtpSplittunnelingaclObject]  # Table field - list of typed objects
    # Enable to override the WTP profile LAN port setting.
    override_lan: Literal["enable", "disable"]
    # WTP LAN port mapping.
    lan: str
    # Enable to override the WTP profile management access configuration.
    override_allowaccess: Literal["enable", "disable"]
    # Control management access to the managed WTP, FortiAP, or AP. Separate entries w
    allowaccess: Literal["https", "ssh", "snmp"]
    # Enable to override the WTP profile login-password (administrator password) setti
    override_login_passwd_change: Literal["enable", "disable"]
    # Change or reset the administrator password of a managed WTP, FortiAP or AP
    login_passwd_change: Literal["yes", "default", "no"]
    # Set the managed WTP, FortiAP, or AP's administrator password.
    login_passwd: str
    # Enable to override the WTP profile default mesh root SSID setting.
    override_default_mesh_root: Literal["enable", "disable"]
    # Configure default mesh root SSID when it is not included by radio's SSID configu
    default_mesh_root: Literal["enable", "disable"]
    # Configuration options for radio 1.
    radio_1: str
    # Configuration options for radio 2.
    radio_2: str
    # Configuration options for radio 3.
    radio_3: str
    # Configuration options for radio 4.
    radio_4: str
    # Enable/disable WTP image download.
    image_download: Literal["enable", "disable"]
    # Enable/disable mesh Ethernet bridge when WTP is configured as a mesh branch/leaf
    mesh_bridge_enable: Literal["default", "enable", "disable"]
    # Purdue Level of this WTP.
    purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"]
    # WTP latitude coordinate.
    coordinate_latitude: str
    # WTP longitude coordinate.
    coordinate_longitude: str
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> WtpPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Wtp:
    """
    Configure Wireless Termination Points (WTPs), that is, FortiAPs or APs to be managed by FortiGate.
    
    Path: wireless_controller/wtp
    Category: cmdb
    Primary Key: wtp-id
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey/name provided as positional arg)
    @overload
    def get(
        self,
        wtp_id: str,
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
    ) -> WtpObject: ...
    
    # Single object (mkey/name provided as keyword arg)
    @overload
    def get(
        self,
        *,
        wtp_id: str,
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
    ) -> WtpObject: ...
    
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
    ) -> list[WtpObject]: ...
    
    @overload
    def get(
        self,
        wtp_id: str | None = ...,
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
        wtp_id: str,
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
    ) -> WtpResponse: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
        wtp_id: str,
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
    ) -> WtpResponse: ...
    
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
    ) -> list[WtpResponse]: ...
    
    # Default overload for dict mode
    @overload
    def get(
        self,
        wtp_id: str | None = ...,
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
        wtp_id: str | None = ...,
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
    ) -> WtpObject | list[WtpObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: WtpPayload | None = ...,
        wtp_id: str | None = ...,
        index: int | None = ...,
        uuid: str | None = ...,
        admin: Literal["discovered", "disable", "enable"] | None = ...,
        name: str | None = ...,
        location: str | None = ...,
        comment: str | None = ...,
        region: str | None = ...,
        region_x: str | None = ...,
        region_y: str | None = ...,
        firmware_provision: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        wtp_profile: str | None = ...,
        apcfg_profile: str | None = ...,
        bonjour_profile: str | None = ...,
        ble_major_id: int | None = ...,
        ble_minor_id: int | None = ...,
        override_led_state: Literal["enable", "disable"] | None = ...,
        led_state: Literal["enable", "disable"] | None = ...,
        override_wan_port_mode: Literal["enable", "disable"] | None = ...,
        wan_port_mode: Literal["wan-lan", "wan-only"] | None = ...,
        override_ip_fragment: Literal["enable", "disable"] | None = ...,
        ip_fragment_preventing: Literal["tcp-mss-adjust", "icmp-unreachable"] | list[str] | None = ...,
        tun_mtu_uplink: int | None = ...,
        tun_mtu_downlink: int | None = ...,
        override_split_tunnel: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl_path: Literal["tunnel", "local"] | None = ...,
        split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl: str | list[str] | list[dict[str, Any]] | None = ...,
        override_lan: Literal["enable", "disable"] | None = ...,
        lan: str | None = ...,
        override_allowaccess: Literal["enable", "disable"] | None = ...,
        allowaccess: Literal["https", "ssh", "snmp"] | list[str] | None = ...,
        override_login_passwd_change: Literal["enable", "disable"] | None = ...,
        login_passwd_change: Literal["yes", "default", "no"] | None = ...,
        login_passwd: str | None = ...,
        override_default_mesh_root: Literal["enable", "disable"] | None = ...,
        default_mesh_root: Literal["enable", "disable"] | None = ...,
        radio_1: str | None = ...,
        radio_2: str | None = ...,
        radio_3: str | None = ...,
        radio_4: str | None = ...,
        image_download: Literal["enable", "disable"] | None = ...,
        mesh_bridge_enable: Literal["default", "enable", "disable"] | None = ...,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        coordinate_latitude: str | None = ...,
        coordinate_longitude: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> WtpObject: ...
    
    @overload
    def post(
        self,
        payload_dict: WtpPayload | None = ...,
        wtp_id: str | None = ...,
        index: int | None = ...,
        uuid: str | None = ...,
        admin: Literal["discovered", "disable", "enable"] | None = ...,
        name: str | None = ...,
        location: str | None = ...,
        comment: str | None = ...,
        region: str | None = ...,
        region_x: str | None = ...,
        region_y: str | None = ...,
        firmware_provision: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        wtp_profile: str | None = ...,
        apcfg_profile: str | None = ...,
        bonjour_profile: str | None = ...,
        ble_major_id: int | None = ...,
        ble_minor_id: int | None = ...,
        override_led_state: Literal["enable", "disable"] | None = ...,
        led_state: Literal["enable", "disable"] | None = ...,
        override_wan_port_mode: Literal["enable", "disable"] | None = ...,
        wan_port_mode: Literal["wan-lan", "wan-only"] | None = ...,
        override_ip_fragment: Literal["enable", "disable"] | None = ...,
        ip_fragment_preventing: Literal["tcp-mss-adjust", "icmp-unreachable"] | list[str] | None = ...,
        tun_mtu_uplink: int | None = ...,
        tun_mtu_downlink: int | None = ...,
        override_split_tunnel: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl_path: Literal["tunnel", "local"] | None = ...,
        split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl: str | list[str] | list[dict[str, Any]] | None = ...,
        override_lan: Literal["enable", "disable"] | None = ...,
        lan: str | None = ...,
        override_allowaccess: Literal["enable", "disable"] | None = ...,
        allowaccess: Literal["https", "ssh", "snmp"] | list[str] | None = ...,
        override_login_passwd_change: Literal["enable", "disable"] | None = ...,
        login_passwd_change: Literal["yes", "default", "no"] | None = ...,
        login_passwd: str | None = ...,
        override_default_mesh_root: Literal["enable", "disable"] | None = ...,
        default_mesh_root: Literal["enable", "disable"] | None = ...,
        radio_1: str | None = ...,
        radio_2: str | None = ...,
        radio_3: str | None = ...,
        radio_4: str | None = ...,
        image_download: Literal["enable", "disable"] | None = ...,
        mesh_bridge_enable: Literal["default", "enable", "disable"] | None = ...,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        coordinate_latitude: str | None = ...,
        coordinate_longitude: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: WtpPayload | None = ...,
        wtp_id: str | None = ...,
        index: int | None = ...,
        uuid: str | None = ...,
        admin: Literal["discovered", "disable", "enable"] | None = ...,
        name: str | None = ...,
        location: str | None = ...,
        comment: str | None = ...,
        region: str | None = ...,
        region_x: str | None = ...,
        region_y: str | None = ...,
        firmware_provision: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        wtp_profile: str | None = ...,
        apcfg_profile: str | None = ...,
        bonjour_profile: str | None = ...,
        ble_major_id: int | None = ...,
        ble_minor_id: int | None = ...,
        override_led_state: Literal["enable", "disable"] | None = ...,
        led_state: Literal["enable", "disable"] | None = ...,
        override_wan_port_mode: Literal["enable", "disable"] | None = ...,
        wan_port_mode: Literal["wan-lan", "wan-only"] | None = ...,
        override_ip_fragment: Literal["enable", "disable"] | None = ...,
        ip_fragment_preventing: Literal["tcp-mss-adjust", "icmp-unreachable"] | list[str] | None = ...,
        tun_mtu_uplink: int | None = ...,
        tun_mtu_downlink: int | None = ...,
        override_split_tunnel: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl_path: Literal["tunnel", "local"] | None = ...,
        split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl: str | list[str] | list[dict[str, Any]] | None = ...,
        override_lan: Literal["enable", "disable"] | None = ...,
        lan: str | None = ...,
        override_allowaccess: Literal["enable", "disable"] | None = ...,
        allowaccess: Literal["https", "ssh", "snmp"] | list[str] | None = ...,
        override_login_passwd_change: Literal["enable", "disable"] | None = ...,
        login_passwd_change: Literal["yes", "default", "no"] | None = ...,
        login_passwd: str | None = ...,
        override_default_mesh_root: Literal["enable", "disable"] | None = ...,
        default_mesh_root: Literal["enable", "disable"] | None = ...,
        radio_1: str | None = ...,
        radio_2: str | None = ...,
        radio_3: str | None = ...,
        radio_4: str | None = ...,
        image_download: Literal["enable", "disable"] | None = ...,
        mesh_bridge_enable: Literal["default", "enable", "disable"] | None = ...,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        coordinate_latitude: str | None = ...,
        coordinate_longitude: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: WtpPayload | None = ...,
        wtp_id: str | None = ...,
        index: int | None = ...,
        uuid: str | None = ...,
        admin: Literal["discovered", "disable", "enable"] | None = ...,
        name: str | None = ...,
        location: str | None = ...,
        comment: str | None = ...,
        region: str | None = ...,
        region_x: str | None = ...,
        region_y: str | None = ...,
        firmware_provision: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        wtp_profile: str | None = ...,
        apcfg_profile: str | None = ...,
        bonjour_profile: str | None = ...,
        ble_major_id: int | None = ...,
        ble_minor_id: int | None = ...,
        override_led_state: Literal["enable", "disable"] | None = ...,
        led_state: Literal["enable", "disable"] | None = ...,
        override_wan_port_mode: Literal["enable", "disable"] | None = ...,
        wan_port_mode: Literal["wan-lan", "wan-only"] | None = ...,
        override_ip_fragment: Literal["enable", "disable"] | None = ...,
        ip_fragment_preventing: Literal["tcp-mss-adjust", "icmp-unreachable"] | list[str] | None = ...,
        tun_mtu_uplink: int | None = ...,
        tun_mtu_downlink: int | None = ...,
        override_split_tunnel: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl_path: Literal["tunnel", "local"] | None = ...,
        split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl: str | list[str] | list[dict[str, Any]] | None = ...,
        override_lan: Literal["enable", "disable"] | None = ...,
        lan: str | None = ...,
        override_allowaccess: Literal["enable", "disable"] | None = ...,
        allowaccess: Literal["https", "ssh", "snmp"] | list[str] | None = ...,
        override_login_passwd_change: Literal["enable", "disable"] | None = ...,
        login_passwd_change: Literal["yes", "default", "no"] | None = ...,
        login_passwd: str | None = ...,
        override_default_mesh_root: Literal["enable", "disable"] | None = ...,
        default_mesh_root: Literal["enable", "disable"] | None = ...,
        radio_1: str | None = ...,
        radio_2: str | None = ...,
        radio_3: str | None = ...,
        radio_4: str | None = ...,
        image_download: Literal["enable", "disable"] | None = ...,
        mesh_bridge_enable: Literal["default", "enable", "disable"] | None = ...,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        coordinate_latitude: str | None = ...,
        coordinate_longitude: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: WtpPayload | None = ...,
        wtp_id: str | None = ...,
        index: int | None = ...,
        uuid: str | None = ...,
        admin: Literal["discovered", "disable", "enable"] | None = ...,
        name: str | None = ...,
        location: str | None = ...,
        comment: str | None = ...,
        region: str | None = ...,
        region_x: str | None = ...,
        region_y: str | None = ...,
        firmware_provision: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        wtp_profile: str | None = ...,
        apcfg_profile: str | None = ...,
        bonjour_profile: str | None = ...,
        ble_major_id: int | None = ...,
        ble_minor_id: int | None = ...,
        override_led_state: Literal["enable", "disable"] | None = ...,
        led_state: Literal["enable", "disable"] | None = ...,
        override_wan_port_mode: Literal["enable", "disable"] | None = ...,
        wan_port_mode: Literal["wan-lan", "wan-only"] | None = ...,
        override_ip_fragment: Literal["enable", "disable"] | None = ...,
        ip_fragment_preventing: Literal["tcp-mss-adjust", "icmp-unreachable"] | list[str] | None = ...,
        tun_mtu_uplink: int | None = ...,
        tun_mtu_downlink: int | None = ...,
        override_split_tunnel: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl_path: Literal["tunnel", "local"] | None = ...,
        split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl: str | list[str] | list[dict[str, Any]] | None = ...,
        override_lan: Literal["enable", "disable"] | None = ...,
        lan: str | None = ...,
        override_allowaccess: Literal["enable", "disable"] | None = ...,
        allowaccess: Literal["https", "ssh", "snmp"] | list[str] | None = ...,
        override_login_passwd_change: Literal["enable", "disable"] | None = ...,
        login_passwd_change: Literal["yes", "default", "no"] | None = ...,
        login_passwd: str | None = ...,
        override_default_mesh_root: Literal["enable", "disable"] | None = ...,
        default_mesh_root: Literal["enable", "disable"] | None = ...,
        radio_1: str | None = ...,
        radio_2: str | None = ...,
        radio_3: str | None = ...,
        radio_4: str | None = ...,
        image_download: Literal["enable", "disable"] | None = ...,
        mesh_bridge_enable: Literal["default", "enable", "disable"] | None = ...,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        coordinate_latitude: str | None = ...,
        coordinate_longitude: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> WtpObject: ...
    
    @overload
    def put(
        self,
        payload_dict: WtpPayload | None = ...,
        wtp_id: str | None = ...,
        index: int | None = ...,
        uuid: str | None = ...,
        admin: Literal["discovered", "disable", "enable"] | None = ...,
        name: str | None = ...,
        location: str | None = ...,
        comment: str | None = ...,
        region: str | None = ...,
        region_x: str | None = ...,
        region_y: str | None = ...,
        firmware_provision: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        wtp_profile: str | None = ...,
        apcfg_profile: str | None = ...,
        bonjour_profile: str | None = ...,
        ble_major_id: int | None = ...,
        ble_minor_id: int | None = ...,
        override_led_state: Literal["enable", "disable"] | None = ...,
        led_state: Literal["enable", "disable"] | None = ...,
        override_wan_port_mode: Literal["enable", "disable"] | None = ...,
        wan_port_mode: Literal["wan-lan", "wan-only"] | None = ...,
        override_ip_fragment: Literal["enable", "disable"] | None = ...,
        ip_fragment_preventing: Literal["tcp-mss-adjust", "icmp-unreachable"] | list[str] | None = ...,
        tun_mtu_uplink: int | None = ...,
        tun_mtu_downlink: int | None = ...,
        override_split_tunnel: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl_path: Literal["tunnel", "local"] | None = ...,
        split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl: str | list[str] | list[dict[str, Any]] | None = ...,
        override_lan: Literal["enable", "disable"] | None = ...,
        lan: str | None = ...,
        override_allowaccess: Literal["enable", "disable"] | None = ...,
        allowaccess: Literal["https", "ssh", "snmp"] | list[str] | None = ...,
        override_login_passwd_change: Literal["enable", "disable"] | None = ...,
        login_passwd_change: Literal["yes", "default", "no"] | None = ...,
        login_passwd: str | None = ...,
        override_default_mesh_root: Literal["enable", "disable"] | None = ...,
        default_mesh_root: Literal["enable", "disable"] | None = ...,
        radio_1: str | None = ...,
        radio_2: str | None = ...,
        radio_3: str | None = ...,
        radio_4: str | None = ...,
        image_download: Literal["enable", "disable"] | None = ...,
        mesh_bridge_enable: Literal["default", "enable", "disable"] | None = ...,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        coordinate_latitude: str | None = ...,
        coordinate_longitude: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: WtpPayload | None = ...,
        wtp_id: str | None = ...,
        index: int | None = ...,
        uuid: str | None = ...,
        admin: Literal["discovered", "disable", "enable"] | None = ...,
        name: str | None = ...,
        location: str | None = ...,
        comment: str | None = ...,
        region: str | None = ...,
        region_x: str | None = ...,
        region_y: str | None = ...,
        firmware_provision: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        wtp_profile: str | None = ...,
        apcfg_profile: str | None = ...,
        bonjour_profile: str | None = ...,
        ble_major_id: int | None = ...,
        ble_minor_id: int | None = ...,
        override_led_state: Literal["enable", "disable"] | None = ...,
        led_state: Literal["enable", "disable"] | None = ...,
        override_wan_port_mode: Literal["enable", "disable"] | None = ...,
        wan_port_mode: Literal["wan-lan", "wan-only"] | None = ...,
        override_ip_fragment: Literal["enable", "disable"] | None = ...,
        ip_fragment_preventing: Literal["tcp-mss-adjust", "icmp-unreachable"] | list[str] | None = ...,
        tun_mtu_uplink: int | None = ...,
        tun_mtu_downlink: int | None = ...,
        override_split_tunnel: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl_path: Literal["tunnel", "local"] | None = ...,
        split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl: str | list[str] | list[dict[str, Any]] | None = ...,
        override_lan: Literal["enable", "disable"] | None = ...,
        lan: str | None = ...,
        override_allowaccess: Literal["enable", "disable"] | None = ...,
        allowaccess: Literal["https", "ssh", "snmp"] | list[str] | None = ...,
        override_login_passwd_change: Literal["enable", "disable"] | None = ...,
        login_passwd_change: Literal["yes", "default", "no"] | None = ...,
        login_passwd: str | None = ...,
        override_default_mesh_root: Literal["enable", "disable"] | None = ...,
        default_mesh_root: Literal["enable", "disable"] | None = ...,
        radio_1: str | None = ...,
        radio_2: str | None = ...,
        radio_3: str | None = ...,
        radio_4: str | None = ...,
        image_download: Literal["enable", "disable"] | None = ...,
        mesh_bridge_enable: Literal["default", "enable", "disable"] | None = ...,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        coordinate_latitude: str | None = ...,
        coordinate_longitude: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: WtpPayload | None = ...,
        wtp_id: str | None = ...,
        index: int | None = ...,
        uuid: str | None = ...,
        admin: Literal["discovered", "disable", "enable"] | None = ...,
        name: str | None = ...,
        location: str | None = ...,
        comment: str | None = ...,
        region: str | None = ...,
        region_x: str | None = ...,
        region_y: str | None = ...,
        firmware_provision: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        wtp_profile: str | None = ...,
        apcfg_profile: str | None = ...,
        bonjour_profile: str | None = ...,
        ble_major_id: int | None = ...,
        ble_minor_id: int | None = ...,
        override_led_state: Literal["enable", "disable"] | None = ...,
        led_state: Literal["enable", "disable"] | None = ...,
        override_wan_port_mode: Literal["enable", "disable"] | None = ...,
        wan_port_mode: Literal["wan-lan", "wan-only"] | None = ...,
        override_ip_fragment: Literal["enable", "disable"] | None = ...,
        ip_fragment_preventing: Literal["tcp-mss-adjust", "icmp-unreachable"] | list[str] | None = ...,
        tun_mtu_uplink: int | None = ...,
        tun_mtu_downlink: int | None = ...,
        override_split_tunnel: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl_path: Literal["tunnel", "local"] | None = ...,
        split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl: str | list[str] | list[dict[str, Any]] | None = ...,
        override_lan: Literal["enable", "disable"] | None = ...,
        lan: str | None = ...,
        override_allowaccess: Literal["enable", "disable"] | None = ...,
        allowaccess: Literal["https", "ssh", "snmp"] | list[str] | None = ...,
        override_login_passwd_change: Literal["enable", "disable"] | None = ...,
        login_passwd_change: Literal["yes", "default", "no"] | None = ...,
        login_passwd: str | None = ...,
        override_default_mesh_root: Literal["enable", "disable"] | None = ...,
        default_mesh_root: Literal["enable", "disable"] | None = ...,
        radio_1: str | None = ...,
        radio_2: str | None = ...,
        radio_3: str | None = ...,
        radio_4: str | None = ...,
        image_download: Literal["enable", "disable"] | None = ...,
        mesh_bridge_enable: Literal["default", "enable", "disable"] | None = ...,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        coordinate_latitude: str | None = ...,
        coordinate_longitude: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        wtp_id: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> WtpObject: ...
    
    @overload
    def delete(
        self,
        wtp_id: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def delete(
        self,
        wtp_id: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def delete(
        self,
        wtp_id: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        wtp_id: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: WtpPayload | None = ...,
        wtp_id: str | None = ...,
        index: int | None = ...,
        uuid: str | None = ...,
        admin: Literal["discovered", "disable", "enable"] | None = ...,
        name: str | None = ...,
        location: str | None = ...,
        comment: str | None = ...,
        region: str | None = ...,
        region_x: str | None = ...,
        region_y: str | None = ...,
        firmware_provision: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        wtp_profile: str | None = ...,
        apcfg_profile: str | None = ...,
        bonjour_profile: str | None = ...,
        ble_major_id: int | None = ...,
        ble_minor_id: int | None = ...,
        override_led_state: Literal["enable", "disable"] | None = ...,
        led_state: Literal["enable", "disable"] | None = ...,
        override_wan_port_mode: Literal["enable", "disable"] | None = ...,
        wan_port_mode: Literal["wan-lan", "wan-only"] | None = ...,
        override_ip_fragment: Literal["enable", "disable"] | None = ...,
        ip_fragment_preventing: Literal["tcp-mss-adjust", "icmp-unreachable"] | list[str] | None = ...,
        tun_mtu_uplink: int | None = ...,
        tun_mtu_downlink: int | None = ...,
        override_split_tunnel: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl_path: Literal["tunnel", "local"] | None = ...,
        split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl: str | list[str] | list[dict[str, Any]] | None = ...,
        override_lan: Literal["enable", "disable"] | None = ...,
        lan: str | None = ...,
        override_allowaccess: Literal["enable", "disable"] | None = ...,
        allowaccess: Literal["https", "ssh", "snmp"] | list[str] | None = ...,
        override_login_passwd_change: Literal["enable", "disable"] | None = ...,
        login_passwd_change: Literal["yes", "default", "no"] | None = ...,
        login_passwd: str | None = ...,
        override_default_mesh_root: Literal["enable", "disable"] | None = ...,
        default_mesh_root: Literal["enable", "disable"] | None = ...,
        radio_1: str | None = ...,
        radio_2: str | None = ...,
        radio_3: str | None = ...,
        radio_4: str | None = ...,
        image_download: Literal["enable", "disable"] | None = ...,
        mesh_bridge_enable: Literal["default", "enable", "disable"] | None = ...,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        coordinate_latitude: str | None = ...,
        coordinate_longitude: str | None = ...,
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
    "Wtp",
    "WtpPayload",
    "WtpObject",
]