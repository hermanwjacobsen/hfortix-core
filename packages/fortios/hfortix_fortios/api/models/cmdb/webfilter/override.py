"""
Pydantic Models for CMDB - webfilter/override

Runtime validation models for webfilter/override configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.webfilter.override import 
    >>>
    >>> # Create with validation
    >>> obj = (
    ...     id=1,
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

class OverrideScopeEnum(str, Enum):
    """Allowed values for scope field."""
    USER = "user"    USER_GROUP = "user-group"    IP = "ip"    IP6 = "ip6"

# ============================================================================
# Main Model
# ============================================================================

class OverrideModel(BaseModel):
    """
    Pydantic model for webfilter/override configuration.
    
    Configure FortiGuard Web Filter administrative overrides.
    
    Validation Rules:        - id: min=0 max=4294967295 pattern=        - status: pattern=        - scope: pattern=        - ip: pattern=        - user: max_length=64 pattern=        - user_group: max_length=63 pattern=        - old_profile: max_length=47 pattern=        - new_profile: max_length=47 pattern=        - ip6: pattern=        - expires: pattern=        - initiator: max_length=64 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="Override rule ID.")    
    status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable override rule.")    
    scope: ScopeEnum | None = Field(default="user", description="Override either the specific user, user group, IPv4 address, or IPv6 address.")    
    ip: str = Field(default="0.0.0.0", description="IPv4 address which the override applies.")    
    user: str = Field(max_length=64, default="", description="Name of the user which the override applies.")    
    user_group: str = Field(max_length=63, default="", description="Specify the user group for which the override applies.")  # datasource: ['user.group.name']    
    old_profile: str = Field(max_length=47, default="", description="Name of the web filter profile which the override applies.")  # datasource: ['webfilter.profile.name']    
    new_profile: str = Field(max_length=47, default="", description="Name of the new web filter profile used by the override.")  # datasource: ['webfilter.profile.name']    
    ip6: str = Field(default="::", description="IPv6 address which the override applies.")    
    expires: str = Field(default="1970/01/01 00:00:00", description="Override expiration date and time, from 5 minutes to 365 from now (format: yyyy/mm/dd hh:mm:ss).")    
    initiator: str | None = Field(max_length=64, default="", description="Initiating user of override (read-only setting).")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('user_group')
    @classmethod
    def validate_user_group(cls, v: Any) -> Any:
        """
        Validate user_group field.
        
        Datasource: ['user.group.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('old_profile')
    @classmethod
    def validate_old_profile(cls, v: Any) -> Any:
        """
        Validate old_profile field.
        
        Datasource: ['webfilter.profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('new_profile')
    @classmethod
    def validate_new_profile(cls, v: Any) -> Any:
        """
        Validate new_profile field.
        
        Datasource: ['webfilter.profile.name']
        
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
    "OverrideModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:32.921324Z
# ============================================================================