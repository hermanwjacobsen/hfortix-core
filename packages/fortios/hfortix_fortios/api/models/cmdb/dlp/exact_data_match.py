"""
Pydantic Models for CMDB - dlp/exact_data_match

Runtime validation models for dlp/exact_data_match configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.dlp.exact_data_match import 
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

from pydantic import BaseModel, Field
from typing import Any

# ============================================================================
# Child Table Models
# ============================================================================

class ExactDataMatchColumns(BaseModel):
    """
    Child table model for columns.
    
    DLP exact-data-match column types.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    index: int | None = Field(ge=1, le=32, default=0, description="Column index.")    
    type: str = Field(max_length=35, default="", description="Data-type for this column.")  # datasource: ['dlp.data-type.name']    
    optional: Literal["enable", "disable"] = Field(default="disable", description="Enable/disable optional match.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class ExactDataMatchModel(BaseModel):
    """
    Pydantic model for dlp/exact_data_match configuration.
    
    Configure exact-data-match template used by DLP scan.
    
    Validation Rules:        - name: max_length=35 pattern=        - optional: min=0 max=32 pattern=        - data: max_length=35 pattern=        - columns: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str = Field(max_length=35, default="", description="Name of table containing the exact-data-match template.")    
    optional: int = Field(ge=0, le=32, default=0, description="Number of optional columns need to match.")    
    data: str = Field(max_length=35, default="", description="External resource for exact data match.")  # datasource: ['system.external-resource.name']    
    columns: list[Columns] = Field(description="DLP exact-data-match column types.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('data')
    @classmethod
    def validate_data(cls, v: Any) -> Any:
        """
        Validate data field.
        
        Datasource: ['system.external-resource.name']
        
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
    "ExactDataMatchModel",    "ExactDataMatchColumns",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:35.086220Z
# ============================================================================