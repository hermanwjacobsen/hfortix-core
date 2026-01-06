"""
Pydantic Models for CMDB - webfilter/urlfilter

Runtime validation models for webfilter/urlfilter configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.webfilter.urlfilter import 
    >>>
    >>> # Create with validation
    >>> obj = (
    ...     id=1,
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

class UrlfilterEntries(BaseModel):
    """
    Child table model for entries.
    
    URL filter entries.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=0, le=4294967295, default=0, description="Id.")    
    url: str | None = Field(max_length=511, default="", description="URL to be filtered.")    
    type: Literal["simple", "regex", "wildcard"] | None = Field(default="simple", description="Filter type (simple, regex, or wildcard).")    
    action: ActionEnum | None = Field(default="exempt", description="Action to take for URL filter matches.")    
    antiphish_action: Literal["block", "log"] | None = Field(default="block", description="Action to take for AntiPhishing matches.")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable this URL filter.")    
    exempt: list[Exempt] = Field(default="av web-content activex-java-cookie dlp fortiguard range-block antiphish all", description="If action is set to exempt, select the security profile operations that exempt URLs skip. Separate multiple options with a space.")    
    web_proxy_profile: str | None = Field(max_length=63, default="", description="Web proxy profile.")  # datasource: ['web-proxy.profile.name']    
    referrer_host: str | None = Field(max_length=255, default="", description="Referrer host name.")    
    dns_address_family: Literal["ipv4", "ipv6", "both"] | None = Field(default="ipv4", description="Resolve IPv4 address, IPv6 address, or both from DNS server.")    
    comment: str | None = Field(max_length=255, default=None, description="Comment.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class UrlfilterModel(BaseModel):
    """
    Pydantic model for webfilter/urlfilter configuration.
    
    Configure URL filter lists.
    
    Validation Rules:        - id: min=0 max=4294967295 pattern=        - name: max_length=63 pattern=        - comment: max_length=255 pattern=        - one_arm_ips_urlfilter: pattern=        - ip_addr_block: pattern=        - ip4_mapped_ip6: pattern=        - include_subdomains: pattern=        - entries: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    id: int = Field(ge=0, le=4294967295, default=0, description="ID.")    
    name: str = Field(max_length=63, default="", description="Name of URL filter list.")    
    comment: str | None = Field(max_length=255, default=None, description="Optional comments.")    
    one_arm_ips_urlfilter: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable DNS resolver for one-arm IPS URL filter operation.")    
    ip_addr_block: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable blocking URLs when the hostname appears as an IP address.")    
    ip4_mapped_ip6: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable matching of IPv4 mapped IPv6 URLs.")    
    include_subdomains: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable matching subdomains. Applies only to simple type (default = enable).")    
    entries: list[Entries] = Field(description="URL filter entries.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
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
    "UrlfilterModel",    "UrlfilterEntries",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:33.757120Z
# ============================================================================