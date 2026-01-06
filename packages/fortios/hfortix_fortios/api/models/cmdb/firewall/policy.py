"""
Pydantic Models for CMDB - firewall/policy

Runtime validation models for firewall/policy configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.firewall.policy import 
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
from uuid import UUID

# ============================================================================
# Child Table Models
# ============================================================================

class PolicySrcintf(BaseModel):
    """
    Child table model for srcintf.
    
    Incoming (ingress) interface.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="Interface name.")  # datasource: ['system.interface.name', 'system.zone.name', 'system.sdwan.zone.name']
class PolicyDstintf(BaseModel):
    """
    Child table model for dstintf.
    
    Outgoing (egress) interface.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="Interface name.")  # datasource: ['system.interface.name', 'system.zone.name', 'system.sdwan.zone.name']
class PolicySrcaddr(BaseModel):
    """
    Child table model for srcaddr.
    
    Source IPv4 address and address group names.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name', 'system.external-resource.name']
class PolicyDstaddr(BaseModel):
    """
    Child table model for dstaddr.
    
    Destination IPv4 address and address group names.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name', 'firewall.vip.name', 'firewall.vipgrp.name', 'system.external-resource.name']
class PolicySrcaddr6(BaseModel):
    """
    Child table model for srcaddr6.
    
    Source IPv6 address name and address group names.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address6.name', 'system.external-resource.name', 'firewall.addrgrp6.name']
class PolicyDstaddr6(BaseModel):
    """
    Child table model for dstaddr6.
    
    Destination IPv6 address name and address group names.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address6.name', 'firewall.addrgrp6.name', 'firewall.vip6.name', 'firewall.vipgrp6.name', 'system.external-resource.name']
class PolicyZtnaEmsTag(BaseModel):
    """
    Child table model for ztna-ems-tag.
    
    Source ztna-ems-tag names.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name']
class PolicyZtnaEmsTagSecondary(BaseModel):
    """
    Child table model for ztna-ems-tag-secondary.
    
    Source ztna-ems-tag-secondary names.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name']
class PolicyZtnaGeoTag(BaseModel):
    """
    Child table model for ztna-geo-tag.
    
    Source ztna-geo-tag names.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name']
class PolicyInternetServiceName(BaseModel):
    """
    Child table model for internet-service-name.
    
    Internet Service name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Internet Service name.")  # datasource: ['firewall.internet-service-name.name']
class PolicyInternetServiceGroup(BaseModel):
    """
    Child table model for internet-service-group.
    
    Internet Service group name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Internet Service group name.")  # datasource: ['firewall.internet-service-group.name']
class PolicyInternetServiceCustom(BaseModel):
    """
    Child table model for internet-service-custom.
    
    Custom Internet Service name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Custom Internet Service name.")  # datasource: ['firewall.internet-service-custom.name']
class PolicyNetworkServiceDynamic(BaseModel):
    """
    Child table model for network-service-dynamic.
    
    Dynamic Network Service name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Dynamic Network Service name.")  # datasource: ['firewall.network-service-dynamic.name']
class PolicyInternetServiceCustomGroup(BaseModel):
    """
    Child table model for internet-service-custom-group.
    
    Custom Internet Service group name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Custom Internet Service group name.")  # datasource: ['firewall.internet-service-custom-group.name']
class PolicyInternetServiceSrcName(BaseModel):
    """
    Child table model for internet-service-src-name.
    
    Internet Service source name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Internet Service name.")  # datasource: ['firewall.internet-service-name.name']
class PolicyInternetServiceSrcGroup(BaseModel):
    """
    Child table model for internet-service-src-group.
    
    Internet Service source group name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Internet Service group name.")  # datasource: ['firewall.internet-service-group.name']
class PolicyInternetServiceSrcCustom(BaseModel):
    """
    Child table model for internet-service-src-custom.
    
    Custom Internet Service source name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Custom Internet Service name.")  # datasource: ['firewall.internet-service-custom.name']
class PolicyNetworkServiceSrcDynamic(BaseModel):
    """
    Child table model for network-service-src-dynamic.
    
    Dynamic Network Service source name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Dynamic Network Service name.")  # datasource: ['firewall.network-service-dynamic.name']
class PolicyInternetServiceSrcCustomGroup(BaseModel):
    """
    Child table model for internet-service-src-custom-group.
    
    Custom Internet Service source group name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Custom Internet Service group name.")  # datasource: ['firewall.internet-service-custom-group.name']
class PolicySrcVendorMac(BaseModel):
    """
    Child table model for src-vendor-mac.
    
    Vendor MAC source ID.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=0, le=4294967295, default=0, description="Vendor MAC ID.")  # datasource: ['firewall.vendor-mac.id']
class PolicyInternetService6Name(BaseModel):
    """
    Child table model for internet-service6-name.
    
    IPv6 Internet Service name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="IPv6 Internet Service name.")  # datasource: ['firewall.internet-service-name.name']
class PolicyInternetService6Group(BaseModel):
    """
    Child table model for internet-service6-group.
    
    Internet Service group name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Internet Service group name.")  # datasource: ['firewall.internet-service-group.name']
class PolicyInternetService6Custom(BaseModel):
    """
    Child table model for internet-service6-custom.
    
    Custom IPv6 Internet Service name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Custom Internet Service name.")  # datasource: ['firewall.internet-service-custom.name']
class PolicyInternetService6CustomGroup(BaseModel):
    """
    Child table model for internet-service6-custom-group.
    
    Custom Internet Service6 group name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Custom Internet Service6 group name.")  # datasource: ['firewall.internet-service-custom-group.name']
class PolicyInternetService6SrcName(BaseModel):
    """
    Child table model for internet-service6-src-name.
    
    IPv6 Internet Service source name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Internet Service name.")  # datasource: ['firewall.internet-service-name.name']
class PolicyInternetService6SrcGroup(BaseModel):
    """
    Child table model for internet-service6-src-group.
    
    Internet Service6 source group name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Internet Service group name.")  # datasource: ['firewall.internet-service-group.name']
class PolicyInternetService6SrcCustom(BaseModel):
    """
    Child table model for internet-service6-src-custom.
    
    Custom IPv6 Internet Service source name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Custom Internet Service name.")  # datasource: ['firewall.internet-service-custom.name']
class PolicyInternetService6SrcCustomGroup(BaseModel):
    """
    Child table model for internet-service6-src-custom-group.
    
    Custom Internet Service6 source group name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Custom Internet Service6 group name.")  # datasource: ['firewall.internet-service-custom-group.name']
class PolicyRtpAddr(BaseModel):
    """
    Child table model for rtp-addr.
    
    Address names if this is an RTP NAT policy.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.internet-service-custom-group.name', 'firewall.addrgrp.name']
class PolicyService(BaseModel):
    """
    Child table model for service.
    
    Service and service group names.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Service and service group names.")  # datasource: ['firewall.service.custom.name', 'firewall.service.group.name']
class PolicyPcpPoolname(BaseModel):
    """
    Child table model for pcp-poolname.
    
    PCP pool names.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="PCP pool name.")  # datasource: ['system.pcp-server.pools.name']
class PolicyPoolname(BaseModel):
    """
    Child table model for poolname.
    
    IP Pool names.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="IP pool name.")  # datasource: ['firewall.ippool.name']
class PolicyPoolname6(BaseModel):
    """
    Child table model for poolname6.
    
    IPv6 pool names.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="IPv6 pool name.")  # datasource: ['firewall.ippool6.name']
class PolicyNtlmEnabledBrowsers(BaseModel):
    """
    Child table model for ntlm-enabled-browsers.
    
    HTTP-User-Agent value of supported browsers.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    user_agent_string: str | None = Field(max_length=79, default="", description="User agent string.")
class PolicyGroups(BaseModel):
    """
    Child table model for groups.
    
    Names of user groups that can authenticate with this policy.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="Group name.")  # datasource: ['user.group.name']
class PolicyUsers(BaseModel):
    """
    Child table model for users.
    
    Names of individual users that can authenticate with this policy.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Names of individual users that can authenticate with this policy.")  # datasource: ['user.local.name', 'user.certificate.name']
class PolicyFssoGroups(BaseModel):
    """
    Child table model for fsso-groups.
    
    Names of FSSO groups.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=511, default="", description="Names of FSSO groups.")  # datasource: ['user.adgrp.name']
class PolicyCustomLogFields(BaseModel):
    """
    Child table model for custom-log-fields.
    
    Custom fields to append to log messages for this policy.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    field_id: str | None = Field(max_length=35, default="", description="Custom log field.")  # datasource: ['log.custom-field.id']
class PolicySgt(BaseModel):
    """
    Child table model for sgt.
    
    Security group tags.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=1, le=65535, default=0, description="Security group tag (1 - 65535).")
class PolicyInternetServiceFortiguard(BaseModel):
    """
    Child table model for internet-service-fortiguard.
    
    FortiGuard Internet Service name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="FortiGuard Internet Service name.")  # datasource: ['firewall.internet-service-fortiguard.name']
class PolicyInternetServiceSrcFortiguard(BaseModel):
    """
    Child table model for internet-service-src-fortiguard.
    
    FortiGuard Internet Service source name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="FortiGuard Internet Service name.")  # datasource: ['firewall.internet-service-fortiguard.name']
class PolicyInternetService6Fortiguard(BaseModel):
    """
    Child table model for internet-service6-fortiguard.
    
    FortiGuard IPv6 Internet Service name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="FortiGuard Internet Service name.")  # datasource: ['firewall.internet-service-fortiguard.name']
class PolicyInternetService6SrcFortiguard(BaseModel):
    """
    Child table model for internet-service6-src-fortiguard.
    
    FortiGuard IPv6 Internet Service source name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="FortiGuard Internet Service name.")  # datasource: ['firewall.internet-service-fortiguard.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class PolicyModel(BaseModel):
    """
    Pydantic model for firewall/policy configuration.
    
    Configure IPv4/IPv6 policies.
    
    Validation Rules:        - policyid: min=0 max=4294967294 pattern=        - status: pattern=        - name: max_length=35 pattern=        - uuid: pattern=        - srcintf: pattern=        - dstintf: pattern=        - action: pattern=        - nat64: pattern=        - nat46: pattern=        - ztna_status: pattern=        - ztna_device_ownership: pattern=        - srcaddr: pattern=        - dstaddr: pattern=        - srcaddr6: pattern=        - dstaddr6: pattern=        - ztna_ems_tag: pattern=        - ztna_ems_tag_secondary: pattern=        - ztna_tags_match_logic: pattern=        - ztna_geo_tag: pattern=        - internet_service: pattern=        - internet_service_name: pattern=        - internet_service_group: pattern=        - internet_service_custom: pattern=        - network_service_dynamic: pattern=        - internet_service_custom_group: pattern=        - internet_service_src: pattern=        - internet_service_src_name: pattern=        - internet_service_src_group: pattern=        - internet_service_src_custom: pattern=        - network_service_src_dynamic: pattern=        - internet_service_src_custom_group: pattern=        - reputation_minimum: min=0 max=4294967295 pattern=        - reputation_direction: pattern=        - src_vendor_mac: pattern=        - internet_service6: pattern=        - internet_service6_name: pattern=        - internet_service6_group: pattern=        - internet_service6_custom: pattern=        - internet_service6_custom_group: pattern=        - internet_service6_src: pattern=        - internet_service6_src_name: pattern=        - internet_service6_src_group: pattern=        - internet_service6_src_custom: pattern=        - internet_service6_src_custom_group: pattern=        - reputation_minimum6: min=0 max=4294967295 pattern=        - reputation_direction6: pattern=        - rtp_nat: pattern=        - rtp_addr: pattern=        - send_deny_packet: pattern=        - firewall_session_dirty: pattern=        - schedule: max_length=35 pattern=        - schedule_timeout: pattern=        - policy_expiry: pattern=        - policy_expiry_date: pattern=        - policy_expiry_date_utc: pattern=        - service: pattern=        - tos_mask: pattern=        - tos: pattern=        - tos_negate: pattern=        - anti_replay: pattern=        - tcp_session_without_syn: pattern=        - geoip_anycast: pattern=        - geoip_match: pattern=        - dynamic_shaping: pattern=        - passive_wan_health_measurement: pattern=        - app_monitor: pattern=        - utm_status: pattern=        - inspection_mode: pattern=        - http_policy_redirect: pattern=        - ssh_policy_redirect: pattern=        - ztna_policy_redirect: pattern=        - webproxy_profile: max_length=63 pattern=        - profile_type: pattern=        - profile_group: max_length=47 pattern=        - profile_protocol_options: max_length=47 pattern=        - ssl_ssh_profile: max_length=47 pattern=        - av_profile: max_length=47 pattern=        - webfilter_profile: max_length=47 pattern=        - dnsfilter_profile: max_length=47 pattern=        - emailfilter_profile: max_length=47 pattern=        - dlp_profile: max_length=47 pattern=        - file_filter_profile: max_length=47 pattern=        - ips_sensor: max_length=47 pattern=        - application_list: max_length=47 pattern=        - voip_profile: max_length=47 pattern=        - ips_voip_filter: max_length=47 pattern=        - sctp_filter_profile: max_length=47 pattern=        - diameter_filter_profile: max_length=47 pattern=        - virtual_patch_profile: max_length=47 pattern=        - icap_profile: max_length=47 pattern=        - videofilter_profile: max_length=47 pattern=        - waf_profile: max_length=47 pattern=        - ssh_filter_profile: max_length=47 pattern=        - casb_profile: max_length=47 pattern=        - logtraffic: pattern=        - logtraffic_start: pattern=        - log_http_transaction: pattern=        - capture_packet: pattern=        - auto_asic_offload: pattern=        - wanopt: pattern=        - wanopt_detection: pattern=        - wanopt_passive_opt: pattern=        - wanopt_profile: max_length=35 pattern=        - wanopt_peer: max_length=35 pattern=        - webcache: pattern=        - webcache_https: pattern=        - webproxy_forward_server: max_length=63 pattern=        - traffic_shaper: max_length=35 pattern=        - traffic_shaper_reverse: max_length=35 pattern=        - per_ip_shaper: max_length=35 pattern=        - nat: pattern=        - pcp_outbound: pattern=        - pcp_inbound: pattern=        - pcp_poolname: pattern=        - permit_any_host: pattern=        - permit_stun_host: pattern=        - fixedport: pattern=        - port_preserve: pattern=        - port_random: pattern=        - ippool: pattern=        - poolname: pattern=        - poolname6: pattern=        - session_ttl: pattern=        - vlan_cos_fwd: min=0 max=7 pattern=        - vlan_cos_rev: min=0 max=7 pattern=        - inbound: pattern=        - outbound: pattern=        - natinbound: pattern=        - natoutbound: pattern=        - fec: pattern=        - wccp: pattern=        - ntlm: pattern=        - ntlm_guest: pattern=        - ntlm_enabled_browsers: pattern=        - fsso_agent_for_ntlm: max_length=35 pattern=        - groups: pattern=        - users: pattern=        - fsso_groups: pattern=        - auth_path: pattern=        - disclaimer: pattern=        - email_collect: pattern=        - vpntunnel: max_length=35 pattern=        - natip: pattern=        - match_vip: pattern=        - match_vip_only: pattern=        - diffserv_copy: pattern=        - diffserv_forward: pattern=        - diffserv_reverse: pattern=        - diffservcode_forward: pattern=        - diffservcode_rev: pattern=        - tcp_mss_sender: min=0 max=65535 pattern=        - tcp_mss_receiver: min=0 max=65535 pattern=        - comments: max_length=1023 pattern=        - auth_cert: max_length=35 pattern=        - auth_redirect_addr: max_length=63 pattern=        - redirect_url: max_length=1023 pattern=        - identity_based_route: max_length=35 pattern=        - block_notification: pattern=        - custom_log_fields: pattern=        - replacemsg_override_group: max_length=35 pattern=        - srcaddr_negate: pattern=        - srcaddr6_negate: pattern=        - dstaddr_negate: pattern=        - dstaddr6_negate: pattern=        - ztna_ems_tag_negate: pattern=        - service_negate: pattern=        - internet_service_negate: pattern=        - internet_service_src_negate: pattern=        - internet_service6_negate: pattern=        - internet_service6_src_negate: pattern=        - timeout_send_rst: pattern=        - captive_portal_exempt: pattern=        - decrypted_traffic_mirror: max_length=35 pattern=        - dsri: pattern=        - radius_mac_auth_bypass: pattern=        - radius_ip_auth_bypass: pattern=        - delay_tcp_npu_session: pattern=        - vlan_filter: pattern=        - sgt_check: pattern=        - sgt: pattern=        - internet_service_fortiguard: pattern=        - internet_service_src_fortiguard: pattern=        - internet_service6_fortiguard: pattern=        - internet_service6_src_fortiguard: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    policyid: int | None = Field(ge=0, le=4294967294, default=0, description="Policy ID (0 - 4294967294).")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable or disable this policy.")    
    name: str | None = Field(max_length=35, default="", description="Policy name.")    
    uuid: str | None = Field(default="00000000-0000-0000-0000-000000000000", description="Universally Unique Identifier (UUID; automatically assigned but can be manually reset).")    
    srcintf: list[Srcintf] = Field(description="Incoming (ingress) interface.")    
    dstintf: list[Dstintf] = Field(description="Outgoing (egress) interface.")    
    action: Literal["accept", "deny", "ipsec"] | None = Field(default="deny", description="Policy action (accept/deny/ipsec).")    
    nat64: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable NAT64.")    
    nat46: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable NAT46.")    
    ztna_status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable zero trust access.")    
    ztna_device_ownership: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable zero trust device ownership.")    
    srcaddr: list[Srcaddr] = Field(default=None, description="Source IPv4 address and address group names.")    
    dstaddr: list[Dstaddr] = Field(default=None, description="Destination IPv4 address and address group names.")    
    srcaddr6: list[Srcaddr6] = Field(default=None, description="Source IPv6 address name and address group names.")    
    dstaddr6: list[Dstaddr6] = Field(default=None, description="Destination IPv6 address name and address group names.")    
    ztna_ems_tag: list[ZtnaEmsTag] = Field(default=None, description="Source ztna-ems-tag names.")    
    ztna_ems_tag_secondary: list[ZtnaEmsTagSecondary] = Field(default=None, description="Source ztna-ems-tag-secondary names.")    
    ztna_tags_match_logic: Literal["or", "and"] | None = Field(default="or", description="ZTNA tag matching logic.")    
    ztna_geo_tag: list[ZtnaGeoTag] = Field(default=None, description="Source ztna-geo-tag names.")    
    internet_service: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable use of Internet Services for this policy. If enabled, destination address and service are not used.")    
    internet_service_name: list[InternetServiceName] = Field(default=None, description="Internet Service name.")    
    internet_service_group: list[InternetServiceGroup] = Field(default=None, description="Internet Service group name.")    
    internet_service_custom: list[InternetServiceCustom] = Field(default=None, description="Custom Internet Service name.")    
    network_service_dynamic: list[NetworkServiceDynamic] = Field(default=None, description="Dynamic Network Service name.")    
    internet_service_custom_group: list[InternetServiceCustomGroup] = Field(default=None, description="Custom Internet Service group name.")    
    internet_service_src: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable use of Internet Services in source for this policy. If enabled, source address is not used.")    
    internet_service_src_name: list[InternetServiceSrcName] = Field(default=None, description="Internet Service source name.")    
    internet_service_src_group: list[InternetServiceSrcGroup] = Field(default=None, description="Internet Service source group name.")    
    internet_service_src_custom: list[InternetServiceSrcCustom] = Field(default=None, description="Custom Internet Service source name.")    
    network_service_src_dynamic: list[NetworkServiceSrcDynamic] = Field(default=None, description="Dynamic Network Service source name.")    
    internet_service_src_custom_group: list[InternetServiceSrcCustomGroup] = Field(default=None, description="Custom Internet Service source group name.")    
    reputation_minimum: int | None = Field(ge=0, le=4294967295, default=0, description="Minimum Reputation to take action.")  # datasource: ['firewall.internet-service-reputation.id']    
    reputation_direction: Literal["source", "destination"] | None = Field(default="destination", description="Direction of the initial traffic for reputation to take effect.")    
    src_vendor_mac: list[SrcVendorMac] = Field(default=None, description="Vendor MAC source ID.")    
    internet_service6: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable use of IPv6 Internet Services for this policy. If enabled, destination address and service are not used.")    
    internet_service6_name: list[InternetService6Name] = Field(default=None, description="IPv6 Internet Service name.")    
    internet_service6_group: list[InternetService6Group] = Field(default=None, description="Internet Service group name.")    
    internet_service6_custom: list[InternetService6Custom] = Field(default=None, description="Custom IPv6 Internet Service name.")    
    internet_service6_custom_group: list[InternetService6CustomGroup] = Field(default=None, description="Custom Internet Service6 group name.")    
    internet_service6_src: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable use of IPv6 Internet Services in source for this policy. If enabled, source address is not used.")    
    internet_service6_src_name: list[InternetService6SrcName] = Field(default=None, description="IPv6 Internet Service source name.")    
    internet_service6_src_group: list[InternetService6SrcGroup] = Field(default=None, description="Internet Service6 source group name.")    
    internet_service6_src_custom: list[InternetService6SrcCustom] = Field(default=None, description="Custom IPv6 Internet Service source name.")    
    internet_service6_src_custom_group: list[InternetService6SrcCustomGroup] = Field(default=None, description="Custom Internet Service6 source group name.")    
    reputation_minimum6: int | None = Field(ge=0, le=4294967295, default=0, description="IPv6 Minimum Reputation to take action.")  # datasource: ['firewall.internet-service-reputation.id']    
    reputation_direction6: Literal["source", "destination"] | None = Field(default="destination", description="Direction of the initial traffic for IPv6 reputation to take effect.")    
    rtp_nat: Literal["disable", "enable"] | None = Field(default="disable", description="Enable Real Time Protocol (RTP) NAT.")    
    rtp_addr: list[RtpAddr] = Field(description="Address names if this is an RTP NAT policy.")    
    send_deny_packet: Literal["disable", "enable"] | None = Field(default="disable", description="Enable to send a reply when a session is denied or blocked by a firewall policy.")    
    firewall_session_dirty: Literal["check-all", "check-new"] | None = Field(default="check-all", description="How to handle sessions if the configuration of this firewall policy changes.")    
    schedule: str = Field(max_length=35, default="", description="Schedule name.")  # datasource: ['firewall.schedule.onetime.name', 'firewall.schedule.recurring.name', 'firewall.schedule.group.name']    
    schedule_timeout: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to force current sessions to end when the schedule object times out. Disable allows them to end from inactivity.")    
    policy_expiry: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable policy expiry.")    
    policy_expiry_date: Any = Field(default="0000-00-00 00:00:00", description="Policy expiry date (YYYY-MM-DD HH:MM:SS).")    
    policy_expiry_date_utc: str | None = Field(default="", description="Policy expiry date and time, in epoch format.")    
    service: list[Service] = Field(default=None, description="Service and service group names.")    
    tos_mask: str | None = Field(default="", description="Non-zero bit positions are used for comparison while zero bit positions are ignored.")    
    tos: str | None = Field(default="", description="ToS (Type of Service) value used for comparison.")    
    tos_negate: Literal["enable", "disable"] | None = Field(default="disable", description="Enable negated TOS match.")    
    anti_replay: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable anti-replay check.")    
    tcp_session_without_syn: Literal["all", "data-only", "disable"] | None = Field(default="disable", description="Enable/disable creation of TCP session without SYN flag.")    
    geoip_anycast: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable recognition of anycast IP addresses using the geography IP database.")    
    geoip_match: Literal["physical-location", "registered-location"] | None = Field(default="physical-location", description="Match geography address based either on its physical location or registered location.")    
    dynamic_shaping: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable dynamic RADIUS defined traffic shaping.")    
    passive_wan_health_measurement: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable passive WAN health measurement. When enabled, auto-asic-offload is disabled.")    
    app_monitor: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable application TCP metrics in session logs.When enabled, auto-asic-offload is disabled.")    
    utm_status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to add one or more security profiles (AV, IPS, etc.) to the firewall policy.")    
    inspection_mode: Literal["proxy", "flow"] | None = Field(default="flow", description="Policy inspection mode (Flow/proxy). Default is Flow mode.")    
    http_policy_redirect: Literal["enable", "disable", "legacy"] | None = Field(default="disable", description="Redirect HTTP(S) traffic to matching transparent web proxy policy.")    
    ssh_policy_redirect: Literal["enable", "disable"] | None = Field(default="disable", description="Redirect SSH traffic to matching transparent proxy policy.")    
    ztna_policy_redirect: Literal["enable", "disable"] | None = Field(default="disable", description="Redirect ZTNA traffic to matching Access-Proxy proxy-policy.")    
    webproxy_profile: str | None = Field(max_length=63, default="", description="Webproxy profile name.")  # datasource: ['web-proxy.profile.name']    
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
    voip_profile: str | None = Field(max_length=47, default="", description="Name of an existing VoIP (voipd) profile.")  # datasource: ['voip.profile.name']    
    ips_voip_filter: str | None = Field(max_length=47, default="", description="Name of an existing VoIP (ips) profile.")  # datasource: ['voip.profile.name']    
    sctp_filter_profile: str | None = Field(max_length=47, default="", description="Name of an existing SCTP filter profile.")  # datasource: ['sctp-filter.profile.name']    
    diameter_filter_profile: str | None = Field(max_length=47, default="", description="Name of an existing Diameter filter profile.")  # datasource: ['diameter-filter.profile.name']    
    virtual_patch_profile: str | None = Field(max_length=47, default="", description="Name of an existing virtual-patch profile.")  # datasource: ['virtual-patch.profile.name']    
    icap_profile: str | None = Field(max_length=47, default="", description="Name of an existing ICAP profile.")  # datasource: ['icap.profile.name']    
    videofilter_profile: str | None = Field(max_length=47, default="", description="Name of an existing VideoFilter profile.")  # datasource: ['videofilter.profile.name']    
    waf_profile: str | None = Field(max_length=47, default="", description="Name of an existing Web application firewall profile.")  # datasource: ['waf.profile.name']    
    ssh_filter_profile: str | None = Field(max_length=47, default="", description="Name of an existing SSH filter profile.")  # datasource: ['ssh-filter.profile.name']    
    casb_profile: str | None = Field(max_length=47, default="", description="Name of an existing CASB profile.")  # datasource: ['casb.profile.name']    
    logtraffic: Literal["all", "utm", "disable"] | None = Field(default="utm", description="Enable or disable logging. Log all sessions or security profile sessions.")    
    logtraffic_start: Literal["enable", "disable"] | None = Field(default="disable", description="Record logs when a session starts.")    
    log_http_transaction: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable HTTP transaction log.")    
    capture_packet: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable capture packets.")    
    auto_asic_offload: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable policy traffic ASIC offloading.")    
    wanopt: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable WAN optimization.")    
    wanopt_detection: Literal["active", "passive", "off"] | None = Field(default="active", description="WAN optimization auto-detection mode.")    
    wanopt_passive_opt: Literal["default", "transparent", "non-transparent"] | None = Field(default="default", description="WAN optimization passive mode options. This option decides what IP address will be used to connect server.")    
    wanopt_profile: str = Field(max_length=35, default="", description="WAN optimization profile.")  # datasource: ['wanopt.profile.name']    
    wanopt_peer: str = Field(max_length=35, default="", description="WAN optimization peer.")  # datasource: ['wanopt.peer.peer-host-id']    
    webcache: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable web cache.")    
    webcache_https: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable web cache for HTTPS.")    
    webproxy_forward_server: str | None = Field(max_length=63, default="", description="Webproxy forward server name.")  # datasource: ['web-proxy.forward-server.name', 'web-proxy.forward-server-group.name']    
    traffic_shaper: str | None = Field(max_length=35, default="", description="Traffic shaper.")  # datasource: ['firewall.shaper.traffic-shaper.name']    
    traffic_shaper_reverse: str | None = Field(max_length=35, default="", description="Reverse traffic shaper.")  # datasource: ['firewall.shaper.traffic-shaper.name']    
    per_ip_shaper: str | None = Field(max_length=35, default="", description="Per-IP traffic shaper.")  # datasource: ['firewall.shaper.per-ip-shaper.name']    
    nat: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable source NAT.")    
    pcp_outbound: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable PCP outbound SNAT.")    
    pcp_inbound: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable PCP inbound DNAT.")    
    pcp_poolname: list[PcpPoolname] = Field(default=None, description="PCP pool names.")    
    permit_any_host: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable fullcone NAT. Accept UDP packets from any host.")    
    permit_stun_host: Literal["enable", "disable"] | None = Field(default="disable", description="Accept UDP packets from any Session Traversal Utilities for NAT (STUN) host.")    
    fixedport: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to prevent source NAT from changing a session's source port.")    
    port_preserve: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable preservation of the original source port from source NAT if it has not been used.")    
    port_random: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable random source port selection for source NAT.")    
    ippool: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to use IP Pools for source NAT.")    
    poolname: list[Poolname] = Field(default=None, description="IP Pool names.")    
    poolname6: list[Poolname6] = Field(default=None, description="IPv6 pool names.")    
    session_ttl: str | None = Field(default="", description="TTL in seconds for sessions accepted by this policy (0 means use the system default session TTL).")    
    vlan_cos_fwd: int | None = Field(ge=0, le=7, default=255, description="VLAN forward direction user priority: 255 passthrough, 0 lowest, 7 highest.")    
    vlan_cos_rev: int | None = Field(ge=0, le=7, default=255, description="VLAN reverse direction user priority: 255 passthrough, 0 lowest, 7 highest.")    
    inbound: Literal["enable", "disable"] | None = Field(default="disable", description="Policy-based IPsec VPN: only traffic from the remote network can initiate a VPN.")    
    outbound: Literal["enable", "disable"] | None = Field(default="enable", description="Policy-based IPsec VPN: only traffic from the internal network can initiate a VPN.")    
    natinbound: Literal["enable", "disable"] | None = Field(default="disable", description="Policy-based IPsec VPN: apply destination NAT to inbound traffic.")    
    natoutbound: Literal["enable", "disable"] | None = Field(default="disable", description="Policy-based IPsec VPN: apply source NAT to outbound traffic.")    
    fec: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable Forward Error Correction on traffic matching this policy on a FEC device.")    
    wccp: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable forwarding traffic matching this policy to a configured WCCP server.")    
    ntlm: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable NTLM authentication.")    
    ntlm_guest: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable NTLM guest user access.")    
    ntlm_enabled_browsers: list[NtlmEnabledBrowsers] = Field(default=None, description="HTTP-User-Agent value of supported browsers.")    
    fsso_agent_for_ntlm: str | None = Field(max_length=35, default="", description="FSSO agent to use for NTLM authentication.")  # datasource: ['user.fsso.name']    
    groups: list[Groups] = Field(default=None, description="Names of user groups that can authenticate with this policy.")    
    users: list[Users] = Field(default=None, description="Names of individual users that can authenticate with this policy.")    
    fsso_groups: list[FssoGroups] = Field(default=None, description="Names of FSSO groups.")    
    auth_path: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable authentication-based routing.")    
    disclaimer: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable user authentication disclaimer.")    
    email_collect: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable email collection.")    
    vpntunnel: str = Field(max_length=35, default="", description="Policy-based IPsec VPN: name of the IPsec VPN Phase 1.")  # datasource: ['vpn.ipsec.phase1.name', 'vpn.ipsec.manualkey.name']    
    natip: str | None = Field(default="0.0.0.0 0.0.0.0", description="Policy-based IPsec VPN: source NAT IP address for outgoing traffic.")    
    match_vip: Literal["enable", "disable"] | None = Field(default="enable", description="Enable to match packets that have had their destination addresses changed by a VIP.")    
    match_vip_only: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable matching of only those packets that have had their destination addresses changed by a VIP.")    
    diffserv_copy: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to copy packet's DiffServ values from session's original direction to its reply direction.")    
    diffserv_forward: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to change packet's DiffServ values to the specified diffservcode-forward value.")    
    diffserv_reverse: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to change packet's reverse (reply) DiffServ values to the specified diffservcode-rev value.")    
    diffservcode_forward: str | None = Field(default="", description="Change packet's DiffServ to this value.")    
    diffservcode_rev: str | None = Field(default="", description="Change packet's reverse (reply) DiffServ to this value.")    
    tcp_mss_sender: int | None = Field(ge=0, le=65535, default=0, description="Sender TCP maximum segment size (MSS).")    
    tcp_mss_receiver: int | None = Field(ge=0, le=65535, default=0, description="Receiver TCP maximum segment size (MSS).")    
    comments: str | None = Field(max_length=1023, default=None, description="Comment.")    
    auth_cert: str | None = Field(max_length=35, default="", description="HTTPS server certificate for policy authentication.")  # datasource: ['vpn.certificate.local.name']    
    auth_redirect_addr: str | None = Field(max_length=63, default="", description="HTTP-to-HTTPS redirect address for firewall authentication.")    
    redirect_url: str | None = Field(max_length=1023, default=None, description="URL users are directed to after seeing and accepting the disclaimer or authenticating.")    
    identity_based_route: str | None = Field(max_length=35, default="", description="Name of identity-based routing rule.")  # datasource: ['firewall.identity-based-route.name']    
    block_notification: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable block notification.")    
    custom_log_fields: list[CustomLogFields] = Field(default=None, description="Custom fields to append to log messages for this policy.")    
    replacemsg_override_group: str | None = Field(max_length=35, default="", description="Override the default replacement message group for this policy.")  # datasource: ['system.replacemsg-group.name']    
    srcaddr_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled srcaddr specifies what the source address must NOT be.")    
    srcaddr6_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled srcaddr6 specifies what the source address must NOT be.")    
    dstaddr_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled dstaddr specifies what the destination address must NOT be.")    
    dstaddr6_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled dstaddr6 specifies what the destination address must NOT be.")    
    ztna_ems_tag_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled ztna-ems-tag specifies what the tags must NOT be.")    
    service_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled service specifies what the service must NOT be.")    
    internet_service_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled internet-service specifies what the service must NOT be.")    
    internet_service_src_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled internet-service-src specifies what the service must NOT be.")    
    internet_service6_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled internet-service6 specifies what the service must NOT be.")    
    internet_service6_src_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled internet-service6-src specifies what the service must NOT be.")    
    timeout_send_rst: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable sending RST packets when TCP sessions expire.")    
    captive_portal_exempt: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to exempt some users from the captive portal.")    
    decrypted_traffic_mirror: str | None = Field(max_length=35, default="", description="Decrypted traffic mirror.")  # datasource: ['firewall.decrypted-traffic-mirror.name']    
    dsri: Literal["enable", "disable"] | None = Field(default="disable", description="Enable DSRI to ignore HTTP server responses.")    
    radius_mac_auth_bypass: Literal["enable", "disable"] | None = Field(default="disable", description="Enable MAC authentication bypass. The bypassed MAC address must be received from RADIUS server.")    
    radius_ip_auth_bypass: Literal["enable", "disable"] | None = Field(default="disable", description="Enable IP authentication bypass. The bypassed IP address must be received from RADIUS server.")    
    delay_tcp_npu_session: Literal["enable", "disable"] | None = Field(default="disable", description="Enable TCP NPU session delay to guarantee packet order of 3-way handshake.")    
    vlan_filter: str | None = Field(default="", description="VLAN ranges to allow")    
    sgt_check: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable security group tags (SGT) check.")    
    sgt: list[Sgt] = Field(default=None, description="Security group tags.")    
    internet_service_fortiguard: list[InternetServiceFortiguard] = Field(default=None, description="FortiGuard Internet Service name.")    
    internet_service_src_fortiguard: list[InternetServiceSrcFortiguard] = Field(default=None, description="FortiGuard Internet Service source name.")    
    internet_service6_fortiguard: list[InternetService6Fortiguard] = Field(default=None, description="FortiGuard IPv6 Internet Service name.")    
    internet_service6_src_fortiguard: list[InternetService6SrcFortiguard] = Field(default=None, description="FortiGuard IPv6 Internet Service source name.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('reputation_minimum')
    @classmethod
    def validate_reputation_minimum(cls, v: Any) -> Any:
        """
        Validate reputation_minimum field.
        
        Datasource: ['firewall.internet-service-reputation.id']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('reputation_minimum6')
    @classmethod
    def validate_reputation_minimum6(cls, v: Any) -> Any:
        """
        Validate reputation_minimum6 field.
        
        Datasource: ['firewall.internet-service-reputation.id']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
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
    @field_validator('voip_profile')
    @classmethod
    def validate_voip_profile(cls, v: Any) -> Any:
        """
        Validate voip_profile field.
        
        Datasource: ['voip.profile.name']
        
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
    @field_validator('diameter_filter_profile')
    @classmethod
    def validate_diameter_filter_profile(cls, v: Any) -> Any:
        """
        Validate diameter_filter_profile field.
        
        Datasource: ['diameter-filter.profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('virtual_patch_profile')
    @classmethod
    def validate_virtual_patch_profile(cls, v: Any) -> Any:
        """
        Validate virtual_patch_profile field.
        
        Datasource: ['virtual-patch.profile.name']
        
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
    @field_validator('wanopt_profile')
    @classmethod
    def validate_wanopt_profile(cls, v: Any) -> Any:
        """
        Validate wanopt_profile field.
        
        Datasource: ['wanopt.profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('wanopt_peer')
    @classmethod
    def validate_wanopt_peer(cls, v: Any) -> Any:
        """
        Validate wanopt_peer field.
        
        Datasource: ['wanopt.peer.peer-host-id']
        
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
    @field_validator('traffic_shaper')
    @classmethod
    def validate_traffic_shaper(cls, v: Any) -> Any:
        """
        Validate traffic_shaper field.
        
        Datasource: ['firewall.shaper.traffic-shaper.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('traffic_shaper_reverse')
    @classmethod
    def validate_traffic_shaper_reverse(cls, v: Any) -> Any:
        """
        Validate traffic_shaper_reverse field.
        
        Datasource: ['firewall.shaper.traffic-shaper.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('per_ip_shaper')
    @classmethod
    def validate_per_ip_shaper(cls, v: Any) -> Any:
        """
        Validate per_ip_shaper field.
        
        Datasource: ['firewall.shaper.per-ip-shaper.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('fsso_agent_for_ntlm')
    @classmethod
    def validate_fsso_agent_for_ntlm(cls, v: Any) -> Any:
        """
        Validate fsso_agent_for_ntlm field.
        
        Datasource: ['user.fsso.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('vpntunnel')
    @classmethod
    def validate_vpntunnel(cls, v: Any) -> Any:
        """
        Validate vpntunnel field.
        
        Datasource: ['vpn.ipsec.phase1.name', 'vpn.ipsec.manualkey.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('auth_cert')
    @classmethod
    def validate_auth_cert(cls, v: Any) -> Any:
        """
        Validate auth_cert field.
        
        Datasource: ['vpn.certificate.local.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('identity_based_route')
    @classmethod
    def validate_identity_based_route(cls, v: Any) -> Any:
        """
        Validate identity_based_route field.
        
        Datasource: ['firewall.identity-based-route.name']
        
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
    "PolicyModel",    "PolicySrcintf",    "PolicyDstintf",    "PolicySrcaddr",    "PolicyDstaddr",    "PolicySrcaddr6",    "PolicyDstaddr6",    "PolicyZtnaEmsTag",    "PolicyZtnaEmsTagSecondary",    "PolicyZtnaGeoTag",    "PolicyInternetServiceName",    "PolicyInternetServiceGroup",    "PolicyInternetServiceCustom",    "PolicyNetworkServiceDynamic",    "PolicyInternetServiceCustomGroup",    "PolicyInternetServiceSrcName",    "PolicyInternetServiceSrcGroup",    "PolicyInternetServiceSrcCustom",    "PolicyNetworkServiceSrcDynamic",    "PolicyInternetServiceSrcCustomGroup",    "PolicySrcVendorMac",    "PolicyInternetService6Name",    "PolicyInternetService6Group",    "PolicyInternetService6Custom",    "PolicyInternetService6CustomGroup",    "PolicyInternetService6SrcName",    "PolicyInternetService6SrcGroup",    "PolicyInternetService6SrcCustom",    "PolicyInternetService6SrcCustomGroup",    "PolicyRtpAddr",    "PolicyService",    "PolicyPcpPoolname",    "PolicyPoolname",    "PolicyPoolname6",    "PolicyNtlmEnabledBrowsers",    "PolicyGroups",    "PolicyUsers",    "PolicyFssoGroups",    "PolicyCustomLogFields",    "PolicySgt",    "PolicyInternetServiceFortiguard",    "PolicyInternetServiceSrcFortiguard",    "PolicyInternetService6Fortiguard",    "PolicyInternetService6SrcFortiguard",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:17:15.599407Z
# ============================================================================