"""
Pydantic Models for CMDB - system/gre_tunnel

Runtime validation models for system/gre_tunnel configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.system.gre_tunnel import 
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
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class GreTunnelModel(BaseModel):
    """
    Pydantic model for system/gre_tunnel configuration.
    
    Configure GRE tunnel.
    
    Validation Rules:        - name: max_length=15 pattern=        - interface: max_length=15 pattern=        - ip_version: pattern=        - remote_gw6: pattern=        - local_gw6: pattern=        - remote_gw: pattern=        - local_gw: pattern=        - use_sdwan: pattern=        - sequence_number_transmission: pattern=        - sequence_number_reception: pattern=        - checksum_transmission: pattern=        - checksum_reception: pattern=        - key_outbound: min=0 max=4294967295 pattern=        - key_inbound: min=0 max=4294967295 pattern=        - dscp_copying: pattern=        - diffservcode: pattern=        - keepalive_interval: min=0 max=32767 pattern=        - keepalive_failtimes: min=1 max=255 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=15, default="", description="Tunnel name.")    
    interface: str | None = Field(max_length=15, default="", description="Interface name.")  # datasource: ['system.interface.name']    
    ip_version: Literal["4", "6"] | None = Field(default="4", description="IP version to use for VPN interface.")    
    remote_gw6: str = Field(default="::", description="IPv6 address of the remote gateway.")    
    local_gw6: str = Field(default="::", description="IPv6 address of the local gateway.")    
    remote_gw: str = Field(default="0.0.0.0", description="IP address of the remote gateway.")    
    local_gw: str = Field(default="0.0.0.0", description="IP address of the local gateway.")    
    use_sdwan: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable use of SD-WAN to reach remote gateway.")    
    sequence_number_transmission: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable including of sequence numbers in transmitted GRE packets.")    
    sequence_number_reception: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable validating sequence numbers in received GRE packets.")    
    checksum_transmission: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable including checksums in transmitted GRE packets.")    
    checksum_reception: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable validating checksums in received GRE packets.")    
    key_outbound: int | None = Field(ge=0, le=4294967295, default=0, description="Include this key in transmitted GRE packets (0 - 4294967295).")    
    key_inbound: int | None = Field(ge=0, le=4294967295, default=0, description="Require received GRE packets contain this key (0 - 4294967295).")    
    dscp_copying: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable DSCP copying.")    
    diffservcode: str | None = Field(default="", description="DiffServ setting to be applied to GRE tunnel outer IP header.")    
    keepalive_interval: int | None = Field(ge=0, le=32767, default=0, description="Keepalive message interval (0 - 32767, 0 = disabled).")    
    keepalive_failtimes: int | None = Field(ge=1, le=255, default=10, description="Number of consecutive unreturned keepalive messages before a GRE connection is considered down (1 - 255).")    
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
    "GreTunnelModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:35.280595Z
# ============================================================================