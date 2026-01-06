"""
Pydantic Models for CMDB - firewall/multicast_policy6

Runtime validation models for firewall/multicast_policy6 configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.firewall.multicast_policy6 import 
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

class MulticastPolicy6Srcaddr(BaseModel):
    """
    Child table model for srcaddr.
    
    IPv6 source address name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address6.name', 'firewall.addrgrp6.name']
class MulticastPolicy6Dstaddr(BaseModel):
    """
    Child table model for dstaddr.
    
    IPv6 destination address name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.multicast-address6.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class MulticastPolicy6Model(BaseModel):
    """
    Pydantic model for firewall/multicast_policy6 configuration.
    
    Configure IPv6 multicast NAT policies.
    
    Validation Rules:        - id: min=0 max=4294967294 pattern=        - uuid: pattern=        - status: pattern=        - name: max_length=35 pattern=        - srcintf: max_length=35 pattern=        - dstintf: max_length=35 pattern=        - srcaddr: pattern=        - dstaddr: pattern=        - action: pattern=        - protocol: min=0 max=255 pattern=        - start_port: min=0 max=65535 pattern=        - end_port: min=0 max=65535 pattern=        - utm_status: pattern=        - ips_sensor: max_length=47 pattern=        - logtraffic: pattern=        - auto_asic_offload: pattern=        - comments: max_length=1023 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    id: int | None = Field(ge=0, le=4294967294, default=0, description="Policy ID (0 - 4294967294).")    
    uuid: str | None = Field(default="00000000-0000-0000-0000-000000000000", description="Universally Unique Identifier (UUID; automatically assigned but can be manually reset).")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable this policy.")    
    name: str | None = Field(max_length=35, default="", description="Policy name.")    
    srcintf: str = Field(max_length=35, default="", description="IPv6 source interface name.")  # datasource: ['system.interface.name', 'system.zone.name', 'system.sdwan.zone.name']    
    dstintf: str = Field(max_length=35, default="", description="IPv6 destination interface name.")  # datasource: ['system.interface.name', 'system.zone.name', 'system.sdwan.zone.name']    
    srcaddr: list[Srcaddr] = Field(description="IPv6 source address name.")    
    dstaddr: list[Dstaddr] = Field(description="IPv6 destination address name.")    
    action: Literal["accept", "deny"] | None = Field(default="accept", description="Accept or deny traffic matching the policy.")    
    protocol: int | None = Field(ge=0, le=255, default=0, description="Integer value for the protocol type as defined by IANA (0 - 255, default = 0).")    
    start_port: int | None = Field(ge=0, le=65535, default=1, description="Integer value for starting TCP/UDP/SCTP destination port in range (1 - 65535, default = 1).")    
    end_port: int | None = Field(ge=0, le=65535, default=65535, description="Integer value for ending TCP/UDP/SCTP destination port in range (1 - 65535, default = 65535).")    
    utm_status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to add an IPS security profile to the policy.")    
    ips_sensor: str | None = Field(max_length=47, default="", description="Name of an existing IPS sensor.")  # datasource: ['ips.sensor.name']    
    logtraffic: Literal["all", "utm", "disable"] | None = Field(default="utm", description="Enable or disable logging. Log all sessions or security profile sessions.")    
    auto_asic_offload: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable offloading policy traffic for hardware acceleration.")    
    comments: str | None = Field(max_length=1023, default=None, description="Comment.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('srcintf')
    @classmethod
    def validate_srcintf(cls, v: Any) -> Any:
        """
        Validate srcintf field.
        
        Datasource: ['system.interface.name', 'system.zone.name', 'system.sdwan.zone.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('dstintf')
    @classmethod
    def validate_dstintf(cls, v: Any) -> Any:
        """
        Validate dstintf field.
        
        Datasource: ['system.interface.name', 'system.zone.name', 'system.sdwan.zone.name']
        
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
    "MulticastPolicy6Model",    "MulticastPolicy6Srcaddr",    "MulticastPolicy6Dstaddr",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:35.405595Z
# ============================================================================