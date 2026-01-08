from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class NacPolicyPayload(TypedDict, total=False):
    """
    Type hints for user/nac_policy payload fields.
    
    Configure NAC policy matching pattern to identify matching NAC devices.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.firewall.address.AddressEndpoint` (via: ems-tag, firewall-address, fortivoice-tag)
        - :class:`~.switch-controller.mac-policy.MacPolicyEndpoint` (via: switch-mac-policy)
        - :class:`~.system.interface.InterfaceEndpoint` (via: switch-fortilink)
        - :class:`~.user.group.GroupEndpoint` (via: user-group)
        - :class:`~.wireless-controller.ssid-policy.SsidPolicyEndpoint` (via: ssid-policy)

    **Usage:**
        payload: NacPolicyPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # NAC policy name.
    description: NotRequired[str]  # Description for the NAC policy matching pattern.
    category: NotRequired[Literal["device", "firewall-user", "ems-tag", "fortivoice-tag", "vulnerability"]]  # Category of NAC policy.
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable NAC policy.
    match_type: NotRequired[Literal["dynamic", "override"]]  # Match and retain the devices based on the type.
    match_period: NotRequired[int]  # Number of days the matched devices will be retained
    match_remove: NotRequired[Literal["default", "link-down"]]  # Options to remove the matched override devices.
    mac: NotRequired[str]  # NAC policy matching MAC address.
    hw_vendor: NotRequired[str]  # NAC policy matching hardware vendor.
    type: NotRequired[str]  # NAC policy matching type.
    family: NotRequired[str]  # NAC policy matching family.
    os: NotRequired[str]  # NAC policy matching operating system.
    hw_version: NotRequired[str]  # NAC policy matching hardware version.
    sw_version: NotRequired[str]  # NAC policy matching software version.
    host: NotRequired[str]  # NAC policy matching host.
    user: NotRequired[str]  # NAC policy matching user.
    src: NotRequired[str]  # NAC policy matching source.
    user_group: NotRequired[str]  # NAC policy matching user group.
    ems_tag: NotRequired[str]  # NAC policy matching EMS tag.
    fortivoice_tag: NotRequired[str]  # NAC policy matching FortiVoice tag.
    severity: NotRequired[list[dict[str, Any]]]  # NAC policy matching devices vulnerability severity lists.
    switch_fortilink: NotRequired[str]  # FortiLink interface for which this NAC policy belongs to.
    switch_group: NotRequired[list[dict[str, Any]]]  # List of managed FortiSwitch groups on which NAC policy can b
    switch_mac_policy: NotRequired[str]  # Switch MAC policy action to be applied on the matched NAC po
    firewall_address: NotRequired[str]  # Dynamic firewall address to associate MAC which match this p
    ssid_policy: NotRequired[str]  # SSID policy to be applied on the matched NAC policy.

# Nested classes for table field children

@final
class NacPolicySeverityObject:
    """Typed object for severity table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Enter multiple severity levels, where 0 = Info, 1 = Low, ..., 4 = Critical
    severity_num: int
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class NacPolicySwitchgroupObject:
    """Typed object for switch-group table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Managed FortiSwitch group name from available options.
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
class NacPolicyResponse(TypedDict):
    """
    Type hints for user/nac_policy API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    description: str
    category: Literal["device", "firewall-user", "ems-tag", "fortivoice-tag", "vulnerability"]
    status: Literal["enable", "disable"]
    match_type: Literal["dynamic", "override"]
    match_period: int
    match_remove: Literal["default", "link-down"]
    mac: str
    hw_vendor: str
    type: str
    family: str
    os: str
    hw_version: str
    sw_version: str
    host: str
    user: str
    src: str
    user_group: str
    ems_tag: str
    fortivoice_tag: str
    severity: list[dict[str, Any]]
    switch_fortilink: str
    switch_group: list[dict[str, Any]]
    switch_mac_policy: str
    firewall_address: str
    ssid_policy: str


@final
class NacPolicyObject:
    """Typed FortiObject for user/nac_policy with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # NAC policy name.
    name: str
    # Description for the NAC policy matching pattern.
    description: str
    # Category of NAC policy.
    category: Literal["device", "firewall-user", "ems-tag", "fortivoice-tag", "vulnerability"]
    # Enable/disable NAC policy.
    status: Literal["enable", "disable"]
    # Match and retain the devices based on the type.
    match_type: Literal["dynamic", "override"]
    # Number of days the matched devices will be retained (0 - always retain)
    match_period: int
    # Options to remove the matched override devices.
    match_remove: Literal["default", "link-down"]
    # NAC policy matching MAC address.
    mac: str
    # NAC policy matching hardware vendor.
    hw_vendor: str
    # NAC policy matching type.
    type: str
    # NAC policy matching family.
    family: str
    # NAC policy matching operating system.
    os: str
    # NAC policy matching hardware version.
    hw_version: str
    # NAC policy matching software version.
    sw_version: str
    # NAC policy matching host.
    host: str
    # NAC policy matching user.
    user: str
    # NAC policy matching source.
    src: str
    # NAC policy matching user group.
    user_group: str
    # NAC policy matching EMS tag.
    ems_tag: str
    # NAC policy matching FortiVoice tag.
    fortivoice_tag: str
    # NAC policy matching devices vulnerability severity lists.
    severity: list[NacPolicySeverityObject]  # Table field - list of typed objects
    # FortiLink interface for which this NAC policy belongs to.
    switch_fortilink: str
    # List of managed FortiSwitch groups on which NAC policy can be applied.
    switch_group: list[NacPolicySwitchgroupObject]  # Table field - list of typed objects
    # Switch MAC policy action to be applied on the matched NAC policy.
    switch_mac_policy: str
    # Dynamic firewall address to associate MAC which match this policy.
    firewall_address: str
    # SSID policy to be applied on the matched NAC policy.
    ssid_policy: str
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> NacPolicyPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class NacPolicy:
    """
    Configure NAC policy matching pattern to identify matching NAC devices.
    
    Path: user/nac_policy
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
    ) -> NacPolicyObject: ...
    
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
    ) -> NacPolicyObject: ...
    
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
    ) -> list[NacPolicyObject]: ...
    
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
    ) -> NacPolicyResponse: ...
    
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
    ) -> NacPolicyResponse: ...
    
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
    ) -> list[NacPolicyResponse]: ...
    
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
    ) -> NacPolicyObject | list[NacPolicyObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: NacPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        category: Literal["device", "firewall-user", "ems-tag", "fortivoice-tag", "vulnerability"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        match_type: Literal["dynamic", "override"] | None = ...,
        match_period: int | None = ...,
        match_remove: Literal["default", "link-down"] | None = ...,
        mac: str | None = ...,
        hw_vendor: str | None = ...,
        type: str | None = ...,
        family: str | None = ...,
        os: str | None = ...,
        hw_version: str | None = ...,
        sw_version: str | None = ...,
        host: str | None = ...,
        user: str | None = ...,
        src: str | None = ...,
        user_group: str | None = ...,
        ems_tag: str | None = ...,
        fortivoice_tag: str | None = ...,
        severity: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_fortilink: str | None = ...,
        switch_group: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_mac_policy: str | None = ...,
        firewall_address: str | None = ...,
        ssid_policy: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> NacPolicyObject: ...
    
    @overload
    def post(
        self,
        payload_dict: NacPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        category: Literal["device", "firewall-user", "ems-tag", "fortivoice-tag", "vulnerability"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        match_type: Literal["dynamic", "override"] | None = ...,
        match_period: int | None = ...,
        match_remove: Literal["default", "link-down"] | None = ...,
        mac: str | None = ...,
        hw_vendor: str | None = ...,
        type: str | None = ...,
        family: str | None = ...,
        os: str | None = ...,
        hw_version: str | None = ...,
        sw_version: str | None = ...,
        host: str | None = ...,
        user: str | None = ...,
        src: str | None = ...,
        user_group: str | None = ...,
        ems_tag: str | None = ...,
        fortivoice_tag: str | None = ...,
        severity: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_fortilink: str | None = ...,
        switch_group: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_mac_policy: str | None = ...,
        firewall_address: str | None = ...,
        ssid_policy: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: NacPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        category: Literal["device", "firewall-user", "ems-tag", "fortivoice-tag", "vulnerability"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        match_type: Literal["dynamic", "override"] | None = ...,
        match_period: int | None = ...,
        match_remove: Literal["default", "link-down"] | None = ...,
        mac: str | None = ...,
        hw_vendor: str | None = ...,
        type: str | None = ...,
        family: str | None = ...,
        os: str | None = ...,
        hw_version: str | None = ...,
        sw_version: str | None = ...,
        host: str | None = ...,
        user: str | None = ...,
        src: str | None = ...,
        user_group: str | None = ...,
        ems_tag: str | None = ...,
        fortivoice_tag: str | None = ...,
        severity: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_fortilink: str | None = ...,
        switch_group: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_mac_policy: str | None = ...,
        firewall_address: str | None = ...,
        ssid_policy: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: NacPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        category: Literal["device", "firewall-user", "ems-tag", "fortivoice-tag", "vulnerability"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        match_type: Literal["dynamic", "override"] | None = ...,
        match_period: int | None = ...,
        match_remove: Literal["default", "link-down"] | None = ...,
        mac: str | None = ...,
        hw_vendor: str | None = ...,
        type: str | None = ...,
        family: str | None = ...,
        os: str | None = ...,
        hw_version: str | None = ...,
        sw_version: str | None = ...,
        host: str | None = ...,
        user: str | None = ...,
        src: str | None = ...,
        user_group: str | None = ...,
        ems_tag: str | None = ...,
        fortivoice_tag: str | None = ...,
        severity: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_fortilink: str | None = ...,
        switch_group: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_mac_policy: str | None = ...,
        firewall_address: str | None = ...,
        ssid_policy: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: NacPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        category: Literal["device", "firewall-user", "ems-tag", "fortivoice-tag", "vulnerability"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        match_type: Literal["dynamic", "override"] | None = ...,
        match_period: int | None = ...,
        match_remove: Literal["default", "link-down"] | None = ...,
        mac: str | None = ...,
        hw_vendor: str | None = ...,
        type: str | None = ...,
        family: str | None = ...,
        os: str | None = ...,
        hw_version: str | None = ...,
        sw_version: str | None = ...,
        host: str | None = ...,
        user: str | None = ...,
        src: str | None = ...,
        user_group: str | None = ...,
        ems_tag: str | None = ...,
        fortivoice_tag: str | None = ...,
        severity: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_fortilink: str | None = ...,
        switch_group: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_mac_policy: str | None = ...,
        firewall_address: str | None = ...,
        ssid_policy: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> NacPolicyObject: ...
    
    @overload
    def put(
        self,
        payload_dict: NacPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        category: Literal["device", "firewall-user", "ems-tag", "fortivoice-tag", "vulnerability"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        match_type: Literal["dynamic", "override"] | None = ...,
        match_period: int | None = ...,
        match_remove: Literal["default", "link-down"] | None = ...,
        mac: str | None = ...,
        hw_vendor: str | None = ...,
        type: str | None = ...,
        family: str | None = ...,
        os: str | None = ...,
        hw_version: str | None = ...,
        sw_version: str | None = ...,
        host: str | None = ...,
        user: str | None = ...,
        src: str | None = ...,
        user_group: str | None = ...,
        ems_tag: str | None = ...,
        fortivoice_tag: str | None = ...,
        severity: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_fortilink: str | None = ...,
        switch_group: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_mac_policy: str | None = ...,
        firewall_address: str | None = ...,
        ssid_policy: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: NacPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        category: Literal["device", "firewall-user", "ems-tag", "fortivoice-tag", "vulnerability"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        match_type: Literal["dynamic", "override"] | None = ...,
        match_period: int | None = ...,
        match_remove: Literal["default", "link-down"] | None = ...,
        mac: str | None = ...,
        hw_vendor: str | None = ...,
        type: str | None = ...,
        family: str | None = ...,
        os: str | None = ...,
        hw_version: str | None = ...,
        sw_version: str | None = ...,
        host: str | None = ...,
        user: str | None = ...,
        src: str | None = ...,
        user_group: str | None = ...,
        ems_tag: str | None = ...,
        fortivoice_tag: str | None = ...,
        severity: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_fortilink: str | None = ...,
        switch_group: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_mac_policy: str | None = ...,
        firewall_address: str | None = ...,
        ssid_policy: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: NacPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        category: Literal["device", "firewall-user", "ems-tag", "fortivoice-tag", "vulnerability"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        match_type: Literal["dynamic", "override"] | None = ...,
        match_period: int | None = ...,
        match_remove: Literal["default", "link-down"] | None = ...,
        mac: str | None = ...,
        hw_vendor: str | None = ...,
        type: str | None = ...,
        family: str | None = ...,
        os: str | None = ...,
        hw_version: str | None = ...,
        sw_version: str | None = ...,
        host: str | None = ...,
        user: str | None = ...,
        src: str | None = ...,
        user_group: str | None = ...,
        ems_tag: str | None = ...,
        fortivoice_tag: str | None = ...,
        severity: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_fortilink: str | None = ...,
        switch_group: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_mac_policy: str | None = ...,
        firewall_address: str | None = ...,
        ssid_policy: str | None = ...,
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
    ) -> NacPolicyObject: ...
    
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
        payload_dict: NacPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        category: Literal["device", "firewall-user", "ems-tag", "fortivoice-tag", "vulnerability"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        match_type: Literal["dynamic", "override"] | None = ...,
        match_period: int | None = ...,
        match_remove: Literal["default", "link-down"] | None = ...,
        mac: str | None = ...,
        hw_vendor: str | None = ...,
        type: str | None = ...,
        family: str | None = ...,
        os: str | None = ...,
        hw_version: str | None = ...,
        sw_version: str | None = ...,
        host: str | None = ...,
        user: str | None = ...,
        src: str | None = ...,
        user_group: str | None = ...,
        ems_tag: str | None = ...,
        fortivoice_tag: str | None = ...,
        severity: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_fortilink: str | None = ...,
        switch_group: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_mac_policy: str | None = ...,
        firewall_address: str | None = ...,
        ssid_policy: str | None = ...,
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
    "NacPolicy",
    "NacPolicyPayload",
    "NacPolicyObject",
]