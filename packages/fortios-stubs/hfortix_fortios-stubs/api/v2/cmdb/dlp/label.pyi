from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class LabelPayload(TypedDict, total=False):
    """
    Type hints for dlp/label payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: LabelPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Name of table containing the label.
    type: NotRequired[Literal[{"description": "Microsoft Purview Information Protection", "help": "Microsoft Purview Information Protection.", "label": "Mpip", "name": "mpip"}, {"help": "FortiData.", "label": "Fortidata", "name": "fortidata"}]]  # Label type.
    mpip_type: NotRequired[Literal[{"description": "Remotely fetched MPIP labels", "help": "Remotely fetched MPIP labels.", "label": "Remote", "name": "remote"}, {"description": "Locally configured MPIP labels", "help": "Locally configured MPIP labels.", "label": "Local", "name": "local"}]]  # MPIP label type.
    connector: NotRequired[str]  # Name of SDN connector.
    comment: NotRequired[str]  # Optional comments.
    entries: list[dict[str, Any]]  # DLP label entries.


class Label:
    """
    Configure labels used by DLP blocking.
    
    Path: dlp/label
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
        payload_dict: LabelPayload | None = ...,
        name: str | None = ...,
        type: Literal[{"description": "Microsoft Purview Information Protection", "help": "Microsoft Purview Information Protection.", "label": "Mpip", "name": "mpip"}, {"help": "FortiData.", "label": "Fortidata", "name": "fortidata"}] | None = ...,
        mpip_type: Literal[{"description": "Remotely fetched MPIP labels", "help": "Remotely fetched MPIP labels.", "label": "Remote", "name": "remote"}, {"description": "Locally configured MPIP labels", "help": "Locally configured MPIP labels.", "label": "Local", "name": "local"}] | None = ...,
        connector: str | None = ...,
        comment: str | None = ...,
        entries: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: LabelPayload | None = ...,
        name: str | None = ...,
        type: Literal[{"description": "Microsoft Purview Information Protection", "help": "Microsoft Purview Information Protection.", "label": "Mpip", "name": "mpip"}, {"help": "FortiData.", "label": "Fortidata", "name": "fortidata"}] | None = ...,
        mpip_type: Literal[{"description": "Remotely fetched MPIP labels", "help": "Remotely fetched MPIP labels.", "label": "Remote", "name": "remote"}, {"description": "Locally configured MPIP labels", "help": "Locally configured MPIP labels.", "label": "Local", "name": "local"}] | None = ...,
        connector: str | None = ...,
        comment: str | None = ...,
        entries: list[dict[str, Any]] | None = ...,
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
        payload_dict: LabelPayload | None = ...,
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
    "Label",
    "LabelPayload",
]