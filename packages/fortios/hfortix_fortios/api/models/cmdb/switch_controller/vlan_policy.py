"""
Pydantic Models for CMDB - switch_controller/vlan_policy

Runtime validation models for switch_controller/vlan_policy configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.switch_controller.vlan_policy import 
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
# Child Table Models
# ============================================================================

class VlanPolicyAllowedVlans(BaseModel):
    """
    Child table model for allowed-vlans.
    
    Allowed VLANs to be applied when using this VLAN policy.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    vlan_name: str = Field(max_length=79, default="", description="VLAN name.")  # datasource: ['system.interface.name']
class VlanPolicyUntaggedVlans(BaseModel):
    """
    Child table model for untagged-vlans.
    
    Untagged VLANs to be applied when using this VLAN policy.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    vlan_name: str = Field(max_length=79, default="", description="VLAN name.")  # datasource: ['system.interface.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class VlanPolicyModel(BaseModel):
    """
    Pydantic model for switch_controller/vlan_policy configuration.
    
    Configure VLAN policy to be applied on the managed FortiSwitch ports through dynamic-port-policy.
    
    Validation Rules:        - name: max_length=63 pattern=        - description: max_length=63 pattern=        - fortilink: max_length=15 pattern=        - vlan: max_length=15 pattern=        - allowed_vlans: pattern=        - untagged_vlans: pattern=        - allowed_vlans_all: pattern=        - discard_mode: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=63, default="", description="VLAN policy name.")    
    description: str | None = Field(max_length=63, default="", description="Description for the VLAN policy.")    
    fortilink: str = Field(max_length=15, default="", description="FortiLink interface for which this VLAN policy belongs to.")  # datasource: ['system.interface.name']    
    vlan: str | None = Field(max_length=15, default="", description="Native VLAN to be applied when using this VLAN policy.")  # datasource: ['system.interface.name']    
    allowed_vlans: list[AllowedVlans] = Field(default=None, description="Allowed VLANs to be applied when using this VLAN policy.")    
    untagged_vlans: list[UntaggedVlans] = Field(default=None, description="Untagged VLANs to be applied when using this VLAN policy.")    
    allowed_vlans_all: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable all defined VLANs when using this VLAN policy.")    
    discard_mode: Literal["none", "all-untagged", "all-tagged"] | None = Field(default="none", description="Discard mode to be applied when using this VLAN policy.")    
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
    "VlanPolicyModel",    "VlanPolicyAllowedVlans",    "VlanPolicyUntaggedVlans",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:34.449101Z
# ============================================================================