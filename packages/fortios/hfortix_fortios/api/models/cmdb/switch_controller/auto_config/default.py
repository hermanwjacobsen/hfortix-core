"""
Pydantic Models for CMDB - switch_controller/auto_config/default

Runtime validation models for switch_controller/auto_config/default configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.switch_controller.auto_config.default import 
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

from pydantic import BaseModel, Field
from typing import Any, Optional

# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class DefaultModel(BaseModel):
    """
    Pydantic model for switch_controller/auto_config/default configuration.
    
    Policies which are applied automatically to all ISL/ICL/FortiLink interfaces.
    
    Validation Rules:        - fgt_policy: max_length=63 pattern=        - isl_policy: max_length=63 pattern=        - icl_policy: max_length=63 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    fgt_policy: str | None = Field(max_length=63, default="default", description="Default FortiLink auto-config policy.")  # datasource: ['switch-controller.auto-config.policy.name']    
    isl_policy: str | None = Field(max_length=63, default="default", description="Default ISL auto-config policy.")  # datasource: ['switch-controller.auto-config.policy.name']    
    icl_policy: str | None = Field(max_length=63, default="default-icl", description="Default ICL auto-config policy.")  # datasource: ['switch-controller.auto-config.policy.name']    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('fgt_policy')
    @classmethod
    def validate_fgt_policy(cls, v: Any) -> Any:
        """
        Validate fgt_policy field.
        
        Datasource: ['switch-controller.auto-config.policy.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('isl_policy')
    @classmethod
    def validate_isl_policy(cls, v: Any) -> Any:
        """
        Validate isl_policy field.
        
        Datasource: ['switch-controller.auto-config.policy.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('icl_policy')
    @classmethod
    def validate_icl_policy(cls, v: Any) -> Any:
        """
        Validate icl_policy field.
        
        Datasource: ['switch-controller.auto-config.policy.name']
        
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
    "DefaultModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:34.282822Z
# ============================================================================