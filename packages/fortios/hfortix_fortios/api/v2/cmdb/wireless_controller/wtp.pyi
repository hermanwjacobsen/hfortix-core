""" - Type Stubs

Auto-generated stub file for type checking and IDE support.

Endpoint: wireless_controller/wtp
Category: cmdb
"""

from __future__ import annotations

from typing import (
    Any,
    ClassVar,
    Literal,
    TypedDict,
    overload,
)

from hfortix_fortios.models import (
    FortiObject,
    FortiObjectList,
)


# ================================================================
# TypedDict Payloads
# ================================================================

class WtpSplittunnelingaclItem:
    """Nested item for split-tunneling-acl field - supports attribute access."""
    id: int
    dest_ip: str


class WtpPayload(TypedDict, total=False):
    """Payload type for Wtp operations."""
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
    ip_fragment_preventing: str | list[str]
    tun_mtu_uplink: int
    tun_mtu_downlink: int
    override_split_tunnel: Literal["enable", "disable"]
    split_tunneling_acl_path: Literal["tunnel", "local"]
    split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"]
    split_tunneling_acl: str | list[str] | list[dict[str, Any]] | list[WtpSplittunnelingaclItem]
    override_lan: Literal["enable", "disable"]
    lan: str
    override_allowaccess: Literal["enable", "disable"]
    allowaccess: str | list[str]
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


# ================================================================
# Response Types (TypedDict for dict-style access)
# ================================================================

class WtpResponse(TypedDict, total=False):
    """Response type for Wtp - use with .dict property for typed dict access."""
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
    ip_fragment_preventing: str
    tun_mtu_uplink: int
    tun_mtu_downlink: int
    override_split_tunnel: Literal["enable", "disable"]
    split_tunneling_acl_path: Literal["tunnel", "local"]
    split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"]
    split_tunneling_acl: list[WtpSplittunnelingaclItem]
    override_lan: Literal["enable", "disable"]
    lan: str
    override_allowaccess: Literal["enable", "disable"]
    allowaccess: str
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


# ================================================================
# Response Types (Class for attribute access)
# ================================================================


class WtpObject(FortiObject):
    """Typed FortiObject for Wtp with field access."""
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
    ip_fragment_preventing: str
    tun_mtu_uplink: int
    tun_mtu_downlink: int
    override_split_tunnel: Literal["enable", "disable"]
    split_tunneling_acl_path: Literal["tunnel", "local"]
    split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"]
    split_tunneling_acl: list[WtpSplittunnelingaclItem]
    override_lan: Literal["enable", "disable"]
    lan: str
    override_allowaccess: Literal["enable", "disable"]
    allowaccess: str
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


# ================================================================
# Main Endpoint Class
# ================================================================

class Wtp:
    """
    
    Endpoint: wireless_controller/wtp
    Category: cmdb
    MKey: wtp-id
    """
    
    # Class attributes for introspection
    endpoint: ClassVar[str] = ...
    path: ClassVar[str] = ...
    category: ClassVar[str] = ...
    mkey: ClassVar[str] = ...
    capabilities: ClassVar[dict[str, Any]] = ...
    
    def __init__(self, client: Any) -> None:
        """Initialize endpoint with HTTP client."""
        ...
    
    # ================================================================
    # GET Methods
    # ================================================================
    
    # CMDB with mkey - overloads for single vs list returns
    @overload
    def get(
        self,
        wtp_id: str,
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
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> WtpObject: ...
    
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
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> FortiObjectList[WtpObject]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...

    # ================================================================
    # POST Method
    # ================================================================
    
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
        ip_fragment_preventing: str | list[str] | None = ...,
        tun_mtu_uplink: int | None = ...,
        tun_mtu_downlink: int | None = ...,
        override_split_tunnel: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl_path: Literal["tunnel", "local"] | None = ...,
        split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl: str | list[str] | list[dict[str, Any]] | list[WtpSplittunnelingaclItem] | None = ...,
        override_lan: Literal["enable", "disable"] | None = ...,
        lan: str | None = ...,
        override_allowaccess: Literal["enable", "disable"] | None = ...,
        allowaccess: str | list[str] | None = ...,
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
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> WtpObject: ...

    # ================================================================
    # PUT Method
    # ================================================================
    
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
        ip_fragment_preventing: str | list[str] | None = ...,
        tun_mtu_uplink: int | None = ...,
        tun_mtu_downlink: int | None = ...,
        override_split_tunnel: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl_path: Literal["tunnel", "local"] | None = ...,
        split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl: str | list[str] | list[dict[str, Any]] | list[WtpSplittunnelingaclItem] | None = ...,
        override_lan: Literal["enable", "disable"] | None = ...,
        lan: str | None = ...,
        override_allowaccess: Literal["enable", "disable"] | None = ...,
        allowaccess: str | list[str] | None = ...,
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
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> WtpObject: ...

    # ================================================================
    # DELETE Method
    # ================================================================
    
    def delete(
        self,
        wtp_id: str | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> FortiObject: ...

    # ================================================================
    # Utility Methods
    # ================================================================
    
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
        split_tunneling_acl: str | list[str] | list[dict[str, Any]] | list[WtpSplittunnelingaclItem] | None = ...,
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
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> FortiObject: ...
    
    # Helper methods
    @staticmethod
    def help(field_name: str | None = ...) -> str: ...
    
    @staticmethod
    def fields(detailed: bool = ...) -> list[str] | list[dict[str, Any]]: ...
    
    @staticmethod
    def field_info(field_name: str) -> FortiObject: ...
    
    @staticmethod
    def validate_field(name: str, value: Any) -> bool: ...
    
    @staticmethod
    def required_fields() -> list[str]: ...
    
    @staticmethod
    def defaults() -> FortiObject: ...
    
    @staticmethod
    def schema() -> FortiObject: ...


__all__ = [
    "Wtp",
    "WtpPayload",
    "WtpResponse",
    "WtpObject",
]