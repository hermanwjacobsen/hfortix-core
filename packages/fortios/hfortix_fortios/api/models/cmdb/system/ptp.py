"""
Pydantic Models for CMDB - system/ptp

Runtime validation models for system/ptp configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.system.ptp import 
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

class PtpServerInterface(BaseModel):
    """
    Child table model for server-interface.
    
    FortiGate interface(s) with PTP server mode enabled. Devices on your network can contact these interfaces for PTP services.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=0, le=4294967295, default=0, description="ID.")    
    server_interface_name: str = Field(max_length=15, default="", description="Interface name.")  # datasource: ['system.interface.name']    
    delay_mechanism: Literal["E2E", "P2P"] | None = Field(default="E2E", description="End to end delay detection or peer to peer delay detection.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class PtpModel(BaseModel):
    """
    Pydantic model for system/ptp configuration.
    
    Configure system PTP information.
    
    Validation Rules:        - status: pattern=        - mode: pattern=        - delay_mechanism: pattern=        - request_interval: min=1 max=6 pattern=        - interface: max_length=15 pattern=        - server_mode: pattern=        - server_interface: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable setting the FortiGate system time by synchronizing with an PTP Server.")    
    mode: Literal["multicast", "hybrid"] | None = Field(default="multicast", description="Multicast transmission or hybrid transmission.")    
    delay_mechanism: Literal["E2E", "P2P"] | None = Field(default="E2E", description="End to end delay detection or peer to peer delay detection.")    
    request_interval: int | None = Field(ge=1, le=6, default=1, description="The delay request value is the logarithmic mean interval in seconds between the delay request messages sent by the slave to the master.")    
    interface: str = Field(max_length=15, default="", description="PTP client will reply through this interface.")  # datasource: ['system.interface.name']    
    server_mode: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable FortiGate PTP server mode. Your FortiGate becomes an PTP server for other devices on your network.")    
    server_interface: list[ServerInterface] = Field(default=None, description="FortiGate interface(s) with PTP server mode enabled. Devices on your network can contact these interfaces for PTP services.")    
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
    "PtpModel",    "PtpServerInterface",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:34.920601Z
# ============================================================================