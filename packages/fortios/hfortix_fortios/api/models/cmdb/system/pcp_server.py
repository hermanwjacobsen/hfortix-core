"""
Pydantic Models for CMDB - system/pcp_server

Runtime validation models for system/pcp_server configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.system.pcp_server import 
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

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class PcpServerPools(BaseModel):
    """
    Child table model for pools.
    
    Configure PCP pools.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="PCP pool name.")    
    description: str | None = Field(max_length=127, default="", description="Description.")    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="ID.")    
    client_subnet: list[ClientSubnet] = Field(description="Subnets from which PCP requests are accepted.")    
    ext_intf: str = Field(max_length=35, default="", description="External interface name.")  # datasource: ['system.interface.name']    
    arp_reply: Literal["disable", "enable"] | None = Field(default="enable", description="Enable to respond to ARP requests for external IP (default = enable).")    
    extip: str = Field(default="", description="IP address or address range on the external interface that you want to map to an address on the internal network.")    
    extport: str = Field(default="", description="Incoming port number range that you want to map to a port number on the internal network.")    
    minimal_lifetime: int | None = Field(ge=60, le=300, default=120, description="Minimal lifetime of a PCP mapping in seconds (60 - 300, default = 120).")    
    maximal_lifetime: int | None = Field(ge=3600, le=604800, default=86400, description="Maximal lifetime of a PCP mapping in seconds (3600 - 604800, default = 86400).")    
    client_mapping_limit: int | None = Field(ge=0, le=65535, default=0, description="Mapping limit per client (0 - 65535, default = 0, 0 = unlimited).")    
    mapping_filter_limit: int | None = Field(ge=0, le=5, default=1, description="Filter limit per mapping (0 - 5, default = 1).")    
    allow_opcode: list[AllowOpcode] = Field(default="map peer announce", description="Allowed PCP opcode.")    
    third_party: Literal["allow", "disallow"] | None = Field(default="disallow", description="Allow/disallow third party option.")    
    third_party_subnet: list[ThirdPartySubnet] = Field(default=None, description="Subnets from which third party requests are accepted.")    
    multicast_announcement: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable multicast announcements.")    
    announcement_count: int | None = Field(ge=3, le=10, default=3, description="Number of multicast announcements.")    
    intl_intf: list[IntlIntf] = Field(description="Internal interface name.")    
    recycle_delay: int | None = Field(ge=0, le=3600, default=0, description="Minimum delay (in seconds) the PCP Server will wait before recycling mappings that have expired (0 - 3600, default = 0).")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class PcpServerModel(BaseModel):
    """
    Pydantic model for system/pcp_server configuration.
    
    Configure PCP server information.
    
    Validation Rules:        - status: pattern=        - pools: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable PCP server.")    
    pools: list[Pools] = Field(default=None, description="Configure PCP pools.")    
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
    "PcpServerModel",    "PcpServerPools",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:34.276100Z
# ============================================================================