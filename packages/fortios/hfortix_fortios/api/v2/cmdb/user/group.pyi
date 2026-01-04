from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class GroupPayload(TypedDict, total=False):
    """
    Type hints for user/group payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: GroupPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Group name.
    id: NotRequired[int]  # Group ID.
    group_type: NotRequired[Literal["firewall", "fsso-service", "rsso", "guest"]]  # Set the group to be for firewall authentication, FSSO, RSSO,
    authtimeout: NotRequired[int]  # Authentication timeout in minutes for this user group. 0 to 
    auth_concurrent_override: NotRequired[Literal["enable", "disable"]]  # Enable/disable overriding the global number of concurrent au
    auth_concurrent_value: NotRequired[int]  # Maximum number of concurrent authenticated connections per u
    http_digest_realm: NotRequired[str]  # Realm attribute for MD5-digest authentication.
    sso_attribute_value: NotRequired[str]  # RADIUS attribute value.
    member: NotRequired[list[dict[str, Any]]]  # Names of users, peers, LDAP severs, RADIUS servers or extern
    match: NotRequired[list[dict[str, Any]]]  # Group matches.
    user_id: NotRequired[Literal["email", "auto-generate", "specify"]]  # Guest user ID type.
    password: NotRequired[Literal["auto-generate", "specify", "disable"]]  # Guest user password type.
    user_name: NotRequired[Literal["disable", "enable"]]  # Enable/disable the guest user name entry.
    sponsor: NotRequired[Literal["optional", "mandatory", "disabled"]]  # Set the action for the sponsor guest user field.
    company: NotRequired[Literal["optional", "mandatory", "disabled"]]  # Set the action for the company guest user field.
    email: NotRequired[Literal["disable", "enable"]]  # Enable/disable the guest user email address field.
    mobile_phone: NotRequired[Literal["disable", "enable"]]  # Enable/disable the guest user mobile phone number field.
    sms_server: NotRequired[Literal["fortiguard", "custom"]]  # Send SMS through FortiGuard or other external server.
    sms_custom_server: NotRequired[str]  # SMS server.
    expire_type: NotRequired[Literal["immediately", "first-successful-login"]]  # Determine when the expiration countdown begins.
    expire: NotRequired[int]  # Time in seconds before guest user accounts expire (1 - 31536
    max_accounts: NotRequired[int]  # Maximum number of guest accounts that can be created for thi
    multiple_guest_add: NotRequired[Literal["disable", "enable"]]  # Enable/disable addition of multiple guests.
    guest: NotRequired[list[dict[str, Any]]]  # Guest User.


class Group:
    """
    Configure user groups.
    
    Path: user/group
    Category: cmdb
    Primary Key: name
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
        payload_dict: GroupPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        group_type: Literal["firewall", "fsso-service", "rsso", "guest"] | None = ...,
        authtimeout: int | None = ...,
        auth_concurrent_override: Literal["enable", "disable"] | None = ...,
        auth_concurrent_value: int | None = ...,
        http_digest_realm: str | None = ...,
        sso_attribute_value: str | None = ...,
        member: list[dict[str, Any]] | None = ...,
        match: list[dict[str, Any]] | None = ...,
        user_id: Literal["email", "auto-generate", "specify"] | None = ...,
        password: Literal["auto-generate", "specify", "disable"] | None = ...,
        user_name: Literal["disable", "enable"] | None = ...,
        sponsor: Literal["optional", "mandatory", "disabled"] | None = ...,
        company: Literal["optional", "mandatory", "disabled"] | None = ...,
        email: Literal["disable", "enable"] | None = ...,
        mobile_phone: Literal["disable", "enable"] | None = ...,
        sms_server: Literal["fortiguard", "custom"] | None = ...,
        sms_custom_server: str | None = ...,
        expire_type: Literal["immediately", "first-successful-login"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: GroupPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        group_type: Literal["firewall", "fsso-service", "rsso", "guest"] | None = ...,
        authtimeout: int | None = ...,
        auth_concurrent_override: Literal["enable", "disable"] | None = ...,
        auth_concurrent_value: int | None = ...,
        http_digest_realm: str | None = ...,
        sso_attribute_value: str | None = ...,
        member: list[dict[str, Any]] | None = ...,
        match: list[dict[str, Any]] | None = ...,
        user_id: Literal["email", "auto-generate", "specify"] | None = ...,
        password: Literal["auto-generate", "specify", "disable"] | None = ...,
        user_name: Literal["disable", "enable"] | None = ...,
        sponsor: Literal["optional", "mandatory", "disabled"] | None = ...,
        company: Literal["optional", "mandatory", "disabled"] | None = ...,
        email: Literal["disable", "enable"] | None = ...,
        mobile_phone: Literal["disable", "enable"] | None = ...,
        sms_server: Literal["fortiguard", "custom"] | None = ...,
        sms_custom_server: str | None = ...,
        expire_type: Literal["immediately", "first-successful-login"] | None = ...,
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
        payload_dict: GroupPayload | None = ...,
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