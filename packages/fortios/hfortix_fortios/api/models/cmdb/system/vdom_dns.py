"""
Pydantic Models for CMDB - system/vdom_dns

Runtime validation models for system/vdom_dns configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.system.vdom_dns import 
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

class VdomDnsServerHostname(BaseModel):
    """
    Child table model for server-hostname.
    
    DNS server host name list.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    hostname: str = Field(max_length=127, default="", description="DNS server host name list separated by space (maximum 4 domains).")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class VdomDnsModel(BaseModel):
    """
    Pydantic model for system/vdom_dns configuration.
    
    Configure DNS servers for a non-management VDOM.
    
    Validation Rules:        - vdom_dns: pattern=        - primary: pattern=        - secondary: pattern=        - protocol: pattern=        - ssl_certificate: max_length=35 pattern=        - server_hostname: pattern=        - ip6_primary: pattern=        - ip6_secondary: pattern=        - source_ip: pattern=        - source_ip_interface: max_length=15 pattern=        - interface_select_method: pattern=        - interface: max_length=15 pattern=        - vrf_select: min=0 max=511 pattern=        - server_select_method: pattern=        - alt_primary: pattern=        - alt_secondary: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    vdom_dns: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable configuring DNS servers for the current VDOM.")    
    primary: str = Field(default="0.0.0.0", description="Primary DNS server IP address for the VDOM.")    
    secondary: str | None = Field(default="0.0.0.0", description="Secondary DNS server IP address for the VDOM.")    
    protocol: list[Protocol] = Field(default="cleartext", description="DNS transport protocols.")    
    ssl_certificate: str | None = Field(max_length=35, default="", description="Name of local certificate for SSL connections.")  # datasource: ['certificate.local.name']    
    server_hostname: list[ServerHostname] = Field(default=None, description="DNS server host name list.")    
    ip6_primary: str | None = Field(default="::", description="Primary IPv6 DNS server IP address for the VDOM.")    
    ip6_secondary: str | None = Field(default="::", description="Secondary IPv6 DNS server IP address for the VDOM.")    
    source_ip: str | None = Field(default="0.0.0.0", description="Source IP for communications with the DNS server.")    
    source_ip_interface: str | None = Field(max_length=15, default="", description="IP address of the specified interface as the source IP address.")  # datasource: ['system.interface.name']    
    interface_select_method: Literal["auto", "sdwan", "specify"] | None = Field(default="auto", description="Specify how to select outgoing interface to reach server.")    
    interface: str = Field(max_length=15, default="", description="Specify outgoing interface to reach server.")  # datasource: ['system.interface.name']    
    vrf_select: int | None = Field(ge=0, le=511, default=0, description="VRF ID used for connection to server.")    
    server_select_method: Literal["least-rtt", "failover"] | None = Field(default="least-rtt", description="Specify how configured servers are prioritized.")    
    alt_primary: str | None = Field(default="0.0.0.0", description="Alternate primary DNS server. This is not used as a failover DNS server.")    
    alt_secondary: str | None = Field(default="0.0.0.0", description="Alternate secondary DNS server. This is not used as a failover DNS server.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
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
    @field_validator('source_ip_interface')
    @classmethod
    def validate_source_ip_interface(cls, v: Any) -> Any:
        """
        Validate source_ip_interface field.
        
        Datasource: ['system.interface.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
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
    "VdomDnsModel",    "VdomDnsServerHostname",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:35.397069Z
# ============================================================================