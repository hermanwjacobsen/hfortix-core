"""
Pydantic Models for CMDB - extension_controller/extender_profile

Runtime validation models for extension_controller/extender_profile configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.extension_controller.extender_profile import 
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

class ExtenderProfileCellular(BaseModel):
    """
    Child table model for cellular.
    
    FortiExtender cellular configuration.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    dataplan: list[Dataplan] = Field(default=None, description="Dataplan names.")    
    controller_report: list[ControllerReport] = Field(default=None, description="FortiExtender controller report configuration.")    
    sms_notification: list[SmsNotification] = Field(default=None, description="FortiExtender cellular SMS notification configuration.")    
    modem1: list[Modem1] = Field(default=None, description="Configuration options for modem 1.")    
    modem2: list[Modem2] = Field(default=None, description="Configuration options for modem 2.")
class ExtenderProfileWifi(BaseModel):
    """
    Child table model for wifi.
    
    FortiExtender Wi-Fi configuration.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    country: CountryEnum | None = Field(default="--", description="Country in which this FEX will operate (default = NA).")    
    radio_1: list[Radio1] = Field(default=None, description="Radio-1 config for Wi-Fi 2.4GHz")    
    radio_2: list[Radio2] = Field(default=None, description="Radio-2 config for Wi-Fi 5GHz")
class ExtenderProfileLanExtension(BaseModel):
    """
    Child table model for lan-extension.
    
    FortiExtender LAN extension configuration.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    link_loadbalance: Literal["activebackup", "loadbalance"] = Field(default="activebackup", description="LAN extension link load balance strategy.")    
    ipsec_tunnel: str | None = Field(max_length=15, default="", description="IPsec tunnel name.")    
    backhaul_interface: str | None = Field(max_length=15, default="", description="IPsec phase1 interface.")  # datasource: ['system.interface.name']    
    backhaul_ip: str | None = Field(max_length=63, default="", description="IPsec phase1 IPv4/FQDN. Used to specify the external IP/FQDN when the FortiGate unit is behind a NAT device.")    
    backhaul: list[Backhaul] = Field(default=None, description="LAN extension backhaul tunnel configuration.")    
    downlinks: list[Downlinks] = Field(default=None, description="Config FortiExtender downlink interface for LAN extension.")    
    traffic_split_services: list[TrafficSplitServices] = Field(default=None, description="Config FortiExtender traffic split interface for LAN extension.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class ExtenderProfileModelEnum(str, Enum):
    """Allowed values for model field."""
    FX201E = "FX201E"    FX211E = "FX211E"    FX200F = "FX200F"    FXA11F = "FXA11F"    FXE11F = "FXE11F"    FXA21F = "FXA21F"    FXE21F = "FXE21F"    FXA22F = "FXA22F"    FXE22F = "FXE22F"    FX212F = "FX212F"    FX311F = "FX311F"    FX312F = "FX312F"    FX511F = "FX511F"    FXR51G = "FXR51G"    FXN51G = "FXN51G"    FXW51G = "FXW51G"    FVG21F = "FVG21F"    FVA21F = "FVA21F"    FVG22F = "FVG22F"    FVA22F = "FVA22F"    FX04DA = "FX04DA"    FG = "FG"    BS10FW = "BS10FW"    BS20GW = "BS20GW"    BS20GN = "BS20GN"    FVG51G = "FVG51G"    FXE11G = "FXE11G"    FX211G = "FX211G"
class ExtenderProfileAllowaccessEnum(str, Enum):
    """Allowed values for allowaccess field."""
    PING = "ping"    TELNET = "telnet"    HTTP = "http"    HTTPS = "https"    SSH = "ssh"    SNMP = "snmp"

# ============================================================================
# Main Model
# ============================================================================

class ExtenderProfileModel(BaseModel):
    """
    Pydantic model for extension_controller/extender_profile configuration.
    
    FortiExtender extender profile configuration.
    
    Validation Rules:        - name: max_length=31 pattern=        - id: min=0 max=102400000 pattern=        - model: pattern=        - extension: pattern=        - allowaccess: pattern=        - login_password_change: pattern=        - login_password: max_length=27 pattern=        - enforce_bandwidth: pattern=        - bandwidth_limit: min=1 max=16776000 pattern=        - cellular: pattern=        - wifi: pattern=        - lan_extension: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=31, default="", description="FortiExtender profile name.")    
    id: int | None = Field(ge=0, le=102400000, default=32, description="ID.")    
    model: ModelEnum = Field(default="FX201E", description="Model.")    
    extension: Literal["wan-extension", "lan-extension"] = Field(default="wan-extension", description="Extension option.")    
    allowaccess: list[Allowaccess] = Field(default="", description="Control management access to the managed extender. Separate entries with a space.")    
    login_password_change: Literal["yes", "default", "no"] | None = Field(default="no", description="Change or reset the administrator password of a managed extender (yes, default, or no, default = no).")    
    login_password: Any = Field(max_length=27, description="Set the managed extender's administrator password.")    
    enforce_bandwidth: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable enforcement of bandwidth on LAN extension interface.")    
    bandwidth_limit: int = Field(ge=1, le=16776000, default=1024, description="FortiExtender LAN extension bandwidth limit (Mbps).")    
    cellular: list[Cellular] = Field(description="FortiExtender cellular configuration.")    
    wifi: list[Wifi] = Field(default=None, description="FortiExtender Wi-Fi configuration.")    
    lan_extension: list[LanExtension] = Field(description="FortiExtender LAN extension configuration.")    
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
    "ExtenderProfileModel",    "ExtenderProfileCellular",    "ExtenderProfileWifi",    "ExtenderProfileLanExtension",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:33.722262Z
# ============================================================================