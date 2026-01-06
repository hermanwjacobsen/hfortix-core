"""
Pydantic Models for CMDB - dlp/sensor

Runtime validation models for dlp/sensor configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.dlp.sensor import 
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

class SensorEntries(BaseModel):
    """
    Child table model for entries.
    
    DLP sensor entries.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=1, le=32, default=0, description="ID.")    
    dictionary: str = Field(max_length=35, default="", description="Select a DLP dictionary or exact-data-match.")  # datasource: ['dlp.dictionary.name', 'dlp.exact-data-match.name']    
    count: int = Field(ge=1, le=255, default=1, description="Count of dictionary matches to trigger sensor entry match (Dictionary might not be able to trigger more than once based on its 'repeat' option, 1 - 255, default = 1).")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable this entry.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class SensorModel(BaseModel):
    """
    Pydantic model for dlp/sensor configuration.
    
    Configure sensors used by DLP blocking.
    
    Validation Rules:        - name: max_length=35 pattern=        - match_type: pattern=        - eval: max_length=255 pattern=        - comment: max_length=255 pattern=        - entries: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str = Field(max_length=35, default="", description="Name of table containing the sensor.")    
    match_type: Literal["match-all", "match-any", "match-eval"] = Field(default="match-any", description="Logical relation between entries (default = match-any).")    
    eval: str | None = Field(max_length=255, default="", description="Expression to evaluate.")    
    comment: str | None = Field(max_length=255, default=None, description="Optional comments.")    
    entries: list[Entries] = Field(description="DLP sensor entries.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
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
    "SensorModel",    "SensorEntries",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:35.169079Z
# ============================================================================