"""
Pydantic Models for CMDB - extension_controller/extender

Runtime validation models for extension_controller/extender configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.extension_controller.extender import 
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

class ExtenderWanExtension(BaseModel):
    """
    Child table model for wan-extension.
    
    FortiExtender wan extension configuration.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    modem1_extension: str | None = Field(max_length=31, default="", description="FortiExtender interface name.")  # datasource: ['system.interface.name']    
    modem2_extension: str | None = Field(max_length=31, default="", description="FortiExtender interface name.")  # datasource: ['system.interface.name']    
    modem1_pdn1_interface: str | None = Field(max_length=31, default="", description="FortiExtender interface name.")  # datasource: ['system.interface.name']    
    modem1_pdn2_interface: str | None = Field(max_length=31, default="", description="FortiExtender interface name.")  # datasource: ['system.interface.name']    
    modem1_pdn3_interface: str | None = Field(max_length=31, default="", description="FortiExtender interface name.")  # datasource: ['system.interface.name']    
    modem1_pdn4_interface: str | None = Field(max_length=31, default="", description="FortiExtender interface name.")  # datasource: ['system.interface.name']    
    modem2_pdn1_interface: str | None = Field(max_length=31, default="", description="FortiExtender interface name.")  # datasource: ['system.interface.name']    
    modem2_pdn2_interface: str | None = Field(max_length=31, default="", description="FortiExtender interface name.")  # datasource: ['system.interface.name']    
    modem2_pdn3_interface: str | None = Field(max_length=31, default="", description="FortiExtender interface name.")  # datasource: ['system.interface.name']    
    modem2_pdn4_interface: str | None = Field(max_length=31, default="", description="FortiExtender interface name.")  # datasource: ['system.interface.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class ExtenderAllowaccessEnum(str, Enum):
    """Allowed values for allowaccess field."""
    PING = "ping"    TELNET = "telnet"    HTTP = "http"    HTTPS = "https"    SSH = "ssh"    SNMP = "snmp"

# ============================================================================
# Main Model
# ============================================================================

class ExtenderModel(BaseModel):
    """
    Pydantic model for extension_controller/extender configuration.
    
    Extender controller configuration.
    
    Validation Rules:        - name: max_length=19 pattern=        - id: max_length=19 pattern=        - authorized: pattern=        - ext_name: max_length=31 pattern=        - description: max_length=255 pattern=        - vdom: min=0 max=4294967295 pattern=        - device_id: min=0 max=4294967295 pattern=        - extension_type: pattern=        - profile: max_length=31 pattern=        - override_allowaccess: pattern=        - allowaccess: pattern=        - override_login_password_change: pattern=        - login_password_change: pattern=        - login_password: max_length=27 pattern=        - override_enforce_bandwidth: pattern=        - enforce_bandwidth: pattern=        - bandwidth_limit: min=1 max=16776000 pattern=        - wan_extension: pattern=        - firmware_provision_latest: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str = Field(max_length=19, default="", description="FortiExtender entry name.")    
    id: str = Field(max_length=19, default="", description="FortiExtender serial number.")    
    authorized: Literal["discovered", "disable", "enable"] = Field(default="discovered", description="FortiExtender Administration (enable or disable).")    
    ext_name: str | None = Field(max_length=31, default="", description="FortiExtender name.")    
    description: str | None = Field(max_length=255, default="", description="Description.")    
    vdom: int | None = Field(ge=0, le=4294967295, default=1, description="VDOM.")    
    device_id: int | None = Field(ge=0, le=4294967295, default=1026, description="Device ID.")    
    extension_type: Literal["wan-extension", "lan-extension"] = Field(default="", description="Extension type for this FortiExtender.")    
    profile: str | None = Field(max_length=31, default="", description="FortiExtender profile configuration.")  # datasource: ['extension-controller.extender-profile.name']    
    override_allowaccess: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to override the extender profile management access configuration.")    
    allowaccess: list[Allowaccess] = Field(default="", description="Control management access to the managed extender. Separate entries with a space.")    
    override_login_password_change: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to override the extender profile login-password (administrator password) setting.")    
    login_password_change: Literal["yes", "default", "no"] | None = Field(default="no", description="Change or reset the administrator password of a managed extender (yes, default, or no, default = no).")    
    login_password: Any = Field(max_length=27, description="Set the managed extender's administrator password.")    
    override_enforce_bandwidth: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to override the extender profile enforce-bandwidth setting.")    
    enforce_bandwidth: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable enforcement of bandwidth on LAN extension interface.")    
    bandwidth_limit: int = Field(ge=1, le=16776000, default=1024, description="FortiExtender LAN extension bandwidth limit (Mbps).")    
    wan_extension: list[WanExtension] = Field(default=None, description="FortiExtender wan extension configuration.")    
    firmware_provision_latest: Literal["disable", "once"] | None = Field(default="disable", description="Enable/disable one-time automatic provisioning of the latest firmware version.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('profile')
    @classmethod
    def validate_profile(cls, v: Any) -> Any:
        """
        Validate profile field.
        
        Datasource: ['extension-controller.extender-profile.name']
        
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
    "ExtenderModel",    "ExtenderWanExtension",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:34.648703Z
# ============================================================================