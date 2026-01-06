"""
Pydantic Models for CMDB - router/static

Runtime validation models for router/static configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.router.static import 
    >>>
    >>> # Create with validation
    >>> obj = (
    ...     seq-num=1,
    ...     name="example",
    ... )
    >>>
    >>> # Validation happens automatically
    >>> # ValidationError raised if constraints violated
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class StaticSdwanZone(BaseModel):
    """
    Child table model for sdwan-zone.
    
    Choose SD-WAN Zone.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="SD-WAN zone name.")  # datasource: ['system.sdwan.zone.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class StaticModel(BaseModel):
    """
    Pydantic model for router/static configuration.
    
    Configure IPv4 static routing tables.
    
    Validation Rules:        - seq_num: min=0 max=4294967295 pattern=        - status: pattern=        - dst: pattern=        - src: pattern=        - gateway: pattern=        - preferred_source: pattern=        - distance: min=1 max=255 pattern=        - weight: min=0 max=255 pattern=        - priority: min=1 max=65535 pattern=        - device: max_length=35 pattern=        - comment: max_length=255 pattern=        - blackhole: pattern=        - dynamic_gateway: pattern=        - sdwan_zone: pattern=        - dstaddr: max_length=79 pattern=        - internet_service: min=0 max=4294967295 pattern=        - internet_service_custom: max_length=64 pattern=        - internet_service_fortiguard: max_length=64 pattern=        - link_monitor_exempt: pattern=        - tag: min=0 max=4294967295 pattern=        - vrf: min=0 max=511 pattern=        - bfd: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    seq_num: int | None = Field(ge=0, le=4294967295, default=0, description="Sequence number.")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable this static route.")    
    dst: str = Field(default="0.0.0.0 0.0.0.0", description="Destination IP and mask for this route.")    
    src: str | None = Field(default="0.0.0.0 0.0.0.0", description="Source prefix for this route.")    
    gateway: str | None = Field(default="0.0.0.0", description="Gateway IP for this route.")    
    preferred_source: str | None = Field(default="0.0.0.0", description="Preferred source IP for this route.")    
    distance: int | None = Field(ge=1, le=255, default=10, description="Administrative distance (1 - 255).")    
    weight: int | None = Field(ge=0, le=255, default=0, description="Administrative weight (0 - 255).")    
    priority: int | None = Field(ge=1, le=65535, default=1, description="Administrative priority (1 - 65535).")    
    device: str = Field(max_length=35, default="", description="Gateway out interface or tunnel.")  # datasource: ['system.interface.name']    
    comment: str | None = Field(max_length=255, default=None, description="Optional comments.")    
    blackhole: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable black hole.")    
    dynamic_gateway: Literal["enable", "disable"] | None = Field(default="disable", description="Enable use of dynamic gateway retrieved from a DHCP or PPP server.")    
    sdwan_zone: list[SdwanZone] = Field(default=None, description="Choose SD-WAN Zone.")    
    dstaddr: str | None = Field(max_length=79, default="", description="Name of firewall address or address group.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name']    
    internet_service: int | None = Field(ge=0, le=4294967295, default=0, description="Application ID in the Internet service database.")  # datasource: ['firewall.internet-service.id']    
    internet_service_custom: str | None = Field(max_length=64, default="", description="Application name in the Internet service custom database.")  # datasource: ['firewall.internet-service-custom.name']    
    internet_service_fortiguard: str | None = Field(max_length=64, default="", description="Application name in the Internet service fortiguard database.")  # datasource: ['firewall.internet-service-fortiguard.name']    
    link_monitor_exempt: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable withdrawal of this static route when link monitor or health check is down.")    
    tag: int | None = Field(ge=0, le=4294967295, default=0, description="Route tag.")    
    vrf: int | None = Field(ge=0, le=511, default="unspecified", description="Virtual Routing Forwarding ID.")    
    bfd: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable Bidirectional Forwarding Detection (BFD).")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('device')
    @classmethod
    def validate_device(cls, v: Any) -> Any:
        """
        Validate device field.
        
        Datasource: ['system.interface.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('dstaddr')
    @classmethod
    def validate_dstaddr(cls, v: Any) -> Any:
        """
        Validate dstaddr field.
        
        Datasource: ['firewall.address.name', 'firewall.addrgrp.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('internet_service')
    @classmethod
    def validate_internet_service(cls, v: Any) -> Any:
        """
        Validate internet_service field.
        
        Datasource: ['firewall.internet-service.id']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('internet_service_custom')
    @classmethod
    def validate_internet_service_custom(cls, v: Any) -> Any:
        """
        Validate internet_service_custom field.
        
        Datasource: ['firewall.internet-service-custom.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('internet_service_fortiguard')
    @classmethod
    def validate_internet_service_fortiguard(cls, v: Any) -> Any:
        """
        Validate internet_service_fortiguard field.
        
        Datasource: ['firewall.internet-service-fortiguard.name']
        
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
    "StaticModel",    "StaticSdwanZone",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:32.968978Z
# ============================================================================