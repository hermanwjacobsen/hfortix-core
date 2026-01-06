"""
Pydantic Models for CMDB - vpn/ipsec/manualkey_interface

Runtime validation models for vpn/ipsec/manualkey_interface configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.vpn.ipsec.manualkey_interface import 
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
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class ManualkeyInterfaceAuth_algEnum(str, Enum):
    """Allowed values for auth_alg field."""
    NULL = "null"    MD5 = "md5"    SHA1 = "sha1"    SHA256 = "sha256"    SHA384 = "sha384"    SHA512 = "sha512"
class ManualkeyInterfaceEnc_algEnum(str, Enum):
    """Allowed values for enc_alg field."""
    NULL = "null"    DES = "des"    3DES = "3des"    AES128 = "aes128"    AES192 = "aes192"    AES256 = "aes256"    ARIA128 = "aria128"    ARIA192 = "aria192"    ARIA256 = "aria256"    SEED = "seed"

# ============================================================================
# Main Model
# ============================================================================

class ManualkeyInterfaceModel(BaseModel):
    """
    Pydantic model for vpn/ipsec/manualkey_interface configuration.
    
    Configure IPsec manual keys.
    
    Validation Rules:        - name: max_length=15 pattern=        - interface: max_length=15 pattern=        - ip_version: pattern=        - addr_type: pattern=        - remote_gw: pattern=        - remote_gw6: pattern=        - local_gw: pattern=        - local_gw6: pattern=        - auth_alg: pattern=        - enc_alg: pattern=        - auth_key: pattern=        - enc_key: pattern=        - local_spi: pattern=        - remote_spi: pattern=        - npu_offload: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=15, default="", description="IPsec tunnel name.")    
    interface: str = Field(max_length=15, default="", description="Name of the physical, aggregate, or VLAN interface.")  # datasource: ['system.interface.name']    
    ip_version: Literal["4", "6"] | None = Field(default="4", description="IP version to use for VPN interface.")    
    addr_type: Literal["4", "6"] | None = Field(default="4", description="IP version to use for IP packets.")    
    remote_gw: str = Field(default="0.0.0.0", description="IPv4 address of the remote gateway's external interface.")    
    remote_gw6: str = Field(default="::", description="Remote IPv6 address of VPN gateway.")    
    local_gw: str | None = Field(default="0.0.0.0", description="IPv4 address of the local gateway's external interface.")    
    local_gw6: str | None = Field(default="::", description="Local IPv6 address of VPN gateway.")    
    auth_alg: AuthAlgEnum = Field(default="null", description="Authentication algorithm. Must be the same for both ends of the tunnel.")    
    enc_alg: EncAlgEnum = Field(default="null", description="Encryption algorithm. Must be the same for both ends of the tunnel.")    
    auth_key: str = Field(default="", description="Hexadecimal authentication key in 16-digit (8-byte) segments separated by hyphens.")    
    enc_key: str = Field(default="", description="Hexadecimal encryption key in 16-digit (8-byte) segments separated by hyphens.")    
    local_spi: str = Field(default="", description="Local SPI, a hexadecimal 8-digit (4-byte) tag. Discerns between two traffic streams with different encryption rules.")    
    remote_spi: str = Field(default="", description="Remote SPI, a hexadecimal 8-digit (4-byte) tag. Discerns between two traffic streams with different encryption rules.")    
    npu_offload: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable offloading IPsec VPN manual key sessions to NPUs.")    
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
    "ManualkeyInterfaceModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:33.146132Z
# ============================================================================