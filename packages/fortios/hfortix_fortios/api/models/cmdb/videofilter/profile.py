"""
Pydantic Models for CMDB - videofilter/profile

Runtime validation models for videofilter/profile configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.videofilter.profile import 
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

class ProfileFilters(BaseModel):
    """
    Child table model for filters.
    
    YouTube filter entries.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=0, le=4294967295, default=0, description="ID.")    
    comment: str | None = Field(max_length=255, default=None, description="Comment.")    
    type: TypeEnum = Field(default="category", description="Filter type.")    
    keyword: int = Field(ge=0, le=4294967295, default=0, description="Video filter keyword ID.")  # datasource: ['videofilter.keyword.id']    
    category: str = Field(max_length=7, default="", description="FortiGuard category ID.")    
    channel: str = Field(max_length=255, default="", description="Channel ID.")    
    action: Literal["allow", "monitor", "block"] | None = Field(default="monitor", description="Video filter action.")    
    log: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable logging.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class ProfileModel(BaseModel):
    """
    Pydantic model for videofilter/profile configuration.
    
    Configure VideoFilter profile.
    
    Validation Rules:        - name: max_length=47 pattern=        - comment: max_length=255 pattern=        - filters: pattern=        - youtube: pattern=        - vimeo: pattern=        - dailymotion: pattern=        - replacemsg_group: max_length=35 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str = Field(max_length=47, default="", description="Name.")    
    comment: str | None = Field(max_length=255, default=None, description="Comment.")    
    filters: list[Filters] = Field(description="YouTube filter entries.")    
    youtube: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable YouTube video source.")    
    vimeo: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable Vimeo video source.")    
    dailymotion: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable Dailymotion video source.")    
    replacemsg_group: str | None = Field(max_length=35, default="", description="Replacement message group.")  # datasource: ['system.replacemsg-group.name']    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('replacemsg_group')
    @classmethod
    def validate_replacemsg_group(cls, v: Any) -> Any:
        """
        Validate replacemsg_group field.
        
        Datasource: ['system.replacemsg-group.name']
        
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
    "ProfileModel",    "ProfileFilters",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:34.753341Z
# ============================================================================