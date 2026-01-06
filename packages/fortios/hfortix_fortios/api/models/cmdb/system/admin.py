"""
Pydantic Models for CMDB - system/admin

Runtime validation models for system/admin configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.system.admin import 
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

class AdminVdom(BaseModel):
    """
    Child table model for vdom.
    
    Virtual domain(s) that the administrator can access.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Virtual domain name.")  # datasource: ['system.vdom.name']
class AdminGuestUsergroups(BaseModel):
    """
    Child table model for guest-usergroups.
    
    Select guest user groups.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Select guest user groups.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class AdminTwo_factorEnum(str, Enum):
    """Allowed values for two_factor field."""
    DISABLE = "disable"    FORTITOKEN = "fortitoken"    FORTITOKEN_CLOUD = "fortitoken-cloud"    EMAIL = "email"    SMS = "sms"

# ============================================================================
# Main Model
# ============================================================================

class AdminModel(BaseModel):
    """
    Pydantic model for system/admin configuration.
    
    Configure admin users.
    
    Validation Rules:        - name: max_length=64 pattern=        - vdom: pattern=        - remote_auth: pattern=        - remote_group: max_length=35 pattern=        - wildcard: pattern=        - password: max_length=128 pattern=        - peer_auth: pattern=        - peer_group: max_length=35 pattern=        - trusthost1: pattern=        - trusthost2: pattern=        - trusthost3: pattern=        - trusthost4: pattern=        - trusthost5: pattern=        - trusthost6: pattern=        - trusthost7: pattern=        - trusthost8: pattern=        - trusthost9: pattern=        - trusthost10: pattern=        - ip6_trusthost1: pattern=        - ip6_trusthost2: pattern=        - ip6_trusthost3: pattern=        - ip6_trusthost4: pattern=        - ip6_trusthost5: pattern=        - ip6_trusthost6: pattern=        - ip6_trusthost7: pattern=        - ip6_trusthost8: pattern=        - ip6_trusthost9: pattern=        - ip6_trusthost10: pattern=        - accprofile: max_length=35 pattern=        - allow_remove_admin_session: pattern=        - comments: max_length=255 pattern=        - ssh_public_key1: pattern=        - ssh_public_key2: pattern=        - ssh_public_key3: pattern=        - ssh_certificate: max_length=35 pattern=        - schedule: max_length=35 pattern=        - accprofile_override: pattern=        - vdom_override: pattern=        - password_expire: pattern=        - force_password_change: pattern=        - two_factor: pattern=        - two_factor_authentication: pattern=        - two_factor_notification: pattern=        - fortitoken: max_length=16 pattern=        - email_to: max_length=63 pattern=        - sms_server: pattern=        - sms_custom_server: max_length=35 pattern=        - sms_phone: max_length=15 pattern=        - guest_auth: pattern=        - guest_usergroups: pattern=        - guest_lang: max_length=35 pattern=        - status: pattern=        - list: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=64, default="", description="User name.")    
    vdom: list[Vdom] = Field(default=None, description="Virtual domain(s) that the administrator can access.")    
    remote_auth: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable authentication using a remote RADIUS, LDAP, or TACACS+ server.")    
    remote_group: str = Field(max_length=35, default="", description="User group name used for remote auth.")    
    wildcard: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable wildcard RADIUS authentication.")    
    password: Any = Field(max_length=128, description="Admin user password.")    
    peer_auth: Literal["enable", "disable"] | None = Field(default="disable", description="Set to enable peer certificate authentication (for HTTPS admin access).")    
    peer_group: str = Field(max_length=35, default="", description="Name of peer group defined under config user group which has PKI members. Used for peer certificate authentication (for HTTPS admin access).")    
    trusthost1: str | None = Field(default="0.0.0.0 0.0.0.0", description="Any IPv4 address or subnet address and netmask from which the administrator can connect to the FortiGate unit. Default allows access from any IPv4 address.")    
    trusthost2: str | None = Field(default="0.0.0.0 0.0.0.0", description="Any IPv4 address or subnet address and netmask from which the administrator can connect to the FortiGate unit. Default allows access from any IPv4 address.")    
    trusthost3: str | None = Field(default="0.0.0.0 0.0.0.0", description="Any IPv4 address or subnet address and netmask from which the administrator can connect to the FortiGate unit. Default allows access from any IPv4 address.")    
    trusthost4: str | None = Field(default="0.0.0.0 0.0.0.0", description="Any IPv4 address or subnet address and netmask from which the administrator can connect to the FortiGate unit. Default allows access from any IPv4 address.")    
    trusthost5: str | None = Field(default="0.0.0.0 0.0.0.0", description="Any IPv4 address or subnet address and netmask from which the administrator can connect to the FortiGate unit. Default allows access from any IPv4 address.")    
    trusthost6: str | None = Field(default="0.0.0.0 0.0.0.0", description="Any IPv4 address or subnet address and netmask from which the administrator can connect to the FortiGate unit. Default allows access from any IPv4 address.")    
    trusthost7: str | None = Field(default="0.0.0.0 0.0.0.0", description="Any IPv4 address or subnet address and netmask from which the administrator can connect to the FortiGate unit. Default allows access from any IPv4 address.")    
    trusthost8: str | None = Field(default="0.0.0.0 0.0.0.0", description="Any IPv4 address or subnet address and netmask from which the administrator can connect to the FortiGate unit. Default allows access from any IPv4 address.")    
    trusthost9: str | None = Field(default="0.0.0.0 0.0.0.0", description="Any IPv4 address or subnet address and netmask from which the administrator can connect to the FortiGate unit. Default allows access from any IPv4 address.")    
    trusthost10: str | None = Field(default="0.0.0.0 0.0.0.0", description="Any IPv4 address or subnet address and netmask from which the administrator can connect to the FortiGate unit. Default allows access from any IPv4 address.")    
    ip6_trusthost1: str | None = Field(default="::/0", description="Any IPv6 address from which the administrator can connect to the FortiGate unit. Default allows access from any IPv6 address.")    
    ip6_trusthost2: str | None = Field(default="::/0", description="Any IPv6 address from which the administrator can connect to the FortiGate unit. Default allows access from any IPv6 address.")    
    ip6_trusthost3: str | None = Field(default="::/0", description="Any IPv6 address from which the administrator can connect to the FortiGate unit. Default allows access from any IPv6 address.")    
    ip6_trusthost4: str | None = Field(default="::/0", description="Any IPv6 address from which the administrator can connect to the FortiGate unit. Default allows access from any IPv6 address.")    
    ip6_trusthost5: str | None = Field(default="::/0", description="Any IPv6 address from which the administrator can connect to the FortiGate unit. Default allows access from any IPv6 address.")    
    ip6_trusthost6: str | None = Field(default="::/0", description="Any IPv6 address from which the administrator can connect to the FortiGate unit. Default allows access from any IPv6 address.")    
    ip6_trusthost7: str | None = Field(default="::/0", description="Any IPv6 address from which the administrator can connect to the FortiGate unit. Default allows access from any IPv6 address.")    
    ip6_trusthost8: str | None = Field(default="::/0", description="Any IPv6 address from which the administrator can connect to the FortiGate unit. Default allows access from any IPv6 address.")    
    ip6_trusthost9: str | None = Field(default="::/0", description="Any IPv6 address from which the administrator can connect to the FortiGate unit. Default allows access from any IPv6 address.")    
    ip6_trusthost10: str | None = Field(default="::/0", description="Any IPv6 address from which the administrator can connect to the FortiGate unit. Default allows access from any IPv6 address.")    
    accprofile: str | None = Field(max_length=35, default="", description="Access profile for this administrator. Access profiles control administrator access to FortiGate features.")  # datasource: ['system.accprofile.name']    
    allow_remove_admin_session: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable allow admin session to be removed by privileged admin users.")    
    comments: str | None = Field(max_length=255, default=None, description="Comment.")    
    ssh_public_key1: str | None = Field(default="", description="Public key of an SSH client. The client is authenticated without being asked for credentials. Create the public-private key pair in the SSH client application.")    
    ssh_public_key2: str | None = Field(default="", description="Public key of an SSH client. The client is authenticated without being asked for credentials. Create the public-private key pair in the SSH client application.")    
    ssh_public_key3: str | None = Field(default="", description="Public key of an SSH client. The client is authenticated without being asked for credentials. Create the public-private key pair in the SSH client application.")    
    ssh_certificate: str | None = Field(max_length=35, default="", description="Select the certificate to be used by the FortiGate for authentication with an SSH client.")  # datasource: ['certificate.remote.name']    
    schedule: str | None = Field(max_length=35, default="", description="Firewall schedule used to restrict when the administrator can log in. No schedule means no restrictions.")    
    accprofile_override: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to use the name of an access profile provided by the remote authentication server to control the FortiGate features that this administrator can access.")    
    vdom_override: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to use the names of VDOMs provided by the remote authentication server to control the VDOMs that this administrator can access.")    
    password_expire: Any = Field(default="0000-00-00 00:00:00", description="Password expire time.")    
    force_password_change: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable force password change on next login.")    
    two_factor: TwoFactorEnum | None = Field(default="disable", description="Enable/disable two-factor authentication.")    
    two_factor_authentication: Literal["fortitoken", "email", "sms"] | None = Field(default="", description="Authentication method by FortiToken Cloud.")    
    two_factor_notification: Literal["email", "sms"] | None = Field(default="", description="Notification method for user activation by FortiToken Cloud.")    
    fortitoken: str | None = Field(max_length=16, default="", description="This administrator's FortiToken serial number.")    
    email_to: str | None = Field(max_length=63, default="", description="This administrator's email address.")    
    sms_server: Literal["fortiguard", "custom"] | None = Field(default="fortiguard", description="Send SMS messages using the FortiGuard SMS server or a custom server.")    
    sms_custom_server: str | None = Field(max_length=35, default="", description="Custom SMS server to send SMS messages to.")  # datasource: ['system.sms-server.name']    
    sms_phone: str | None = Field(max_length=15, default="", description="Phone number on which the administrator receives SMS messages.")    
    guest_auth: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable guest authentication.")    
    guest_usergroups: list[GuestUsergroups] = Field(default=None, description="Select guest user groups.")    
    guest_lang: str | None = Field(max_length=35, default="", description="Guest management portal language.")  # datasource: ['system.custom-language.name']    
    status: Any = Field(default=None, description="print admin status information")    
    list: Any = Field(default=None, description="print admin list information")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('accprofile')
    @classmethod
    def validate_accprofile(cls, v: Any) -> Any:
        """
        Validate accprofile field.
        
        Datasource: ['system.accprofile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('ssh_certificate')
    @classmethod
    def validate_ssh_certificate(cls, v: Any) -> Any:
        """
        Validate ssh_certificate field.
        
        Datasource: ['certificate.remote.name']
        
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
    @field_validator('guest_lang')
    @classmethod
    def validate_guest_lang(cls, v: Any) -> Any:
        """
        Validate guest_lang field.
        
        Datasource: ['system.custom-language.name']
        
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
    "AdminModel",    "AdminVdom",    "AdminGuestUsergroups",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:33.270994Z
# ============================================================================