"""
Pydantic Models for CMDB - user/tacacs_plus

Runtime validation models for user/tacacs_plus configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.user.tacacs_plus import 
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

class TacacsPlusAuthen_typeEnum(str, Enum):
    """Allowed values for authen_type field."""
    MSCHAP = "mschap"    CHAP = "chap"    PAP = "pap"    ASCII = "ascii"    AUTO = "auto"

# ============================================================================
# Main Model
# ============================================================================

class TacacsPlusModel(BaseModel):
    """
    Pydantic model for user/tacacs_plus configuration.
    
    Configure TACACS+ server entries.
    
    Validation Rules:        - name: max_length=35 pattern=        - server: max_length=63 pattern=        - secondary_server: max_length=63 pattern=        - tertiary_server: max_length=63 pattern=        - port: min=1 max=65535 pattern=        - key: max_length=128 pattern=        - secondary_key: max_length=128 pattern=        - tertiary_key: max_length=128 pattern=        - status_ttl: min=0 max=600 pattern=        - authen_type: pattern=        - authorization: pattern=        - source_ip: max_length=63 pattern=        - interface_select_method: pattern=        - interface: max_length=15 pattern=        - vrf_select: min=0 max=511 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=35, default="", description="TACACS+ server entry name.")    
    server: str = Field(max_length=63, default="", description="Primary TACACS+ server CN domain name or IP address.")    
    secondary_server: str | None = Field(max_length=63, default="", description="Secondary TACACS+ server CN domain name or IP address.")    
    tertiary_server: str | None = Field(max_length=63, default="", description="Tertiary TACACS+ server CN domain name or IP address.")    
    port: int | None = Field(ge=1, le=65535, default=49, description="Port number of the TACACS+ server.")    
    key: Any = Field(max_length=128, default=None, description="Key to access the primary server.")    
    secondary_key: Any = Field(max_length=128, default=None, description="Key to access the secondary server.")    
    tertiary_key: Any = Field(max_length=128, default=None, description="Key to access the tertiary server.")    
    status_ttl: int | None = Field(ge=0, le=600, default=300, description="Time for which server reachability is cached so that when a server is unreachable, it will not be retried for at least this period of time (0 = cache disabled, default = 300).")    
    authen_type: AuthenTypeEnum | None = Field(default="auto", description="Allowed authentication protocols/methods.")    
    authorization: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable TACACS+ authorization.")    
    source_ip: str | None = Field(max_length=63, default="", description="Source IP address for communications to TACACS+ server.")    
    interface_select_method: Literal["auto", "sdwan", "specify"] | None = Field(default="auto", description="Specify how to select outgoing interface to reach server.")    
    interface: str = Field(max_length=15, default="", description="Specify outgoing interface to reach server.")  # datasource: ['system.interface.name']    
    vrf_select: int | None = Field(ge=0, le=511, default=0, description="VRF ID used for connection to server.")    
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
    "TacacsPlusModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:33.970564Z
# ============================================================================