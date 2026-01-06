"""
Pydantic Models for CMDB - system/mobile_tunnel

Runtime validation models for system/mobile_tunnel configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.system.mobile_tunnel import 
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

class MobileTunnelNetwork(BaseModel):
    """
    Child table model for network.
    
    NEMO network configuration.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="Network entry ID.")    
    interface: str | None = Field(max_length=15, default="", description="Select the associated interface name from available options.")  # datasource: ['system.interface.name']    
    prefix: str | None = Field(default="0.0.0.0 0.0.0.0", description="Class IP and Netmask with correction (Format:xxx.xxx.xxx.xxx xxx.xxx.xxx.xxx or xxx.xxx.xxx.xxx/x).")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class MobileTunnelModel(BaseModel):
    """
    Pydantic model for system/mobile_tunnel configuration.
    
    Configure Mobile tunnels, an implementation of Network Mobility (NEMO) extensions for Mobile IPv4 RFC5177.
    
    Validation Rules:        - name: max_length=15 pattern=        - status: pattern=        - roaming_interface: max_length=15 pattern=        - home_agent: pattern=        - home_address: pattern=        - renew_interval: min=5 max=60 pattern=        - lifetime: min=180 max=65535 pattern=        - reg_interval: min=5 max=300 pattern=        - reg_retry: min=1 max=30 pattern=        - n_mhae_spi: min=0 max=4294967295 pattern=        - n_mhae_key_type: pattern=        - n_mhae_key: pattern=        - hash_algorithm: pattern=        - tunnel_mode: pattern=        - network: pattern=    """
    
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
    status: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable this mobile tunnel.")    
    roaming_interface: str = Field(max_length=15, default="", description="Select the associated interface name from available options.")  # datasource: ['system.interface.name']    
    home_agent: str = Field(default="0.0.0.0", description="IPv4 address of the NEMO HA (Format: xxx.xxx.xxx.xxx).")    
    home_address: str | None = Field(default="0.0.0.0", description="Home IP address (Format: xxx.xxx.xxx.xxx).")    
    renew_interval: int = Field(ge=5, le=60, default=60, description="Time before lifetime expiration to send NMMO HA re-registration (5 - 60, default = 60).")    
    lifetime: int = Field(ge=180, le=65535, default=65535, description="NMMO HA registration request lifetime (180 - 65535 sec, default = 65535).")    
    reg_interval: int = Field(ge=5, le=300, default=5, description="NMMO HA registration interval (5 - 300, default = 5).")    
    reg_retry: int = Field(ge=1, le=30, default=3, description="Maximum number of NMMO HA registration retries (1 to 30, default = 3).")    
    n_mhae_spi: int = Field(ge=0, le=4294967295, default=256, description="NEMO authentication SPI (default: 256).")    
    n_mhae_key_type: Literal["ascii", "base64"] = Field(default="ascii", description="NEMO authentication key type (ASCII or base64).")    
    n_mhae_key: Any = Field(default=None, description="NEMO authentication key.")    
    hash_algorithm: Literal["hmac-md5"] = Field(default="hmac-md5", description="Hash Algorithm (Keyed MD5).")    
    tunnel_mode: Literal["gre"] = Field(default="gre", description="NEMO tunnel mode (GRE tunnel).")    
    network: list[Network] = Field(default=None, description="NEMO network configuration.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('roaming_interface')
    @classmethod
    def validate_roaming_interface(cls, v: Any) -> Any:
        """
        Validate roaming_interface field.
        
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
    "MobileTunnelModel",    "MobileTunnelNetwork",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:33.553487Z
# ============================================================================