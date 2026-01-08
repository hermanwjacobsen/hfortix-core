from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class DomainControllerPayload(TypedDict, total=False):
    """
    Type hints for user/domain_controller payload fields.
    
    Configure domain controller entries.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface)

    **Usage:**
        payload: DomainControllerPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Domain controller entry name.
    ad_mode: NotRequired[Literal["none", "ds", "lds"]]  # Set Active Directory mode.
    hostname: str  # Hostname of the server to connect to.
    username: str  # User name to sign in with. Must have proper permissions for 
    password: str  # Password for specified username.
    ip_address: NotRequired[str]  # Domain controller IPv4 address.
    ip6: NotRequired[str]  # Domain controller IPv6 address.
    port: NotRequired[int]  # Port to be used for communication with the domain controller
    source_ip_address: NotRequired[str]  # FortiGate IPv4 address to be used for communication with the
    source_ip6: NotRequired[str]  # FortiGate IPv6 address to be used for communication with the
    source_port: NotRequired[int]  # Source port to be used for communication with the domain con
    interface_select_method: NotRequired[Literal["auto", "sdwan", "specify"]]  # Specify how to select outgoing interface to reach server.
    interface: str  # Specify outgoing interface to reach server.
    extra_server: NotRequired[list[dict[str, Any]]]  # Extra servers.
    domain_name: NotRequired[str]  # Domain DNS name.
    replication_port: NotRequired[int]  # Port to be used for communication with the domain controller
    ldap_server: NotRequired[list[dict[str, Any]]]  # LDAP server name(s).
    change_detection: NotRequired[Literal["enable", "disable"]]  # Enable/disable detection of a configuration change in the Ac
    change_detection_period: NotRequired[int]  # Minutes to detect a configuration change in the Active Direc
    dns_srv_lookup: NotRequired[Literal["enable", "disable"]]  # Enable/disable DNS service lookup.
    adlds_dn: str  # AD LDS distinguished name.
    adlds_ip_address: NotRequired[str]  # AD LDS IPv4 address.
    adlds_ip6: NotRequired[str]  # AD LDS IPv6 address.
    adlds_port: NotRequired[int]  # Port number of AD LDS service (default = 389).


class DomainControllerObject(FortiObject[DomainControllerPayload]):
    """Typed FortiObject for user/domain_controller with IDE autocomplete support."""
    
    # Domain controller entry name.
    name: str
    # Set Active Directory mode.
    ad_mode: Literal["none", "ds", "lds"]
    # Hostname of the server to connect to.
    hostname: str
    # User name to sign in with. Must have proper permissions for service.
    username: str
    # Password for specified username.
    password: str
    # Domain controller IPv4 address.
    ip_address: str
    # Domain controller IPv6 address.
    ip6: str
    # Port to be used for communication with the domain controller (default = 445).
    port: int
    # FortiGate IPv4 address to be used for communication with the domain controller.
    source_ip_address: str
    # FortiGate IPv6 address to be used for communication with the domain controller.
    source_ip6: str
    # Source port to be used for communication with the domain controller.
    source_port: int
    # Specify how to select outgoing interface to reach server.
    interface_select_method: Literal["auto", "sdwan", "specify"]
    # Specify outgoing interface to reach server.
    interface: str
    # Extra servers.
    extra_server: list[str]  # Auto-flattened from member_table
    # Domain DNS name.
    domain_name: str
    # Port to be used for communication with the domain controller for replication ser
    replication_port: int
    # LDAP server name(s).
    ldap_server: list[str]  # Auto-flattened from member_table
    # Enable/disable detection of a configuration change in the Active Directory serve
    change_detection: Literal["enable", "disable"]
    # Minutes to detect a configuration change in the Active Directory server (5 - 100
    change_detection_period: int
    # Enable/disable DNS service lookup.
    dns_srv_lookup: Literal["enable", "disable"]
    # AD LDS distinguished name.
    adlds_dn: str
    # AD LDS IPv4 address.
    adlds_ip_address: str
    # AD LDS IPv6 address.
    adlds_ip6: str
    # Port number of AD LDS service (default = 389).
    adlds_port: int
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> DomainControllerPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class DomainController:
    """
    Configure domain controller entries.
    
    Path: user/domain_controller
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
    ) -> DomainControllerObject: ...
    
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
    ) -> list[DomainControllerObject]: ...
    
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
    ) -> DomainControllerObject | list[DomainControllerObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: DomainControllerPayload | None = ...,
        name: str | None = ...,
        ad_mode: Literal["none", "ds", "lds"] | None = ...,
        hostname: str | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        ip_address: str | None = ...,
        ip6: str | None = ...,
        port: int | None = ...,
        source_ip_address: str | None = ...,
        source_ip6: str | None = ...,
        source_port: int | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        extra_server: str | list[str] | list[dict[str, Any]] | None = ...,
        domain_name: str | None = ...,
        replication_port: int | None = ...,
        ldap_server: str | list[str] | list[dict[str, Any]] | None = ...,
        change_detection: Literal["enable", "disable"] | None = ...,
        change_detection_period: int | None = ...,
        dns_srv_lookup: Literal["enable", "disable"] | None = ...,
        adlds_dn: str | None = ...,
        adlds_ip_address: str | None = ...,
        adlds_ip6: str | None = ...,
        adlds_port: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> DomainControllerObject: ...
    
    @overload
    def post(
        self,
        payload_dict: DomainControllerPayload | None = ...,
        name: str | None = ...,
        ad_mode: Literal["none", "ds", "lds"] | None = ...,
        hostname: str | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        ip_address: str | None = ...,
        ip6: str | None = ...,
        port: int | None = ...,
        source_ip_address: str | None = ...,
        source_ip6: str | None = ...,
        source_port: int | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        extra_server: str | list[str] | list[dict[str, Any]] | None = ...,
        domain_name: str | None = ...,
        replication_port: int | None = ...,
        ldap_server: str | list[str] | list[dict[str, Any]] | None = ...,
        change_detection: Literal["enable", "disable"] | None = ...,
        change_detection_period: int | None = ...,
        dns_srv_lookup: Literal["enable", "disable"] | None = ...,
        adlds_dn: str | None = ...,
        adlds_ip_address: str | None = ...,
        adlds_ip6: str | None = ...,
        adlds_port: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: DomainControllerPayload | None = ...,
        name: str | None = ...,
        ad_mode: Literal["none", "ds", "lds"] | None = ...,
        hostname: str | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        ip_address: str | None = ...,
        ip6: str | None = ...,
        port: int | None = ...,
        source_ip_address: str | None = ...,
        source_ip6: str | None = ...,
        source_port: int | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        extra_server: str | list[str] | list[dict[str, Any]] | None = ...,
        domain_name: str | None = ...,
        replication_port: int | None = ...,
        ldap_server: str | list[str] | list[dict[str, Any]] | None = ...,
        change_detection: Literal["enable", "disable"] | None = ...,
        change_detection_period: int | None = ...,
        dns_srv_lookup: Literal["enable", "disable"] | None = ...,
        adlds_dn: str | None = ...,
        adlds_ip_address: str | None = ...,
        adlds_ip6: str | None = ...,
        adlds_port: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: DomainControllerPayload | None = ...,
        name: str | None = ...,
        ad_mode: Literal["none", "ds", "lds"] | None = ...,
        hostname: str | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        ip_address: str | None = ...,
        ip6: str | None = ...,
        port: int | None = ...,
        source_ip_address: str | None = ...,
        source_ip6: str | None = ...,
        source_port: int | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        extra_server: str | list[str] | list[dict[str, Any]] | None = ...,
        domain_name: str | None = ...,
        replication_port: int | None = ...,
        ldap_server: str | list[str] | list[dict[str, Any]] | None = ...,
        change_detection: Literal["enable", "disable"] | None = ...,
        change_detection_period: int | None = ...,
        dns_srv_lookup: Literal["enable", "disable"] | None = ...,
        adlds_dn: str | None = ...,
        adlds_ip_address: str | None = ...,
        adlds_ip6: str | None = ...,
        adlds_port: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: DomainControllerPayload | None = ...,
        name: str | None = ...,
        ad_mode: Literal["none", "ds", "lds"] | None = ...,
        hostname: str | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        ip_address: str | None = ...,
        ip6: str | None = ...,
        port: int | None = ...,
        source_ip_address: str | None = ...,
        source_ip6: str | None = ...,
        source_port: int | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        extra_server: str | list[str] | list[dict[str, Any]] | None = ...,
        domain_name: str | None = ...,
        replication_port: int | None = ...,
        ldap_server: str | list[str] | list[dict[str, Any]] | None = ...,
        change_detection: Literal["enable", "disable"] | None = ...,
        change_detection_period: int | None = ...,
        dns_srv_lookup: Literal["enable", "disable"] | None = ...,
        adlds_dn: str | None = ...,
        adlds_ip_address: str | None = ...,
        adlds_ip6: str | None = ...,
        adlds_port: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> DomainControllerObject: ...
    
    @overload
    def put(
        self,
        payload_dict: DomainControllerPayload | None = ...,
        name: str | None = ...,
        ad_mode: Literal["none", "ds", "lds"] | None = ...,
        hostname: str | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        ip_address: str | None = ...,
        ip6: str | None = ...,
        port: int | None = ...,
        source_ip_address: str | None = ...,
        source_ip6: str | None = ...,
        source_port: int | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        extra_server: str | list[str] | list[dict[str, Any]] | None = ...,
        domain_name: str | None = ...,
        replication_port: int | None = ...,
        ldap_server: str | list[str] | list[dict[str, Any]] | None = ...,
        change_detection: Literal["enable", "disable"] | None = ...,
        change_detection_period: int | None = ...,
        dns_srv_lookup: Literal["enable", "disable"] | None = ...,
        adlds_dn: str | None = ...,
        adlds_ip_address: str | None = ...,
        adlds_ip6: str | None = ...,
        adlds_port: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: DomainControllerPayload | None = ...,
        name: str | None = ...,
        ad_mode: Literal["none", "ds", "lds"] | None = ...,
        hostname: str | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        ip_address: str | None = ...,
        ip6: str | None = ...,
        port: int | None = ...,
        source_ip_address: str | None = ...,
        source_ip6: str | None = ...,
        source_port: int | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        extra_server: str | list[str] | list[dict[str, Any]] | None = ...,
        domain_name: str | None = ...,
        replication_port: int | None = ...,
        ldap_server: str | list[str] | list[dict[str, Any]] | None = ...,
        change_detection: Literal["enable", "disable"] | None = ...,
        change_detection_period: int | None = ...,
        dns_srv_lookup: Literal["enable", "disable"] | None = ...,
        adlds_dn: str | None = ...,
        adlds_ip_address: str | None = ...,
        adlds_ip6: str | None = ...,
        adlds_port: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: DomainControllerPayload | None = ...,
        name: str | None = ...,
        ad_mode: Literal["none", "ds", "lds"] | None = ...,
        hostname: str | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        ip_address: str | None = ...,
        ip6: str | None = ...,
        port: int | None = ...,
        source_ip_address: str | None = ...,
        source_ip6: str | None = ...,
        source_port: int | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        extra_server: str | list[str] | list[dict[str, Any]] | None = ...,
        domain_name: str | None = ...,
        replication_port: int | None = ...,
        ldap_server: str | list[str] | list[dict[str, Any]] | None = ...,
        change_detection: Literal["enable", "disable"] | None = ...,
        change_detection_period: int | None = ...,
        dns_srv_lookup: Literal["enable", "disable"] | None = ...,
        adlds_dn: str | None = ...,
        adlds_ip_address: str | None = ...,
        adlds_ip6: str | None = ...,
        adlds_port: int | None = ...,
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
    ) -> DomainControllerObject: ...
    
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
        payload_dict: DomainControllerPayload | None = ...,
        name: str | None = ...,
        ad_mode: Literal["none", "ds", "lds"] | None = ...,
        hostname: str | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        ip_address: str | None = ...,
        ip6: str | None = ...,
        port: int | None = ...,
        source_ip_address: str | None = ...,
        source_ip6: str | None = ...,
        source_port: int | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        extra_server: str | list[str] | list[dict[str, Any]] | None = ...,
        domain_name: str | None = ...,
        replication_port: int | None = ...,
        ldap_server: str | list[str] | list[dict[str, Any]] | None = ...,
        change_detection: Literal["enable", "disable"] | None = ...,
        change_detection_period: int | None = ...,
        dns_srv_lookup: Literal["enable", "disable"] | None = ...,
        adlds_dn: str | None = ...,
        adlds_ip_address: str | None = ...,
        adlds_ip6: str | None = ...,
        adlds_port: int | None = ...,
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
    "DomainController",
    "DomainControllerPayload",
    "DomainControllerObject",
]