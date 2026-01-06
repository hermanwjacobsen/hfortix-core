"""
Pydantic Models for CMDB - system/acme

Runtime validation models for system/acme configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.system.acme import 
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

class AcmeInterface(BaseModel):
    """
    Child table model for interface.
    
    Interface(s) on which the ACME client will listen for challenges.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    interface_name: str = Field(max_length=79, default="", description="Interface name.")  # datasource: ['system.interface.name']
class AcmeAccounts(BaseModel):
    """
    Child table model for accounts.
    
    ACME accounts list.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: str | None = Field(max_length=255, default="", description="Account id.")    
    status: str = Field(max_length=127, default="", description="Account status.")    
    url: str = Field(max_length=511, default="", description="Account url.")    
    ca_url: str = Field(max_length=255, default="", description="Account ca_url.")    
    email: str = Field(max_length=255, default="", description="Account email.")    
    eab_key_id: str | None = Field(max_length=255, default=None, description="External Acccount Binding Key ID.")    
    eab_key_hmac: Any = Field(max_length=128, default=None, description="External Acccount Binding Key HMAC.")    
    privatekey: str = Field(max_length=8191, default="", description="Account Private Key.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class AcmeModel(BaseModel):
    """
    Pydantic model for system/acme configuration.
    
    Configure ACME client.
    
    Validation Rules:        - interface: pattern=        - use_ha_direct: pattern=        - source_ip: pattern=        - source_ip6: pattern=        - accounts: pattern=        - acc_details: pattern=        - status: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    interface: list[Interface] = Field(default=None, description="Interface(s) on which the ACME client will listen for challenges.")    
    use_ha_direct: Literal["enable", "disable"] | None = Field(default="disable", description="Enable the use of 'ha-mgmt' interface to connect to the ACME server when 'ha-direct' is enabled in HA configuration")    
    source_ip: str | None = Field(default="0.0.0.0", description="Source IPv4 address used to connect to the ACME server.")    
    source_ip6: str | None = Field(default="::", description="Source IPv6 address used to connect to the ACME server.")    
    accounts: list[Accounts] = Field(default=None, description="ACME accounts list.")    
    acc_details: Any = Field(default=None, description="Print Account information and decrypted key.")    
    status: Any = Field(default=None, description="Print information about the current status of the acme client.")    
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
    "AcmeModel",    "AcmeInterface",    "AcmeAccounts",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:34.980816Z
# ============================================================================