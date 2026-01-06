"""
Pydantic Models for CMDB - firewall/internet_service_custom

Runtime validation models for firewall/internet_service_custom configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.firewall.internet_service_custom import 
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
from typing import Any, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class InternetServiceCustomEntry(BaseModel):
    """
    Child table model for entry.
    
    Entries added to the Internet Service database and custom database.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=255, default=0, description="Entry ID(1-255).")    
    addr_mode: Literal["ipv4", "ipv6"] | None = Field(default="ipv4", description="Address mode (IPv4 or IPv6).")    
    protocol: int | None = Field(ge=0, le=255, default=0, description="Integer value for the protocol type as defined by IANA (0 - 255).")    
    port_range: list[PortRange] = Field(default=None, description="Port ranges in the custom entry.")    
    dst: list[Dst] = Field(default=None, description="Destination address or address group name.")    
    dst6: list[Dst6] = Field(default=None, description="Destination address6 or address6 group name.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class InternetServiceCustomModel(BaseModel):
    """
    Pydantic model for firewall/internet_service_custom configuration.
    
    Configure custom Internet Services.
    
    Validation Rules:        - name: max_length=63 pattern=        - reputation: min=0 max=4294967295 pattern=        - comment: max_length=255 pattern=        - entry: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=63, default="", description="Internet Service name.")    
    reputation: int | None = Field(ge=0, le=4294967295, default=3, description="Reputation level of the custom Internet Service.")  # datasource: ['firewall.internet-service-reputation.id']    
    comment: str | None = Field(max_length=255, default=None, description="Comment.")    
    entry: list[Entry] = Field(default=None, description="Entries added to the Internet Service database and custom database.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('reputation')
    @classmethod
    def validate_reputation(cls, v: Any) -> Any:
        """
        Validate reputation field.
        
        Datasource: ['firewall.internet-service-reputation.id']
        
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
    "InternetServiceCustomModel",    "InternetServiceCustomEntry",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:35.706985Z
# ============================================================================