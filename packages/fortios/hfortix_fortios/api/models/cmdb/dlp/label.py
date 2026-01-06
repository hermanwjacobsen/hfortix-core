"""
Pydantic Models for CMDB - dlp/label

Runtime validation models for dlp/label configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.dlp.label import 
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

class LabelEntries(BaseModel):
    """
    Child table model for entries.
    
    DLP label entries.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=1, le=32, default=0, description="ID.")    
    fortidata_label_name: str = Field(max_length=127, default="", description="Name of FortiData label")  # datasource: ['dlp.fdata-label.name']    
    mpip_label_name: str = Field(max_length=127, default="", description="Name of MPIP label.")  # datasource: ['dlp.mpip-label.name']    
    guid: str = Field(max_length=36, default="", description="MPIP label guid.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class LabelModel(BaseModel):
    """
    Pydantic model for dlp/label configuration.
    
    Configure labels used by DLP blocking.
    
    Validation Rules:        - name: max_length=35 pattern=        - type: pattern=        - mpip_type: pattern=        - connector: max_length=35 pattern=        - comment: max_length=255 pattern=        - entries: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=35, default="", description="Name of table containing the label.")    
    type: Literal["mpip", "fortidata"] | None = Field(default="mpip", description="Label type.")    
    mpip_type: Literal["remote", "local"] | None = Field(default="remote", description="MPIP label type.")    
    connector: str | None = Field(max_length=35, default="", description="Name of SDN connector.")  # datasource: ['system.sdn-connector.name']    
    comment: str | None = Field(max_length=255, default=None, description="Optional comments.")    
    entries: list[Entries] = Field(description="DLP label entries.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('connector')
    @classmethod
    def validate_connector(cls, v: Any) -> Any:
        """
        Validate connector field.
        
        Datasource: ['system.sdn-connector.name']
        
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
    "LabelModel",    "LabelEntries",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:34.031836Z
# ============================================================================