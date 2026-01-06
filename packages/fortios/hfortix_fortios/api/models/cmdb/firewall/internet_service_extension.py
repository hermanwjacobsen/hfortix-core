"""
Pydantic Models for CMDB - firewall/internet_service_extension

Runtime validation models for firewall/internet_service_extension configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.firewall.internet_service_extension import 
    >>>
    >>> # Create with validation
    >>> obj = (
    ...     id=1,
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

class InternetServiceExtensionEntry(BaseModel):
    """
    Child table model for entry.
    
    Entries added to the Internet Service extension database.
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
class InternetServiceExtensionDisableEntry(BaseModel):
    """
    Child table model for disable-entry.
    
    Disable entries in the Internet Service database.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="Disable entry ID.")    
    addr_mode: Literal["ipv4", "ipv6"] | None = Field(default="ipv4", description="Address mode (IPv4 or IPv6).")    
    protocol: int = Field(ge=0, le=255, default=0, description="Integer value for the protocol type as defined by IANA (0 - 255).")    
    port_range: list[PortRange] = Field(default=None, description="Port ranges in the disable entry.")    
    ip_range: list[IpRange] = Field(default=None, description="IPv4 ranges in the disable entry.")    
    ip6_range: list[Ip6Range] = Field(default=None, description="IPv6 ranges in the disable entry.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class InternetServiceExtensionModel(BaseModel):
    """
    Pydantic model for firewall/internet_service_extension configuration.
    
    Configure Internet Services Extension.
    
    Validation Rules:        - id: min=0 max=4294967295 pattern=        - comment: max_length=255 pattern=        - entry: pattern=        - disable_entry: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="Internet Service ID in the Internet Service database.")  # datasource: ['firewall.internet-service.id']    
    comment: str | None = Field(max_length=255, default=None, description="Comment.")    
    entry: list[Entry] = Field(default=None, description="Entries added to the Internet Service extension database.")    
    disable_entry: list[DisableEntry] = Field(default=None, description="Disable entries in the Internet Service database.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('id')
    @classmethod
    def validate_id(cls, v: Any) -> Any:
        """
        Validate id field.
        
        Datasource: ['firewall.internet-service.id']
        
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
    "InternetServiceExtensionModel",    "InternetServiceExtensionEntry",    "InternetServiceExtensionDisableEntry",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:34.757163Z
# ============================================================================