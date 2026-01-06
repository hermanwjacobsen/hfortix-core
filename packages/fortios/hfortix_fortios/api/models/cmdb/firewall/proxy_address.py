"""
Pydantic Models for CMDB - firewall/proxy_address

Runtime validation models for firewall/proxy_address configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.firewall.proxy_address import 
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
from uuid import UUID

# ============================================================================
# Child Table Models
# ============================================================================

class ProxyAddressCategory(BaseModel):
    """
    Child table model for category.
    
    FortiGuard category ID.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="FortiGuard category ID.")
class ProxyAddressHeaderGroup(BaseModel):
    """
    Child table model for header-group.
    
    HTTP header group.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="ID.")    
    header_name: str = Field(max_length=79, default="", description="HTTP header.")    
    header: str = Field(max_length=255, default="", description="HTTP header regular expression.")    
    case_sensitivity: Literal["disable", "enable"] | None = Field(default="disable", description="Case sensitivity in pattern.")
class ProxyAddressTagging(BaseModel):
    """
    Child table model for tagging.
    
    Config object tagging.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=63, default="", description="Tagging entry name.")    
    category: str | None = Field(max_length=63, default="", description="Tag category.")  # datasource: ['system.object-tagging.category']    
    tags: list[Tags] = Field(default=None, description="Tags.")
class ProxyAddressApplication(BaseModel):
    """
    Child table model for application.
    
    SaaS application.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="SaaS application name.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class ProxyAddressTypeEnum(str, Enum):
    """Allowed values for type field."""
    HOST_REGEX = "host-regex"    URL = "url"    CATEGORY = "category"    METHOD = "method"    UA = "ua"    HEADER = "header"    SRC_ADVANCED = "src-advanced"    DST_ADVANCED = "dst-advanced"    SAAS = "saas"
class ProxyAddressMethodEnum(str, Enum):
    """Allowed values for method field."""
    GET = "get"    POST = "post"    PUT = "put"    HEAD = "head"    CONNECT = "connect"    TRACE = "trace"    OPTIONS = "options"    DELETE = "delete"    UPDATE = "update"    PATCH = "patch"    OTHER = "other"
class ProxyAddressUaEnum(str, Enum):
    """Allowed values for ua field."""
    CHROME = "chrome"    MS = "ms"    FIREFOX = "firefox"    SAFARI = "safari"    IE = "ie"    EDGE = "edge"    OTHER = "other"

# ============================================================================
# Main Model
# ============================================================================

class ProxyAddressModel(BaseModel):
    """
    Pydantic model for firewall/proxy_address configuration.
    
    Configure web proxy address.
    
    Validation Rules:        - name: max_length=79 pattern=        - uuid: pattern=        - type: pattern=        - host: max_length=79 pattern=        - host_regex: max_length=255 pattern=        - path: max_length=255 pattern=        - query: max_length=255 pattern=        - referrer: pattern=        - category: pattern=        - method: pattern=        - ua: pattern=        - ua_min_ver: max_length=63 pattern=        - ua_max_ver: max_length=63 pattern=        - header_name: max_length=79 pattern=        - header: max_length=255 pattern=        - case_sensitivity: pattern=        - header_group: pattern=        - color: min=0 max=32 pattern=        - tagging: pattern=        - comment: max_length=255 pattern=        - application: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=79, default="", description="Address name.")    
    uuid: str | None = Field(default="00000000-0000-0000-0000-000000000000", description="Universally Unique Identifier (UUID; automatically assigned but can be manually reset).")    
    type: TypeEnum | None = Field(default="url", description="Proxy address type.")    
    host: str = Field(max_length=79, default="", description="Address object for the host.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name', 'firewall.proxy-address.name', 'firewall.vipgrp.name', 'firewall.vip.name']    
    host_regex: str | None = Field(max_length=255, default="", description="Host name as a regular expression.")    
    path: str | None = Field(max_length=255, default="", description="URL path as a regular expression.")    
    query: str | None = Field(max_length=255, default="", description="Match the query part of the URL as a regular expression.")    
    referrer: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable use of referrer field in the HTTP header to match the address.")    
    category: list[Category] = Field(default=None, description="FortiGuard category ID.")    
    method: list[Method] = Field(default="", description="HTTP request methods to be used.")    
    ua: list[Ua] = Field(default="", description="Names of browsers to be used as user agent.")    
    ua_min_ver: str | None = Field(max_length=63, default="", description="Minimum version of the user agent specified in dotted notation. For example, use 90.0.1 with the ua field set to \"chrome\" to require Google Chrome's minimum version must be 90.0.1.")    
    ua_max_ver: str | None = Field(max_length=63, default="", description="Maximum version of the user agent specified in dotted notation. For example, use 120 with the ua field set to \"chrome\" to require Google Chrome's maximum version must be 120.")    
    header_name: str | None = Field(max_length=79, default="", description="Name of HTTP header.")    
    header: str | None = Field(max_length=255, default="", description="HTTP header name as a regular expression.")    
    case_sensitivity: Literal["disable", "enable"] | None = Field(default="disable", description="Enable to make the pattern case sensitive.")    
    header_group: list[HeaderGroup] = Field(default=None, description="HTTP header group.")    
    color: int | None = Field(ge=0, le=32, default=0, description="Integer value to determine the color of the icon in the GUI (1 - 32, default = 0, which sets value to 1).")    
    tagging: list[Tagging] = Field(default=None, description="Config object tagging.")    
    comment: str | None = Field(max_length=255, default=None, description="Optional comments.")    
    application: list[Application] = Field(description="SaaS application.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('host')
    @classmethod
    def validate_host(cls, v: Any) -> Any:
        """
        Validate host field.
        
        Datasource: ['firewall.address.name', 'firewall.addrgrp.name', 'firewall.proxy-address.name', 'firewall.vipgrp.name', 'firewall.vip.name']
        
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
    "ProxyAddressModel",    "ProxyAddressCategory",    "ProxyAddressHeaderGroup",    "ProxyAddressTagging",    "ProxyAddressApplication",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:32.659579Z
# ============================================================================