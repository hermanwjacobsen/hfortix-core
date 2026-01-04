from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class ThreatWeightPayload(TypedDict, total=False):
    """
    Type hints for log/threat_weight payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: ThreatWeightPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable the threat weight feature.
    level: NotRequired[str]  # Score mapping for threat weight levels.
    blocked_connection: NotRequired[Literal["disable", "low", "medium", "high", "critical"]]  # Threat weight score for blocked connections.
    failed_connection: NotRequired[Literal["disable", "low", "medium", "high", "critical"]]  # Threat weight score for failed connections.
    url_block_detected: NotRequired[Literal["disable", "low", "medium", "high", "critical"]]  # Threat weight score for URL blocking.
    botnet_connection_detected: NotRequired[Literal["disable", "low", "medium", "high", "critical"]]  # Threat weight score for detected botnet connections.
    malware: NotRequired[str]  # Anti-virus malware threat weight settings.
    ips: NotRequired[str]  # IPS threat weight settings.
    web: NotRequired[list[dict[str, Any]]]  # Web filtering threat weight settings.
    geolocation: NotRequired[list[dict[str, Any]]]  # Geolocation-based threat weight settings.
    application: NotRequired[list[dict[str, Any]]]  # Application-control threat weight settings.


class ThreatWeight:
    """
    Configure threat weight settings.
    
    Path: log/threat_weight
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
        payload_dict: ThreatWeightPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        level: str | None = ...,
        blocked_connection: Literal["disable", "low", "medium", "high", "critical"] | None = ...,
        failed_connection: Literal["disable", "low", "medium", "high", "critical"] | None = ...,
        url_block_detected: Literal["disable", "low", "medium", "high", "critical"] | None = ...,
        botnet_connection_detected: Literal["disable", "low", "medium", "high", "critical"] | None = ...,
        malware: str | None = ...,
        ips: str | None = ...,
        web: list[dict[str, Any]] | None = ...,
        geolocation: list[dict[str, Any]] | None = ...,
        application: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: ThreatWeightPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        level: str | None = ...,
        blocked_connection: Literal["disable", "low", "medium", "high", "critical"] | None = ...,
        failed_connection: Literal["disable", "low", "medium", "high", "critical"] | None = ...,
        url_block_detected: Literal["disable", "low", "medium", "high", "critical"] | None = ...,
        botnet_connection_detected: Literal["disable", "low", "medium", "high", "critical"] | None = ...,
        malware: str | None = ...,
        ips: str | None = ...,
        web: list[dict[str, Any]] | None = ...,
        geolocation: list[dict[str, Any]] | None = ...,
        application: list[dict[str, Any]] | None = ...,
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
        payload_dict: ThreatWeightPayload | None = ...,
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