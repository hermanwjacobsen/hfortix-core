from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
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
    match_period: NotRequired[int]  # Number of days the matched devices will be retained (0 - alw
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


class NacPolicyObject(FortiObject[NacPolicyPayload]):
    """Typed FortiObject for user/nac_policy with IDE autocomplete support."""
    
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
    severity: list[str]  # Auto-flattened from member_table
    # FortiLink interface for which this NAC policy belongs to.
    switch_fortilink: str
    # List of managed FortiSwitch groups on which NAC policy can be applied.
    switch_group: list[str]  # Auto-flattened from member_table
    # Switch MAC policy action to be applied on the matched NAC policy.
    switch_mac_policy: str
    # Dynamic firewall address to associate MAC which match this policy.
    firewall_address: str
    # SSID policy to be applied on the matched NAC policy.
    ssid_policy: str
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> NacPolicyPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class NacPolicy:
    """
    Configure NAC policy matching pattern to identify matching NAC devices.
    
    Path: user/nac_policy
    Category: cmdb
    Primary Key: name
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey provided)
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
        *,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> NacPolicyObject: ...
    
    # List of objects (no mkey provided - most specific for list returns)
    # For singleton endpoints (no mkey), returns single object; for table endpoints, returns list
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
        response_mode: Literal["object"],
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
        raw_json: Literal[True],
        *,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Dict mode with mkey provided (single dict)
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
    ) -> dict[str, Any]: ...
    
    # Dict mode without mkey (returns dict with results array)
    @overload
    def get(
        self,
        name: None = None,
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
    ) -> dict[str, Any]: ...
    
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