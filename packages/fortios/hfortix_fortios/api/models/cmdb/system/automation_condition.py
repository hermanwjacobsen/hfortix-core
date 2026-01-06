"""
Pydantic Models for CMDB - system/automation_condition

Runtime validation models for system/automation_condition configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.system.automation_condition import 
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

class AutomationConditionModel(BaseModel):
    """
    Pydantic model for system/automation_condition configuration.
    
    Condition for automation stitches.
    
    Validation Rules:        - name: max_length=35 pattern=        - description: max_length=255 pattern=        - condition_type: pattern=        - cpu_usage_percent: min=0 max=100 pattern=        - mem_usage_percent: min=0 max=100 pattern=        - vdom: max_length=31 pattern=        - vpn_tunnel_name: max_length=79 pattern=        - vpn_tunnel_state: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=35, default="", description="Name.")    
    description: str | None = Field(max_length=255, default=None, description="Description.")    
    condition_type: Literal["cpu", "memory", "vpn"] | None = Field(default="cpu", description="Condition type.")    
    cpu_usage_percent: int = Field(ge=0, le=100, default=0, description="CPU usage reaches specified percentage.")    
    mem_usage_percent: int = Field(ge=0, le=100, default=0, description="Memory usage reaches specified percentage.")    
    vdom: str = Field(max_length=31, default="root", description="Virtual domain which the tunnel belongs to.")  # datasource: ['system.vdom.name']    
    vpn_tunnel_name: str = Field(max_length=79, default="", description="VPN tunnel name.")    
    vpn_tunnel_state: Literal["tunnel-up", "tunnel-down"] | None = Field(default="tunnel-up", description="VPN tunnel state.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('vdom')
    @classmethod
    def validate_vdom(cls, v: Any) -> Any:
        """
        Validate vdom field.
        
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
    "AutomationConditionModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:35.248271Z
# ============================================================================