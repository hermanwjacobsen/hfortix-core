from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class ProfilePayload(TypedDict, total=False):
    """
    Type hints for voip/profile payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: ProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Profile name.
    feature_set: NotRequired[Literal[{"description": "IPS Engine feature set for ips-voip-filter", "help": "IPS Engine feature set for ips-voip-filter.", "label": "Ips", "name": "ips"}, {"description": "SIP ALG feature set for voip-profile", "help": "SIP ALG feature set for voip-profile.", "label": "Voipd", "name": "voipd"}]]  # IPS or voipd (SIP-ALG) inspection feature set.
    comment: NotRequired[str]  # Comment.
    sip: NotRequired[str]  # SIP.
    sccp: NotRequired[str]  # SCCP.
    msrp: NotRequired[str]  # MSRP.


class Profile:
    """
    Configure VoIP profiles.
    
    Path: voip/profile
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
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        feature_set: Literal[{"description": "IPS Engine feature set for ips-voip-filter", "help": "IPS Engine feature set for ips-voip-filter.", "label": "Ips", "name": "ips"}, {"description": "SIP ALG feature set for voip-profile", "help": "SIP ALG feature set for voip-profile.", "label": "Voipd", "name": "voipd"}] | None = ...,
        comment: str | None = ...,
        sip: str | None = ...,
        sccp: str | None = ...,
        msrp: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        feature_set: Literal[{"description": "IPS Engine feature set for ips-voip-filter", "help": "IPS Engine feature set for ips-voip-filter.", "label": "Ips", "name": "ips"}, {"description": "SIP ALG feature set for voip-profile", "help": "SIP ALG feature set for voip-profile.", "label": "Voipd", "name": "voipd"}] | None = ...,
        comment: str | None = ...,
        sip: str | None = ...,
        sccp: str | None = ...,
        msrp: str | None = ...,
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
        payload_dict: ProfilePayload | None = ...,
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
    "Profile",
    "ProfilePayload",
]