from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class PasswordPolicyPayload(TypedDict, total=False):
    """
    Type hints for user/password_policy payload fields.
    
    Configure user password policy.
    
    **Usage:**
        payload: PasswordPolicyPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Password policy name.
    expire_status: NotRequired[Literal["enable", "disable"]]  # Enable/disable password expiration.
    expire_days: NotRequired[int]  # Time in days before the user's password expires.
    warn_days: NotRequired[int]  # Time in days before a password expiration warning message is
    expired_password_renewal: NotRequired[Literal["enable", "disable"]]  # Enable/disable renewal of a password that already is expired
    minimum_length: NotRequired[int]  # Minimum password length (8 - 128, default = 8).
    min_lower_case_letter: NotRequired[int]  # Minimum number of lowercase characters in password (0 - 128,
    min_upper_case_letter: NotRequired[int]  # Minimum number of uppercase characters in password (0 - 128,
    min_non_alphanumeric: NotRequired[int]  # Minimum number of non-alphanumeric characters in password (0
    min_number: NotRequired[int]  # Minimum number of numeric characters in password (0 - 128, d
    min_change_characters: NotRequired[int]  # Minimum number of unique characters in new password which do
    reuse_password: NotRequired[Literal["enable", "disable"]]  # Enable/disable reuse of password. If both reuse-password and
    reuse_password_limit: NotRequired[int]  # Number of times passwords can be reused (0 - 20, default = 0


class PasswordPolicyObject(FortiObject[PasswordPolicyPayload]):
    """Typed FortiObject for user/password_policy with IDE autocomplete support."""
    
    # Password policy name.
    name: str
    # Enable/disable password expiration.
    expire_status: Literal["enable", "disable"]
    # Time in days before the user's password expires.
    expire_days: int
    # Time in days before a password expiration warning message is displayed to the us
    warn_days: int
    # Enable/disable renewal of a password that already is expired.
    expired_password_renewal: Literal["enable", "disable"]
    # Minimum password length (8 - 128, default = 8).
    minimum_length: int
    # Minimum number of lowercase characters in password (0 - 128, default = 0).
    min_lower_case_letter: int
    # Minimum number of uppercase characters in password (0 - 128, default = 0).
    min_upper_case_letter: int
    # Minimum number of non-alphanumeric characters in password (0 - 128, default = 0)
    min_non_alphanumeric: int
    # Minimum number of numeric characters in password (0 - 128, default = 0).
    min_number: int
    # Minimum number of unique characters in new password which do not exist in old pa
    min_change_characters: int
    # Enable/disable reuse of password. If both reuse-password and min-change-characte
    reuse_password: Literal["enable", "disable"]
    # Number of times passwords can be reused (0 - 20, default = 0. If set to 0, can r
    reuse_password_limit: int
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> PasswordPolicyPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class PasswordPolicy:
    """
    Configure user password policy.
    
    Path: user/password_policy
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
    ) -> list[PasswordPolicyObject]: ...
    
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
    ) -> PasswordPolicyObject | list[PasswordPolicyObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: PasswordPolicyPayload | None = ...,
        name: str | None = ...,
        expire_status: Literal["enable", "disable"] | None = ...,
        expire_days: int | None = ...,
        warn_days: int | None = ...,
        expired_password_renewal: Literal["enable", "disable"] | None = ...,
        minimum_length: int | None = ...,
        min_lower_case_letter: int | None = ...,
        min_upper_case_letter: int | None = ...,
        min_non_alphanumeric: int | None = ...,
        min_number: int | None = ...,
        min_change_characters: int | None = ...,
        reuse_password: Literal["enable", "disable"] | None = ...,
        reuse_password_limit: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> PasswordPolicyObject: ...
    
    @overload
    def post(
        self,
        payload_dict: PasswordPolicyPayload | None = ...,
        name: str | None = ...,
        expire_status: Literal["enable", "disable"] | None = ...,
        expire_days: int | None = ...,
        warn_days: int | None = ...,
        expired_password_renewal: Literal["enable", "disable"] | None = ...,
        minimum_length: int | None = ...,
        min_lower_case_letter: int | None = ...,
        min_upper_case_letter: int | None = ...,
        min_non_alphanumeric: int | None = ...,
        min_number: int | None = ...,
        min_change_characters: int | None = ...,
        reuse_password: Literal["enable", "disable"] | None = ...,
        reuse_password_limit: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: PasswordPolicyPayload | None = ...,
        name: str | None = ...,
        expire_status: Literal["enable", "disable"] | None = ...,
        expire_days: int | None = ...,
        warn_days: int | None = ...,
        expired_password_renewal: Literal["enable", "disable"] | None = ...,
        minimum_length: int | None = ...,
        min_lower_case_letter: int | None = ...,
        min_upper_case_letter: int | None = ...,
        min_non_alphanumeric: int | None = ...,
        min_number: int | None = ...,
        min_change_characters: int | None = ...,
        reuse_password: Literal["enable", "disable"] | None = ...,
        reuse_password_limit: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: PasswordPolicyPayload | None = ...,
        name: str | None = ...,
        expire_status: Literal["enable", "disable"] | None = ...,
        expire_days: int | None = ...,
        warn_days: int | None = ...,
        expired_password_renewal: Literal["enable", "disable"] | None = ...,
        minimum_length: int | None = ...,
        min_lower_case_letter: int | None = ...,
        min_upper_case_letter: int | None = ...,
        min_non_alphanumeric: int | None = ...,
        min_number: int | None = ...,
        min_change_characters: int | None = ...,
        reuse_password: Literal["enable", "disable"] | None = ...,
        reuse_password_limit: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: PasswordPolicyPayload | None = ...,
        name: str | None = ...,
        expire_status: Literal["enable", "disable"] | None = ...,
        expire_days: int | None = ...,
        warn_days: int | None = ...,
        expired_password_renewal: Literal["enable", "disable"] | None = ...,
        minimum_length: int | None = ...,
        min_lower_case_letter: int | None = ...,
        min_upper_case_letter: int | None = ...,
        min_non_alphanumeric: int | None = ...,
        min_number: int | None = ...,
        min_change_characters: int | None = ...,
        reuse_password: Literal["enable", "disable"] | None = ...,
        reuse_password_limit: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> PasswordPolicyObject: ...
    
    @overload
    def put(
        self,
        payload_dict: PasswordPolicyPayload | None = ...,
        name: str | None = ...,
        expire_status: Literal["enable", "disable"] | None = ...,
        expire_days: int | None = ...,
        warn_days: int | None = ...,
        expired_password_renewal: Literal["enable", "disable"] | None = ...,
        minimum_length: int | None = ...,
        min_lower_case_letter: int | None = ...,
        min_upper_case_letter: int | None = ...,
        min_non_alphanumeric: int | None = ...,
        min_number: int | None = ...,
        min_change_characters: int | None = ...,
        reuse_password: Literal["enable", "disable"] | None = ...,
        reuse_password_limit: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: PasswordPolicyPayload | None = ...,
        name: str | None = ...,
        expire_status: Literal["enable", "disable"] | None = ...,
        expire_days: int | None = ...,
        warn_days: int | None = ...,
        expired_password_renewal: Literal["enable", "disable"] | None = ...,
        minimum_length: int | None = ...,
        min_lower_case_letter: int | None = ...,
        min_upper_case_letter: int | None = ...,
        min_non_alphanumeric: int | None = ...,
        min_number: int | None = ...,
        min_change_characters: int | None = ...,
        reuse_password: Literal["enable", "disable"] | None = ...,
        reuse_password_limit: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: PasswordPolicyPayload | None = ...,
        name: str | None = ...,
        expire_status: Literal["enable", "disable"] | None = ...,
        expire_days: int | None = ...,
        warn_days: int | None = ...,
        expired_password_renewal: Literal["enable", "disable"] | None = ...,
        minimum_length: int | None = ...,
        min_lower_case_letter: int | None = ...,
        min_upper_case_letter: int | None = ...,
        min_non_alphanumeric: int | None = ...,
        min_number: int | None = ...,
        min_change_characters: int | None = ...,
        reuse_password: Literal["enable", "disable"] | None = ...,
        reuse_password_limit: int | None = ...,
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
    ) -> PasswordPolicyObject: ...
    
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
        payload_dict: PasswordPolicyPayload | None = ...,
        name: str | None = ...,
        expire_status: Literal["enable", "disable"] | None = ...,
        expire_days: int | None = ...,
        warn_days: int | None = ...,
        expired_password_renewal: Literal["enable", "disable"] | None = ...,
        minimum_length: int | None = ...,
        min_lower_case_letter: int | None = ...,
        min_upper_case_letter: int | None = ...,
        min_non_alphanumeric: int | None = ...,
        min_number: int | None = ...,
        min_change_characters: int | None = ...,
        reuse_password: Literal["enable", "disable"] | None = ...,
        reuse_password_limit: int | None = ...,
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