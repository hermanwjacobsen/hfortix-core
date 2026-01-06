"""
Pydantic Models for CMDB - firewall/ttl_policy

Runtime validation models for firewall/ttl_policy configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.firewall.ttl_policy import 
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

# ============================================================================
# Child Table Models
# ============================================================================

class TtlPolicySrcaddr(BaseModel):
    """
    Child table model for srcaddr.
    
    Source address object(s) from available options. Separate multiple names with a space.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name']
class TtlPolicyService(BaseModel):
    """
    Child table model for service.
    
    Service object(s) from available options. Separate multiple names with a space.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Service name.")  # datasource: ['firewall.service.custom.name', 'firewall.service.group.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class TtlPolicyModel(BaseModel):
    """
    Pydantic model for firewall/ttl_policy configuration.
    
    Configure TTL policies.
    
    Validation Rules:        - id: min=0 max=4294967295 pattern=        - status: pattern=        - action: pattern=        - srcintf: max_length=35 pattern=        - srcaddr: pattern=        - service: pattern=        - schedule: max_length=35 pattern=        - ttl: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    id: int = Field(ge=0, le=4294967295, default=0, description="ID.")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable this TTL policy.")    
    action: Literal["accept", "deny"] | None = Field(default="deny", description="Action to be performed on traffic matching this policy (default = deny).")    
    srcintf: str = Field(max_length=35, default="", description="Source interface name from available interfaces.")  # datasource: ['system.zone.name', 'system.sdwan.zone.name', 'system.interface.name']    
    srcaddr: list[Srcaddr] = Field(description="Source address object(s) from available options. Separate multiple names with a space.")    
    service: list[Service] = Field(description="Service object(s) from available options. Separate multiple names with a space.")    
    schedule: str = Field(max_length=35, default="", description="Schedule object from available options.")  # datasource: ['firewall.schedule.onetime.name', 'firewall.schedule.recurring.name', 'firewall.schedule.group.name']    
    ttl: str = Field(default="", description="Value/range to match against the packet's Time to Live value (format: ttl[ - ttl_high], 1 - 255).")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('srcintf')
    @classmethod
    def validate_srcintf(cls, v: Any) -> Any:
        """
        Validate srcintf field.
        
        Datasource: ['system.zone.name', 'system.sdwan.zone.name', 'system.interface.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('schedule')
    @classmethod
    def validate_schedule(cls, v: Any) -> Any:
        """
        Validate schedule field.
        
        Datasource: ['firewall.schedule.onetime.name', 'firewall.schedule.recurring.name', 'firewall.schedule.group.name']
        
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
    "TtlPolicyModel",    "TtlPolicySrcaddr",    "TtlPolicyService",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:34.612708Z
# ============================================================================