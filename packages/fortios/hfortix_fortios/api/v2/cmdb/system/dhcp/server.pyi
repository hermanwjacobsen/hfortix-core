""" - Type Stubs

Auto-generated stub file for type checking and IDE support.

Endpoint: system/dhcp/server
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

class ServerIprangeItem:
    """Nested item for ip-range field - supports attribute access."""
    id: int
    start_ip: str
    end_ip: str
    vci_match: Literal["disable", "enable"]
    vci_string: str
    uci_match: Literal["disable", "enable"]
    uci_string: str
    lease_time: int


class ServerTftpserverItem:
    """Nested item for tftp-server field - supports attribute access."""
    tftp_server: str


class ServerOptionsItem:
    """Nested item for options field - supports attribute access."""
    id: int
    code: int
    type: Literal["hex", "string", "ip", "fqdn"]
    value: str
    ip: str
    vci_match: Literal["disable", "enable"]
    vci_string: str
    uci_match: Literal["disable", "enable"]
    uci_string: str


class ServerVcistringItem:
    """Nested item for vci-string field - supports attribute access."""
    vci_string: str


class ServerExcluderangeItem:
    """Nested item for exclude-range field - supports attribute access."""
    id: int
    start_ip: str
    end_ip: str
    vci_match: Literal["disable", "enable"]
    vci_string: str
    uci_match: Literal["disable", "enable"]
    uci_string: str
    lease_time: int


class ServerReservedaddressItem:
    """Nested item for reserved-address field - supports attribute access."""
    id: int
    type: Literal["mac", "option82"]
    ip: str
    mac: str
    action: Literal["assign", "block", "reserved"]
    circuit_id_type: Literal["hex", "string"]
    circuit_id: str
    remote_id_type: Literal["hex", "string"]
    remote_id: str
    description: str


class ServerPayload(TypedDict, total=False):
    """Payload type for Server operations."""
    id: int
    status: Literal["disable", "enable"]
    lease_time: int
    mac_acl_default_action: Literal["assign", "block"]
    forticlient_on_net_status: Literal["disable", "enable"]
    dns_service: Literal["local", "default", "specify"]
    dns_server1: str
    dns_server2: str
    dns_server3: str
    dns_server4: str
    wifi_ac_service: Literal["specify", "local"]
    wifi_ac1: str
    wifi_ac2: str
    wifi_ac3: str
    ntp_service: Literal["local", "default", "specify"]
    ntp_server1: str
    ntp_server2: str
    ntp_server3: str
    domain: str
    wins_server1: str
    wins_server2: str
    default_gateway: str
    next_server: str
    netmask: str
    interface: str
    ip_range: str | list[str] | list[dict[str, Any]] | list[ServerIprangeItem]
    timezone_option: Literal["disable", "default", "specify"]
    timezone: str
    tftp_server: str | list[str] | list[dict[str, Any]] | list[ServerTftpserverItem]
    filename: str
    options: str | list[str] | list[dict[str, Any]] | list[ServerOptionsItem]
    server_type: Literal["regular", "ipsec"]
    ip_mode: Literal["range", "usrgrp"]
    conflicted_ip_timeout: int
    ipsec_lease_hold: int
    auto_configuration: Literal["disable", "enable"]
    dhcp_settings_from_fortiipam: Literal["disable", "enable"]
    auto_managed_status: Literal["disable", "enable"]
    ddns_update: Literal["disable", "enable"]
    ddns_update_override: Literal["disable", "enable"]
    ddns_server_ip: str
    ddns_zone: str
    ddns_auth: Literal["disable", "tsig"]
    ddns_keyname: str
    ddns_key: str
    ddns_ttl: int
    vci_match: Literal["disable", "enable"]
    vci_string: str | list[str] | list[dict[str, Any]] | list[ServerVcistringItem]
    exclude_range: str | list[str] | list[dict[str, Any]] | list[ServerExcluderangeItem]
    shared_subnet: Literal["disable", "enable"]
    relay_agent: str
    reserved_address: str | list[str] | list[dict[str, Any]] | list[ServerReservedaddressItem]


# ================================================================
# Response Types (TypedDict for dict-style access)
# ================================================================

class ServerResponse(TypedDict, total=False):
    """Response type for Server - use with .dict property for typed dict access."""
    id: int
    status: Literal["disable", "enable"]
    lease_time: int
    mac_acl_default_action: Literal["assign", "block"]
    forticlient_on_net_status: Literal["disable", "enable"]
    dns_service: Literal["local", "default", "specify"]
    dns_server1: str
    dns_server2: str
    dns_server3: str
    dns_server4: str
    wifi_ac_service: Literal["specify", "local"]
    wifi_ac1: str
    wifi_ac2: str
    wifi_ac3: str
    ntp_service: Literal["local", "default", "specify"]
    ntp_server1: str
    ntp_server2: str
    ntp_server3: str
    domain: str
    wins_server1: str
    wins_server2: str
    default_gateway: str
    next_server: str
    netmask: str
    interface: str
    ip_range: list[ServerIprangeItem]
    timezone_option: Literal["disable", "default", "specify"]
    timezone: str
    tftp_server: list[ServerTftpserverItem]
    filename: str
    options: list[ServerOptionsItem]
    server_type: Literal["regular", "ipsec"]
    ip_mode: Literal["range", "usrgrp"]
    conflicted_ip_timeout: int
    ipsec_lease_hold: int
    auto_configuration: Literal["disable", "enable"]
    dhcp_settings_from_fortiipam: Literal["disable", "enable"]
    auto_managed_status: Literal["disable", "enable"]
    ddns_update: Literal["disable", "enable"]
    ddns_update_override: Literal["disable", "enable"]
    ddns_server_ip: str
    ddns_zone: str
    ddns_auth: Literal["disable", "tsig"]
    ddns_keyname: str
    ddns_key: str
    ddns_ttl: int
    vci_match: Literal["disable", "enable"]
    vci_string: list[ServerVcistringItem]
    exclude_range: list[ServerExcluderangeItem]
    shared_subnet: Literal["disable", "enable"]
    relay_agent: str
    reserved_address: list[ServerReservedaddressItem]


# ================================================================
# Response Types (Class for attribute access)
# ================================================================


class ServerObject(FortiObject):
    """Typed FortiObject for Server with field access."""
    id: int
    status: Literal["disable", "enable"]
    lease_time: int
    mac_acl_default_action: Literal["assign", "block"]
    forticlient_on_net_status: Literal["disable", "enable"]
    dns_service: Literal["local", "default", "specify"]
    dns_server1: str
    dns_server2: str
    dns_server3: str
    dns_server4: str
    wifi_ac_service: Literal["specify", "local"]
    wifi_ac1: str
    wifi_ac2: str
    wifi_ac3: str
    ntp_service: Literal["local", "default", "specify"]
    ntp_server1: str
    ntp_server2: str
    ntp_server3: str
    domain: str
    wins_server1: str
    wins_server2: str
    default_gateway: str
    next_server: str
    netmask: str
    interface: str
    ip_range: list[ServerIprangeItem]
    timezone_option: Literal["disable", "default", "specify"]
    timezone: str
    tftp_server: list[ServerTftpserverItem]
    filename: str
    options: list[ServerOptionsItem]
    server_type: Literal["regular", "ipsec"]
    ip_mode: Literal["range", "usrgrp"]
    conflicted_ip_timeout: int
    ipsec_lease_hold: int
    auto_configuration: Literal["disable", "enable"]
    dhcp_settings_from_fortiipam: Literal["disable", "enable"]
    auto_managed_status: Literal["disable", "enable"]
    ddns_update: Literal["disable", "enable"]
    ddns_update_override: Literal["disable", "enable"]
    ddns_server_ip: str
    ddns_zone: str
    ddns_auth: Literal["disable", "tsig"]
    ddns_keyname: str
    ddns_key: str
    ddns_ttl: int
    vci_match: Literal["disable", "enable"]
    vci_string: list[ServerVcistringItem]
    exclude_range: list[ServerExcluderangeItem]
    shared_subnet: Literal["disable", "enable"]
    relay_agent: str
    reserved_address: list[ServerReservedaddressItem]


# ================================================================
# Main Endpoint Class
# ================================================================

class Server:
    """
    
    Endpoint: system/dhcp/server
    Category: cmdb
    MKey: id
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
        id: int,
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
    ) -> ServerObject: ...
    
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
    ) -> FortiObjectList[ServerObject]: ...
    
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
        payload_dict: ServerPayload | None = ...,
        id: int | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        lease_time: int | None = ...,
        mac_acl_default_action: Literal["assign", "block"] | None = ...,
        forticlient_on_net_status: Literal["disable", "enable"] | None = ...,
        dns_service: Literal["local", "default", "specify"] | None = ...,
        dns_server1: str | None = ...,
        dns_server2: str | None = ...,
        dns_server3: str | None = ...,
        dns_server4: str | None = ...,
        wifi_ac_service: Literal["specify", "local"] | None = ...,
        wifi_ac1: str | None = ...,
        wifi_ac2: str | None = ...,
        wifi_ac3: str | None = ...,
        ntp_service: Literal["local", "default", "specify"] | None = ...,
        ntp_server1: str | None = ...,
        ntp_server2: str | None = ...,
        ntp_server3: str | None = ...,
        domain: str | None = ...,
        wins_server1: str | None = ...,
        wins_server2: str | None = ...,
        default_gateway: str | None = ...,
        next_server: str | None = ...,
        netmask: str | None = ...,
        interface: str | None = ...,
        ip_range: str | list[str] | list[dict[str, Any]] | list[ServerIprangeItem] | None = ...,
        timezone_option: Literal["disable", "default", "specify"] | None = ...,
        timezone: str | None = ...,
        tftp_server: str | list[str] | list[dict[str, Any]] | list[ServerTftpserverItem] | None = ...,
        filename: str | None = ...,
        options: str | list[str] | list[dict[str, Any]] | list[ServerOptionsItem] | None = ...,
        server_type: Literal["regular", "ipsec"] | None = ...,
        ip_mode: Literal["range", "usrgrp"] | None = ...,
        conflicted_ip_timeout: int | None = ...,
        ipsec_lease_hold: int | None = ...,
        auto_configuration: Literal["disable", "enable"] | None = ...,
        dhcp_settings_from_fortiipam: Literal["disable", "enable"] | None = ...,
        auto_managed_status: Literal["disable", "enable"] | None = ...,
        ddns_update: Literal["disable", "enable"] | None = ...,
        ddns_update_override: Literal["disable", "enable"] | None = ...,
        ddns_server_ip: str | None = ...,
        ddns_zone: str | None = ...,
        ddns_auth: Literal["disable", "tsig"] | None = ...,
        ddns_keyname: str | None = ...,
        ddns_key: str | None = ...,
        ddns_ttl: int | None = ...,
        vci_match: Literal["disable", "enable"] | None = ...,
        vci_string: str | list[str] | list[dict[str, Any]] | list[ServerVcistringItem] | None = ...,
        exclude_range: str | list[str] | list[dict[str, Any]] | list[ServerExcluderangeItem] | None = ...,
        shared_subnet: Literal["disable", "enable"] | None = ...,
        relay_agent: str | None = ...,
        reserved_address: str | list[str] | list[dict[str, Any]] | list[ServerReservedaddressItem] | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> ServerObject: ...

    # ================================================================
    # PUT Method
    # ================================================================
    
    def put(
        self,
        payload_dict: ServerPayload | None = ...,
        id: int | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        lease_time: int | None = ...,
        mac_acl_default_action: Literal["assign", "block"] | None = ...,
        forticlient_on_net_status: Literal["disable", "enable"] | None = ...,
        dns_service: Literal["local", "default", "specify"] | None = ...,
        dns_server1: str | None = ...,
        dns_server2: str | None = ...,
        dns_server3: str | None = ...,
        dns_server4: str | None = ...,
        wifi_ac_service: Literal["specify", "local"] | None = ...,
        wifi_ac1: str | None = ...,
        wifi_ac2: str | None = ...,
        wifi_ac3: str | None = ...,
        ntp_service: Literal["local", "default", "specify"] | None = ...,
        ntp_server1: str | None = ...,
        ntp_server2: str | None = ...,
        ntp_server3: str | None = ...,
        domain: str | None = ...,
        wins_server1: str | None = ...,
        wins_server2: str | None = ...,
        default_gateway: str | None = ...,
        next_server: str | None = ...,
        netmask: str | None = ...,
        interface: str | None = ...,
        ip_range: str | list[str] | list[dict[str, Any]] | list[ServerIprangeItem] | None = ...,
        timezone_option: Literal["disable", "default", "specify"] | None = ...,
        timezone: str | None = ...,
        tftp_server: str | list[str] | list[dict[str, Any]] | list[ServerTftpserverItem] | None = ...,
        filename: str | None = ...,
        options: str | list[str] | list[dict[str, Any]] | list[ServerOptionsItem] | None = ...,
        server_type: Literal["regular", "ipsec"] | None = ...,
        ip_mode: Literal["range", "usrgrp"] | None = ...,
        conflicted_ip_timeout: int | None = ...,
        ipsec_lease_hold: int | None = ...,
        auto_configuration: Literal["disable", "enable"] | None = ...,
        dhcp_settings_from_fortiipam: Literal["disable", "enable"] | None = ...,
        auto_managed_status: Literal["disable", "enable"] | None = ...,
        ddns_update: Literal["disable", "enable"] | None = ...,
        ddns_update_override: Literal["disable", "enable"] | None = ...,
        ddns_server_ip: str | None = ...,
        ddns_zone: str | None = ...,
        ddns_auth: Literal["disable", "tsig"] | None = ...,
        ddns_keyname: str | None = ...,
        ddns_key: str | None = ...,
        ddns_ttl: int | None = ...,
        vci_match: Literal["disable", "enable"] | None = ...,
        vci_string: str | list[str] | list[dict[str, Any]] | list[ServerVcistringItem] | None = ...,
        exclude_range: str | list[str] | list[dict[str, Any]] | list[ServerExcluderangeItem] | None = ...,
        shared_subnet: Literal["disable", "enable"] | None = ...,
        relay_agent: str | None = ...,
        reserved_address: str | list[str] | list[dict[str, Any]] | list[ServerReservedaddressItem] | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> ServerObject: ...

    # ================================================================
    # DELETE Method
    # ================================================================
    
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> FortiObject: ...

    # ================================================================
    # Utility Methods
    # ================================================================
    
    def exists(
        self,
        id: int,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: ServerPayload | None = ...,
        id: int | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        lease_time: int | None = ...,
        mac_acl_default_action: Literal["assign", "block"] | None = ...,
        forticlient_on_net_status: Literal["disable", "enable"] | None = ...,
        dns_service: Literal["local", "default", "specify"] | None = ...,
        dns_server1: str | None = ...,
        dns_server2: str | None = ...,
        dns_server3: str | None = ...,
        dns_server4: str | None = ...,
        wifi_ac_service: Literal["specify", "local"] | None = ...,
        wifi_ac1: str | None = ...,
        wifi_ac2: str | None = ...,
        wifi_ac3: str | None = ...,
        ntp_service: Literal["local", "default", "specify"] | None = ...,
        ntp_server1: str | None = ...,
        ntp_server2: str | None = ...,
        ntp_server3: str | None = ...,
        domain: str | None = ...,
        wins_server1: str | None = ...,
        wins_server2: str | None = ...,
        default_gateway: str | None = ...,
        next_server: str | None = ...,
        netmask: str | None = ...,
        interface: str | None = ...,
        ip_range: str | list[str] | list[dict[str, Any]] | list[ServerIprangeItem] | None = ...,
        timezone_option: Literal["disable", "default", "specify"] | None = ...,
        timezone: str | None = ...,
        tftp_server: str | list[str] | list[dict[str, Any]] | list[ServerTftpserverItem] | None = ...,
        filename: str | None = ...,
        options: str | list[str] | list[dict[str, Any]] | list[ServerOptionsItem] | None = ...,
        server_type: Literal["regular", "ipsec"] | None = ...,
        ip_mode: Literal["range", "usrgrp"] | None = ...,
        conflicted_ip_timeout: int | None = ...,
        ipsec_lease_hold: int | None = ...,
        auto_configuration: Literal["disable", "enable"] | None = ...,
        dhcp_settings_from_fortiipam: Literal["disable", "enable"] | None = ...,
        auto_managed_status: Literal["disable", "enable"] | None = ...,
        ddns_update: Literal["disable", "enable"] | None = ...,
        ddns_update_override: Literal["disable", "enable"] | None = ...,
        ddns_server_ip: str | None = ...,
        ddns_zone: str | None = ...,
        ddns_auth: Literal["disable", "tsig"] | None = ...,
        ddns_keyname: str | None = ...,
        ddns_key: str | None = ...,
        ddns_ttl: int | None = ...,
        vci_match: Literal["disable", "enable"] | None = ...,
        vci_string: str | list[str] | list[dict[str, Any]] | list[ServerVcistringItem] | None = ...,
        exclude_range: str | list[str] | list[dict[str, Any]] | list[ServerExcluderangeItem] | None = ...,
        shared_subnet: Literal["disable", "enable"] | None = ...,
        relay_agent: str | None = ...,
        reserved_address: str | list[str] | list[dict[str, Any]] | list[ServerReservedaddressItem] | None = ...,
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
    "Server",
    "ServerPayload",
    "ServerResponse",
    "ServerObject",
]