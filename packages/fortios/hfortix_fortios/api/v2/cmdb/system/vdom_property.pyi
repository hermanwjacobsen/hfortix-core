from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class VdomPropertyPayload(TypedDict, total=False):
    """
    Type hints for system/vdom_property payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: VdomPropertyPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # VDOM name.
    description: NotRequired[str]  # Description.
    snmp_index: NotRequired[int]  # Permanent SNMP Index of the virtual domain (1 - 2147483647).
    session: NotRequired[str]  # Maximum guaranteed number of sessions.
    ipsec_phase1: NotRequired[str]  # Maximum guaranteed number of VPN IPsec phase 1 tunnels.
    ipsec_phase2: NotRequired[str]  # Maximum guaranteed number of VPN IPsec phase 2 tunnels.
    ipsec_phase1_interface: NotRequired[str]  # Maximum guaranteed number of VPN IPsec phase1 interface tunn
    ipsec_phase2_interface: NotRequired[str]  # Maximum guaranteed number of VPN IPsec phase2 interface tunn
    dialup_tunnel: NotRequired[str]  # Maximum guaranteed number of dial-up tunnels.
    firewall_policy: NotRequired[str]  # Maximum guaranteed number of firewall policies (policy, DoS-
    firewall_address: NotRequired[str]  # Maximum guaranteed number of firewall addresses (IPv4, IPv6,
    firewall_addrgrp: NotRequired[str]  # Maximum guaranteed number of firewall address groups (IPv4, 
    custom_service: NotRequired[str]  # Maximum guaranteed number of firewall custom services.
    service_group: NotRequired[str]  # Maximum guaranteed number of firewall service groups.
    onetime_schedule: NotRequired[str]  # Maximum guaranteed number of firewall one-time schedules..
    recurring_schedule: NotRequired[str]  # Maximum guaranteed number of firewall recurring schedules.
    user: NotRequired[str]  # Maximum guaranteed number of local users.
    user_group: NotRequired[str]  # Maximum guaranteed number of user groups.
    sslvpn: NotRequired[str]  # Maximum guaranteed number of Agentless VPNs.
    proxy: NotRequired[str]  # Maximum guaranteed number of concurrent proxy users.
    log_disk_quota: NotRequired[str]  # Log disk quota in megabytes (MB). Range depends on how much 


class VdomProperty:
    """
    Configure VDOM property.
    
    Path: system/vdom_property
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
        payload_dict: VdomPropertyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        snmp_index: int | None = ...,
        session: str | None = ...,
        ipsec_phase1: str | None = ...,
        ipsec_phase2: str | None = ...,
        ipsec_phase1_interface: str | None = ...,
        ipsec_phase2_interface: str | None = ...,
        dialup_tunnel: str | None = ...,
        firewall_policy: str | None = ...,
        firewall_address: str | None = ...,
        firewall_addrgrp: str | None = ...,
        custom_service: str | None = ...,
        service_group: str | None = ...,
        onetime_schedule: str | None = ...,
        recurring_schedule: str | None = ...,
        user: str | None = ...,
        user_group: str | None = ...,
        sslvpn: str | None = ...,
        proxy: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: VdomPropertyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        snmp_index: int | None = ...,
        session: str | None = ...,
        ipsec_phase1: str | None = ...,
        ipsec_phase2: str | None = ...,
        ipsec_phase1_interface: str | None = ...,
        ipsec_phase2_interface: str | None = ...,
        dialup_tunnel: str | None = ...,
        firewall_policy: str | None = ...,
        firewall_address: str | None = ...,
        firewall_addrgrp: str | None = ...,
        custom_service: str | None = ...,
        service_group: str | None = ...,
        onetime_schedule: str | None = ...,
        recurring_schedule: str | None = ...,
        user: str | None = ...,
        user_group: str | None = ...,
        sslvpn: str | None = ...,
        proxy: str | None = ...,
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
        payload_dict: VdomPropertyPayload | None = ...,
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