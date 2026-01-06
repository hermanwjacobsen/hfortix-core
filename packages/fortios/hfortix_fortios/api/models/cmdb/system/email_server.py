"""
Pydantic Models for CMDB - system/email_server

Runtime validation models for system/email_server configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.system.email_server import 
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
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class EmailServerSsl_min_proto_versionEnum(str, Enum):
    """Allowed values for ssl_min_proto_version field."""
    DEFAULT = "default"    SSLV3 = "SSLv3"    TLSV1 = "TLSv1"    TLSV1_1 = "TLSv1-1"    TLSV1_2 = "TLSv1-2"    TLSV1_3 = "TLSv1-3"

# ============================================================================
# Main Model
# ============================================================================

class EmailServerModel(BaseModel):
    """
    Pydantic model for system/email_server configuration.
    
    Configure the email server used by the FortiGate various things. For example, for sending email messages to users to support user authentication features.
    
    Validation Rules:        - type: pattern=        - server: max_length=63 pattern=        - port: min=1 max=65535 pattern=        - source_ip: pattern=        - source_ip6: pattern=        - authenticate: pattern=        - validate_server: pattern=        - username: max_length=255 pattern=        - password: max_length=128 pattern=        - security: pattern=        - ssl_min_proto_version: pattern=        - interface_select_method: pattern=        - interface: max_length=15 pattern=        - vrf_select: min=0 max=511 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    type: Literal["custom"] | None = Field(default="custom", description="Use FortiGuard Message service or custom email server.")    
    server: str | None = Field(max_length=63, default="", description="SMTP server IP address or hostname.")    
    port: int | None = Field(ge=1, le=65535, default=25, description="SMTP server port.")    
    source_ip: str | None = Field(default="0.0.0.0", description="SMTP server IPv4 source IP.")    
    source_ip6: str | None = Field(default="::", description="SMTP server IPv6 source IP.")    
    authenticate: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable authentication.")    
    validate_server: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable validation of server certificate.")    
    username: str | None = Field(max_length=255, default="", description="SMTP server user name for authentication.")    
    password: Any = Field(max_length=128, default=None, description="SMTP server user password for authentication.")    
    security: Literal["none", "starttls", "smtps"] | None = Field(default="none", description="Connection security used by the email server.")    
    ssl_min_proto_version: SslMinProtoVersionEnum | None = Field(default="default", description="Minimum supported protocol version for SSL/TLS connections (default is to follow system global setting).")    
    interface_select_method: Literal["auto", "sdwan", "specify"] | None = Field(default="auto", description="Specify how to select outgoing interface to reach server.")    
    interface: str = Field(max_length=15, default="", description="Specify outgoing interface to reach server.")  # datasource: ['system.interface.name']    
    vrf_select: int | None = Field(ge=0, le=511, default=0, description="VRF ID used for connection to server.")    
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
    "EmailServerModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:34.027552Z
# ============================================================================