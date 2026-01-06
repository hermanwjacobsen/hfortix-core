"""
Pydantic Models for CMDB - router/bfd

Runtime validation models for router/bfd configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.router.bfd import 
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
# Child Table Models
# ============================================================================

class BfdNeighbor(BaseModel):
    """
    Child table model for neighbor.
    
    Neighbor.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    ip: str = Field(default="0.0.0.0", description="IPv4 address of the BFD neighbor.")    
    interface: str = Field(max_length=15, default="", description="Interface name.")  # datasource: ['system.interface.name']
class BfdMultihopTemplate(BaseModel):
    """
    Child table model for multihop-template.
    
    BFD multi-hop template table.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=0, le=4294967295, default=0, description="ID.")    
    src: str = Field(default="0.0.0.0 0.0.0.0", description="Source prefix.")    
    dst: str = Field(default="0.0.0.0 0.0.0.0", description="Destination prefix.")    
    bfd_desired_min_tx: int | None = Field(ge=100, le=30000, default=250, description="BFD desired minimal transmit interval (milliseconds).")    
    bfd_required_min_rx: int | None = Field(ge=100, le=30000, default=250, description="BFD required minimal receive interval (milliseconds).")    
    bfd_detect_mult: int | None = Field(ge=3, le=50, default=3, description="BFD detection multiplier.")    
    auth_mode: Literal["none", "md5"] | None = Field(default="none", description="Authentication mode.")    
    md5_key: Any = Field(max_length=16, default=None, description="MD5 key of key ID 1.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class BfdModel(BaseModel):
    """
    Pydantic model for router/bfd configuration.
    
    Configure BFD.
    
    Validation Rules:        - neighbor: pattern=        - multihop_template: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    neighbor: list[Neighbor] = Field(default=None, description="Neighbor.")    
    multihop_template: list[MultihopTemplate] = Field(default=None, description="BFD multi-hop template table.")    
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
    "BfdModel",    "BfdNeighbor",    "BfdMultihopTemplate",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:35.797187Z
# ============================================================================