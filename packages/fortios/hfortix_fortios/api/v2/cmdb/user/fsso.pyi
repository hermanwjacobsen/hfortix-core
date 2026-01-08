from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class FssoPayload(TypedDict, total=False):
    """
    Type hints for user/fsso payload fields.
    
    Configure Fortinet Single Sign On (FSSO) agents.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface)
        - :class:`~.user.ldap.LdapEndpoint` (via: ldap-server, user-info-server)
        - :class:`~.vpn.certificate.ca.CaEndpoint` (via: ssl-trusted-cert)
        - :class:`~.vpn.certificate.remote.RemoteEndpoint` (via: ssl-trusted-cert)

    **Usage:**
        payload: FssoPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Name.
    type: NotRequired[Literal["default", "fortinac"]]  # Server type.
    server: str  # Domain name or IP address of the first FSSO collector agent.
    port: int  # Port of the first FSSO collector agent.
    password: NotRequired[str]  # Password of the first FSSO collector agent.
    server2: NotRequired[str]  # Domain name or IP address of the second FSSO collector agent
    port2: NotRequired[int]  # Port of the second FSSO collector agent.
    password2: NotRequired[str]  # Password of the second FSSO collector agent.
    server3: NotRequired[str]  # Domain name or IP address of the third FSSO collector agent.
    port3: NotRequired[int]  # Port of the third FSSO collector agent.
    password3: NotRequired[str]  # Password of the third FSSO collector agent.
    server4: NotRequired[str]  # Domain name or IP address of the fourth FSSO collector agent
    port4: NotRequired[int]  # Port of the fourth FSSO collector agent.
    password4: NotRequired[str]  # Password of the fourth FSSO collector agent.
    server5: NotRequired[str]  # Domain name or IP address of the fifth FSSO collector agent.
    port5: NotRequired[int]  # Port of the fifth FSSO collector agent.
    password5: NotRequired[str]  # Password of the fifth FSSO collector agent.
    logon_timeout: NotRequired[int]  # Interval in minutes to keep logons after FSSO server down.
    ldap_server: NotRequired[str]  # LDAP server to get group information.
    group_poll_interval: NotRequired[int]  # Interval in minutes within to fetch groups from FSSO server,
    ldap_poll: NotRequired[Literal["enable", "disable"]]  # Enable/disable automatic fetching of groups from LDAP server
    ldap_poll_interval: NotRequired[int]  # Interval in minutes within to fetch groups from LDAP server.
    ldap_poll_filter: NotRequired[str]  # Filter used to fetch groups.
    user_info_server: NotRequired[str]  # LDAP server to get user information.
    ssl: NotRequired[Literal["enable", "disable"]]  # Enable/disable use of SSL.
    sni: NotRequired[str]  # Server Name Indication.
    ssl_server_host_ip_check: NotRequired[Literal["enable", "disable"]]  # Enable/disable server host/IP verification.
    ssl_trusted_cert: NotRequired[str]  # Trusted server certificate or CA certificate.
    source_ip: NotRequired[str]  # Source IP for communications to FSSO agent.
    source_ip6: NotRequired[str]  # IPv6 source for communications to FSSO agent.
    interface_select_method: NotRequired[Literal["auto", "sdwan", "specify"]]  # Specify how to select outgoing interface to reach server.
    interface: str  # Specify outgoing interface to reach server.
    vrf_select: NotRequired[int]  # VRF ID used for connection to server.

# Nested classes for table field children


# Response TypedDict for GET returns (all fields present in API response)
class FssoResponse(TypedDict):
    """
    Type hints for user/fsso API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    type: Literal["default", "fortinac"]
    server: str
    port: int
    password: str
    server2: str
    port2: int
    password2: str
    server3: str
    port3: int
    password3: str
    server4: str
    port4: int
    password4: str
    server5: str
    port5: int
    password5: str
    logon_timeout: int
    ldap_server: str
    group_poll_interval: int
    ldap_poll: Literal["enable", "disable"]
    ldap_poll_interval: int
    ldap_poll_filter: str
    user_info_server: str
    ssl: Literal["enable", "disable"]
    sni: str
    ssl_server_host_ip_check: Literal["enable", "disable"]
    ssl_trusted_cert: str
    source_ip: str
    source_ip6: str
    interface_select_method: Literal["auto", "sdwan", "specify"]
    interface: str
    vrf_select: int


@final
class FssoObject:
    """Typed FortiObject for user/fsso with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Name.
    name: str
    # Server type.
    type: Literal["default", "fortinac"]
    # Domain name or IP address of the first FSSO collector agent.
    server: str
    # Port of the first FSSO collector agent.
    port: int
    # Password of the first FSSO collector agent.
    password: str
    # Domain name or IP address of the second FSSO collector agent.
    server2: str
    # Port of the second FSSO collector agent.
    port2: int
    # Password of the second FSSO collector agent.
    password2: str
    # Domain name or IP address of the third FSSO collector agent.
    server3: str
    # Port of the third FSSO collector agent.
    port3: int
    # Password of the third FSSO collector agent.
    password3: str
    # Domain name or IP address of the fourth FSSO collector agent.
    server4: str
    # Port of the fourth FSSO collector agent.
    port4: int
    # Password of the fourth FSSO collector agent.
    password4: str
    # Domain name or IP address of the fifth FSSO collector agent.
    server5: str
    # Port of the fifth FSSO collector agent.
    port5: int
    # Password of the fifth FSSO collector agent.
    password5: str
    # Interval in minutes to keep logons after FSSO server down.
    logon_timeout: int
    # LDAP server to get group information.
    ldap_server: str
    # Interval in minutes within to fetch groups from FSSO server, or unset to disable
    group_poll_interval: int
    # Enable/disable automatic fetching of groups from LDAP server.
    ldap_poll: Literal["enable", "disable"]
    # Interval in minutes within to fetch groups from LDAP server.
    ldap_poll_interval: int
    # Filter used to fetch groups.
    ldap_poll_filter: str
    # LDAP server to get user information.
    user_info_server: str
    # Enable/disable use of SSL.
    ssl: Literal["enable", "disable"]
    # Server Name Indication.
    sni: str
    # Enable/disable server host/IP verification.
    ssl_server_host_ip_check: Literal["enable", "disable"]
    # Trusted server certificate or CA certificate.
    ssl_trusted_cert: str
    # Source IP for communications to FSSO agent.
    source_ip: str
    # IPv6 source for communications to FSSO agent.
    source_ip6: str
    # Specify how to select outgoing interface to reach server.
    interface_select_method: Literal["auto", "sdwan", "specify"]
    # Specify outgoing interface to reach server.
    interface: str
    # VRF ID used for connection to server.
    vrf_select: int
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FssoPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Fsso:
    """
    Configure Fortinet Single Sign On (FSSO) agents.
    
    Path: user/fsso
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
    ) -> FssoObject: ...
    
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
    ) -> FssoObject: ...
    
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
    ) -> list[FssoObject]: ...
    
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
    ) -> FssoResponse: ...
    
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
    ) -> FssoResponse: ...
    
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
    ) -> list[FssoResponse]: ...
    
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
    ) -> FssoObject | list[FssoObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: FssoPayload | None = ...,
        name: str | None = ...,
        type: Literal["default", "fortinac"] | None = ...,
        server: str | None = ...,
        port: int | None = ...,
        password: str | None = ...,
        server2: str | None = ...,
        port2: int | None = ...,
        password2: str | None = ...,
        server3: str | None = ...,
        port3: int | None = ...,
        password3: str | None = ...,
        server4: str | None = ...,
        port4: int | None = ...,
        password4: str | None = ...,
        server5: str | None = ...,
        port5: int | None = ...,
        password5: str | None = ...,
        logon_timeout: int | None = ...,
        ldap_server: str | None = ...,
        group_poll_interval: int | None = ...,
        ldap_poll: Literal["enable", "disable"] | None = ...,
        ldap_poll_interval: int | None = ...,
        ldap_poll_filter: str | None = ...,
        user_info_server: str | None = ...,
        ssl: Literal["enable", "disable"] | None = ...,
        sni: str | None = ...,
        ssl_server_host_ip_check: Literal["enable", "disable"] | None = ...,
        ssl_trusted_cert: str | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> FssoObject: ...
    
    @overload
    def post(
        self,
        payload_dict: FssoPayload | None = ...,
        name: str | None = ...,
        type: Literal["default", "fortinac"] | None = ...,
        server: str | None = ...,
        port: int | None = ...,
        password: str | None = ...,
        server2: str | None = ...,
        port2: int | None = ...,
        password2: str | None = ...,
        server3: str | None = ...,
        port3: int | None = ...,
        password3: str | None = ...,
        server4: str | None = ...,
        port4: int | None = ...,
        password4: str | None = ...,
        server5: str | None = ...,
        port5: int | None = ...,
        password5: str | None = ...,
        logon_timeout: int | None = ...,
        ldap_server: str | None = ...,
        group_poll_interval: int | None = ...,
        ldap_poll: Literal["enable", "disable"] | None = ...,
        ldap_poll_interval: int | None = ...,
        ldap_poll_filter: str | None = ...,
        user_info_server: str | None = ...,
        ssl: Literal["enable", "disable"] | None = ...,
        sni: str | None = ...,
        ssl_server_host_ip_check: Literal["enable", "disable"] | None = ...,
        ssl_trusted_cert: str | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: FssoPayload | None = ...,
        name: str | None = ...,
        type: Literal["default", "fortinac"] | None = ...,
        server: str | None = ...,
        port: int | None = ...,
        password: str | None = ...,
        server2: str | None = ...,
        port2: int | None = ...,
        password2: str | None = ...,
        server3: str | None = ...,
        port3: int | None = ...,
        password3: str | None = ...,
        server4: str | None = ...,
        port4: int | None = ...,
        password4: str | None = ...,
        server5: str | None = ...,
        port5: int | None = ...,
        password5: str | None = ...,
        logon_timeout: int | None = ...,
        ldap_server: str | None = ...,
        group_poll_interval: int | None = ...,
        ldap_poll: Literal["enable", "disable"] | None = ...,
        ldap_poll_interval: int | None = ...,
        ldap_poll_filter: str | None = ...,
        user_info_server: str | None = ...,
        ssl: Literal["enable", "disable"] | None = ...,
        sni: str | None = ...,
        ssl_server_host_ip_check: Literal["enable", "disable"] | None = ...,
        ssl_trusted_cert: str | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: FssoPayload | None = ...,
        name: str | None = ...,
        type: Literal["default", "fortinac"] | None = ...,
        server: str | None = ...,
        port: int | None = ...,
        password: str | None = ...,
        server2: str | None = ...,
        port2: int | None = ...,
        password2: str | None = ...,
        server3: str | None = ...,
        port3: int | None = ...,
        password3: str | None = ...,
        server4: str | None = ...,
        port4: int | None = ...,
        password4: str | None = ...,
        server5: str | None = ...,
        port5: int | None = ...,
        password5: str | None = ...,
        logon_timeout: int | None = ...,
        ldap_server: str | None = ...,
        group_poll_interval: int | None = ...,
        ldap_poll: Literal["enable", "disable"] | None = ...,
        ldap_poll_interval: int | None = ...,
        ldap_poll_filter: str | None = ...,
        user_info_server: str | None = ...,
        ssl: Literal["enable", "disable"] | None = ...,
        sni: str | None = ...,
        ssl_server_host_ip_check: Literal["enable", "disable"] | None = ...,
        ssl_trusted_cert: str | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: FssoPayload | None = ...,
        name: str | None = ...,
        type: Literal["default", "fortinac"] | None = ...,
        server: str | None = ...,
        port: int | None = ...,
        password: str | None = ...,
        server2: str | None = ...,
        port2: int | None = ...,
        password2: str | None = ...,
        server3: str | None = ...,
        port3: int | None = ...,
        password3: str | None = ...,
        server4: str | None = ...,
        port4: int | None = ...,
        password4: str | None = ...,
        server5: str | None = ...,
        port5: int | None = ...,
        password5: str | None = ...,
        logon_timeout: int | None = ...,
        ldap_server: str | None = ...,
        group_poll_interval: int | None = ...,
        ldap_poll: Literal["enable", "disable"] | None = ...,
        ldap_poll_interval: int | None = ...,
        ldap_poll_filter: str | None = ...,
        user_info_server: str | None = ...,
        ssl: Literal["enable", "disable"] | None = ...,
        sni: str | None = ...,
        ssl_server_host_ip_check: Literal["enable", "disable"] | None = ...,
        ssl_trusted_cert: str | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> FssoObject: ...
    
    @overload
    def put(
        self,
        payload_dict: FssoPayload | None = ...,
        name: str | None = ...,
        type: Literal["default", "fortinac"] | None = ...,
        server: str | None = ...,
        port: int | None = ...,
        password: str | None = ...,
        server2: str | None = ...,
        port2: int | None = ...,
        password2: str | None = ...,
        server3: str | None = ...,
        port3: int | None = ...,
        password3: str | None = ...,
        server4: str | None = ...,
        port4: int | None = ...,
        password4: str | None = ...,
        server5: str | None = ...,
        port5: int | None = ...,
        password5: str | None = ...,
        logon_timeout: int | None = ...,
        ldap_server: str | None = ...,
        group_poll_interval: int | None = ...,
        ldap_poll: Literal["enable", "disable"] | None = ...,
        ldap_poll_interval: int | None = ...,
        ldap_poll_filter: str | None = ...,
        user_info_server: str | None = ...,
        ssl: Literal["enable", "disable"] | None = ...,
        sni: str | None = ...,
        ssl_server_host_ip_check: Literal["enable", "disable"] | None = ...,
        ssl_trusted_cert: str | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: FssoPayload | None = ...,
        name: str | None = ...,
        type: Literal["default", "fortinac"] | None = ...,
        server: str | None = ...,
        port: int | None = ...,
        password: str | None = ...,
        server2: str | None = ...,
        port2: int | None = ...,
        password2: str | None = ...,
        server3: str | None = ...,
        port3: int | None = ...,
        password3: str | None = ...,
        server4: str | None = ...,
        port4: int | None = ...,
        password4: str | None = ...,
        server5: str | None = ...,
        port5: int | None = ...,
        password5: str | None = ...,
        logon_timeout: int | None = ...,
        ldap_server: str | None = ...,
        group_poll_interval: int | None = ...,
        ldap_poll: Literal["enable", "disable"] | None = ...,
        ldap_poll_interval: int | None = ...,
        ldap_poll_filter: str | None = ...,
        user_info_server: str | None = ...,
        ssl: Literal["enable", "disable"] | None = ...,
        sni: str | None = ...,
        ssl_server_host_ip_check: Literal["enable", "disable"] | None = ...,
        ssl_trusted_cert: str | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: FssoPayload | None = ...,
        name: str | None = ...,
        type: Literal["default", "fortinac"] | None = ...,
        server: str | None = ...,
        port: int | None = ...,
        password: str | None = ...,
        server2: str | None = ...,
        port2: int | None = ...,
        password2: str | None = ...,
        server3: str | None = ...,
        port3: int | None = ...,
        password3: str | None = ...,
        server4: str | None = ...,
        port4: int | None = ...,
        password4: str | None = ...,
        server5: str | None = ...,
        port5: int | None = ...,
        password5: str | None = ...,
        logon_timeout: int | None = ...,
        ldap_server: str | None = ...,
        group_poll_interval: int | None = ...,
        ldap_poll: Literal["enable", "disable"] | None = ...,
        ldap_poll_interval: int | None = ...,
        ldap_poll_filter: str | None = ...,
        user_info_server: str | None = ...,
        ssl: Literal["enable", "disable"] | None = ...,
        sni: str | None = ...,
        ssl_server_host_ip_check: Literal["enable", "disable"] | None = ...,
        ssl_trusted_cert: str | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
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
    ) -> FssoObject: ...
    
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
        payload_dict: FssoPayload | None = ...,
        name: str | None = ...,
        type: Literal["default", "fortinac"] | None = ...,
        server: str | None = ...,
        port: int | None = ...,
        password: str | None = ...,
        server2: str | None = ...,
        port2: int | None = ...,
        password2: str | None = ...,
        server3: str | None = ...,
        port3: int | None = ...,
        password3: str | None = ...,
        server4: str | None = ...,
        port4: int | None = ...,
        password4: str | None = ...,
        server5: str | None = ...,
        port5: int | None = ...,
        password5: str | None = ...,
        logon_timeout: int | None = ...,
        ldap_server: str | None = ...,
        group_poll_interval: int | None = ...,
        ldap_poll: Literal["enable", "disable"] | None = ...,
        ldap_poll_interval: int | None = ...,
        ldap_poll_filter: str | None = ...,
        user_info_server: str | None = ...,
        ssl: Literal["enable", "disable"] | None = ...,
        sni: str | None = ...,
        ssl_server_host_ip_check: Literal["enable", "disable"] | None = ...,
        ssl_trusted_cert: str | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
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
    "Fsso",
    "FssoPayload",
    "FssoObject",
]