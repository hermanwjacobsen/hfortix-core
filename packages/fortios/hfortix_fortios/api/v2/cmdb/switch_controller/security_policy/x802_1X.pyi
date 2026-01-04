from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class X8021xPayload(TypedDict, total=False):
    """
    Type hints for switch_controller/security_policy/x802_1X payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: X8021xPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Policy name.
    security_mode: NotRequired[Literal["802.1X", "802.1X-mac-based"]]  # Port or MAC based 802.1X security mode.
    user_group: list[dict[str, Any]]  # Name of user-group to assign to this MAC Authentication Bypa
    mac_auth_bypass: NotRequired[Literal["disable", "enable"]]  # Enable/disable MAB for this policy.
    auth_order: NotRequired[Literal["dot1x-mab", "mab-dot1x", "mab"]]  # Configure authentication order.
    auth_priority: NotRequired[Literal["legacy", "dot1x-mab", "mab-dot1x"]]  # Configure authentication priority.
    open_auth: NotRequired[Literal["disable", "enable"]]  # Enable/disable open authentication for this policy.
    eap_passthru: NotRequired[Literal["disable", "enable"]]  # Enable/disable EAP pass-through mode, allowing protocols (su
    eap_auto_untagged_vlans: NotRequired[Literal["disable", "enable"]]  # Enable/disable automatic inclusion of untagged VLANs.
    guest_vlan: NotRequired[Literal["disable", "enable"]]  # Enable the guest VLAN feature to allow limited access to non
    guest_vlan_id: str  # Guest VLAN name.
    guest_auth_delay: NotRequired[int]  # Guest authentication delay (1 - 900  sec, default = 30).
    auth_fail_vlan: NotRequired[Literal["disable", "enable"]]  # Enable to allow limited access to clients that cannot authen
    auth_fail_vlan_id: str  # VLAN ID on which authentication failed.
    framevid_apply: NotRequired[Literal["disable", "enable"]]  # Enable/disable the capability to apply the EAP/MAB frame VLA
    radius_timeout_overwrite: NotRequired[Literal["disable", "enable"]]  # Enable to override the global RADIUS session timeout.
    policy_type: NotRequired[Literal["802.1X"]]  # Policy type.
    authserver_timeout_period: NotRequired[int]  # Authentication server timeout period (3 - 15 sec, default = 
    authserver_timeout_vlan: NotRequired[Literal["disable", "enable"]]  # Enable/disable the authentication server timeout VLAN to all
    authserver_timeout_vlanid: str  # Authentication server timeout VLAN name.
    authserver_timeout_tagged: NotRequired[Literal["disable", "lldp-voice", "static"]]  # Configure timeout option for the tagged VLAN which allows li
    authserver_timeout_tagged_vlanid: str  # Tagged VLAN name for which the timeout option is applied to 
    dacl: NotRequired[Literal["disable", "enable"]]  # Enable/disable dynamic access control list on this interface


class X8021x:
    """
    Configure 802.1x MAC Authentication Bypass (MAB) policies.
    
    Path: switch_controller/security_policy/x802_1X
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
        payload_dict: X8021xPayload | None = ...,
        name: str | None = ...,
        security_mode: Literal["802.1X", "802.1X-mac-based"] | None = ...,
        user_group: list[dict[str, Any]] | None = ...,
        mac_auth_bypass: Literal["disable", "enable"] | None = ...,
        auth_order: Literal["dot1x-mab", "mab-dot1x", "mab"] | None = ...,
        auth_priority: Literal["legacy", "dot1x-mab", "mab-dot1x"] | None = ...,
        open_auth: Literal["disable", "enable"] | None = ...,
        eap_passthru: Literal["disable", "enable"] | None = ...,
        eap_auto_untagged_vlans: Literal["disable", "enable"] | None = ...,
        guest_vlan: Literal["disable", "enable"] | None = ...,
        guest_vlan_id: str | None = ...,
        guest_auth_delay: int | None = ...,
        auth_fail_vlan: Literal["disable", "enable"] | None = ...,
        auth_fail_vlan_id: str | None = ...,
        framevid_apply: Literal["disable", "enable"] | None = ...,
        radius_timeout_overwrite: Literal["disable", "enable"] | None = ...,
        policy_type: Literal["802.1X"] | None = ...,
        authserver_timeout_period: int | None = ...,
        authserver_timeout_vlan: Literal["disable", "enable"] | None = ...,
        authserver_timeout_vlanid: str | None = ...,
        authserver_timeout_tagged: Literal["disable", "lldp-voice", "static"] | None = ...,
        authserver_timeout_tagged_vlanid: str | None = ...,
        dacl: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: X8021xPayload | None = ...,
        name: str | None = ...,
        security_mode: Literal["802.1X", "802.1X-mac-based"] | None = ...,
        user_group: list[dict[str, Any]] | None = ...,
        mac_auth_bypass: Literal["disable", "enable"] | None = ...,
        auth_order: Literal["dot1x-mab", "mab-dot1x", "mab"] | None = ...,
        auth_priority: Literal["legacy", "dot1x-mab", "mab-dot1x"] | None = ...,
        open_auth: Literal["disable", "enable"] | None = ...,
        eap_passthru: Literal["disable", "enable"] | None = ...,
        eap_auto_untagged_vlans: Literal["disable", "enable"] | None = ...,
        guest_vlan: Literal["disable", "enable"] | None = ...,
        guest_vlan_id: str | None = ...,
        guest_auth_delay: int | None = ...,
        auth_fail_vlan: Literal["disable", "enable"] | None = ...,
        auth_fail_vlan_id: str | None = ...,
        framevid_apply: Literal["disable", "enable"] | None = ...,
        radius_timeout_overwrite: Literal["disable", "enable"] | None = ...,
        policy_type: Literal["802.1X"] | None = ...,
        authserver_timeout_period: int | None = ...,
        authserver_timeout_vlan: Literal["disable", "enable"] | None = ...,
        authserver_timeout_vlanid: str | None = ...,
        authserver_timeout_tagged: Literal["disable", "lldp-voice", "static"] | None = ...,
        authserver_timeout_tagged_vlanid: str | None = ...,
        dacl: Literal["disable", "enable"] | None = ...,
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
        payload_dict: X8021xPayload | None = ...,
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


__all__ = [
    "X8021x",
    "X8021xPayload",
]