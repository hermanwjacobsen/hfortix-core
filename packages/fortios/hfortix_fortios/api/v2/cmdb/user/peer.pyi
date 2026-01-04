from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class PeerPayload(TypedDict, total=False):
    """
    Type hints for user/peer payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: PeerPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Peer name.
    mandatory_ca_verify: NotRequired[Literal["enable", "disable"]]  # Determine what happens to the peer if the CA certificate is 
    ca: NotRequired[str]  # Name of the CA certificate.
    subject: NotRequired[str]  # Peer certificate name constraints.
    cn: NotRequired[str]  # Peer certificate common name.
    cn_type: NotRequired[Literal["string", "email", "FQDN", "ipv4", "ipv6"]]  # Peer certificate common name type.
    mfa_mode: NotRequired[Literal["none", "password", "subject-identity"]]  # MFA mode for remote peer authentication/authorization.
    mfa_server: NotRequired[str]  # Name of a remote authenticator. Performs client access right
    mfa_username: NotRequired[str]  # Unified username for remote authentication.
    mfa_password: NotRequired[str]  # Unified password for remote authentication. This field may b
    ocsp_override_server: NotRequired[str]  # Online Certificate Status Protocol (OCSP) server for certifi
    two_factor: NotRequired[Literal["enable", "disable"]]  # Enable/disable two-factor authentication, applying certifica
    passwd: NotRequired[str]  # Peer's password used for two-factor authentication.


class Peer:
    """
    Configure peer users.
    
    Path: user/peer
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
        payload_dict: PeerPayload | None = ...,
        name: str | None = ...,
        mandatory_ca_verify: Literal["enable", "disable"] | None = ...,
        ca: str | None = ...,
        subject: str | None = ...,
        cn: str | None = ...,
        cn_type: Literal["string", "email", "FQDN", "ipv4", "ipv6"] | None = ...,
        mfa_mode: Literal["none", "password", "subject-identity"] | None = ...,
        mfa_server: str | None = ...,
        mfa_username: str | None = ...,
        mfa_password: str | None = ...,
        ocsp_override_server: str | None = ...,
        two_factor: Literal["enable", "disable"] | None = ...,
        passwd: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: PeerPayload | None = ...,
        name: str | None = ...,
        mandatory_ca_verify: Literal["enable", "disable"] | None = ...,
        ca: str | None = ...,
        subject: str | None = ...,
        cn: str | None = ...,
        cn_type: Literal["string", "email", "FQDN", "ipv4", "ipv6"] | None = ...,
        mfa_mode: Literal["none", "password", "subject-identity"] | None = ...,
        mfa_server: str | None = ...,
        mfa_username: str | None = ...,
        mfa_password: str | None = ...,
        ocsp_override_server: str | None = ...,
        two_factor: Literal["enable", "disable"] | None = ...,
        passwd: str | None = ...,
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
        payload_dict: PeerPayload | None = ...,
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