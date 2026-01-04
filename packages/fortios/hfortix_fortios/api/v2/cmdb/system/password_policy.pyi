from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class PasswordPolicyPayload(TypedDict, total=False):
    """
    Type hints for system/password_policy payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: PasswordPolicyPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable setting a password policy for locally defined
    apply_to: NotRequired[Literal["admin-password", "ipsec-preshared-key"]]  # Apply password policy to administrator passwords or IPsec pr
    minimum_length: NotRequired[int]  # Minimum password length (8 - 128, default = 8).
    min_lower_case_letter: NotRequired[int]  # Minimum number of lowercase characters in password (0 - 128,
    min_upper_case_letter: NotRequired[int]  # Minimum number of uppercase characters in password (0 - 128,
    min_non_alphanumeric: NotRequired[int]  # Minimum number of non-alphanumeric characters in password (0
    min_number: NotRequired[int]  # Minimum number of numeric characters in password (0 - 128, d
    expire_status: NotRequired[Literal["enable", "disable"]]  # Enable/disable password expiration.
    expire_day: NotRequired[int]  # Number of days after which passwords expire (1 - 999 days, d
    reuse_password: NotRequired[Literal["enable", "disable"]]  # Enable/disable reuse of password.
    reuse_password_limit: NotRequired[int]  # Number of times passwords can be reused (0 - 20, default = 0
    login_lockout_upon_weaker_encryption: NotRequired[Literal["enable", "disable"]]  # Enable/disable administrative user login lockout upon downgr


class PasswordPolicy:
    """
    Configure password policy for locally defined administrator passwords and IPsec VPN pre-shared keys.
    
    Path: system/password_policy
    Category: cmdb
    """
    
    def get(
        self,
        name: str | None = ...,
        filter: str | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def post(
        self,
        payload_dict: PasswordPolicyPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        apply_to: Literal["admin-password", "ipsec-preshared-key"] | None = ...,
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
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: PasswordPolicyPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        apply_to: Literal["admin-password", "ipsec-preshared-key"] | None = ...,
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
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> Union[bool, Coroutine[Any, Any, bool]]: ...
    
    def set(
        self,
        payload_dict: PasswordPolicyPayload | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
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