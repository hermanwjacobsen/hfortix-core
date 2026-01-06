"""
Pydantic Models for CMDB - vpn/l2tp

Runtime validation models for vpn/l2tp configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.vpn.l2tp import 
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
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class L2tpModel(BaseModel):
    """
    Pydantic model for vpn/l2tp configuration.
    
    Configure L2TP.
    
    Validation Rules:        - status: pattern=        - eip: pattern=        - sip: pattern=        - usrgrp: max_length=35 pattern=        - enforce_ipsec: pattern=        - lcp_echo_interval: min=0 max=32767 pattern=        - lcp_max_echo_fails: min=0 max=32767 pattern=        - hello_interval: min=0 max=3600 pattern=        - compress: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    status: Literal["enable", "disable"] = Field(default="disable", description="Enable/disable FortiGate as a L2TP gateway.")    
    eip: str = Field(default="0.0.0.0", description="End IP.")    
    sip: str = Field(default="0.0.0.0", description="Start IP.")    
    usrgrp: str = Field(max_length=35, default="", description="User group.")  # datasource: ['user.group.name']    
    enforce_ipsec: Literal["enable", "disable"] = Field(default="disable", description="Enable/disable IPsec enforcement.")    
    lcp_echo_interval: int | None = Field(ge=0, le=32767, default=5, description="Time in seconds between PPPoE Link Control Protocol (LCP) echo requests.")    
    lcp_max_echo_fails: int | None = Field(ge=0, le=32767, default=3, description="Maximum number of missed LCP echo messages before disconnect.")    
    hello_interval: int | None = Field(ge=0, le=3600, default=60, description="L2TP hello message interval in seconds (0 - 3600 sec, default = 60).")    
    compress: Literal["enable", "disable"] = Field(default="disable", description="Enable/disable data compression.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('usrgrp')
    @classmethod
    def validate_usrgrp(cls, v: Any) -> Any:
        """
        Validate usrgrp field.
        
        Datasource: ['user.group.name']
        
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
    "L2tpModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:34.439605Z
# ============================================================================