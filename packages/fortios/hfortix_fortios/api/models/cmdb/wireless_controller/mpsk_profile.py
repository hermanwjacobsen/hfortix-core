"""
Pydantic Models for CMDB - wireless_controller/mpsk_profile

Runtime validation models for wireless_controller/mpsk_profile configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.wireless_controller.mpsk_profile import 
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

# ============================================================================
# Child Table Models
# ============================================================================

class MpskProfileMpskGroup(BaseModel):
    """
    Child table model for mpsk-group.
    
    List of multiple PSK groups.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=35, default="", description="MPSK group name.")    
    vlan_type: Literal["no-vlan", "fixed-vlan"] | None = Field(default="no-vlan", description="MPSK group VLAN options.")    
    vlan_id: int | None = Field(ge=1, le=4094, default=0, description="Optional VLAN ID.")    
    mpsk_key: list[MpskKey] = Field(default=None, description="List of multiple PSK entries.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class MpskProfileModel(BaseModel):
    """
    Pydantic model for wireless_controller/mpsk_profile configuration.
    
    Configure MPSK profile.
    
    Validation Rules:        - name: max_length=35 pattern=        - mpsk_concurrent_clients: min=0 max=65535 pattern=        - mpsk_external_server_auth: pattern=        - mpsk_external_server: max_length=35 pattern=        - mpsk_type: pattern=        - mpsk_group: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=35, default="", description="MPSK profile name.")    
    mpsk_concurrent_clients: int | None = Field(ge=0, le=65535, default=0, description="Maximum number of concurrent clients that connect using the same passphrase in multiple PSK authentication (0 - 65535, default = 0, meaning no limitation).")    
    mpsk_external_server_auth: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/Disable MPSK external server authentication (default = disable).")    
    mpsk_external_server: str | None = Field(max_length=35, default="", description="RADIUS server to be used to authenticate MPSK users.")  # datasource: ['user.radius.name']    
    mpsk_type: Literal["wpa2-personal", "wpa3-sae", "wpa3-sae-transition"] | None = Field(default="wpa2-personal", description="Select the security type of keys for this profile.")    
    mpsk_group: list[MpskGroup] = Field(default=None, description="List of multiple PSK groups.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('mpsk_external_server')
    @classmethod
    def validate_mpsk_external_server(cls, v: Any) -> Any:
        """
        Validate mpsk_external_server field.
        
        Datasource: ['user.radius.name']
        
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
    "MpskProfileModel",    "MpskProfileMpskGroup",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:34.796102Z
# ============================================================================