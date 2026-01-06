"""
Pydantic Models for CMDB - firewall/access_proxy_virtual_host

Runtime validation models for firewall/access_proxy_virtual_host configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.firewall.access_proxy_virtual_host import 
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

class AccessProxyVirtualHostSslCertificate(BaseModel):
    """
    Child table model for ssl-certificate.
    
    SSL certificates for this host.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="Certificate list.")  # datasource: ['vpn.certificate.local.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class AccessProxyVirtualHostModel(BaseModel):
    """
    Pydantic model for firewall/access_proxy_virtual_host configuration.
    
    Configure Access Proxy virtual hosts.
    
    Validation Rules:        - name: max_length=79 pattern=        - ssl_certificate: pattern=        - host: max_length=79 pattern=        - host_type: pattern=        - replacemsg_group: max_length=35 pattern=        - empty_cert_action: pattern=        - user_agent_detect: pattern=        - client_cert: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=79, default="", description="Virtual host name.")    
    ssl_certificate: list[SslCertificate] = Field(description="SSL certificates for this host.")    
    host: str = Field(max_length=79, default="", description="The host name.")    
    host_type: Literal["sub-string", "wildcard"] = Field(default="sub-string", description="Type of host pattern.")    
    replacemsg_group: str | None = Field(max_length=35, default="", description="Access-proxy-virtual-host replacement message override group.")  # datasource: ['system.replacemsg-group.name']    
    empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = Field(default="block", description="Action for an empty client certificate.")    
    user_agent_detect: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable detecting device type by HTTP user-agent if no client certificate is provided.")    
    client_cert: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable requesting client certificate.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('replacemsg_group')
    @classmethod
    def validate_replacemsg_group(cls, v: Any) -> Any:
        """
        Validate replacemsg_group field.
        
        Datasource: ['system.replacemsg-group.name']
        
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
    "AccessProxyVirtualHostModel",    "AccessProxyVirtualHostSslCertificate",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:33.761904Z
# ============================================================================