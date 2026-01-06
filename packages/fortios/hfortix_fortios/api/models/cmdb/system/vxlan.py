"""
Pydantic Models for CMDB - system/vxlan

Runtime validation models for system/vxlan configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.system.vxlan import 
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
from enum import Enum

# ============================================================================
# Child Table Models
# ============================================================================

class VxlanRemoteIp(BaseModel):
    """
    Child table model for remote-ip.
    
    IPv4 address of the VXLAN interface on the device at the remote end of the VXLAN.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    ip: str = Field(max_length=15, default="", description="IPv4 address.")
class VxlanRemoteIp6(BaseModel):
    """
    Child table model for remote-ip6.
    
    IPv6 IP address of the VXLAN interface on the device at the remote end of the VXLAN.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    ip6: str = Field(max_length=45, default="", description="IPv6 address.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class VxlanIp_versionEnum(str, Enum):
    """Allowed values for ip_version field."""
    IPV4_UNICAST = "ipv4-unicast"    IPV6_UNICAST = "ipv6-unicast"    IPV4_MULTICAST = "ipv4-multicast"    IPV6_MULTICAST = "ipv6-multicast"

# ============================================================================
# Main Model
# ============================================================================

class VxlanModel(BaseModel):
    """
    Pydantic model for system/vxlan configuration.
    
    Configure VXLAN devices.
    
    Validation Rules:        - name: max_length=15 pattern=        - interface: max_length=15 pattern=        - vni: min=1 max=16777215 pattern=        - ip_version: pattern=        - remote_ip: pattern=        - local_ip: pattern=        - remote_ip6: pattern=        - local_ip6: pattern=        - dstport: min=1 max=65535 pattern=        - multicast_ttl: min=1 max=255 pattern=        - evpn_id: min=1 max=65535 pattern=        - learn_from_traffic: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=15, default="", description="VXLAN device or interface name. Must be a unique interface name.")    
    interface: str = Field(max_length=15, default="", description="Outgoing interface for VXLAN encapsulated traffic.")  # datasource: ['system.interface.name']    
    vni: int = Field(ge=1, le=16777215, default=0, description="VXLAN network ID.")    
    ip_version: IpVersionEnum = Field(default="ipv4-unicast", description="IP version to use for the VXLAN interface and so for communication over the VXLAN. IPv4 or IPv6 unicast or multicast.")    
    remote_ip: list[RemoteIp] = Field(default=None, description="IPv4 address of the VXLAN interface on the device at the remote end of the VXLAN.")    
    local_ip: str | None = Field(default="0.0.0.0", description="IPv4 address to use as the source address for egress VXLAN packets.")    
    remote_ip6: list[RemoteIp6] = Field(description="IPv6 IP address of the VXLAN interface on the device at the remote end of the VXLAN.")    
    local_ip6: str | None = Field(default="::", description="IPv6 address to use as the source address for egress VXLAN packets.")    
    dstport: int | None = Field(ge=1, le=65535, default=4789, description="VXLAN destination port (1 - 65535, default = 4789).")    
    multicast_ttl: int = Field(ge=1, le=255, default=0, description="VXLAN multicast TTL (1-255, default = 0).")    
    evpn_id: int | None = Field(ge=1, le=65535, default=0, description="EVPN instance.")  # datasource: ['system.evpn.id']    
    learn_from_traffic: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable VXLAN MAC learning from traffic.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('interface')
    @classmethod
    def validate_interface(cls, v: Any) -> Any:
        """
        Validate interface field.
        
        Datasource: ['system.interface.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('evpn_id')
    @classmethod
    def validate_evpn_id(cls, v: Any) -> Any:
        """
        Validate evpn_id field.
        
        Datasource: ['system.evpn.id']
        
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
    "VxlanModel",    "VxlanRemoteIp",    "VxlanRemoteIp6",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:35.852287Z
# ============================================================================