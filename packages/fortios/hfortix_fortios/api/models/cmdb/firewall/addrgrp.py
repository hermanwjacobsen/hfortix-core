"""
Pydantic Models for CMDB - firewall/addrgrp

Runtime validation models for firewall/addrgrp configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.firewall.addrgrp import 
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
from uuid import UUID

# ============================================================================
# Child Table Models
# ============================================================================

class AddrgrpMember(BaseModel):
    """
    Child table model for member.
    
    Address objects contained within the group.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name']
class AddrgrpExcludeMember(BaseModel):
    """
    Child table model for exclude-member.
    
    Address exclusion member.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name']
class AddrgrpTagging(BaseModel):
    """
    Child table model for tagging.
    
    Config object tagging.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=63, default="", description="Tagging entry name.")    
    category: str | None = Field(max_length=63, default="", description="Tag category.")  # datasource: ['system.object-tagging.category']    
    tags: list[Tags] = Field(default=None, description="Tags.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class AddrgrpModel(BaseModel):
    """
    Pydantic model for firewall/addrgrp configuration.
    
    Configure IPv4 address groups.
    
    Validation Rules:        - name: max_length=79 pattern=        - type: pattern=        - category: pattern=        - allow_routing: pattern=        - member: pattern=        - comment: max_length=255 pattern=        - uuid: pattern=        - exclude: pattern=        - exclude_member: pattern=        - color: min=0 max=32 pattern=        - tagging: pattern=        - fabric_object: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str = Field(max_length=79, default="", description="Address group name.")    
    type: Literal["default", "folder"] | None = Field(default="default", description="Address group type.")    
    category: Literal["default", "ztna-ems-tag", "ztna-geo-tag"] | None = Field(default="default", description="Address group category.")    
    allow_routing: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable use of this group in routing configurations.")    
    member: list[Member] = Field(default=None, description="Address objects contained within the group.")    
    comment: str | None = Field(max_length=255, default=None, description="Comment.")    
    uuid: str | None = Field(default="00000000-0000-0000-0000-000000000000", description="Universally Unique Identifier (UUID; automatically assigned but can be manually reset).")    
    exclude: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable address exclusion.")    
    exclude_member: list[ExcludeMember] = Field(description="Address exclusion member.")    
    color: int | None = Field(ge=0, le=32, default=0, description="Color of icon on the GUI.")    
    tagging: list[Tagging] = Field(default=None, description="Config object tagging.")    
    fabric_object: Literal["enable", "disable"] | None = Field(default="disable", description="Security Fabric global object setting.")    
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
    "AddrgrpModel",    "AddrgrpMember",    "AddrgrpExcludeMember",    "AddrgrpTagging",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:33.243253Z
# ============================================================================