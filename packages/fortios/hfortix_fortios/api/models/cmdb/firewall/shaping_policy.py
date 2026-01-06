"""
Pydantic Models for CMDB - firewall/shaping_policy

Runtime validation models for firewall/shaping_policy configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.firewall.shaping_policy import 
    >>>
    >>> # Create with validation
    >>> obj = (
    ...     id=1,
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

class ShapingPolicySrcaddr(BaseModel):
    """
    Child table model for srcaddr.
    
    IPv4 source address and address group names.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name']
class ShapingPolicyDstaddr(BaseModel):
    """
    Child table model for dstaddr.
    
    IPv4 destination address and address group names.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name']
class ShapingPolicySrcaddr6(BaseModel):
    """
    Child table model for srcaddr6.
    
    IPv6 source address and address group names.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address6.name', 'firewall.addrgrp6.name']
class ShapingPolicyDstaddr6(BaseModel):
    """
    Child table model for dstaddr6.
    
    IPv6 destination address and address group names.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address6.name', 'firewall.addrgrp6.name']
class ShapingPolicyInternetServiceName(BaseModel):
    """
    Child table model for internet-service-name.
    
    Internet Service ID.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Internet Service name.")  # datasource: ['firewall.internet-service-name.name']
class ShapingPolicyInternetServiceGroup(BaseModel):
    """
    Child table model for internet-service-group.
    
    Internet Service group name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Internet Service group name.")  # datasource: ['firewall.internet-service-group.name']
class ShapingPolicyInternetServiceCustom(BaseModel):
    """
    Child table model for internet-service-custom.
    
    Custom Internet Service name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Custom Internet Service name.")  # datasource: ['firewall.internet-service-custom.name']
class ShapingPolicyInternetServiceCustomGroup(BaseModel):
    """
    Child table model for internet-service-custom-group.
    
    Custom Internet Service group name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Custom Internet Service group name.")  # datasource: ['firewall.internet-service-custom-group.name']
class ShapingPolicyInternetServiceFortiguard(BaseModel):
    """
    Child table model for internet-service-fortiguard.
    
    FortiGuard Internet Service name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="FortiGuard Internet Service name.")  # datasource: ['firewall.internet-service-fortiguard.name']
class ShapingPolicyInternetServiceSrcName(BaseModel):
    """
    Child table model for internet-service-src-name.
    
    Internet Service source name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Internet Service name.")  # datasource: ['firewall.internet-service-name.name']
class ShapingPolicyInternetServiceSrcGroup(BaseModel):
    """
    Child table model for internet-service-src-group.
    
    Internet Service source group name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Internet Service group name.")  # datasource: ['firewall.internet-service-group.name']
class ShapingPolicyInternetServiceSrcCustom(BaseModel):
    """
    Child table model for internet-service-src-custom.
    
    Custom Internet Service source name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Custom Internet Service name.")  # datasource: ['firewall.internet-service-custom.name']
class ShapingPolicyInternetServiceSrcCustomGroup(BaseModel):
    """
    Child table model for internet-service-src-custom-group.
    
    Custom Internet Service source group name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Custom Internet Service group name.")  # datasource: ['firewall.internet-service-custom-group.name']
class ShapingPolicyInternetServiceSrcFortiguard(BaseModel):
    """
    Child table model for internet-service-src-fortiguard.
    
    FortiGuard Internet Service source name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="FortiGuard Internet Service name.")  # datasource: ['firewall.internet-service-fortiguard.name']
class ShapingPolicyService(BaseModel):
    """
    Child table model for service.
    
    Service and service group names.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Service name.")  # datasource: ['firewall.service.custom.name', 'firewall.service.group.name']
class ShapingPolicyUsers(BaseModel):
    """
    Child table model for users.
    
    Apply this traffic shaping policy to individual users that have authenticated with the FortiGate.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="User name.")  # datasource: ['user.local.name']
class ShapingPolicyGroups(BaseModel):
    """
    Child table model for groups.
    
    Apply this traffic shaping policy to user groups that have authenticated with the FortiGate.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Group name.")  # datasource: ['user.group.name']
class ShapingPolicyApplication(BaseModel):
    """
    Child table model for application.
    
    IDs of one or more applications that this shaper applies application control traffic shaping to.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=0, le=4294967295, default=0, description="Application IDs.")
class ShapingPolicyAppCategory(BaseModel):
    """
    Child table model for app-category.
    
    IDs of one or more application categories that this shaper applies application control traffic shaping to.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=0, le=4294967295, default=0, description="Category IDs.")
class ShapingPolicyAppGroup(BaseModel):
    """
    Child table model for app-group.
    
    One or more application group names.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Application group name.")  # datasource: ['application.group.name']
class ShapingPolicyUrlCategory(BaseModel):
    """
    Child table model for url-category.
    
    IDs of one or more FortiGuard Web Filtering categories that this shaper applies traffic shaping to.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=0, le=4294967295, default=0, description="URL category ID.")
class ShapingPolicySrcintf(BaseModel):
    """
    Child table model for srcintf.
    
    One or more incoming (ingress) interfaces.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Interface name.")  # datasource: ['system.interface.name', 'system.zone.name', 'system.sdwan.zone.name']
class ShapingPolicyDstintf(BaseModel):
    """
    Child table model for dstintf.
    
    One or more outgoing (egress) interfaces.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Interface name.")  # datasource: ['system.interface.name', 'system.zone.name', 'system.sdwan.zone.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class ShapingPolicyModel(BaseModel):
    """
    Pydantic model for firewall/shaping_policy configuration.
    
    Configure shaping policies.
    
    Validation Rules:        - id: min=0 max=4294967295 pattern=        - uuid: pattern=        - name: max_length=35 pattern=        - comment: max_length=255 pattern=        - status: pattern=        - ip_version: pattern=        - traffic_type: pattern=        - srcaddr: pattern=        - dstaddr: pattern=        - srcaddr6: pattern=        - dstaddr6: pattern=        - internet_service: pattern=        - internet_service_name: pattern=        - internet_service_group: pattern=        - internet_service_custom: pattern=        - internet_service_custom_group: pattern=        - internet_service_fortiguard: pattern=        - internet_service_src: pattern=        - internet_service_src_name: pattern=        - internet_service_src_group: pattern=        - internet_service_src_custom: pattern=        - internet_service_src_custom_group: pattern=        - internet_service_src_fortiguard: pattern=        - service: pattern=        - schedule: max_length=35 pattern=        - users: pattern=        - groups: pattern=        - application: pattern=        - app_category: pattern=        - app_group: pattern=        - url_category: pattern=        - srcintf: pattern=        - dstintf: pattern=        - tos_mask: pattern=        - tos: pattern=        - tos_negate: pattern=        - traffic_shaper: max_length=35 pattern=        - traffic_shaper_reverse: max_length=35 pattern=        - per_ip_shaper: max_length=35 pattern=        - class_id: min=0 max=4294967295 pattern=        - diffserv_forward: pattern=        - diffserv_reverse: pattern=        - diffservcode_forward: pattern=        - diffservcode_rev: pattern=        - cos_mask: pattern=        - cos: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="Shaping policy ID (0 - 4294967295).")    
    uuid: str | None = Field(default="00000000-0000-0000-0000-000000000000", description="Universally Unique Identifier (UUID; automatically assigned but can be manually reset).")    
    name: str | None = Field(max_length=35, default="", description="Shaping policy name.")    
    comment: str | None = Field(max_length=255, default=None, description="Comments.")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable this traffic shaping policy.")    
    ip_version: Literal["4", "6"] | None = Field(default="4", description="Apply this traffic shaping policy to IPv4 or IPv6 traffic.")    
    traffic_type: Literal["forwarding", "local-in", "local-out"] | None = Field(default="forwarding", description="Traffic type.")    
    srcaddr: list[Srcaddr] = Field(description="IPv4 source address and address group names.")    
    dstaddr: list[Dstaddr] = Field(description="IPv4 destination address and address group names.")    
    srcaddr6: list[Srcaddr6] = Field(description="IPv6 source address and address group names.")    
    dstaddr6: list[Dstaddr6] = Field(description="IPv6 destination address and address group names.")    
    internet_service: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable use of Internet Services for this policy. If enabled, destination address and service are not used.")    
    internet_service_name: list[InternetServiceName] = Field(default=None, description="Internet Service ID.")    
    internet_service_group: list[InternetServiceGroup] = Field(default=None, description="Internet Service group name.")    
    internet_service_custom: list[InternetServiceCustom] = Field(default=None, description="Custom Internet Service name.")    
    internet_service_custom_group: list[InternetServiceCustomGroup] = Field(default=None, description="Custom Internet Service group name.")    
    internet_service_fortiguard: list[InternetServiceFortiguard] = Field(default=None, description="FortiGuard Internet Service name.")    
    internet_service_src: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable use of Internet Services in source for this policy. If enabled, source address is not used.")    
    internet_service_src_name: list[InternetServiceSrcName] = Field(default=None, description="Internet Service source name.")    
    internet_service_src_group: list[InternetServiceSrcGroup] = Field(default=None, description="Internet Service source group name.")    
    internet_service_src_custom: list[InternetServiceSrcCustom] = Field(default=None, description="Custom Internet Service source name.")    
    internet_service_src_custom_group: list[InternetServiceSrcCustomGroup] = Field(default=None, description="Custom Internet Service source group name.")    
    internet_service_src_fortiguard: list[InternetServiceSrcFortiguard] = Field(default=None, description="FortiGuard Internet Service source name.")    
    service: list[Service] = Field(description="Service and service group names.")    
    schedule: str | None = Field(max_length=35, default="", description="Schedule name.")  # datasource: ['firewall.schedule.onetime.name', 'firewall.schedule.recurring.name', 'firewall.schedule.group.name']    
    users: list[Users] = Field(default=None, description="Apply this traffic shaping policy to individual users that have authenticated with the FortiGate.")    
    groups: list[Groups] = Field(default=None, description="Apply this traffic shaping policy to user groups that have authenticated with the FortiGate.")    
    application: list[Application] = Field(default=None, description="IDs of one or more applications that this shaper applies application control traffic shaping to.")    
    app_category: list[AppCategory] = Field(default=None, description="IDs of one or more application categories that this shaper applies application control traffic shaping to.")    
    app_group: list[AppGroup] = Field(default=None, description="One or more application group names.")    
    url_category: list[UrlCategory] = Field(default=None, description="IDs of one or more FortiGuard Web Filtering categories that this shaper applies traffic shaping to.")    
    srcintf: list[Srcintf] = Field(default=None, description="One or more incoming (ingress) interfaces.")    
    dstintf: list[Dstintf] = Field(description="One or more outgoing (egress) interfaces.")    
    tos_mask: str | None = Field(default="", description="Non-zero bit positions are used for comparison while zero bit positions are ignored.")    
    tos: str | None = Field(default="", description="ToS (Type of Service) value used for comparison.")    
    tos_negate: Literal["enable", "disable"] | None = Field(default="disable", description="Enable negated TOS match.")    
    traffic_shaper: str | None = Field(max_length=35, default="", description="Traffic shaper to apply to traffic forwarded by the firewall policy.")  # datasource: ['firewall.shaper.traffic-shaper.name']    
    traffic_shaper_reverse: str | None = Field(max_length=35, default="", description="Traffic shaper to apply to response traffic received by the firewall policy.")  # datasource: ['firewall.shaper.traffic-shaper.name']    
    per_ip_shaper: str | None = Field(max_length=35, default="", description="Per-IP traffic shaper to apply with this policy.")  # datasource: ['firewall.shaper.per-ip-shaper.name']    
    class_id: int | None = Field(ge=0, le=4294967295, default=0, description="Traffic class ID.")  # datasource: ['firewall.traffic-class.class-id']    
    diffserv_forward: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to change packet's DiffServ values to the specified diffservcode-forward value.")    
    diffserv_reverse: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to change packet's reverse (reply) DiffServ values to the specified diffservcode-rev value.")    
    diffservcode_forward: str | None = Field(default="", description="Change packet's DiffServ to this value.")    
    diffservcode_rev: str | None = Field(default="", description="Change packet's reverse (reply) DiffServ to this value.")    
    cos_mask: str | None = Field(default="", description="VLAN CoS evaluated bits.")    
    cos: str | None = Field(default="", description="VLAN CoS bit pattern.")    
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
    @field_validator('class_id')
    @classmethod
    def validate_class_id(cls, v: Any) -> Any:
        """
        Validate class_id field.
        
        Datasource: ['firewall.traffic-class.class-id']
        
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
    "ShapingPolicyModel",    "ShapingPolicySrcaddr",    "ShapingPolicyDstaddr",    "ShapingPolicySrcaddr6",    "ShapingPolicyDstaddr6",    "ShapingPolicyInternetServiceName",    "ShapingPolicyInternetServiceGroup",    "ShapingPolicyInternetServiceCustom",    "ShapingPolicyInternetServiceCustomGroup",    "ShapingPolicyInternetServiceFortiguard",    "ShapingPolicyInternetServiceSrcName",    "ShapingPolicyInternetServiceSrcGroup",    "ShapingPolicyInternetServiceSrcCustom",    "ShapingPolicyInternetServiceSrcCustomGroup",    "ShapingPolicyInternetServiceSrcFortiguard",    "ShapingPolicyService",    "ShapingPolicyUsers",    "ShapingPolicyGroups",    "ShapingPolicyApplication",    "ShapingPolicyAppCategory",    "ShapingPolicyAppGroup",    "ShapingPolicyUrlCategory",    "ShapingPolicySrcintf",    "ShapingPolicyDstintf",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:33.104665Z
# ============================================================================