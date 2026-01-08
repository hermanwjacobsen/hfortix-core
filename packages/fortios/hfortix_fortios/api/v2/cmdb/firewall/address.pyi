from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class AddressPayload(TypedDict, total=False):
    """
    Type hints for firewall/address payload fields.
    
    Configure IPv4 addresses.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: associated-interface, interface)
        - :class:`~.system.sdn-connector.SdnConnectorEndpoint` (via: sdn)
        - :class:`~.system.zone.ZoneEndpoint` (via: associated-interface)

    **Usage:**
        payload: AddressPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Address name.
    uuid: NotRequired[str]  # Universally Unique Identifier
    subnet: NotRequired[str]  # IP address and subnet mask of address.
    type: NotRequired[Literal["ipmask", "iprange", "fqdn", "geography", "wildcard", "dynamic", "interface-subnet", "mac", "route-tag"]]  # Type of address.
    route_tag: NotRequired[int]  # route-tag address.
    sub_type: NotRequired[Literal["sdn", "clearpass-spt", "fsso", "rsso", "ems-tag", "fortivoice-tag", "fortinac-tag", "swc-tag", "device-identification", "external-resource", "obsolete"]]  # Sub-type of address.
    clearpass_spt: NotRequired[Literal["unknown", "healthy", "quarantine", "checkup", "transient", "infected"]]  # SPT (System Posture Token) value.
    macaddr: NotRequired[list[dict[str, Any]]]  # Multiple MAC address ranges.
    start_ip: NotRequired[str]  # First IP address (inclusive) in the range for the address.
    end_ip: NotRequired[str]  # Final IP address (inclusive) in the range for the address.
    fqdn: NotRequired[str]  # Fully Qualified Domain Name address.
    country: NotRequired[str]  # IP addresses associated to a specific country.
    wildcard_fqdn: NotRequired[str]  # Fully Qualified Domain Name with wildcard characters.
    cache_ttl: NotRequired[int]  # Defines the minimal TTL of individual IP addresses in FQDN c
    wildcard: NotRequired[str]  # IP address and wildcard netmask.
    sdn: NotRequired[str]  # SDN.
    fsso_group: NotRequired[list[dict[str, Any]]]  # FSSO group(s).
    sso_attribute_value: NotRequired[list[dict[str, Any]]]  # RADIUS attributes value.
    interface: str  # Name of interface whose IP address is to be used.
    tenant: NotRequired[str]  # Tenant.
    organization: NotRequired[str]  # Organization domain name (Syntax: organization/domain).
    epg_name: NotRequired[str]  # Endpoint group name.
    subnet_name: NotRequired[str]  # Subnet name.
    sdn_tag: NotRequired[str]  # SDN Tag.
    policy_group: NotRequired[str]  # Policy group name.
    obj_tag: NotRequired[str]  # Tag of dynamic address object.
    obj_type: NotRequired[Literal["ip", "mac"]]  # Object type.
    tag_detection_level: NotRequired[str]  # Tag detection level of dynamic address object.
    tag_type: NotRequired[str]  # Tag type of dynamic address object.
    hw_vendor: NotRequired[str]  # Dynamic address matching hardware vendor.
    hw_model: NotRequired[str]  # Dynamic address matching hardware model.
    os: NotRequired[str]  # Dynamic address matching operating system.
    sw_version: NotRequired[str]  # Dynamic address matching software version.
    comment: NotRequired[str]  # Comment.
    associated_interface: NotRequired[str]  # Network interface associated with address.
    color: NotRequired[int]  # Color of icon on the GUI.
    filter: str  # Match criteria filter.
    sdn_addr_type: NotRequired[Literal["private", "public", "all"]]  # Type of addresses to collect.
    node_ip_only: NotRequired[Literal["enable", "disable"]]  # Enable/disable collection of node addresses only in Kubernet
    obj_id: NotRequired[str]  # Object ID for NSX.
    list: NotRequired[list[dict[str, Any]]]  # IP address list.
    tagging: NotRequired[list[dict[str, Any]]]  # Config object tagging.
    allow_routing: NotRequired[Literal["enable", "disable"]]  # Enable/disable use of this address in routing configurations
    passive_fqdn_learning: NotRequired[Literal["disable", "enable"]]  # Enable/disable passive learning of FQDNs.  When enabled, the
    fabric_object: NotRequired[Literal["enable", "disable"]]  # Security Fabric global object setting.

# Nested classes for table field children

@final
class AddressMacaddrObject:
    """Typed object for macaddr table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # MAC address ranges <start>[-<end>] separated by space.
    macaddr: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class AddressFssogroupObject:
    """Typed object for fsso-group table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # FSSO group name.
    name: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class AddressSsoattributevalueObject:
    """Typed object for sso-attribute-value table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # RADIUS attribute value.
    name: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class AddressListObject:
    """Typed object for list table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # IP.
    ip: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class AddressTaggingObject:
    """Typed object for tagging table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Tagging entry name.
    name: str
    # Tag category.
    category: str
    # Tags.
    tags: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class AddressResponse(TypedDict):
    """
    Type hints for firewall/address API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    uuid: str
    subnet: str
    type: Literal["ipmask", "iprange", "fqdn", "geography", "wildcard", "dynamic", "interface-subnet", "mac", "route-tag"]
    route_tag: int
    sub_type: Literal["sdn", "clearpass-spt", "fsso", "rsso", "ems-tag", "fortivoice-tag", "fortinac-tag", "swc-tag", "device-identification", "external-resource", "obsolete"]
    clearpass_spt: Literal["unknown", "healthy", "quarantine", "checkup", "transient", "infected"]
    macaddr: list[dict[str, Any]]
    start_ip: str
    end_ip: str
    fqdn: str
    country: str
    wildcard_fqdn: str
    cache_ttl: int
    wildcard: str
    sdn: str
    fsso_group: list[dict[str, Any]]
    sso_attribute_value: list[dict[str, Any]]
    interface: str
    tenant: str
    organization: str
    epg_name: str
    subnet_name: str
    sdn_tag: str
    policy_group: str
    obj_tag: str
    obj_type: Literal["ip", "mac"]
    tag_detection_level: str
    tag_type: str
    hw_vendor: str
    hw_model: str
    os: str
    sw_version: str
    comment: str
    associated_interface: str
    color: int
    filter: str
    sdn_addr_type: Literal["private", "public", "all"]
    node_ip_only: Literal["enable", "disable"]
    obj_id: str
    list: list[dict[str, Any]]
    tagging: list[dict[str, Any]]
    allow_routing: Literal["enable", "disable"]
    passive_fqdn_learning: Literal["disable", "enable"]
    fabric_object: Literal["enable", "disable"]


@final
class AddressObject:
    """Typed FortiObject for firewall/address with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Address name.
    name: str
    # Universally Unique Identifier
    uuid: str
    # IP address and subnet mask of address.
    subnet: str
    # Type of address.
    type: Literal["ipmask", "iprange", "fqdn", "geography", "wildcard", "dynamic", "interface-subnet", "mac", "route-tag"]
    # route-tag address.
    route_tag: int
    # Sub-type of address.
    sub_type: Literal["sdn", "clearpass-spt", "fsso", "rsso", "ems-tag", "fortivoice-tag", "fortinac-tag", "swc-tag", "device-identification", "external-resource", "obsolete"]
    # SPT (System Posture Token) value.
    clearpass_spt: Literal["unknown", "healthy", "quarantine", "checkup", "transient", "infected"]
    # Multiple MAC address ranges.
    macaddr: list[AddressMacaddrObject]  # Table field - list of typed objects
    # First IP address (inclusive) in the range for the address.
    start_ip: str
    # Final IP address (inclusive) in the range for the address.
    end_ip: str
    # Fully Qualified Domain Name address.
    fqdn: str
    # IP addresses associated to a specific country.
    country: str
    # Fully Qualified Domain Name with wildcard characters.
    wildcard_fqdn: str
    # Defines the minimal TTL of individual IP addresses in FQDN cache measured in sec
    cache_ttl: int
    # IP address and wildcard netmask.
    wildcard: str
    # SDN.
    sdn: str
    # FSSO group(s).
    fsso_group: list[AddressFssogroupObject]  # Table field - list of typed objects
    # RADIUS attributes value.
    sso_attribute_value: list[AddressSsoattributevalueObject]  # Table field - list of typed objects
    # Name of interface whose IP address is to be used.
    interface: str
    # Tenant.
    tenant: str
    # Organization domain name (Syntax: organization/domain).
    organization: str
    # Endpoint group name.
    epg_name: str
    # Subnet name.
    subnet_name: str
    # SDN Tag.
    sdn_tag: str
    # Policy group name.
    policy_group: str
    # Tag of dynamic address object.
    obj_tag: str
    # Object type.
    obj_type: Literal["ip", "mac"]
    # Tag detection level of dynamic address object.
    tag_detection_level: str
    # Tag type of dynamic address object.
    tag_type: str
    # Dynamic address matching hardware vendor.
    hw_vendor: str
    # Dynamic address matching hardware model.
    hw_model: str
    # Dynamic address matching operating system.
    os: str
    # Dynamic address matching software version.
    sw_version: str
    # Comment.
    comment: str
    # Network interface associated with address.
    associated_interface: str
    # Color of icon on the GUI.
    color: int
    # Match criteria filter.
    filter: str
    # Type of addresses to collect.
    sdn_addr_type: Literal["private", "public", "all"]
    # Enable/disable collection of node addresses only in Kubernetes.
    node_ip_only: Literal["enable", "disable"]
    # Object ID for NSX.
    obj_id: str
    # IP address list.
    list: list[AddressListObject]  # Table field - list of typed objects
    # Config object tagging.
    tagging: list[AddressTaggingObject]  # Table field - list of typed objects
    # Enable/disable use of this address in routing configurations.
    allow_routing: Literal["enable", "disable"]
    # Enable/disable passive learning of FQDNs.  When enabled, the FortiGate learns, t
    passive_fqdn_learning: Literal["disable", "enable"]
    # Security Fabric global object setting.
    fabric_object: Literal["enable", "disable"]
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> AddressPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Address:
    """
    Configure IPv4 addresses.
    
    Path: firewall/address
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
    ) -> AddressObject: ...
    
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
    ) -> AddressObject: ...
    
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
    ) -> list[AddressObject]: ...
    
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
    ) -> AddressResponse: ...
    
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
    ) -> AddressResponse: ...
    
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
    ) -> list[AddressResponse]: ...
    
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
    ) -> AddressObject | list[AddressObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: AddressPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        subnet: str | None = ...,
        type: Literal["ipmask", "iprange", "fqdn", "geography", "wildcard", "dynamic", "interface-subnet", "mac", "route-tag"] | None = ...,
        route_tag: int | None = ...,
        sub_type: Literal["sdn", "clearpass-spt", "fsso", "rsso", "ems-tag", "fortivoice-tag", "fortinac-tag", "swc-tag", "device-identification", "external-resource", "obsolete"] | None = ...,
        clearpass_spt: Literal["unknown", "healthy", "quarantine", "checkup", "transient", "infected"] | None = ...,
        macaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        start_ip: str | None = ...,
        end_ip: str | None = ...,
        fqdn: str | None = ...,
        country: str | None = ...,
        wildcard_fqdn: str | None = ...,
        cache_ttl: int | None = ...,
        wildcard: str | None = ...,
        sdn: str | None = ...,
        fsso_group: str | list[str] | list[dict[str, Any]] | None = ...,
        sso_attribute_value: str | list[str] | list[dict[str, Any]] | None = ...,
        interface: str | None = ...,
        tenant: str | None = ...,
        organization: str | None = ...,
        epg_name: str | None = ...,
        subnet_name: str | None = ...,
        sdn_tag: str | None = ...,
        policy_group: str | None = ...,
        obj_tag: str | None = ...,
        obj_type: Literal["ip", "mac"] | None = ...,
        tag_detection_level: str | None = ...,
        tag_type: str | None = ...,
        hw_vendor: str | None = ...,
        hw_model: str | None = ...,
        os: str | None = ...,
        sw_version: str | None = ...,
        comment: str | None = ...,
        associated_interface: str | None = ...,
        color: int | None = ...,
        filter: str | None = ...,
        sdn_addr_type: Literal["private", "public", "all"] | None = ...,
        node_ip_only: Literal["enable", "disable"] | None = ...,
        obj_id: str | None = ...,
        list: str | list[str] | list[dict[str, Any]] | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        allow_routing: Literal["enable", "disable"] | None = ...,
        passive_fqdn_learning: Literal["disable", "enable"] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> AddressObject: ...
    
    @overload
    def post(
        self,
        payload_dict: AddressPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        subnet: str | None = ...,
        type: Literal["ipmask", "iprange", "fqdn", "geography", "wildcard", "dynamic", "interface-subnet", "mac", "route-tag"] | None = ...,
        route_tag: int | None = ...,
        sub_type: Literal["sdn", "clearpass-spt", "fsso", "rsso", "ems-tag", "fortivoice-tag", "fortinac-tag", "swc-tag", "device-identification", "external-resource", "obsolete"] | None = ...,
        clearpass_spt: Literal["unknown", "healthy", "quarantine", "checkup", "transient", "infected"] | None = ...,
        macaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        start_ip: str | None = ...,
        end_ip: str | None = ...,
        fqdn: str | None = ...,
        country: str | None = ...,
        wildcard_fqdn: str | None = ...,
        cache_ttl: int | None = ...,
        wildcard: str | None = ...,
        sdn: str | None = ...,
        fsso_group: str | list[str] | list[dict[str, Any]] | None = ...,
        sso_attribute_value: str | list[str] | list[dict[str, Any]] | None = ...,
        interface: str | None = ...,
        tenant: str | None = ...,
        organization: str | None = ...,
        epg_name: str | None = ...,
        subnet_name: str | None = ...,
        sdn_tag: str | None = ...,
        policy_group: str | None = ...,
        obj_tag: str | None = ...,
        obj_type: Literal["ip", "mac"] | None = ...,
        tag_detection_level: str | None = ...,
        tag_type: str | None = ...,
        hw_vendor: str | None = ...,
        hw_model: str | None = ...,
        os: str | None = ...,
        sw_version: str | None = ...,
        comment: str | None = ...,
        associated_interface: str | None = ...,
        color: int | None = ...,
        filter: str | None = ...,
        sdn_addr_type: Literal["private", "public", "all"] | None = ...,
        node_ip_only: Literal["enable", "disable"] | None = ...,
        obj_id: str | None = ...,
        list: str | list[str] | list[dict[str, Any]] | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        allow_routing: Literal["enable", "disable"] | None = ...,
        passive_fqdn_learning: Literal["disable", "enable"] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: AddressPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        subnet: str | None = ...,
        type: Literal["ipmask", "iprange", "fqdn", "geography", "wildcard", "dynamic", "interface-subnet", "mac", "route-tag"] | None = ...,
        route_tag: int | None = ...,
        sub_type: Literal["sdn", "clearpass-spt", "fsso", "rsso", "ems-tag", "fortivoice-tag", "fortinac-tag", "swc-tag", "device-identification", "external-resource", "obsolete"] | None = ...,
        clearpass_spt: Literal["unknown", "healthy", "quarantine", "checkup", "transient", "infected"] | None = ...,
        macaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        start_ip: str | None = ...,
        end_ip: str | None = ...,
        fqdn: str | None = ...,
        country: str | None = ...,
        wildcard_fqdn: str | None = ...,
        cache_ttl: int | None = ...,
        wildcard: str | None = ...,
        sdn: str | None = ...,
        fsso_group: str | list[str] | list[dict[str, Any]] | None = ...,
        sso_attribute_value: str | list[str] | list[dict[str, Any]] | None = ...,
        interface: str | None = ...,
        tenant: str | None = ...,
        organization: str | None = ...,
        epg_name: str | None = ...,
        subnet_name: str | None = ...,
        sdn_tag: str | None = ...,
        policy_group: str | None = ...,
        obj_tag: str | None = ...,
        obj_type: Literal["ip", "mac"] | None = ...,
        tag_detection_level: str | None = ...,
        tag_type: str | None = ...,
        hw_vendor: str | None = ...,
        hw_model: str | None = ...,
        os: str | None = ...,
        sw_version: str | None = ...,
        comment: str | None = ...,
        associated_interface: str | None = ...,
        color: int | None = ...,
        filter: str | None = ...,
        sdn_addr_type: Literal["private", "public", "all"] | None = ...,
        node_ip_only: Literal["enable", "disable"] | None = ...,
        obj_id: str | None = ...,
        list: str | list[str] | list[dict[str, Any]] | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        allow_routing: Literal["enable", "disable"] | None = ...,
        passive_fqdn_learning: Literal["disable", "enable"] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: AddressPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        subnet: str | None = ...,
        type: Literal["ipmask", "iprange", "fqdn", "geography", "wildcard", "dynamic", "interface-subnet", "mac", "route-tag"] | None = ...,
        route_tag: int | None = ...,
        sub_type: Literal["sdn", "clearpass-spt", "fsso", "rsso", "ems-tag", "fortivoice-tag", "fortinac-tag", "swc-tag", "device-identification", "external-resource", "obsolete"] | None = ...,
        clearpass_spt: Literal["unknown", "healthy", "quarantine", "checkup", "transient", "infected"] | None = ...,
        macaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        start_ip: str | None = ...,
        end_ip: str | None = ...,
        fqdn: str | None = ...,
        country: str | None = ...,
        wildcard_fqdn: str | None = ...,
        cache_ttl: int | None = ...,
        wildcard: str | None = ...,
        sdn: str | None = ...,
        fsso_group: str | list[str] | list[dict[str, Any]] | None = ...,
        sso_attribute_value: str | list[str] | list[dict[str, Any]] | None = ...,
        interface: str | None = ...,
        tenant: str | None = ...,
        organization: str | None = ...,
        epg_name: str | None = ...,
        subnet_name: str | None = ...,
        sdn_tag: str | None = ...,
        policy_group: str | None = ...,
        obj_tag: str | None = ...,
        obj_type: Literal["ip", "mac"] | None = ...,
        tag_detection_level: str | None = ...,
        tag_type: str | None = ...,
        hw_vendor: str | None = ...,
        hw_model: str | None = ...,
        os: str | None = ...,
        sw_version: str | None = ...,
        comment: str | None = ...,
        associated_interface: str | None = ...,
        color: int | None = ...,
        filter: str | None = ...,
        sdn_addr_type: Literal["private", "public", "all"] | None = ...,
        node_ip_only: Literal["enable", "disable"] | None = ...,
        obj_id: str | None = ...,
        list: str | list[str] | list[dict[str, Any]] | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        allow_routing: Literal["enable", "disable"] | None = ...,
        passive_fqdn_learning: Literal["disable", "enable"] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: AddressPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        subnet: str | None = ...,
        type: Literal["ipmask", "iprange", "fqdn", "geography", "wildcard", "dynamic", "interface-subnet", "mac", "route-tag"] | None = ...,
        route_tag: int | None = ...,
        sub_type: Literal["sdn", "clearpass-spt", "fsso", "rsso", "ems-tag", "fortivoice-tag", "fortinac-tag", "swc-tag", "device-identification", "external-resource", "obsolete"] | None = ...,
        clearpass_spt: Literal["unknown", "healthy", "quarantine", "checkup", "transient", "infected"] | None = ...,
        macaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        start_ip: str | None = ...,
        end_ip: str | None = ...,
        fqdn: str | None = ...,
        country: str | None = ...,
        wildcard_fqdn: str | None = ...,
        cache_ttl: int | None = ...,
        wildcard: str | None = ...,
        sdn: str | None = ...,
        fsso_group: str | list[str] | list[dict[str, Any]] | None = ...,
        sso_attribute_value: str | list[str] | list[dict[str, Any]] | None = ...,
        interface: str | None = ...,
        tenant: str | None = ...,
        organization: str | None = ...,
        epg_name: str | None = ...,
        subnet_name: str | None = ...,
        sdn_tag: str | None = ...,
        policy_group: str | None = ...,
        obj_tag: str | None = ...,
        obj_type: Literal["ip", "mac"] | None = ...,
        tag_detection_level: str | None = ...,
        tag_type: str | None = ...,
        hw_vendor: str | None = ...,
        hw_model: str | None = ...,
        os: str | None = ...,
        sw_version: str | None = ...,
        comment: str | None = ...,
        associated_interface: str | None = ...,
        color: int | None = ...,
        filter: str | None = ...,
        sdn_addr_type: Literal["private", "public", "all"] | None = ...,
        node_ip_only: Literal["enable", "disable"] | None = ...,
        obj_id: str | None = ...,
        list: str | list[str] | list[dict[str, Any]] | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        allow_routing: Literal["enable", "disable"] | None = ...,
        passive_fqdn_learning: Literal["disable", "enable"] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> AddressObject: ...
    
    @overload
    def put(
        self,
        payload_dict: AddressPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        subnet: str | None = ...,
        type: Literal["ipmask", "iprange", "fqdn", "geography", "wildcard", "dynamic", "interface-subnet", "mac", "route-tag"] | None = ...,
        route_tag: int | None = ...,
        sub_type: Literal["sdn", "clearpass-spt", "fsso", "rsso", "ems-tag", "fortivoice-tag", "fortinac-tag", "swc-tag", "device-identification", "external-resource", "obsolete"] | None = ...,
        clearpass_spt: Literal["unknown", "healthy", "quarantine", "checkup", "transient", "infected"] | None = ...,
        macaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        start_ip: str | None = ...,
        end_ip: str | None = ...,
        fqdn: str | None = ...,
        country: str | None = ...,
        wildcard_fqdn: str | None = ...,
        cache_ttl: int | None = ...,
        wildcard: str | None = ...,
        sdn: str | None = ...,
        fsso_group: str | list[str] | list[dict[str, Any]] | None = ...,
        sso_attribute_value: str | list[str] | list[dict[str, Any]] | None = ...,
        interface: str | None = ...,
        tenant: str | None = ...,
        organization: str | None = ...,
        epg_name: str | None = ...,
        subnet_name: str | None = ...,
        sdn_tag: str | None = ...,
        policy_group: str | None = ...,
        obj_tag: str | None = ...,
        obj_type: Literal["ip", "mac"] | None = ...,
        tag_detection_level: str | None = ...,
        tag_type: str | None = ...,
        hw_vendor: str | None = ...,
        hw_model: str | None = ...,
        os: str | None = ...,
        sw_version: str | None = ...,
        comment: str | None = ...,
        associated_interface: str | None = ...,
        color: int | None = ...,
        filter: str | None = ...,
        sdn_addr_type: Literal["private", "public", "all"] | None = ...,
        node_ip_only: Literal["enable", "disable"] | None = ...,
        obj_id: str | None = ...,
        list: str | list[str] | list[dict[str, Any]] | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        allow_routing: Literal["enable", "disable"] | None = ...,
        passive_fqdn_learning: Literal["disable", "enable"] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: AddressPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        subnet: str | None = ...,
        type: Literal["ipmask", "iprange", "fqdn", "geography", "wildcard", "dynamic", "interface-subnet", "mac", "route-tag"] | None = ...,
        route_tag: int | None = ...,
        sub_type: Literal["sdn", "clearpass-spt", "fsso", "rsso", "ems-tag", "fortivoice-tag", "fortinac-tag", "swc-tag", "device-identification", "external-resource", "obsolete"] | None = ...,
        clearpass_spt: Literal["unknown", "healthy", "quarantine", "checkup", "transient", "infected"] | None = ...,
        macaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        start_ip: str | None = ...,
        end_ip: str | None = ...,
        fqdn: str | None = ...,
        country: str | None = ...,
        wildcard_fqdn: str | None = ...,
        cache_ttl: int | None = ...,
        wildcard: str | None = ...,
        sdn: str | None = ...,
        fsso_group: str | list[str] | list[dict[str, Any]] | None = ...,
        sso_attribute_value: str | list[str] | list[dict[str, Any]] | None = ...,
        interface: str | None = ...,
        tenant: str | None = ...,
        organization: str | None = ...,
        epg_name: str | None = ...,
        subnet_name: str | None = ...,
        sdn_tag: str | None = ...,
        policy_group: str | None = ...,
        obj_tag: str | None = ...,
        obj_type: Literal["ip", "mac"] | None = ...,
        tag_detection_level: str | None = ...,
        tag_type: str | None = ...,
        hw_vendor: str | None = ...,
        hw_model: str | None = ...,
        os: str | None = ...,
        sw_version: str | None = ...,
        comment: str | None = ...,
        associated_interface: str | None = ...,
        color: int | None = ...,
        filter: str | None = ...,
        sdn_addr_type: Literal["private", "public", "all"] | None = ...,
        node_ip_only: Literal["enable", "disable"] | None = ...,
        obj_id: str | None = ...,
        list: str | list[str] | list[dict[str, Any]] | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        allow_routing: Literal["enable", "disable"] | None = ...,
        passive_fqdn_learning: Literal["disable", "enable"] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: AddressPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        subnet: str | None = ...,
        type: Literal["ipmask", "iprange", "fqdn", "geography", "wildcard", "dynamic", "interface-subnet", "mac", "route-tag"] | None = ...,
        route_tag: int | None = ...,
        sub_type: Literal["sdn", "clearpass-spt", "fsso", "rsso", "ems-tag", "fortivoice-tag", "fortinac-tag", "swc-tag", "device-identification", "external-resource", "obsolete"] | None = ...,
        clearpass_spt: Literal["unknown", "healthy", "quarantine", "checkup", "transient", "infected"] | None = ...,
        macaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        start_ip: str | None = ...,
        end_ip: str | None = ...,
        fqdn: str | None = ...,
        country: str | None = ...,
        wildcard_fqdn: str | None = ...,
        cache_ttl: int | None = ...,
        wildcard: str | None = ...,
        sdn: str | None = ...,
        fsso_group: str | list[str] | list[dict[str, Any]] | None = ...,
        sso_attribute_value: str | list[str] | list[dict[str, Any]] | None = ...,
        interface: str | None = ...,
        tenant: str | None = ...,
        organization: str | None = ...,
        epg_name: str | None = ...,
        subnet_name: str | None = ...,
        sdn_tag: str | None = ...,
        policy_group: str | None = ...,
        obj_tag: str | None = ...,
        obj_type: Literal["ip", "mac"] | None = ...,
        tag_detection_level: str | None = ...,
        tag_type: str | None = ...,
        hw_vendor: str | None = ...,
        hw_model: str | None = ...,
        os: str | None = ...,
        sw_version: str | None = ...,
        comment: str | None = ...,
        associated_interface: str | None = ...,
        color: int | None = ...,
        filter: str | None = ...,
        sdn_addr_type: Literal["private", "public", "all"] | None = ...,
        node_ip_only: Literal["enable", "disable"] | None = ...,
        obj_id: str | None = ...,
        list: str | list[str] | list[dict[str, Any]] | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        allow_routing: Literal["enable", "disable"] | None = ...,
        passive_fqdn_learning: Literal["disable", "enable"] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
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
    ) -> AddressObject: ...
    
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
        payload_dict: AddressPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        subnet: str | None = ...,
        type: Literal["ipmask", "iprange", "fqdn", "geography", "wildcard", "dynamic", "interface-subnet", "mac", "route-tag"] | None = ...,
        route_tag: int | None = ...,
        sub_type: Literal["sdn", "clearpass-spt", "fsso", "rsso", "ems-tag", "fortivoice-tag", "fortinac-tag", "swc-tag", "device-identification", "external-resource", "obsolete"] | None = ...,
        clearpass_spt: Literal["unknown", "healthy", "quarantine", "checkup", "transient", "infected"] | None = ...,
        macaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        start_ip: str | None = ...,
        end_ip: str | None = ...,
        fqdn: str | None = ...,
        country: str | None = ...,
        wildcard_fqdn: str | None = ...,
        cache_ttl: int | None = ...,
        wildcard: str | None = ...,
        sdn: str | None = ...,
        fsso_group: str | list[str] | list[dict[str, Any]] | None = ...,
        sso_attribute_value: str | list[str] | list[dict[str, Any]] | None = ...,
        interface: str | None = ...,
        tenant: str | None = ...,
        organization: str | None = ...,
        epg_name: str | None = ...,
        subnet_name: str | None = ...,
        sdn_tag: str | None = ...,
        policy_group: str | None = ...,
        obj_tag: str | None = ...,
        obj_type: Literal["ip", "mac"] | None = ...,
        tag_detection_level: str | None = ...,
        tag_type: str | None = ...,
        hw_vendor: str | None = ...,
        hw_model: str | None = ...,
        os: str | None = ...,
        sw_version: str | None = ...,
        comment: str | None = ...,
        associated_interface: str | None = ...,
        color: int | None = ...,
        filter: str | None = ...,
        sdn_addr_type: Literal["private", "public", "all"] | None = ...,
        node_ip_only: Literal["enable", "disable"] | None = ...,
        obj_id: str | None = ...,
        list: str | list[str] | list[dict[str, Any]] | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        allow_routing: Literal["enable", "disable"] | None = ...,
        passive_fqdn_learning: Literal["disable", "enable"] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
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
    "Address",
    "AddressPayload",
    "AddressObject",
]