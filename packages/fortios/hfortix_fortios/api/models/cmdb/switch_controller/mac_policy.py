"""
Pydantic Models for CMDB - switch_controller/mac_policy

Runtime validation models for switch_controller/mac_policy configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.switch_controller.mac_policy import 
    >>>
    >>> # Create with validation
    >>> obj = (
    ...     name=1,
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

class MacPolicyModel(BaseModel):
    """
    Pydantic model for switch_controller/mac_policy configuration.
    
    Configure MAC policy to be applied on the managed FortiSwitch devices through NAC device.
    
    Validation Rules:        - name: max_length=63 pattern=        - description: max_length=63 pattern=        - fortilink: max_length=15 pattern=        - vlan: max_length=15 pattern=        - traffic_policy: max_length=63 pattern=        - count: pattern=        - bounce_port_link: pattern=        - bounce_port_duration: min=1 max=30 pattern=        - poe_reset: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=63, default="", description="MAC policy name.")    
    description: str | None = Field(max_length=63, default="", description="Description for the MAC policy.")    
    fortilink: str = Field(max_length=15, default="", description="FortiLink interface for which this MAC policy belongs to.")  # datasource: ['system.interface.name']    
    vlan: str | None = Field(max_length=15, default="", description="Ingress traffic VLAN assignment for the MAC address matching this MAC policy.")  # datasource: ['system.interface.name']    
    traffic_policy: str | None = Field(max_length=63, default="", description="Traffic policy to be applied when using this MAC policy.")  # datasource: ['switch-controller.traffic-policy.name']    
    count: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable packet count on the NAC device.")    
    bounce_port_link: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable bouncing (administratively bring the link down, up) of a switch port where this mac-policy is applied.")    
    bounce_port_duration: int | None = Field(ge=1, le=30, default=5, description="Bounce duration in seconds of a switch port where this mac-policy is applied.")    
    poe_reset: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable POE reset of a switch port where this mac-policy is applied.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('fortilink')
    @classmethod
    def validate_fortilink(cls, v: Any) -> Any:
        """
        Validate fortilink field.
        
        Datasource: ['system.interface.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('vlan')
    @classmethod
    def validate_vlan(cls, v: Any) -> Any:
        """
        Validate vlan field.
        
        Datasource: ['system.interface.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
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
    "MacPolicyModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:33.218335Z
# ============================================================================