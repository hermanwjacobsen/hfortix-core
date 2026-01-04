from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class ProxyPolicyPayload(TypedDict, total=False):
    """
    Type hints for firewall/proxy_policy payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
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


class ProxyPolicy:
    """
    Configure proxy policies.
    
    Path: firewall/proxy_policy
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
        payload_dict: ProxyPolicyPayload | None = ...,
        uuid: str | None = ...,
        policyid: int | None = ...,
        name: str | None = ...,
        proxy: Literal["explicit-web", "transparent-web", "ftp", "ssh", "ssh-tunnel", "access-proxy", "ztna-proxy", "wanopt"] | None = ...,
        access_proxy: list[dict[str, Any]] | None = ...,
        access_proxy6: list[dict[str, Any]] | None = ...,
        ztna_proxy: list[dict[str, Any]] | None = ...,
        srcintf: list[dict[str, Any]] | None = ...,
        dstintf: list[dict[str, Any]] | None = ...,
        srcaddr: list[dict[str, Any]] | None = ...,
        poolname: list[dict[str, Any]] | None = ...,
        dstaddr: list[dict[str, Any]] | None = ...,
        ztna_ems_tag: list[dict[str, Any]] | None = ...,
        ztna_tags_match_logic: Literal["or", "and"] | None = ...,
        device_ownership: Literal["enable", "disable"] | None = ...,
        url_risk: list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_name: list[dict[str, Any]] | None = ...,
        internet_service_group: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: ProxyPolicyPayload | None = ...,
        uuid: str | None = ...,
        policyid: int | None = ...,
        name: str | None = ...,
        proxy: Literal["explicit-web", "transparent-web", "ftp", "ssh", "ssh-tunnel", "access-proxy", "ztna-proxy", "wanopt"] | None = ...,
        access_proxy: list[dict[str, Any]] | None = ...,
        access_proxy6: list[dict[str, Any]] | None = ...,
        ztna_proxy: list[dict[str, Any]] | None = ...,
        srcintf: list[dict[str, Any]] | None = ...,
        dstintf: list[dict[str, Any]] | None = ...,
        srcaddr: list[dict[str, Any]] | None = ...,
        poolname: list[dict[str, Any]] | None = ...,
        dstaddr: list[dict[str, Any]] | None = ...,
        ztna_ems_tag: list[dict[str, Any]] | None = ...,
        ztna_tags_match_logic: Literal["or", "and"] | None = ...,
        device_ownership: Literal["enable", "disable"] | None = ...,
        url_risk: list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_name: list[dict[str, Any]] | None = ...,
        internet_service_group: list[dict[str, Any]] | None = ...,
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
        payload_dict: ProxyPolicyPayload | None = ...,
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