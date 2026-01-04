from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class FabricVpnPayload(TypedDict, total=False):
    """
    Type hints for system/fabric_vpn payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: FabricVpnPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    status: Literal["enable", "disable"]  # Enable/disable Fabric VPN.
    sync_mode: Literal["enable", "disable"]  # Setting synchronised by fabric or manual.
    branch_name: NotRequired[str]  # Branch name.
    policy_rule: NotRequired[Literal["health-check", "manual", "auto"]]  # Policy creation rule.
    vpn_role: Literal["hub", "spoke"]  # Fabric VPN role.
    overlays: NotRequired[list[dict[str, Any]]]  # Local overlay interfaces table.
    advertised_subnets: NotRequired[list[dict[str, Any]]]  # Local advertised subnets.
    loopback_address_block: str  # IPv4 address and subnet mask for hub's loopback address, syn
    loopback_interface: NotRequired[str]  # Loopback interface.
    loopback_advertised_subnet: NotRequired[int]  # Loopback advertised subnet reference.
    psksecret: str  # Pre-shared secret for ADVPN.
    bgp_as: str  # BGP Router AS number, asplain/asdot/asdot+ format.
    sdwan_zone: NotRequired[str]  # Reference to created SD-WAN zone.
    health_checks: NotRequired[str]  # Underlying health checks.


class FabricVpn:
    """
    Setup for self orchestrated fabric auto discovery VPN.
    
    Path: system/fabric_vpn
    Category: cmdb
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
        payload_dict: FabricVpnPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        sync_mode: Literal["enable", "disable"] | None = ...,
        branch_name: str | None = ...,
        policy_rule: Literal["health-check", "manual", "auto"] | None = ...,
        vpn_role: Literal["hub", "spoke"] | None = ...,
        overlays: list[dict[str, Any]] | None = ...,
        advertised_subnets: list[dict[str, Any]] | None = ...,
        loopback_address_block: str | None = ...,
        loopback_interface: str | None = ...,
        loopback_advertised_subnet: int | None = ...,
        psksecret: str | None = ...,
        bgp_as: str | None = ...,
        sdwan_zone: str | None = ...,
        health_checks: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: FabricVpnPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        sync_mode: Literal["enable", "disable"] | None = ...,
        branch_name: str | None = ...,
        policy_rule: Literal["health-check", "manual", "auto"] | None = ...,
        vpn_role: Literal["hub", "spoke"] | None = ...,
        overlays: list[dict[str, Any]] | None = ...,
        advertised_subnets: list[dict[str, Any]] | None = ...,
        loopback_address_block: str | None = ...,
        loopback_interface: str | None = ...,
        loopback_advertised_subnet: int | None = ...,
        psksecret: str | None = ...,
        bgp_as: str | None = ...,
        sdwan_zone: str | None = ...,
        health_checks: str | None = ...,
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
        payload_dict: FabricVpnPayload | None = ...,
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