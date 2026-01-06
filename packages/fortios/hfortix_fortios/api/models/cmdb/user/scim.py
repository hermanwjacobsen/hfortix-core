"""
Pydantic Models for CMDB - user/scim

Runtime validation models for user/scim configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.user.scim import 
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

class ScimModel(BaseModel):
    """
    Pydantic model for user/scim configuration.
    
    Configure SCIM client entries.
    
    Validation Rules:        - name: max_length=35 pattern=        - id: min=0 max=4294967295 pattern=        - status: pattern=        - base_url: max_length=127 pattern=        - auth_method: pattern=        - token_certificate: max_length=79 pattern=        - secret: max_length=128 pattern=        - certificate: max_length=79 pattern=        - client_identity_check: pattern=        - cascade: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str = Field(max_length=35, default="", description="SCIM client name.")    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="SCIM client ID.")    
    status: Literal["enable", "disable"] = Field(default="disable", description="Enable/disable System for Cross-domain Identity Management (SCIM).")    
    base_url: str | None = Field(max_length=127, default="", description="Server URL to receive SCIM create, read, update, delete (CRUD) requests.")    
    auth_method: Literal["token", "base"] | None = Field(default="token", description="TLS client authentication methods (default = bearer token).")    
    token_certificate: str | None = Field(max_length=79, default="", description="Certificate for token verification.")  # datasource: ['vpn.certificate.remote.name', 'vpn.certificate.local.name']    
    secret: Any = Field(max_length=128, default=None, description="Secret for token verification or base authentication.")    
    certificate: str | None = Field(max_length=79, default="", description="Certificate for client verification during TLS handshake.")  # datasource: ['vpn.certificate.ca.name', 'vpn.certificate.remote.name', 'certificate.ca.name', 'certificate.remote.name']    
    client_identity_check: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable client identity check.")    
    cascade: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable to follow SCIM users/groups changes in IDP.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('token_certificate')
    @classmethod
    def validate_token_certificate(cls, v: Any) -> Any:
        """
        Validate token_certificate field.
        
        Datasource: ['vpn.certificate.remote.name', 'vpn.certificate.local.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('certificate')
    @classmethod
    def validate_certificate(cls, v: Any) -> Any:
        """
        Validate certificate field.
        
        Datasource: ['vpn.certificate.ca.name', 'vpn.certificate.remote.name', 'certificate.ca.name', 'certificate.remote.name']
        
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
    "ScimModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:32.926237Z
# ============================================================================