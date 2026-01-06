"""
Pydantic Models for CMDB - firewall/central_snat_map

Runtime validation models for firewall/central_snat_map configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.firewall.central_snat_map import 
    >>>
    >>> # Create with validation
    >>> obj = (
    ...     policyid=1,
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

class CentralSnatMapSrcintf(BaseModel):
    """
    Child table model for srcintf.
    
    Source interface name from available interfaces.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="Interface name.")  # datasource: ['system.interface.name', 'system.zone.name', 'system.sdwan.zone.name']
class CentralSnatMapDstintf(BaseModel):
    """
    Child table model for dstintf.
    
    Destination interface name from available interfaces.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Interface name.")  # datasource: ['system.interface.name', 'system.zone.name', 'system.sdwan.zone.name']
class CentralSnatMapOrigAddr(BaseModel):
    """
    Child table model for orig-addr.
    
    IPv4 Original address.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name', 'system.external-resource.name']
class CentralSnatMapOrigAddr6(BaseModel):
    """
    Child table model for orig-addr6.
    
    IPv6 Original address.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address6.name', 'firewall.addrgrp6.name', 'system.external-resource.name']
class CentralSnatMapDstAddr(BaseModel):
    """
    Child table model for dst-addr.
    
    IPv4 Destination address.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name']
class CentralSnatMapDstAddr6(BaseModel):
    """
    Child table model for dst-addr6.
    
    IPv6 Destination address.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address6.name', 'firewall.addrgrp6.name']
class CentralSnatMapNatIppool(BaseModel):
    """
    Child table model for nat-ippool.
    
    Name of the IP pools to be used to translate addresses from available IP Pools.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="IP pool name.")  # datasource: ['firewall.ippool.name']
class CentralSnatMapNatIppool6(BaseModel):
    """
    Child table model for nat-ippool6.
    
    IPv6 pools to be used for source NAT.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="IPv6 pool name.")  # datasource: ['firewall.ippool6.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class CentralSnatMapModel(BaseModel):
    """
    Pydantic model for firewall/central_snat_map configuration.
    
    Configure IPv4 and IPv6 central SNAT policies.
    
    Validation Rules:        - policyid: min=0 max=4294967295 pattern=        - uuid: pattern=        - status: pattern=        - type: pattern=        - srcintf: pattern=        - dstintf: pattern=        - orig_addr: pattern=        - orig_addr6: pattern=        - dst_addr: pattern=        - dst_addr6: pattern=        - protocol: min=0 max=255 pattern=        - orig_port: pattern=        - nat: pattern=        - nat46: pattern=        - nat64: pattern=        - nat_ippool: pattern=        - nat_ippool6: pattern=        - port_preserve: pattern=        - port_random: pattern=        - nat_port: pattern=        - dst_port: pattern=        - comments: max_length=1023 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    policyid: int | None = Field(ge=0, le=4294967295, default=0, description="Policy ID.")    
    uuid: str | None = Field(default="00000000-0000-0000-0000-000000000000", description="Universally Unique Identifier (UUID; automatically assigned but can be manually reset).")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable the active status of this policy.")    
    type: Literal["ipv4", "ipv6"] | None = Field(default="ipv4", description="IPv4/IPv6 source NAT.")    
    srcintf: list[Srcintf] = Field(description="Source interface name from available interfaces.")    
    dstintf: list[Dstintf] = Field(description="Destination interface name from available interfaces.")    
    orig_addr: list[OrigAddr] = Field(description="IPv4 Original address.")    
    orig_addr6: list[OrigAddr6] = Field(description="IPv6 Original address.")    
    dst_addr: list[DstAddr] = Field(description="IPv4 Destination address.")    
    dst_addr6: list[DstAddr6] = Field(description="IPv6 Destination address.")    
    protocol: int | None = Field(ge=0, le=255, default=0, description="Integer value for the protocol type (0 - 255).")    
    orig_port: str | None = Field(default="", description="Original TCP port (1 to 65535, 0 means any port).")    
    nat: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable source NAT.")    
    nat46: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable NAT46.")    
    nat64: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable NAT64.")    
    nat_ippool: list[NatIppool] = Field(default=None, description="Name of the IP pools to be used to translate addresses from available IP Pools.")    
    nat_ippool6: list[NatIppool6] = Field(default=None, description="IPv6 pools to be used for source NAT.")    
    port_preserve: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable preservation of the original source port from source NAT if it has not been used.")    
    port_random: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable random source port selection for source NAT.")    
    nat_port: str | None = Field(default="", description="Translated port or port range (1 to 65535, 0 means any port).")    
    dst_port: str | None = Field(default="", description="Destination port or port range (1 to 65535, 0 means any port).")    
    comments: str | None = Field(max_length=1023, default=None, description="Comment.")    
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
    "CentralSnatMapModel",    "CentralSnatMapSrcintf",    "CentralSnatMapDstintf",    "CentralSnatMapOrigAddr",    "CentralSnatMapOrigAddr6",    "CentralSnatMapDstAddr",    "CentralSnatMapDstAddr6",    "CentralSnatMapNatIppool",    "CentralSnatMapNatIppool6",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:34.312429Z
# ============================================================================