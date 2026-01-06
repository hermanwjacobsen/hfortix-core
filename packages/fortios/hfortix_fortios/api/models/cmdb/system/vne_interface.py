"""
Pydantic Models for CMDB - system/vne_interface

Runtime validation models for system/vne_interface configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.system.vne_interface import 
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

class VneInterfaceModel(BaseModel):
    """
    Pydantic model for system/vne_interface configuration.
    
    Configure virtual network enabler tunnels.
    
    Validation Rules:        - name: max_length=15 pattern=        - interface: max_length=15 pattern=        - ssl_certificate: max_length=35 pattern=        - bmr_hostname: max_length=128 pattern=        - auto_asic_offload: pattern=        - ipv4_address: pattern=        - br: max_length=255 pattern=        - update_url: max_length=511 pattern=        - mode: pattern=        - http_username: max_length=64 pattern=        - http_password: max_length=128 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=15, default="", description="VNE tunnel name.")    
    interface: str = Field(max_length=15, default="", description="Interface name.")  # datasource: ['system.interface.name']    
    ssl_certificate: str = Field(max_length=35, default="Fortinet_Factory", description="Name of local certificate for SSL connections.")  # datasource: ['certificate.local.name']    
    bmr_hostname: Any = Field(max_length=128, description="BMR hostname.")    
    auto_asic_offload: Literal["enable", "disable"] = Field(default="enable", description="Enable/disable tunnel ASIC offloading.")    
    ipv4_address: Any = Field(default="0.0.0.0 0.0.0.0", description="Tunnel IPv4 address and netmask.")    
    br: str = Field(max_length=255, default="", description="IPv6 address or FQDN of the border relay.")    
    update_url: str = Field(max_length=511, default="", description="URL of provisioning server.")    
    mode: Literal["map-e", "fixed-ip", "ds-lite"] = Field(default="map-e", description="VNE tunnel mode.")    
    http_username: str | None = Field(max_length=64, default="", description="HTTP authentication user name.")    
    http_password: Any = Field(max_length=128, default=None, description="HTTP authentication password.")    
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
    @field_validator('ssl_certificate')
    @classmethod
    def validate_ssl_certificate(cls, v: Any) -> Any:
        """
        Validate ssl_certificate field.
        
        Datasource: ['certificate.local.name']
        
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
    "VneInterfaceModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:32.942213Z
# ============================================================================