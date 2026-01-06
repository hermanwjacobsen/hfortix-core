"""
Pydantic Models for CMDB - firewall/DoS_policy

Runtime validation models for firewall/DoS_policy configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.firewall.DoS_policy import 
    >>>
    >>> # Create with validation
    >>> obj = (
    ...     policyid=1,
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

class DosPolicySrcaddr(BaseModel):
    """
    Child table model for srcaddr.
    
    Source address name from available addresses.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name']
class DosPolicyDstaddr(BaseModel):
    """
    Child table model for dstaddr.
    
    Destination address name from available addresses.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name']
class DosPolicyService(BaseModel):
    """
    Child table model for service.
    
    Service object from available options.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Service name.")  # datasource: ['firewall.service.custom.name', 'firewall.service.group.name']
class DosPolicyAnomaly(BaseModel):
    """
    Child table model for anomaly.
    
    Anomaly name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=63, default="", description="Anomaly name.")    
    status: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable this anomaly.")    
    log: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable anomaly logging.")    
    action: Literal["pass", "block"] | None = Field(default="pass", description="Action taken when the threshold is reached.")    
    quarantine: Literal["none", "attacker"] | None = Field(default="none", description="Quarantine method.")    
    quarantine_expiry: str | None = Field(default="5m", description="Duration of quarantine. (Format ###d##h##m, minimum 1m, maximum 364d23h59m, default = 5m). Requires quarantine set to attacker.")    
    quarantine_log: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable quarantine logging.")    
    threshold: int | None = Field(ge=1, le=2147483647, default=0, description="Anomaly threshold. Number of detected instances (packets per second or concurrent session number) that triggers the anomaly action.")    
    threshold(default): int | None = Field(ge=0, le=4294967295, default=0, description="Number of detected instances (packets per second or concurrent session number) which triggers action (1 - 2147483647, default = 1000). Note that each anomaly has a different threshold value assigned to it.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class DosPolicyModel(BaseModel):
    """
    Pydantic model for firewall/DoS_policy configuration.
    
    Configure IPv4 DoS policies.
    
    Validation Rules:        - policyid: min=0 max=9999 pattern=        - status: pattern=        - name: max_length=35 pattern=        - comments: max_length=1023 pattern=        - interface: max_length=35 pattern=        - srcaddr: pattern=        - dstaddr: pattern=        - service: pattern=        - anomaly: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    policyid: int | None = Field(ge=0, le=9999, default=0, description="Policy ID.")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable this policy.")    
    name: str | None = Field(max_length=35, default="", description="Policy name.")    
    comments: str | None = Field(max_length=1023, default=None, description="Comment.")    
    interface: str = Field(max_length=35, default="", description="Incoming interface name from available interfaces.")  # datasource: ['system.zone.name', 'system.sdwan.zone.name', 'system.interface.name']    
    srcaddr: list[Srcaddr] = Field(description="Source address name from available addresses.")    
    dstaddr: list[Dstaddr] = Field(description="Destination address name from available addresses.")    
    service: list[Service] = Field(description="Service object from available options.")    
    anomaly: list[Anomaly] = Field(default=None, description="Anomaly name.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('interface')
    @classmethod
    def validate_interface(cls, v: Any) -> Any:
        """
        Validate interface field.
        
        Datasource: ['system.zone.name', 'system.sdwan.zone.name', 'system.interface.name']
        
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
    "DosPolicyModel",    "DosPolicySrcaddr",    "DosPolicyDstaddr",    "DosPolicyService",    "DosPolicyAnomaly",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:33.739155Z
# ============================================================================