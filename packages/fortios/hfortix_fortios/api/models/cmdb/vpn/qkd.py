"""
Pydantic Models for CMDB - vpn/qkd

Runtime validation models for vpn/qkd configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.vpn.qkd import 
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

from pydantic import BaseModel, Field
from typing import Any, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class QkdCertificate(BaseModel):
    """
    Child table model for certificate.
    
    Names of up to 4 certificates to offer to the KME.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Certificate name.")  # datasource: ['vpn.certificate.local.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class QkdModel(BaseModel):
    """
    Pydantic model for vpn/qkd configuration.
    
    Configure Quantum Key Distribution servers
    
    Validation Rules:        - name: max_length=35 pattern=        - server: max_length=63 pattern=        - port: min=1 max=65535 pattern=        - id: max_length=291 pattern=        - peer: max_length=35 pattern=        - certificate: pattern=        - comment: max_length=255 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str = Field(max_length=35, default="", description="Quantum Key Distribution configuration name.")    
    server: str = Field(max_length=63, default="", description="IPv4, IPv6 or DNS address of the KME.")    
    port: int = Field(ge=1, le=65535, default=0, description="Port to connect to on the KME.")    
    id: str = Field(max_length=291, default="", description="Quantum Key Distribution ID assigned by the KME.")    
    peer: str = Field(max_length=35, default="", description="Authenticate Quantum Key Device's certificate with the peer/peergrp.")  # datasource: ['user.peer.name', 'user.peergrp.name']    
    certificate: list[Certificate] = Field(default=None, description="Names of up to 4 certificates to offer to the KME.")    
    comment: str | None = Field(max_length=255, default=None, description="Comment.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('peer')
    @classmethod
    def validate_peer(cls, v: Any) -> Any:
        """
        Validate peer field.
        
        Datasource: ['user.peer.name', 'user.peergrp.name']
        
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
    "QkdModel",    "QkdCertificate",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:35.529405Z
# ============================================================================