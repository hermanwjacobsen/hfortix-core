from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class GeneratePayload(TypedDict, total=False):
    """
    Type hints for vpn_certificate/csr/generate payload fields.
    
    Generate a certificate signing request (CSR) and a private key. The CSR can be retrieved / downloaded from CLI, GUI and REST API.
    
    **Usage:**
        payload: GeneratePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    certname: str  # certname
    subject: str  # subject
    keytype: str  # keytype
    keysize: str  # keysize
    curvename: str  # curvename
    orgunits: str  # orgunits
    org: str  # org
    city: str  # city
    state: str  # state
    countrycode: str  # countrycode
    email: str  # email
    subject_alt_name: str  # subject_alt_name
    password: str  # password
    scep_url: str  # scep_url
    scep_password: str  # scep_password
    scope: str  # scope

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class GenerateResponse(TypedDict):
    """
    Type hints for vpn_certificate/csr/generate API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    certname: str
    subject: str
    keytype: str
    keysize: str
    curvename: str
    orgunits: str
    org: str
    city: str
    state: str
    countrycode: str
    email: str
    subject_alt_name: str
    password: str
    scep_url: str
    scep_password: str
    scope: str


@final
class GenerateObject:
    """Typed FortiObject for vpn_certificate/csr/generate with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # certname
    certname: str
    # subject
    subject: str
    # keytype
    keytype: str
    # keysize
    keysize: str
    # curvename
    curvename: str
    # orgunits
    orgunits: str
    # org
    org: str
    # city
    city: str
    # state
    state: str
    # countrycode
    countrycode: str
    # email
    email: str
    # subject_alt_name
    subject_alt_name: str
    # password
    password: str
    # scep_url
    scep_url: str
    # scep_password
    scep_password: str
    # scope
    scope: str
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> str:
        """Get pretty-printed JSON string."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> GeneratePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Generate:
    """
    Generate a certificate signing request (CSR) and a private key. The CSR can be retrieved / downloaded from CLI, GUI and REST API.
    
    Path: vpn_certificate/csr/generate
    Category: monitor
    """
    
    # ================================================================
    # GET OVERLOADS - Always returns FortiObject
    # Pylance matches overloads top-to-bottom, so these must come first!
    # ================================================================
    
    # With mkey as positional arg -> returns FortiObject
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
    ) -> GenerateObject: ...
    
    # With mkey as keyword arg -> returns FortiObject
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
    ) -> GenerateObject: ...
    
    # Without mkey -> returns list of FortiObjects
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
    ) -> GenerateObject: ...
    
    # ================================================================
    # (removed - all GET now returns FortiObject)
    # ================================================================
    
    # With mkey as positional arg -> returns single object
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
    ) -> GenerateObject: ...
    
    # With mkey as keyword arg -> returns single object
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
    ) -> GenerateObject: ...
    
    # With no mkey -> returns list of objects
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
    ) -> GenerateObject: ...
    
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
    ) -> GenerateObject: ...
    
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
    ) -> GenerateObject: ...
    
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
    ) -> GenerateObject: ...
    
    # Fallback overload for all other cases
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
    ) -> dict[str, Any] | FortiObject: ...
    
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
    ) -> GenerateObject | dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: GeneratePayload | None = ...,
        certname: str | None = ...,
        subject: str | None = ...,
        keytype: str | None = ...,
        keysize: str | None = ...,
        curvename: str | None = ...,
        orgunits: str | None = ...,
        org: str | None = ...,
        city: str | None = ...,
        state: str | None = ...,
        countrycode: str | None = ...,
        email: str | None = ...,
        subject_alt_name: str | None = ...,
        password: str | None = ...,
        scep_url: str | None = ...,
        scep_password: str | None = ...,
        scope: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> GenerateObject: ...
    
    @overload
    def post(
        self,
        payload_dict: GeneratePayload | None = ...,
        certname: str | None = ...,
        subject: str | None = ...,
        keytype: str | None = ...,
        keysize: str | None = ...,
        curvename: str | None = ...,
        orgunits: str | None = ...,
        org: str | None = ...,
        city: str | None = ...,
        state: str | None = ...,
        countrycode: str | None = ...,
        email: str | None = ...,
        subject_alt_name: str | None = ...,
        password: str | None = ...,
        scep_url: str | None = ...,
        scep_password: str | None = ...,
        scope: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: GeneratePayload | None = ...,
        certname: str | None = ...,
        subject: str | None = ...,
        keytype: str | None = ...,
        keysize: str | None = ...,
        curvename: str | None = ...,
        orgunits: str | None = ...,
        org: str | None = ...,
        city: str | None = ...,
        state: str | None = ...,
        countrycode: str | None = ...,
        email: str | None = ...,
        subject_alt_name: str | None = ...,
        password: str | None = ...,
        scep_url: str | None = ...,
        scep_password: str | None = ...,
        scope: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: GeneratePayload | None = ...,
        certname: str | None = ...,
        subject: str | None = ...,
        keytype: str | None = ...,
        keysize: str | None = ...,
        curvename: str | None = ...,
        orgunits: str | None = ...,
        org: str | None = ...,
        city: str | None = ...,
        state: str | None = ...,
        countrycode: str | None = ...,
        email: str | None = ...,
        subject_alt_name: str | None = ...,
        password: str | None = ...,
        scep_url: str | None = ...,
        scep_password: str | None = ...,
        scope: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: GeneratePayload | None = ...,
        certname: str | None = ...,
        subject: str | None = ...,
        keytype: str | None = ...,
        keysize: str | None = ...,
        curvename: str | None = ...,
        orgunits: str | None = ...,
        org: str | None = ...,
        city: str | None = ...,
        state: str | None = ...,
        countrycode: str | None = ...,
        email: str | None = ...,
        subject_alt_name: str | None = ...,
        password: str | None = ...,
        scep_url: str | None = ...,
        scep_password: str | None = ...,
        scope: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> GenerateObject: ...
    
    @overload
    def put(
        self,
        payload_dict: GeneratePayload | None = ...,
        certname: str | None = ...,
        subject: str | None = ...,
        keytype: str | None = ...,
        keysize: str | None = ...,
        curvename: str | None = ...,
        orgunits: str | None = ...,
        org: str | None = ...,
        city: str | None = ...,
        state: str | None = ...,
        countrycode: str | None = ...,
        email: str | None = ...,
        subject_alt_name: str | None = ...,
        password: str | None = ...,
        scep_url: str | None = ...,
        scep_password: str | None = ...,
        scope: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: GeneratePayload | None = ...,
        certname: str | None = ...,
        subject: str | None = ...,
        keytype: str | None = ...,
        keysize: str | None = ...,
        curvename: str | None = ...,
        orgunits: str | None = ...,
        org: str | None = ...,
        city: str | None = ...,
        state: str | None = ...,
        countrycode: str | None = ...,
        email: str | None = ...,
        subject_alt_name: str | None = ...,
        password: str | None = ...,
        scep_url: str | None = ...,
        scep_password: str | None = ...,
        scope: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: GeneratePayload | None = ...,
        certname: str | None = ...,
        subject: str | None = ...,
        keytype: str | None = ...,
        keysize: str | None = ...,
        curvename: str | None = ...,
        orgunits: str | None = ...,
        org: str | None = ...,
        city: str | None = ...,
        state: str | None = ...,
        countrycode: str | None = ...,
        email: str | None = ...,
        subject_alt_name: str | None = ...,
        password: str | None = ...,
        scep_url: str | None = ...,
        scep_password: str | None = ...,
        scope: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: GeneratePayload | None = ...,
        certname: str | None = ...,
        subject: str | None = ...,
        keytype: str | None = ...,
        keysize: str | None = ...,
        curvename: str | None = ...,
        orgunits: str | None = ...,
        org: str | None = ...,
        city: str | None = ...,
        state: str | None = ...,
        countrycode: str | None = ...,
        email: str | None = ...,
        subject_alt_name: str | None = ...,
        password: str | None = ...,
        scep_url: str | None = ...,
        scep_password: str | None = ...,
        scope: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Helper methods
    @staticmethod
    def help(field_name: str | None = ...) -> str: ...
    
    @staticmethod
    def fields(detailed: bool = ...) -> Union[list[str], list[dict[str, Any]]]: ...
    
    @staticmethod
    def field_info(field_name: str) -> FortiObject: ...
    
    @staticmethod
    def validate_field(name: str, value: Any) -> bool: ...
    
    @staticmethod
    def required_fields() -> list[str]: ...
    
    @staticmethod
    def defaults() -> FortiObject: ...
    
    @staticmethod
    def schema() -> FortiObject: ...


# ================================================================


__all__ = [
    "Generate",
    "GeneratePayload",
    "GenerateResponse",
    "GenerateObject",
]