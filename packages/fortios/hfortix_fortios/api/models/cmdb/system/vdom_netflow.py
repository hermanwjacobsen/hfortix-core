"""
Pydantic Models for CMDB - system/vdom_netflow

Runtime validation models for system/vdom_netflow configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.system.vdom_netflow import 
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

class VdomNetflowCollectors(BaseModel):
    """
    Child table model for collectors.
    
    Netflow collectors.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=1, le=6, default=0, description="ID.")    
    collector_ip: str = Field(max_length=63, default="", description="Collector IP.")    
    collector_port: int | None = Field(ge=0, le=65535, default=2055, description="NetFlow collector port number.")    
    source_ip: str | None = Field(max_length=63, default="", description="Source IP address for communication with the NetFlow agent.")    
    source_ip_interface: str | None = Field(max_length=15, default="", description="Name of the interface used to determine the source IP for exporting packets.")  # datasource: ['system.interface.name']    
    interface_select_method: Literal["auto", "sdwan", "specify"] | None = Field(default="auto", description="Specify how to select outgoing interface to reach server.")    
    interface: str = Field(max_length=15, default="", description="Specify outgoing interface to reach server.")  # datasource: ['system.interface.name']    
    vrf_select: int | None = Field(ge=0, le=511, default=0, description="VRF ID used for connection to server.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class VdomNetflowModel(BaseModel):
    """
    Pydantic model for system/vdom_netflow configuration.
    
    Configure NetFlow per VDOM.
    
    Validation Rules:        - vdom_netflow: pattern=        - collectors: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    vdom_netflow: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable NetFlow per VDOM.")    
    collectors: list[Collectors] = Field(default=None, description="Netflow collectors.")    
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
    "VdomNetflowModel",    "VdomNetflowCollectors",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:33.611375Z
# ============================================================================