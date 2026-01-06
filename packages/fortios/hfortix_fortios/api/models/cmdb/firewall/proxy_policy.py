"""
Pydantic Models for CMDB - firewall/proxy_policy

Runtime validation models for firewall/proxy_policy configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.firewall.proxy_policy import 
    >>>
    >>> # Create with validation
    >>> obj = (
    ...     policyid=1,
    ...     name="example",
    ... )
    >>>
    >>> # Validation happens automatically
    >>> # ValidationError raised if constraints violated
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum
from uuid import UUID

# ============================================================================
# Child Table Models
# ============================================================================

class ProxyPolicyAccessProxy(BaseModel):
    """
    Child table model for access-proxy.
    
    IPv4 access proxy.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Access Proxy name.")  # datasource: ['firewall.access-proxy.name']
class ProxyPolicyAccessProxy6(BaseModel):
    """
    Child table model for access-proxy6.
    
    IPv6 access proxy.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Access proxy name.")  # datasource: ['firewall.access-proxy6.name']
class ProxyPolicyZtnaProxy(BaseModel):
    """
    Child table model for ztna-proxy.
    
    ZTNA proxies.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="ZTNA proxy name.")  # datasource: ['ztna.traffic-forward-proxy.name', 'ztna.web-proxy.name', 'ztna.web-portal.name']
class ProxyPolicySrcintf(BaseModel):
    """
    Child table model for srcintf.
    
    Source interface names.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="Interface name.")  # datasource: ['system.interface.name', 'system.zone.name', 'system.sdwan.zone.name']
class ProxyPolicyDstintf(BaseModel):
    """
    Child table model for dstintf.
    
    Destination interface names.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="Interface name.")  # datasource: ['system.interface.name', 'system.zone.name', 'system.sdwan.zone.name']
class ProxyPolicySrcaddr(BaseModel):
    """
    Child table model for srcaddr.
    
    Source address objects.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name', 'firewall.proxy-address.name', 'firewall.proxy-addrgrp.name', 'system.external-resource.name']
class ProxyPolicyPoolname(BaseModel):
    """
    Child table model for poolname.
    
    Name of IP pool object.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="IP pool name.")  # datasource: ['firewall.ippool.name']
class ProxyPolicyPoolname6(BaseModel):
    """
    Child table model for poolname6.
    
    Name of IPv6 pool object.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="IPv6 pool name.")  # datasource: ['firewall.ippool6.name']
class ProxyPolicyDstaddr(BaseModel):
    """
    Child table model for dstaddr.
    
    Destination address objects.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name', 'firewall.proxy-address.name', 'firewall.proxy-addrgrp.name', 'firewall.vip.name', 'firewall.vipgrp.name', 'system.external-resource.name']
class ProxyPolicyZtnaEmsTag(BaseModel):
    """
    Child table model for ztna-ems-tag.
    
    ZTNA EMS Tag names.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="EMS Tag name.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name']
class ProxyPolicyUrlRisk(BaseModel):
    """
    Child table model for url-risk.
    
    URL risk level name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="Risk level name.")  # datasource: ['webfilter.ftgd-risk-level.name']
class ProxyPolicyInternetServiceName(BaseModel):
    """
    Child table model for internet-service-name.
    
    Internet Service name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="Internet Service name.")  # datasource: ['firewall.internet-service-name.name']
class ProxyPolicyInternetServiceGroup(BaseModel):
    """
    Child table model for internet-service-group.
    
    Internet Service group name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Internet Service group name.")  # datasource: ['firewall.internet-service-group.name']
class ProxyPolicyInternetServiceCustom(BaseModel):
    """
    Child table model for internet-service-custom.
    
    Custom Internet Service name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Custom Internet Service name.")  # datasource: ['firewall.internet-service-custom.name']
class ProxyPolicyInternetServiceCustomGroup(BaseModel):
    """
    Child table model for internet-service-custom-group.
    
    Custom Internet Service group name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Custom Internet Service group name.")  # datasource: ['firewall.internet-service-custom-group.name']
class ProxyPolicyInternetServiceFortiguard(BaseModel):
    """
    Child table model for internet-service-fortiguard.
    
    FortiGuard Internet Service name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="FortiGuard Internet Service name.")  # datasource: ['firewall.internet-service-fortiguard.name']
class ProxyPolicyInternetService6Name(BaseModel):
    """
    Child table model for internet-service6-name.
    
    Internet Service IPv6 name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="Internet Service IPv6 name.")  # datasource: ['firewall.internet-service-name.name']
class ProxyPolicyInternetService6Group(BaseModel):
    """
    Child table model for internet-service6-group.
    
    Internet Service IPv6 group name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Internet Service IPv6 group name.")  # datasource: ['firewall.internet-service-group.name']
class ProxyPolicyInternetService6Custom(BaseModel):
    """
    Child table model for internet-service6-custom.
    
    Custom Internet Service IPv6 name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Custom Internet Service IPv6 name.")  # datasource: ['firewall.internet-service-custom.name']
class ProxyPolicyInternetService6CustomGroup(BaseModel):
    """
    Child table model for internet-service6-custom-group.
    
    Custom Internet Service IPv6 group name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Custom Internet Service IPv6 group name.")  # datasource: ['firewall.internet-service-custom-group.name']
class ProxyPolicyInternetService6Fortiguard(BaseModel):
    """
    Child table model for internet-service6-fortiguard.
    
    FortiGuard Internet Service IPv6 name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="FortiGuard Internet Service IPv6 name.")  # datasource: ['firewall.internet-service-fortiguard.name']
class ProxyPolicyService(BaseModel):
    """
    Child table model for service.
    
    Name of service objects.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Service name.")  # datasource: ['firewall.service.custom.name', 'firewall.service.group.name']
class ProxyPolicySrcaddr6(BaseModel):
    """
    Child table model for srcaddr6.
    
    IPv6 source address objects.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address6.name', 'firewall.addrgrp6.name', 'system.external-resource.name']
class ProxyPolicyDstaddr6(BaseModel):
    """
    Child table model for dstaddr6.
    
    IPv6 destination address objects.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address6.name', 'firewall.addrgrp6.name', 'firewall.vip6.name', 'firewall.vipgrp6.name', 'system.external-resource.name']
class ProxyPolicyGroups(BaseModel):
    """
    Child table model for groups.
    
    Names of group objects.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Group name.")  # datasource: ['user.group.name']
class ProxyPolicyUsers(BaseModel):
    """
    Child table model for users.
    
    Names of user objects.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Group name.")  # datasource: ['user.local.name', 'user.certificate.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class ProxyPolicyProxyEnum(str, Enum):
    """Allowed values for proxy field."""
    EXPLICIT_WEB = "explicit-web"    TRANSPARENT_WEB = "transparent-web"    FTP = "ftp"    SSH = "ssh"    SSH_TUNNEL = "ssh-tunnel"    ACCESS_PROXY = "access-proxy"    ZTNA_PROXY = "ztna-proxy"    WANOPT = "wanopt"
class ProxyPolicyActionEnum(str, Enum):
    """Allowed values for action field."""
    ACCEPT = "accept"    DENY = "deny"    REDIRECT = "redirect"    ISOLATE = "isolate"
class ProxyPolicyDisclaimerEnum(str, Enum):
    """Allowed values for disclaimer field."""
    DISABLE = "disable"    DOMAIN = "domain"    POLICY = "policy"    USER = "user"

# ============================================================================
# Main Model
# ============================================================================

class ProxyPolicyModel(BaseModel):
    """
    Pydantic model for firewall/proxy_policy configuration.
    
    Configure proxy policies.
    
    Validation Rules:        - uuid: pattern=        - policyid: min=0 max=4294967295 pattern=        - name: max_length=35 pattern=        - proxy: pattern=        - access_proxy: pattern=        - access_proxy6: pattern=        - ztna_proxy: pattern=        - srcintf: pattern=        - dstintf: pattern=        - srcaddr: pattern=        - poolname: pattern=        - poolname6: pattern=        - dstaddr: pattern=        - ztna_ems_tag: pattern=        - ztna_tags_match_logic: pattern=        - device_ownership: pattern=        - url_risk: pattern=        - internet_service: pattern=        - internet_service_negate: pattern=        - internet_service_name: pattern=        - internet_service_group: pattern=        - internet_service_custom: pattern=        - internet_service_custom_group: pattern=        - internet_service_fortiguard: pattern=        - internet_service6: pattern=        - internet_service6_negate: pattern=        - internet_service6_name: pattern=        - internet_service6_group: pattern=        - internet_service6_custom: pattern=        - internet_service6_custom_group: pattern=        - internet_service6_fortiguard: pattern=        - service: pattern=        - srcaddr_negate: pattern=        - dstaddr_negate: pattern=        - ztna_ems_tag_negate: pattern=        - service_negate: pattern=        - action: pattern=        - status: pattern=        - schedule: max_length=35 pattern=        - logtraffic: pattern=        - session_ttl: min=300 max=2764800 pattern=        - srcaddr6: pattern=        - dstaddr6: pattern=        - groups: pattern=        - users: pattern=        - http_tunnel_auth: pattern=        - ssh_policy_redirect: pattern=        - webproxy_forward_server: max_length=63 pattern=        - isolator_server: max_length=63 pattern=        - webproxy_profile: max_length=63 pattern=        - transparent: pattern=        - webcache: pattern=        - webcache_https: pattern=        - disclaimer: pattern=        - utm_status: pattern=        - profile_type: pattern=        - profile_group: max_length=47 pattern=        - profile_protocol_options: max_length=47 pattern=        - ssl_ssh_profile: max_length=47 pattern=        - av_profile: max_length=47 pattern=        - webfilter_profile: max_length=47 pattern=        - dnsfilter_profile: max_length=47 pattern=        - emailfilter_profile: max_length=47 pattern=        - dlp_profile: max_length=47 pattern=        - file_filter_profile: max_length=47 pattern=        - ips_sensor: max_length=47 pattern=        - application_list: max_length=47 pattern=        - ips_voip_filter: max_length=47 pattern=        - sctp_filter_profile: max_length=47 pattern=        - icap_profile: max_length=47 pattern=        - videofilter_profile: max_length=47 pattern=        - waf_profile: max_length=47 pattern=        - ssh_filter_profile: max_length=47 pattern=        - casb_profile: max_length=47 pattern=        - replacemsg_override_group: max_length=35 pattern=        - logtraffic_start: pattern=        - log_http_transaction: pattern=        - comments: max_length=1023 pattern=        - block_notification: pattern=        - redirect_url: max_length=1023 pattern=        - https_sub_category: pattern=        - decrypted_traffic_mirror: max_length=35 pattern=        - detect_https_in_http_request: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    uuid: str | None = Field(default="00000000-0000-0000-0000-000000000000", description="Universally Unique Identifier (UUID; automatically assigned but can be manually reset).")    
    policyid: int | None = Field(ge=0, le=4294967295, default=0, description="Policy ID.")    
    name: str | None = Field(max_length=35, default="", description="Policy name.")    
    proxy: ProxyEnum = Field(default="", description="Type of explicit proxy.")    
    access_proxy: list[AccessProxy] = Field(default=None, description="IPv4 access proxy.")    
    access_proxy6: list[AccessProxy6] = Field(default=None, description="IPv6 access proxy.")    
    ztna_proxy: list[ZtnaProxy] = Field(default=None, description="ZTNA proxies.")    
    srcintf: list[Srcintf] = Field(description="Source interface names.")    
    dstintf: list[Dstintf] = Field(description="Destination interface names.")    
    srcaddr: list[Srcaddr] = Field(default=None, description="Source address objects.")    
    poolname: list[Poolname] = Field(default=None, description="Name of IP pool object.")    
    poolname6: list[Poolname6] = Field(default=None, description="Name of IPv6 pool object.")    
    dstaddr: list[Dstaddr] = Field(default=None, description="Destination address objects.")    
    ztna_ems_tag: list[ZtnaEmsTag] = Field(default=None, description="ZTNA EMS Tag names.")    
    ztna_tags_match_logic: Literal["or", "and"] | None = Field(default="or", description="ZTNA tag matching logic.")    
    device_ownership: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled, the ownership enforcement will be done at policy level.")    
    url_risk: list[UrlRisk] = Field(default=None, description="URL risk level name.")    
    internet_service: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable use of Internet Services for this policy. If enabled, destination address and service are not used.")    
    internet_service_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled, Internet Services match against any internet service EXCEPT the selected Internet Service.")    
    internet_service_name: list[InternetServiceName] = Field(default=None, description="Internet Service name.")    
    internet_service_group: list[InternetServiceGroup] = Field(default=None, description="Internet Service group name.")    
    internet_service_custom: list[InternetServiceCustom] = Field(default=None, description="Custom Internet Service name.")    
    internet_service_custom_group: list[InternetServiceCustomGroup] = Field(default=None, description="Custom Internet Service group name.")    
    internet_service_fortiguard: list[InternetServiceFortiguard] = Field(default=None, description="FortiGuard Internet Service name.")    
    internet_service6: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable use of Internet Services IPv6 for this policy. If enabled, destination IPv6 address and service are not used.")    
    internet_service6_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled, Internet Services match against any internet service IPv6 EXCEPT the selected Internet Service IPv6.")    
    internet_service6_name: list[InternetService6Name] = Field(default=None, description="Internet Service IPv6 name.")    
    internet_service6_group: list[InternetService6Group] = Field(default=None, description="Internet Service IPv6 group name.")    
    internet_service6_custom: list[InternetService6Custom] = Field(default=None, description="Custom Internet Service IPv6 name.")    
    internet_service6_custom_group: list[InternetService6CustomGroup] = Field(default=None, description="Custom Internet Service IPv6 group name.")    
    internet_service6_fortiguard: list[InternetService6Fortiguard] = Field(default=None, description="FortiGuard Internet Service IPv6 name.")    
    service: list[Service] = Field(default=None, description="Name of service objects.")    
    srcaddr_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled, source addresses match against any address EXCEPT the specified source addresses.")    
    dstaddr_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled, destination addresses match against any address EXCEPT the specified destination addresses.")    
    ztna_ems_tag_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled, ZTNA EMS tags match against any tag EXCEPT the specified ZTNA EMS tags.")    
    service_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled, services match against any service EXCEPT the specified destination services.")    
    action: ActionEnum | None = Field(default="deny", description="Accept or deny traffic matching the policy parameters.")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable the active status of the policy.")    
    schedule: str = Field(max_length=35, default="", description="Name of schedule object.")  # datasource: ['firewall.schedule.onetime.name', 'firewall.schedule.recurring.name', 'firewall.schedule.group.name']    
    logtraffic: Literal["all", "utm", "disable"] | None = Field(default="utm", description="Enable/disable logging traffic through the policy.")    
    session_ttl: int | None = Field(ge=300, le=2764800, default=0, description="TTL in seconds for sessions accepted by this policy (0 means use the system default session TTL).")    
    srcaddr6: list[Srcaddr6] = Field(default=None, description="IPv6 source address objects.")    
    dstaddr6: list[Dstaddr6] = Field(default=None, description="IPv6 destination address objects.")    
    groups: list[Groups] = Field(default=None, description="Names of group objects.")    
    users: list[Users] = Field(default=None, description="Names of user objects.")    
    http_tunnel_auth: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable HTTP tunnel authentication.")    
    ssh_policy_redirect: Literal["enable", "disable"] | None = Field(default="disable", description="Redirect SSH traffic to matching transparent proxy policy.")    
    webproxy_forward_server: str | None = Field(max_length=63, default="", description="Web proxy forward server name.")  # datasource: ['web-proxy.forward-server.name', 'web-proxy.forward-server-group.name']    
    isolator_server: str = Field(max_length=63, default="", description="Isolator server name.")  # datasource: ['web-proxy.isolator-server.name']    
    webproxy_profile: str | None = Field(max_length=63, default="", description="Name of web proxy profile.")  # datasource: ['web-proxy.profile.name']    
    transparent: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to use the IP address of the client to connect to the server.")    
    webcache: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable web caching.")    
    webcache_https: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable web caching for HTTPS (Requires deep-inspection enabled in ssl-ssh-profile).")    
    disclaimer: DisclaimerEnum | None = Field(default="disable", description="Web proxy disclaimer setting: by domain, policy, or user.")    
    utm_status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable the use of UTM profiles/sensors/lists.")    
    profile_type: Literal["single", "group"] | None = Field(default="single", description="Determine whether the firewall policy allows security profile groups or single profiles only.")    
    profile_group: str | None = Field(max_length=47, default="", description="Name of profile group.")  # datasource: ['firewall.profile-group.name']    
    profile_protocol_options: str | None = Field(max_length=47, default="default", description="Name of an existing Protocol options profile.")  # datasource: ['firewall.profile-protocol-options.name']    
    ssl_ssh_profile: str | None = Field(max_length=47, default="no-inspection", description="Name of an existing SSL SSH profile.")  # datasource: ['firewall.ssl-ssh-profile.name']    
    av_profile: str | None = Field(max_length=47, default="", description="Name of an existing Antivirus profile.")  # datasource: ['antivirus.profile.name']    
    webfilter_profile: str | None = Field(max_length=47, default="", description="Name of an existing Web filter profile.")  # datasource: ['webfilter.profile.name']    
    dnsfilter_profile: str | None = Field(max_length=47, default="", description="Name of an existing DNS filter profile.")  # datasource: ['dnsfilter.profile.name']    
    emailfilter_profile: str | None = Field(max_length=47, default="", description="Name of an existing email filter profile.")  # datasource: ['emailfilter.profile.name']    
    dlp_profile: str | None = Field(max_length=47, default="", description="Name of an existing DLP profile.")  # datasource: ['dlp.profile.name']    
    file_filter_profile: str | None = Field(max_length=47, default="", description="Name of an existing file-filter profile.")  # datasource: ['file-filter.profile.name']    
    ips_sensor: str | None = Field(max_length=47, default="", description="Name of an existing IPS sensor.")  # datasource: ['ips.sensor.name']    
    application_list: str | None = Field(max_length=47, default="", description="Name of an existing Application list.")  # datasource: ['application.list.name']    
    ips_voip_filter: str | None = Field(max_length=47, default="", description="Name of an existing VoIP (ips) profile.")  # datasource: ['voip.profile.name']    
    sctp_filter_profile: str | None = Field(max_length=47, default="", description="Name of an existing SCTP filter profile.")  # datasource: ['sctp-filter.profile.name']    
    icap_profile: str | None = Field(max_length=47, default="", description="Name of an existing ICAP profile.")  # datasource: ['icap.profile.name']    
    videofilter_profile: str | None = Field(max_length=47, default="", description="Name of an existing VideoFilter profile.")  # datasource: ['videofilter.profile.name']    
    waf_profile: str | None = Field(max_length=47, default="", description="Name of an existing Web application firewall profile.")  # datasource: ['waf.profile.name']    
    ssh_filter_profile: str | None = Field(max_length=47, default="", description="Name of an existing SSH filter profile.")  # datasource: ['ssh-filter.profile.name']    
    casb_profile: str | None = Field(max_length=47, default="", description="Name of an existing CASB profile.")  # datasource: ['casb.profile.name']    
    replacemsg_override_group: str | None = Field(max_length=35, default="", description="Authentication replacement message override group.")  # datasource: ['system.replacemsg-group.name']    
    logtraffic_start: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable policy log traffic start.")    
    log_http_transaction: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable HTTP transaction log.")    
    comments: str | None = Field(max_length=1023, default=None, description="Optional comments.")    
    block_notification: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable block notification.")    
    redirect_url: str | None = Field(max_length=1023, default=None, description="Redirect URL for further explicit web proxy processing.")    
    https_sub_category: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable HTTPS sub-category policy matching.")    
    decrypted_traffic_mirror: str | None = Field(max_length=35, default="", description="Decrypted traffic mirror.")  # datasource: ['firewall.decrypted-traffic-mirror.name']    
    detect_https_in_http_request: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable detection of HTTPS in HTTP request.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('schedule')
    @classmethod
    def validate_schedule(cls, v: Any) -> Any:
        """
        Validate schedule field.
        
        Datasource: ['firewall.schedule.onetime.name', 'firewall.schedule.recurring.name', 'firewall.schedule.group.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('webproxy_forward_server')
    @classmethod
    def validate_webproxy_forward_server(cls, v: Any) -> Any:
        """
        Validate webproxy_forward_server field.
        
        Datasource: ['web-proxy.forward-server.name', 'web-proxy.forward-server-group.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('isolator_server')
    @classmethod
    def validate_isolator_server(cls, v: Any) -> Any:
        """
        Validate isolator_server field.
        
        Datasource: ['web-proxy.isolator-server.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('webproxy_profile')
    @classmethod
    def validate_webproxy_profile(cls, v: Any) -> Any:
        """
        Validate webproxy_profile field.
        
        Datasource: ['web-proxy.profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('profile_group')
    @classmethod
    def validate_profile_group(cls, v: Any) -> Any:
        """
        Validate profile_group field.
        
        Datasource: ['firewall.profile-group.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('profile_protocol_options')
    @classmethod
    def validate_profile_protocol_options(cls, v: Any) -> Any:
        """
        Validate profile_protocol_options field.
        
        Datasource: ['firewall.profile-protocol-options.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('ssl_ssh_profile')
    @classmethod
    def validate_ssl_ssh_profile(cls, v: Any) -> Any:
        """
        Validate ssl_ssh_profile field.
        
        Datasource: ['firewall.ssl-ssh-profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('av_profile')
    @classmethod
    def validate_av_profile(cls, v: Any) -> Any:
        """
        Validate av_profile field.
        
        Datasource: ['antivirus.profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('webfilter_profile')
    @classmethod
    def validate_webfilter_profile(cls, v: Any) -> Any:
        """
        Validate webfilter_profile field.
        
        Datasource: ['webfilter.profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('dnsfilter_profile')
    @classmethod
    def validate_dnsfilter_profile(cls, v: Any) -> Any:
        """
        Validate dnsfilter_profile field.
        
        Datasource: ['dnsfilter.profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('emailfilter_profile')
    @classmethod
    def validate_emailfilter_profile(cls, v: Any) -> Any:
        """
        Validate emailfilter_profile field.
        
        Datasource: ['emailfilter.profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('dlp_profile')
    @classmethod
    def validate_dlp_profile(cls, v: Any) -> Any:
        """
        Validate dlp_profile field.
        
        Datasource: ['dlp.profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('file_filter_profile')
    @classmethod
    def validate_file_filter_profile(cls, v: Any) -> Any:
        """
        Validate file_filter_profile field.
        
        Datasource: ['file-filter.profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('ips_sensor')
    @classmethod
    def validate_ips_sensor(cls, v: Any) -> Any:
        """
        Validate ips_sensor field.
        
        Datasource: ['ips.sensor.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('application_list')
    @classmethod
    def validate_application_list(cls, v: Any) -> Any:
        """
        Validate application_list field.
        
        Datasource: ['application.list.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('ips_voip_filter')
    @classmethod
    def validate_ips_voip_filter(cls, v: Any) -> Any:
        """
        Validate ips_voip_filter field.
        
        Datasource: ['voip.profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('sctp_filter_profile')
    @classmethod
    def validate_sctp_filter_profile(cls, v: Any) -> Any:
        """
        Validate sctp_filter_profile field.
        
        Datasource: ['sctp-filter.profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('icap_profile')
    @classmethod
    def validate_icap_profile(cls, v: Any) -> Any:
        """
        Validate icap_profile field.
        
        Datasource: ['icap.profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('videofilter_profile')
    @classmethod
    def validate_videofilter_profile(cls, v: Any) -> Any:
        """
        Validate videofilter_profile field.
        
        Datasource: ['videofilter.profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('waf_profile')
    @classmethod
    def validate_waf_profile(cls, v: Any) -> Any:
        """
        Validate waf_profile field.
        
        Datasource: ['waf.profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('ssh_filter_profile')
    @classmethod
    def validate_ssh_filter_profile(cls, v: Any) -> Any:
        """
        Validate ssh_filter_profile field.
        
        Datasource: ['ssh-filter.profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('casb_profile')
    @classmethod
    def validate_casb_profile(cls, v: Any) -> Any:
        """
        Validate casb_profile field.
        
        Datasource: ['casb.profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('replacemsg_override_group')
    @classmethod
    def validate_replacemsg_override_group(cls, v: Any) -> Any:
        """
        Validate replacemsg_override_group field.
        
        Datasource: ['system.replacemsg-group.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('decrypted_traffic_mirror')
    @classmethod
    def validate_decrypted_traffic_mirror(cls, v: Any) -> Any:
        """
        Validate decrypted_traffic_mirror field.
        
        Datasource: ['firewall.decrypted-traffic-mirror.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    # ========================================================================
    # Helper Methods
    # ========================================================================
    
    def to_fortios_dict(self) -> dict[str, Any]:
        """
        Convert model to FortiOS API payload format.
        
        Returns:
            Dict suitable for POST/PUT operations
        """
        # Export with exclude_none to avoid sending null values
        return self.model_dump(exclude_none=True, by_alias=True)
    
    @classmethod
    def from_fortios_response(cls, data: dict[str, Any]) -> "":
        """
        Create model instance from FortiOS API response.
        
        Args:
            data: Response data from API
            
        Returns:
            Validated model instance
        """
        return cls(**data)


# ============================================================================
# Type Aliases for Convenience
# ============================================================================

Dict = dict[str, Any]  # For backward compatibility

# ============================================================================
# Module Exports
# ============================================================================

__all__ = [
    "ProxyPolicyModel",    "ProxyPolicyAccessProxy",    "ProxyPolicyAccessProxy6",    "ProxyPolicyZtnaProxy",    "ProxyPolicySrcintf",    "ProxyPolicyDstintf",    "ProxyPolicySrcaddr",    "ProxyPolicyPoolname",    "ProxyPolicyPoolname6",    "ProxyPolicyDstaddr",    "ProxyPolicyZtnaEmsTag",    "ProxyPolicyUrlRisk",    "ProxyPolicyInternetServiceName",    "ProxyPolicyInternetServiceGroup",    "ProxyPolicyInternetServiceCustom",    "ProxyPolicyInternetServiceCustomGroup",    "ProxyPolicyInternetServiceFortiguard",    "ProxyPolicyInternetService6Name",    "ProxyPolicyInternetService6Group",    "ProxyPolicyInternetService6Custom",    "ProxyPolicyInternetService6CustomGroup",    "ProxyPolicyInternetService6Fortiguard",    "ProxyPolicyService",    "ProxyPolicySrcaddr6",    "ProxyPolicyDstaddr6",    "ProxyPolicyGroups",    "ProxyPolicyUsers",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:34.470810Z
# ============================================================================