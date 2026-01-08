from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class CloudServicePayload(TypedDict, total=False):
    """
    Type hints for system/cloud_service payload fields.
    
    Configure system cloud service.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.vdom.VdomEndpoint` (via: traffic-vdom)

    **Usage:**
        payload: CloudServicePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Name.
    vendor: NotRequired[Literal["unknown", "google-cloud-kms"]]  # Cloud service vendor.
    traffic_vdom: NotRequired[str]  # Vdom used to communicate with cloud service.
    gck_service_account: NotRequired[str]  # Service account (e.g. "account-id@sampledomain.com").
    gck_private_key: NotRequired[str]  # Service account private key in PEM format
    gck_keyid: NotRequired[str]  # Key id, also referred as "kid".
    gck_access_token_lifetime: NotRequired[int]  # Lifetime of automatically generated access tokens in minutes

# Nested classes for table field children


# Response TypedDict for GET returns (all fields present in API response)
class CloudServiceResponse(TypedDict):
    """
    Type hints for system/cloud_service API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    vendor: Literal["unknown", "google-cloud-kms"]
    traffic_vdom: str
    gck_service_account: str
    gck_private_key: str
    gck_keyid: str
    gck_access_token_lifetime: int


@final
class CloudServiceObject:
    """Typed FortiObject for system/cloud_service with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Name.
    name: str
    # Cloud service vendor.
    vendor: Literal["unknown", "google-cloud-kms"]
    # Vdom used to communicate with cloud service.
    traffic_vdom: str
    # Service account (e.g. "account-id@sampledomain.com").
    gck_service_account: str
    # Service account private key in PEM format
    gck_private_key: str
    # Key id, also referred as "kid".
    gck_keyid: str
    # Lifetime of automatically generated access tokens in minutes
    gck_access_token_lifetime: int
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> CloudServicePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class CloudService:
    """
    Configure system cloud service.
    
    Path: system/cloud_service
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
    ) -> CloudServiceObject: ...
    
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
    ) -> CloudServiceObject: ...
    
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
    ) -> list[CloudServiceObject]: ...
    
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
    ) -> CloudServiceResponse: ...
    
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
    ) -> CloudServiceResponse: ...
    
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
    ) -> list[CloudServiceResponse]: ...
    
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
    ) -> CloudServiceObject | list[CloudServiceObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: CloudServicePayload | None = ...,
        name: str | None = ...,
        vendor: Literal["unknown", "google-cloud-kms"] | None = ...,
        traffic_vdom: str | None = ...,
        gck_service_account: str | None = ...,
        gck_private_key: str | None = ...,
        gck_keyid: str | None = ...,
        gck_access_token_lifetime: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> CloudServiceObject: ...
    
    @overload
    def post(
        self,
        payload_dict: CloudServicePayload | None = ...,
        name: str | None = ...,
        vendor: Literal["unknown", "google-cloud-kms"] | None = ...,
        traffic_vdom: str | None = ...,
        gck_service_account: str | None = ...,
        gck_private_key: str | None = ...,
        gck_keyid: str | None = ...,
        gck_access_token_lifetime: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: CloudServicePayload | None = ...,
        name: str | None = ...,
        vendor: Literal["unknown", "google-cloud-kms"] | None = ...,
        traffic_vdom: str | None = ...,
        gck_service_account: str | None = ...,
        gck_private_key: str | None = ...,
        gck_keyid: str | None = ...,
        gck_access_token_lifetime: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: CloudServicePayload | None = ...,
        name: str | None = ...,
        vendor: Literal["unknown", "google-cloud-kms"] | None = ...,
        traffic_vdom: str | None = ...,
        gck_service_account: str | None = ...,
        gck_private_key: str | None = ...,
        gck_keyid: str | None = ...,
        gck_access_token_lifetime: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: CloudServicePayload | None = ...,
        name: str | None = ...,
        vendor: Literal["unknown", "google-cloud-kms"] | None = ...,
        traffic_vdom: str | None = ...,
        gck_service_account: str | None = ...,
        gck_private_key: str | None = ...,
        gck_keyid: str | None = ...,
        gck_access_token_lifetime: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> CloudServiceObject: ...
    
    @overload
    def put(
        self,
        payload_dict: CloudServicePayload | None = ...,
        name: str | None = ...,
        vendor: Literal["unknown", "google-cloud-kms"] | None = ...,
        traffic_vdom: str | None = ...,
        gck_service_account: str | None = ...,
        gck_private_key: str | None = ...,
        gck_keyid: str | None = ...,
        gck_access_token_lifetime: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: CloudServicePayload | None = ...,
        name: str | None = ...,
        vendor: Literal["unknown", "google-cloud-kms"] | None = ...,
        traffic_vdom: str | None = ...,
        gck_service_account: str | None = ...,
        gck_private_key: str | None = ...,
        gck_keyid: str | None = ...,
        gck_access_token_lifetime: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: CloudServicePayload | None = ...,
        name: str | None = ...,
        vendor: Literal["unknown", "google-cloud-kms"] | None = ...,
        traffic_vdom: str | None = ...,
        gck_service_account: str | None = ...,
        gck_private_key: str | None = ...,
        gck_keyid: str | None = ...,
        gck_access_token_lifetime: int | None = ...,
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
    ) -> CloudServiceObject: ...
    
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
        payload_dict: CloudServicePayload | None = ...,
        name: str | None = ...,
        vendor: Literal["unknown", "google-cloud-kms"] | None = ...,
        traffic_vdom: str | None = ...,
        gck_service_account: str | None = ...,
        gck_private_key: str | None = ...,
        gck_keyid: str | None = ...,
        gck_access_token_lifetime: int | None = ...,
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
    "CloudService",
    "CloudServicePayload",
    "CloudServiceObject",
]