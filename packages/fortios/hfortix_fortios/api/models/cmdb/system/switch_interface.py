"""
Pydantic Models for CMDB - system/switch_interface

Runtime validation models for system/switch_interface configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.system.switch_interface import 
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

# ============================================================================
# Child Table Models
# ============================================================================

class SwitchInterfaceSpanSourcePort(BaseModel):
    """
    Child table model for span-source-port.
    
    Physical interface name. Port spanning echoes all traffic on the SPAN source ports to the SPAN destination port.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    interface_name: str = Field(max_length=79, default="", description="Physical interface name.")  # datasource: ['system.interface.name']
class SwitchInterfaceMember(BaseModel):
    """
    Child table model for member.
    
    Names of the interfaces that belong to the virtual switch.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    interface_name: str = Field(max_length=79, default="", description="Interface name.")  # datasource: ['system.interface.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class SwitchInterfaceModel(BaseModel):
    """
    Pydantic model for system/switch_interface configuration.
    
    Configure software switch interfaces by grouping physical and WiFi interfaces.
    
    Validation Rules:        - name: max_length=15 pattern=        - vdom: max_length=31 pattern=        - span_dest_port: max_length=15 pattern=        - span_source_port: pattern=        - member: pattern=        - type: pattern=        - intra_switch_policy: pattern=        - mac_ttl: min=300 max=8640000 pattern=        - span: pattern=        - span_direction: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str = Field(max_length=15, default="", description="Interface name (name cannot be in use by any other interfaces, VLANs, or inter-VDOM links).")    
    vdom: str = Field(max_length=31, default="", description="VDOM that the software switch belongs to.")  # datasource: ['system.vdom.name']    
    span_dest_port: str | None = Field(max_length=15, default="", description="SPAN destination port name. All traffic on the SPAN source ports is echoed to the SPAN destination port.")  # datasource: ['system.interface.name']    
    span_source_port: list[SpanSourcePort] = Field(default=None, description="Physical interface name. Port spanning echoes all traffic on the SPAN source ports to the SPAN destination port.")    
    member: list[Member] = Field(default=None, description="Names of the interfaces that belong to the virtual switch.")    
    type: Literal["switch", "hub"] | None = Field(default="switch", description="Type of switch based on functionality: switch for normal functionality, or hub to duplicate packets to all port members.")    
    intra_switch_policy: Literal["implicit", "explicit"] | None = Field(default="implicit", description="Allow any traffic between switch interfaces or require firewall policies to allow traffic between switch interfaces.")    
    mac_ttl: int | None = Field(ge=300, le=8640000, default=300, description="Duration for which MAC addresses are held in the ARP table (300 - 8640000 sec, default = 300).")    
    span: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable port spanning. Port spanning echoes traffic received by the software switch to the span destination port.")    
    span_direction: Literal["rx", "tx", "both"] | None = Field(default="both", description="The direction in which the SPAN port operates, either: rx, tx, or both.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('vdom')
    @classmethod
    def validate_vdom(cls, v: Any) -> Any:
        """
        Validate vdom field.
        
        Datasource: ['system.vdom.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('span_dest_port')
    @classmethod
    def validate_span_dest_port(cls, v: Any) -> Any:
        """
        Validate span_dest_port field.
        
        Datasource: ['system.interface.name']
        
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
    "SwitchInterfaceModel",    "SwitchInterfaceSpanSourcePort",    "SwitchInterfaceMember",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:34.885477Z
# ============================================================================