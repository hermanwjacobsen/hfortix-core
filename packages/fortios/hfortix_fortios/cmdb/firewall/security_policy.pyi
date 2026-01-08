from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class SecurityPolicyPayload(TypedDict, total=False):
    """
    Type hints for firewall/security_policy payload fields.
    
    Configure NGFW IPv4/IPv6 application policies.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.antivirus.profile.ProfileEndpoint` (via: av-profile)
        - :class:`~.application.list.ListEndpoint` (via: application-list)
        - :class:`~.casb.profile.ProfileEndpoint` (via: casb-profile)
        - :class:`~.diameter-filter.profile.ProfileEndpoint` (via: diameter-filter-profile)
        - :class:`~.dlp.profile.ProfileEndpoint` (via: dlp-profile)
        - :class:`~.dnsfilter.profile.ProfileEndpoint` (via: dnsfilter-profile)
        - :class:`~.emailfilter.profile.ProfileEndpoint` (via: emailfilter-profile)
        - :class:`~.file-filter.profile.ProfileEndpoint` (via: file-filter-profile)
        - :class:`~.firewall.profile-group.ProfileGroupEndpoint` (via: profile-group)
        - :class:`~.firewall.profile-protocol-options.ProfileProtocolOptionsEndpoint` (via: profile-protocol-options)
        - ... and 12 more dependencies

    **Usage:**
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
    internet_service_fortiguard: NotRequired[list[dict[str, Any]]]  # FortiGuard Internet Service name.
    internet_service_src: NotRequired[Literal["enable", "disable"]]  # Enable/disable use of Internet Services in source for this p
    internet_service_src_name: NotRequired[list[dict[str, Any]]]  # Internet Service source name.
    internet_service_src_negate: NotRequired[Literal["enable", "disable"]]  # When enabled internet-service-src specifies what the service
    internet_service_src_group: NotRequired[list[dict[str, Any]]]  # Internet Service source group name.
    internet_service_src_custom: NotRequired[list[dict[str, Any]]]  # Custom Internet Service source name.
    internet_service_src_custom_group: NotRequired[list[dict[str, Any]]]  # Custom Internet Service source group name.
    internet_service_src_fortiguard: NotRequired[list[dict[str, Any]]]  # FortiGuard Internet Service source name.
    internet_service6: NotRequired[Literal["enable", "disable"]]  # Enable/disable use of IPv6 Internet Services for this policy
    internet_service6_name: NotRequired[list[dict[str, Any]]]  # IPv6 Internet Service name.
    internet_service6_negate: NotRequired[Literal["enable", "disable"]]  # When enabled internet-service6 specifies what the service mu
    internet_service6_group: NotRequired[list[dict[str, Any]]]  # Internet Service group name.
    internet_service6_custom: NotRequired[list[dict[str, Any]]]  # Custom IPv6 Internet Service name.
    internet_service6_custom_group: NotRequired[list[dict[str, Any]]]  # Custom IPv6 Internet Service group name.
    internet_service6_fortiguard: NotRequired[list[dict[str, Any]]]  # FortiGuard IPv6 Internet Service name.
    internet_service6_src: NotRequired[Literal["enable", "disable"]]  # Enable/disable use of IPv6 Internet Services in source for t
    internet_service6_src_name: NotRequired[list[dict[str, Any]]]  # IPv6 Internet Service source name.
    internet_service6_src_negate: NotRequired[Literal["enable", "disable"]]  # When enabled internet-service6-src specifies what the servic
    internet_service6_src_group: NotRequired[list[dict[str, Any]]]  # Internet Service6 source group name.
    internet_service6_src_custom: NotRequired[list[dict[str, Any]]]  # Custom IPv6 Internet Service source name.
    internet_service6_src_custom_group: NotRequired[list[dict[str, Any]]]  # Custom Internet Service6 source group name.
    internet_service6_src_fortiguard: NotRequired[list[dict[str, Any]]]  # FortiGuard IPv6 Internet Service source name.
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
    url_category: NotRequired[list[dict[str, Any]]]  # URL categories or groups.
    app_group: NotRequired[list[dict[str, Any]]]  # Application group names.
    groups: NotRequired[list[dict[str, Any]]]  # Names of user groups that can authenticate with this policy.
    users: NotRequired[list[dict[str, Any]]]  # Names of individual users that can authenticate with this po
    fsso_groups: NotRequired[list[dict[str, Any]]]  # Names of FSSO groups.


class SecurityPolicyObject(FortiObject[SecurityPolicyPayload]):
    """Typed FortiObject for firewall/security_policy with IDE autocomplete support."""
    
    # Universally Unique Identifier (UUID; automatically assigned but can be manually 
    uuid: str
    # Policy ID.
    policyid: int
    # Policy name.
    name: str
    # Comment.
    comments: str
    # Incoming (ingress) interface.
    srcintf: list[str]  # Auto-flattened from member_table
    # Outgoing (egress) interface.
    dstintf: list[str]  # Auto-flattened from member_table
    # Source IPv4 address name and address group names.
    srcaddr: list[str]  # Auto-flattened from member_table
    # When enabled srcaddr specifies what the source address must NOT be.
    srcaddr_negate: Literal["enable", "disable"]
    # Destination IPv4 address name and address group names.
    dstaddr: list[str]  # Auto-flattened from member_table
    # When enabled dstaddr specifies what the destination address must NOT be.
    dstaddr_negate: Literal["enable", "disable"]
    # Source IPv6 address name and address group names.
    srcaddr6: list[str]  # Auto-flattened from member_table
    # When enabled srcaddr6 specifies what the source address must NOT be.
    srcaddr6_negate: Literal["enable", "disable"]
    # Destination IPv6 address name and address group names.
    dstaddr6: list[str]  # Auto-flattened from member_table
    # When enabled dstaddr6 specifies what the destination address must NOT be.
    dstaddr6_negate: Literal["enable", "disable"]
    # Enable/disable use of Internet Services for this policy. If enabled, destination
    internet_service: Literal["enable", "disable"]
    # Internet Service name.
    internet_service_name: list[str]  # Auto-flattened from member_table
    # When enabled internet-service specifies what the service must NOT be.
    internet_service_negate: Literal["enable", "disable"]
    # Internet Service group name.
    internet_service_group: list[str]  # Auto-flattened from member_table
    # Custom Internet Service name.
    internet_service_custom: list[str]  # Auto-flattened from member_table
    # Custom Internet Service group name.
    internet_service_custom_group: list[str]  # Auto-flattened from member_table
    # FortiGuard Internet Service name.
    internet_service_fortiguard: list[str]  # Auto-flattened from member_table
    # Enable/disable use of Internet Services in source for this policy. If enabled, s
    internet_service_src: Literal["enable", "disable"]
    # Internet Service source name.
    internet_service_src_name: list[str]  # Auto-flattened from member_table
    # When enabled internet-service-src specifies what the service must NOT be.
    internet_service_src_negate: Literal["enable", "disable"]
    # Internet Service source group name.
    internet_service_src_group: list[str]  # Auto-flattened from member_table
    # Custom Internet Service source name.
    internet_service_src_custom: list[str]  # Auto-flattened from member_table
    # Custom Internet Service source group name.
    internet_service_src_custom_group: list[str]  # Auto-flattened from member_table
    # FortiGuard Internet Service source name.
    internet_service_src_fortiguard: list[str]  # Auto-flattened from member_table
    # Enable/disable use of IPv6 Internet Services for this policy. If enabled, destin
    internet_service6: Literal["enable", "disable"]
    # IPv6 Internet Service name.
    internet_service6_name: list[str]  # Auto-flattened from member_table
    # When enabled internet-service6 specifies what the service must NOT be.
    internet_service6_negate: Literal["enable", "disable"]
    # Internet Service group name.
    internet_service6_group: list[str]  # Auto-flattened from member_table
    # Custom IPv6 Internet Service name.
    internet_service6_custom: list[str]  # Auto-flattened from member_table
    # Custom IPv6 Internet Service group name.
    internet_service6_custom_group: list[str]  # Auto-flattened from member_table
    # FortiGuard IPv6 Internet Service name.
    internet_service6_fortiguard: list[str]  # Auto-flattened from member_table
    # Enable/disable use of IPv6 Internet Services in source for this policy. If enabl
    internet_service6_src: Literal["enable", "disable"]
    # IPv6 Internet Service source name.
    internet_service6_src_name: list[str]  # Auto-flattened from member_table
    # When enabled internet-service6-src specifies what the service must NOT be.
    internet_service6_src_negate: Literal["enable", "disable"]
    # Internet Service6 source group name.
    internet_service6_src_group: list[str]  # Auto-flattened from member_table
    # Custom IPv6 Internet Service source name.
    internet_service6_src_custom: list[str]  # Auto-flattened from member_table
    # Custom Internet Service6 source group name.
    internet_service6_src_custom_group: list[str]  # Auto-flattened from member_table
    # FortiGuard IPv6 Internet Service source name.
    internet_service6_src_fortiguard: list[str]  # Auto-flattened from member_table
    # Enable/disable default application port enforcement for allowed applications.
    enforce_default_app_port: Literal["enable", "disable"]
    # Service and service group names.
    service: list[str]  # Auto-flattened from member_table
    # When enabled service specifies what the service must NOT be.
    service_negate: Literal["enable", "disable"]
    # Policy action (accept/deny).
    action: Literal["accept", "deny"]
    # Enable to send a reply when a session is denied or blocked by a firewall policy.
    send_deny_packet: Literal["disable", "enable"]
    # Schedule name.
    schedule: str
    # Enable or disable this policy.
    status: Literal["enable", "disable"]
    # Enable or disable logging. Log all sessions or security profile sessions.
    logtraffic: Literal["all", "utm", "disable"]
    # Enable to allow everything, but log all of the meaningful data for security info
    learning_mode: Literal["enable", "disable"]
    # Enable/disable NAT46.
    nat46: Literal["enable", "disable"]
    # Enable/disable NAT64.
    nat64: Literal["enable", "disable"]
    # Determine whether the firewall policy allows security profile groups or single p
    profile_type: Literal["single", "group"]
    # Name of profile group.
    profile_group: str
    # Name of an existing Protocol options profile.
    profile_protocol_options: str
    # Name of an existing SSL SSH profile.
    ssl_ssh_profile: str
    # Name of an existing Antivirus profile.
    av_profile: str
    # Name of an existing Web filter profile.
    webfilter_profile: str
    # Name of an existing DNS filter profile.
    dnsfilter_profile: str
    # Name of an existing email filter profile.
    emailfilter_profile: str
    # Name of an existing DLP profile.
    dlp_profile: str
    # Name of an existing file-filter profile.
    file_filter_profile: str
    # Name of an existing IPS sensor.
    ips_sensor: str
    # Name of an existing Application list.
    application_list: str
    # Name of an existing VoIP (voipd) profile.
    voip_profile: str
    # Name of an existing VoIP (ips) profile.
    ips_voip_filter: str
    # Name of an existing SCTP filter profile.
    sctp_filter_profile: str
    # Name of an existing Diameter filter profile.
    diameter_filter_profile: str
    # Name of an existing virtual-patch profile.
    virtual_patch_profile: str
    # Name of an existing ICAP profile.
    icap_profile: str
    # Name of an existing VideoFilter profile.
    videofilter_profile: str
    # Name of an existing SSH filter profile.
    ssh_filter_profile: str
    # Name of an existing CASB profile.
    casb_profile: str
    # Application ID list.
    application: list[str]  # Auto-flattened from member_table
    # Application category ID list.
    app_category: list[str]  # Auto-flattened from member_table
    # URL categories or groups.
    url_category: list[str]  # Auto-flattened from member_table
    # Application group names.
    app_group: list[str]  # Auto-flattened from member_table
    # Names of user groups that can authenticate with this policy.
    groups: list[str]  # Auto-flattened from member_table
    # Names of individual users that can authenticate with this policy.
    users: list[str]  # Auto-flattened from member_table
    # Names of FSSO groups.
    fsso_groups: list[str]  # Auto-flattened from member_table
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> SecurityPolicyPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class SecurityPolicy:
    """
    Configure NGFW IPv4/IPv6 application policies.
    
    Path: firewall/security_policy
    Category: cmdb
    Primary Key: policyid
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey provided)
    @overload
    def get(
        self,
        policyid: int,
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
    ) -> SecurityPolicyObject: ...
    
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
    ) -> list[SecurityPolicyObject]: ...
    
    @overload
    def get(
        self,
        policyid: int | None = ...,
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
        policyid: int,
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
        policyid: None = None,
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
        policyid: int | None = ...,
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
        policyid: int | None = ...,
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
    ) -> SecurityPolicyObject | list[SecurityPolicyObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: SecurityPolicyPayload | None = ...,
        uuid: str | None = ...,
        policyid: int | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6_negate: Literal["enable", "disable"] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6_negate: Literal["enable", "disable"] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src: Literal["enable", "disable"] | None = ...,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        enforce_default_app_port: Literal["enable", "disable"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        send_deny_packet: Literal["disable", "enable"] | None = ...,
        schedule: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        learning_mode: Literal["enable", "disable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        profile_type: Literal["single", "group"] | None = ...,
        profile_group: str | None = ...,
        profile_protocol_options: str | None = ...,
        ssl_ssh_profile: str | None = ...,
        av_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        dnsfilter_profile: str | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile: str | None = ...,
        file_filter_profile: str | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        voip_profile: str | None = ...,
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        diameter_filter_profile: str | None = ...,
        virtual_patch_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        app_category: str | list[str] | list[dict[str, Any]] | None = ...,
        url_category: str | list[str] | list[dict[str, Any]] | None = ...,
        app_group: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SecurityPolicyObject: ...
    
    @overload
    def post(
        self,
        payload_dict: SecurityPolicyPayload | None = ...,
        uuid: str | None = ...,
        policyid: int | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6_negate: Literal["enable", "disable"] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6_negate: Literal["enable", "disable"] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src: Literal["enable", "disable"] | None = ...,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        enforce_default_app_port: Literal["enable", "disable"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        send_deny_packet: Literal["disable", "enable"] | None = ...,
        schedule: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        learning_mode: Literal["enable", "disable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        profile_type: Literal["single", "group"] | None = ...,
        profile_group: str | None = ...,
        profile_protocol_options: str | None = ...,
        ssl_ssh_profile: str | None = ...,
        av_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        dnsfilter_profile: str | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile: str | None = ...,
        file_filter_profile: str | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        voip_profile: str | None = ...,
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        diameter_filter_profile: str | None = ...,
        virtual_patch_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        app_category: str | list[str] | list[dict[str, Any]] | None = ...,
        url_category: str | list[str] | list[dict[str, Any]] | None = ...,
        app_group: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: SecurityPolicyPayload | None = ...,
        uuid: str | None = ...,
        policyid: int | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6_negate: Literal["enable", "disable"] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6_negate: Literal["enable", "disable"] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src: Literal["enable", "disable"] | None = ...,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        enforce_default_app_port: Literal["enable", "disable"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        send_deny_packet: Literal["disable", "enable"] | None = ...,
        schedule: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        learning_mode: Literal["enable", "disable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        profile_type: Literal["single", "group"] | None = ...,
        profile_group: str | None = ...,
        profile_protocol_options: str | None = ...,
        ssl_ssh_profile: str | None = ...,
        av_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        dnsfilter_profile: str | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile: str | None = ...,
        file_filter_profile: str | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        voip_profile: str | None = ...,
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        diameter_filter_profile: str | None = ...,
        virtual_patch_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        app_category: str | list[str] | list[dict[str, Any]] | None = ...,
        url_category: str | list[str] | list[dict[str, Any]] | None = ...,
        app_group: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: SecurityPolicyPayload | None = ...,
        uuid: str | None = ...,
        policyid: int | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6_negate: Literal["enable", "disable"] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6_negate: Literal["enable", "disable"] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src: Literal["enable", "disable"] | None = ...,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        enforce_default_app_port: Literal["enable", "disable"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        send_deny_packet: Literal["disable", "enable"] | None = ...,
        schedule: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        learning_mode: Literal["enable", "disable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        profile_type: Literal["single", "group"] | None = ...,
        profile_group: str | None = ...,
        profile_protocol_options: str | None = ...,
        ssl_ssh_profile: str | None = ...,
        av_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        dnsfilter_profile: str | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile: str | None = ...,
        file_filter_profile: str | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        voip_profile: str | None = ...,
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        diameter_filter_profile: str | None = ...,
        virtual_patch_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        app_category: str | list[str] | list[dict[str, Any]] | None = ...,
        url_category: str | list[str] | list[dict[str, Any]] | None = ...,
        app_group: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: SecurityPolicyPayload | None = ...,
        uuid: str | None = ...,
        policyid: int | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6_negate: Literal["enable", "disable"] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6_negate: Literal["enable", "disable"] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src: Literal["enable", "disable"] | None = ...,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        enforce_default_app_port: Literal["enable", "disable"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        send_deny_packet: Literal["disable", "enable"] | None = ...,
        schedule: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        learning_mode: Literal["enable", "disable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        profile_type: Literal["single", "group"] | None = ...,
        profile_group: str | None = ...,
        profile_protocol_options: str | None = ...,
        ssl_ssh_profile: str | None = ...,
        av_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        dnsfilter_profile: str | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile: str | None = ...,
        file_filter_profile: str | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        voip_profile: str | None = ...,
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        diameter_filter_profile: str | None = ...,
        virtual_patch_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        app_category: str | list[str] | list[dict[str, Any]] | None = ...,
        url_category: str | list[str] | list[dict[str, Any]] | None = ...,
        app_group: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SecurityPolicyObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SecurityPolicyPayload | None = ...,
        uuid: str | None = ...,
        policyid: int | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6_negate: Literal["enable", "disable"] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6_negate: Literal["enable", "disable"] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src: Literal["enable", "disable"] | None = ...,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        enforce_default_app_port: Literal["enable", "disable"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        send_deny_packet: Literal["disable", "enable"] | None = ...,
        schedule: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        learning_mode: Literal["enable", "disable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        profile_type: Literal["single", "group"] | None = ...,
        profile_group: str | None = ...,
        profile_protocol_options: str | None = ...,
        ssl_ssh_profile: str | None = ...,
        av_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        dnsfilter_profile: str | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile: str | None = ...,
        file_filter_profile: str | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        voip_profile: str | None = ...,
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        diameter_filter_profile: str | None = ...,
        virtual_patch_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        app_category: str | list[str] | list[dict[str, Any]] | None = ...,
        url_category: str | list[str] | list[dict[str, Any]] | None = ...,
        app_group: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: SecurityPolicyPayload | None = ...,
        uuid: str | None = ...,
        policyid: int | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6_negate: Literal["enable", "disable"] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6_negate: Literal["enable", "disable"] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src: Literal["enable", "disable"] | None = ...,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        enforce_default_app_port: Literal["enable", "disable"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        send_deny_packet: Literal["disable", "enable"] | None = ...,
        schedule: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        learning_mode: Literal["enable", "disable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        profile_type: Literal["single", "group"] | None = ...,
        profile_group: str | None = ...,
        profile_protocol_options: str | None = ...,
        ssl_ssh_profile: str | None = ...,
        av_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        dnsfilter_profile: str | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile: str | None = ...,
        file_filter_profile: str | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        voip_profile: str | None = ...,
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        diameter_filter_profile: str | None = ...,
        virtual_patch_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        app_category: str | list[str] | list[dict[str, Any]] | None = ...,
        url_category: str | list[str] | list[dict[str, Any]] | None = ...,
        app_group: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: SecurityPolicyPayload | None = ...,
        uuid: str | None = ...,
        policyid: int | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6_negate: Literal["enable", "disable"] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6_negate: Literal["enable", "disable"] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src: Literal["enable", "disable"] | None = ...,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        enforce_default_app_port: Literal["enable", "disable"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        send_deny_packet: Literal["disable", "enable"] | None = ...,
        schedule: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        learning_mode: Literal["enable", "disable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        profile_type: Literal["single", "group"] | None = ...,
        profile_group: str | None = ...,
        profile_protocol_options: str | None = ...,
        ssl_ssh_profile: str | None = ...,
        av_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        dnsfilter_profile: str | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile: str | None = ...,
        file_filter_profile: str | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        voip_profile: str | None = ...,
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        diameter_filter_profile: str | None = ...,
        virtual_patch_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        app_category: str | list[str] | list[dict[str, Any]] | None = ...,
        url_category: str | list[str] | list[dict[str, Any]] | None = ...,
        app_group: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SecurityPolicyObject: ...
    
    @overload
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        policyid: int,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: SecurityPolicyPayload | None = ...,
        uuid: str | None = ...,
        policyid: int | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6_negate: Literal["enable", "disable"] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6_negate: Literal["enable", "disable"] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src: Literal["enable", "disable"] | None = ...,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        enforce_default_app_port: Literal["enable", "disable"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        send_deny_packet: Literal["disable", "enable"] | None = ...,
        schedule: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        learning_mode: Literal["enable", "disable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        profile_type: Literal["single", "group"] | None = ...,
        profile_group: str | None = ...,
        profile_protocol_options: str | None = ...,
        ssl_ssh_profile: str | None = ...,
        av_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        dnsfilter_profile: str | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile: str | None = ...,
        file_filter_profile: str | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        voip_profile: str | None = ...,
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        diameter_filter_profile: str | None = ...,
        virtual_patch_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        app_category: str | list[str] | list[dict[str, Any]] | None = ...,
        url_category: str | list[str] | list[dict[str, Any]] | None = ...,
        app_group: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_groups: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "SecurityPolicy",
    "SecurityPolicyPayload",
    "SecurityPolicyObject",
]