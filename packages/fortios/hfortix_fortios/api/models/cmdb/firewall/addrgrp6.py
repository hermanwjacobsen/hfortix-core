"""
Pydantic Models for CMDB - firewall/addrgrp6

Runtime validation models for firewall/addrgrp6 configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.firewall.addrgrp6 import 
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

class Addrgrp6Member(BaseModel):
    """
    Child table model for member.
    
    Address objects contained within the group.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address6/addrgrp6 name.")  # datasource: ['firewall.address6.name', 'firewall.addrgrp6.name']
class Addrgrp6ExcludeMember(BaseModel):
    """
    Child table model for exclude-member.
    
    Address6 exclusion member.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address6 name.")  # datasource: ['firewall.address6.name', 'firewall.addrgrp6.name']
class Addrgrp6Tagging(BaseModel):
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

class Addrgrp6Model(BaseModel):
    """
    Pydantic model for firewall/addrgrp6 configuration.
    
    Configure IPv6 address groups.
    
    Validation Rules:        - name: max_length=79 pattern=        - uuid: pattern=        - color: min=0 max=32 pattern=        - comment: max_length=255 pattern=        - member: pattern=        - exclude: pattern=        - exclude_member: pattern=        - tagging: pattern=        - fabric_object: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str = Field(max_length=79, default="", description="IPv6 address group name.")    
    uuid: str | None = Field(default="00000000-0000-0000-0000-000000000000", description="Universally Unique Identifier (UUID; automatically assigned but can be manually reset).")    
    color: int | None = Field(ge=0, le=32, default=0, description="Integer value to determine the color of the icon in the GUI (1 - 32, default = 0, which sets the value to 1).")    
    comment: str | None = Field(max_length=255, default=None, description="Comment.")    
    member: list[Member] = Field(default=None, description="Address objects contained within the group.")    
    exclude: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable address6 exclusion.")    
    exclude_member: list[ExcludeMember] = Field(description="Address6 exclusion member.")    
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
    "Addrgrp6Model",    "Addrgrp6Member",    "Addrgrp6ExcludeMember",    "Addrgrp6Tagging",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:33.675681Z
# ============================================================================