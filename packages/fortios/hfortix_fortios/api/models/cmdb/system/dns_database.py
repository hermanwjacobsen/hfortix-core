"""
Pydantic Models for CMDB - system/dns_database

Runtime validation models for system/dns_database configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.system.dns_database import 
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

class DnsDatabaseDnsEntry(BaseModel):
    """
    Child table model for dns-entry.
    
    DNS entry.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=0, le=4294967295, default=0, description="DNS entry ID.")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable resource record status.")    
    type: TypeEnum = Field(default="A", description="Resource record type.")    
    ttl: int | None = Field(ge=0, le=2147483647, default=0, description="Time-to-live for this entry (0 to 2147483647 sec, default = 0).")    
    preference: int | None = Field(ge=0, le=65535, default=10, description="DNS entry preference (0 - 65535, highest preference = 0, default = 10).")    
    ip: str | None = Field(default="0.0.0.0", description="IPv4 address of the host.")    
    ipv6: str | None = Field(default="::", description="IPv6 address of the host.")    
    hostname: str = Field(max_length=255, default="", description="Name of the host.")    
    canonical_name: str | None = Field(max_length=255, default="", description="Canonical name of the host.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class DnsDatabaseViewEnum(str, Enum):
    """Allowed values for view field."""
    SHADOW = "shadow"    PUBLIC = "public"    SHADOW_ZTNA = "shadow-ztna"    PROXY = "proxy"

# ============================================================================
# Main Model
# ============================================================================

class DnsDatabaseModel(BaseModel):
    """
    Pydantic model for system/dns_database configuration.
    
    Configure DNS databases.
    
    Validation Rules:        - name: max_length=35 pattern=        - status: pattern=        - domain: max_length=255 pattern=        - allow_transfer: pattern=        - type: pattern=        - view: pattern=        - ip_primary: pattern=        - primary_name: max_length=255 pattern=        - contact: max_length=255 pattern=        - ttl: min=0 max=2147483647 pattern=        - authoritative: pattern=        - forwarder: pattern=        - forwarder6: pattern=        - source_ip: pattern=        - source_ip6: pattern=        - source_ip_interface: max_length=15 pattern=        - rr_max: min=10 max=65536 pattern=        - dns_entry: pattern=        - interface_select_method: pattern=        - interface: max_length=15 pattern=        - vrf_select: min=0 max=511 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str = Field(max_length=35, default="", description="Zone name.")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable this DNS zone.")    
    domain: str = Field(max_length=255, default="", description="Domain name.")    
    allow_transfer: list[AllowTransfer] = Field(default="", description="DNS zone transfer IP address list.")    
    type: Literal["primary", "secondary"] = Field(default="primary", description="Zone type (primary to manage entries directly, secondary to import entries from other zones).")    
    view: ViewEnum = Field(default="shadow", description="Zone view (public to serve public clients, shadow to serve internal clients).")    
    ip_primary: str | None = Field(default="0.0.0.0", description="IP address of primary DNS server. Entries in this primary DNS server and imported into the DNS zone.")    
    primary_name: str | None = Field(max_length=255, default="dns", description="Domain name of the default DNS server for this zone.")    
    contact: str | None = Field(max_length=255, default="host", description="Email address of the administrator for this zone. You can specify only the username, such as admin or the full email address, such as admin@test.com When using only a username, the domain of the email will be this zone.")    
    ttl: int = Field(ge=0, le=2147483647, default=86400, description="Default time-to-live value for the entries of this DNS zone (0 - 2147483647 sec, default = 86400).")    
    authoritative: Literal["enable", "disable"] = Field(default="enable", description="Enable/disable authoritative zone.")    
    forwarder: list[Forwarder] = Field(default="", description="DNS zone forwarder IP address list.")    
    forwarder6: str | None = Field(default="::", description="Forwarder IPv6 address.")    
    source_ip: str | None = Field(default="0.0.0.0", description="Source IP for forwarding to DNS server.")    
    source_ip6: str | None = Field(default="::", description="IPv6 source IP address for forwarding to DNS server.")    
    source_ip_interface: str | None = Field(max_length=15, default="", description="IP address of the specified interface as the source IP address.")  # datasource: ['system.interface.name']    
    rr_max: int | None = Field(ge=10, le=65536, default=16384, description="Maximum number of resource records (10 - 65536, 0 means infinite).")    
    dns_entry: list[DnsEntry] = Field(description="DNS entry.")    
    interface_select_method: Literal["auto", "sdwan", "specify"] | None = Field(default="auto", description="Specify how to select outgoing interface to reach server.")    
    interface: str = Field(max_length=15, default="", description="Specify outgoing interface to reach server.")  # datasource: ['system.interface.name']    
    vrf_select: int | None = Field(ge=0, le=511, default=0, description="VRF ID used for connection to server.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('source_ip_interface')
    @classmethod
    def validate_source_ip_interface(cls, v: Any) -> Any:
        """
        Validate source_ip_interface field.
        
        Datasource: ['system.interface.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('interface')
    @classmethod
    def validate_interface(cls, v: Any) -> Any:
        """
        Validate interface field.
        
        Datasource: ['system.interface.name']
        
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
    "DnsDatabaseModel",    "DnsDatabaseDnsEntry",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:35.481152Z
# ============================================================================