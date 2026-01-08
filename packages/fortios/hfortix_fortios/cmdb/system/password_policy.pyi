from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
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
    min_lower_case_letter: NotRequired[int]  # Minimum number of lowercase characters in password (0 - 128,
    min_upper_case_letter: NotRequired[int]  # Minimum number of uppercase characters in password (0 - 128,
    min_non_alphanumeric: NotRequired[int]  # Minimum number of non-alphanumeric characters in password (0
    min_number: NotRequired[int]  # Minimum number of numeric characters in password (0 - 128, d
    expire_status: NotRequired[Literal["enable", "disable"]]  # Enable/disable password expiration.
    expire_day: NotRequired[int]  # Number of days after which passwords expire (1 - 999 days, d
    reuse_password: NotRequired[Literal["enable", "disable"]]  # Enable/disable reuse of password.
    reuse_password_limit: NotRequired[int]  # Number of times passwords can be reused (0 - 20, default = 0
    login_lockout_upon_weaker_encryption: NotRequired[Literal["enable", "disable"]]  # Enable/disable administrative user login lockout upon downgr


class PasswordPolicyObject(FortiObject[PasswordPolicyPayload]):
    """Typed FortiObject for system/password_policy with IDE autocomplete support."""
    
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
    # Number of times passwords can be reused (0 - 20, default = 0. If set to 0, can r
    reuse_password_limit: int
    # Enable/disable administrative user login lockout upon downgrade (defaut = disabl
    login_lockout_upon_weaker_encryption: Literal["enable", "disable"]
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> PasswordPolicyPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class PasswordPolicy:
    """
    Configure password policy for locally defined administrator passwords and IPsec VPN pre-shared keys.
    
    Path: system/password_policy
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
    ) -> PasswordPolicyObject: ...
    
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
        apply_to: Literal["admin-password", "ipsec-preshared-key"] | list[str] | list[dict[str, Any]] | None = ...,
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
        apply_to: Literal["admin-password", "ipsec-preshared-key"] | list[str] | list[dict[str, Any]] | None = ...,
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
        apply_to: Literal["admin-password", "ipsec-preshared-key"] | list[str] | list[dict[str, Any]] | None = ...,
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
        apply_to: Literal["admin-password", "ipsec-preshared-key"] | list[str] | list[dict[str, Any]] | None = ...,
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
        apply_to: Literal["admin-password", "ipsec-preshared-key"] | list[str] | list[dict[str, Any]] | None = ...,
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