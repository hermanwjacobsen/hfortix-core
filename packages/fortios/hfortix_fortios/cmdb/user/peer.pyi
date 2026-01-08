from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class PeerPayload(TypedDict, total=False):
    """
    Type hints for user/peer payload fields.
    
    Configure peer users.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.user.ldap.LdapEndpoint` (via: mfa-server)
        - :class:`~.user.radius.RadiusEndpoint` (via: mfa-server)
        - :class:`~.vpn.certificate.ca.CaEndpoint` (via: ca)
        - :class:`~.vpn.certificate.ocsp-server.OcspServerEndpoint` (via: ocsp-override-server)

    **Usage:**
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


class PeerObject(FortiObject[PeerPayload]):
    """Typed FortiObject for user/peer with IDE autocomplete support."""
    
    # Peer name.
    name: str
    # Determine what happens to the peer if the CA certificate is not installed. Disab
    mandatory_ca_verify: Literal["enable", "disable"]
    # Name of the CA certificate.
    ca: str
    # Peer certificate name constraints.
    subject: str
    # Peer certificate common name.
    cn: str
    # Peer certificate common name type.
    cn_type: Literal["string", "email", "FQDN", "ipv4", "ipv6"]
    # MFA mode for remote peer authentication/authorization.
    mfa_mode: Literal["none", "password", "subject-identity"]
    # Name of a remote authenticator. Performs client access right check.
    mfa_server: str
    # Unified username for remote authentication.
    mfa_username: str
    # Unified password for remote authentication. This field may be left empty when RA
    mfa_password: str
    # Online Certificate Status Protocol (OCSP) server for certificate retrieval.
    ocsp_override_server: str
    # Enable/disable two-factor authentication, applying certificate and password-base
    two_factor: Literal["enable", "disable"]
    # Peer's password used for two-factor authentication.
    passwd: str
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> PeerPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Peer:
    """
    Configure peer users.
    
    Path: user/peer
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
    ) -> PeerObject: ...
    
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
    ) -> list[PeerObject]: ...
    
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
    ) -> PeerObject | list[PeerObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> PeerObject: ...
    
    @overload
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
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
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> PeerObject: ...
    
    @overload
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
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
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
    ) -> PeerObject: ...
    
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
    "Peer",
    "PeerPayload",
    "PeerObject",
]