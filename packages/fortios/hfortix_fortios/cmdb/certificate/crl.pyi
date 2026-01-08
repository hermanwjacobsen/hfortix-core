from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class CrlPayload(TypedDict, total=False):
    """
    Type hints for certificate/crl payload fields.
    
    Certificate Revocation List as a PEM file.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.certificate.local.LocalEndpoint` (via: scep-cert)
        - :class:`~.system.vdom.VdomEndpoint` (via: update-vdom)

    **Usage:**
        payload: CrlPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Name.
    crl: NotRequired[str]  # Certificate Revocation List as a PEM file.
    range: NotRequired[Literal["global", "vdom"]]  # Either global or VDOM IP address range for the certificate.
    source: NotRequired[Literal["factory", "user", "bundle"]]  # Certificate source type.
    update_vdom: NotRequired[str]  # VDOM for CRL update.
    ldap_server: NotRequired[str]  # LDAP server name for CRL auto-update.
    ldap_username: NotRequired[str]  # LDAP server user name.
    ldap_password: NotRequired[str]  # LDAP server user password.
    http_url: NotRequired[str]  # HTTP server URL for CRL auto-update.
    scep_url: NotRequired[str]  # SCEP server URL for CRL auto-update.
    scep_cert: NotRequired[str]  # Local certificate for SCEP communication for CRL auto-update
    update_interval: NotRequired[int]  # Time in seconds before the FortiGate checks for an updated C
    source_ip: NotRequired[str]  # Source IP address for communications to a HTTP or SCEP CA se


class CrlObject(FortiObject[CrlPayload]):
    """Typed FortiObject for certificate/crl with IDE autocomplete support."""
    
    # Name.
    name: str
    # Certificate Revocation List as a PEM file.
    crl: str
    # Either global or VDOM IP address range for the certificate.
    range: Literal["global", "vdom"]
    # Certificate source type.
    source: Literal["factory", "user", "bundle"]
    # VDOM for CRL update.
    update_vdom: str
    # LDAP server name for CRL auto-update.
    ldap_server: str
    # LDAP server user name.
    ldap_username: str
    # LDAP server user password.
    ldap_password: str
    # HTTP server URL for CRL auto-update.
    http_url: str
    # SCEP server URL for CRL auto-update.
    scep_url: str
    # Local certificate for SCEP communication for CRL auto-update.
    scep_cert: str
    # Time in seconds before the FortiGate checks for an updated CRL. Set to 0 to upda
    update_interval: int
    # Source IP address for communications to a HTTP or SCEP CA server.
    source_ip: str
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> CrlPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Crl:
    """
    Certificate Revocation List as a PEM file.
    
    Path: certificate/crl
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
    ) -> CrlObject: ...
    
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
    ) -> list[CrlObject]: ...
    
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
    ) -> CrlObject | list[CrlObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: CrlPayload | None = ...,
        name: str | None = ...,
        crl: str | None = ...,
        range: Literal["global", "vdom"] | None = ...,
        source: Literal["factory", "user", "bundle"] | None = ...,
        update_vdom: str | None = ...,
        ldap_server: str | None = ...,
        ldap_username: str | None = ...,
        ldap_password: str | None = ...,
        http_url: str | None = ...,
        scep_url: str | None = ...,
        scep_cert: str | None = ...,
        update_interval: int | None = ...,
        source_ip: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> CrlObject: ...
    
    @overload
    def put(
        self,
        payload_dict: CrlPayload | None = ...,
        name: str | None = ...,
        crl: str | None = ...,
        range: Literal["global", "vdom"] | None = ...,
        source: Literal["factory", "user", "bundle"] | None = ...,
        update_vdom: str | None = ...,
        ldap_server: str | None = ...,
        ldap_username: str | None = ...,
        ldap_password: str | None = ...,
        http_url: str | None = ...,
        scep_url: str | None = ...,
        scep_cert: str | None = ...,
        update_interval: int | None = ...,
        source_ip: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: CrlPayload | None = ...,
        name: str | None = ...,
        crl: str | None = ...,
        range: Literal["global", "vdom"] | None = ...,
        source: Literal["factory", "user", "bundle"] | None = ...,
        update_vdom: str | None = ...,
        ldap_server: str | None = ...,
        ldap_username: str | None = ...,
        ldap_password: str | None = ...,
        http_url: str | None = ...,
        scep_url: str | None = ...,
        scep_cert: str | None = ...,
        update_interval: int | None = ...,
        source_ip: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: CrlPayload | None = ...,
        name: str | None = ...,
        crl: str | None = ...,
        range: Literal["global", "vdom"] | None = ...,
        source: Literal["factory", "user", "bundle"] | None = ...,
        update_vdom: str | None = ...,
        ldap_server: str | None = ...,
        ldap_username: str | None = ...,
        ldap_password: str | None = ...,
        http_url: str | None = ...,
        scep_url: str | None = ...,
        scep_cert: str | None = ...,
        update_interval: int | None = ...,
        source_ip: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: CrlPayload | None = ...,
        name: str | None = ...,
        crl: str | None = ...,
        range: Literal["global", "vdom"] | None = ...,
        source: Literal["factory", "user", "bundle"] | None = ...,
        update_vdom: str | None = ...,
        ldap_server: str | None = ...,
        ldap_username: str | None = ...,
        ldap_password: str | None = ...,
        http_url: str | None = ...,
        scep_url: str | None = ...,
        scep_cert: str | None = ...,
        update_interval: int | None = ...,
        source_ip: str | None = ...,
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
    "Crl",
    "CrlPayload",
    "CrlObject",
]