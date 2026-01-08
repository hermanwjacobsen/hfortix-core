from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class LldpProfilePayload(TypedDict, total=False):
    """
    Type hints for switch_controller/lldp_profile payload fields.
    
    Configure FortiSwitch LLDP profiles.
    
    **Usage:**
        payload: LldpProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Profile name.
    med_tlvs: NotRequired[Literal["inventory-management", "network-policy", "power-management", "location-identification"]]  # Transmitted LLDP-MED TLVs (type-length-value descriptions).
    x802_1_tlvs: NotRequired[Literal["port-vlan-id"]]  # Transmitted IEEE 802.1 TLVs.
    x802_3_tlvs: NotRequired[Literal["max-frame-size", "power-negotiation"]]  # Transmitted IEEE 802.3 TLVs.
    auto_isl: NotRequired[Literal["disable", "enable"]]  # Enable/disable auto inter-switch LAG.
    auto_isl_hello_timer: NotRequired[int]  # Auto inter-switch LAG hello timer duration (1 - 30 sec, defa
    auto_isl_receive_timeout: NotRequired[int]  # Auto inter-switch LAG timeout if no response is received (3 
    auto_isl_port_group: NotRequired[int]  # Auto inter-switch LAG port group ID (0 - 9).
    auto_mclag_icl: NotRequired[Literal["disable", "enable"]]  # Enable/disable MCLAG inter chassis link.
    auto_isl_auth: NotRequired[Literal["legacy", "strict", "relax"]]  # Auto inter-switch LAG authentication mode.
    auto_isl_auth_user: NotRequired[str]  # Auto inter-switch LAG authentication user certificate.
    auto_isl_auth_identity: NotRequired[str]  # Auto inter-switch LAG authentication identity.
    auto_isl_auth_reauth: NotRequired[int]  # Auto inter-switch LAG authentication reauth period in second
    auto_isl_auth_encrypt: NotRequired[Literal["none", "mixed", "must"]]  # Auto inter-switch LAG encryption mode.
    auto_isl_auth_macsec_profile: NotRequired[str]  # Auto inter-switch LAG macsec profile for encryption.
    med_network_policy: NotRequired[list[dict[str, Any]]]  # Configuration method to edit Media Endpoint Discovery (MED) 
    med_location_service: NotRequired[list[dict[str, Any]]]  # Configuration method to edit Media Endpoint Discovery (MED) 
    custom_tlvs: NotRequired[list[dict[str, Any]]]  # Configuration method to edit custom TLV entries.


class LldpProfileObject(FortiObject[LldpProfilePayload]):
    """Typed FortiObject for switch_controller/lldp_profile with IDE autocomplete support."""
    
    # Profile name.
    name: str
    # Transmitted LLDP-MED TLVs (type-length-value descriptions).
    med_tlvs: Literal["inventory-management", "network-policy", "power-management", "location-identification"]
    # Transmitted IEEE 802.1 TLVs.
    x802_1_tlvs: Literal["port-vlan-id"]
    # Transmitted IEEE 802.3 TLVs.
    x802_3_tlvs: Literal["max-frame-size", "power-negotiation"]
    # Enable/disable auto inter-switch LAG.
    auto_isl: Literal["disable", "enable"]
    # Auto inter-switch LAG hello timer duration (1 - 30 sec, default = 3).
    auto_isl_hello_timer: int
    # Auto inter-switch LAG timeout if no response is received (3 - 90 sec, default = 
    auto_isl_receive_timeout: int
    # Auto inter-switch LAG port group ID (0 - 9).
    auto_isl_port_group: int
    # Enable/disable MCLAG inter chassis link.
    auto_mclag_icl: Literal["disable", "enable"]
    # Auto inter-switch LAG authentication mode.
    auto_isl_auth: Literal["legacy", "strict", "relax"]
    # Auto inter-switch LAG authentication user certificate.
    auto_isl_auth_user: str
    # Auto inter-switch LAG authentication identity.
    auto_isl_auth_identity: str
    # Auto inter-switch LAG authentication reauth period in seconds(10 - 3600, default
    auto_isl_auth_reauth: int
    # Auto inter-switch LAG encryption mode.
    auto_isl_auth_encrypt: Literal["none", "mixed", "must"]
    # Auto inter-switch LAG macsec profile for encryption.
    auto_isl_auth_macsec_profile: str
    # Configuration method to edit Media Endpoint Discovery (MED) network policy type-
    med_network_policy: list[str]  # Auto-flattened from member_table
    # Configuration method to edit Media Endpoint Discovery (MED) location service typ
    med_location_service: list[str]  # Auto-flattened from member_table
    # Configuration method to edit custom TLV entries.
    custom_tlvs: list[str]  # Auto-flattened from member_table
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> LldpProfilePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class LldpProfile:
    """
    Configure FortiSwitch LLDP profiles.
    
    Path: switch_controller/lldp_profile
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
    ) -> LldpProfileObject: ...
    
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
    ) -> list[LldpProfileObject]: ...
    
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
    ) -> LldpProfileObject | list[LldpProfileObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: LldpProfilePayload | None = ...,
        name: str | None = ...,
        med_tlvs: Literal["inventory-management", "network-policy", "power-management", "location-identification"] | list[str] | list[dict[str, Any]] | None = ...,
        x802_1_tlvs: Literal["port-vlan-id"] | list[str] | list[dict[str, Any]] | None = ...,
        x802_3_tlvs: Literal["max-frame-size", "power-negotiation"] | list[str] | list[dict[str, Any]] | None = ...,
        auto_isl: Literal["disable", "enable"] | None = ...,
        auto_isl_hello_timer: int | None = ...,
        auto_isl_receive_timeout: int | None = ...,
        auto_isl_port_group: int | None = ...,
        auto_mclag_icl: Literal["disable", "enable"] | None = ...,
        auto_isl_auth: Literal["legacy", "strict", "relax"] | None = ...,
        auto_isl_auth_user: str | None = ...,
        auto_isl_auth_identity: str | None = ...,
        auto_isl_auth_reauth: int | None = ...,
        auto_isl_auth_encrypt: Literal["none", "mixed", "must"] | None = ...,
        auto_isl_auth_macsec_profile: str | None = ...,
        med_network_policy: str | list[str] | list[dict[str, Any]] | None = ...,
        med_location_service: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_tlvs: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> LldpProfileObject: ...
    
    @overload
    def post(
        self,
        payload_dict: LldpProfilePayload | None = ...,
        name: str | None = ...,
        med_tlvs: Literal["inventory-management", "network-policy", "power-management", "location-identification"] | list[str] | list[dict[str, Any]] | None = ...,
        x802_1_tlvs: Literal["port-vlan-id"] | list[str] | list[dict[str, Any]] | None = ...,
        x802_3_tlvs: Literal["max-frame-size", "power-negotiation"] | list[str] | list[dict[str, Any]] | None = ...,
        auto_isl: Literal["disable", "enable"] | None = ...,
        auto_isl_hello_timer: int | None = ...,
        auto_isl_receive_timeout: int | None = ...,
        auto_isl_port_group: int | None = ...,
        auto_mclag_icl: Literal["disable", "enable"] | None = ...,
        auto_isl_auth: Literal["legacy", "strict", "relax"] | None = ...,
        auto_isl_auth_user: str | None = ...,
        auto_isl_auth_identity: str | None = ...,
        auto_isl_auth_reauth: int | None = ...,
        auto_isl_auth_encrypt: Literal["none", "mixed", "must"] | None = ...,
        auto_isl_auth_macsec_profile: str | None = ...,
        med_network_policy: str | list[str] | list[dict[str, Any]] | None = ...,
        med_location_service: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_tlvs: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: LldpProfilePayload | None = ...,
        name: str | None = ...,
        med_tlvs: Literal["inventory-management", "network-policy", "power-management", "location-identification"] | list[str] | list[dict[str, Any]] | None = ...,
        x802_1_tlvs: Literal["port-vlan-id"] | list[str] | list[dict[str, Any]] | None = ...,
        x802_3_tlvs: Literal["max-frame-size", "power-negotiation"] | list[str] | list[dict[str, Any]] | None = ...,
        auto_isl: Literal["disable", "enable"] | None = ...,
        auto_isl_hello_timer: int | None = ...,
        auto_isl_receive_timeout: int | None = ...,
        auto_isl_port_group: int | None = ...,
        auto_mclag_icl: Literal["disable", "enable"] | None = ...,
        auto_isl_auth: Literal["legacy", "strict", "relax"] | None = ...,
        auto_isl_auth_user: str | None = ...,
        auto_isl_auth_identity: str | None = ...,
        auto_isl_auth_reauth: int | None = ...,
        auto_isl_auth_encrypt: Literal["none", "mixed", "must"] | None = ...,
        auto_isl_auth_macsec_profile: str | None = ...,
        med_network_policy: str | list[str] | list[dict[str, Any]] | None = ...,
        med_location_service: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_tlvs: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: LldpProfilePayload | None = ...,
        name: str | None = ...,
        med_tlvs: Literal["inventory-management", "network-policy", "power-management", "location-identification"] | list[str] | list[dict[str, Any]] | None = ...,
        x802_1_tlvs: Literal["port-vlan-id"] | list[str] | list[dict[str, Any]] | None = ...,
        x802_3_tlvs: Literal["max-frame-size", "power-negotiation"] | list[str] | list[dict[str, Any]] | None = ...,
        auto_isl: Literal["disable", "enable"] | None = ...,
        auto_isl_hello_timer: int | None = ...,
        auto_isl_receive_timeout: int | None = ...,
        auto_isl_port_group: int | None = ...,
        auto_mclag_icl: Literal["disable", "enable"] | None = ...,
        auto_isl_auth: Literal["legacy", "strict", "relax"] | None = ...,
        auto_isl_auth_user: str | None = ...,
        auto_isl_auth_identity: str | None = ...,
        auto_isl_auth_reauth: int | None = ...,
        auto_isl_auth_encrypt: Literal["none", "mixed", "must"] | None = ...,
        auto_isl_auth_macsec_profile: str | None = ...,
        med_network_policy: str | list[str] | list[dict[str, Any]] | None = ...,
        med_location_service: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_tlvs: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: LldpProfilePayload | None = ...,
        name: str | None = ...,
        med_tlvs: Literal["inventory-management", "network-policy", "power-management", "location-identification"] | list[str] | list[dict[str, Any]] | None = ...,
        x802_1_tlvs: Literal["port-vlan-id"] | list[str] | list[dict[str, Any]] | None = ...,
        x802_3_tlvs: Literal["max-frame-size", "power-negotiation"] | list[str] | list[dict[str, Any]] | None = ...,
        auto_isl: Literal["disable", "enable"] | None = ...,
        auto_isl_hello_timer: int | None = ...,
        auto_isl_receive_timeout: int | None = ...,
        auto_isl_port_group: int | None = ...,
        auto_mclag_icl: Literal["disable", "enable"] | None = ...,
        auto_isl_auth: Literal["legacy", "strict", "relax"] | None = ...,
        auto_isl_auth_user: str | None = ...,
        auto_isl_auth_identity: str | None = ...,
        auto_isl_auth_reauth: int | None = ...,
        auto_isl_auth_encrypt: Literal["none", "mixed", "must"] | None = ...,
        auto_isl_auth_macsec_profile: str | None = ...,
        med_network_policy: str | list[str] | list[dict[str, Any]] | None = ...,
        med_location_service: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_tlvs: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> LldpProfileObject: ...
    
    @overload
    def put(
        self,
        payload_dict: LldpProfilePayload | None = ...,
        name: str | None = ...,
        med_tlvs: Literal["inventory-management", "network-policy", "power-management", "location-identification"] | list[str] | list[dict[str, Any]] | None = ...,
        x802_1_tlvs: Literal["port-vlan-id"] | list[str] | list[dict[str, Any]] | None = ...,
        x802_3_tlvs: Literal["max-frame-size", "power-negotiation"] | list[str] | list[dict[str, Any]] | None = ...,
        auto_isl: Literal["disable", "enable"] | None = ...,
        auto_isl_hello_timer: int | None = ...,
        auto_isl_receive_timeout: int | None = ...,
        auto_isl_port_group: int | None = ...,
        auto_mclag_icl: Literal["disable", "enable"] | None = ...,
        auto_isl_auth: Literal["legacy", "strict", "relax"] | None = ...,
        auto_isl_auth_user: str | None = ...,
        auto_isl_auth_identity: str | None = ...,
        auto_isl_auth_reauth: int | None = ...,
        auto_isl_auth_encrypt: Literal["none", "mixed", "must"] | None = ...,
        auto_isl_auth_macsec_profile: str | None = ...,
        med_network_policy: str | list[str] | list[dict[str, Any]] | None = ...,
        med_location_service: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_tlvs: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: LldpProfilePayload | None = ...,
        name: str | None = ...,
        med_tlvs: Literal["inventory-management", "network-policy", "power-management", "location-identification"] | list[str] | list[dict[str, Any]] | None = ...,
        x802_1_tlvs: Literal["port-vlan-id"] | list[str] | list[dict[str, Any]] | None = ...,
        x802_3_tlvs: Literal["max-frame-size", "power-negotiation"] | list[str] | list[dict[str, Any]] | None = ...,
        auto_isl: Literal["disable", "enable"] | None = ...,
        auto_isl_hello_timer: int | None = ...,
        auto_isl_receive_timeout: int | None = ...,
        auto_isl_port_group: int | None = ...,
        auto_mclag_icl: Literal["disable", "enable"] | None = ...,
        auto_isl_auth: Literal["legacy", "strict", "relax"] | None = ...,
        auto_isl_auth_user: str | None = ...,
        auto_isl_auth_identity: str | None = ...,
        auto_isl_auth_reauth: int | None = ...,
        auto_isl_auth_encrypt: Literal["none", "mixed", "must"] | None = ...,
        auto_isl_auth_macsec_profile: str | None = ...,
        med_network_policy: str | list[str] | list[dict[str, Any]] | None = ...,
        med_location_service: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_tlvs: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: LldpProfilePayload | None = ...,
        name: str | None = ...,
        med_tlvs: Literal["inventory-management", "network-policy", "power-management", "location-identification"] | list[str] | list[dict[str, Any]] | None = ...,
        x802_1_tlvs: Literal["port-vlan-id"] | list[str] | list[dict[str, Any]] | None = ...,
        x802_3_tlvs: Literal["max-frame-size", "power-negotiation"] | list[str] | list[dict[str, Any]] | None = ...,
        auto_isl: Literal["disable", "enable"] | None = ...,
        auto_isl_hello_timer: int | None = ...,
        auto_isl_receive_timeout: int | None = ...,
        auto_isl_port_group: int | None = ...,
        auto_mclag_icl: Literal["disable", "enable"] | None = ...,
        auto_isl_auth: Literal["legacy", "strict", "relax"] | None = ...,
        auto_isl_auth_user: str | None = ...,
        auto_isl_auth_identity: str | None = ...,
        auto_isl_auth_reauth: int | None = ...,
        auto_isl_auth_encrypt: Literal["none", "mixed", "must"] | None = ...,
        auto_isl_auth_macsec_profile: str | None = ...,
        med_network_policy: str | list[str] | list[dict[str, Any]] | None = ...,
        med_location_service: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_tlvs: str | list[str] | list[dict[str, Any]] | None = ...,
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
    ) -> LldpProfileObject: ...
    
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
        payload_dict: LldpProfilePayload | None = ...,
        name: str | None = ...,
        med_tlvs: Literal["inventory-management", "network-policy", "power-management", "location-identification"] | list[str] | list[dict[str, Any]] | None = ...,
        x802_1_tlvs: Literal["port-vlan-id"] | list[str] | list[dict[str, Any]] | None = ...,
        x802_3_tlvs: Literal["max-frame-size", "power-negotiation"] | list[str] | list[dict[str, Any]] | None = ...,
        auto_isl: Literal["disable", "enable"] | None = ...,
        auto_isl_hello_timer: int | None = ...,
        auto_isl_receive_timeout: int | None = ...,
        auto_isl_port_group: int | None = ...,
        auto_mclag_icl: Literal["disable", "enable"] | None = ...,
        auto_isl_auth: Literal["legacy", "strict", "relax"] | None = ...,
        auto_isl_auth_user: str | None = ...,
        auto_isl_auth_identity: str | None = ...,
        auto_isl_auth_reauth: int | None = ...,
        auto_isl_auth_encrypt: Literal["none", "mixed", "must"] | None = ...,
        auto_isl_auth_macsec_profile: str | None = ...,
        med_network_policy: str | list[str] | list[dict[str, Any]] | None = ...,
        med_location_service: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_tlvs: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "LldpProfile",
    "LldpProfilePayload",
    "LldpProfileObject",
]