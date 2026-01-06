"""
Pydantic Models for CMDB - casb/user_activity

Runtime validation models for casb/user_activity configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.casb.user_activity import 
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

class UserActivityMatch(BaseModel):
    """
    Child table model for match.
    
    CASB user activity match rules.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="CASB user activity match rules ID.")    
    strategy: Literal["and", "or"] | None = Field(default="and", description="CASB user activity rules strategy.")    
    rules: list[Rules] = Field(default=None, description="CASB user activity rules.")    
    tenant_extraction: list[TenantExtraction] = Field(default=None, description="CASB user activity tenant extraction.")
class UserActivityControlOptions(BaseModel):
    """
    Child table model for control-options.
    
    CASB control options.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="CASB control option name.")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="CASB control option status.")    
    operations: list[Operations] = Field(default=None, description="CASB control option operations.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class UserActivityCategoryEnum(str, Enum):
    """Allowed values for category field."""
    ACTIVITY_CONTROL = "activity-control"    TENANT_CONTROL = "tenant-control"    DOMAIN_CONTROL = "domain-control"    SAFE_SEARCH_CONTROL = "safe-search-control"    ADVANCED_TENANT_CONTROL = "advanced-tenant-control"    OTHER = "other"

# ============================================================================
# Main Model
# ============================================================================

class UserActivityModel(BaseModel):
    """
    Pydantic model for casb/user_activity configuration.
    
    Configure CASB user activity.
    
    Validation Rules:        - name: max_length=79 pattern=        - uuid: max_length=36 pattern=        - status: pattern=        - description: max_length=63 pattern=        - type: pattern=        - casb_name: max_length=79 pattern=        - application: max_length=79 pattern=        - category: pattern=        - match_strategy: pattern=        - match: pattern=        - control_options: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=79, default="", description="CASB user activity name.")    
    uuid: str | None = Field(max_length=36, default="", description="Universally Unique Identifier (UUID; automatically assigned but can be manually reset).")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="CASB user activity status.")    
    description: str | None = Field(max_length=63, default="", description="CASB user activity description.")    
    type: Literal["built-in", "customized"] | None = Field(default="customized", description="CASB user activity type.")    
    casb_name: str | None = Field(max_length=79, default="", description="CASB user activity signature name.")    
    application: str = Field(max_length=79, default="", description="CASB SaaS application name.")  # datasource: ['casb.saas-application.name']    
    category: CategoryEnum | None = Field(default="activity-control", description="CASB user activity category.")    
    match_strategy: Literal["and", "or"] | None = Field(default="or", description="CASB user activity match strategy.")    
    match: list[Match] = Field(default=None, description="CASB user activity match rules.")    
    control_options: list[ControlOptions] = Field(default=None, description="CASB control options.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('application')
    @classmethod
    def validate_application(cls, v: Any) -> Any:
        """
        Validate application field.
        
        Datasource: ['casb.saas-application.name']
        
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
    "UserActivityModel",    "UserActivityMatch",    "UserActivityControlOptions",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:34.682890Z
# ============================================================================