from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class ScimPayload(TypedDict, total=False):
    """
    Type hints for user/scim payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: ScimPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # SCIM client name.
    id: NotRequired[int]  # SCIM client ID.
    status: Literal["enable", "disable"]  # Enable/disable System for Cross-domain Identity Management (
    base_url: NotRequired[str]  # Server URL to receive SCIM create, read, update, delete (CRU
    auth_method: NotRequired[Literal["token", "base"]]  # TLS client authentication methods (default = bearer token).
    token_certificate: NotRequired[str]  # Certificate for token verification.
    secret: NotRequired[str]  # Secret for token verification or base authentication.
    certificate: NotRequired[str]  # Certificate for client verification during TLS handshake.
    client_identity_check: NotRequired[Literal["enable", "disable"]]  # Enable/disable client identity check.
    cascade: NotRequired[Literal["disable", "enable"]]  # Enable/disable to follow SCIM users/groups changes in IDP.


class Scim:
    """
    Configure SCIM client entries.
    
    Path: user/scim
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
        payload_dict: ScimPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        base_url: str | None = ...,
        auth_method: Literal["token", "base"] | None = ...,
        token_certificate: str | None = ...,
        secret: str | None = ...,
        certificate: str | None = ...,
        client_identity_check: Literal["enable", "disable"] | None = ...,
        cascade: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: ScimPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        base_url: str | None = ...,
        auth_method: Literal["token", "base"] | None = ...,
        token_certificate: str | None = ...,
        secret: str | None = ...,
        certificate: str | None = ...,
        client_identity_check: Literal["enable", "disable"] | None = ...,
        cascade: Literal["disable", "enable"] | None = ...,
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
        payload_dict: ScimPayload | None = ...,
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