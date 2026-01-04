from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class SshHostKeyPayload(TypedDict, total=False):
    """
    Type hints for firewall/ssh_host_key payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: SshHostKeyPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # SSH public key name.
    status: NotRequired[Literal["trusted", "revoked"]]  # Set the trust status of the public key.
    type: NotRequired[Literal["RSA", "DSA", "ECDSA", "ED25519", "RSA-CA", "DSA-CA", "ECDSA-CA", "ED25519-CA"]]  # Set the type of the public key.
    nid: NotRequired[Literal["256", "384", "521"]]  # Set the nid of the ECDSA key.
    usage: NotRequired[Literal["transparent-proxy", "access-proxy"]]  # Usage for this public key.
    ip: NotRequired[str]  # IP address of the SSH server.
    port: NotRequired[int]  # Port of the SSH server.
    hostname: NotRequired[str]  # Hostname of the SSH server to match SSH certificate principa
    public_key: NotRequired[str]  # SSH public key.


class SshHostKey:
    """
    SSH proxy host public keys.
    
    Path: firewall/ssh_host_key
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
        payload_dict: SshHostKeyPayload | None = ...,
        name: str | None = ...,
        status: Literal["trusted", "revoked"] | None = ...,
        type: Literal["RSA", "DSA", "ECDSA", "ED25519", "RSA-CA", "DSA-CA", "ECDSA-CA", "ED25519-CA"] | None = ...,
        nid: Literal["256", "384", "521"] | None = ...,
        usage: Literal["transparent-proxy", "access-proxy"] | None = ...,
        ip: str | None = ...,
        port: int | None = ...,
        hostname: str | None = ...,
        public_key: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: SshHostKeyPayload | None = ...,
        name: str | None = ...,
        status: Literal["trusted", "revoked"] | None = ...,
        type: Literal["RSA", "DSA", "ECDSA", "ED25519", "RSA-CA", "DSA-CA", "ECDSA-CA", "ED25519-CA"] | None = ...,
        nid: Literal["256", "384", "521"] | None = ...,
        usage: Literal["transparent-proxy", "access-proxy"] | None = ...,
        ip: str | None = ...,
        port: int | None = ...,
        hostname: str | None = ...,
        public_key: str | None = ...,
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
        payload_dict: SshHostKeyPayload | None = ...,
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