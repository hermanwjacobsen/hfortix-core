from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class ListPayload(TypedDict, total=False):
    """
    Type hints for application/list payload fields.
    
    Configure application control lists.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.replacemsg-group.ReplacemsgGroupEndpoint` (via: replacemsg-group)

    **Usage:**
        payload: ListPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # List name.
    comment: NotRequired[str]  # Comments.
    replacemsg_group: NotRequired[str]  # Replacement message group.
    extended_log: NotRequired[Literal["enable", "disable"]]  # Enable/disable extended logging.
    other_application_action: NotRequired[Literal["pass", "block"]]  # Action for other applications.
    app_replacemsg: NotRequired[Literal["disable", "enable"]]  # Enable/disable replacement messages for blocked applications
    other_application_log: NotRequired[Literal["disable", "enable"]]  # Enable/disable logging for other applications.
    enforce_default_app_port: NotRequired[Literal["disable", "enable"]]  # Enable/disable default application port enforcement for allo
    force_inclusion_ssl_di_sigs: NotRequired[Literal["disable", "enable"]]  # Enable/disable forced inclusion of SSL deep inspection signa
    unknown_application_action: NotRequired[Literal["pass", "block"]]  # Pass or block traffic from unknown applications.
    unknown_application_log: NotRequired[Literal["disable", "enable"]]  # Enable/disable logging for unknown applications.
    p2p_block_list: NotRequired[Literal["skype", "edonkey", "bittorrent"]]  # P2P applications to be block listed.
    deep_app_inspection: NotRequired[Literal["disable", "enable"]]  # Enable/disable deep application inspection.
    options: NotRequired[Literal["allow-dns", "allow-icmp", "allow-http", "allow-ssl"]]  # Basic application protocol signatures allowed by default.
    entries: NotRequired[list[dict[str, Any]]]  # Application list entries.
    control_default_network_services: NotRequired[Literal["disable", "enable"]]  # Enable/disable enforcement of protocols over selected ports.
    default_network_services: NotRequired[list[dict[str, Any]]]  # Default network service entries.

# Nested classes for table field children

@final
class ListEntriesObject:
    """Typed object for entries table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Entry ID.
    id: int
    # Risk, or impact, of allowing traffic from this application to occur
    risk: str
    # Category ID list.
    category: str
    # ID of allowed applications.
    application: str
    # Application protocol filter.
    protocols: str
    # Application vendor filter.
    vendor: str
    # Application technology filter.
    technology: str
    # Application behavior filter.
    behavior: str
    # Application popularity filter (1 - 5, from least to most popular).
    popularity: Literal["1", "2", "3", "4", "5"]
    # ID of excluded applications.
    exclusion: str
    # Application parameters.
    parameters: str
    # Pass or block traffic, or reset connection for traffic from this application.
    action: Literal["pass", "block", "reset"]
    # Enable/disable logging for this application list.
    log: Literal["disable", "enable"]
    # Enable/disable packet logging.
    log_packet: Literal["disable", "enable"]
    # Count of the rate.
    rate_count: int
    # Duration (sec) of the rate.
    rate_duration: int
    # Rate limit mode.
    rate_mode: Literal["periodical", "continuous"]
    # Track the packet protocol field.
    rate_track: Literal["none", "src-ip", "dest-ip", "dhcp-client-mac", "dns-domain"]
    # Session TTL (0 = default).
    session_ttl: int
    # Traffic shaper.
    shaper: str
    # Reverse traffic shaper.
    shaper_reverse: str
    # Per-IP traffic shaper.
    per_ip_shaper: str
    # Quarantine method.
    quarantine: Literal["none", "attacker"]
    # Duration of quarantine.
    quarantine_expiry: str
    # Enable/disable quarantine logging.
    quarantine_log: Literal["disable", "enable"]
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class ListDefaultnetworkservicesObject:
    """Typed object for default-network-services table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Entry ID.
    id: int
    # Port number.
    port: int
    # Network protocols.
    services: Literal["http", "ssh", "telnet", "ftp", "dns", "smtp", "pop3", "imap", "snmp", "nntp", "https"]
    # Action for protocols not in the allowlist for selected port.
    violation_action: Literal["pass", "monitor", "block"]
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class ListResponse(TypedDict):
    """
    Type hints for application/list API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    comment: str
    replacemsg_group: str
    extended_log: Literal["enable", "disable"]
    other_application_action: Literal["pass", "block"]
    app_replacemsg: Literal["disable", "enable"]
    other_application_log: Literal["disable", "enable"]
    enforce_default_app_port: Literal["disable", "enable"]
    force_inclusion_ssl_di_sigs: Literal["disable", "enable"]
    unknown_application_action: Literal["pass", "block"]
    unknown_application_log: Literal["disable", "enable"]
    p2p_block_list: Literal["skype", "edonkey", "bittorrent"]
    deep_app_inspection: Literal["disable", "enable"]
    options: Literal["allow-dns", "allow-icmp", "allow-http", "allow-ssl"]
    entries: list[dict[str, Any]]
    control_default_network_services: Literal["disable", "enable"]
    default_network_services: list[dict[str, Any]]


@final
class ListObject:
    """Typed FortiObject for application/list with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # List name.
    name: str
    # Comments.
    comment: str
    # Replacement message group.
    replacemsg_group: str
    # Enable/disable extended logging.
    extended_log: Literal["enable", "disable"]
    # Action for other applications.
    other_application_action: Literal["pass", "block"]
    # Enable/disable replacement messages for blocked applications.
    app_replacemsg: Literal["disable", "enable"]
    # Enable/disable logging for other applications.
    other_application_log: Literal["disable", "enable"]
    # Enable/disable default application port enforcement for allowed applications.
    enforce_default_app_port: Literal["disable", "enable"]
    # Enable/disable forced inclusion of SSL deep inspection signatures.
    force_inclusion_ssl_di_sigs: Literal["disable", "enable"]
    # Pass or block traffic from unknown applications.
    unknown_application_action: Literal["pass", "block"]
    # Enable/disable logging for unknown applications.
    unknown_application_log: Literal["disable", "enable"]
    # P2P applications to be block listed.
    p2p_block_list: Literal["skype", "edonkey", "bittorrent"]
    # Enable/disable deep application inspection.
    deep_app_inspection: Literal["disable", "enable"]
    # Basic application protocol signatures allowed by default.
    options: Literal["allow-dns", "allow-icmp", "allow-http", "allow-ssl"]
    # Application list entries.
    entries: list[ListEntriesObject]  # Table field - list of typed objects
    # Enable/disable enforcement of protocols over selected ports.
    control_default_network_services: Literal["disable", "enable"]
    # Default network service entries.
    default_network_services: list[ListDefaultnetworkservicesObject]  # Table field - list of typed objects
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> ListPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class List:
    """
    Configure application control lists.
    
    Path: application/list
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
    ) -> ListObject: ...
    
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
    ) -> ListObject: ...
    
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
    ) -> list[ListObject]: ...
    
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
    ) -> ListResponse: ...
    
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
    ) -> ListResponse: ...
    
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
    ) -> list[ListResponse]: ...
    
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
    ) -> ListObject | list[ListObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: ListPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        other_application_action: Literal["pass", "block"] | None = ...,
        app_replacemsg: Literal["disable", "enable"] | None = ...,
        other_application_log: Literal["disable", "enable"] | None = ...,
        enforce_default_app_port: Literal["disable", "enable"] | None = ...,
        force_inclusion_ssl_di_sigs: Literal["disable", "enable"] | None = ...,
        unknown_application_action: Literal["pass", "block"] | None = ...,
        unknown_application_log: Literal["disable", "enable"] | None = ...,
        p2p_block_list: Literal["skype", "edonkey", "bittorrent"] | list[str] | None = ...,
        deep_app_inspection: Literal["disable", "enable"] | None = ...,
        options: Literal["allow-dns", "allow-icmp", "allow-http", "allow-ssl"] | list[str] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        control_default_network_services: Literal["disable", "enable"] | None = ...,
        default_network_services: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ListObject: ...
    
    @overload
    def post(
        self,
        payload_dict: ListPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        other_application_action: Literal["pass", "block"] | None = ...,
        app_replacemsg: Literal["disable", "enable"] | None = ...,
        other_application_log: Literal["disable", "enable"] | None = ...,
        enforce_default_app_port: Literal["disable", "enable"] | None = ...,
        force_inclusion_ssl_di_sigs: Literal["disable", "enable"] | None = ...,
        unknown_application_action: Literal["pass", "block"] | None = ...,
        unknown_application_log: Literal["disable", "enable"] | None = ...,
        p2p_block_list: Literal["skype", "edonkey", "bittorrent"] | list[str] | None = ...,
        deep_app_inspection: Literal["disable", "enable"] | None = ...,
        options: Literal["allow-dns", "allow-icmp", "allow-http", "allow-ssl"] | list[str] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        control_default_network_services: Literal["disable", "enable"] | None = ...,
        default_network_services: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: ListPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        other_application_action: Literal["pass", "block"] | None = ...,
        app_replacemsg: Literal["disable", "enable"] | None = ...,
        other_application_log: Literal["disable", "enable"] | None = ...,
        enforce_default_app_port: Literal["disable", "enable"] | None = ...,
        force_inclusion_ssl_di_sigs: Literal["disable", "enable"] | None = ...,
        unknown_application_action: Literal["pass", "block"] | None = ...,
        unknown_application_log: Literal["disable", "enable"] | None = ...,
        p2p_block_list: Literal["skype", "edonkey", "bittorrent"] | list[str] | None = ...,
        deep_app_inspection: Literal["disable", "enable"] | None = ...,
        options: Literal["allow-dns", "allow-icmp", "allow-http", "allow-ssl"] | list[str] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        control_default_network_services: Literal["disable", "enable"] | None = ...,
        default_network_services: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: ListPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        other_application_action: Literal["pass", "block"] | None = ...,
        app_replacemsg: Literal["disable", "enable"] | None = ...,
        other_application_log: Literal["disable", "enable"] | None = ...,
        enforce_default_app_port: Literal["disable", "enable"] | None = ...,
        force_inclusion_ssl_di_sigs: Literal["disable", "enable"] | None = ...,
        unknown_application_action: Literal["pass", "block"] | None = ...,
        unknown_application_log: Literal["disable", "enable"] | None = ...,
        p2p_block_list: Literal["skype", "edonkey", "bittorrent"] | list[str] | None = ...,
        deep_app_inspection: Literal["disable", "enable"] | None = ...,
        options: Literal["allow-dns", "allow-icmp", "allow-http", "allow-ssl"] | list[str] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        control_default_network_services: Literal["disable", "enable"] | None = ...,
        default_network_services: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ListPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        other_application_action: Literal["pass", "block"] | None = ...,
        app_replacemsg: Literal["disable", "enable"] | None = ...,
        other_application_log: Literal["disable", "enable"] | None = ...,
        enforce_default_app_port: Literal["disable", "enable"] | None = ...,
        force_inclusion_ssl_di_sigs: Literal["disable", "enable"] | None = ...,
        unknown_application_action: Literal["pass", "block"] | None = ...,
        unknown_application_log: Literal["disable", "enable"] | None = ...,
        p2p_block_list: Literal["skype", "edonkey", "bittorrent"] | list[str] | None = ...,
        deep_app_inspection: Literal["disable", "enable"] | None = ...,
        options: Literal["allow-dns", "allow-icmp", "allow-http", "allow-ssl"] | list[str] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        control_default_network_services: Literal["disable", "enable"] | None = ...,
        default_network_services: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ListObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ListPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        other_application_action: Literal["pass", "block"] | None = ...,
        app_replacemsg: Literal["disable", "enable"] | None = ...,
        other_application_log: Literal["disable", "enable"] | None = ...,
        enforce_default_app_port: Literal["disable", "enable"] | None = ...,
        force_inclusion_ssl_di_sigs: Literal["disable", "enable"] | None = ...,
        unknown_application_action: Literal["pass", "block"] | None = ...,
        unknown_application_log: Literal["disable", "enable"] | None = ...,
        p2p_block_list: Literal["skype", "edonkey", "bittorrent"] | list[str] | None = ...,
        deep_app_inspection: Literal["disable", "enable"] | None = ...,
        options: Literal["allow-dns", "allow-icmp", "allow-http", "allow-ssl"] | list[str] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        control_default_network_services: Literal["disable", "enable"] | None = ...,
        default_network_services: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: ListPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        other_application_action: Literal["pass", "block"] | None = ...,
        app_replacemsg: Literal["disable", "enable"] | None = ...,
        other_application_log: Literal["disable", "enable"] | None = ...,
        enforce_default_app_port: Literal["disable", "enable"] | None = ...,
        force_inclusion_ssl_di_sigs: Literal["disable", "enable"] | None = ...,
        unknown_application_action: Literal["pass", "block"] | None = ...,
        unknown_application_log: Literal["disable", "enable"] | None = ...,
        p2p_block_list: Literal["skype", "edonkey", "bittorrent"] | list[str] | None = ...,
        deep_app_inspection: Literal["disable", "enable"] | None = ...,
        options: Literal["allow-dns", "allow-icmp", "allow-http", "allow-ssl"] | list[str] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        control_default_network_services: Literal["disable", "enable"] | None = ...,
        default_network_services: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: ListPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        other_application_action: Literal["pass", "block"] | None = ...,
        app_replacemsg: Literal["disable", "enable"] | None = ...,
        other_application_log: Literal["disable", "enable"] | None = ...,
        enforce_default_app_port: Literal["disable", "enable"] | None = ...,
        force_inclusion_ssl_di_sigs: Literal["disable", "enable"] | None = ...,
        unknown_application_action: Literal["pass", "block"] | None = ...,
        unknown_application_log: Literal["disable", "enable"] | None = ...,
        p2p_block_list: Literal["skype", "edonkey", "bittorrent"] | list[str] | None = ...,
        deep_app_inspection: Literal["disable", "enable"] | None = ...,
        options: Literal["allow-dns", "allow-icmp", "allow-http", "allow-ssl"] | list[str] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        control_default_network_services: Literal["disable", "enable"] | None = ...,
        default_network_services: str | list[str] | list[dict[str, Any]] | None = ...,
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
    ) -> ListObject: ...
    
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
        payload_dict: ListPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        other_application_action: Literal["pass", "block"] | None = ...,
        app_replacemsg: Literal["disable", "enable"] | None = ...,
        other_application_log: Literal["disable", "enable"] | None = ...,
        enforce_default_app_port: Literal["disable", "enable"] | None = ...,
        force_inclusion_ssl_di_sigs: Literal["disable", "enable"] | None = ...,
        unknown_application_action: Literal["pass", "block"] | None = ...,
        unknown_application_log: Literal["disable", "enable"] | None = ...,
        p2p_block_list: Literal["skype", "edonkey", "bittorrent"] | list[str] | None = ...,
        deep_app_inspection: Literal["disable", "enable"] | None = ...,
        options: Literal["allow-dns", "allow-icmp", "allow-http", "allow-ssl"] | list[str] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        control_default_network_services: Literal["disable", "enable"] | None = ...,
        default_network_services: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "List",
    "ListPayload",
    "ListObject",
]