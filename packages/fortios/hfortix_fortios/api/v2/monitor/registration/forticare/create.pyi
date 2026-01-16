from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class CreatePayload(TypedDict, total=False):
    """
    Type hints for registration/forticare/create payload fields.
    
    Create a new FortiCare account.
    
    **Usage:**
        payload: CreatePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    email: str  # email
    password: str  # password
    first_name: str  # first_name
    last_name: str  # last_name
    title: str  # title
    company: str  # company
    address: str  # address
    city: str  # city
    country_code: str  # country_code
    state: str  # state
    state_code: str  # state_code
    postal_code: str  # postal_code
    phone: str  # phone
    industry: str  # industry
    industry_id: str  # industry_id
    orgsize_id: str  # orgsize_id
    reseller_name: str  # reseller_name
    reseller_id: str  # reseller_id
    is_government: str  # is_government

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class CreateResponse(TypedDict):
    """
    Type hints for registration/forticare/create API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    email: str
    password: str
    first_name: str
    last_name: str
    title: str
    company: str
    address: str
    city: str
    country_code: str
    state: str
    state_code: str
    postal_code: str
    phone: str
    industry: str
    industry_id: str
    orgsize_id: str
    reseller_name: str
    reseller_id: str
    is_government: str


@final
class CreateObject:
    """Typed FortiObject for registration/forticare/create with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # email
    email: str
    # password
    password: str
    # first_name
    first_name: str
    # last_name
    last_name: str
    # title
    title: str
    # company
    company: str
    # address
    address: str
    # city
    city: str
    # country_code
    country_code: str
    # state
    state: str
    # state_code
    state_code: str
    # postal_code
    postal_code: str
    # phone
    phone: str
    # industry
    industry: str
    # industry_id
    industry_id: str
    # orgsize_id
    orgsize_id: str
    # reseller_name
    reseller_name: str
    # reseller_id
    reseller_id: str
    # is_government
    is_government: str
    
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
    def to_dict(self) -> CreatePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Create:
    """
    Create a new FortiCare account.
    
    Path: registration/forticare/create
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
    ) -> CreateObject: ...
    
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
    ) -> CreateObject: ...
    
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
    ) -> CreateObject: ...
    
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
    ) -> CreateObject: ...
    
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
    ) -> CreateObject: ...
    
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
    ) -> CreateObject: ...
    
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
    ) -> CreateObject: ...
    
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
    ) -> CreateObject: ...
    
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
    ) -> CreateObject: ...
    
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
    ) -> CreateObject | dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: CreatePayload | None = ...,
        email: str | None = ...,
        password: str | None = ...,
        first_name: str | None = ...,
        last_name: str | None = ...,
        title: str | None = ...,
        company: str | None = ...,
        address: str | None = ...,
        city: str | None = ...,
        country_code: str | None = ...,
        state: str | None = ...,
        state_code: str | None = ...,
        postal_code: str | None = ...,
        phone: str | None = ...,
        industry: str | None = ...,
        industry_id: str | None = ...,
        orgsize_id: str | None = ...,
        reseller_name: str | None = ...,
        reseller_id: str | None = ...,
        is_government: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> CreateObject: ...
    
    @overload
    def post(
        self,
        payload_dict: CreatePayload | None = ...,
        email: str | None = ...,
        password: str | None = ...,
        first_name: str | None = ...,
        last_name: str | None = ...,
        title: str | None = ...,
        company: str | None = ...,
        address: str | None = ...,
        city: str | None = ...,
        country_code: str | None = ...,
        state: str | None = ...,
        state_code: str | None = ...,
        postal_code: str | None = ...,
        phone: str | None = ...,
        industry: str | None = ...,
        industry_id: str | None = ...,
        orgsize_id: str | None = ...,
        reseller_name: str | None = ...,
        reseller_id: str | None = ...,
        is_government: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: CreatePayload | None = ...,
        email: str | None = ...,
        password: str | None = ...,
        first_name: str | None = ...,
        last_name: str | None = ...,
        title: str | None = ...,
        company: str | None = ...,
        address: str | None = ...,
        city: str | None = ...,
        country_code: str | None = ...,
        state: str | None = ...,
        state_code: str | None = ...,
        postal_code: str | None = ...,
        phone: str | None = ...,
        industry: str | None = ...,
        industry_id: str | None = ...,
        orgsize_id: str | None = ...,
        reseller_name: str | None = ...,
        reseller_id: str | None = ...,
        is_government: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: CreatePayload | None = ...,
        email: str | None = ...,
        password: str | None = ...,
        first_name: str | None = ...,
        last_name: str | None = ...,
        title: str | None = ...,
        company: str | None = ...,
        address: str | None = ...,
        city: str | None = ...,
        country_code: str | None = ...,
        state: str | None = ...,
        state_code: str | None = ...,
        postal_code: str | None = ...,
        phone: str | None = ...,
        industry: str | None = ...,
        industry_id: str | None = ...,
        orgsize_id: str | None = ...,
        reseller_name: str | None = ...,
        reseller_id: str | None = ...,
        is_government: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: CreatePayload | None = ...,
        email: str | None = ...,
        password: str | None = ...,
        first_name: str | None = ...,
        last_name: str | None = ...,
        title: str | None = ...,
        company: str | None = ...,
        address: str | None = ...,
        city: str | None = ...,
        country_code: str | None = ...,
        state: str | None = ...,
        state_code: str | None = ...,
        postal_code: str | None = ...,
        phone: str | None = ...,
        industry: str | None = ...,
        industry_id: str | None = ...,
        orgsize_id: str | None = ...,
        reseller_name: str | None = ...,
        reseller_id: str | None = ...,
        is_government: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> CreateObject: ...
    
    @overload
    def put(
        self,
        payload_dict: CreatePayload | None = ...,
        email: str | None = ...,
        password: str | None = ...,
        first_name: str | None = ...,
        last_name: str | None = ...,
        title: str | None = ...,
        company: str | None = ...,
        address: str | None = ...,
        city: str | None = ...,
        country_code: str | None = ...,
        state: str | None = ...,
        state_code: str | None = ...,
        postal_code: str | None = ...,
        phone: str | None = ...,
        industry: str | None = ...,
        industry_id: str | None = ...,
        orgsize_id: str | None = ...,
        reseller_name: str | None = ...,
        reseller_id: str | None = ...,
        is_government: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: CreatePayload | None = ...,
        email: str | None = ...,
        password: str | None = ...,
        first_name: str | None = ...,
        last_name: str | None = ...,
        title: str | None = ...,
        company: str | None = ...,
        address: str | None = ...,
        city: str | None = ...,
        country_code: str | None = ...,
        state: str | None = ...,
        state_code: str | None = ...,
        postal_code: str | None = ...,
        phone: str | None = ...,
        industry: str | None = ...,
        industry_id: str | None = ...,
        orgsize_id: str | None = ...,
        reseller_name: str | None = ...,
        reseller_id: str | None = ...,
        is_government: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: CreatePayload | None = ...,
        email: str | None = ...,
        password: str | None = ...,
        first_name: str | None = ...,
        last_name: str | None = ...,
        title: str | None = ...,
        company: str | None = ...,
        address: str | None = ...,
        city: str | None = ...,
        country_code: str | None = ...,
        state: str | None = ...,
        state_code: str | None = ...,
        postal_code: str | None = ...,
        phone: str | None = ...,
        industry: str | None = ...,
        industry_id: str | None = ...,
        orgsize_id: str | None = ...,
        reseller_name: str | None = ...,
        reseller_id: str | None = ...,
        is_government: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: CreatePayload | None = ...,
        email: str | None = ...,
        password: str | None = ...,
        first_name: str | None = ...,
        last_name: str | None = ...,
        title: str | None = ...,
        company: str | None = ...,
        address: str | None = ...,
        city: str | None = ...,
        country_code: str | None = ...,
        state: str | None = ...,
        state_code: str | None = ...,
        postal_code: str | None = ...,
        phone: str | None = ...,
        industry: str | None = ...,
        industry_id: str | None = ...,
        orgsize_id: str | None = ...,
        reseller_name: str | None = ...,
        reseller_id: str | None = ...,
        is_government: str | None = ...,
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
    "Create",
    "CreatePayload",
    "CreateResponse",
    "CreateObject",
]