"""
Pydantic Models for CMDB - vpn/certificate/ocsp_server

Runtime validation models for vpn/certificate/ocsp_server configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.vpn.certificate.ocsp_server import 
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

class OcspServerModel(BaseModel):
    """
    Pydantic model for vpn/certificate/ocsp_server configuration.
    
    OCSP server configuration.
    
    Validation Rules:        - name: max_length=35 pattern=        - url: max_length=127 pattern=        - cert: max_length=127 pattern=        - secondary_url: max_length=127 pattern=        - secondary_cert: max_length=127 pattern=        - unavail_action: pattern=        - source_ip: max_length=63 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=35, default="", description="OCSP server entry name.")    
    url: str | None = Field(max_length=127, default="", description="OCSP server URL.")    
    cert: str | None = Field(max_length=127, default="", description="OCSP server certificate.")  # datasource: ['vpn.certificate.remote.name', 'vpn.certificate.ca.name']    
    secondary_url: str | None = Field(max_length=127, default="", description="Secondary OCSP server URL.")    
    secondary_cert: str | None = Field(max_length=127, default="", description="Secondary OCSP server certificate.")  # datasource: ['vpn.certificate.remote.name', 'vpn.certificate.ca.name']    
    unavail_action: Literal["revoke", "ignore"] | None = Field(default="revoke", description="Action when server is unavailable (revoke the certificate or ignore the result of the check).")    
    source_ip: str | None = Field(max_length=63, default="", description="Source IP address for dynamic AIA and OCSP queries.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('cert')
    @classmethod
    def validate_cert(cls, v: Any) -> Any:
        """
        Validate cert field.
        
        Datasource: ['vpn.certificate.remote.name', 'vpn.certificate.ca.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('secondary_cert')
    @classmethod
    def validate_secondary_cert(cls, v: Any) -> Any:
        """
        Validate secondary_cert field.
        
        Datasource: ['vpn.certificate.remote.name', 'vpn.certificate.ca.name']
        
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
    "OcspServerModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:34.687354Z
# ============================================================================