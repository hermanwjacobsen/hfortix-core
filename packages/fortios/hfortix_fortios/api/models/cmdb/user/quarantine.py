"""
Pydantic Models for CMDB - user/quarantine

Runtime validation models for user/quarantine configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.user.quarantine import 
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

class QuarantineTargets(BaseModel):
    """
    Child table model for targets.
    
    Quarantine entry to hold multiple MACs.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    entry: str = Field(max_length=63, default="", description="Quarantine entry name.")    
    description: str | None = Field(max_length=63, default="", description="Description for the quarantine entry.")    
    macs: list[Macs] = Field(default=None, description="Quarantine MACs.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class QuarantineModel(BaseModel):
    """
    Pydantic model for user/quarantine configuration.
    
    Configure quarantine support.
    
    Validation Rules:        - quarantine: pattern=        - traffic_policy: max_length=63 pattern=        - firewall_groups: max_length=79 pattern=        - targets: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    quarantine: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable quarantine.")    
    traffic_policy: str | None = Field(max_length=63, default="", description="Traffic policy for quarantined MACs.")  # datasource: ['switch-controller.traffic-policy.name']    
    firewall_groups: str | None = Field(max_length=79, default="", description="Firewall address group which includes all quarantine MAC address.")  # datasource: ['firewall.addrgrp.name']    
    targets: list[Targets] = Field(default=None, description="Quarantine entry to hold multiple MACs.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('traffic_policy')
    @classmethod
    def validate_traffic_policy(cls, v: Any) -> Any:
        """
        Validate traffic_policy field.
        
        Datasource: ['switch-controller.traffic-policy.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('firewall_groups')
    @classmethod
    def validate_firewall_groups(cls, v: Any) -> Any:
        """
        Validate firewall_groups field.
        
        Datasource: ['firewall.addrgrp.name']
        
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
    "QuarantineModel",    "QuarantineTargets",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:33.347992Z
# ============================================================================