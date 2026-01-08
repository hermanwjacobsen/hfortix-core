from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class LocalInPolicyPayload(TypedDict, total=False):
    """
    Type hints for firewall/local_in_policy payload fields.
    
    Configure user defined IPv4 local-in policies.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.firewall.schedule.group.GroupEndpoint` (via: schedule)
        - :class:`~.firewall.schedule.onetime.OnetimeEndpoint` (via: schedule)
        - :class:`~.firewall.schedule.recurring.RecurringEndpoint` (via: schedule)

    **Usage:**
        payload: LocalInPolicyPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    policyid: NotRequired[int]  # User defined local in policy ID.
    uuid: NotRequired[str]  # Universally Unique Identifier
    ha_mgmt_intf_only: NotRequired[Literal["enable", "disable"]]  # Enable/disable dedicating the HA management interface only f
    intf: list[dict[str, Any]]  # Incoming interface name from available options.
    srcaddr: list[dict[str, Any]]  # Source address object from available options.
    srcaddr_negate: NotRequired[Literal["enable", "disable"]]  # When enabled srcaddr specifies what the source address must
    dstaddr: list[dict[str, Any]]  # Destination address object from available options.
    internet_service_src: NotRequired[Literal["enable", "disable"]]  # Enable/disable use of Internet Services in source for this l
    internet_service_src_name: NotRequired[list[dict[str, Any]]]  # Internet Service source name.
    internet_service_src_group: NotRequired[list[dict[str, Any]]]  # Internet Service source group name.
    internet_service_src_custom: NotRequired[list[dict[str, Any]]]  # Custom Internet Service source name.
    internet_service_src_custom_group: NotRequired[list[dict[str, Any]]]  # Custom Internet Service source group name.
    internet_service_src_fortiguard: NotRequired[list[dict[str, Any]]]  # FortiGuard Internet Service source name.
    dstaddr_negate: NotRequired[Literal["enable", "disable"]]  # When enabled dstaddr specifies what the destination address
    action: NotRequired[Literal["accept", "deny"]]  # Action performed on traffic matching the policy
    service: list[dict[str, Any]]  # Service object from available options.
    service_negate: NotRequired[Literal["enable", "disable"]]  # When enabled service specifies what the service must NOT be.
    internet_service_src_negate: NotRequired[Literal["enable", "disable"]]  # When enabled internet-service-src specifies what the service
    schedule: str  # Schedule object from available options.
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable this local-in policy.
    virtual_patch: NotRequired[Literal["enable", "disable"]]  # Enable/disable virtual patching.
    logtraffic: NotRequired[Literal["enable", "disable"]]  # Enable/disable local-in traffic logging.
    comments: NotRequired[str]  # Comment.

# Nested classes for table field children

@final
class LocalInPolicyIntfObject:
    """Typed object for intf table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Address name.
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
class LocalInPolicySrcaddrObject:
    """Typed object for srcaddr table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Address name.
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
class LocalInPolicyDstaddrObject:
    """Typed object for dstaddr table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Address name.
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
class LocalInPolicyInternetservicesrcnameObject:
    """Typed object for internet-service-src-name table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Internet Service name.
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
class LocalInPolicyInternetservicesrcgroupObject:
    """Typed object for internet-service-src-group table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Internet Service group name.
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
class LocalInPolicyInternetservicesrccustomObject:
    """Typed object for internet-service-src-custom table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Custom Internet Service name.
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
class LocalInPolicyInternetservicesrccustomgroupObject:
    """Typed object for internet-service-src-custom-group table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Custom Internet Service group name.
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
class LocalInPolicyInternetservicesrcfortiguardObject:
    """Typed object for internet-service-src-fortiguard table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # FortiGuard Internet Service name.
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
class LocalInPolicyServiceObject:
    """Typed object for service table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Service name.
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
class LocalInPolicyResponse(TypedDict):
    """
    Type hints for firewall/local_in_policy API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    policyid: int
    uuid: str
    ha_mgmt_intf_only: Literal["enable", "disable"]
    intf: list[dict[str, Any]]
    srcaddr: list[dict[str, Any]]
    srcaddr_negate: Literal["enable", "disable"]
    dstaddr: list[dict[str, Any]]
    internet_service_src: Literal["enable", "disable"]
    internet_service_src_name: list[dict[str, Any]]
    internet_service_src_group: list[dict[str, Any]]
    internet_service_src_custom: list[dict[str, Any]]
    internet_service_src_custom_group: list[dict[str, Any]]
    internet_service_src_fortiguard: list[dict[str, Any]]
    dstaddr_negate: Literal["enable", "disable"]
    action: Literal["accept", "deny"]
    service: list[dict[str, Any]]
    service_negate: Literal["enable", "disable"]
    internet_service_src_negate: Literal["enable", "disable"]
    schedule: str
    status: Literal["enable", "disable"]
    virtual_patch: Literal["enable", "disable"]
    logtraffic: Literal["enable", "disable"]
    comments: str


@final
class LocalInPolicyObject:
    """Typed FortiObject for firewall/local_in_policy with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # User defined local in policy ID.
    policyid: int
    # Universally Unique Identifier
    uuid: str
    # Enable/disable dedicating the HA management interface only for local-in policy.
    ha_mgmt_intf_only: Literal["enable", "disable"]
    # Incoming interface name from available options.
    intf: list[LocalInPolicyIntfObject]  # Table field - list of typed objects
    # Source address object from available options.
    srcaddr: list[LocalInPolicySrcaddrObject]  # Table field - list of typed objects
    # When enabled srcaddr specifies what the source address must NOT be.
    srcaddr_negate: Literal["enable", "disable"]
    # Destination address object from available options.
    dstaddr: list[LocalInPolicyDstaddrObject]  # Table field - list of typed objects
    # Enable/disable use of Internet Services in source for this local-in policy. If e
    internet_service_src: Literal["enable", "disable"]
    # Internet Service source name.
    internet_service_src_name: list[LocalInPolicyInternetservicesrcnameObject]  # Table field - list of typed objects
    # Internet Service source group name.
    internet_service_src_group: list[LocalInPolicyInternetservicesrcgroupObject]  # Table field - list of typed objects
    # Custom Internet Service source name.
    internet_service_src_custom: list[LocalInPolicyInternetservicesrccustomObject]  # Table field - list of typed objects
    # Custom Internet Service source group name.
    internet_service_src_custom_group: list[LocalInPolicyInternetservicesrccustomgroupObject]  # Table field - list of typed objects
    # FortiGuard Internet Service source name.
    internet_service_src_fortiguard: list[LocalInPolicyInternetservicesrcfortiguardObject]  # Table field - list of typed objects
    # When enabled dstaddr specifies what the destination address must NOT be.
    dstaddr_negate: Literal["enable", "disable"]
    # Action performed on traffic matching the policy (default = deny).
    action: Literal["accept", "deny"]
    # Service object from available options.
    service: list[LocalInPolicyServiceObject]  # Table field - list of typed objects
    # When enabled service specifies what the service must NOT be.
    service_negate: Literal["enable", "disable"]
    # When enabled internet-service-src specifies what the service must NOT be.
    internet_service_src_negate: Literal["enable", "disable"]
    # Schedule object from available options.
    schedule: str
    # Enable/disable this local-in policy.
    status: Literal["enable", "disable"]
    # Enable/disable virtual patching.
    virtual_patch: Literal["enable", "disable"]
    # Enable/disable local-in traffic logging.
    logtraffic: Literal["enable", "disable"]
    # Comment.
    comments: str
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> LocalInPolicyPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class LocalInPolicy:
    """
    Configure user defined IPv4 local-in policies.
    
    Path: firewall/local_in_policy
    Category: cmdb
    Primary Key: policyid
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey/name provided as positional arg)
    @overload
    def get(
        self,
        policyid: int,
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
    ) -> LocalInPolicyObject: ...
    
    # Single object (mkey/name provided as keyword arg)
    @overload
    def get(
        self,
        *,
        policyid: int,
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
    ) -> LocalInPolicyObject: ...
    
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
    ) -> list[LocalInPolicyObject]: ...
    
    @overload
    def get(
        self,
        policyid: int | None = ...,
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
        policyid: int,
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
    ) -> LocalInPolicyResponse: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
        policyid: int,
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
    ) -> LocalInPolicyResponse: ...
    
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
    ) -> list[LocalInPolicyResponse]: ...
    
    # Default overload for dict mode
    @overload
    def get(
        self,
        policyid: int | None = ...,
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
        policyid: int | None = ...,
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
    ) -> LocalInPolicyObject | list[LocalInPolicyObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: LocalInPolicyPayload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        ha_mgmt_intf_only: Literal["enable", "disable"] | None = ...,
        intf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        schedule: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        virtual_patch: Literal["enable", "disable"] | None = ...,
        logtraffic: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> LocalInPolicyObject: ...
    
    @overload
    def post(
        self,
        payload_dict: LocalInPolicyPayload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        ha_mgmt_intf_only: Literal["enable", "disable"] | None = ...,
        intf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        schedule: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        virtual_patch: Literal["enable", "disable"] | None = ...,
        logtraffic: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: LocalInPolicyPayload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        ha_mgmt_intf_only: Literal["enable", "disable"] | None = ...,
        intf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        schedule: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        virtual_patch: Literal["enable", "disable"] | None = ...,
        logtraffic: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: LocalInPolicyPayload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        ha_mgmt_intf_only: Literal["enable", "disable"] | None = ...,
        intf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        schedule: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        virtual_patch: Literal["enable", "disable"] | None = ...,
        logtraffic: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: LocalInPolicyPayload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        ha_mgmt_intf_only: Literal["enable", "disable"] | None = ...,
        intf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        schedule: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        virtual_patch: Literal["enable", "disable"] | None = ...,
        logtraffic: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> LocalInPolicyObject: ...
    
    @overload
    def put(
        self,
        payload_dict: LocalInPolicyPayload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        ha_mgmt_intf_only: Literal["enable", "disable"] | None = ...,
        intf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        schedule: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        virtual_patch: Literal["enable", "disable"] | None = ...,
        logtraffic: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: LocalInPolicyPayload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        ha_mgmt_intf_only: Literal["enable", "disable"] | None = ...,
        intf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        schedule: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        virtual_patch: Literal["enable", "disable"] | None = ...,
        logtraffic: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: LocalInPolicyPayload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        ha_mgmt_intf_only: Literal["enable", "disable"] | None = ...,
        intf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        schedule: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        virtual_patch: Literal["enable", "disable"] | None = ...,
        logtraffic: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> LocalInPolicyObject: ...
    
    @overload
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        policyid: int,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: LocalInPolicyPayload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        ha_mgmt_intf_only: Literal["enable", "disable"] | None = ...,
        intf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        schedule: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        virtual_patch: Literal["enable", "disable"] | None = ...,
        logtraffic: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
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
    "LocalInPolicy",
    "LocalInPolicyPayload",
    "LocalInPolicyObject",
]