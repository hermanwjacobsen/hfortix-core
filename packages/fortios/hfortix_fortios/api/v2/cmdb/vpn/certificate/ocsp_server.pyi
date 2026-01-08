from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class OcspServerPayload(TypedDict, total=False):
    """
    Type hints for vpn/certificate/ocsp_server payload fields.
    
    OCSP server configuration.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.vpn.certificate.ca.CaEndpoint` (via: cert, secondary-cert)
        - :class:`~.vpn.certificate.remote.RemoteEndpoint` (via: cert, secondary-cert)

    **Usage:**
        payload: OcspServerPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # OCSP server entry name.
    url: NotRequired[str]  # OCSP server URL.
    cert: NotRequired[str]  # OCSP server certificate.
    secondary_url: NotRequired[str]  # Secondary OCSP server URL.
    secondary_cert: NotRequired[str]  # Secondary OCSP server certificate.
    unavail_action: NotRequired[Literal["revoke", "ignore"]]  # Action when server is unavailable
    source_ip: NotRequired[str]  # Source IP address for dynamic AIA and OCSP queries.

# Nested classes for table field children


# Response TypedDict for GET returns (all fields present in API response)
class OcspServerResponse(TypedDict):
    """
    Type hints for vpn/certificate/ocsp_server API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    url: str
    cert: str
    secondary_url: str
    secondary_cert: str
    unavail_action: Literal["revoke", "ignore"]
    source_ip: str


@final
class OcspServerObject:
    """Typed FortiObject for vpn/certificate/ocsp_server with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # OCSP server entry name.
    name: str
    # OCSP server URL.
    url: str
    # OCSP server certificate.
    cert: str
    # Secondary OCSP server URL.
    secondary_url: str
    # Secondary OCSP server certificate.
    secondary_cert: str
    # Action when server is unavailable
    unavail_action: Literal["revoke", "ignore"]
    # Source IP address for dynamic AIA and OCSP queries.
    source_ip: str
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> OcspServerPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class OcspServer:
    """
    OCSP server configuration.
    
    Path: vpn/certificate/ocsp_server
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
    ) -> OcspServerObject: ...
    
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
    ) -> OcspServerObject: ...
    
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
    ) -> list[OcspServerObject]: ...
    
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
    ) -> OcspServerResponse: ...
    
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
    ) -> OcspServerResponse: ...
    
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
    ) -> list[OcspServerResponse]: ...
    
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
    ) -> OcspServerObject | list[OcspServerObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: OcspServerPayload | None = ...,
        name: str | None = ...,
        url: str | None = ...,
        cert: str | None = ...,
        secondary_url: str | None = ...,
        secondary_cert: str | None = ...,
        unavail_action: Literal["revoke", "ignore"] | None = ...,
        source_ip: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> OcspServerObject: ...
    
    @overload
    def post(
        self,
        payload_dict: OcspServerPayload | None = ...,
        name: str | None = ...,
        url: str | None = ...,
        cert: str | None = ...,
        secondary_url: str | None = ...,
        secondary_cert: str | None = ...,
        unavail_action: Literal["revoke", "ignore"] | None = ...,
        source_ip: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: OcspServerPayload | None = ...,
        name: str | None = ...,
        url: str | None = ...,
        cert: str | None = ...,
        secondary_url: str | None = ...,
        secondary_cert: str | None = ...,
        unavail_action: Literal["revoke", "ignore"] | None = ...,
        source_ip: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: OcspServerPayload | None = ...,
        name: str | None = ...,
        url: str | None = ...,
        cert: str | None = ...,
        secondary_url: str | None = ...,
        secondary_cert: str | None = ...,
        unavail_action: Literal["revoke", "ignore"] | None = ...,
        source_ip: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: OcspServerPayload | None = ...,
        name: str | None = ...,
        url: str | None = ...,
        cert: str | None = ...,
        secondary_url: str | None = ...,
        secondary_cert: str | None = ...,
        unavail_action: Literal["revoke", "ignore"] | None = ...,
        source_ip: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> OcspServerObject: ...
    
    @overload
    def put(
        self,
        payload_dict: OcspServerPayload | None = ...,
        name: str | None = ...,
        url: str | None = ...,
        cert: str | None = ...,
        secondary_url: str | None = ...,
        secondary_cert: str | None = ...,
        unavail_action: Literal["revoke", "ignore"] | None = ...,
        source_ip: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: OcspServerPayload | None = ...,
        name: str | None = ...,
        url: str | None = ...,
        cert: str | None = ...,
        secondary_url: str | None = ...,
        secondary_cert: str | None = ...,
        unavail_action: Literal["revoke", "ignore"] | None = ...,
        source_ip: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: OcspServerPayload | None = ...,
        name: str | None = ...,
        url: str | None = ...,
        cert: str | None = ...,
        secondary_url: str | None = ...,
        secondary_cert: str | None = ...,
        unavail_action: Literal["revoke", "ignore"] | None = ...,
        source_ip: str | None = ...,
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
    ) -> OcspServerObject: ...
    
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
        payload_dict: OcspServerPayload | None = ...,
        name: str | None = ...,
        url: str | None = ...,
        cert: str | None = ...,
        secondary_url: str | None = ...,
        secondary_cert: str | None = ...,
        unavail_action: Literal["revoke", "ignore"] | None = ...,
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
    "OcspServer",
    "OcspServerPayload",
    "OcspServerObject",
]