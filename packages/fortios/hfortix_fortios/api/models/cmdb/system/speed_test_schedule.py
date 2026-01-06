"""
Pydantic Models for CMDB - system/speed_test_schedule

Runtime validation models for system/speed_test_schedule configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.system.speed_test_schedule import 
    >>>
    >>> # Create with validation
    >>> obj = (
    ...     interface=1,
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

class SpeedTestScheduleSchedules(BaseModel):
    """
    Child table model for schedules.
    
    Schedules for the interface.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=31, default="", description="Name of a firewall recurring schedule.")  # datasource: ['firewall.schedule.recurring.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class SpeedTestScheduleUpdate_shaperEnum(str, Enum):
    """Allowed values for update_shaper field."""
    DISABLE = "disable"    LOCAL = "local"    REMOTE = "remote"    BOTH = "both"

# ============================================================================
# Main Model
# ============================================================================

class SpeedTestScheduleModel(BaseModel):
    """
    Pydantic model for system/speed_test_schedule configuration.
    
    Speed test schedule for each interface.
    
    Validation Rules:        - interface: max_length=35 pattern=        - status: pattern=        - diffserv: pattern=        - server_name: max_length=35 pattern=        - mode: pattern=        - schedules: pattern=        - dynamic_server: pattern=        - ctrl_port: min=1 max=65535 pattern=        - server_port: min=1 max=65535 pattern=        - update_shaper: pattern=        - update_inbandwidth: pattern=        - update_outbandwidth: pattern=        - update_interface_shaping: pattern=        - update_inbandwidth_maximum: min=0 max=16776000 pattern=        - update_inbandwidth_minimum: min=0 max=16776000 pattern=        - update_outbandwidth_maximum: min=0 max=16776000 pattern=        - update_outbandwidth_minimum: min=0 max=16776000 pattern=        - expected_inbandwidth_minimum: min=0 max=16776000 pattern=        - expected_inbandwidth_maximum: min=0 max=16776000 pattern=        - expected_outbandwidth_minimum: min=0 max=16776000 pattern=        - expected_outbandwidth_maximum: min=0 max=16776000 pattern=        - retries: min=1 max=10 pattern=        - retry_pause: min=60 max=3600 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    interface: str | None = Field(max_length=35, default="", description="Interface name.")  # datasource: ['system.interface.name']    
    status: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable scheduled speed test.")    
    diffserv: str | None = Field(default="", description="DSCP used for speed test.")    
    server_name: str | None = Field(max_length=35, default="", description="Speed test server name in system.speed-test-server list or leave it as empty to choose default server \"FTNT_Auto\".")  # datasource: ['system.speed-test-server.name']    
    mode: Literal["UDP", "TCP", "Auto"] | None = Field(default="Auto", description="Protocol Auto(default), TCP or UDP used for speed test.")    
    schedules: list[Schedules] = Field(description="Schedules for the interface.")    
    dynamic_server: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable dynamic server option.")    
    ctrl_port: int | None = Field(ge=1, le=65535, default=5200, description="Port of the controller to get access token.")    
    server_port: int | None = Field(ge=1, le=65535, default=5201, description="Port of the server to run speed test.")    
    update_shaper: UpdateShaperEnum | None = Field(default="disable", description="Set egress shaper based on the test result.")    
    update_inbandwidth: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable bypassing interface's inbound bandwidth setting.")    
    update_outbandwidth: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable bypassing interface's outbound bandwidth setting.")    
    update_interface_shaping: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable using the speedtest results as reference for interface shaping (overriding configured in/outbandwidth).")    
    update_inbandwidth_maximum: int | None = Field(ge=0, le=16776000, default=0, description="Maximum downloading bandwidth (kbps) to be used in a speed test.")    
    update_inbandwidth_minimum: int | None = Field(ge=0, le=16776000, default=0, description="Minimum downloading bandwidth (kbps) to be considered effective.")    
    update_outbandwidth_maximum: int | None = Field(ge=0, le=16776000, default=0, description="Maximum uploading bandwidth (kbps) to be used in a speed test.")    
    update_outbandwidth_minimum: int | None = Field(ge=0, le=16776000, default=0, description="Minimum uploading bandwidth (kbps) to be considered effective.")    
    expected_inbandwidth_minimum: int | None = Field(ge=0, le=16776000, default=0, description="Set the minimum inbandwidth threshold for applying speedtest results on shaping-profile.")    
    expected_inbandwidth_maximum: int | None = Field(ge=0, le=16776000, default=0, description="Set the maximum inbandwidth threshold for applying speedtest results on shaping-profile.")    
    expected_outbandwidth_minimum: int | None = Field(ge=0, le=16776000, default=0, description="Set the minimum outbandwidth threshold for applying speedtest results on shaping-profile.")    
    expected_outbandwidth_maximum: int | None = Field(ge=0, le=16776000, default=0, description="Set the maximum outbandwidth threshold for applying speedtest results on shaping-profile.")    
    retries: int | None = Field(ge=1, le=10, default=5, description="Maximum number of times the FortiGate unit will attempt to contact the same server before considering the speed test has failed (1 - 10, default = 5).")    
    retry_pause: int | None = Field(ge=60, le=3600, default=300, description="Number of seconds the FortiGate pauses between successive speed tests before trying a different server (60 - 3600, default = 300).")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
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
    @field_validator('server_name')
    @classmethod
    def validate_server_name(cls, v: Any) -> Any:
        """
        Validate server_name field.
        
        Datasource: ['system.speed-test-server.name']
        
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
    "SpeedTestScheduleModel",    "SpeedTestScheduleSchedules",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:33.071890Z
# ============================================================================