from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class AddressPayload(TypedDict, total=False):
    """
    Type hints for firewall/address payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: AddressPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Address name.
    uuid: NotRequired[str]  # Universally Unique Identifier (UUID; automatically assigned 
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
    fabric_object: NotRequired[Literal["enable", "disable"]]  # Security Fabric global object setting.


class Address:
    """
    Configure IPv4 addresses.
    
    Path: firewall/address
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
        payload_dict: AddressPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        subnet: str | None = ...,
        type: Literal["ipmask", "iprange", "fqdn", "geography", "wildcard", "dynamic", "interface-subnet", "mac", "route-tag"] | None = ...,
        route_tag: int | None = ...,
        sub_type: Literal["sdn", "clearpass-spt", "fsso", "rsso", "ems-tag", "fortivoice-tag", "fortinac-tag", "swc-tag", "device-identification", "external-resource", "obsolete"] | None = ...,
        clearpass_spt: Literal["unknown", "healthy", "quarantine", "checkup", "transient", "infected"] | None = ...,
        macaddr: list[dict[str, Any]] | None = ...,
        start_ip: str | None = ...,
        end_ip: str | None = ...,
        fqdn: str | None = ...,
        country: str | None = ...,
        wildcard_fqdn: str | None = ...,
        cache_ttl: int | None = ...,
        wildcard: str | None = ...,
        sdn: str | None = ...,
        fsso_group: list[dict[str, Any]] | None = ...,
        sso_attribute_value: list[dict[str, Any]] | None = ...,
        interface: str | None = ...,
        tenant: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
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
        macaddr: list[dict[str, Any]] | None = ...,
        start_ip: str | None = ...,
        end_ip: str | None = ...,
        fqdn: str | None = ...,
        country: str | None = ...,
        wildcard_fqdn: str | None = ...,
        cache_ttl: int | None = ...,
        wildcard: str | None = ...,
        sdn: str | None = ...,
        fsso_group: list[dict[str, Any]] | None = ...,
        sso_attribute_value: list[dict[str, Any]] | None = ...,
        interface: str | None = ...,
        tenant: str | None = ...,
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
        payload_dict: AddressPayload | None = ...,
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