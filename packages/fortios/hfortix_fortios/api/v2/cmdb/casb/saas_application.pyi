from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class SaasApplicationPayload(TypedDict, total=False):
    """
    Type hints for casb/saas_application payload fields.
    
    Configure CASB SaaS application.
    
    **Usage:**
        payload: SaasApplicationPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # SaaS application name.
    uuid: NotRequired[str]  # Universally Unique Identifier
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable setting.
    type: NotRequired[Literal["built-in", "customized"]]  # SaaS application type.
    casb_name: NotRequired[str]  # SaaS application signature name.
    description: NotRequired[str]  # SaaS application description.
    domains: NotRequired[list[dict[str, Any]]]  # SaaS application domain list.
    output_attributes: NotRequired[list[dict[str, Any]]]  # SaaS application output attributes.
    input_attributes: NotRequired[list[dict[str, Any]]]  # SaaS application input attributes.

# Nested classes for table field children

@final
class SaasApplicationDomainsObject:
    """Typed object for domains table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Domain list separated by space.
    domain: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class SaasApplicationOutputattributesObject:
    """Typed object for output-attributes table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # CASB attribute name.
    name: str
    # CASB attribute description.
    description: str
    # CASB attribute format type.
    type: Literal["string", "string-list", "integer", "integer-list", "boolean"]
    # CASB output attribute optional.
    optional: Literal["enable", "disable"]
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class SaasApplicationInputattributesObject:
    """Typed object for input-attributes table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # CASB attribute name.
    name: str
    # CASB attribute description.
    description: str
    # CASB attribute format type.
    type: Literal["string"]
    # CASB input attribute required.
    required: Literal["enable", "disable"]
    # CASB attribute default value.
    default: Literal["string", "string-list"]
    # CASB attribute legacy input.
    fallback_input: Literal["enable", "disable"]
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class SaasApplicationResponse(TypedDict):
    """
    Type hints for casb/saas_application API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    uuid: str
    status: Literal["enable", "disable"]
    type: Literal["built-in", "customized"]
    casb_name: str
    description: str
    domains: list[dict[str, Any]]
    output_attributes: list[dict[str, Any]]
    input_attributes: list[dict[str, Any]]


@final
class SaasApplicationObject:
    """Typed FortiObject for casb/saas_application with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # SaaS application name.
    name: str
    # Universally Unique Identifier
    uuid: str
    # Enable/disable setting.
    status: Literal["enable", "disable"]
    # SaaS application type.
    type: Literal["built-in", "customized"]
    # SaaS application signature name.
    casb_name: str
    # SaaS application description.
    description: str
    # SaaS application domain list.
    domains: list[SaasApplicationDomainsObject]  # Table field - list of typed objects
    # SaaS application output attributes.
    output_attributes: list[SaasApplicationOutputattributesObject]  # Table field - list of typed objects
    # SaaS application input attributes.
    input_attributes: list[SaasApplicationInputattributesObject]  # Table field - list of typed objects
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> SaasApplicationPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class SaasApplication:
    """
    Configure CASB SaaS application.
    
    Path: casb/saas_application
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
    ) -> SaasApplicationObject: ...
    
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
    ) -> SaasApplicationObject: ...
    
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
    ) -> list[SaasApplicationObject]: ...
    
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
    ) -> SaasApplicationResponse: ...
    
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
    ) -> SaasApplicationResponse: ...
    
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
    ) -> list[SaasApplicationResponse]: ...
    
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
    ) -> SaasApplicationObject | list[SaasApplicationObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: SaasApplicationPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["built-in", "customized"] | None = ...,
        casb_name: str | None = ...,
        description: str | None = ...,
        domains: str | list[str] | list[dict[str, Any]] | None = ...,
        output_attributes: str | list[str] | list[dict[str, Any]] | None = ...,
        input_attributes: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SaasApplicationObject: ...
    
    @overload
    def post(
        self,
        payload_dict: SaasApplicationPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["built-in", "customized"] | None = ...,
        casb_name: str | None = ...,
        description: str | None = ...,
        domains: str | list[str] | list[dict[str, Any]] | None = ...,
        output_attributes: str | list[str] | list[dict[str, Any]] | None = ...,
        input_attributes: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: SaasApplicationPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["built-in", "customized"] | None = ...,
        casb_name: str | None = ...,
        description: str | None = ...,
        domains: str | list[str] | list[dict[str, Any]] | None = ...,
        output_attributes: str | list[str] | list[dict[str, Any]] | None = ...,
        input_attributes: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: SaasApplicationPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["built-in", "customized"] | None = ...,
        casb_name: str | None = ...,
        description: str | None = ...,
        domains: str | list[str] | list[dict[str, Any]] | None = ...,
        output_attributes: str | list[str] | list[dict[str, Any]] | None = ...,
        input_attributes: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: SaasApplicationPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["built-in", "customized"] | None = ...,
        casb_name: str | None = ...,
        description: str | None = ...,
        domains: str | list[str] | list[dict[str, Any]] | None = ...,
        output_attributes: str | list[str] | list[dict[str, Any]] | None = ...,
        input_attributes: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SaasApplicationObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SaasApplicationPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["built-in", "customized"] | None = ...,
        casb_name: str | None = ...,
        description: str | None = ...,
        domains: str | list[str] | list[dict[str, Any]] | None = ...,
        output_attributes: str | list[str] | list[dict[str, Any]] | None = ...,
        input_attributes: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: SaasApplicationPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["built-in", "customized"] | None = ...,
        casb_name: str | None = ...,
        description: str | None = ...,
        domains: str | list[str] | list[dict[str, Any]] | None = ...,
        output_attributes: str | list[str] | list[dict[str, Any]] | None = ...,
        input_attributes: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: SaasApplicationPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["built-in", "customized"] | None = ...,
        casb_name: str | None = ...,
        description: str | None = ...,
        domains: str | list[str] | list[dict[str, Any]] | None = ...,
        output_attributes: str | list[str] | list[dict[str, Any]] | None = ...,
        input_attributes: str | list[str] | list[dict[str, Any]] | None = ...,
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
    ) -> SaasApplicationObject: ...
    
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
        payload_dict: SaasApplicationPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["built-in", "customized"] | None = ...,
        casb_name: str | None = ...,
        description: str | None = ...,
        domains: str | list[str] | list[dict[str, Any]] | None = ...,
        output_attributes: str | list[str] | list[dict[str, Any]] | None = ...,
        input_attributes: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "SaasApplication",
    "SaasApplicationPayload",
    "SaasApplicationObject",
]