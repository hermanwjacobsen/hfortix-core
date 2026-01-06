"""
Pydantic Models for CMDB - system/sdn_vpn

Runtime validation models for system/sdn_vpn configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.system.sdn_vpn import 
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

class SdnVpnModel(BaseModel):
    """
    Pydantic model for system/sdn_vpn configuration.
    
    Configure public cloud VPN service.
    
    Validation Rules:        - name: max_length=35 pattern=        - sdn: max_length=35 pattern=        - remote_type: pattern=        - routing_type: pattern=        - vgw_id: max_length=63 pattern=        - tgw_id: max_length=63 pattern=        - subnet_id: max_length=63 pattern=        - bgp_as: min=1 max=4294967295 pattern=        - cgw_gateway: pattern=        - nat_traversal: pattern=        - tunnel_interface: max_length=15 pattern=        - internal_interface: max_length=15 pattern=        - local_cidr: pattern=        - remote_cidr: pattern=        - cgw_name: max_length=35 pattern=        - psksecret: pattern=        - type: min=0 max=65535 pattern=        - status: min=0 max=255 pattern=        - code: min=0 max=255 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=35, default="", description="Public cloud VPN name.")    
    sdn: str = Field(max_length=35, default="", description="SDN connector name.")  # datasource: ['system.sdn-connector.name']    
    remote_type: Literal["vgw", "tgw"] = Field(default="vgw", description="Type of remote device.")    
    routing_type: Literal["static", "dynamic"] = Field(default="dynamic", description="Type of routing.")    
    vgw_id: str = Field(max_length=63, default="", description="Virtual private gateway id.")    
    tgw_id: str = Field(max_length=63, default="", description="Transit gateway id.")    
    subnet_id: str | None = Field(max_length=63, default="", description="AWS subnet id for TGW route propagation.")    
    bgp_as: int = Field(ge=1, le=4294967295, default=65000, description="BGP Router AS number.")    
    cgw_gateway: str = Field(default="0.0.0.0", description="Public IP address of the customer gateway.")    
    nat_traversal: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable use for NAT traversal. Please enable if your FortiGate device is behind a NAT/PAT device.")    
    tunnel_interface: str = Field(max_length=15, default="", description="Tunnel interface with public IP.")  # datasource: ['system.interface.name']    
    internal_interface: str = Field(max_length=15, default="", description="Internal interface with local subnet.")  # datasource: ['system.interface.name']    
    local_cidr: str = Field(default="0.0.0.0 0.0.0.0", description="Local subnet address and subnet mask.")    
    remote_cidr: str = Field(default="0.0.0.0 0.0.0.0", description="Remote subnet address and subnet mask.")    
    cgw_name: str | None = Field(max_length=35, default="", description="AWS customer gateway name to be created.")    
    psksecret: Any = Field(default=None, description="Pre-shared secret for PSK authentication. Auto-generated if not specified")    
    type: int | None = Field(ge=0, le=65535, default=0, description="SDN VPN type.")    
    status: int | None = Field(ge=0, le=255, default=0, description="SDN VPN status.")    
    code: int | None = Field(ge=0, le=255, default=0, description="SDN VPN error code.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('sdn')
    @classmethod
    def validate_sdn(cls, v: Any) -> Any:
        """
        Validate sdn field.
        
        Datasource: ['system.sdn-connector.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('tunnel_interface')
    @classmethod
    def validate_tunnel_interface(cls, v: Any) -> Any:
        """
        Validate tunnel_interface field.
        
        Datasource: ['system.interface.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('internal_interface')
    @classmethod
    def validate_internal_interface(cls, v: Any) -> Any:
        """
        Validate internal_interface field.
        
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
    "SdnVpnModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:35.937867Z
# ============================================================================