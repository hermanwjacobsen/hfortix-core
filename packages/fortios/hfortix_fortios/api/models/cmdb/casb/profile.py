"""
Pydantic Models for CMDB - casb/profile

Runtime validation models for casb/profile configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.casb.profile import 
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

from pydantic import BaseModel, Field
from typing import Any, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class ProfileSaasApplication(BaseModel):
    """
    Child table model for saas-application.
    
    CASB profile SaaS application.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="CASB profile SaaS application name.")  # datasource: ['casb.saas-application.name']    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable setting.")    
    safe_search: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable safe search.")    
    safe_search_control: list[SafeSearchControl] = Field(description="CASB profile safe search control.")    
    tenant_control: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable tenant control.")    
    tenant_control_tenants: list[TenantControlTenants] = Field(description="CASB profile tenant control tenants.")    
    advanced_tenant_control: list[AdvancedTenantControl] = Field(default=None, description="CASB profile advanced tenant control.")    
    domain_control: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable domain control.")    
    domain_control_domains: list[DomainControlDomains] = Field(description="CASB profile domain control domains.")    
    log: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable log settings.")    
    access_rule: list[AccessRule] = Field(default=None, description="CASB profile access rule.")    
    custom_control: list[CustomControl] = Field(default=None, description="CASB profile custom control.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class ProfileModel(BaseModel):
    """
    Pydantic model for casb/profile configuration.
    
    Configure CASB profile.
    
    Validation Rules:        - name: max_length=47 pattern=        - comment: max_length=255 pattern=        - saas_application: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=47, default="", description="CASB profile name.")    
    comment: str | None = Field(max_length=255, default=None, description="Comment.")    
    saas_application: list[SaasApplication] = Field(default=None, description="CASB profile SaaS application.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
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
    "ProfileModel",    "ProfileSaasApplication",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:35.152124Z
# ============================================================================