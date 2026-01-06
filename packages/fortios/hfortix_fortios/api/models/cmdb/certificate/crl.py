"""
Pydantic Models for CMDB - certificate/crl

Runtime validation models for certificate/crl configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.certificate.crl import 
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

class CrlModel(BaseModel):
    """
    Pydantic model for certificate/crl configuration.
    
    Certificate Revocation List as a PEM file.
    
    Validation Rules:        - name: max_length=35 pattern=        - crl: pattern=        - range: pattern=        - source: pattern=        - update_vdom: max_length=31 pattern=        - ldap_server: max_length=35 pattern=        - ldap_username: max_length=63 pattern=        - ldap_password: max_length=128 pattern=        - http_url: max_length=255 pattern=        - scep_url: max_length=255 pattern=        - scep_cert: max_length=35 pattern=        - update_interval: min=0 max=4294967295 pattern=        - source_ip: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str = Field(max_length=35, default="", description="Name.")    
    crl: str | None = Field(default="", description="Certificate Revocation List as a PEM file.")    
    range: Literal["global", "vdom"] | None = Field(default="global", description="Either global or VDOM IP address range for the certificate.")    
    source: Literal["factory", "user", "bundle"] | None = Field(default="user", description="Certificate source type.")    
    update_vdom: str | None = Field(max_length=31, default="root", description="VDOM for CRL update.")  # datasource: ['system.vdom.name']    
    ldap_server: str | None = Field(max_length=35, default="", description="LDAP server name for CRL auto-update.")    
    ldap_username: str | None = Field(max_length=63, default="", description="LDAP server user name.")    
    ldap_password: Any = Field(max_length=128, default=None, description="LDAP server user password.")    
    http_url: str | None = Field(max_length=255, default="", description="HTTP server URL for CRL auto-update.")    
    scep_url: str | None = Field(max_length=255, default="", description="SCEP server URL for CRL auto-update.")    
    scep_cert: str | None = Field(max_length=35, default="Fortinet_CA_SSL", description="Local certificate for SCEP communication for CRL auto-update.")  # datasource: ['certificate.local.name']    
    update_interval: int | None = Field(ge=0, le=4294967295, default=0, description="Time in seconds before the FortiGate checks for an updated CRL. Set to 0 to update only when it expires.")    
    source_ip: str | None = Field(default="0.0.0.0", description="Source IP address for communications to a HTTP or SCEP CA server.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('update_vdom')
    @classmethod
    def validate_update_vdom(cls, v: Any) -> Any:
        """
        Validate update_vdom field.
        
        Datasource: ['system.vdom.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('scep_cert')
    @classmethod
    def validate_scep_cert(cls, v: Any) -> Any:
        """
        Validate scep_cert field.
        
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
    "CrlModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:35.192329Z
# ============================================================================