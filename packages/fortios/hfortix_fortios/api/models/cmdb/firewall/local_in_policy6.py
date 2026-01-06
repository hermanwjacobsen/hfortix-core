"""
Pydantic Models for CMDB - firewall/local_in_policy6

Runtime validation models for firewall/local_in_policy6 configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.firewall.local_in_policy6 import 
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

class LocalInPolicy6Intf(BaseModel):
    """
    Child table model for intf.
    
    Incoming interface name from available options.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['system.zone.name', 'system.sdwan.zone.name', 'system.interface.name']
class LocalInPolicy6Srcaddr(BaseModel):
    """
    Child table model for srcaddr.
    
    Source address object from available options.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address6.name', 'firewall.addrgrp6.name', 'system.external-resource.name']
class LocalInPolicy6Dstaddr(BaseModel):
    """
    Child table model for dstaddr.
    
    Destination address object from available options.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address6.name', 'firewall.addrgrp6.name', 'system.external-resource.name']
class LocalInPolicy6InternetService6SrcName(BaseModel):
    """
    Child table model for internet-service6-src-name.
    
    IPv6 Internet Service source name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Internet Service name.")  # datasource: ['firewall.internet-service-name.name']
class LocalInPolicy6InternetService6SrcGroup(BaseModel):
    """
    Child table model for internet-service6-src-group.
    
    Internet Service6 source group name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Internet Service group name.")  # datasource: ['firewall.internet-service-group.name']
class LocalInPolicy6InternetService6SrcCustom(BaseModel):
    """
    Child table model for internet-service6-src-custom.
    
    Custom IPv6 Internet Service source name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Custom Internet Service name.")  # datasource: ['firewall.internet-service-custom.name']
class LocalInPolicy6InternetService6SrcCustomGroup(BaseModel):
    """
    Child table model for internet-service6-src-custom-group.
    
    Custom Internet Service6 source group name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Custom Internet Service6 group name.")  # datasource: ['firewall.internet-service-custom-group.name']
class LocalInPolicy6InternetService6SrcFortiguard(BaseModel):
    """
    Child table model for internet-service6-src-fortiguard.
    
    FortiGuard IPv6 Internet Service source name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="FortiGuard Internet Service name.")  # datasource: ['firewall.internet-service-fortiguard.name']
class LocalInPolicy6Service(BaseModel):
    """
    Child table model for service.
    
    Service object from available options. Separate names with a space.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Service name.")  # datasource: ['firewall.service.custom.name', 'firewall.service.group.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class LocalInPolicy6Model(BaseModel):
    """
    Pydantic model for firewall/local_in_policy6 configuration.
    
    Configure user defined IPv6 local-in policies.
    
    Validation Rules:        - policyid: min=0 max=4294967295 pattern=        - uuid: pattern=        - intf: pattern=        - srcaddr: pattern=        - srcaddr_negate: pattern=        - dstaddr: pattern=        - internet_service6_src: pattern=        - internet_service6_src_name: pattern=        - internet_service6_src_group: pattern=        - internet_service6_src_custom: pattern=        - internet_service6_src_custom_group: pattern=        - internet_service6_src_fortiguard: pattern=        - dstaddr_negate: pattern=        - action: pattern=        - service: pattern=        - service_negate: pattern=        - internet_service6_src_negate: pattern=        - schedule: max_length=35 pattern=        - status: pattern=        - virtual_patch: pattern=        - logtraffic: pattern=        - comments: max_length=1023 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    policyid: int | None = Field(ge=0, le=4294967295, default=0, description="User defined local in policy ID.")    
    uuid: str | None = Field(default="00000000-0000-0000-0000-000000000000", description="Universally Unique Identifier (UUID; automatically assigned but can be manually reset).")    
    intf: list[Intf] = Field(description="Incoming interface name from available options.")    
    srcaddr: list[Srcaddr] = Field(description="Source address object from available options.")    
    srcaddr_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled srcaddr specifies what the source address must NOT be.")    
    dstaddr: list[Dstaddr] = Field(description="Destination address object from available options.")    
    internet_service6_src: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable use of IPv6 Internet Services in source for this local-in policy.If enabled, source address is not used.")    
    internet_service6_src_name: list[InternetService6SrcName] = Field(default=None, description="IPv6 Internet Service source name.")    
    internet_service6_src_group: list[InternetService6SrcGroup] = Field(default=None, description="Internet Service6 source group name.")    
    internet_service6_src_custom: list[InternetService6SrcCustom] = Field(default=None, description="Custom IPv6 Internet Service source name.")    
    internet_service6_src_custom_group: list[InternetService6SrcCustomGroup] = Field(default=None, description="Custom Internet Service6 source group name.")    
    internet_service6_src_fortiguard: list[InternetService6SrcFortiguard] = Field(default=None, description="FortiGuard IPv6 Internet Service source name.")    
    dstaddr_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled dstaddr specifies what the destination address must NOT be.")    
    action: Literal["accept", "deny"] | None = Field(default="deny", description="Action performed on traffic matching the policy (default = deny).")    
    service: list[Service] = Field(description="Service object from available options. Separate names with a space.")    
    service_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled service specifies what the service must NOT be.")    
    internet_service6_src_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled internet-service6-src specifies what the service must NOT be.")    
    schedule: str = Field(max_length=35, default="", description="Schedule object from available options.")  # datasource: ['firewall.schedule.onetime.name', 'firewall.schedule.recurring.name', 'firewall.schedule.group.name']    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable this local-in policy.")    
    virtual_patch: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable the virtual patching feature.")    
    logtraffic: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable local-in traffic logging.")    
    comments: str | None = Field(max_length=1023, default=None, description="Comment.")    
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
    "LocalInPolicy6Model",    "LocalInPolicy6Intf",    "LocalInPolicy6Srcaddr",    "LocalInPolicy6Dstaddr",    "LocalInPolicy6InternetService6SrcName",    "LocalInPolicy6InternetService6SrcGroup",    "LocalInPolicy6InternetService6SrcCustom",    "LocalInPolicy6InternetService6SrcCustomGroup",    "LocalInPolicy6InternetService6SrcFortiguard",    "LocalInPolicy6Service",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:34.137824Z
# ============================================================================