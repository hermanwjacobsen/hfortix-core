"""
Pydantic Models for CMDB - authentication/scheme

Runtime validation models for authentication/scheme configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.authentication.scheme import 
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
# Child Table Models
# ============================================================================

class SchemeUserDatabase(BaseModel):
    """
    Child table model for user-database.
    
    Authentication server to contain user information; "local-user-db" (default) or "123" (for LDAP).
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Authentication server name.")  # datasource: ['system.datasource.name', 'user.radius.name', 'user.tacacs+.name', 'user.ldap.name', 'user.group.name', 'user.scim.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class SchemeMethodEnum(str, Enum):
    """Allowed values for method field."""
    NTLM = "ntlm"    BASIC = "basic"    DIGEST = "digest"    FORM = "form"    NEGOTIATE = "negotiate"    FSSO = "fsso"    RSSO = "rsso"    SSH_PUBLICKEY = "ssh-publickey"    CERT = "cert"    SAML = "saml"    ENTRA_SSO = "entra-sso"

# ============================================================================
# Main Model
# ============================================================================

class SchemeModel(BaseModel):
    """
    Pydantic model for authentication/scheme configuration.
    
    Configure Authentication Schemes.
    
    Validation Rules:        - name: max_length=35 pattern=        - method: pattern=        - negotiate_ntlm: pattern=        - kerberos_keytab: max_length=35 pattern=        - domain_controller: max_length=35 pattern=        - saml_server: max_length=35 pattern=        - saml_timeout: min=30 max=1200 pattern=        - fsso_agent_for_ntlm: max_length=35 pattern=        - require_tfa: pattern=        - fsso_guest: pattern=        - user_cert: pattern=        - cert_http_header: pattern=        - user_database: pattern=        - ssh_ca: max_length=35 pattern=        - external_idp: max_length=35 pattern=        - group_attr_type: pattern=        - digest_algo: pattern=        - digest_rfc2069: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=35, default="", description="Authentication scheme name.")    
    method: list[Method] = Field(default="", description="Authentication methods (default = basic).")    
    negotiate_ntlm: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable negotiate authentication for NTLM (default = disable).")    
    kerberos_keytab: str | None = Field(max_length=35, default="", description="Kerberos keytab setting.")  # datasource: ['user.krb-keytab.name']    
    domain_controller: str | None = Field(max_length=35, default="", description="Domain controller setting.")  # datasource: ['user.domain-controller.name']    
    saml_server: str | None = Field(max_length=35, default="", description="SAML configuration.")  # datasource: ['user.saml.name']    
    saml_timeout: int | None = Field(ge=30, le=1200, default=120, description="SAML authentication timeout in seconds.")    
    fsso_agent_for_ntlm: str | None = Field(max_length=35, default="", description="FSSO agent to use for NTLM authentication.")  # datasource: ['user.fsso.name']    
    require_tfa: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable two-factor authentication (default = disable).")    
    fsso_guest: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable user fsso-guest authentication (default = disable).")    
    user_cert: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable authentication with user certificate (default = disable).")    
    cert_http_header: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable authentication with user certificate in Client-Cert HTTP header (default = disable).")    
    user_database: list[UserDatabase] = Field(default=None, description="Authentication server to contain user information; \"local-user-db\" (default) or \"123\" (for LDAP).")    
    ssh_ca: str | None = Field(max_length=35, default="", description="SSH CA name.")  # datasource: ['firewall.ssh.local-ca.name']    
    external_idp: str | None = Field(max_length=35, default="", description="External identity provider configuration.")  # datasource: ['user.external-identity-provider.name']    
    group_attr_type: Literal["display-name", "external-id"] | None = Field(default="display-name", description="Group attribute type used to match SCIM groups (default = display-name).")    
    digest_algo: list[DigestAlgo] = Field(default="md5 sha-256", description="Digest Authentication Algorithms.")    
    digest_rfc2069: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable support for the deprecated RFC2069 Digest Client (no cnonce field, default = disable).")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('kerberos_keytab')
    @classmethod
    def validate_kerberos_keytab(cls, v: Any) -> Any:
        """
        Validate kerberos_keytab field.
        
        Datasource: ['user.krb-keytab.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('domain_controller')
    @classmethod
    def validate_domain_controller(cls, v: Any) -> Any:
        """
        Validate domain_controller field.
        
        Datasource: ['user.domain-controller.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('saml_server')
    @classmethod
    def validate_saml_server(cls, v: Any) -> Any:
        """
        Validate saml_server field.
        
        Datasource: ['user.saml.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('fsso_agent_for_ntlm')
    @classmethod
    def validate_fsso_agent_for_ntlm(cls, v: Any) -> Any:
        """
        Validate fsso_agent_for_ntlm field.
        
        Datasource: ['user.fsso.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('ssh_ca')
    @classmethod
    def validate_ssh_ca(cls, v: Any) -> Any:
        """
        Validate ssh_ca field.
        
        Datasource: ['firewall.ssh.local-ca.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('external_idp')
    @classmethod
    def validate_external_idp(cls, v: Any) -> Any:
        """
        Validate external_idp field.
        
        Datasource: ['user.external-identity-provider.name']
        
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
    "SchemeModel",    "SchemeUserDatabase",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:35.218201Z
# ============================================================================