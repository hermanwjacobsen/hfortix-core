from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class PasswordPolicyPayload(TypedDict, total=False):
    """
    Type hints for system/password_policy payload fields.
    
    Configure password policy for locally defined administrator passwords and IPsec VPN pre-shared keys.
    
    **Usage:**
        payload: PasswordPolicyPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable setting a password policy for locally defined
    apply_to: NotRequired[Literal["admin-password", "ipsec-preshared-key"]]  # Apply password policy to administrator passwords or IPsec pr
    minimum_length: NotRequired[int]  # Minimum password length (12 - 128, default = 12).
    min_lower_case_letter: NotRequired[int]  # Minimum number of lowercase characters in password
    min_upper_case_letter: NotRequired[int]  # Minimum number of uppercase characters in password
    min_non_alphanumeric: NotRequired[int]  # Minimum number of non-alphanumeric characters in password
    min_number: NotRequired[int]  # Minimum number of numeric characters in password
    expire_status: NotRequired[Literal["enable", "disable"]]  # Enable/disable password expiration.
    expire_day: NotRequired[int]  # Number of days after which passwords expire
    reuse_password: NotRequired[Literal["enable", "disable"]]  # Enable/disable reuse of password.
    reuse_password_limit: NotRequired[int]  # Number of times passwords can be reused
    login_lockout_upon_weaker_encryption: NotRequired[Literal["enable", "disable"]]  # Enable/disable administrative user login lockout upon downgr

# Nested classes for table field children


# Response TypedDict for GET returns (all fields present in API response)
class PasswordPolicyResponse(TypedDict):
    """
    Type hints for system/password_policy API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    status: Literal["enable", "disable"]
    apply_to: Literal["admin-password", "ipsec-preshared-key"]
    minimum_length: int
    min_lower_case_letter: int
    min_upper_case_letter: int
    min_non_alphanumeric: int
    min_number: int
    expire_status: Literal["enable", "disable"]
    expire_day: int
    reuse_password: Literal["enable", "disable"]
    reuse_password_limit: int
    login_lockout_upon_weaker_encryption: Literal["enable", "disable"]


@final
class PasswordPolicyObject:
    """Typed FortiObject for system/password_policy with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Enable/disable setting a password policy for locally defined administrator passw
    status: Literal["enable", "disable"]
    # Apply password policy to administrator passwords or IPsec pre-shared keys or bot
    apply_to: Literal["admin-password", "ipsec-preshared-key"]
    # Minimum password length (12 - 128, default = 12).
    minimum_length: int
    # Minimum number of lowercase characters in password (0 - 128, default = 1).
    min_lower_case_letter: int
    # Minimum number of uppercase characters in password (0 - 128, default = 1).
    min_upper_case_letter: int
    # Minimum number of non-alphanumeric characters in password (0 - 128, default = 1)
    min_non_alphanumeric: int
    # Minimum number of numeric characters in password (0 - 128, default = 1).
    min_number: int
    # Enable/disable password expiration.
    expire_status: Literal["enable", "disable"]
    # Number of days after which passwords expire (1 - 999 days, default = 90).
    expire_day: int
    # Enable/disable reuse of password.
    reuse_password: Literal["enable", "disable"]
    # Number of times passwords can be reused
    reuse_password_limit: int
    # Enable/disable administrative user login lockout upon downgrade
    login_lockout_upon_weaker_encryption: Literal["enable", "disable"]
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> PasswordPolicyPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class PasswordPolicy:
    """
    Configure password policy for locally defined administrator passwords and IPsec VPN pre-shared keys.
    
    Path: system/password_policy
    Category: cmdb
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
    ) -> PasswordPolicyObject: ...
    
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
    ) -> PasswordPolicyObject: ...
    
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
    ) -> PasswordPolicyObject: ...
    
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
    ) -> PasswordPolicyResponse: ...
    
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
    ) -> PasswordPolicyResponse: ...
    
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
    ) -> PasswordPolicyResponse: ...
    
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
    ) -> PasswordPolicyObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: PasswordPolicyPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        apply_to: Literal["admin-password", "ipsec-preshared-key"] | list[str] | None = ...,
        minimum_length: int | None = ...,
        min_lower_case_letter: int | None = ...,
        min_upper_case_letter: int | None = ...,
        min_non_alphanumeric: int | None = ...,
        min_number: int | None = ...,
        expire_status: Literal["enable", "disable"] | None = ...,
        expire_day: int | None = ...,
        reuse_password: Literal["enable", "disable"] | None = ...,
        reuse_password_limit: int | None = ...,
        login_lockout_upon_weaker_encryption: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> PasswordPolicyObject: ...
    
    @overload
    def put(
        self,
        payload_dict: PasswordPolicyPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        apply_to: Literal["admin-password", "ipsec-preshared-key"] | list[str] | None = ...,
        minimum_length: int | None = ...,
        min_lower_case_letter: int | None = ...,
        min_upper_case_letter: int | None = ...,
        min_non_alphanumeric: int | None = ...,
        min_number: int | None = ...,
        expire_status: Literal["enable", "disable"] | None = ...,
        expire_day: int | None = ...,
        reuse_password: Literal["enable", "disable"] | None = ...,
        reuse_password_limit: int | None = ...,
        login_lockout_upon_weaker_encryption: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: PasswordPolicyPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        apply_to: Literal["admin-password", "ipsec-preshared-key"] | list[str] | None = ...,
        minimum_length: int | None = ...,
        min_lower_case_letter: int | None = ...,
        min_upper_case_letter: int | None = ...,
        min_non_alphanumeric: int | None = ...,
        min_number: int | None = ...,
        expire_status: Literal["enable", "disable"] | None = ...,
        expire_day: int | None = ...,
        reuse_password: Literal["enable", "disable"] | None = ...,
        reuse_password_limit: int | None = ...,
        login_lockout_upon_weaker_encryption: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: PasswordPolicyPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        apply_to: Literal["admin-password", "ipsec-preshared-key"] | list[str] | None = ...,
        minimum_length: int | None = ...,
        min_lower_case_letter: int | None = ...,
        min_upper_case_letter: int | None = ...,
        min_non_alphanumeric: int | None = ...,
        min_number: int | None = ...,
        expire_status: Literal["enable", "disable"] | None = ...,
        expire_day: int | None = ...,
        reuse_password: Literal["enable", "disable"] | None = ...,
        reuse_password_limit: int | None = ...,
        login_lockout_upon_weaker_encryption: Literal["enable", "disable"] | None = ...,
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
        payload_dict: PasswordPolicyPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        apply_to: Literal["admin-password", "ipsec-preshared-key"] | list[str] | None = ...,
        minimum_length: int | None = ...,
        min_lower_case_letter: int | None = ...,
        min_upper_case_letter: int | None = ...,
        min_non_alphanumeric: int | None = ...,
        min_number: int | None = ...,
        expire_status: Literal["enable", "disable"] | None = ...,
        expire_day: int | None = ...,
        reuse_password: Literal["enable", "disable"] | None = ...,
        reuse_password_limit: int | None = ...,
        login_lockout_upon_weaker_encryption: Literal["enable", "disable"] | None = ...,
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
    "PasswordPolicy",
    "PasswordPolicyPayload",
    "PasswordPolicyObject",
]