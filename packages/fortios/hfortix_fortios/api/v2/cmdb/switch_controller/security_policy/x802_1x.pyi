from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class X8021xPayload(TypedDict, total=False):
    """
    Type hints for switch_controller/security_policy/x802_1x payload fields.
    
    Configure 802.1x MAC Authentication Bypass (MAB) policies.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: auth-fail-vlan-id, authserver-timeout-tagged-vlanid, authserver-timeout-vlanid, +1 more)

    **Usage:**
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
    eap_passthru: NotRequired[Literal["disable", "enable"]]  # Enable/disable EAP pass-through mode, allowing protocols
    eap_auto_untagged_vlans: NotRequired[Literal["disable", "enable"]]  # Enable/disable automatic inclusion of untagged VLANs.
    guest_vlan: NotRequired[Literal["disable", "enable"]]  # Enable the guest VLAN feature to allow limited access to non
    guest_vlan_id: str  # Guest VLAN name.
    guest_auth_delay: NotRequired[int]  # Guest authentication delay (1 - 900  sec, default = 30).
    auth_fail_vlan: NotRequired[Literal["disable", "enable"]]  # Enable to allow limited access to clients that cannot authen
    auth_fail_vlan_id: str  # VLAN ID on which authentication failed.
    framevid_apply: NotRequired[Literal["disable", "enable"]]  # Enable/disable the capability to apply the EAP/MAB frame VLA
    radius_timeout_overwrite: NotRequired[Literal["disable", "enable"]]  # Enable to override the global RADIUS session timeout.
    policy_type: NotRequired[Literal["802.1X"]]  # Policy type.
    authserver_timeout_period: NotRequired[int]  # Authentication server timeout period
    authserver_timeout_vlan: NotRequired[Literal["disable", "enable"]]  # Enable/disable the authentication server timeout VLAN to all
    authserver_timeout_vlanid: str  # Authentication server timeout VLAN name.
    authserver_timeout_tagged: NotRequired[Literal["disable", "lldp-voice", "static"]]  # Configure timeout option for the tagged VLAN which allows li
    authserver_timeout_tagged_vlanid: str  # Tagged VLAN name for which the timeout option is applied to
    dacl: NotRequired[Literal["disable", "enable"]]  # Enable/disable dynamic access control list on this interface

# Nested classes for table field children

@final
class X8021xUsergroupObject:
    """Typed object for user-group table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Group name.
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
class X8021xResponse(TypedDict):
    """
    Type hints for switch_controller/security_policy/x802_1x API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    security_mode: Literal["802.1X", "802.1X-mac-based"]
    user_group: list[dict[str, Any]]
    mac_auth_bypass: Literal["disable", "enable"]
    auth_order: Literal["dot1x-mab", "mab-dot1x", "mab"]
    auth_priority: Literal["legacy", "dot1x-mab", "mab-dot1x"]
    open_auth: Literal["disable", "enable"]
    eap_passthru: Literal["disable", "enable"]
    eap_auto_untagged_vlans: Literal["disable", "enable"]
    guest_vlan: Literal["disable", "enable"]
    guest_vlan_id: str
    guest_auth_delay: int
    auth_fail_vlan: Literal["disable", "enable"]
    auth_fail_vlan_id: str
    framevid_apply: Literal["disable", "enable"]
    radius_timeout_overwrite: Literal["disable", "enable"]
    policy_type: Literal["802.1X"]
    authserver_timeout_period: int
    authserver_timeout_vlan: Literal["disable", "enable"]
    authserver_timeout_vlanid: str
    authserver_timeout_tagged: Literal["disable", "lldp-voice", "static"]
    authserver_timeout_tagged_vlanid: str
    dacl: Literal["disable", "enable"]


@final
class X8021xObject:
    """Typed FortiObject for switch_controller/security_policy/x802_1x with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Policy name.
    name: str
    # Port or MAC based 802.1X security mode.
    security_mode: Literal["802.1X", "802.1X-mac-based"]
    # Name of user-group to assign to this MAC Authentication Bypass (MAB) policy.
    user_group: list[X8021xUsergroupObject]  # Table field - list of typed objects
    # Enable/disable MAB for this policy.
    mac_auth_bypass: Literal["disable", "enable"]
    # Configure authentication order.
    auth_order: Literal["dot1x-mab", "mab-dot1x", "mab"]
    # Configure authentication priority.
    auth_priority: Literal["legacy", "dot1x-mab", "mab-dot1x"]
    # Enable/disable open authentication for this policy.
    open_auth: Literal["disable", "enable"]
    # Enable/disable EAP pass-through mode, allowing protocols (such as LLDP) to pass
    eap_passthru: Literal["disable", "enable"]
    # Enable/disable automatic inclusion of untagged VLANs.
    eap_auto_untagged_vlans: Literal["disable", "enable"]
    # Enable the guest VLAN feature to allow limited access to non-802.1X-compliant cl
    guest_vlan: Literal["disable", "enable"]
    # Guest VLAN name.
    guest_vlan_id: str
    # Guest authentication delay (1 - 900  sec, default = 30).
    guest_auth_delay: int
    # Enable to allow limited access to clients that cannot authenticate.
    auth_fail_vlan: Literal["disable", "enable"]
    # VLAN ID on which authentication failed.
    auth_fail_vlan_id: str
    # Enable/disable the capability to apply the EAP/MAB frame VLAN to the port native
    framevid_apply: Literal["disable", "enable"]
    # Enable to override the global RADIUS session timeout.
    radius_timeout_overwrite: Literal["disable", "enable"]
    # Policy type.
    policy_type: Literal["802.1X"]
    # Authentication server timeout period (3 - 15 sec, default = 3).
    authserver_timeout_period: int
    # Enable/disable the authentication server timeout VLAN to allow limited access wh
    authserver_timeout_vlan: Literal["disable", "enable"]
    # Authentication server timeout VLAN name.
    authserver_timeout_vlanid: str
    # Configure timeout option for the tagged VLAN which allows limited access when th
    authserver_timeout_tagged: Literal["disable", "lldp-voice", "static"]
    # Tagged VLAN name for which the timeout option is applied to (only one VLAN ID).
    authserver_timeout_tagged_vlanid: str
    # Enable/disable dynamic access control list on this interface.
    dacl: Literal["disable", "enable"]
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> X8021xPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class X8021x:
    """
    Configure 802.1x MAC Authentication Bypass (MAB) policies.
    
    Path: switch_controller/security_policy/x802_1x
    Category: cmdb
    Primary Key: name
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey/name provided as positional arg)
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
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> X8021xObject: ...
    
    # Single object (mkey/name provided as keyword arg)
    @overload
    def get(
        self,
        *,
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
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> X8021xObject: ...
    
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
    ) -> list[X8021xObject]: ...
    
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
        raw_json: Literal[True] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Dict mode with mkey provided as positional arg (single dict)
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
    ) -> X8021xResponse: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
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
    ) -> X8021xResponse: ...
    
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
    ) -> list[X8021xResponse]: ...
    
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
    ) -> X8021xObject | list[X8021xObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: X8021xPayload | None = ...,
        name: str | None = ...,
        security_mode: Literal["802.1X", "802.1X-mac-based"] | None = ...,
        user_group: str | list[str] | list[dict[str, Any]] | None = ...,
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> X8021xObject: ...
    
    @overload
    def post(
        self,
        payload_dict: X8021xPayload | None = ...,
        name: str | None = ...,
        security_mode: Literal["802.1X", "802.1X-mac-based"] | None = ...,
        user_group: str | list[str] | list[dict[str, Any]] | None = ...,
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: X8021xPayload | None = ...,
        name: str | None = ...,
        security_mode: Literal["802.1X", "802.1X-mac-based"] | None = ...,
        user_group: str | list[str] | list[dict[str, Any]] | None = ...,
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
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: X8021xPayload | None = ...,
        name: str | None = ...,
        security_mode: Literal["802.1X", "802.1X-mac-based"] | None = ...,
        user_group: str | list[str] | list[dict[str, Any]] | None = ...,
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
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: X8021xPayload | None = ...,
        name: str | None = ...,
        security_mode: Literal["802.1X", "802.1X-mac-based"] | None = ...,
        user_group: str | list[str] | list[dict[str, Any]] | None = ...,
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> X8021xObject: ...
    
    @overload
    def put(
        self,
        payload_dict: X8021xPayload | None = ...,
        name: str | None = ...,
        security_mode: Literal["802.1X", "802.1X-mac-based"] | None = ...,
        user_group: str | list[str] | list[dict[str, Any]] | None = ...,
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: X8021xPayload | None = ...,
        name: str | None = ...,
        security_mode: Literal["802.1X", "802.1X-mac-based"] | None = ...,
        user_group: str | list[str] | list[dict[str, Any]] | None = ...,
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
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: X8021xPayload | None = ...,
        name: str | None = ...,
        security_mode: Literal["802.1X", "802.1X-mac-based"] | None = ...,
        user_group: str | list[str] | list[dict[str, Any]] | None = ...,
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
    ) -> X8021xObject: ...
    
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
        payload_dict: X8021xPayload | None = ...,
        name: str | None = ...,
        security_mode: Literal["802.1X", "802.1X-mac-based"] | None = ...,
        user_group: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "X8021x",
    "X8021xPayload",
    "X8021xObject",
]