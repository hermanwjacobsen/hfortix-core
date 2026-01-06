"""
Pydantic Models for CMDB - user/external_identity_provider

Runtime validation models for user/external_identity_provider configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.user.external_identity_provider import 
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
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class ExternalIdentityProviderModel(BaseModel):
    """
    Pydantic model for user/external_identity_provider configuration.
    
    Configure external identity provider.
    
    Validation Rules:        - name: max_length=35 pattern=        - type: pattern=        - version: pattern=        - url: max_length=127 pattern=        - user_attr_name: max_length=63 pattern=        - group_attr_name: max_length=63 pattern=        - port: min=0 max=65535 pattern=        - source_ip: max_length=63 pattern=        - interface_select_method: pattern=        - interface: max_length=15 pattern=        - vrf_select: min=0 max=511 pattern=        - server_identity_check: pattern=        - timeout: min=1 max=60 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=35, default="", description="External identity provider name.")    
    type: Literal["ms-graph"] = Field(default="", description="External identity provider type.")    
    version: Literal["v1.0", "beta"] | None = Field(default="", description="External identity API version.")    
    url: str | None = Field(max_length=127, default="", description="External identity provider URL (e.g. \"https://example.com:8080/api/v1\").")    
    user_attr_name: str | None = Field(max_length=63, default="userPrincipalName", description="User attribute name in authentication query.")    
    group_attr_name: str | None = Field(max_length=63, default="id", description="Group attribute name in authentication query.")    
    port: int | None = Field(ge=0, le=65535, default=0, description="External identity provider service port number (0 to use default).")    
    source_ip: str | None = Field(max_length=63, default="", description="Use this IPv4/v6 address to connect to the external identity provider.")    
    interface_select_method: Literal["auto", "sdwan", "specify"] | None = Field(default="auto", description="Specify how to select outgoing interface to reach server.")    
    interface: str = Field(max_length=15, default="", description="Specify outgoing interface to reach server.")  # datasource: ['system.interface.name']    
    vrf_select: int | None = Field(ge=0, le=511, default=0, description="VRF ID used for connection to server.")    
    server_identity_check: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable server's identity check against its certificate and subject alternative name(s).")    
    timeout: int | None = Field(ge=1, le=60, default=5, description="Connection timeout value in seconds (default=5).")    
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
    "ExternalIdentityProviderModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:33.923126Z
# ============================================================================