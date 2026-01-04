from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class NacPolicyPayload(TypedDict, total=False):
    """
    Type hints for user/nac_policy payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
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


class NacPolicy:
    """
    Configure NAC policy matching pattern to identify matching NAC devices.
    
    Path: user/nac_policy
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
        severity: list[dict[str, Any]] | None = ...,
        switch_fortilink: str | None = ...,
        switch_group: list[dict[str, Any]] | None = ...,
        switch_mac_policy: str | None = ...,
        firewall_address: str | None = ...,
        ssid_policy: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
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
        severity: list[dict[str, Any]] | None = ...,
        switch_fortilink: str | None = ...,
        switch_group: list[dict[str, Any]] | None = ...,
        switch_mac_policy: str | None = ...,
        firewall_address: str | None = ...,
        ssid_policy: str | None = ...,
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
        payload_dict: NacPolicyPayload | None = ...,
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
    "NacPolicy",
    "NacPolicyPayload",
]