"""
Pydantic Models for CMDB - firewall/internet_service_name

Runtime validation models for firewall/internet_service_name configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.firewall.internet_service_name import 
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

class InternetServiceNameModel(BaseModel):
    """
    Pydantic model for firewall/internet_service_name configuration.
    
    Define internet service names.
    
    Validation Rules:        - name: max_length=63 pattern=        - type: pattern=        - internet_service_id: min=0 max=4294967295 pattern=        - country_id: min=0 max=4294967295 pattern=        - region_id: min=0 max=4294967295 pattern=        - city_id: min=0 max=4294967295 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=63, default="", description="Internet Service name.")    
    type: Literal["default", "location"] | None = Field(default="default", description="Internet Service name type.")    
    internet_service_id: int = Field(ge=0, le=4294967295, default=0, description="Internet Service ID.")  # datasource: ['firewall.internet-service.id']    
    country_id: int | None = Field(ge=0, le=4294967295, default=0, description="Country or Area ID.")  # datasource: ['firewall.country.id']    
    region_id: int | None = Field(ge=0, le=4294967295, default=0, description="Region ID.")  # datasource: ['firewall.region.id']    
    city_id: int | None = Field(ge=0, le=4294967295, default=0, description="City ID.")  # datasource: ['firewall.city.id']    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('internet_service_id')
    @classmethod
    def validate_internet_service_id(cls, v: Any) -> Any:
        """
        Validate internet_service_id field.
        
        Datasource: ['firewall.internet-service.id']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('country_id')
    @classmethod
    def validate_country_id(cls, v: Any) -> Any:
        """
        Validate country_id field.
        
        Datasource: ['firewall.country.id']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('region_id')
    @classmethod
    def validate_region_id(cls, v: Any) -> Any:
        """
        Validate region_id field.
        
        Datasource: ['firewall.region.id']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('city_id')
    @classmethod
    def validate_city_id(cls, v: Any) -> Any:
        """
        Validate city_id field.
        
        Datasource: ['firewall.city.id']
        
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
    "InternetServiceNameModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:34.878213Z
# ============================================================================