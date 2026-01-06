"""
Pydantic Models for CMDB - ztna/web_proxy

Runtime validation models for ztna/web_proxy configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.ztna.web_proxy import 
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
# Child Table Models
# ============================================================================

class WebProxyApiGateway(BaseModel):
    """
    Child table model for api-gateway.
    
    Set IPv4 API Gateway.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="API Gateway ID.")    
    url_map: str = Field(max_length=511, default="/", description="URL pattern to match.")    
    service: Literal["http", "https"] = Field(default="https", description="Service.")    
    ldb_method: LdbMethodEnum | None = Field(default="static", description="Method used to distribute sessions to real servers.")    
    url_map_type: Literal["sub-string", "wildcard", "regex"] = Field(default="sub-string", description="Type of url-map.")    
    h2_support: Literal["enable", "disable"] = Field(default="enable", description="HTTP2 support, default=Enable.")    
    h3_support: Literal["enable", "disable"] | None = Field(default="disable", description="HTTP3/QUIC support, default=Disable.")    
    quic: list[Quic] = Field(default=None, description="QUIC setting.")    
    realservers: list[Realservers] = Field(default=None, description="Select the real servers that this Access Proxy will distribute traffic to.")    
    persistence: Literal["none", "http-cookie"] | None = Field(default="none", description="Configure how to make sure that clients connect to the same server every time they make a request that is part of the same session.")    
    http_cookie_domain_from_host: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable use of HTTP cookie domain from host field in HTTP.")    
    http_cookie_domain: str | None = Field(max_length=35, default="", description="Domain that HTTP cookie persistence should apply to.")    
    http_cookie_path: str | None = Field(max_length=35, default="", description="Limit HTTP cookie persistence to the specified path.")    
    http_cookie_generation: int | None = Field(ge=0, le=4294967295, default=0, description="Generation of HTTP cookie to be accepted. Changing invalidates all existing cookies.")    
    http_cookie_age: int | None = Field(ge=0, le=525600, default=60, description="Time in minutes that client web browsers should keep a cookie. Default is 60 minutes. 0 = no time limit.")    
    http_cookie_share: Literal["disable", "same-ip"] | None = Field(default="same-ip", description="Control sharing of cookies across API Gateway. Use of same-ip means a cookie from one virtual server can be used by another. Disable stops cookie sharing.")    
    https_cookie_secure: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable verification that inserted HTTPS cookies are secure.")    
    ssl_dh_bits: SslDhBitsEnum | None = Field(default="2048", description="Number of bits to use in the Diffie-Hellman exchange for RSA encryption of SSL sessions.")    
    ssl_algorithm: Literal["high", "medium", "low"] | None = Field(default="high", description="Permitted encryption algorithms for the server side of SSL full mode sessions according to encryption strength.")    
    ssl_cipher_suites: list[SslCipherSuites] = Field(default=None, description="SSL/TLS cipher suites to offer to a server, ordered by priority.")    
    ssl_min_version: SslMinVersionEnum | None = Field(default="tls-1.1", description="Lowest SSL/TLS version acceptable from a server.")    
    ssl_max_version: SslMaxVersionEnum | None = Field(default="tls-1.3", description="Highest SSL/TLS version acceptable from a server.")    
    ssl_renegotiation: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable secure renegotiation to comply with RFC 5746.")
class WebProxyApiGateway6(BaseModel):
    """
    Child table model for api-gateway6.
    
    Set IPv6 API Gateway.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="API Gateway ID.")    
    url_map: str = Field(max_length=511, default="/", description="URL pattern to match.")    
    service: Literal["http", "https"] = Field(default="https", description="Service.")    
    ldb_method: LdbMethodEnum | None = Field(default="static", description="Method used to distribute sessions to real servers.")    
    url_map_type: Literal["sub-string", "wildcard", "regex"] = Field(default="sub-string", description="Type of url-map.")    
    h2_support: Literal["enable", "disable"] = Field(default="enable", description="HTTP2 support, default=Enable.")    
    h3_support: Literal["enable", "disable"] | None = Field(default="disable", description="HTTP3/QUIC support, default=Disable.")    
    quic: list[Quic] = Field(default=None, description="QUIC setting.")    
    realservers: list[Realservers] = Field(default=None, description="Select the real servers that this Access Proxy will distribute traffic to.")    
    persistence: Literal["none", "http-cookie"] | None = Field(default="none", description="Configure how to make sure that clients connect to the same server every time they make a request that is part of the same session.")    
    http_cookie_domain_from_host: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable use of HTTP cookie domain from host field in HTTP.")    
    http_cookie_domain: str | None = Field(max_length=35, default="", description="Domain that HTTP cookie persistence should apply to.")    
    http_cookie_path: str | None = Field(max_length=35, default="", description="Limit HTTP cookie persistence to the specified path.")    
    http_cookie_generation: int | None = Field(ge=0, le=4294967295, default=0, description="Generation of HTTP cookie to be accepted. Changing invalidates all existing cookies.")    
    http_cookie_age: int | None = Field(ge=0, le=525600, default=60, description="Time in minutes that client web browsers should keep a cookie. Default is 60 minutes. 0 = no time limit.")    
    http_cookie_share: Literal["disable", "same-ip"] | None = Field(default="same-ip", description="Control sharing of cookies across API Gateway. Use of same-ip means a cookie from one virtual server can be used by another. Disable stops cookie sharing.")    
    https_cookie_secure: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable verification that inserted HTTPS cookies are secure.")    
    ssl_dh_bits: SslDhBitsEnum | None = Field(default="2048", description="Number of bits to use in the Diffie-Hellman exchange for RSA encryption of SSL sessions.")    
    ssl_algorithm: Literal["high", "medium", "low"] | None = Field(default="high", description="Permitted encryption algorithms for the server side of SSL full mode sessions according to encryption strength.")    
    ssl_cipher_suites: list[SslCipherSuites] = Field(default=None, description="SSL/TLS cipher suites to offer to a server, ordered by priority.")    
    ssl_min_version: SslMinVersionEnum | None = Field(default="tls-1.1", description="Lowest SSL/TLS version acceptable from a server.")    
    ssl_max_version: SslMaxVersionEnum | None = Field(default="tls-1.3", description="Highest SSL/TLS version acceptable from a server.")    
    ssl_renegotiation: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable secure renegotiation to comply with RFC 5746.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class WebProxyModel(BaseModel):
    """
    Pydantic model for ztna/web_proxy configuration.
    
    Configure ZTNA web-proxy.
    
    Validation Rules:        - name: max_length=79 pattern=        - vip: max_length=79 pattern=        - host: max_length=79 pattern=        - decrypted_traffic_mirror: max_length=35 pattern=        - log_blocked_traffic: pattern=        - auth_portal: pattern=        - auth_virtual_host: max_length=79 pattern=        - vip6: max_length=79 pattern=        - svr_pool_multiplex: pattern=        - svr_pool_ttl: min=0 max=2147483647 pattern=        - svr_pool_server_max_request: min=0 max=2147483647 pattern=        - svr_pool_server_max_concurrent_request: min=0 max=2147483647 pattern=        - api_gateway: pattern=        - api_gateway6: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=79, default="", description="ZTNA proxy name.")    
    vip: str | None = Field(max_length=79, default="", description="Virtual IP name.")  # datasource: ['firewall.vip.name']    
    host: str | None = Field(max_length=79, default="", description="Virtual or real host name.")  # datasource: ['firewall.access-proxy-virtual-host.name']    
    decrypted_traffic_mirror: str | None = Field(max_length=35, default="", description="Decrypted traffic mirror.")  # datasource: ['firewall.decrypted-traffic-mirror.name']    
    log_blocked_traffic: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable logging of blocked traffic.")    
    auth_portal: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable authentication portal.")    
    auth_virtual_host: str | None = Field(max_length=79, default="", description="Virtual host for authentication portal.")  # datasource: ['firewall.access-proxy-virtual-host.name']    
    vip6: str | None = Field(max_length=79, default="", description="Virtual IPv6 name.")  # datasource: ['firewall.vip6.name']    
    svr_pool_multiplex: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable server pool multiplexing (default = disable). Share connected server in HTTP and HTTPS api-gateways.")    
    svr_pool_ttl: int | None = Field(ge=0, le=2147483647, default=15, description="Time-to-live in the server pool for idle connections to servers.")    
    svr_pool_server_max_request: int | None = Field(ge=0, le=2147483647, default=0, description="Maximum number of requests that servers in the server pool handle before disconnecting (default = unlimited).")    
    svr_pool_server_max_concurrent_request: int | None = Field(ge=0, le=2147483647, default=0, description="Maximum number of concurrent requests that servers in the server pool could handle (default = unlimited).")    
    api_gateway: list[ApiGateway] = Field(default=None, description="Set IPv4 API Gateway.")    
    api_gateway6: list[ApiGateway6] = Field(default=None, description="Set IPv6 API Gateway.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('vip')
    @classmethod
    def validate_vip(cls, v: Any) -> Any:
        """
        Validate vip field.
        
        Datasource: ['firewall.vip.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('host')
    @classmethod
    def validate_host(cls, v: Any) -> Any:
        """
        Validate host field.
        
        Datasource: ['firewall.access-proxy-virtual-host.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('decrypted_traffic_mirror')
    @classmethod
    def validate_decrypted_traffic_mirror(cls, v: Any) -> Any:
        """
        Validate decrypted_traffic_mirror field.
        
        Datasource: ['firewall.decrypted-traffic-mirror.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('auth_virtual_host')
    @classmethod
    def validate_auth_virtual_host(cls, v: Any) -> Any:
        """
        Validate auth_virtual_host field.
        
        Datasource: ['firewall.access-proxy-virtual-host.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('vip6')
    @classmethod
    def validate_vip6(cls, v: Any) -> Any:
        """
        Validate vip6 field.
        
        Datasource: ['firewall.vip6.name']
        
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
    "WebProxyModel",    "WebProxyApiGateway",    "WebProxyApiGateway6",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:34.402768Z
# ============================================================================