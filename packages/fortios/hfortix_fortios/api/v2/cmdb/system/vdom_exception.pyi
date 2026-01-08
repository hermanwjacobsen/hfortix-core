from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class VdomExceptionPayload(TypedDict, total=False):
    """
    Type hints for system/vdom_exception payload fields.
    
    Global configuration objects that can be configured independently across different ha peers for all VDOMs or for the defined VDOM scope.
    
    **Usage:**
        payload: VdomExceptionPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    id: NotRequired[int]  # Index (1 - 4096).
    object: Literal["log.fortianalyzer.setting", "log.fortianalyzer.override-setting", "log.fortianalyzer2.setting", "log.fortianalyzer2.override-setting", "log.fortianalyzer3.setting", "log.fortianalyzer3.override-setting", "log.fortianalyzer-cloud.setting", "log.fortianalyzer-cloud.override-setting", "log.syslogd.setting", "log.syslogd.override-setting", "log.syslogd2.setting", "log.syslogd2.override-setting", "log.syslogd3.setting", "log.syslogd3.override-setting", "log.syslogd4.setting", "log.syslogd4.override-setting", "system.gre-tunnel", "system.central-management", "system.csf", "user.radius", "system.interface", "vpn.ipsec.phase1-interface", "vpn.ipsec.phase2-interface", "router.bgp", "router.route-map", "router.prefix-list", "firewall.ippool", "firewall.ippool6", "router.static", "router.static6", "firewall.vip", "firewall.vip6", "system.sdwan", "system.saml", "router.policy", "router.policy6", "log.syslogd.setting", "log.syslogd.override-setting", "firewall.address"]  # Name of the configuration object that can be configured inde
    scope: NotRequired[Literal["all", "inclusive", "exclusive"]]  # Determine whether the configuration object can be configured
    vdom: NotRequired[list[dict[str, Any]]]  # Names of the VDOMs.

# Nested classes for table field children

@final
class VdomExceptionVdomObject:
    """Typed object for vdom table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # VDOM name.
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
class VdomExceptionResponse(TypedDict):
    """
    Type hints for system/vdom_exception API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    id: int
    object: Literal["log.fortianalyzer.setting", "log.fortianalyzer.override-setting", "log.fortianalyzer2.setting", "log.fortianalyzer2.override-setting", "log.fortianalyzer3.setting", "log.fortianalyzer3.override-setting", "log.fortianalyzer-cloud.setting", "log.fortianalyzer-cloud.override-setting", "log.syslogd.setting", "log.syslogd.override-setting", "log.syslogd2.setting", "log.syslogd2.override-setting", "log.syslogd3.setting", "log.syslogd3.override-setting", "log.syslogd4.setting", "log.syslogd4.override-setting", "system.gre-tunnel", "system.central-management", "system.csf", "user.radius", "system.interface", "vpn.ipsec.phase1-interface", "vpn.ipsec.phase2-interface", "router.bgp", "router.route-map", "router.prefix-list", "firewall.ippool", "firewall.ippool6", "router.static", "router.static6", "firewall.vip", "firewall.vip6", "system.sdwan", "system.saml", "router.policy", "router.policy6", "log.syslogd.setting", "log.syslogd.override-setting", "firewall.address"]
    scope: Literal["all", "inclusive", "exclusive"]
    vdom: list[dict[str, Any]]


@final
class VdomExceptionObject:
    """Typed FortiObject for system/vdom_exception with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Index (1 - 4096).
    id: int
    # Name of the configuration object that can be configured independently for all VD
    object: Literal["log.fortianalyzer.setting", "log.fortianalyzer.override-setting", "log.fortianalyzer2.setting", "log.fortianalyzer2.override-setting", "log.fortianalyzer3.setting", "log.fortianalyzer3.override-setting", "log.fortianalyzer-cloud.setting", "log.fortianalyzer-cloud.override-setting", "log.syslogd.setting", "log.syslogd.override-setting", "log.syslogd2.setting", "log.syslogd2.override-setting", "log.syslogd3.setting", "log.syslogd3.override-setting", "log.syslogd4.setting", "log.syslogd4.override-setting", "system.gre-tunnel", "system.central-management", "system.csf", "user.radius", "system.interface", "vpn.ipsec.phase1-interface", "vpn.ipsec.phase2-interface", "router.bgp", "router.route-map", "router.prefix-list", "firewall.ippool", "firewall.ippool6", "router.static", "router.static6", "firewall.vip", "firewall.vip6", "system.sdwan", "system.saml", "router.policy", "router.policy6", "log.syslogd.setting", "log.syslogd.override-setting", "firewall.address"]
    # Determine whether the configuration object can be configured separately for all
    scope: Literal["all", "inclusive", "exclusive"]
    # Names of the VDOMs.
    vdom: list[VdomExceptionVdomObject]  # Table field - list of typed objects
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> VdomExceptionPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class VdomException:
    """
    Global configuration objects that can be configured independently across different ha peers for all VDOMs or for the defined VDOM scope.
    
    Path: system/vdom_exception
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
    ) -> VdomExceptionObject: ...
    
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
    ) -> VdomExceptionObject: ...
    
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
    ) -> list[VdomExceptionObject]: ...
    
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
    ) -> VdomExceptionResponse: ...
    
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
    ) -> VdomExceptionResponse: ...
    
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
    ) -> list[VdomExceptionResponse]: ...
    
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
    ) -> VdomExceptionObject | list[VdomExceptionObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: VdomExceptionPayload | None = ...,
        id: int | None = ...,
        object: Literal["log.fortianalyzer.setting", "log.fortianalyzer.override-setting", "log.fortianalyzer2.setting", "log.fortianalyzer2.override-setting", "log.fortianalyzer3.setting", "log.fortianalyzer3.override-setting", "log.fortianalyzer-cloud.setting", "log.fortianalyzer-cloud.override-setting", "log.syslogd.setting", "log.syslogd.override-setting", "log.syslogd2.setting", "log.syslogd2.override-setting", "log.syslogd3.setting", "log.syslogd3.override-setting", "log.syslogd4.setting", "log.syslogd4.override-setting", "system.gre-tunnel", "system.central-management", "system.csf", "user.radius", "system.interface", "vpn.ipsec.phase1-interface", "vpn.ipsec.phase2-interface", "router.bgp", "router.route-map", "router.prefix-list", "firewall.ippool", "firewall.ippool6", "router.static", "router.static6", "firewall.vip", "firewall.vip6", "system.sdwan", "system.saml", "router.policy", "router.policy6", "log.syslogd.setting", "log.syslogd.override-setting", "firewall.address"] | None = ...,
        scope: Literal["all", "inclusive", "exclusive"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> VdomExceptionObject: ...
    
    @overload
    def post(
        self,
        payload_dict: VdomExceptionPayload | None = ...,
        id: int | None = ...,
        object: Literal["log.fortianalyzer.setting", "log.fortianalyzer.override-setting", "log.fortianalyzer2.setting", "log.fortianalyzer2.override-setting", "log.fortianalyzer3.setting", "log.fortianalyzer3.override-setting", "log.fortianalyzer-cloud.setting", "log.fortianalyzer-cloud.override-setting", "log.syslogd.setting", "log.syslogd.override-setting", "log.syslogd2.setting", "log.syslogd2.override-setting", "log.syslogd3.setting", "log.syslogd3.override-setting", "log.syslogd4.setting", "log.syslogd4.override-setting", "system.gre-tunnel", "system.central-management", "system.csf", "user.radius", "system.interface", "vpn.ipsec.phase1-interface", "vpn.ipsec.phase2-interface", "router.bgp", "router.route-map", "router.prefix-list", "firewall.ippool", "firewall.ippool6", "router.static", "router.static6", "firewall.vip", "firewall.vip6", "system.sdwan", "system.saml", "router.policy", "router.policy6", "log.syslogd.setting", "log.syslogd.override-setting", "firewall.address"] | None = ...,
        scope: Literal["all", "inclusive", "exclusive"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: VdomExceptionPayload | None = ...,
        id: int | None = ...,
        object: Literal["log.fortianalyzer.setting", "log.fortianalyzer.override-setting", "log.fortianalyzer2.setting", "log.fortianalyzer2.override-setting", "log.fortianalyzer3.setting", "log.fortianalyzer3.override-setting", "log.fortianalyzer-cloud.setting", "log.fortianalyzer-cloud.override-setting", "log.syslogd.setting", "log.syslogd.override-setting", "log.syslogd2.setting", "log.syslogd2.override-setting", "log.syslogd3.setting", "log.syslogd3.override-setting", "log.syslogd4.setting", "log.syslogd4.override-setting", "system.gre-tunnel", "system.central-management", "system.csf", "user.radius", "system.interface", "vpn.ipsec.phase1-interface", "vpn.ipsec.phase2-interface", "router.bgp", "router.route-map", "router.prefix-list", "firewall.ippool", "firewall.ippool6", "router.static", "router.static6", "firewall.vip", "firewall.vip6", "system.sdwan", "system.saml", "router.policy", "router.policy6", "log.syslogd.setting", "log.syslogd.override-setting", "firewall.address"] | None = ...,
        scope: Literal["all", "inclusive", "exclusive"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: VdomExceptionPayload | None = ...,
        id: int | None = ...,
        object: Literal["log.fortianalyzer.setting", "log.fortianalyzer.override-setting", "log.fortianalyzer2.setting", "log.fortianalyzer2.override-setting", "log.fortianalyzer3.setting", "log.fortianalyzer3.override-setting", "log.fortianalyzer-cloud.setting", "log.fortianalyzer-cloud.override-setting", "log.syslogd.setting", "log.syslogd.override-setting", "log.syslogd2.setting", "log.syslogd2.override-setting", "log.syslogd3.setting", "log.syslogd3.override-setting", "log.syslogd4.setting", "log.syslogd4.override-setting", "system.gre-tunnel", "system.central-management", "system.csf", "user.radius", "system.interface", "vpn.ipsec.phase1-interface", "vpn.ipsec.phase2-interface", "router.bgp", "router.route-map", "router.prefix-list", "firewall.ippool", "firewall.ippool6", "router.static", "router.static6", "firewall.vip", "firewall.vip6", "system.sdwan", "system.saml", "router.policy", "router.policy6", "log.syslogd.setting", "log.syslogd.override-setting", "firewall.address"] | None = ...,
        scope: Literal["all", "inclusive", "exclusive"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: VdomExceptionPayload | None = ...,
        id: int | None = ...,
        object: Literal["log.fortianalyzer.setting", "log.fortianalyzer.override-setting", "log.fortianalyzer2.setting", "log.fortianalyzer2.override-setting", "log.fortianalyzer3.setting", "log.fortianalyzer3.override-setting", "log.fortianalyzer-cloud.setting", "log.fortianalyzer-cloud.override-setting", "log.syslogd.setting", "log.syslogd.override-setting", "log.syslogd2.setting", "log.syslogd2.override-setting", "log.syslogd3.setting", "log.syslogd3.override-setting", "log.syslogd4.setting", "log.syslogd4.override-setting", "system.gre-tunnel", "system.central-management", "system.csf", "user.radius", "system.interface", "vpn.ipsec.phase1-interface", "vpn.ipsec.phase2-interface", "router.bgp", "router.route-map", "router.prefix-list", "firewall.ippool", "firewall.ippool6", "router.static", "router.static6", "firewall.vip", "firewall.vip6", "system.sdwan", "system.saml", "router.policy", "router.policy6", "log.syslogd.setting", "log.syslogd.override-setting", "firewall.address"] | None = ...,
        scope: Literal["all", "inclusive", "exclusive"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> VdomExceptionObject: ...
    
    @overload
    def put(
        self,
        payload_dict: VdomExceptionPayload | None = ...,
        id: int | None = ...,
        object: Literal["log.fortianalyzer.setting", "log.fortianalyzer.override-setting", "log.fortianalyzer2.setting", "log.fortianalyzer2.override-setting", "log.fortianalyzer3.setting", "log.fortianalyzer3.override-setting", "log.fortianalyzer-cloud.setting", "log.fortianalyzer-cloud.override-setting", "log.syslogd.setting", "log.syslogd.override-setting", "log.syslogd2.setting", "log.syslogd2.override-setting", "log.syslogd3.setting", "log.syslogd3.override-setting", "log.syslogd4.setting", "log.syslogd4.override-setting", "system.gre-tunnel", "system.central-management", "system.csf", "user.radius", "system.interface", "vpn.ipsec.phase1-interface", "vpn.ipsec.phase2-interface", "router.bgp", "router.route-map", "router.prefix-list", "firewall.ippool", "firewall.ippool6", "router.static", "router.static6", "firewall.vip", "firewall.vip6", "system.sdwan", "system.saml", "router.policy", "router.policy6", "log.syslogd.setting", "log.syslogd.override-setting", "firewall.address"] | None = ...,
        scope: Literal["all", "inclusive", "exclusive"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: VdomExceptionPayload | None = ...,
        id: int | None = ...,
        object: Literal["log.fortianalyzer.setting", "log.fortianalyzer.override-setting", "log.fortianalyzer2.setting", "log.fortianalyzer2.override-setting", "log.fortianalyzer3.setting", "log.fortianalyzer3.override-setting", "log.fortianalyzer-cloud.setting", "log.fortianalyzer-cloud.override-setting", "log.syslogd.setting", "log.syslogd.override-setting", "log.syslogd2.setting", "log.syslogd2.override-setting", "log.syslogd3.setting", "log.syslogd3.override-setting", "log.syslogd4.setting", "log.syslogd4.override-setting", "system.gre-tunnel", "system.central-management", "system.csf", "user.radius", "system.interface", "vpn.ipsec.phase1-interface", "vpn.ipsec.phase2-interface", "router.bgp", "router.route-map", "router.prefix-list", "firewall.ippool", "firewall.ippool6", "router.static", "router.static6", "firewall.vip", "firewall.vip6", "system.sdwan", "system.saml", "router.policy", "router.policy6", "log.syslogd.setting", "log.syslogd.override-setting", "firewall.address"] | None = ...,
        scope: Literal["all", "inclusive", "exclusive"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: VdomExceptionPayload | None = ...,
        id: int | None = ...,
        object: Literal["log.fortianalyzer.setting", "log.fortianalyzer.override-setting", "log.fortianalyzer2.setting", "log.fortianalyzer2.override-setting", "log.fortianalyzer3.setting", "log.fortianalyzer3.override-setting", "log.fortianalyzer-cloud.setting", "log.fortianalyzer-cloud.override-setting", "log.syslogd.setting", "log.syslogd.override-setting", "log.syslogd2.setting", "log.syslogd2.override-setting", "log.syslogd3.setting", "log.syslogd3.override-setting", "log.syslogd4.setting", "log.syslogd4.override-setting", "system.gre-tunnel", "system.central-management", "system.csf", "user.radius", "system.interface", "vpn.ipsec.phase1-interface", "vpn.ipsec.phase2-interface", "router.bgp", "router.route-map", "router.prefix-list", "firewall.ippool", "firewall.ippool6", "router.static", "router.static6", "firewall.vip", "firewall.vip6", "system.sdwan", "system.saml", "router.policy", "router.policy6", "log.syslogd.setting", "log.syslogd.override-setting", "firewall.address"] | None = ...,
        scope: Literal["all", "inclusive", "exclusive"] | None = ...,
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
    ) -> VdomExceptionObject: ...
    
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
        payload_dict: VdomExceptionPayload | None = ...,
        id: int | None = ...,
        object: Literal["log.fortianalyzer.setting", "log.fortianalyzer.override-setting", "log.fortianalyzer2.setting", "log.fortianalyzer2.override-setting", "log.fortianalyzer3.setting", "log.fortianalyzer3.override-setting", "log.fortianalyzer-cloud.setting", "log.fortianalyzer-cloud.override-setting", "log.syslogd.setting", "log.syslogd.override-setting", "log.syslogd2.setting", "log.syslogd2.override-setting", "log.syslogd3.setting", "log.syslogd3.override-setting", "log.syslogd4.setting", "log.syslogd4.override-setting", "system.gre-tunnel", "system.central-management", "system.csf", "user.radius", "system.interface", "vpn.ipsec.phase1-interface", "vpn.ipsec.phase2-interface", "router.bgp", "router.route-map", "router.prefix-list", "firewall.ippool", "firewall.ippool6", "router.static", "router.static6", "firewall.vip", "firewall.vip6", "system.sdwan", "system.saml", "router.policy", "router.policy6", "log.syslogd.setting", "log.syslogd.override-setting", "firewall.address"] | None = ...,
        scope: Literal["all", "inclusive", "exclusive"] | None = ...,
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
    "VdomException",
    "VdomExceptionPayload",
    "VdomExceptionObject",
]