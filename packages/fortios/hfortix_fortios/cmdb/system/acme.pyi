from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class AcmePayload(TypedDict, total=False):
    """
    Type hints for system/acme payload fields.
    
    Configure ACME client.
    
    **Usage:**
        payload: AcmePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    interface: NotRequired[list[dict[str, Any]]]  # Interface(s) on which the ACME client will listen for challe
    use_ha_direct: NotRequired[Literal["enable", "disable"]]  # Enable the use of 'ha-mgmt' interface to connect to the ACME
    source_ip: NotRequired[str]  # Source IPv4 address used to connect to the ACME server.
    source_ip6: NotRequired[str]  # Source IPv6 address used to connect to the ACME server.
    accounts: NotRequired[list[dict[str, Any]]]  # ACME accounts list.
    acc_details: NotRequired[str]  # Print Account information and decrypted key.
    status: NotRequired[str]  # Print information about the current status of the acme clien


class AcmeObject(FortiObject[AcmePayload]):
    """Typed FortiObject for system/acme with IDE autocomplete support."""
    
    # Interface(s) on which the ACME client will listen for challenges.
    interface: list[str]  # Auto-flattened from member_table
    # Enable the use of 'ha-mgmt' interface to connect to the ACME server when 'ha-dir
    use_ha_direct: Literal["enable", "disable"]
    # Source IPv4 address used to connect to the ACME server.
    source_ip: str
    # Source IPv6 address used to connect to the ACME server.
    source_ip6: str
    # ACME accounts list.
    accounts: list[str]  # Auto-flattened from member_table
    # Print Account information and decrypted key.
    acc_details: str
    # Print information about the current status of the acme client.
    status: str
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> AcmePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Acme:
    """
    Configure ACME client.
    
    Path: system/acme
    Category: cmdb
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
    ) -> AcmeObject: ...
    
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
    ) -> AcmeObject: ...
    
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
    ) -> dict[str, Any]: ...
    
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
    ) -> AcmeObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: AcmePayload | None = ...,
        interface: str | list[str] | list[dict[str, Any]] | None = ...,
        use_ha_direct: Literal["enable", "disable"] | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        accounts: str | list[str] | list[dict[str, Any]] | None = ...,
        acc_details: str | None = ...,
        status: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> AcmeObject: ...
    
    @overload
    def put(
        self,
        payload_dict: AcmePayload | None = ...,
        interface: str | list[str] | list[dict[str, Any]] | None = ...,
        use_ha_direct: Literal["enable", "disable"] | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        accounts: str | list[str] | list[dict[str, Any]] | None = ...,
        acc_details: str | None = ...,
        status: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: AcmePayload | None = ...,
        interface: str | list[str] | list[dict[str, Any]] | None = ...,
        use_ha_direct: Literal["enable", "disable"] | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        accounts: str | list[str] | list[dict[str, Any]] | None = ...,
        acc_details: str | None = ...,
        status: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: AcmePayload | None = ...,
        interface: str | list[str] | list[dict[str, Any]] | None = ...,
        use_ha_direct: Literal["enable", "disable"] | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        accounts: str | list[str] | list[dict[str, Any]] | None = ...,
        acc_details: str | None = ...,
        status: str | None = ...,
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
        payload_dict: AcmePayload | None = ...,
        interface: str | list[str] | list[dict[str, Any]] | None = ...,
        use_ha_direct: Literal["enable", "disable"] | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        accounts: str | list[str] | list[dict[str, Any]] | None = ...,
        acc_details: str | None = ...,
        status: str | None = ...,
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
    "Acme",
    "AcmePayload",
    "AcmeObject",
]