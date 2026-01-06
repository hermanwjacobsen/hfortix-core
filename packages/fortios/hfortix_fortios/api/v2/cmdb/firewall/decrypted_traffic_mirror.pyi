from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class DecryptedTrafficMirrorPayload(TypedDict, total=False):
    """
    Type hints for firewall/decrypted_traffic_mirror payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: DecryptedTrafficMirrorPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Name.
    dstmac: NotRequired[str]  # Set destination MAC address for mirrored traffic.
    traffic_type: NotRequired[Literal[{"description": "Mirror decrypted SSL traffic", "help": "Mirror decrypted SSL traffic.", "label": "Ssl", "name": "ssl"}, {"description": "Mirror decrypted SSH traffic", "help": "Mirror decrypted SSH traffic.", "label": "Ssh", "name": "ssh"}]]  # Types of decrypted traffic to be mirrored.
    traffic_source: NotRequired[Literal[{"description": "Mirror client side decrypted traffic", "help": "Mirror client side decrypted traffic.", "label": "Client", "name": "client"}, {"description": "Mirror server side decrypted traffic", "help": "Mirror server side decrypted traffic.", "label": "Server", "name": "server"}, {"description": "Mirror both client and server side decrypted traffic", "help": "Mirror both client and server side decrypted traffic.", "label": "Both", "name": "both"}]]  # Source of decrypted traffic to be mirrored.
    interface: list[dict[str, Any]]  # Decrypted traffic mirror interface.


class DecryptedTrafficMirror:
    """
    Configure decrypted traffic mirror.
    
    Path: firewall/decrypted_traffic_mirror
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
        payload_dict: DecryptedTrafficMirrorPayload | None = ...,
        name: str | None = ...,
        dstmac: str | None = ...,
        traffic_type: Literal[{"description": "Mirror decrypted SSL traffic", "help": "Mirror decrypted SSL traffic.", "label": "Ssl", "name": "ssl"}, {"description": "Mirror decrypted SSH traffic", "help": "Mirror decrypted SSH traffic.", "label": "Ssh", "name": "ssh"}] | None = ...,
        traffic_source: Literal[{"description": "Mirror client side decrypted traffic", "help": "Mirror client side decrypted traffic.", "label": "Client", "name": "client"}, {"description": "Mirror server side decrypted traffic", "help": "Mirror server side decrypted traffic.", "label": "Server", "name": "server"}, {"description": "Mirror both client and server side decrypted traffic", "help": "Mirror both client and server side decrypted traffic.", "label": "Both", "name": "both"}] | None = ...,
        interface: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: DecryptedTrafficMirrorPayload | None = ...,
        name: str | None = ...,
        dstmac: str | None = ...,
        traffic_type: Literal[{"description": "Mirror decrypted SSL traffic", "help": "Mirror decrypted SSL traffic.", "label": "Ssl", "name": "ssl"}, {"description": "Mirror decrypted SSH traffic", "help": "Mirror decrypted SSH traffic.", "label": "Ssh", "name": "ssh"}] | None = ...,
        traffic_source: Literal[{"description": "Mirror client side decrypted traffic", "help": "Mirror client side decrypted traffic.", "label": "Client", "name": "client"}, {"description": "Mirror server side decrypted traffic", "help": "Mirror server side decrypted traffic.", "label": "Server", "name": "server"}, {"description": "Mirror both client and server side decrypted traffic", "help": "Mirror both client and server side decrypted traffic.", "label": "Both", "name": "both"}] | None = ...,
        interface: list[dict[str, Any]] | None = ...,
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
        payload_dict: DecryptedTrafficMirrorPayload | None = ...,
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


__all__ = [
    "DecryptedTrafficMirror",
    "DecryptedTrafficMirrorPayload",
]