"""
Pydantic Models for CMDB - system/ntp

Runtime validation models for system/ntp configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.system.ntp import 
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

class NtpNtpserver(BaseModel):
    """
    Child table model for ntpserver.
    
    Configure the FortiGate to connect to any available third-party NTP server.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=0, le=4294967295, default=0, description="NTP server ID.")    
    server: str = Field(max_length=63, default="", description="IP address or hostname of the NTP Server.")    
    ntpv3: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to use NTPv3 instead of NTPv4.")    
    authentication: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable authentication.")    
    key_type: Literal["MD5", "SHA1", "SHA256"] | None = Field(default="MD5", description="Select NTP authentication type.")    
    key: Any = Field(max_length=64, description="Key for MD5(NTPv3)/SHA1(NTPv4)/SHA256(NTPv4) authentication.")    
    key_id: int = Field(ge=0, le=4294967295, default=0, description="Key ID for authentication.")    
    ip_type: Literal["IPv6", "IPv4", "Both"] | None = Field(default="Both", description="Choose to connect to IPv4 or/and IPv6 NTP server.")    
    interface_select_method: Literal["auto", "sdwan", "specify"] | None = Field(default="auto", description="Specify how to select outgoing interface to reach server.")    
    interface: str = Field(max_length=15, default="", description="Specify outgoing interface to reach server.")  # datasource: ['system.interface.name']    
    vrf_select: int | None = Field(ge=0, le=511, default=0, description="VRF ID used for connection to server.")
class NtpInterface(BaseModel):
    """
    Child table model for interface.
    
    FortiGate interface(s) with NTP server mode enabled. Devices on your network can contact these interfaces for NTP services.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    interface_name: str = Field(max_length=79, default="", description="Interface name.")  # datasource: ['system.interface.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class NtpModel(BaseModel):
    """
    Pydantic model for system/ntp configuration.
    
    Configure system NTP information.
    
    Validation Rules:        - ntpsync: pattern=        - type: pattern=        - syncinterval: min=1 max=1440 pattern=        - ntpserver: pattern=        - source_ip: pattern=        - source_ip6: pattern=        - server_mode: pattern=        - authentication: pattern=        - key_type: pattern=        - key: max_length=64 pattern=        - key_id: min=0 max=4294967295 pattern=        - interface: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    ntpsync: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable setting the FortiGate system time by synchronizing with an NTP Server.")    
    type: Literal["fortiguard", "custom"] | None = Field(default="fortiguard", description="Use the FortiGuard NTP server or any other available NTP Server.")    
    syncinterval: int | None = Field(ge=1, le=1440, default=60, description="NTP synchronization interval (1 - 1440 min).")    
    ntpserver: list[Ntpserver] = Field(default=None, description="Configure the FortiGate to connect to any available third-party NTP server.")    
    source_ip: str | None = Field(default="0.0.0.0", description="Source IP address for communication to the NTP server.")    
    source_ip6: str | None = Field(default="::", description="Source IPv6 address for communication to the NTP server.")    
    server_mode: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable FortiGate NTP Server Mode. Your FortiGate becomes an NTP server for other devices on your network. The FortiGate relays NTP requests to its configured NTP server.")    
    authentication: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable authentication.")    
    key_type: Literal["MD5", "SHA1", "SHA256"] | None = Field(default="MD5", description="Key type for authentication (MD5, SHA1, SHA256).")    
    key: Any = Field(max_length=64, description="Key for authentication.")    
    key_id: int = Field(ge=0, le=4294967295, default=0, description="Key ID for authentication.")    
    interface: list[Interface] = Field(default=None, description="FortiGate interface(s) with NTP server mode enabled. Devices on your network can contact these interfaces for NTP services.")    
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
    "NtpModel",    "NtpNtpserver",    "NtpInterface",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:35.036932Z
# ============================================================================