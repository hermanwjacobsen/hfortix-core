from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class SnifferPayload(TypedDict, total=False):
    """
    Type hints for firewall/sniffer payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: SnifferPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    id: NotRequired[int]  # Sniffer ID (0 - 9999).
    uuid: NotRequired[str]  # Universally Unique Identifier (UUID; automatically assigned 
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable the active status of the sniffer.
    logtraffic: NotRequired[Literal["all", "utm", "disable"]]  # Either log all sessions, only sessions that have a security 
    ipv6: NotRequired[Literal["enable", "disable"]]  # Enable/disable sniffing IPv6 packets.
    non_ip: NotRequired[Literal["enable", "disable"]]  # Enable/disable sniffing non-IP packets.
    interface: NotRequired[str]  # Interface name that traffic sniffing will take place on.
    host: NotRequired[str]  # Hosts to filter for in sniffer traffic (Format examples: 1.1
    port: NotRequired[str]  # Ports to sniff (Format examples: 10, :20, 30:40, 50-, 100-20
    protocol: NotRequired[str]  # Integer value for the protocol type as defined by IANA (0 - 
    vlan: NotRequired[str]  # List of VLANs to sniff.
    application_list_status: NotRequired[Literal["enable", "disable"]]  # Enable/disable application control profile.
    application_list: str  # Name of an existing application list.
    ips_sensor_status: NotRequired[Literal["enable", "disable"]]  # Enable/disable IPS sensor.
    ips_sensor: str  # Name of an existing IPS sensor.
    dsri: NotRequired[Literal["enable", "disable"]]  # Enable/disable DSRI.
    av_profile_status: NotRequired[Literal["enable", "disable"]]  # Enable/disable antivirus profile.
    av_profile: str  # Name of an existing antivirus profile.
    webfilter_profile_status: NotRequired[Literal["enable", "disable"]]  # Enable/disable web filter profile.
    webfilter_profile: str  # Name of an existing web filter profile.
    emailfilter_profile_status: NotRequired[Literal["enable", "disable"]]  # Enable/disable emailfilter.
    emailfilter_profile: str  # Name of an existing email filter profile.
    dlp_profile_status: NotRequired[Literal["enable", "disable"]]  # Enable/disable DLP profile.
    dlp_profile: str  # Name of an existing DLP profile.
    ip_threatfeed_status: NotRequired[Literal["enable", "disable"]]  # Enable/disable IP threat feed.
    ip_threatfeed: NotRequired[list[dict[str, Any]]]  # Name of an existing IP threat feed.
    file_filter_profile_status: NotRequired[Literal["enable", "disable"]]  # Enable/disable file filter.
    file_filter_profile: str  # Name of an existing file-filter profile.
    ips_dos_status: NotRequired[Literal["enable", "disable"]]  # Enable/disable IPS DoS anomaly detection.
    anomaly: NotRequired[list[dict[str, Any]]]  # Configuration method to edit Denial of Service (DoS) anomaly


class Sniffer:
    """
    Configure sniffer.
    
    Path: firewall/sniffer
    Category: cmdb
    Primary Key: id
    """
    
    def get(
        self,
        id: int | None = ...,
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
        payload_dict: SnifferPayload | None = ...,
        id: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        ipv6: Literal["enable", "disable"] | None = ...,
        non_ip: Literal["enable", "disable"] | None = ...,
        interface: str | None = ...,
        host: str | None = ...,
        port: str | None = ...,
        protocol: str | None = ...,
        vlan: str | None = ...,
        application_list_status: Literal["enable", "disable"] | None = ...,
        application_list: str | None = ...,
        ips_sensor_status: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        dsri: Literal["enable", "disable"] | None = ...,
        av_profile_status: Literal["enable", "disable"] | None = ...,
        av_profile: str | None = ...,
        webfilter_profile_status: Literal["enable", "disable"] | None = ...,
        webfilter_profile: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: SnifferPayload | None = ...,
        id: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        ipv6: Literal["enable", "disable"] | None = ...,
        non_ip: Literal["enable", "disable"] | None = ...,
        interface: str | None = ...,
        host: str | None = ...,
        port: str | None = ...,
        protocol: str | None = ...,
        vlan: str | None = ...,
        application_list_status: Literal["enable", "disable"] | None = ...,
        application_list: str | None = ...,
        ips_sensor_status: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        dsri: Literal["enable", "disable"] | None = ...,
        av_profile_status: Literal["enable", "disable"] | None = ...,
        av_profile: str | None = ...,
        webfilter_profile_status: Literal["enable", "disable"] | None = ...,
        webfilter_profile: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def exists(
        self,
        id: int,
        vdom: str | bool | None = ...,
    ) -> Union[bool, Coroutine[Any, Any, bool]]: ...
    
    def set(
        self,
        payload_dict: SnifferPayload | None = ...,
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