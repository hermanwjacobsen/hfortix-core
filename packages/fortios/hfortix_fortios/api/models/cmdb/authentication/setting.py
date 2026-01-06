"""
Pydantic Models for CMDB - authentication/setting

Runtime validation models for authentication/setting configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.authentication.setting import 
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

# ============================================================================
# Child Table Models
# ============================================================================

class SettingUserCertCa(BaseModel):
    """
    Child table model for user-cert-ca.
    
    CA certificate used for client certificate verification.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="CA certificate list.")  # datasource: ['vpn.certificate.ca.name', 'vpn.certificate.local.name']
class SettingDevRange(BaseModel):
    """
    Child table model for dev-range.
    
    Address range for the IP based device query.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class SettingModel(BaseModel):
    """
    Pydantic model for authentication/setting configuration.
    
    Configure authentication setting.
    
    Validation Rules:        - active_auth_scheme: max_length=35 pattern=        - sso_auth_scheme: max_length=35 pattern=        - update_time: pattern=        - persistent_cookie: pattern=        - ip_auth_cookie: pattern=        - cookie_max_age: min=30 max=10080 pattern=        - cookie_refresh_div: min=2 max=4 pattern=        - captive_portal_type: pattern=        - captive_portal_ip: pattern=        - captive_portal_ip6: pattern=        - captive_portal: max_length=255 pattern=        - captive_portal6: max_length=255 pattern=        - cert_auth: pattern=        - cert_captive_portal: max_length=255 pattern=        - cert_captive_portal_ip: pattern=        - cert_captive_portal_port: min=1 max=65535 pattern=        - captive_portal_port: min=1 max=65535 pattern=        - auth_https: pattern=        - captive_portal_ssl_port: min=1 max=65535 pattern=        - user_cert_ca: pattern=        - dev_range: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    active_auth_scheme: str | None = Field(max_length=35, default="", description="Active authentication method (scheme name).")  # datasource: ['authentication.scheme.name']    
    sso_auth_scheme: str | None = Field(max_length=35, default="", description="Single-Sign-On authentication method (scheme name).")  # datasource: ['authentication.scheme.name']    
    update_time: str | None = Field(default="", description="Time of the last update.")    
    persistent_cookie: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable persistent cookie on web portal authentication (default = enable).")    
    ip_auth_cookie: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable persistent cookie on IP based web portal authentication (default = disable).")    
    cookie_max_age: int | None = Field(ge=30, le=10080, default=480, description="Persistent web portal cookie maximum age in minutes (30 - 10080 (1 week), default = 480 (8 hours)).")    
    cookie_refresh_div: int | None = Field(ge=2, le=4, default=2, description="Refresh rate divider of persistent web portal cookie (default = 2). Refresh value = cookie-max-age/cookie-refresh-div.")    
    captive_portal_type: Literal["fqdn", "ip"] | None = Field(default="fqdn", description="Captive portal type.")    
    captive_portal_ip: str | None = Field(default="0.0.0.0", description="Captive portal IP address.")    
    captive_portal_ip6: str | None = Field(default="::", description="Captive portal IPv6 address.")    
    captive_portal: str | None = Field(max_length=255, default="", description="Captive portal host name.")  # datasource: ['firewall.address.name']    
    captive_portal6: str | None = Field(max_length=255, default="", description="IPv6 captive portal host name.")  # datasource: ['firewall.address6.name']    
    cert_auth: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable redirecting certificate authentication to HTTPS portal.")    
    cert_captive_portal: str | None = Field(max_length=255, default="", description="Certificate captive portal host name.")  # datasource: ['firewall.address.name']    
    cert_captive_portal_ip: str | None = Field(default="0.0.0.0", description="Certificate captive portal IP address.")    
    cert_captive_portal_port: int | None = Field(ge=1, le=65535, default=7832, description="Certificate captive portal port number (1 - 65535, default = 7832).")    
    captive_portal_port: int | None = Field(ge=1, le=65535, default=7830, description="Captive portal port number (1 - 65535, default = 7830).")    
    auth_https: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable redirecting HTTP user authentication to HTTPS.")    
    captive_portal_ssl_port: int | None = Field(ge=1, le=65535, default=7831, description="Captive portal SSL port number (1 - 65535, default = 7831).")    
    user_cert_ca: list[UserCertCa] = Field(default=None, description="CA certificate used for client certificate verification.")    
    dev_range: list[DevRange] = Field(default=None, description="Address range for the IP based device query.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('active_auth_scheme')
    @classmethod
    def validate_active_auth_scheme(cls, v: Any) -> Any:
        """
        Validate active_auth_scheme field.
        
        Datasource: ['authentication.scheme.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('sso_auth_scheme')
    @classmethod
    def validate_sso_auth_scheme(cls, v: Any) -> Any:
        """
        Validate sso_auth_scheme field.
        
        Datasource: ['authentication.scheme.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('captive_portal')
    @classmethod
    def validate_captive_portal(cls, v: Any) -> Any:
        """
        Validate captive_portal field.
        
        Datasource: ['firewall.address.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('captive_portal6')
    @classmethod
    def validate_captive_portal6(cls, v: Any) -> Any:
        """
        Validate captive_portal6 field.
        
        Datasource: ['firewall.address6.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('cert_captive_portal')
    @classmethod
    def validate_cert_captive_portal(cls, v: Any) -> Any:
        """
        Validate cert_captive_portal field.
        
        Datasource: ['firewall.address.name']
        
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
    "SettingModel",    "SettingUserCertCa",    "SettingDevRange",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:33.039809Z
# ============================================================================