from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class LldpProfilePayload(TypedDict, total=False):
    """
    Type hints for switch_controller/lldp_profile payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: LldpProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Profile name.
    med_tlvs: NotRequired[Literal["inventory-management", "network-policy", "power-management", "location-identification"]]  # Transmitted LLDP-MED TLVs (type-length-value descriptions).
    802.1_tlvs: NotRequired[Literal["port-vlan-id"]]  # Transmitted IEEE 802.1 TLVs.
    802.3_tlvs: NotRequired[Literal["max-frame-size", "power-negotiation"]]  # Transmitted IEEE 802.3 TLVs.
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


class LldpProfile:
    """
    Configure FortiSwitch LLDP profiles.
    
    Path: switch_controller/lldp_profile
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
        payload_dict: LldpProfilePayload | None = ...,
        name: str | None = ...,
        med_tlvs: Literal["inventory-management", "network-policy", "power-management", "location-identification"] | None = ...,
        802.1_tlvs: Literal["port-vlan-id"] | None = ...,
        802.3_tlvs: Literal["max-frame-size", "power-negotiation"] | None = ...,
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
        med_network_policy: list[dict[str, Any]] | None = ...,
        med_location_service: list[dict[str, Any]] | None = ...,
        custom_tlvs: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: LldpProfilePayload | None = ...,
        name: str | None = ...,
        med_tlvs: Literal["inventory-management", "network-policy", "power-management", "location-identification"] | None = ...,
        802.1_tlvs: Literal["port-vlan-id"] | None = ...,
        802.3_tlvs: Literal["max-frame-size", "power-negotiation"] | None = ...,
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
        med_network_policy: list[dict[str, Any]] | None = ...,
        med_location_service: list[dict[str, Any]] | None = ...,
        custom_tlvs: list[dict[str, Any]] | None = ...,
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
        payload_dict: LldpProfilePayload | None = ...,
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