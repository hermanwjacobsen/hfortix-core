"""
Pydantic Models for CMDB - casb/attribute_match

Runtime validation models for casb/attribute_match configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.casb.attribute_match import 
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

class AttributeMatchMatch(BaseModel):
    """
    Child table model for match.
    
    CASB tenant match rules.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="CASB attribute match rule ID.")    
    rule_strategy: Literal["and", "or"] | None = Field(default="and", description="CASB attribute match rule strategy.")    
    rule: list[Rule] = Field(default=None, description="CASB attribute match rule.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class AttributeMatchModel(BaseModel):
    """
    Pydantic model for casb/attribute_match configuration.
    
    Configure CASB attribute match rule.
    
    Validation Rules:        - name: max_length=79 pattern=        - application: max_length=79 pattern=        - match_strategy: pattern=        - match: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=79, default="", description="CASB attribute match name.")    
    application: str = Field(max_length=79, default="", description="CASB attribute application name.")  # datasource: ['casb.saas-application.name']    
    match_strategy: Literal["or", "and", "subset"] | None = Field(default="or", description="CASB attribute match strategy.")    
    match: list[Match] = Field(default=None, description="CASB tenant match rules.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('application')
    @classmethod
    def validate_application(cls, v: Any) -> Any:
        """
        Validate application field.
        
        Datasource: ['casb.saas-application.name']
        
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
    "AttributeMatchModel",    "AttributeMatchMatch",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:33.121495Z
# ============================================================================