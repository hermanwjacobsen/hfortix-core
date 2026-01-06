"""
Pydantic Models for CMDB - system/vdom_radius_server

Runtime validation models for system/vdom_radius_server configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.system.vdom_radius_server import 
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

class VdomRadiusServerModel(BaseModel):
    """
    Pydantic model for system/vdom_radius_server configuration.
    
    Configure a RADIUS server to use as a RADIUS Single Sign On (RSSO) server for this VDOM.
    
    Validation Rules:        - name: max_length=31 pattern=        - status: pattern=        - radius_server_vdom: max_length=31 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=31, default="", description="Name of the VDOM that you are adding the RADIUS server to.")  # datasource: ['system.vdom.name']    
    status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable the RSSO RADIUS server for this VDOM.")    
    radius_server_vdom: str = Field(max_length=31, default="", description="Use this option to select another VDOM containing a VDOM RSSO RADIUS server to use for the current VDOM.")  # datasource: ['system.vdom.name']    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('name')
    @classmethod
    def validate_name(cls, v: Any) -> Any:
        """
        Validate name field.
        
        Datasource: ['system.vdom.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('radius_server_vdom')
    @classmethod
    def validate_radius_server_vdom(cls, v: Any) -> Any:
        """
        Validate radius_server_vdom field.
        
        Datasource: ['system.vdom.name']
        
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
    "VdomRadiusServerModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:32.809705Z
# ============================================================================