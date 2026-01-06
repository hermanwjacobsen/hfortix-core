"""
Pydantic Models for CMDB - router/multicast6

Runtime validation models for router/multicast6 configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.router.multicast6 import 
    >>>
    >>> # Create with validation
    >>> obj = (
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

class Multicast6Interface(BaseModel):
    """
    Child table model for interface.
    
    Protocol Independent Multicast (PIM) interfaces.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=15, default="", description="Interface name.")  # datasource: ['system.interface.name']    
    hello_interval: int | None = Field(ge=1, le=65535, default=30, description="Interval between sending PIM hello messages in seconds (1 - 65535, default = 30).")    
    hello_holdtime: int | None = Field(ge=1, le=65535, default="", description="Time before old neighbor information expires in seconds (1 - 65535, default = 105).")
class Multicast6PimSmGlobal(BaseModel):
    """
    Child table model for pim-sm-global.
    
    PIM sparse-mode global settings.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    register_rate_limit: int | None = Field(ge=0, le=65535, default=0, description="Limit of packets/sec per source registered through this RP (0 means unlimited).")    
    pim_use_sdwan: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable use of SDWAN when checking RPF neighbor and sending of REG packet.")    
    rp_address: list[RpAddress] = Field(default=None, description="Statically configured RP addresses.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class Multicast6Model(BaseModel):
    """
    Pydantic model for router/multicast6 configuration.
    
    Configure IPv6 multicast.
    
    Validation Rules:        - multicast_routing: pattern=        - multicast_pmtu: pattern=        - interface: pattern=        - pim_sm_global: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    multicast_routing: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable IPv6 multicast routing.")    
    multicast_pmtu: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable PMTU for IPv6 multicast.")    
    interface: list[Interface] = Field(default=None, description="Protocol Independent Multicast (PIM) interfaces.")    
    pim_sm_global: list[PimSmGlobal] = Field(default=None, description="PIM sparse-mode global settings.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
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
    "Multicast6Model",    "Multicast6Interface",    "Multicast6PimSmGlobal",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:32.832351Z
# ============================================================================