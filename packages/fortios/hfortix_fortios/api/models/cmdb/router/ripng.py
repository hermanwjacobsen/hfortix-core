"""
Pydantic Models for CMDB - router/ripng

Runtime validation models for router/ripng configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.router.ripng import 
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

class RipngDistance(BaseModel):
    """
    Child table model for distance.
    
    Distance.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=0, le=4294967295, default=0, description="Distance ID.")    
    distance: int = Field(ge=1, le=255, default=0, description="Distance (1 - 255).")    
    prefix6: str | None = Field(default="::/0", description="Distance prefix6.")    
    access_list6: str | None = Field(max_length=35, default="", description="Access list for route destination.")  # datasource: ['router.access-list6.name']
class RipngDistributeList(BaseModel):
    """
    Child table model for distribute-list.
    
    Distribute list.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=0, le=4294967295, default=0, description="Distribute list ID.")    
    status: Literal["enable", "disable"] | None = Field(default="disable", description="Status.")    
    direction: Literal["in", "out"] = Field(default="out", description="Distribute list direction.")    
    listname: str = Field(max_length=35, default="", description="Distribute access/prefix list name.")  # datasource: ['router.access-list6.name', 'router.prefix-list6.name']    
    interface: str | None = Field(max_length=15, default="", description="Distribute list interface name.")  # datasource: ['system.interface.name']
class RipngNeighbor(BaseModel):
    """
    Child table model for neighbor.
    
    Neighbor.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="Neighbor entry ID.")    
    ip6: str = Field(default="::", description="IPv6 link-local address.")    
    interface: str = Field(max_length=15, default="", description="Interface name.")  # datasource: ['system.interface.name']
class RipngNetwork(BaseModel):
    """
    Child table model for network.
    
    Network.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="Network entry ID.")    
    prefix: str | None = Field(default="::/0", description="Network IPv6 link-local prefix.")
class RipngAggregateAddress(BaseModel):
    """
    Child table model for aggregate-address.
    
    Aggregate address.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="Aggregate address entry ID.")    
    prefix6: str | None = Field(default="::/0", description="Aggregate address prefix.")
class RipngOffsetList(BaseModel):
    """
    Child table model for offset-list.
    
    Offset list.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=0, le=4294967295, default=0, description="Offset-list ID.")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Status.")    
    direction: Literal["in", "out"] = Field(default="out", description="Offset list direction.")    
    access_list6: str = Field(max_length=35, default="", description="IPv6 access list name.")  # datasource: ['router.access-list6.name']    
    offset: int = Field(ge=1, le=16, default=0, description="Offset.")    
    interface: str | None = Field(max_length=15, default="", description="Interface name.")  # datasource: ['system.interface.name']
class RipngPassiveInterface(BaseModel):
    """
    Child table model for passive-interface.
    
    Passive interface configuration.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Passive interface name.")  # datasource: ['system.interface.name']
class RipngRedistribute(BaseModel):
    """
    Child table model for redistribute.
    
    Redistribute configuration.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=35, default="", description="Redistribute name.")    
    status: Literal["enable", "disable"] | None = Field(default="disable", description="Status.")    
    metric: int | None = Field(ge=1, le=16, default=0, description="Redistribute metric setting.")    
    routemap: str | None = Field(max_length=35, default="", description="Route map name.")  # datasource: ['router.route-map.name']
class RipngInterface(BaseModel):
    """
    Child table model for interface.
    
    RIPng interface configuration.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=35, default="", description="Interface name.")  # datasource: ['system.interface.name']    
    split_horizon_status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable split horizon.")    
    split_horizon: Literal["poisoned", "regular"] | None = Field(default="poisoned", description="Enable/disable split horizon.")    
    flags: int | None = Field(ge=0, le=255, default=8, description="Flags.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class RipngModel(BaseModel):
    """
    Pydantic model for router/ripng configuration.
    
    Configure RIPng.
    
    Validation Rules:        - default_information_originate: pattern=        - default_metric: min=1 max=16 pattern=        - max_out_metric: min=0 max=15 pattern=        - distance: pattern=        - distribute_list: pattern=        - neighbor: pattern=        - network: pattern=        - aggregate_address: pattern=        - offset_list: pattern=        - passive_interface: pattern=        - redistribute: pattern=        - update_timer: min=5 max=2147483647 pattern=        - timeout_timer: min=5 max=2147483647 pattern=        - garbage_timer: min=5 max=2147483647 pattern=        - interface: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    default_information_originate: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable generation of default route.")    
    default_metric: int | None = Field(ge=1, le=16, default=1, description="Default metric.")    
    max_out_metric: int | None = Field(ge=0, le=15, default=0, description="Maximum metric allowed to output(0 means 'not set').")    
    distance: list[Distance] = Field(default=None, description="Distance.")    
    distribute_list: list[DistributeList] = Field(default=None, description="Distribute list.")    
    neighbor: list[Neighbor] = Field(default=None, description="Neighbor.")    
    network: list[Network] = Field(default=None, description="Network.")    
    aggregate_address: list[AggregateAddress] = Field(default=None, description="Aggregate address.")    
    offset_list: list[OffsetList] = Field(default=None, description="Offset list.")    
    passive_interface: list[PassiveInterface] = Field(default=None, description="Passive interface configuration.")    
    redistribute: list[Redistribute] = Field(default=None, description="Redistribute configuration.")    
    update_timer: int | None = Field(ge=5, le=2147483647, default=30, description="Update timer in seconds.")    
    timeout_timer: int | None = Field(ge=5, le=2147483647, default=180, description="Timeout timer in seconds.")    
    garbage_timer: int | None = Field(ge=5, le=2147483647, default=120, description="Garbage timer in seconds.")    
    interface: list[Interface] = Field(default=None, description="RIPng interface configuration.")    
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
    "RipngModel",    "RipngDistance",    "RipngDistributeList",    "RipngNeighbor",    "RipngNetwork",    "RipngAggregateAddress",    "RipngOffsetList",    "RipngPassiveInterface",    "RipngRedistribute",    "RipngInterface",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:35.719311Z
# ============================================================================