"""
Pydantic Models for CMDB - user/local

Runtime validation models for user/local configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.user.local import 
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

class LocalTypeEnum(str, Enum):
    """Allowed values for type field."""
    PASSWORD = "password"    RADIUS = "radius"    TACACS = "tacacs+"    LDAP = "ldap"    SAML = "saml"
class LocalTwo_factorEnum(str, Enum):
    """Allowed values for two_factor field."""
    DISABLE = "disable"    FORTITOKEN = "fortitoken"    FORTITOKEN_CLOUD = "fortitoken-cloud"    EMAIL = "email"    SMS = "sms"

# ============================================================================
# Main Model
# ============================================================================

class LocalModel(BaseModel):
    """
    Pydantic model for user/local configuration.
    
    Configure local users.
    
    Validation Rules:        - name: max_length=64 pattern=        - id: min=0 max=4294967295 pattern=        - status: pattern=        - type: pattern=        - passwd: max_length=128 pattern=        - ldap_server: max_length=35 pattern=        - radius_server: max_length=35 pattern=        - tacacs+_server: max_length=35 pattern=        - saml_server: max_length=35 pattern=        - two_factor: pattern=        - two_factor_authentication: pattern=        - two_factor_notification: pattern=        - fortitoken: max_length=16 pattern=        - email_to: max_length=63 pattern=        - sms_server: pattern=        - sms_custom_server: max_length=35 pattern=        - sms_phone: max_length=15 pattern=        - passwd_policy: max_length=35 pattern=        - passwd_time: pattern=        - authtimeout: min=0 max=1440 pattern=        - workstation: max_length=35 pattern=        - auth_concurrent_override: pattern=        - auth_concurrent_value: min=0 max=100 pattern=        - ppk_secret: pattern=        - ppk_identity: max_length=35 pattern=        - qkd_profile: max_length=35 pattern=        - username_sensitivity: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=64, default="", description="Local user name.")    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="User ID.")    
    status: Literal["enable", "disable"] = Field(default="enable", description="Enable/disable allowing the local user to authenticate with the FortiGate unit.")    
    type: TypeEnum = Field(default="password", description="Authentication method.")    
    passwd: Any = Field(max_length=128, description="User's password.")    
    ldap_server: str = Field(max_length=35, default="", description="Name of LDAP server with which the user must authenticate.")  # datasource: ['user.ldap.name']    
    radius_server: str = Field(max_length=35, default="", description="Name of RADIUS server with which the user must authenticate.")  # datasource: ['user.radius.name']    
    tacacs+_server: str = Field(max_length=35, default="", description="Name of TACACS+ server with which the user must authenticate.")  # datasource: ['user.tacacs+.name']    
    saml_server: str = Field(max_length=35, default="", description="Name of SAML server with which the user must authenticate.")  # datasource: ['user.saml.name']    
    two_factor: TwoFactorEnum | None = Field(default="disable", description="Enable/disable two-factor authentication.")    
    two_factor_authentication: Literal["fortitoken", "email", "sms"] | None = Field(default="", description="Authentication method by FortiToken Cloud.")    
    two_factor_notification: Literal["email", "sms"] | None = Field(default="", description="Notification method for user activation by FortiToken Cloud.")    
    fortitoken: str | None = Field(max_length=16, default="", description="Two-factor recipient's FortiToken serial number.")  # datasource: ['user.fortitoken.serial-number']    
    email_to: str | None = Field(max_length=63, default="", description="Two-factor recipient's email address.")    
    sms_server: Literal["fortiguard", "custom"] | None = Field(default="fortiguard", description="Send SMS through FortiGuard or other external server.")    
    sms_custom_server: str | None = Field(max_length=35, default="", description="Two-factor recipient's SMS server.")  # datasource: ['system.sms-server.name']    
    sms_phone: str | None = Field(max_length=15, default="", description="Two-factor recipient's mobile phone number.")    
    passwd_policy: str | None = Field(max_length=35, default="", description="Password policy to apply to this user, as defined in config user password-policy.")  # datasource: ['user.password-policy.name']    
    passwd_time: str | None = Field(default="", description="Time of the last password update.")    
    authtimeout: int | None = Field(ge=0, le=1440, default=0, description="Time in minutes before the authentication timeout for a user is reached.")    
    workstation: str | None = Field(max_length=35, default="", description="Name of the remote user workstation, if you want to limit the user to authenticate only from a particular workstation.")    
    auth_concurrent_override: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable overriding the policy-auth-concurrent under config system global.")    
    auth_concurrent_value: int | None = Field(ge=0, le=100, default=0, description="Maximum number of concurrent logins permitted from the same user.")    
    ppk_secret: Any = Field(default=None, description="IKEv2 Postquantum Preshared Key (ASCII string or hexadecimal encoded with a leading 0x).")    
    ppk_identity: str | None = Field(max_length=35, default="", description="IKEv2 Postquantum Preshared Key Identity.")    
    qkd_profile: str | None = Field(max_length=35, default="", description="Quantum Key Distribution (QKD) profile.")  # datasource: ['vpn.qkd.name']    
    username_sensitivity: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable case and accent sensitivity when performing username matching (accents are stripped and case is ignored when disabled).")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('ldap_server')
    @classmethod
    def validate_ldap_server(cls, v: Any) -> Any:
        """
        Validate ldap_server field.
        
        Datasource: ['user.ldap.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('radius_server')
    @classmethod
    def validate_radius_server(cls, v: Any) -> Any:
        """
        Validate radius_server field.
        
        Datasource: ['user.radius.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('tacacs+_server')
    @classmethod
    def validate_tacacs+_server(cls, v: Any) -> Any:
        """
        Validate tacacs+_server field.
        
        Datasource: ['user.tacacs+.name']
        
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
    @field_validator('fortitoken')
    @classmethod
    def validate_fortitoken(cls, v: Any) -> Any:
        """
        Validate fortitoken field.
        
        Datasource: ['user.fortitoken.serial-number']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('sms_custom_server')
    @classmethod
    def validate_sms_custom_server(cls, v: Any) -> Any:
        """
        Validate sms_custom_server field.
        
        Datasource: ['system.sms-server.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('passwd_policy')
    @classmethod
    def validate_passwd_policy(cls, v: Any) -> Any:
        """
        Validate passwd_policy field.
        
        Datasource: ['user.password-policy.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('qkd_profile')
    @classmethod
    def validate_qkd_profile(cls, v: Any) -> Any:
        """
        Validate qkd_profile field.
        
        Datasource: ['vpn.qkd.name']
        
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
    "LocalModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:33.337004Z
# ============================================================================