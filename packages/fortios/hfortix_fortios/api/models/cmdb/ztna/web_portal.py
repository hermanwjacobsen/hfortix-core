"""
Pydantic Models for CMDB - ztna/web_portal

Runtime validation models for ztna/web_portal configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.ztna.web_portal import 
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

class WebPortalThemeEnum(str, Enum):
    """Allowed values for theme field."""
    JADE = "jade"    NEUTRINO = "neutrino"    MARINER = "mariner"    GRAPHITE = "graphite"    MELONGENE = "melongene"    JET_STREAM = "jet-stream"    SECURITY_FABRIC = "security-fabric"    DARK_MATTER = "dark-matter"    ONYX = "onyx"    ECLIPSE = "eclipse"

# ============================================================================
# Main Model
# ============================================================================

class WebPortalModel(BaseModel):
    """
    Pydantic model for ztna/web_portal configuration.
    
    Configure ztna web-portal.
    
    Validation Rules:        - name: max_length=79 pattern=        - vip: max_length=79 pattern=        - host: max_length=79 pattern=        - decrypted_traffic_mirror: max_length=35 pattern=        - log_blocked_traffic: pattern=        - auth_portal: pattern=        - auth_virtual_host: max_length=79 pattern=        - vip6: max_length=79 pattern=        - auth_rule: max_length=35 pattern=        - display_bookmark: pattern=        - focus_bookmark: pattern=        - display_status: pattern=        - display_history: pattern=        - policy_auth_sso: pattern=        - heading: max_length=31 pattern=        - theme: pattern=        - clipboard: pattern=        - default_window_width: min=0 max=65535 pattern=        - default_window_height: min=0 max=65535 pattern=        - cookie_age: min=0 max=525600 pattern=        - forticlient_download: pattern=        - customize_forticlient_download_url: pattern=        - windows_forticlient_download_url: max_length=1023 pattern=        - macos_forticlient_download_url: max_length=1023 pattern=    """
    
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
    auth_rule: str | None = Field(max_length=35, default="", description="Authentication Rule.")  # datasource: ['authentication.rule.name']    
    display_bookmark: Literal["enable", "disable"] | None = Field(default="enable", description="Enable to display the web portal bookmark widget.")    
    focus_bookmark: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to prioritize the placement of the bookmark section over the quick-connection section in the ztna web-portal.")    
    display_status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable to display the web portal status widget.")    
    display_history: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to display the web portal user login history widget.")    
    policy_auth_sso: Literal["enable", "disable"] | None = Field(default="enable", description="Enable policy sso authentication.")    
    heading: str | None = Field(max_length=31, default="ZTNA Portal", description="Web portal heading message.")    
    theme: ThemeEnum | None = Field(default="security-fabric", description="Web portal color scheme.")    
    clipboard: Literal["enable", "disable"] | None = Field(default="enable", description="Enable to support RDP/VPC clipboard functionality.")    
    default_window_width: int | None = Field(ge=0, le=65535, default=1024, description="Screen width (range from 0 - 65535, default = 1024).")    
    default_window_height: int | None = Field(ge=0, le=65535, default=768, description="Screen height (range from 0 - 65535, default = 768).")    
    cookie_age: int | None = Field(ge=0, le=525600, default=60, description="Time in minutes that client web browsers should keep a cookie. Default is 60 minutes. 0 = no time limit.")    
    forticlient_download: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable download option for FortiClient.")    
    customize_forticlient_download_url: Literal["enable", "disable"] | None = Field(default="disable", description="Enable support of customized download URL for FortiClient.")    
    windows_forticlient_download_url: str | None = Field(max_length=1023, default=None, description="Download URL for Windows FortiClient.")    
    macos_forticlient_download_url: str | None = Field(max_length=1023, default=None, description="Download URL for Mac FortiClient.")    
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
    @field_validator('auth_rule')
    @classmethod
    def validate_auth_rule(cls, v: Any) -> Any:
        """
        Validate auth_rule field.
        
        Datasource: ['authentication.rule.name']
        
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
    "WebPortalModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:35.929592Z
# ============================================================================