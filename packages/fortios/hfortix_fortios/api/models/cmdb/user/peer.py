"""
Pydantic Models for CMDB - user/peer

Runtime validation models for user/peer configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.user.peer import 
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
from enum import Enum

# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class PeerCn_typeEnum(str, Enum):
    """Allowed values for cn_type field."""
    STRING = "string"    EMAIL = "email"    FQDN = "FQDN"    IPV4 = "ipv4"    IPV6 = "ipv6"

# ============================================================================
# Main Model
# ============================================================================

class PeerModel(BaseModel):
    """
    Pydantic model for user/peer configuration.
    
    Configure peer users.
    
    Validation Rules:        - name: max_length=35 pattern=        - mandatory_ca_verify: pattern=        - ca: max_length=127 pattern=        - subject: max_length=255 pattern=        - cn: max_length=255 pattern=        - cn_type: pattern=        - mfa_mode: pattern=        - mfa_server: max_length=35 pattern=        - mfa_username: max_length=35 pattern=        - mfa_password: max_length=128 pattern=        - ocsp_override_server: max_length=35 pattern=        - two_factor: pattern=        - passwd: max_length=128 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=35, default="", description="Peer name.")    
    mandatory_ca_verify: Literal["enable", "disable"] | None = Field(default="enable", description="Determine what happens to the peer if the CA certificate is not installed. Disable to automatically consider the peer certificate as valid.")    
    ca: str | None = Field(max_length=127, default="", description="Name of the CA certificate.")  # datasource: ['vpn.certificate.ca.name']    
    subject: str | None = Field(max_length=255, default="", description="Peer certificate name constraints.")    
    cn: str | None = Field(max_length=255, default="", description="Peer certificate common name.")    
    cn_type: CnTypeEnum | None = Field(default="string", description="Peer certificate common name type.")    
    mfa_mode: Literal["none", "password", "subject-identity"] | None = Field(default="none", description="MFA mode for remote peer authentication/authorization.")    
    mfa_server: str | None = Field(max_length=35, default="", description="Name of a remote authenticator. Performs client access right check.")  # datasource: ['user.radius.name', 'user.ldap.name']    
    mfa_username: str | None = Field(max_length=35, default="", description="Unified username for remote authentication.")    
    mfa_password: Any = Field(max_length=128, default=None, description="Unified password for remote authentication. This field may be left empty when RADIUS authentication is used, in which case the FortiGate will use the RADIUS username as a password. ")    
    ocsp_override_server: str | None = Field(max_length=35, default="", description="Online Certificate Status Protocol (OCSP) server for certificate retrieval.")  # datasource: ['vpn.certificate.ocsp-server.name']    
    two_factor: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable two-factor authentication, applying certificate and password-based authentication.")    
    passwd: Any = Field(max_length=128, default=None, description="Peer's password used for two-factor authentication.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('ca')
    @classmethod
    def validate_ca(cls, v: Any) -> Any:
        """
        Validate ca field.
        
        Datasource: ['vpn.certificate.ca.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('mfa_server')
    @classmethod
    def validate_mfa_server(cls, v: Any) -> Any:
        """
        Validate mfa_server field.
        
        Datasource: ['user.radius.name', 'user.ldap.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('ocsp_override_server')
    @classmethod
    def validate_ocsp_override_server(cls, v: Any) -> Any:
        """
        Validate ocsp_override_server field.
        
        Datasource: ['vpn.certificate.ocsp-server.name']
        
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
    "PeerModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:33.766579Z
# ============================================================================