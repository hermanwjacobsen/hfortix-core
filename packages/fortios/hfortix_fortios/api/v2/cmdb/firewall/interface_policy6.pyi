from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class InterfacePolicy6Payload(TypedDict, total=False):
    """
    Type hints for firewall/interface_policy6 payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: InterfacePolicy6Payload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    policyid: NotRequired[int]  # Policy ID (0 - 4294967295).
    uuid: NotRequired[str]  # Universally Unique Identifier (UUID; automatically assigned 
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable this policy.
    comments: NotRequired[str]  # Comments.
    logtraffic: NotRequired[Literal["all", "utm", "disable"]]  # Logging type to be used in this policy (Options: all | utm |
    interface: str  # Monitored interface name from available interfaces.
    srcaddr6: list[dict[str, Any]]  # IPv6 address object to limit traffic monitoring to network t
    dstaddr6: list[dict[str, Any]]  # IPv6 address object to limit traffic monitoring to network t
    service6: NotRequired[list[dict[str, Any]]]  # Service name.
    application_list_status: NotRequired[Literal["enable", "disable"]]  # Enable/disable application control.
    application_list: str  # Application list name.
    ips_sensor_status: NotRequired[Literal["enable", "disable"]]  # Enable/disable IPS.
    ips_sensor: str  # IPS sensor name.
    dsri: NotRequired[Literal["enable", "disable"]]  # Enable/disable DSRI.
    av_profile_status: NotRequired[Literal["enable", "disable"]]  # Enable/disable antivirus.
    av_profile: str  # Antivirus profile.
    webfilter_profile_status: NotRequired[Literal["enable", "disable"]]  # Enable/disable web filtering.
    webfilter_profile: str  # Web filter profile.
    casb_profile_status: NotRequired[Literal["enable", "disable"]]  # Enable/disable CASB.
    casb_profile: str  # CASB profile.
    emailfilter_profile_status: NotRequired[Literal["enable", "disable"]]  # Enable/disable email filter.
    emailfilter_profile: str  # Email filter profile.
    dlp_profile_status: NotRequired[Literal["enable", "disable"]]  # Enable/disable DLP.
    dlp_profile: str  # DLP profile name.


class InterfacePolicy6:
    """
    Configure IPv6 interface policies.
    
    Path: firewall/interface_policy6
    Category: cmdb
    Primary Key: policyid
    """
    
    def get(
        self,
        policyid: int | None = ...,
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
        payload_dict: InterfacePolicy6Payload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        interface: str | None = ...,
        srcaddr6: list[dict[str, Any]] | None = ...,
        dstaddr6: list[dict[str, Any]] | None = ...,
        service6: list[dict[str, Any]] | None = ...,
        application_list_status: Literal["enable", "disable"] | None = ...,
        application_list: str | None = ...,
        ips_sensor_status: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        dsri: Literal["enable", "disable"] | None = ...,
        av_profile_status: Literal["enable", "disable"] | None = ...,
        av_profile: str | None = ...,
        webfilter_profile_status: Literal["enable", "disable"] | None = ...,
        webfilter_profile: str | None = ...,
        casb_profile_status: Literal["enable", "disable"] | None = ...,
        casb_profile: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: InterfacePolicy6Payload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        interface: str | None = ...,
        srcaddr6: list[dict[str, Any]] | None = ...,
        dstaddr6: list[dict[str, Any]] | None = ...,
        service6: list[dict[str, Any]] | None = ...,
        application_list_status: Literal["enable", "disable"] | None = ...,
        application_list: str | None = ...,
        ips_sensor_status: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        dsri: Literal["enable", "disable"] | None = ...,
        av_profile_status: Literal["enable", "disable"] | None = ...,
        av_profile: str | None = ...,
        webfilter_profile_status: Literal["enable", "disable"] | None = ...,
        webfilter_profile: str | None = ...,
        casb_profile_status: Literal["enable", "disable"] | None = ...,
        casb_profile: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def exists(
        self,
        policyid: int,
        vdom: str | bool | None = ...,
    ) -> Union[bool, Coroutine[Any, Any, bool]]: ...
    
    def set(
        self,
        payload_dict: InterfacePolicy6Payload | None = ...,
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