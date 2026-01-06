"""
Pydantic Models for CMDB - ftp_proxy/explicit

Runtime validation models for ftp_proxy/explicit configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.ftp_proxy.explicit import 
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
from enum import Enum

# ============================================================================
# Child Table Models
# ============================================================================

class ExplicitSslCert(BaseModel):
    """
    Child table model for ssl-cert.
    
    List of certificate names to use for SSL connections to this server.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="Fortinet_SSL", description="Certificate list.")  # datasource: ['vpn.certificate.local.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class ExplicitSsl_dh_bitsEnum(str, Enum):
    """Allowed values for ssl_dh_bits field."""
    768 = "768"    1024 = "1024"    1536 = "1536"    2048 = "2048"

# ============================================================================
# Main Model
# ============================================================================

class ExplicitModel(BaseModel):
    """
    Pydantic model for ftp_proxy/explicit configuration.
    
    Configure explicit FTP proxy settings.
    
    Validation Rules:        - status: pattern=        - incoming_port: pattern=        - incoming_ip: pattern=        - outgoing_ip: pattern=        - sec_default_action: pattern=        - server_data_mode: pattern=        - ssl: pattern=        - ssl_cert: pattern=        - ssl_dh_bits: pattern=        - ssl_algorithm: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable the explicit FTP proxy.")    
    incoming_port: str | None = Field(default="", description="Accept incoming FTP requests on one or more ports.")    
    incoming_ip: str | None = Field(default="0.0.0.0", description="Accept incoming FTP requests from this IP address. An interface must have this IP address.")    
    outgoing_ip: list[OutgoingIp] = Field(default="", description="Outgoing FTP requests will leave from this IP address. An interface must have this IP address.")    
    sec_default_action: Literal["accept", "deny"] | None = Field(default="deny", description="Accept or deny explicit FTP proxy sessions when no FTP proxy firewall policy exists.")    
    server_data_mode: Literal["client", "passive"] | None = Field(default="client", description="Determine mode of data session on FTP server side.")    
    ssl: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable the explicit FTPS proxy.")    
    ssl_cert: list[SslCert] = Field(default=None, description="List of certificate names to use for SSL connections to this server.")    
    ssl_dh_bits: SslDhBitsEnum | None = Field(default="2048", description="Bit-size of Diffie-Hellman (DH) prime used in DHE-RSA negotiation (default = 2048).")    
    ssl_algorithm: Literal["high", "medium", "low"] | None = Field(default="high", description="Relative strength of encryption algorithms accepted in negotiation.")    
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
    "ExplicitModel",    "ExplicitSslCert",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:33.454219Z
# ============================================================================