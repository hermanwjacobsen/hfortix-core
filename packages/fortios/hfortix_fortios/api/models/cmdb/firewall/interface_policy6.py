"""
Pydantic Models for CMDB - firewall/interface_policy6

Runtime validation models for firewall/interface_policy6 configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.firewall.interface_policy6 import 
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

class InterfacePolicy6Srcaddr6(BaseModel):
    """
    Child table model for srcaddr6.
    
    IPv6 address object to limit traffic monitoring to network traffic sent from the specified address or range.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address6.name', 'firewall.addrgrp6.name']
class InterfacePolicy6Dstaddr6(BaseModel):
    """
    Child table model for dstaddr6.
    
    IPv6 address object to limit traffic monitoring to network traffic sent to the specified address or range.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address6.name', 'firewall.addrgrp6.name']
class InterfacePolicy6Service6(BaseModel):
    """
    Child table model for service6.
    
    Service name.
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

class InterfacePolicy6Model(BaseModel):
    """
    Pydantic model for firewall/interface_policy6 configuration.
    
    Configure IPv6 interface policies.
    
    Validation Rules:        - policyid: min=0 max=4294967295 pattern=        - uuid: pattern=        - status: pattern=        - comments: max_length=1023 pattern=        - logtraffic: pattern=        - interface: max_length=35 pattern=        - srcaddr6: pattern=        - dstaddr6: pattern=        - service6: pattern=        - application_list_status: pattern=        - application_list: max_length=47 pattern=        - ips_sensor_status: pattern=        - ips_sensor: max_length=47 pattern=        - dsri: pattern=        - av_profile_status: pattern=        - av_profile: max_length=47 pattern=        - webfilter_profile_status: pattern=        - webfilter_profile: max_length=47 pattern=        - casb_profile_status: pattern=        - casb_profile: max_length=47 pattern=        - emailfilter_profile_status: pattern=        - emailfilter_profile: max_length=47 pattern=        - dlp_profile_status: pattern=        - dlp_profile: max_length=47 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    policyid: int | None = Field(ge=0, le=4294967295, default=0, description="Policy ID (0 - 4294967295).")    
    uuid: str | None = Field(default="00000000-0000-0000-0000-000000000000", description="Universally Unique Identifier (UUID; automatically assigned but can be manually reset).")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable this policy.")    
    comments: str | None = Field(max_length=1023, default=None, description="Comments.")    
    logtraffic: Literal["all", "utm", "disable"] | None = Field(default="utm", description="Logging type to be used in this policy (Options: all | utm | disable, Default: utm).")    
    interface: str = Field(max_length=35, default="", description="Monitored interface name from available interfaces.")  # datasource: ['system.zone.name', 'system.sdwan.zone.name', 'system.interface.name']    
    srcaddr6: list[Srcaddr6] = Field(description="IPv6 address object to limit traffic monitoring to network traffic sent from the specified address or range.")    
    dstaddr6: list[Dstaddr6] = Field(description="IPv6 address object to limit traffic monitoring to network traffic sent to the specified address or range.")    
    service6: list[Service6] = Field(default=None, description="Service name.")    
    application_list_status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable application control.")    
    application_list: str = Field(max_length=47, default="", description="Application list name.")  # datasource: ['application.list.name']    
    ips_sensor_status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable IPS.")    
    ips_sensor: str = Field(max_length=47, default="", description="IPS sensor name.")  # datasource: ['ips.sensor.name']    
    dsri: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable DSRI.")    
    av_profile_status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable antivirus.")    
    av_profile: str = Field(max_length=47, default="", description="Antivirus profile.")  # datasource: ['antivirus.profile.name']    
    webfilter_profile_status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable web filtering.")    
    webfilter_profile: str = Field(max_length=47, default="", description="Web filter profile.")  # datasource: ['webfilter.profile.name']    
    casb_profile_status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable CASB.")    
    casb_profile: str = Field(max_length=47, default="", description="CASB profile.")  # datasource: ['casb.profile.name']    
    emailfilter_profile_status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable email filter.")    
    emailfilter_profile: str = Field(max_length=47, default="", description="Email filter profile.")  # datasource: ['emailfilter.profile.name']    
    dlp_profile_status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable DLP.")    
    dlp_profile: str = Field(max_length=47, default="", description="DLP profile name.")  # datasource: ['dlp.profile.name']    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('interface')
    @classmethod
    def validate_interface(cls, v: Any) -> Any:
        """
        Validate interface field.
        
        Datasource: ['system.zone.name', 'system.sdwan.zone.name', 'system.interface.name']
        
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
    "InterfacePolicy6Model",    "InterfacePolicy6Srcaddr6",    "InterfacePolicy6Dstaddr6",    "InterfacePolicy6Service6",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:33.602837Z
# ============================================================================