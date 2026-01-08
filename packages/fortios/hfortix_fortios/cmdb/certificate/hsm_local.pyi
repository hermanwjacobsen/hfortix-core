from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class HsmLocalPayload(TypedDict, total=False):
    """
    Type hints for certificate/hsm_local payload fields.
    
    Local certificates whose keys are stored on HSM.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.cloud-service.CloudServiceEndpoint` (via: gch-cloud-service-name)

    **Usage:**
        payload: HsmLocalPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Name.
    comments: NotRequired[str]  # Comment.
    vendor: Literal["unknown", "gch"]  # HSM vendor.
    api_version: NotRequired[Literal["unknown", "gch-default"]]  # API version for communicating with HSM.
    certificate: NotRequired[str]  # PEM format certificate.
    range: NotRequired[Literal["global", "vdom"]]  # Either a global or VDOM IP address range for the certificate
    source: NotRequired[Literal["factory", "user", "bundle"]]  # Certificate source type.
    gch_url: NotRequired[str]  # Google Cloud HSM key URL (e.g. "https://cloudkms.googleapis.
    gch_project: NotRequired[str]  # Google Cloud HSM project ID.
    gch_location: NotRequired[str]  # Google Cloud HSM location.
    gch_keyring: NotRequired[str]  # Google Cloud HSM keyring.
    gch_cryptokey: NotRequired[str]  # Google Cloud HSM cryptokey.
    gch_cryptokey_version: NotRequired[str]  # Google Cloud HSM cryptokey version.
    gch_cloud_service_name: NotRequired[str]  # Cloud service config name to generate access token.
    gch_cryptokey_algorithm: NotRequired[Literal["rsa-sign-pkcs1-2048-sha256", "rsa-sign-pkcs1-3072-sha256", "rsa-sign-pkcs1-4096-sha256", "rsa-sign-pkcs1-4096-sha512", "rsa-sign-pss-2048-sha256", "rsa-sign-pss-3072-sha256", "rsa-sign-pss-4096-sha256", "rsa-sign-pss-4096-sha512", "ec-sign-p256-sha256", "ec-sign-p384-sha384", "ec-sign-secp256k1-sha256"]]  # Google Cloud HSM cryptokey algorithm.
    details: NotRequired[str]  # Print hsm-local certificate detailed information.


class HsmLocalObject(FortiObject[HsmLocalPayload]):
    """Typed FortiObject for certificate/hsm_local with IDE autocomplete support."""
    
    # Name.
    name: str
    # Comment.
    comments: str
    # HSM vendor.
    vendor: Literal["unknown", "gch"]
    # API version for communicating with HSM.
    api_version: Literal["unknown", "gch-default"]
    # PEM format certificate.
    certificate: str
    # Either a global or VDOM IP address range for the certificate.
    range: Literal["global", "vdom"]
    # Certificate source type.
    source: Literal["factory", "user", "bundle"]
    # Google Cloud HSM key URL (e.g. "https://cloudkms.googleapis.com/v1/projects/samp
    gch_url: str
    # Google Cloud HSM project ID.
    gch_project: str
    # Google Cloud HSM location.
    gch_location: str
    # Google Cloud HSM keyring.
    gch_keyring: str
    # Google Cloud HSM cryptokey.
    gch_cryptokey: str
    # Google Cloud HSM cryptokey version.
    gch_cryptokey_version: str
    # Cloud service config name to generate access token.
    gch_cloud_service_name: str
    # Google Cloud HSM cryptokey algorithm.
    gch_cryptokey_algorithm: Literal["rsa-sign-pkcs1-2048-sha256", "rsa-sign-pkcs1-3072-sha256", "rsa-sign-pkcs1-4096-sha256", "rsa-sign-pkcs1-4096-sha512", "rsa-sign-pss-2048-sha256", "rsa-sign-pss-3072-sha256", "rsa-sign-pss-4096-sha256", "rsa-sign-pss-4096-sha512", "ec-sign-p256-sha256", "ec-sign-p384-sha384", "ec-sign-secp256k1-sha256"]
    # Print hsm-local certificate detailed information.
    details: str
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> HsmLocalPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class HsmLocal:
    """
    Local certificates whose keys are stored on HSM.
    
    Path: certificate/hsm_local
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
    ) -> HsmLocalObject: ...
    
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
    ) -> list[HsmLocalObject]: ...
    
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
    ) -> HsmLocalObject | list[HsmLocalObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: HsmLocalPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        vendor: Literal["unknown", "gch"] | None = ...,
        api_version: Literal["unknown", "gch-default"] | None = ...,
        certificate: str | None = ...,
        range: Literal["global", "vdom"] | None = ...,
        source: Literal["factory", "user", "bundle"] | None = ...,
        gch_url: str | None = ...,
        gch_project: str | None = ...,
        gch_location: str | None = ...,
        gch_keyring: str | None = ...,
        gch_cryptokey: str | None = ...,
        gch_cryptokey_version: str | None = ...,
        gch_cloud_service_name: str | None = ...,
        gch_cryptokey_algorithm: Literal["rsa-sign-pkcs1-2048-sha256", "rsa-sign-pkcs1-3072-sha256", "rsa-sign-pkcs1-4096-sha256", "rsa-sign-pkcs1-4096-sha512", "rsa-sign-pss-2048-sha256", "rsa-sign-pss-3072-sha256", "rsa-sign-pss-4096-sha256", "rsa-sign-pss-4096-sha512", "ec-sign-p256-sha256", "ec-sign-p384-sha384", "ec-sign-secp256k1-sha256"] | None = ...,
        details: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> HsmLocalObject: ...
    
    @overload
    def post(
        self,
        payload_dict: HsmLocalPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        vendor: Literal["unknown", "gch"] | None = ...,
        api_version: Literal["unknown", "gch-default"] | None = ...,
        certificate: str | None = ...,
        range: Literal["global", "vdom"] | None = ...,
        source: Literal["factory", "user", "bundle"] | None = ...,
        gch_url: str | None = ...,
        gch_project: str | None = ...,
        gch_location: str | None = ...,
        gch_keyring: str | None = ...,
        gch_cryptokey: str | None = ...,
        gch_cryptokey_version: str | None = ...,
        gch_cloud_service_name: str | None = ...,
        gch_cryptokey_algorithm: Literal["rsa-sign-pkcs1-2048-sha256", "rsa-sign-pkcs1-3072-sha256", "rsa-sign-pkcs1-4096-sha256", "rsa-sign-pkcs1-4096-sha512", "rsa-sign-pss-2048-sha256", "rsa-sign-pss-3072-sha256", "rsa-sign-pss-4096-sha256", "rsa-sign-pss-4096-sha512", "ec-sign-p256-sha256", "ec-sign-p384-sha384", "ec-sign-secp256k1-sha256"] | None = ...,
        details: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: HsmLocalPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        vendor: Literal["unknown", "gch"] | None = ...,
        api_version: Literal["unknown", "gch-default"] | None = ...,
        certificate: str | None = ...,
        range: Literal["global", "vdom"] | None = ...,
        source: Literal["factory", "user", "bundle"] | None = ...,
        gch_url: str | None = ...,
        gch_project: str | None = ...,
        gch_location: str | None = ...,
        gch_keyring: str | None = ...,
        gch_cryptokey: str | None = ...,
        gch_cryptokey_version: str | None = ...,
        gch_cloud_service_name: str | None = ...,
        gch_cryptokey_algorithm: Literal["rsa-sign-pkcs1-2048-sha256", "rsa-sign-pkcs1-3072-sha256", "rsa-sign-pkcs1-4096-sha256", "rsa-sign-pkcs1-4096-sha512", "rsa-sign-pss-2048-sha256", "rsa-sign-pss-3072-sha256", "rsa-sign-pss-4096-sha256", "rsa-sign-pss-4096-sha512", "ec-sign-p256-sha256", "ec-sign-p384-sha384", "ec-sign-secp256k1-sha256"] | None = ...,
        details: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: HsmLocalPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        vendor: Literal["unknown", "gch"] | None = ...,
        api_version: Literal["unknown", "gch-default"] | None = ...,
        certificate: str | None = ...,
        range: Literal["global", "vdom"] | None = ...,
        source: Literal["factory", "user", "bundle"] | None = ...,
        gch_url: str | None = ...,
        gch_project: str | None = ...,
        gch_location: str | None = ...,
        gch_keyring: str | None = ...,
        gch_cryptokey: str | None = ...,
        gch_cryptokey_version: str | None = ...,
        gch_cloud_service_name: str | None = ...,
        gch_cryptokey_algorithm: Literal["rsa-sign-pkcs1-2048-sha256", "rsa-sign-pkcs1-3072-sha256", "rsa-sign-pkcs1-4096-sha256", "rsa-sign-pkcs1-4096-sha512", "rsa-sign-pss-2048-sha256", "rsa-sign-pss-3072-sha256", "rsa-sign-pss-4096-sha256", "rsa-sign-pss-4096-sha512", "ec-sign-p256-sha256", "ec-sign-p384-sha384", "ec-sign-secp256k1-sha256"] | None = ...,
        details: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: HsmLocalPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        vendor: Literal["unknown", "gch"] | None = ...,
        api_version: Literal["unknown", "gch-default"] | None = ...,
        certificate: str | None = ...,
        range: Literal["global", "vdom"] | None = ...,
        source: Literal["factory", "user", "bundle"] | None = ...,
        gch_url: str | None = ...,
        gch_project: str | None = ...,
        gch_location: str | None = ...,
        gch_keyring: str | None = ...,
        gch_cryptokey: str | None = ...,
        gch_cryptokey_version: str | None = ...,
        gch_cloud_service_name: str | None = ...,
        gch_cryptokey_algorithm: Literal["rsa-sign-pkcs1-2048-sha256", "rsa-sign-pkcs1-3072-sha256", "rsa-sign-pkcs1-4096-sha256", "rsa-sign-pkcs1-4096-sha512", "rsa-sign-pss-2048-sha256", "rsa-sign-pss-3072-sha256", "rsa-sign-pss-4096-sha256", "rsa-sign-pss-4096-sha512", "ec-sign-p256-sha256", "ec-sign-p384-sha384", "ec-sign-secp256k1-sha256"] | None = ...,
        details: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> HsmLocalObject: ...
    
    @overload
    def put(
        self,
        payload_dict: HsmLocalPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        vendor: Literal["unknown", "gch"] | None = ...,
        api_version: Literal["unknown", "gch-default"] | None = ...,
        certificate: str | None = ...,
        range: Literal["global", "vdom"] | None = ...,
        source: Literal["factory", "user", "bundle"] | None = ...,
        gch_url: str | None = ...,
        gch_project: str | None = ...,
        gch_location: str | None = ...,
        gch_keyring: str | None = ...,
        gch_cryptokey: str | None = ...,
        gch_cryptokey_version: str | None = ...,
        gch_cloud_service_name: str | None = ...,
        gch_cryptokey_algorithm: Literal["rsa-sign-pkcs1-2048-sha256", "rsa-sign-pkcs1-3072-sha256", "rsa-sign-pkcs1-4096-sha256", "rsa-sign-pkcs1-4096-sha512", "rsa-sign-pss-2048-sha256", "rsa-sign-pss-3072-sha256", "rsa-sign-pss-4096-sha256", "rsa-sign-pss-4096-sha512", "ec-sign-p256-sha256", "ec-sign-p384-sha384", "ec-sign-secp256k1-sha256"] | None = ...,
        details: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: HsmLocalPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        vendor: Literal["unknown", "gch"] | None = ...,
        api_version: Literal["unknown", "gch-default"] | None = ...,
        certificate: str | None = ...,
        range: Literal["global", "vdom"] | None = ...,
        source: Literal["factory", "user", "bundle"] | None = ...,
        gch_url: str | None = ...,
        gch_project: str | None = ...,
        gch_location: str | None = ...,
        gch_keyring: str | None = ...,
        gch_cryptokey: str | None = ...,
        gch_cryptokey_version: str | None = ...,
        gch_cloud_service_name: str | None = ...,
        gch_cryptokey_algorithm: Literal["rsa-sign-pkcs1-2048-sha256", "rsa-sign-pkcs1-3072-sha256", "rsa-sign-pkcs1-4096-sha256", "rsa-sign-pkcs1-4096-sha512", "rsa-sign-pss-2048-sha256", "rsa-sign-pss-3072-sha256", "rsa-sign-pss-4096-sha256", "rsa-sign-pss-4096-sha512", "ec-sign-p256-sha256", "ec-sign-p384-sha384", "ec-sign-secp256k1-sha256"] | None = ...,
        details: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: HsmLocalPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        vendor: Literal["unknown", "gch"] | None = ...,
        api_version: Literal["unknown", "gch-default"] | None = ...,
        certificate: str | None = ...,
        range: Literal["global", "vdom"] | None = ...,
        source: Literal["factory", "user", "bundle"] | None = ...,
        gch_url: str | None = ...,
        gch_project: str | None = ...,
        gch_location: str | None = ...,
        gch_keyring: str | None = ...,
        gch_cryptokey: str | None = ...,
        gch_cryptokey_version: str | None = ...,
        gch_cloud_service_name: str | None = ...,
        gch_cryptokey_algorithm: Literal["rsa-sign-pkcs1-2048-sha256", "rsa-sign-pkcs1-3072-sha256", "rsa-sign-pkcs1-4096-sha256", "rsa-sign-pkcs1-4096-sha512", "rsa-sign-pss-2048-sha256", "rsa-sign-pss-3072-sha256", "rsa-sign-pss-4096-sha256", "rsa-sign-pss-4096-sha512", "ec-sign-p256-sha256", "ec-sign-p384-sha384", "ec-sign-secp256k1-sha256"] | None = ...,
        details: str | None = ...,
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
    ) -> HsmLocalObject: ...
    
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
        payload_dict: HsmLocalPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        vendor: Literal["unknown", "gch"] | None = ...,
        api_version: Literal["unknown", "gch-default"] | None = ...,
        certificate: str | None = ...,
        range: Literal["global", "vdom"] | None = ...,
        source: Literal["factory", "user", "bundle"] | None = ...,
        gch_url: str | None = ...,
        gch_project: str | None = ...,
        gch_location: str | None = ...,
        gch_keyring: str | None = ...,
        gch_cryptokey: str | None = ...,
        gch_cryptokey_version: str | None = ...,
        gch_cloud_service_name: str | None = ...,
        gch_cryptokey_algorithm: Literal["rsa-sign-pkcs1-2048-sha256", "rsa-sign-pkcs1-3072-sha256", "rsa-sign-pkcs1-4096-sha256", "rsa-sign-pkcs1-4096-sha512", "rsa-sign-pss-2048-sha256", "rsa-sign-pss-3072-sha256", "rsa-sign-pss-4096-sha256", "rsa-sign-pss-4096-sha512", "ec-sign-p256-sha256", "ec-sign-p384-sha384", "ec-sign-secp256k1-sha256"] | None = ...,
        details: str | None = ...,
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
    "HsmLocal",
    "HsmLocalPayload",
    "HsmLocalObject",
]