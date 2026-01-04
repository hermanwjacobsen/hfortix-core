from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class WtpPayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/wtp payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: WtpPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    wtp_id: str  # WTP ID.
    index: NotRequired[int]  # Index (0 - 4294967295).
    uuid: NotRequired[str]  # Universally Unique Identifier (UUID; automatically assigned 
    admin: NotRequired[Literal["discovered", "disable", "enable"]]  # Configure how the FortiGate operating as a wireless controll
    name: NotRequired[str]  # WTP, AP or FortiAP configuration name.
    location: NotRequired[str]  # Field for describing the physical location of the WTP, AP or
    comment: NotRequired[str]  # Comment.
    region: NotRequired[str]  # Region name WTP is associated with.
    region_x: NotRequired[str]  # Relative horizontal region coordinate (between 0 and 1).
    region_y: NotRequired[str]  # Relative vertical region coordinate (between 0 and 1).
    firmware_provision: NotRequired[str]  # Firmware version to provision to this FortiAP on bootup (maj
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
    tun_mtu_downlink: NotRequired[int]  # The MTU of downlink CAPWAP tunnel (576 - 1500 bytes or 0; 0 
    override_split_tunnel: NotRequired[Literal["enable", "disable"]]  # Enable/disable overriding the WTP profile split tunneling se
    split_tunneling_acl_path: NotRequired[Literal["tunnel", "local"]]  # Split tunneling ACL path is local/tunnel.
    split_tunneling_acl_local_ap_subnet: NotRequired[Literal["enable", "disable"]]  # Enable/disable automatically adding local subnetwork of Fort
    split_tunneling_acl: NotRequired[list[dict[str, Any]]]  # Split tunneling ACL filter list.
    override_lan: NotRequired[Literal["enable", "disable"]]  # Enable to override the WTP profile LAN port setting.
    lan: NotRequired[str]  # WTP LAN port mapping.
    override_allowaccess: NotRequired[Literal["enable", "disable"]]  # Enable to override the WTP profile management access configu
    allowaccess: NotRequired[Literal["https", "ssh", "snmp"]]  # Control management access to the managed WTP, FortiAP, or AP
    override_login_passwd_change: NotRequired[Literal["enable", "disable"]]  # Enable to override the WTP profile login-password (administr
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


class Wtp:
    """
    Configure Wireless Termination Points (WTPs), that is, FortiAPs or APs to be managed by FortiGate.
    
    Path: wireless_controller/wtp
    Category: cmdb
    Primary Key: wtp-id
    """
    
    def get(
        self,
        wtp_id: str | None = ...,
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
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
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
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def delete(
        self,
        wtp_id: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def exists(
        self,
        wtp_id: str,
        vdom: str | bool | None = ...,
    ) -> Union[bool, Coroutine[Any, Any, bool]]: ...
    
    def set(
        self,
        payload_dict: WtpPayload | None = ...,
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