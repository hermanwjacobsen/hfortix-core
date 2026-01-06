"""
Pydantic Models for CMDB - firewall/auth_portal

Runtime validation models for firewall/auth_portal configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.firewall.auth_portal import 
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

class AuthPortalGroups(BaseModel):
    """
    Child table model for groups.
    
    Firewall user groups permitted to authenticate through this portal. Separate group names with spaces.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Group name.")  # datasource: ['user.group.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class AuthPortalModel(BaseModel):
    """
    Pydantic model for firewall/auth_portal configuration.
    
    Configure firewall authentication portals.
    
    Validation Rules:        - groups: pattern=        - portal_addr: max_length=63 pattern=        - portal_addr6: max_length=63 pattern=        - identity_based_route: max_length=35 pattern=        - proxy_auth: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    groups: list[Groups] = Field(default=None, description="Firewall user groups permitted to authenticate through this portal. Separate group names with spaces.")    
    portal_addr: str | None = Field(max_length=63, default="", description="Address (or FQDN) of the authentication portal.")    
    portal_addr6: str | None = Field(max_length=63, default="", description="IPv6 address (or FQDN) of authentication portal.")    
    identity_based_route: str | None = Field(max_length=35, default="", description="Name of the identity-based route that applies to this portal.")  # datasource: ['firewall.identity-based-route.name']    
    proxy_auth: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable authentication by proxy daemon (default = disable).")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('identity_based_route')
    @classmethod
    def validate_identity_based_route(cls, v: Any) -> Any:
        """
        Validate identity_based_route field.
        
        Datasource: ['firewall.identity-based-route.name']
        
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
    "AuthPortalModel",    "AuthPortalGroups",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:35.212882Z
# ============================================================================