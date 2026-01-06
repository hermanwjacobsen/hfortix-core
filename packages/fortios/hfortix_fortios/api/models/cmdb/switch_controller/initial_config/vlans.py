"""
Pydantic Models for CMDB - switch_controller/initial_config/vlans

Runtime validation models for switch_controller/initial_config/vlans configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.switch_controller.initial_config.vlans import 
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

class VlansModel(BaseModel):
    """
    Pydantic model for switch_controller/initial_config/vlans configuration.
    
    Configure initial template for auto-generated VLAN interfaces.
    
    Validation Rules:        - optional_vlans: pattern=        - default_vlan: max_length=63 pattern=        - quarantine: max_length=63 pattern=        - rspan: max_length=63 pattern=        - voice: max_length=63 pattern=        - video: max_length=63 pattern=        - nac: max_length=63 pattern=        - nac_segment: max_length=63 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    optional_vlans: Literal["enable", "disable"] | None = Field(default="enable", description="Auto-generate pre-configured VLANs upon switch discovery.")    
    default_vlan: str | None = Field(max_length=63, default="_default", description="Default VLAN (native) assigned to all switch ports upon discovery.")  # datasource: ['switch-controller.initial-config.template.name']    
    quarantine: str | None = Field(max_length=63, default="quarantine", description="VLAN for quarantined traffic.")  # datasource: ['switch-controller.initial-config.template.name']    
    rspan: str | None = Field(max_length=63, default="rspan", description="VLAN for RSPAN/ERSPAN mirrored traffic.")  # datasource: ['switch-controller.initial-config.template.name']    
    voice: str | None = Field(max_length=63, default="voice", description="VLAN dedicated for voice devices.")  # datasource: ['switch-controller.initial-config.template.name']    
    video: str | None = Field(max_length=63, default="video", description="VLAN dedicated for video devices.")  # datasource: ['switch-controller.initial-config.template.name']    
    nac: str | None = Field(max_length=63, default="onboarding", description="VLAN for NAC onboarding devices.")  # datasource: ['switch-controller.initial-config.template.name']    
    nac_segment: str | None = Field(max_length=63, default="nac_segment", description="VLAN for NAC segment primary interface.")  # datasource: ['switch-controller.initial-config.template.name']    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('default_vlan')
    @classmethod
    def validate_default_vlan(cls, v: Any) -> Any:
        """
        Validate default_vlan field.
        
        Datasource: ['switch-controller.initial-config.template.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('quarantine')
    @classmethod
    def validate_quarantine(cls, v: Any) -> Any:
        """
        Validate quarantine field.
        
        Datasource: ['switch-controller.initial-config.template.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('rspan')
    @classmethod
    def validate_rspan(cls, v: Any) -> Any:
        """
        Validate rspan field.
        
        Datasource: ['switch-controller.initial-config.template.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('voice')
    @classmethod
    def validate_voice(cls, v: Any) -> Any:
        """
        Validate voice field.
        
        Datasource: ['switch-controller.initial-config.template.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('video')
    @classmethod
    def validate_video(cls, v: Any) -> Any:
        """
        Validate video field.
        
        Datasource: ['switch-controller.initial-config.template.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('nac')
    @classmethod
    def validate_nac(cls, v: Any) -> Any:
        """
        Validate nac field.
        
        Datasource: ['switch-controller.initial-config.template.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('nac_segment')
    @classmethod
    def validate_nac_segment(cls, v: Any) -> Any:
        """
        Validate nac_segment field.
        
        Datasource: ['switch-controller.initial-config.template.name']
        
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
    "VlansModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:34.803801Z
# ============================================================================