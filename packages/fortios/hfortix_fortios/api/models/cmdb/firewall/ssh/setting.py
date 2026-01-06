"""
Pydantic Models for CMDB - firewall/ssh/setting

Runtime validation models for firewall/ssh/setting configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.firewall.ssh.setting import 
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
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class SettingModel(BaseModel):
    """
    Pydantic model for firewall/ssh/setting configuration.
    
    SSH proxy settings.
    
    Validation Rules:        - caname: max_length=35 pattern=        - untrusted_caname: max_length=35 pattern=        - hostkey_rsa2048: max_length=35 pattern=        - hostkey_dsa1024: max_length=35 pattern=        - hostkey_ecdsa256: max_length=35 pattern=        - hostkey_ecdsa384: max_length=35 pattern=        - hostkey_ecdsa521: max_length=35 pattern=        - hostkey_ed25519: max_length=35 pattern=        - host_trusted_checking: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    caname: str | None = Field(max_length=35, default="", description="CA certificate used by SSH Inspection.")  # datasource: ['firewall.ssh.local-ca.name']    
    untrusted_caname: str | None = Field(max_length=35, default="", description="Untrusted CA certificate used by SSH Inspection.")  # datasource: ['firewall.ssh.local-ca.name']    
    hostkey_rsa2048: str | None = Field(max_length=35, default="", description="RSA certificate used by SSH proxy.")  # datasource: ['firewall.ssh.local-key.name']    
    hostkey_dsa1024: str | None = Field(max_length=35, default="", description="DSA certificate used by SSH proxy.")  # datasource: ['firewall.ssh.local-key.name']    
    hostkey_ecdsa256: str | None = Field(max_length=35, default="", description="ECDSA nid256 certificate used by SSH proxy.")  # datasource: ['firewall.ssh.local-key.name']    
    hostkey_ecdsa384: str | None = Field(max_length=35, default="", description="ECDSA nid384 certificate used by SSH proxy.")  # datasource: ['firewall.ssh.local-key.name']    
    hostkey_ecdsa521: str | None = Field(max_length=35, default="", description="ECDSA nid384 certificate used by SSH proxy.")  # datasource: ['firewall.ssh.local-key.name']    
    hostkey_ed25519: str | None = Field(max_length=35, default="", description="ED25519 hostkey used by SSH proxy.")  # datasource: ['firewall.ssh.local-key.name']    
    host_trusted_checking: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable host trusted checking.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('caname')
    @classmethod
    def validate_caname(cls, v: Any) -> Any:
        """
        Validate caname field.
        
        Datasource: ['firewall.ssh.local-ca.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('untrusted_caname')
    @classmethod
    def validate_untrusted_caname(cls, v: Any) -> Any:
        """
        Validate untrusted_caname field.
        
        Datasource: ['firewall.ssh.local-ca.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('hostkey_rsa2048')
    @classmethod
    def validate_hostkey_rsa2048(cls, v: Any) -> Any:
        """
        Validate hostkey_rsa2048 field.
        
        Datasource: ['firewall.ssh.local-key.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('hostkey_dsa1024')
    @classmethod
    def validate_hostkey_dsa1024(cls, v: Any) -> Any:
        """
        Validate hostkey_dsa1024 field.
        
        Datasource: ['firewall.ssh.local-key.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('hostkey_ecdsa256')
    @classmethod
    def validate_hostkey_ecdsa256(cls, v: Any) -> Any:
        """
        Validate hostkey_ecdsa256 field.
        
        Datasource: ['firewall.ssh.local-key.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('hostkey_ecdsa384')
    @classmethod
    def validate_hostkey_ecdsa384(cls, v: Any) -> Any:
        """
        Validate hostkey_ecdsa384 field.
        
        Datasource: ['firewall.ssh.local-key.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('hostkey_ecdsa521')
    @classmethod
    def validate_hostkey_ecdsa521(cls, v: Any) -> Any:
        """
        Validate hostkey_ecdsa521 field.
        
        Datasource: ['firewall.ssh.local-key.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('hostkey_ed25519')
    @classmethod
    def validate_hostkey_ed25519(cls, v: Any) -> Any:
        """
        Validate hostkey_ed25519 field.
        
        Datasource: ['firewall.ssh.local-key.name']
        
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
    "SettingModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:35.916172Z
# ============================================================================