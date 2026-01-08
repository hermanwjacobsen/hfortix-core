from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class ProxyPolicyPayload(TypedDict, total=False):
    """
    Type hints for firewall/proxy_policy payload fields.
    
    Configure proxy policies.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.antivirus.profile.ProfileEndpoint` (via: av-profile)
        - :class:`~.application.list.ListEndpoint` (via: application-list)
        - :class:`~.casb.profile.ProfileEndpoint` (via: casb-profile)
        - :class:`~.dlp.profile.ProfileEndpoint` (via: dlp-profile)
        - :class:`~.dnsfilter.profile.ProfileEndpoint` (via: dnsfilter-profile)
        - :class:`~.emailfilter.profile.ProfileEndpoint` (via: emailfilter-profile)
        - :class:`~.file-filter.profile.ProfileEndpoint` (via: file-filter-profile)
        - :class:`~.firewall.decrypted-traffic-mirror.DecryptedTrafficMirrorEndpoint` (via: decrypted-traffic-mirror)
        - :class:`~.firewall.profile-group.ProfileGroupEndpoint` (via: profile-group)
        - :class:`~.firewall.profile-protocol-options.ProfileProtocolOptionsEndpoint` (via: profile-protocol-options)
        - ... and 17 more dependencies

    **Usage:**
        payload: ProxyPolicyPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    uuid: NotRequired[str]  # Universally Unique Identifier (UUID; automatically assigned 
    policyid: NotRequired[int]  # Policy ID.
    name: NotRequired[str]  # Policy name.
    proxy: Literal["explicit-web", "transparent-web", "ftp", "ssh", "ssh-tunnel", "access-proxy", "ztna-proxy", "wanopt"]  # Type of explicit proxy.
    access_proxy: NotRequired[list[dict[str, Any]]]  # IPv4 access proxy.
    access_proxy6: NotRequired[list[dict[str, Any]]]  # IPv6 access proxy.
    ztna_proxy: NotRequired[list[dict[str, Any]]]  # ZTNA proxies.
    srcintf: list[dict[str, Any]]  # Source interface names.
    dstintf: list[dict[str, Any]]  # Destination interface names.
    srcaddr: NotRequired[list[dict[str, Any]]]  # Source address objects.
    poolname: NotRequired[list[dict[str, Any]]]  # Name of IP pool object.
    poolname6: NotRequired[list[dict[str, Any]]]  # Name of IPv6 pool object.
    dstaddr: NotRequired[list[dict[str, Any]]]  # Destination address objects.
    ztna_ems_tag: NotRequired[list[dict[str, Any]]]  # ZTNA EMS Tag names.
    ztna_tags_match_logic: NotRequired[Literal["or", "and"]]  # ZTNA tag matching logic.
    device_ownership: NotRequired[Literal["enable", "disable"]]  # When enabled, the ownership enforcement will be done at poli
    url_risk: NotRequired[list[dict[str, Any]]]  # URL risk level name.
    internet_service: NotRequired[Literal["enable", "disable"]]  # Enable/disable use of Internet Services for this policy. If 
    internet_service_negate: NotRequired[Literal["enable", "disable"]]  # When enabled, Internet Services match against any internet s
    internet_service_name: NotRequired[list[dict[str, Any]]]  # Internet Service name.
    internet_service_group: NotRequired[list[dict[str, Any]]]  # Internet Service group name.
    internet_service_custom: NotRequired[list[dict[str, Any]]]  # Custom Internet Service name.
    internet_service_custom_group: NotRequired[list[dict[str, Any]]]  # Custom Internet Service group name.
    internet_service_fortiguard: NotRequired[list[dict[str, Any]]]  # FortiGuard Internet Service name.
    internet_service6: NotRequired[Literal["enable", "disable"]]  # Enable/disable use of Internet Services IPv6 for this policy
    internet_service6_negate: NotRequired[Literal["enable", "disable"]]  # When enabled, Internet Services match against any internet s
    internet_service6_name: NotRequired[list[dict[str, Any]]]  # Internet Service IPv6 name.
    internet_service6_group: NotRequired[list[dict[str, Any]]]  # Internet Service IPv6 group name.
    internet_service6_custom: NotRequired[list[dict[str, Any]]]  # Custom Internet Service IPv6 name.
    internet_service6_custom_group: NotRequired[list[dict[str, Any]]]  # Custom Internet Service IPv6 group name.
    internet_service6_fortiguard: NotRequired[list[dict[str, Any]]]  # FortiGuard Internet Service IPv6 name.
    service: NotRequired[list[dict[str, Any]]]  # Name of service objects.
    srcaddr_negate: NotRequired[Literal["enable", "disable"]]  # When enabled, source addresses match against any address EXC
    dstaddr_negate: NotRequired[Literal["enable", "disable"]]  # When enabled, destination addresses match against any addres
    ztna_ems_tag_negate: NotRequired[Literal["enable", "disable"]]  # When enabled, ZTNA EMS tags match against any tag EXCEPT the
    service_negate: NotRequired[Literal["enable", "disable"]]  # When enabled, services match against any service EXCEPT the 
    action: NotRequired[Literal["accept", "deny", "redirect", "isolate"]]  # Accept or deny traffic matching the policy parameters.
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable the active status of the policy.
    schedule: str  # Name of schedule object.
    logtraffic: NotRequired[Literal["all", "utm", "disable"]]  # Enable/disable logging traffic through the policy.
    session_ttl: NotRequired[int]  # TTL in seconds for sessions accepted by this policy (0 means
    srcaddr6: NotRequired[list[dict[str, Any]]]  # IPv6 source address objects.
    dstaddr6: NotRequired[list[dict[str, Any]]]  # IPv6 destination address objects.
    groups: NotRequired[list[dict[str, Any]]]  # Names of group objects.
    users: NotRequired[list[dict[str, Any]]]  # Names of user objects.
    http_tunnel_auth: NotRequired[Literal["enable", "disable"]]  # Enable/disable HTTP tunnel authentication.
    ssh_policy_redirect: NotRequired[Literal["enable", "disable"]]  # Redirect SSH traffic to matching transparent proxy policy.
    webproxy_forward_server: NotRequired[str]  # Web proxy forward server name.
    isolator_server: str  # Isolator server name.
    webproxy_profile: NotRequired[str]  # Name of web proxy profile.
    transparent: NotRequired[Literal["enable", "disable"]]  # Enable to use the IP address of the client to connect to the
    webcache: NotRequired[Literal["enable", "disable"]]  # Enable/disable web caching.
    webcache_https: NotRequired[Literal["disable", "enable"]]  # Enable/disable web caching for HTTPS (Requires deep-inspecti
    disclaimer: NotRequired[Literal["disable", "domain", "policy", "user"]]  # Web proxy disclaimer setting: by domain, policy, or user.
    utm_status: NotRequired[Literal["enable", "disable"]]  # Enable the use of UTM profiles/sensors/lists.
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
    ips_voip_filter: NotRequired[str]  # Name of an existing VoIP (ips) profile.
    sctp_filter_profile: NotRequired[str]  # Name of an existing SCTP filter profile.
    icap_profile: NotRequired[str]  # Name of an existing ICAP profile.
    videofilter_profile: NotRequired[str]  # Name of an existing VideoFilter profile.
    waf_profile: NotRequired[str]  # Name of an existing Web application firewall profile.
    ssh_filter_profile: NotRequired[str]  # Name of an existing SSH filter profile.
    casb_profile: NotRequired[str]  # Name of an existing CASB profile.
    replacemsg_override_group: NotRequired[str]  # Authentication replacement message override group.
    logtraffic_start: NotRequired[Literal["enable", "disable"]]  # Enable/disable policy log traffic start.
    log_http_transaction: NotRequired[Literal["enable", "disable"]]  # Enable/disable HTTP transaction log.
    comments: NotRequired[str]  # Optional comments.
    block_notification: NotRequired[Literal["enable", "disable"]]  # Enable/disable block notification.
    redirect_url: NotRequired[str]  # Redirect URL for further explicit web proxy processing.
    https_sub_category: NotRequired[Literal["enable", "disable"]]  # Enable/disable HTTPS sub-category policy matching.
    decrypted_traffic_mirror: NotRequired[str]  # Decrypted traffic mirror.
    detect_https_in_http_request: NotRequired[Literal["enable", "disable"]]  # Enable/disable detection of HTTPS in HTTP request.


class ProxyPolicyObject(FortiObject[ProxyPolicyPayload]):
    """Typed FortiObject for firewall/proxy_policy with IDE autocomplete support."""
    
    # Universally Unique Identifier (UUID; automatically assigned but can be manually 
    uuid: str
    # Policy ID.
    policyid: int
    # Policy name.
    name: str
    # Type of explicit proxy.
    proxy: Literal["explicit-web", "transparent-web", "ftp", "ssh", "ssh-tunnel", "access-proxy", "ztna-proxy", "wanopt"]
    # IPv4 access proxy.
    access_proxy: list[str]  # Auto-flattened from member_table
    # IPv6 access proxy.
    access_proxy6: list[str]  # Auto-flattened from member_table
    # ZTNA proxies.
    ztna_proxy: list[str]  # Auto-flattened from member_table
    # Source interface names.
    srcintf: list[str]  # Auto-flattened from member_table
    # Destination interface names.
    dstintf: list[str]  # Auto-flattened from member_table
    # Source address objects.
    srcaddr: list[str]  # Auto-flattened from member_table
    # Name of IP pool object.
    poolname: list[str]  # Auto-flattened from member_table
    # Name of IPv6 pool object.
    poolname6: list[str]  # Auto-flattened from member_table
    # Destination address objects.
    dstaddr: list[str]  # Auto-flattened from member_table
    # ZTNA EMS Tag names.
    ztna_ems_tag: list[str]  # Auto-flattened from member_table
    # ZTNA tag matching logic.
    ztna_tags_match_logic: Literal["or", "and"]
    # When enabled, the ownership enforcement will be done at policy level.
    device_ownership: Literal["enable", "disable"]
    # URL risk level name.
    url_risk: list[str]  # Auto-flattened from member_table
    # Enable/disable use of Internet Services for this policy. If enabled, destination
    internet_service: Literal["enable", "disable"]
    # When enabled, Internet Services match against any internet service EXCEPT the se
    internet_service_negate: Literal["enable", "disable"]
    # Internet Service name.
    internet_service_name: list[str]  # Auto-flattened from member_table
    # Internet Service group name.
    internet_service_group: list[str]  # Auto-flattened from member_table
    # Custom Internet Service name.
    internet_service_custom: list[str]  # Auto-flattened from member_table
    # Custom Internet Service group name.
    internet_service_custom_group: list[str]  # Auto-flattened from member_table
    # FortiGuard Internet Service name.
    internet_service_fortiguard: list[str]  # Auto-flattened from member_table
    # Enable/disable use of Internet Services IPv6 for this policy. If enabled, destin
    internet_service6: Literal["enable", "disable"]
    # When enabled, Internet Services match against any internet service IPv6 EXCEPT t
    internet_service6_negate: Literal["enable", "disable"]
    # Internet Service IPv6 name.
    internet_service6_name: list[str]  # Auto-flattened from member_table
    # Internet Service IPv6 group name.
    internet_service6_group: list[str]  # Auto-flattened from member_table
    # Custom Internet Service IPv6 name.
    internet_service6_custom: list[str]  # Auto-flattened from member_table
    # Custom Internet Service IPv6 group name.
    internet_service6_custom_group: list[str]  # Auto-flattened from member_table
    # FortiGuard Internet Service IPv6 name.
    internet_service6_fortiguard: list[str]  # Auto-flattened from member_table
    # Name of service objects.
    service: list[str]  # Auto-flattened from member_table
    # When enabled, source addresses match against any address EXCEPT the specified so
    srcaddr_negate: Literal["enable", "disable"]
    # When enabled, destination addresses match against any address EXCEPT the specifi
    dstaddr_negate: Literal["enable", "disable"]
    # When enabled, ZTNA EMS tags match against any tag EXCEPT the specified ZTNA EMS 
    ztna_ems_tag_negate: Literal["enable", "disable"]
    # When enabled, services match against any service EXCEPT the specified destinatio
    service_negate: Literal["enable", "disable"]
    # Accept or deny traffic matching the policy parameters.
    action: Literal["accept", "deny", "redirect", "isolate"]
    # Enable/disable the active status of the policy.
    status: Literal["enable", "disable"]
    # Name of schedule object.
    schedule: str
    # Enable/disable logging traffic through the policy.
    logtraffic: Literal["all", "utm", "disable"]
    # TTL in seconds for sessions accepted by this policy (0 means use the system defa
    session_ttl: int
    # IPv6 source address objects.
    srcaddr6: list[str]  # Auto-flattened from member_table
    # IPv6 destination address objects.
    dstaddr6: list[str]  # Auto-flattened from member_table
    # Names of group objects.
    groups: list[str]  # Auto-flattened from member_table
    # Names of user objects.
    users: list[str]  # Auto-flattened from member_table
    # Enable/disable HTTP tunnel authentication.
    http_tunnel_auth: Literal["enable", "disable"]
    # Redirect SSH traffic to matching transparent proxy policy.
    ssh_policy_redirect: Literal["enable", "disable"]
    # Web proxy forward server name.
    webproxy_forward_server: str
    # Isolator server name.
    isolator_server: str
    # Name of web proxy profile.
    webproxy_profile: str
    # Enable to use the IP address of the client to connect to the server.
    transparent: Literal["enable", "disable"]
    # Enable/disable web caching.
    webcache: Literal["enable", "disable"]
    # Enable/disable web caching for HTTPS (Requires deep-inspection enabled in ssl-ss
    webcache_https: Literal["disable", "enable"]
    # Web proxy disclaimer setting: by domain, policy, or user.
    disclaimer: Literal["disable", "domain", "policy", "user"]
    # Enable the use of UTM profiles/sensors/lists.
    utm_status: Literal["enable", "disable"]
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
    # Name of an existing VoIP (ips) profile.
    ips_voip_filter: str
    # Name of an existing SCTP filter profile.
    sctp_filter_profile: str
    # Name of an existing ICAP profile.
    icap_profile: str
    # Name of an existing VideoFilter profile.
    videofilter_profile: str
    # Name of an existing Web application firewall profile.
    waf_profile: str
    # Name of an existing SSH filter profile.
    ssh_filter_profile: str
    # Name of an existing CASB profile.
    casb_profile: str
    # Authentication replacement message override group.
    replacemsg_override_group: str
    # Enable/disable policy log traffic start.
    logtraffic_start: Literal["enable", "disable"]
    # Enable/disable HTTP transaction log.
    log_http_transaction: Literal["enable", "disable"]
    # Optional comments.
    comments: str
    # Enable/disable block notification.
    block_notification: Literal["enable", "disable"]
    # Redirect URL for further explicit web proxy processing.
    redirect_url: str
    # Enable/disable HTTPS sub-category policy matching.
    https_sub_category: Literal["enable", "disable"]
    # Decrypted traffic mirror.
    decrypted_traffic_mirror: str
    # Enable/disable detection of HTTPS in HTTP request.
    detect_https_in_http_request: Literal["enable", "disable"]
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> ProxyPolicyPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class ProxyPolicy:
    """
    Configure proxy policies.
    
    Path: firewall/proxy_policy
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
    ) -> ProxyPolicyObject: ...
    
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
    ) -> list[ProxyPolicyObject]: ...
    
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
    ) -> ProxyPolicyObject | list[ProxyPolicyObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: ProxyPolicyPayload | None = ...,
        uuid: str | None = ...,
        policyid: int | None = ...,
        name: str | None = ...,
        proxy: Literal["explicit-web", "transparent-web", "ftp", "ssh", "ssh-tunnel", "access-proxy", "ztna-proxy", "wanopt"] | None = ...,
        access_proxy: str | list[str] | list[dict[str, Any]] | None = ...,
        access_proxy6: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_proxy: str | list[str] | list[dict[str, Any]] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_tags_match_logic: Literal["or", "and"] | None = ...,
        device_ownership: Literal["enable", "disable"] | None = ...,
        url_risk: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        ztna_ems_tag_negate: Literal["enable", "disable"] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny", "redirect", "isolate"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        schedule: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        session_ttl: int | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        http_tunnel_auth: Literal["enable", "disable"] | None = ...,
        ssh_policy_redirect: Literal["enable", "disable"] | None = ...,
        webproxy_forward_server: str | None = ...,
        isolator_server: str | None = ...,
        webproxy_profile: str | None = ...,
        transparent: Literal["enable", "disable"] | None = ...,
        webcache: Literal["enable", "disable"] | None = ...,
        webcache_https: Literal["disable", "enable"] | None = ...,
        disclaimer: Literal["disable", "domain", "policy", "user"] | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
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
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        waf_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        replacemsg_override_group: str | None = ...,
        logtraffic_start: Literal["enable", "disable"] | None = ...,
        log_http_transaction: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        block_notification: Literal["enable", "disable"] | None = ...,
        redirect_url: str | None = ...,
        https_sub_category: Literal["enable", "disable"] | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        detect_https_in_http_request: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ProxyPolicyObject: ...
    
    @overload
    def post(
        self,
        payload_dict: ProxyPolicyPayload | None = ...,
        uuid: str | None = ...,
        policyid: int | None = ...,
        name: str | None = ...,
        proxy: Literal["explicit-web", "transparent-web", "ftp", "ssh", "ssh-tunnel", "access-proxy", "ztna-proxy", "wanopt"] | None = ...,
        access_proxy: str | list[str] | list[dict[str, Any]] | None = ...,
        access_proxy6: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_proxy: str | list[str] | list[dict[str, Any]] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_tags_match_logic: Literal["or", "and"] | None = ...,
        device_ownership: Literal["enable", "disable"] | None = ...,
        url_risk: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        ztna_ems_tag_negate: Literal["enable", "disable"] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny", "redirect", "isolate"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        schedule: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        session_ttl: int | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        http_tunnel_auth: Literal["enable", "disable"] | None = ...,
        ssh_policy_redirect: Literal["enable", "disable"] | None = ...,
        webproxy_forward_server: str | None = ...,
        isolator_server: str | None = ...,
        webproxy_profile: str | None = ...,
        transparent: Literal["enable", "disable"] | None = ...,
        webcache: Literal["enable", "disable"] | None = ...,
        webcache_https: Literal["disable", "enable"] | None = ...,
        disclaimer: Literal["disable", "domain", "policy", "user"] | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
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
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        waf_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        replacemsg_override_group: str | None = ...,
        logtraffic_start: Literal["enable", "disable"] | None = ...,
        log_http_transaction: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        block_notification: Literal["enable", "disable"] | None = ...,
        redirect_url: str | None = ...,
        https_sub_category: Literal["enable", "disable"] | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        detect_https_in_http_request: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: ProxyPolicyPayload | None = ...,
        uuid: str | None = ...,
        policyid: int | None = ...,
        name: str | None = ...,
        proxy: Literal["explicit-web", "transparent-web", "ftp", "ssh", "ssh-tunnel", "access-proxy", "ztna-proxy", "wanopt"] | None = ...,
        access_proxy: str | list[str] | list[dict[str, Any]] | None = ...,
        access_proxy6: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_proxy: str | list[str] | list[dict[str, Any]] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_tags_match_logic: Literal["or", "and"] | None = ...,
        device_ownership: Literal["enable", "disable"] | None = ...,
        url_risk: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        ztna_ems_tag_negate: Literal["enable", "disable"] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny", "redirect", "isolate"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        schedule: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        session_ttl: int | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        http_tunnel_auth: Literal["enable", "disable"] | None = ...,
        ssh_policy_redirect: Literal["enable", "disable"] | None = ...,
        webproxy_forward_server: str | None = ...,
        isolator_server: str | None = ...,
        webproxy_profile: str | None = ...,
        transparent: Literal["enable", "disable"] | None = ...,
        webcache: Literal["enable", "disable"] | None = ...,
        webcache_https: Literal["disable", "enable"] | None = ...,
        disclaimer: Literal["disable", "domain", "policy", "user"] | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
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
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        waf_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        replacemsg_override_group: str | None = ...,
        logtraffic_start: Literal["enable", "disable"] | None = ...,
        log_http_transaction: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        block_notification: Literal["enable", "disable"] | None = ...,
        redirect_url: str | None = ...,
        https_sub_category: Literal["enable", "disable"] | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        detect_https_in_http_request: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: ProxyPolicyPayload | None = ...,
        uuid: str | None = ...,
        policyid: int | None = ...,
        name: str | None = ...,
        proxy: Literal["explicit-web", "transparent-web", "ftp", "ssh", "ssh-tunnel", "access-proxy", "ztna-proxy", "wanopt"] | None = ...,
        access_proxy: str | list[str] | list[dict[str, Any]] | None = ...,
        access_proxy6: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_proxy: str | list[str] | list[dict[str, Any]] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_tags_match_logic: Literal["or", "and"] | None = ...,
        device_ownership: Literal["enable", "disable"] | None = ...,
        url_risk: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        ztna_ems_tag_negate: Literal["enable", "disable"] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny", "redirect", "isolate"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        schedule: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        session_ttl: int | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        http_tunnel_auth: Literal["enable", "disable"] | None = ...,
        ssh_policy_redirect: Literal["enable", "disable"] | None = ...,
        webproxy_forward_server: str | None = ...,
        isolator_server: str | None = ...,
        webproxy_profile: str | None = ...,
        transparent: Literal["enable", "disable"] | None = ...,
        webcache: Literal["enable", "disable"] | None = ...,
        webcache_https: Literal["disable", "enable"] | None = ...,
        disclaimer: Literal["disable", "domain", "policy", "user"] | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
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
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        waf_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        replacemsg_override_group: str | None = ...,
        logtraffic_start: Literal["enable", "disable"] | None = ...,
        log_http_transaction: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        block_notification: Literal["enable", "disable"] | None = ...,
        redirect_url: str | None = ...,
        https_sub_category: Literal["enable", "disable"] | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        detect_https_in_http_request: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ProxyPolicyPayload | None = ...,
        uuid: str | None = ...,
        policyid: int | None = ...,
        name: str | None = ...,
        proxy: Literal["explicit-web", "transparent-web", "ftp", "ssh", "ssh-tunnel", "access-proxy", "ztna-proxy", "wanopt"] | None = ...,
        access_proxy: str | list[str] | list[dict[str, Any]] | None = ...,
        access_proxy6: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_proxy: str | list[str] | list[dict[str, Any]] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_tags_match_logic: Literal["or", "and"] | None = ...,
        device_ownership: Literal["enable", "disable"] | None = ...,
        url_risk: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        ztna_ems_tag_negate: Literal["enable", "disable"] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny", "redirect", "isolate"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        schedule: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        session_ttl: int | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        http_tunnel_auth: Literal["enable", "disable"] | None = ...,
        ssh_policy_redirect: Literal["enable", "disable"] | None = ...,
        webproxy_forward_server: str | None = ...,
        isolator_server: str | None = ...,
        webproxy_profile: str | None = ...,
        transparent: Literal["enable", "disable"] | None = ...,
        webcache: Literal["enable", "disable"] | None = ...,
        webcache_https: Literal["disable", "enable"] | None = ...,
        disclaimer: Literal["disable", "domain", "policy", "user"] | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
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
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        waf_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        replacemsg_override_group: str | None = ...,
        logtraffic_start: Literal["enable", "disable"] | None = ...,
        log_http_transaction: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        block_notification: Literal["enable", "disable"] | None = ...,
        redirect_url: str | None = ...,
        https_sub_category: Literal["enable", "disable"] | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        detect_https_in_http_request: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ProxyPolicyObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ProxyPolicyPayload | None = ...,
        uuid: str | None = ...,
        policyid: int | None = ...,
        name: str | None = ...,
        proxy: Literal["explicit-web", "transparent-web", "ftp", "ssh", "ssh-tunnel", "access-proxy", "ztna-proxy", "wanopt"] | None = ...,
        access_proxy: str | list[str] | list[dict[str, Any]] | None = ...,
        access_proxy6: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_proxy: str | list[str] | list[dict[str, Any]] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_tags_match_logic: Literal["or", "and"] | None = ...,
        device_ownership: Literal["enable", "disable"] | None = ...,
        url_risk: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        ztna_ems_tag_negate: Literal["enable", "disable"] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny", "redirect", "isolate"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        schedule: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        session_ttl: int | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        http_tunnel_auth: Literal["enable", "disable"] | None = ...,
        ssh_policy_redirect: Literal["enable", "disable"] | None = ...,
        webproxy_forward_server: str | None = ...,
        isolator_server: str | None = ...,
        webproxy_profile: str | None = ...,
        transparent: Literal["enable", "disable"] | None = ...,
        webcache: Literal["enable", "disable"] | None = ...,
        webcache_https: Literal["disable", "enable"] | None = ...,
        disclaimer: Literal["disable", "domain", "policy", "user"] | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
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
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        waf_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        replacemsg_override_group: str | None = ...,
        logtraffic_start: Literal["enable", "disable"] | None = ...,
        log_http_transaction: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        block_notification: Literal["enable", "disable"] | None = ...,
        redirect_url: str | None = ...,
        https_sub_category: Literal["enable", "disable"] | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        detect_https_in_http_request: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: ProxyPolicyPayload | None = ...,
        uuid: str | None = ...,
        policyid: int | None = ...,
        name: str | None = ...,
        proxy: Literal["explicit-web", "transparent-web", "ftp", "ssh", "ssh-tunnel", "access-proxy", "ztna-proxy", "wanopt"] | None = ...,
        access_proxy: str | list[str] | list[dict[str, Any]] | None = ...,
        access_proxy6: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_proxy: str | list[str] | list[dict[str, Any]] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_tags_match_logic: Literal["or", "and"] | None = ...,
        device_ownership: Literal["enable", "disable"] | None = ...,
        url_risk: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        ztna_ems_tag_negate: Literal["enable", "disable"] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny", "redirect", "isolate"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        schedule: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        session_ttl: int | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        http_tunnel_auth: Literal["enable", "disable"] | None = ...,
        ssh_policy_redirect: Literal["enable", "disable"] | None = ...,
        webproxy_forward_server: str | None = ...,
        isolator_server: str | None = ...,
        webproxy_profile: str | None = ...,
        transparent: Literal["enable", "disable"] | None = ...,
        webcache: Literal["enable", "disable"] | None = ...,
        webcache_https: Literal["disable", "enable"] | None = ...,
        disclaimer: Literal["disable", "domain", "policy", "user"] | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
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
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        waf_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        replacemsg_override_group: str | None = ...,
        logtraffic_start: Literal["enable", "disable"] | None = ...,
        log_http_transaction: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        block_notification: Literal["enable", "disable"] | None = ...,
        redirect_url: str | None = ...,
        https_sub_category: Literal["enable", "disable"] | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        detect_https_in_http_request: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: ProxyPolicyPayload | None = ...,
        uuid: str | None = ...,
        policyid: int | None = ...,
        name: str | None = ...,
        proxy: Literal["explicit-web", "transparent-web", "ftp", "ssh", "ssh-tunnel", "access-proxy", "ztna-proxy", "wanopt"] | None = ...,
        access_proxy: str | list[str] | list[dict[str, Any]] | None = ...,
        access_proxy6: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_proxy: str | list[str] | list[dict[str, Any]] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_tags_match_logic: Literal["or", "and"] | None = ...,
        device_ownership: Literal["enable", "disable"] | None = ...,
        url_risk: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        ztna_ems_tag_negate: Literal["enable", "disable"] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny", "redirect", "isolate"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        schedule: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        session_ttl: int | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        http_tunnel_auth: Literal["enable", "disable"] | None = ...,
        ssh_policy_redirect: Literal["enable", "disable"] | None = ...,
        webproxy_forward_server: str | None = ...,
        isolator_server: str | None = ...,
        webproxy_profile: str | None = ...,
        transparent: Literal["enable", "disable"] | None = ...,
        webcache: Literal["enable", "disable"] | None = ...,
        webcache_https: Literal["disable", "enable"] | None = ...,
        disclaimer: Literal["disable", "domain", "policy", "user"] | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
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
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        waf_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        replacemsg_override_group: str | None = ...,
        logtraffic_start: Literal["enable", "disable"] | None = ...,
        log_http_transaction: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        block_notification: Literal["enable", "disable"] | None = ...,
        redirect_url: str | None = ...,
        https_sub_category: Literal["enable", "disable"] | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        detect_https_in_http_request: Literal["enable", "disable"] | None = ...,
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
    ) -> ProxyPolicyObject: ...
    
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
        payload_dict: ProxyPolicyPayload | None = ...,
        uuid: str | None = ...,
        policyid: int | None = ...,
        name: str | None = ...,
        proxy: Literal["explicit-web", "transparent-web", "ftp", "ssh", "ssh-tunnel", "access-proxy", "ztna-proxy", "wanopt"] | None = ...,
        access_proxy: str | list[str] | list[dict[str, Any]] | None = ...,
        access_proxy6: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_proxy: str | list[str] | list[dict[str, Any]] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_tags_match_logic: Literal["or", "and"] | None = ...,
        device_ownership: Literal["enable", "disable"] | None = ...,
        url_risk: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        ztna_ems_tag_negate: Literal["enable", "disable"] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny", "redirect", "isolate"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        schedule: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        session_ttl: int | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        http_tunnel_auth: Literal["enable", "disable"] | None = ...,
        ssh_policy_redirect: Literal["enable", "disable"] | None = ...,
        webproxy_forward_server: str | None = ...,
        isolator_server: str | None = ...,
        webproxy_profile: str | None = ...,
        transparent: Literal["enable", "disable"] | None = ...,
        webcache: Literal["enable", "disable"] | None = ...,
        webcache_https: Literal["disable", "enable"] | None = ...,
        disclaimer: Literal["disable", "domain", "policy", "user"] | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
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
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        waf_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        replacemsg_override_group: str | None = ...,
        logtraffic_start: Literal["enable", "disable"] | None = ...,
        log_http_transaction: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        block_notification: Literal["enable", "disable"] | None = ...,
        redirect_url: str | None = ...,
        https_sub_category: Literal["enable", "disable"] | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        detect_https_in_http_request: Literal["enable", "disable"] | None = ...,
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
    "ProxyPolicy",
    "ProxyPolicyPayload",
    "ProxyPolicyObject",
]