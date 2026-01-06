"""
Pydantic Models for CMDB - switch_controller/fortilink_settings

Runtime validation models for switch_controller/fortilink_settings configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.switch_controller.fortilink_settings import 
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

class FortilinkSettingsNacPorts(BaseModel):
    """
    Child table model for nac-ports.
    
    NAC specific configuration.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    onboarding_vlan: str = Field(max_length=15, default="", description="Default NAC Onboarding VLAN when NAC devices are discovered.")  # datasource: ['system.interface.name']    
    lan_segment: Literal["enabled", "disabled"] | None = Field(default="disabled", description="Enable/disable LAN segment feature on the FortiLink interface.")    
    nac_lan_interface: str = Field(max_length=15, default="", description="Configure NAC LAN interface.")  # datasource: ['system.interface.name']    
    nac_segment_vlans: list[NacSegmentVlans] = Field(description="Configure NAC segment VLANs.")    
    parent_key: str | None = Field(max_length=35, default="", description="Parent key name.")    
    member_change: int | None = Field(ge=0, le=255, default=0, description="Member change flag.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class FortilinkSettingsModel(BaseModel):
    """
    Pydantic model for switch_controller/fortilink_settings configuration.
    
    Configure integrated FortiLink settings for FortiSwitch.
    
    Validation Rules:        - name: max_length=35 pattern=        - fortilink: max_length=15 pattern=        - inactive_timer: min=1 max=1440 pattern=        - link_down_flush: pattern=        - access_vlan_mode: pattern=        - nac_ports: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=35, default="", description="FortiLink settings name.")    
    fortilink: str | None = Field(max_length=15, default="", description="FortiLink interface to which this fortilink-setting belongs.")  # datasource: ['system.interface.name']    
    inactive_timer: int | None = Field(ge=1, le=1440, default=15, description="Time interval(minutes) to be included in the inactive devices expiry calculation (mac age-out + inactive-time + periodic scan interval).")    
    link_down_flush: Literal["disable", "enable"] | None = Field(default="enable", description="Clear NAC and dynamic devices on switch ports on link down event.")    
    access_vlan_mode: Literal["legacy", "fail-open", "fail-close"] | None = Field(default="legacy", description="Intra VLAN traffic behavior with loss of connection to the FortiGate.")    
    nac_ports: list[NacPorts] = Field(default=None, description="NAC specific configuration.")    
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
    "FortilinkSettingsModel",    "FortilinkSettingsNacPorts",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:33.873044Z
# ============================================================================