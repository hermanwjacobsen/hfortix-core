"""
Pydantic Models for CMDB - switch_controller/traffic_sniffer

Runtime validation models for switch_controller/traffic_sniffer configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.switch_controller.traffic_sniffer import 
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

class TrafficSnifferTargetMac(BaseModel):
    """
    Child table model for target-mac.
    
    Sniffer MACs to filter.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    mac: str = Field(default="00:00:00:00:00:00", description="Sniffer MAC.")    
    description: str | None = Field(max_length=63, default="", description="Description for the sniffer MAC.")
class TrafficSnifferTargetIp(BaseModel):
    """
    Child table model for target-ip.
    
    Sniffer IPs to filter.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    ip: str = Field(default="0.0.0.0", description="Sniffer IP.")    
    description: str | None = Field(max_length=63, default="", description="Description for the sniffer IP.")
class TrafficSnifferTargetPort(BaseModel):
    """
    Child table model for target-port.
    
    Sniffer ports to filter.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    switch_id: str = Field(max_length=35, default="", description="Managed-switch ID.")  # datasource: ['switch-controller.managed-switch.switch-id']    
    description: str | None = Field(max_length=63, default="", description="Description for the sniffer port entry.")    
    in_ports: list[InPorts] = Field(default=None, description="Configure source ingress port interfaces.")    
    out_ports: list[OutPorts] = Field(default=None, description="Configure source egress port interfaces.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class TrafficSnifferModel(BaseModel):
    """
    Pydantic model for switch_controller/traffic_sniffer configuration.
    
    Configure FortiSwitch RSPAN/ERSPAN traffic sniffing parameters.
    
    Validation Rules:        - mode: pattern=        - erspan_ip: pattern=        - target_mac: pattern=        - target_ip: pattern=        - target_port: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    mode: Literal["erspan-auto", "rspan", "none"] | None = Field(default="erspan-auto", description="Configure traffic sniffer mode.")    
    erspan_ip: str | None = Field(default="0.0.0.0", description="Configure ERSPAN collector IP address.")    
    target_mac: list[TargetMac] = Field(default=None, description="Sniffer MACs to filter.")    
    target_ip: list[TargetIp] = Field(default=None, description="Sniffer IPs to filter.")    
    target_port: list[TargetPort] = Field(default=None, description="Sniffer ports to filter.")    
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
    "TrafficSnifferModel",    "TrafficSnifferTargetMac",    "TrafficSnifferTargetIp",    "TrafficSnifferTargetPort",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:35.357397Z
# ============================================================================