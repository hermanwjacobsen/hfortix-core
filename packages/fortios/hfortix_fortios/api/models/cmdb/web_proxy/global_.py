"""
Pydantic Models for CMDB - web_proxy/global_

Runtime validation models for web_proxy/global_ configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.web_proxy.global_ import 
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

class GlobalLearnClientIpSrcaddr(BaseModel):
    """
    Child table model for learn-client-ip-srcaddr.
    
    Source address name (srcaddr or srcaddr6 must be set).
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name']
class GlobalLearnClientIpSrcaddr6(BaseModel):
    """
    Child table model for learn-client-ip-srcaddr6.
    
    IPv6 Source address name (srcaddr or srcaddr6 must be set).
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address6.name', 'firewall.addrgrp6.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class GlobalModel(BaseModel):
    """
    Pydantic model for web_proxy/global_ configuration.
    
    Configure Web proxy global settings.
    
    Validation Rules:        - ssl_cert: max_length=35 pattern=        - ssl_ca_cert: max_length=35 pattern=        - fast_policy_match: pattern=        - ldap_user_cache: pattern=        - proxy_fqdn: max_length=255 pattern=        - max_request_length: min=2 max=64 pattern=        - max_message_length: min=16 max=256 pattern=        - http2_client_window_size: min=65535 max=2147483647 pattern=        - http2_server_window_size: min=65535 max=2147483647 pattern=        - auth_sign_timeout: min=30 max=3600 pattern=        - strict_web_check: pattern=        - forward_proxy_auth: pattern=        - forward_server_affinity_timeout: min=6 max=60 pattern=        - max_waf_body_cache_length: min=1 max=1024 pattern=        - webproxy_profile: max_length=63 pattern=        - learn_client_ip: pattern=        - always_learn_client_ip: pattern=        - learn_client_ip_from_header: pattern=        - learn_client_ip_srcaddr: pattern=        - learn_client_ip_srcaddr6: pattern=        - src_affinity_exempt_addr: pattern=        - src_affinity_exempt_addr6: pattern=        - policy_partial_match: pattern=        - log_policy_pending: pattern=        - log_forward_server: pattern=        - log_app_id: pattern=        - proxy_transparent_cert_inspection: pattern=        - request_obs_fold: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    ssl_cert: str | None = Field(max_length=35, default="Fortinet_Factory", description="SSL certificate for SSL interception.")  # datasource: ['vpn.certificate.local.name']    
    ssl_ca_cert: str | None = Field(max_length=35, default="Fortinet_CA_SSL", description="SSL CA certificate for SSL interception.")  # datasource: ['vpn.certificate.local.name', 'vpn.certificate.hsm-local.name']    
    fast_policy_match: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable fast matching algorithm for explicit and transparent proxy policy.")    
    ldap_user_cache: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable LDAP user cache for explicit and transparent proxy user.")    
    proxy_fqdn: str = Field(max_length=255, default="default.fqdn", description="Fully Qualified Domain Name of the explicit web proxy (default = default.fqdn) that clients connect to.")    
    max_request_length: int | None = Field(ge=2, le=64, default=8, description="Maximum length of HTTP request line (2 - 64 Kbytes, default = 8).")    
    max_message_length: int | None = Field(ge=16, le=256, default=32, description="Maximum length of HTTP message, not including body (16 - 256 Kbytes, default = 32).")    
    http2_client_window_size: int | None = Field(ge=65535, le=2147483647, default=1048576, description="HTTP/2 client initial window size in bytes (65535 - 2147483647, default = 1048576 (1MB)).")    
    http2_server_window_size: int | None = Field(ge=65535, le=2147483647, default=1048576, description="HTTP/2 server initial window size in bytes (65535 - 2147483647, default = 1048576 (1MB)).")    
    auth_sign_timeout: int | None = Field(ge=30, le=3600, default=120, description="Proxy auth query sign timeout in seconds (30 - 3600, default = 120).")    
    strict_web_check: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable strict web checking to block web sites that send incorrect headers that don't conform to HTTP.")    
    forward_proxy_auth: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable forwarding proxy authentication headers.")    
    forward_server_affinity_timeout: int | None = Field(ge=6, le=60, default=30, description="Period of time before the source IP's traffic is no longer assigned to the forwarding server (6 - 60 min, default = 30).")    
    max_waf_body_cache_length: int | None = Field(ge=1, le=1024, default=1, description="Maximum length of HTTP messages processed by Web Application Firewall (WAF) (1 - 1024 Kbytes, default = 1).")    
    webproxy_profile: str | None = Field(max_length=63, default="", description="Name of the web proxy profile to apply when explicit proxy traffic is allowed by default and traffic is accepted that does not match an explicit proxy policy.")  # datasource: ['web-proxy.profile.name']    
    learn_client_ip: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable learning the client's IP address from headers.")    
    always_learn_client_ip: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable learning the client's IP address from headers for every request.")    
    learn_client_ip_from_header: list[LearnClientIpFromHeader] = Field(default="", description="Learn client IP address from the specified headers.")    
    learn_client_ip_srcaddr: list[LearnClientIpSrcaddr] = Field(default=None, description="Source address name (srcaddr or srcaddr6 must be set).")    
    learn_client_ip_srcaddr6: list[LearnClientIpSrcaddr6] = Field(default=None, description="IPv6 Source address name (srcaddr or srcaddr6 must be set).")    
    src_affinity_exempt_addr: list[SrcAffinityExemptAddr] = Field(default="", description="IPv4 source addresses to exempt proxy affinity.")    
    src_affinity_exempt_addr6: list[SrcAffinityExemptAddr6] = Field(default="", description="IPv6 source addresses to exempt proxy affinity.")    
    policy_partial_match: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable policy partial matching.")    
    log_policy_pending: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable logging sessions that are pending on policy matching.")    
    log_forward_server: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable forward server name logging in forward traffic log.")    
    log_app_id: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable always log application type in traffic log.")    
    proxy_transparent_cert_inspection: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable transparent proxy certificate inspection.")    
    request_obs_fold: Literal["replace-with-sp", "block", "keep"] | None = Field(default="keep", description="Action when HTTP/1.x request header contains obs-fold (default = keep).")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('ssl_cert')
    @classmethod
    def validate_ssl_cert(cls, v: Any) -> Any:
        """
        Validate ssl_cert field.
        
        Datasource: ['vpn.certificate.local.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('ssl_ca_cert')
    @classmethod
    def validate_ssl_ca_cert(cls, v: Any) -> Any:
        """
        Validate ssl_ca_cert field.
        
        Datasource: ['vpn.certificate.local.name', 'vpn.certificate.hsm-local.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('webproxy_profile')
    @classmethod
    def validate_webproxy_profile(cls, v: Any) -> Any:
        """
        Validate webproxy_profile field.
        
        Datasource: ['web-proxy.profile.name']
        
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
    "GlobalModel",    "GlobalLearnClientIpSrcaddr",    "GlobalLearnClientIpSrcaddr6",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:33.378591Z
# ============================================================================