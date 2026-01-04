from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class SecurityPolicyPayload(TypedDict, total=False):
    """
    Type hints for firewall/security_policy payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: SecurityPolicyPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    uuid: NotRequired[str]  # Universally Unique Identifier (UUID; automatically assigned 
    policyid: NotRequired[int]  # Policy ID.
    name: NotRequired[str]  # Policy name.
    comments: NotRequired[str]  # Comment.
    srcintf: list[dict[str, Any]]  # Incoming (ingress) interface.
    dstintf: list[dict[str, Any]]  # Outgoing (egress) interface.
    srcaddr: NotRequired[list[dict[str, Any]]]  # Source IPv4 address name and address group names.
    srcaddr_negate: NotRequired[Literal["enable", "disable"]]  # When enabled srcaddr specifies what the source address must 
    dstaddr: NotRequired[list[dict[str, Any]]]  # Destination IPv4 address name and address group names.
    dstaddr_negate: NotRequired[Literal["enable", "disable"]]  # When enabled dstaddr specifies what the destination address 
    srcaddr6: NotRequired[list[dict[str, Any]]]  # Source IPv6 address name and address group names.
    srcaddr6_negate: NotRequired[Literal["enable", "disable"]]  # When enabled srcaddr6 specifies what the source address must
    dstaddr6: NotRequired[list[dict[str, Any]]]  # Destination IPv6 address name and address group names.
    dstaddr6_negate: NotRequired[Literal["enable", "disable"]]  # When enabled dstaddr6 specifies what the destination address
    internet_service: NotRequired[Literal["enable", "disable"]]  # Enable/disable use of Internet Services for this policy. If 
    internet_service_name: NotRequired[list[dict[str, Any]]]  # Internet Service name.
    internet_service_negate: NotRequired[Literal["enable", "disable"]]  # When enabled internet-service specifies what the service mus
    internet_service_group: NotRequired[list[dict[str, Any]]]  # Internet Service group name.
    internet_service_custom: NotRequired[list[dict[str, Any]]]  # Custom Internet Service name.
    internet_service_custom_group: NotRequired[list[dict[str, Any]]]  # Custom Internet Service group name.
    internet_service_src: NotRequired[Literal["enable", "disable"]]  # Enable/disable use of Internet Services in source for this p
    internet_service_src_name: NotRequired[list[dict[str, Any]]]  # Internet Service source name.
    internet_service_src_negate: NotRequired[Literal["enable", "disable"]]  # When enabled internet-service-src specifies what the service
    internet_service_src_group: NotRequired[list[dict[str, Any]]]  # Internet Service source group name.
    internet_service_src_custom: NotRequired[list[dict[str, Any]]]  # Custom Internet Service source name.
    internet_service_src_custom_group: NotRequired[list[dict[str, Any]]]  # Custom Internet Service source group name.
    internet_service6: NotRequired[Literal["enable", "disable"]]  # Enable/disable use of IPv6 Internet Services for this policy
    internet_service6_name: NotRequired[list[dict[str, Any]]]  # IPv6 Internet Service name.
    internet_service6_negate: NotRequired[Literal["enable", "disable"]]  # When enabled internet-service6 specifies what the service mu
    internet_service6_group: NotRequired[list[dict[str, Any]]]  # Internet Service group name.
    internet_service6_custom: NotRequired[list[dict[str, Any]]]  # Custom IPv6 Internet Service name.
    internet_service6_custom_group: NotRequired[list[dict[str, Any]]]  # Custom IPv6 Internet Service group name.
    internet_service6_src: NotRequired[Literal["enable", "disable"]]  # Enable/disable use of IPv6 Internet Services in source for t
    internet_service6_src_name: NotRequired[list[dict[str, Any]]]  # IPv6 Internet Service source name.
    internet_service6_src_negate: NotRequired[Literal["enable", "disable"]]  # When enabled internet-service6-src specifies what the servic
    internet_service6_src_group: NotRequired[list[dict[str, Any]]]  # Internet Service6 source group name.
    internet_service6_src_custom: NotRequired[list[dict[str, Any]]]  # Custom IPv6 Internet Service source name.
    internet_service6_src_custom_group: NotRequired[list[dict[str, Any]]]  # Custom Internet Service6 source group name.
    enforce_default_app_port: NotRequired[Literal["enable", "disable"]]  # Enable/disable default application port enforcement for allo
    service: NotRequired[list[dict[str, Any]]]  # Service and service group names.
    service_negate: NotRequired[Literal["enable", "disable"]]  # When enabled service specifies what the service must NOT be.
    action: NotRequired[Literal["accept", "deny"]]  # Policy action (accept/deny).
    send_deny_packet: NotRequired[Literal["disable", "enable"]]  # Enable to send a reply when a session is denied or blocked b
    schedule: str  # Schedule name.
    status: NotRequired[Literal["enable", "disable"]]  # Enable or disable this policy.
    logtraffic: NotRequired[Literal["all", "utm", "disable"]]  # Enable or disable logging. Log all sessions or security prof
    learning_mode: NotRequired[Literal["enable", "disable"]]  # Enable to allow everything, but log all of the meaningful da
    nat46: NotRequired[Literal["enable", "disable"]]  # Enable/disable NAT46.
    nat64: NotRequired[Literal["enable", "disable"]]  # Enable/disable NAT64.
    profile_type: NotRequired[Literal["single", "group"]]  # Determine whether the firewall policy allows security profil
    profile_group: NotRequired[str]  # Name of profile group.
    profile_protocol_options: NotRequired[str]  # Name of an existing Protocol options profile.
    ssl_ssh_profile: NotRequired[str]  # Name of an existing SSL SSH profile.
    av_profile: NotRequired[str]  # Name of an existing Antivirus profile.
    webfilter_profile: NotRequired[str]  # Name of an existing Web filter profile.
    dnsfilter_profile: NotRequired[str]  # Name of an existing DNS filter profile.
    emailfilter_profile: NotRequired[str]  # Name of an existing email filter profile.
    dlp_profile: NotRequired[str]  # Name of an existing DLP profile.
    file_filter_profile: NotRequired[str]  # Name of an existing file-filter profile.
    ips_sensor: NotRequired[str]  # Name of an existing IPS sensor.
    application_list: NotRequired[str]  # Name of an existing Application list.
    voip_profile: NotRequired[str]  # Name of an existing VoIP (voipd) profile.
    ips_voip_filter: NotRequired[str]  # Name of an existing VoIP (ips) profile.
    sctp_filter_profile: NotRequired[str]  # Name of an existing SCTP filter profile.
    diameter_filter_profile: NotRequired[str]  # Name of an existing Diameter filter profile.
    virtual_patch_profile: NotRequired[str]  # Name of an existing virtual-patch profile.
    icap_profile: NotRequired[str]  # Name of an existing ICAP profile.
    videofilter_profile: NotRequired[str]  # Name of an existing VideoFilter profile.
    ssh_filter_profile: NotRequired[str]  # Name of an existing SSH filter profile.
    casb_profile: NotRequired[str]  # Name of an existing CASB profile.
    application: NotRequired[list[dict[str, Any]]]  # Application ID list.
    app_category: NotRequired[list[dict[str, Any]]]  # Application category ID list.
    url_category: NotRequired[str]  # URL categories or groups.
    app_group: NotRequired[list[dict[str, Any]]]  # Application group names.
    groups: NotRequired[list[dict[str, Any]]]  # Names of user groups that can authenticate with this policy.
    users: NotRequired[list[dict[str, Any]]]  # Names of individual users that can authenticate with this po
    fsso_groups: NotRequired[list[dict[str, Any]]]  # Names of FSSO groups.


class SecurityPolicy:
    """
    Configure NGFW IPv4/IPv6 application policies.
    
    Path: firewall/security_policy
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
        payload_dict: SecurityPolicyPayload | None = ...,
        uuid: str | None = ...,
        policyid: int | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        srcintf: list[dict[str, Any]] | None = ...,
        dstintf: list[dict[str, Any]] | None = ...,
        srcaddr: list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr: list[dict[str, Any]] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        srcaddr6: list[dict[str, Any]] | None = ...,
        srcaddr6_negate: Literal["enable", "disable"] | None = ...,
        dstaddr6: list[dict[str, Any]] | None = ...,
        dstaddr6_negate: Literal["enable", "disable"] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: list[dict[str, Any]] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_group: list[dict[str, Any]] | None = ...,
        internet_service_custom: list[dict[str, Any]] | None = ...,
        internet_service_custom_group: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: SecurityPolicyPayload | None = ...,
        uuid: str | None = ...,
        policyid: int | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        srcintf: list[dict[str, Any]] | None = ...,
        dstintf: list[dict[str, Any]] | None = ...,
        srcaddr: list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr: list[dict[str, Any]] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        srcaddr6: list[dict[str, Any]] | None = ...,
        srcaddr6_negate: Literal["enable", "disable"] | None = ...,
        dstaddr6: list[dict[str, Any]] | None = ...,
        dstaddr6_negate: Literal["enable", "disable"] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: list[dict[str, Any]] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_group: list[dict[str, Any]] | None = ...,
        internet_service_custom: list[dict[str, Any]] | None = ...,
        internet_service_custom_group: list[dict[str, Any]] | None = ...,
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
        payload_dict: SecurityPolicyPayload | None = ...,
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