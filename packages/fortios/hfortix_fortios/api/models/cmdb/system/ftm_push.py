"""
Pydantic Models for CMDB - system/ftm_push

Runtime validation models for system/ftm_push configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.system.ftm_push import 
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
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class FtmPushModel(BaseModel):
    """
    Pydantic model for system/ftm_push configuration.
    
    Configure FortiToken Mobile push services.
    
    Validation Rules:        - proxy: pattern=        - interface: max_length=35 pattern=        - server: max_length=127 pattern=        - server_port: min=1 max=65535 pattern=        - server_cert: max_length=35 pattern=        - server_ip: pattern=        - status: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    proxy: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable communication to the proxy server in FortiGuard configuration.")    
    interface: str | None = Field(max_length=35, default="", description="Interface of FortiToken Mobile push services server.")  # datasource: ['system.interface.name']    
    server: str | None = Field(max_length=127, default="", description="IPv4 address or domain name of FortiToken Mobile push services server.")    
    server_port: int | None = Field(ge=1, le=65535, default=4433, description="Port to communicate with FortiToken Mobile push services server (1 - 65535, default = 4433).")    
    server_cert: str | None = Field(max_length=35, default="Fortinet_GUI_Server", description="Name of the server certificate to be used for SSL.")  # datasource: ['certificate.local.name']    
    server_ip: str | None = Field(default="0.0.0.0", description="IPv4 address of FortiToken Mobile push services server (format: xxx.xxx.xxx.xxx).")    
    status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable the use of FortiToken Mobile push services.")    
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
    @field_validator('server_cert')
    @classmethod
    def validate_server_cert(cls, v: Any) -> Any:
        """
        Validate server_cert field.
        
        Datasource: ['certificate.local.name']
        
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
    "FtmPushModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:32.945917Z
# ============================================================================