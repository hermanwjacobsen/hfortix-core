"""
Pydantic Models for CMDB - system/automation_stitch

Runtime validation models for system/automation_stitch configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.system.automation_stitch import 
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

class AutomationStitchCondition(BaseModel):
    """
    Child table model for condition.
    
    Automation conditions.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Condition name.")  # datasource: ['system.automation-condition.name']
class AutomationStitchActions(BaseModel):
    """
    Child table model for actions.
    
    Configure stitch actions.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="Entry ID.")    
    action: str = Field(max_length=64, default="", description="Action name.")  # datasource: ['system.automation-action.name']    
    delay: int | None = Field(ge=0, le=3600, default=0, description="Delay before execution (in seconds).")    
    required: Literal["enable", "disable"] | None = Field(default="disable", description="Required in action chain.")
class AutomationStitchDestination(BaseModel):
    """
    Child table model for destination.
    
    Serial number/HA group-name of destination devices.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Destination name.")  # datasource: ['system.automation-destination.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class AutomationStitchModel(BaseModel):
    """
    Pydantic model for system/automation_stitch configuration.
    
    Automation stitches.
    
    Validation Rules:        - name: max_length=35 pattern=        - description: max_length=255 pattern=        - status: pattern=        - trigger: max_length=35 pattern=        - condition: pattern=        - condition_logic: pattern=        - actions: pattern=        - destination: pattern=    """
    
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
    status: Literal["enable", "disable"] = Field(default="enable", description="Enable/disable this stitch.")    
    trigger: str = Field(max_length=35, default="", description="Trigger name.")  # datasource: ['system.automation-trigger.name']    
    condition: list[Condition] = Field(default=None, description="Automation conditions.")    
    condition_logic: Literal["and", "or"] = Field(default="and", description="Apply AND/OR logic to the specified automation conditions.")    
    actions: list[Actions] = Field(default=None, description="Configure stitch actions.")    
    destination: list[Destination] = Field(default=None, description="Serial number/HA group-name of destination devices.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('trigger')
    @classmethod
    def validate_trigger(cls, v: Any) -> Any:
        """
        Validate trigger field.
        
        Datasource: ['system.automation-trigger.name']
        
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
    "AutomationStitchModel",    "AutomationStitchCondition",    "AutomationStitchActions",    "AutomationStitchDestination",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:34.712342Z
# ============================================================================