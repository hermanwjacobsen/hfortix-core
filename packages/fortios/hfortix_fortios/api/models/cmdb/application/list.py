"""
Pydantic Models for CMDB - application/list

Runtime validation models for application/list configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.application.list import 
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

class ListEntries(BaseModel):
    """
    Child table model for entries.
    
    Application list entries.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="Entry ID.")    
    risk: list[Risk] = Field(default=None, description="Risk, or impact, of allowing traffic from this application to occur (1 - 5; Low, Elevated, Medium, High, and Critical).")    
    category: list[Category] = Field(default=None, description="Category ID list.")    
    application: list[Application] = Field(default=None, description="ID of allowed applications.")    
    protocols: list[Protocols] = Field(default="all", description="Application protocol filter.")    
    vendor: list[Vendor] = Field(default="all", description="Application vendor filter.")    
    technology: list[Technology] = Field(default="all", description="Application technology filter.")    
    behavior: list[Behavior] = Field(default="all", description="Application behavior filter.")    
    popularity: list[Popularity] = Field(default="1 2 3 4 5", description="Application popularity filter (1 - 5, from least to most popular).")    
    exclusion: list[Exclusion] = Field(default=None, description="ID of excluded applications.")    
    parameters: list[Parameters] = Field(default=None, description="Application parameters.")    
    action: Literal["pass", "block", "reset"] | None = Field(default="block", description="Pass or block traffic, or reset connection for traffic from this application.")    
    log: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable logging for this application list.")    
    log_packet: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable packet logging.")    
    rate_count: int | None = Field(ge=0, le=65535, default=0, description="Count of the rate.")    
    rate_duration: int | None = Field(ge=1, le=65535, default=60, description="Duration (sec) of the rate.")    
    rate_mode: Literal["periodical", "continuous"] | None = Field(default="continuous", description="Rate limit mode.")    
    rate_track: RateTrackEnum | None = Field(default="none", description="Track the packet protocol field.")    
    session_ttl: int | None = Field(ge=0, le=4294967295, default=0, description="Session TTL (0 = default).")    
    shaper: str | None = Field(max_length=35, default="", description="Traffic shaper.")  # datasource: ['firewall.shaper.traffic-shaper.name']    
    shaper_reverse: str | None = Field(max_length=35, default="", description="Reverse traffic shaper.")  # datasource: ['firewall.shaper.traffic-shaper.name']    
    per_ip_shaper: str | None = Field(max_length=35, default="", description="Per-IP traffic shaper.")  # datasource: ['firewall.shaper.per-ip-shaper.name']    
    quarantine: Literal["none", "attacker"] | None = Field(default="none", description="Quarantine method.")    
    quarantine_expiry: str | None = Field(default="5m", description="Duration of quarantine. (Format ###d##h##m, minimum 1m, maximum 364d23h59m, default = 5m). Requires quarantine set to attacker.")    
    quarantine_log: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable quarantine logging.")
class ListDefaultNetworkServices(BaseModel):
    """
    Child table model for default-network-services.
    
    Default network service entries.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=0, le=4294967295, default=0, description="Entry ID.")    
    port: int = Field(ge=0, le=65535, default=0, description="Port number.")    
    services: list[Services] = Field(default="", description="Network protocols.")    
    violation_action: Literal["pass", "monitor", "block"] | None = Field(default="block", description="Action for protocols not in the allowlist for selected port.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class ListOptionsEnum(str, Enum):
    """Allowed values for options field."""
    ALLOW_DNS = "allow-dns"    ALLOW_ICMP = "allow-icmp"    ALLOW_HTTP = "allow-http"    ALLOW_SSL = "allow-ssl"

# ============================================================================
# Main Model
# ============================================================================

class ListModel(BaseModel):
    """
    Pydantic model for application/list configuration.
    
    Configure application control lists.
    
    Validation Rules:        - name: max_length=47 pattern=        - comment: max_length=255 pattern=        - replacemsg_group: max_length=35 pattern=        - extended_log: pattern=        - other_application_action: pattern=        - app_replacemsg: pattern=        - other_application_log: pattern=        - enforce_default_app_port: pattern=        - force_inclusion_ssl_di_sigs: pattern=        - unknown_application_action: pattern=        - unknown_application_log: pattern=        - p2p_block_list: pattern=        - deep_app_inspection: pattern=        - options: pattern=        - entries: pattern=        - control_default_network_services: pattern=        - default_network_services: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str = Field(max_length=47, default="", description="List name.")    
    comment: str | None = Field(max_length=255, default=None, description="Comments.")    
    replacemsg_group: str | None = Field(max_length=35, default="", description="Replacement message group.")  # datasource: ['system.replacemsg-group.name']    
    extended_log: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable extended logging.")    
    other_application_action: Literal["pass", "block"] | None = Field(default="pass", description="Action for other applications.")    
    app_replacemsg: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable replacement messages for blocked applications.")    
    other_application_log: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable logging for other applications.")    
    enforce_default_app_port: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable default application port enforcement for allowed applications.")    
    force_inclusion_ssl_di_sigs: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable forced inclusion of SSL deep inspection signatures.")    
    unknown_application_action: Literal["pass", "block"] | None = Field(default="pass", description="Pass or block traffic from unknown applications.")    
    unknown_application_log: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable logging for unknown applications.")    
    p2p_block_list: list[P2PBlockList] = Field(default="", description="P2P applications to be block listed.")    
    deep_app_inspection: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable deep application inspection.")    
    options: list[Options] = Field(default="allow-dns", description="Basic application protocol signatures allowed by default.")    
    entries: list[Entries] = Field(default=None, description="Application list entries.")    
    control_default_network_services: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable enforcement of protocols over selected ports.")    
    default_network_services: list[DefaultNetworkServices] = Field(default=None, description="Default network service entries.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('replacemsg_group')
    @classmethod
    def validate_replacemsg_group(cls, v: Any) -> Any:
        """
        Validate replacemsg_group field.
        
        Datasource: ['system.replacemsg-group.name']
        
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
    "ListModel",    "ListEntries",    "ListDefaultNetworkServices",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:35.254170Z
# ============================================================================