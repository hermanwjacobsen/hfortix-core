"""
Pydantic Models for CMDB - authentication/rule

Runtime validation models for authentication/rule configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.authentication.rule import 
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

class RuleSrcintf(BaseModel):
    """
    Child table model for srcintf.
    
    Incoming (ingress) interface.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="Interface name.")  # datasource: ['system.interface.name', 'system.zone.name', 'system.sdwan.zone.name']
class RuleSrcaddr(BaseModel):
    """
    Child table model for srcaddr.
    
    Authentication is required for the selected IPv4 source address.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name', 'firewall.proxy-address.name', 'firewall.proxy-addrgrp.name', 'system.external-resource.name']
class RuleDstaddr(BaseModel):
    """
    Child table model for dstaddr.
    
    Select an IPv4 destination address from available options. Required for web proxy authentication.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name', 'firewall.proxy-address.name', 'firewall.proxy-addrgrp.name', 'system.external-resource.name']
class RuleSrcaddr6(BaseModel):
    """
    Child table model for srcaddr6.
    
    Authentication is required for the selected IPv6 source address.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address6.name', 'firewall.addrgrp6.name']
class RuleDstaddr6(BaseModel):
    """
    Child table model for dstaddr6.
    
    Select an IPv6 destination address from available options. Required for web proxy authentication.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address6.name', 'firewall.addrgrp6.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class RuleProtocolEnum(str, Enum):
    """Allowed values for protocol field."""
    HTTP = "http"    FTP = "ftp"    SOCKS = "socks"    SSH = "ssh"    ZTNA_PORTAL = "ztna-portal"

# ============================================================================
# Main Model
# ============================================================================

class RuleModel(BaseModel):
    """
    Pydantic model for authentication/rule configuration.
    
    Configure Authentication Rules.
    
    Validation Rules:        - name: max_length=35 pattern=        - status: pattern=        - protocol: pattern=        - srcintf: pattern=        - srcaddr: pattern=        - dstaddr: pattern=        - srcaddr6: pattern=        - dstaddr6: pattern=        - ip_based: pattern=        - active_auth_method: max_length=35 pattern=        - sso_auth_method: max_length=35 pattern=        - web_auth_cookie: pattern=        - cors_stateful: pattern=        - cors_depth: min=1 max=8 pattern=        - cert_auth_cookie: pattern=        - transaction_based: pattern=        - web_portal: pattern=        - comments: max_length=1023 pattern=        - session_logout: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=35, default="", description="Authentication rule name.")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable this authentication rule.")    
    protocol: ProtocolEnum | None = Field(default="http", description="Authentication is required for the selected protocol (default = HTTP).")    
    srcintf: list[Srcintf] = Field(default=None, description="Incoming (ingress) interface.")    
    srcaddr: list[Srcaddr] = Field(default=None, description="Authentication is required for the selected IPv4 source address.")    
    dstaddr: list[Dstaddr] = Field(default=None, description="Select an IPv4 destination address from available options. Required for web proxy authentication.")    
    srcaddr6: list[Srcaddr6] = Field(default=None, description="Authentication is required for the selected IPv6 source address.")    
    dstaddr6: list[Dstaddr6] = Field(default=None, description="Select an IPv6 destination address from available options. Required for web proxy authentication.")    
    ip_based: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable IP-based authentication. When enabled, previously authenticated users from the same IP address will be exempted.")    
    active_auth_method: str | None = Field(max_length=35, default="", description="Select an active authentication method.")  # datasource: ['authentication.scheme.name']    
    sso_auth_method: str | None = Field(max_length=35, default="", description="Select a single-sign on (SSO) authentication method.")  # datasource: ['authentication.scheme.name']    
    web_auth_cookie: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable Web authentication cookies (default = disable).")    
    cors_stateful: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable allowance of CORS access (default = disable).")    
    cors_depth: int | None = Field(ge=1, le=8, default=3, description="Depth to allow CORS access (default = 3).")    
    cert_auth_cookie: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable to use device certificate as authentication cookie (default = enable).")    
    transaction_based: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable transaction based authentication (default = disable).")    
    web_portal: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable web portal for proxy transparent policy (default = enable).")    
    comments: str | None = Field(max_length=1023, default=None, description="Comment.")    
    session_logout: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable logout of a user from the current session.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('active_auth_method')
    @classmethod
    def validate_active_auth_method(cls, v: Any) -> Any:
        """
        Validate active_auth_method field.
        
        Datasource: ['authentication.scheme.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('sso_auth_method')
    @classmethod
    def validate_sso_auth_method(cls, v: Any) -> Any:
        """
        Validate sso_auth_method field.
        
        Datasource: ['authentication.scheme.name']
        
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
    "RuleModel",    "RuleSrcintf",    "RuleSrcaddr",    "RuleDstaddr",    "RuleSrcaddr6",    "RuleDstaddr6",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:34.676676Z
# ============================================================================