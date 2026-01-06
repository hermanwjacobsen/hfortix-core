"""
Pydantic Models for CMDB - firewall/security_policy

Runtime validation models for firewall/security_policy configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.firewall.security_policy import 
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

class SecurityPolicySrcintf(BaseModel):
    """
    Child table model for srcintf.
    
    Incoming (ingress) interface.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="Interface name.")  # datasource: ['system.interface.name', 'system.zone.name', 'system.sdwan.zone.name']
class SecurityPolicyDstintf(BaseModel):
    """
    Child table model for dstintf.
    
    Outgoing (egress) interface.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="Interface name.")  # datasource: ['system.interface.name', 'system.zone.name', 'system.sdwan.zone.name']
class SecurityPolicySrcaddr(BaseModel):
    """
    Child table model for srcaddr.
    
    Source IPv4 address name and address group names.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name', 'system.external-resource.name']
class SecurityPolicyDstaddr(BaseModel):
    """
    Child table model for dstaddr.
    
    Destination IPv4 address name and address group names.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name', 'firewall.vip.name', 'firewall.vipgrp.name', 'system.external-resource.name']
class SecurityPolicySrcaddr6(BaseModel):
    """
    Child table model for srcaddr6.
    
    Source IPv6 address name and address group names.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address6.name', 'firewall.addrgrp6.name', 'system.external-resource.name']
class SecurityPolicyDstaddr6(BaseModel):
    """
    Child table model for dstaddr6.
    
    Destination IPv6 address name and address group names.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address6.name', 'firewall.addrgrp6.name', 'firewall.vip6.name', 'firewall.vipgrp6.name', 'system.external-resource.name']
class SecurityPolicyInternetServiceName(BaseModel):
    """
    Child table model for internet-service-name.
    
    Internet Service name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Internet Service name.")  # datasource: ['firewall.internet-service-name.name']
class SecurityPolicyInternetServiceGroup(BaseModel):
    """
    Child table model for internet-service-group.
    
    Internet Service group name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Internet Service group name.")  # datasource: ['firewall.internet-service-group.name']
class SecurityPolicyInternetServiceCustom(BaseModel):
    """
    Child table model for internet-service-custom.
    
    Custom Internet Service name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Custom Internet Service name.")  # datasource: ['firewall.internet-service-custom.name']
class SecurityPolicyInternetServiceCustomGroup(BaseModel):
    """
    Child table model for internet-service-custom-group.
    
    Custom Internet Service group name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Custom Internet Service group name.")  # datasource: ['firewall.internet-service-custom-group.name']
class SecurityPolicyInternetServiceFortiguard(BaseModel):
    """
    Child table model for internet-service-fortiguard.
    
    FortiGuard Internet Service name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="FortiGuard Internet Service name.")  # datasource: ['firewall.internet-service-fortiguard.name']
class SecurityPolicyInternetServiceSrcName(BaseModel):
    """
    Child table model for internet-service-src-name.
    
    Internet Service source name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Internet Service name.")  # datasource: ['firewall.internet-service-name.name']
class SecurityPolicyInternetServiceSrcGroup(BaseModel):
    """
    Child table model for internet-service-src-group.
    
    Internet Service source group name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Internet Service group name.")  # datasource: ['firewall.internet-service-group.name']
class SecurityPolicyInternetServiceSrcCustom(BaseModel):
    """
    Child table model for internet-service-src-custom.
    
    Custom Internet Service source name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Custom Internet Service name.")  # datasource: ['firewall.internet-service-custom.name']
class SecurityPolicyInternetServiceSrcCustomGroup(BaseModel):
    """
    Child table model for internet-service-src-custom-group.
    
    Custom Internet Service source group name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Custom Internet Service group name.")  # datasource: ['firewall.internet-service-custom-group.name']
class SecurityPolicyInternetServiceSrcFortiguard(BaseModel):
    """
    Child table model for internet-service-src-fortiguard.
    
    FortiGuard Internet Service source name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="FortiGuard Internet Service name.")  # datasource: ['firewall.internet-service-fortiguard.name']
class SecurityPolicyInternetService6Name(BaseModel):
    """
    Child table model for internet-service6-name.
    
    IPv6 Internet Service name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="IPv6 Internet Service name.")  # datasource: ['firewall.internet-service-name.name']
class SecurityPolicyInternetService6Group(BaseModel):
    """
    Child table model for internet-service6-group.
    
    Internet Service group name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Internet Service group name.")  # datasource: ['firewall.internet-service-group.name']
class SecurityPolicyInternetService6Custom(BaseModel):
    """
    Child table model for internet-service6-custom.
    
    Custom IPv6 Internet Service name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Custom IPv6 Internet Service name.")  # datasource: ['firewall.internet-service-custom.name']
class SecurityPolicyInternetService6CustomGroup(BaseModel):
    """
    Child table model for internet-service6-custom-group.
    
    Custom IPv6 Internet Service group name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Custom IPv6 Internet Service group name.")  # datasource: ['firewall.internet-service-custom-group.name']
class SecurityPolicyInternetService6Fortiguard(BaseModel):
    """
    Child table model for internet-service6-fortiguard.
    
    FortiGuard IPv6 Internet Service name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="FortiGuard Internet Service name.")  # datasource: ['firewall.internet-service-fortiguard.name']
class SecurityPolicyInternetService6SrcName(BaseModel):
    """
    Child table model for internet-service6-src-name.
    
    IPv6 Internet Service source name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Internet Service name.")  # datasource: ['firewall.internet-service-name.name']
class SecurityPolicyInternetService6SrcGroup(BaseModel):
    """
    Child table model for internet-service6-src-group.
    
    Internet Service6 source group name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Internet Service group name.")  # datasource: ['firewall.internet-service-group.name']
class SecurityPolicyInternetService6SrcCustom(BaseModel):
    """
    Child table model for internet-service6-src-custom.
    
    Custom IPv6 Internet Service source name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Custom Internet Service name.")  # datasource: ['firewall.internet-service-custom.name']
class SecurityPolicyInternetService6SrcCustomGroup(BaseModel):
    """
    Child table model for internet-service6-src-custom-group.
    
    Custom Internet Service6 source group name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Custom Internet Service6 group name.")  # datasource: ['firewall.internet-service-custom-group.name']
class SecurityPolicyInternetService6SrcFortiguard(BaseModel):
    """
    Child table model for internet-service6-src-fortiguard.
    
    FortiGuard IPv6 Internet Service source name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="FortiGuard Internet Service name.")  # datasource: ['firewall.internet-service-fortiguard.name']
class SecurityPolicyService(BaseModel):
    """
    Child table model for service.
    
    Service and service group names.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Service name.")  # datasource: ['firewall.service.custom.name', 'firewall.service.group.name']
class SecurityPolicyApplication(BaseModel):
    """
    Child table model for application.
    
    Application ID list.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=0, le=4294967295, default=0, description="Application IDs.")
class SecurityPolicyAppCategory(BaseModel):
    """
    Child table model for app-category.
    
    Application category ID list.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=0, le=4294967295, default=0, description="Category IDs.")
class SecurityPolicyAppGroup(BaseModel):
    """
    Child table model for app-group.
    
    Application group names.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Application group names.")  # datasource: ['application.group.name']
class SecurityPolicyGroups(BaseModel):
    """
    Child table model for groups.
    
    Names of user groups that can authenticate with this policy.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="User group name.")  # datasource: ['user.group.name']
class SecurityPolicyUsers(BaseModel):
    """
    Child table model for users.
    
    Names of individual users that can authenticate with this policy.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="User name.")  # datasource: ['user.local.name']
class SecurityPolicyFssoGroups(BaseModel):
    """
    Child table model for fsso-groups.
    
    Names of FSSO groups.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=511, default="", description="Names of FSSO groups.")  # datasource: ['user.adgrp.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class SecurityPolicyModel(BaseModel):
    """
    Pydantic model for firewall/security_policy configuration.
    
    Configure NGFW IPv4/IPv6 application policies.
    
    Validation Rules:        - uuid: pattern=        - policyid: min=0 max=4294967294 pattern=        - name: max_length=35 pattern=        - comments: max_length=1023 pattern=        - srcintf: pattern=        - dstintf: pattern=        - srcaddr: pattern=        - srcaddr_negate: pattern=        - dstaddr: pattern=        - dstaddr_negate: pattern=        - srcaddr6: pattern=        - srcaddr6_negate: pattern=        - dstaddr6: pattern=        - dstaddr6_negate: pattern=        - internet_service: pattern=        - internet_service_name: pattern=        - internet_service_negate: pattern=        - internet_service_group: pattern=        - internet_service_custom: pattern=        - internet_service_custom_group: pattern=        - internet_service_fortiguard: pattern=        - internet_service_src: pattern=        - internet_service_src_name: pattern=        - internet_service_src_negate: pattern=        - internet_service_src_group: pattern=        - internet_service_src_custom: pattern=        - internet_service_src_custom_group: pattern=        - internet_service_src_fortiguard: pattern=        - internet_service6: pattern=        - internet_service6_name: pattern=        - internet_service6_negate: pattern=        - internet_service6_group: pattern=        - internet_service6_custom: pattern=        - internet_service6_custom_group: pattern=        - internet_service6_fortiguard: pattern=        - internet_service6_src: pattern=        - internet_service6_src_name: pattern=        - internet_service6_src_negate: pattern=        - internet_service6_src_group: pattern=        - internet_service6_src_custom: pattern=        - internet_service6_src_custom_group: pattern=        - internet_service6_src_fortiguard: pattern=        - enforce_default_app_port: pattern=        - service: pattern=        - service_negate: pattern=        - action: pattern=        - send_deny_packet: pattern=        - schedule: max_length=35 pattern=        - status: pattern=        - logtraffic: pattern=        - learning_mode: pattern=        - nat46: pattern=        - nat64: pattern=        - profile_type: pattern=        - profile_group: max_length=47 pattern=        - profile_protocol_options: max_length=47 pattern=        - ssl_ssh_profile: max_length=47 pattern=        - av_profile: max_length=47 pattern=        - webfilter_profile: max_length=47 pattern=        - dnsfilter_profile: max_length=47 pattern=        - emailfilter_profile: max_length=47 pattern=        - dlp_profile: max_length=47 pattern=        - file_filter_profile: max_length=47 pattern=        - ips_sensor: max_length=47 pattern=        - application_list: max_length=47 pattern=        - voip_profile: max_length=47 pattern=        - ips_voip_filter: max_length=47 pattern=        - sctp_filter_profile: max_length=47 pattern=        - diameter_filter_profile: max_length=47 pattern=        - virtual_patch_profile: max_length=47 pattern=        - icap_profile: max_length=47 pattern=        - videofilter_profile: max_length=47 pattern=        - ssh_filter_profile: max_length=47 pattern=        - casb_profile: max_length=47 pattern=        - application: pattern=        - app_category: pattern=        - url_category: pattern=        - app_group: pattern=        - groups: pattern=        - users: pattern=        - fsso_groups: pattern=    """
    
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
    policyid: int | None = Field(ge=0, le=4294967294, default=0, description="Policy ID.")    
    name: str | None = Field(max_length=35, default="", description="Policy name.")    
    comments: str | None = Field(max_length=1023, default=None, description="Comment.")    
    srcintf: list[Srcintf] = Field(description="Incoming (ingress) interface.")    
    dstintf: list[Dstintf] = Field(description="Outgoing (egress) interface.")    
    srcaddr: list[Srcaddr] = Field(default=None, description="Source IPv4 address name and address group names.")    
    srcaddr_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled srcaddr specifies what the source address must NOT be.")    
    dstaddr: list[Dstaddr] = Field(default=None, description="Destination IPv4 address name and address group names.")    
    dstaddr_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled dstaddr specifies what the destination address must NOT be.")    
    srcaddr6: list[Srcaddr6] = Field(default=None, description="Source IPv6 address name and address group names.")    
    srcaddr6_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled srcaddr6 specifies what the source address must NOT be.")    
    dstaddr6: list[Dstaddr6] = Field(default=None, description="Destination IPv6 address name and address group names.")    
    dstaddr6_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled dstaddr6 specifies what the destination address must NOT be.")    
    internet_service: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable use of Internet Services for this policy. If enabled, destination address, service and default application port enforcement are not used.")    
    internet_service_name: list[InternetServiceName] = Field(default=None, description="Internet Service name.")    
    internet_service_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled internet-service specifies what the service must NOT be.")    
    internet_service_group: list[InternetServiceGroup] = Field(default=None, description="Internet Service group name.")    
    internet_service_custom: list[InternetServiceCustom] = Field(default=None, description="Custom Internet Service name.")    
    internet_service_custom_group: list[InternetServiceCustomGroup] = Field(default=None, description="Custom Internet Service group name.")    
    internet_service_fortiguard: list[InternetServiceFortiguard] = Field(default=None, description="FortiGuard Internet Service name.")    
    internet_service_src: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable use of Internet Services in source for this policy. If enabled, source address is not used.")    
    internet_service_src_name: list[InternetServiceSrcName] = Field(default=None, description="Internet Service source name.")    
    internet_service_src_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled internet-service-src specifies what the service must NOT be.")    
    internet_service_src_group: list[InternetServiceSrcGroup] = Field(default=None, description="Internet Service source group name.")    
    internet_service_src_custom: list[InternetServiceSrcCustom] = Field(default=None, description="Custom Internet Service source name.")    
    internet_service_src_custom_group: list[InternetServiceSrcCustomGroup] = Field(default=None, description="Custom Internet Service source group name.")    
    internet_service_src_fortiguard: list[InternetServiceSrcFortiguard] = Field(default=None, description="FortiGuard Internet Service source name.")    
    internet_service6: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable use of IPv6 Internet Services for this policy. If enabled, destination address, service and default application port enforcement are not used.")    
    internet_service6_name: list[InternetService6Name] = Field(default=None, description="IPv6 Internet Service name.")    
    internet_service6_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled internet-service6 specifies what the service must NOT be.")    
    internet_service6_group: list[InternetService6Group] = Field(default=None, description="Internet Service group name.")    
    internet_service6_custom: list[InternetService6Custom] = Field(default=None, description="Custom IPv6 Internet Service name.")    
    internet_service6_custom_group: list[InternetService6CustomGroup] = Field(default=None, description="Custom IPv6 Internet Service group name.")    
    internet_service6_fortiguard: list[InternetService6Fortiguard] = Field(default=None, description="FortiGuard IPv6 Internet Service name.")    
    internet_service6_src: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable use of IPv6 Internet Services in source for this policy. If enabled, source address is not used.")    
    internet_service6_src_name: list[InternetService6SrcName] = Field(default=None, description="IPv6 Internet Service source name.")    
    internet_service6_src_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled internet-service6-src specifies what the service must NOT be.")    
    internet_service6_src_group: list[InternetService6SrcGroup] = Field(default=None, description="Internet Service6 source group name.")    
    internet_service6_src_custom: list[InternetService6SrcCustom] = Field(default=None, description="Custom IPv6 Internet Service source name.")    
    internet_service6_src_custom_group: list[InternetService6SrcCustomGroup] = Field(default=None, description="Custom Internet Service6 source group name.")    
    internet_service6_src_fortiguard: list[InternetService6SrcFortiguard] = Field(default=None, description="FortiGuard IPv6 Internet Service source name.")    
    enforce_default_app_port: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable default application port enforcement for allowed applications.")    
    service: list[Service] = Field(default=None, description="Service and service group names.")    
    service_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled service specifies what the service must NOT be.")    
    action: Literal["accept", "deny"] | None = Field(default="deny", description="Policy action (accept/deny).")    
    send_deny_packet: Literal["disable", "enable"] | None = Field(default="disable", description="Enable to send a reply when a session is denied or blocked by a firewall policy.")    
    schedule: str = Field(max_length=35, default="", description="Schedule name.")  # datasource: ['firewall.schedule.onetime.name', 'firewall.schedule.recurring.name', 'firewall.schedule.group.name']    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable or disable this policy.")    
    logtraffic: Literal["all", "utm", "disable"] | None = Field(default="utm", description="Enable or disable logging. Log all sessions or security profile sessions.")    
    learning_mode: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to allow everything, but log all of the meaningful data for security information gathering. A learning report will be generated.")    
    nat46: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable NAT46.")    
    nat64: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable NAT64.")    
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
    ssh_filter_profile: str | None = Field(max_length=47, default="", description="Name of an existing SSH filter profile.")  # datasource: ['ssh-filter.profile.name']    
    casb_profile: str | None = Field(max_length=47, default="", description="Name of an existing CASB profile.")  # datasource: ['casb.profile.name']    
    application: list[Application] = Field(default=None, description="Application ID list.")    
    app_category: list[AppCategory] = Field(default=None, description="Application category ID list.")    
    url_category: list[UrlCategory] = Field(default="", description="URL categories or groups.")    
    app_group: list[AppGroup] = Field(default=None, description="Application group names.")    
    groups: list[Groups] = Field(default=None, description="Names of user groups that can authenticate with this policy.")    
    users: list[Users] = Field(default=None, description="Names of individual users that can authenticate with this policy.")    
    fsso_groups: list[FssoGroups] = Field(default=None, description="Names of FSSO groups.")    
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
    "SecurityPolicyModel",    "SecurityPolicySrcintf",    "SecurityPolicyDstintf",    "SecurityPolicySrcaddr",    "SecurityPolicyDstaddr",    "SecurityPolicySrcaddr6",    "SecurityPolicyDstaddr6",    "SecurityPolicyInternetServiceName",    "SecurityPolicyInternetServiceGroup",    "SecurityPolicyInternetServiceCustom",    "SecurityPolicyInternetServiceCustomGroup",    "SecurityPolicyInternetServiceFortiguard",    "SecurityPolicyInternetServiceSrcName",    "SecurityPolicyInternetServiceSrcGroup",    "SecurityPolicyInternetServiceSrcCustom",    "SecurityPolicyInternetServiceSrcCustomGroup",    "SecurityPolicyInternetServiceSrcFortiguard",    "SecurityPolicyInternetService6Name",    "SecurityPolicyInternetService6Group",    "SecurityPolicyInternetService6Custom",    "SecurityPolicyInternetService6CustomGroup",    "SecurityPolicyInternetService6Fortiguard",    "SecurityPolicyInternetService6SrcName",    "SecurityPolicyInternetService6SrcGroup",    "SecurityPolicyInternetService6SrcCustom",    "SecurityPolicyInternetService6SrcCustomGroup",    "SecurityPolicyInternetService6SrcFortiguard",    "SecurityPolicyService",    "SecurityPolicyApplication",    "SecurityPolicyAppCategory",    "SecurityPolicyAppGroup",    "SecurityPolicyGroups",    "SecurityPolicyUsers",    "SecurityPolicyFssoGroups",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:33.319647Z
# ============================================================================