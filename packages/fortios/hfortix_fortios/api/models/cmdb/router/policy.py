"""
Pydantic Models for CMDB - router/policy

Runtime validation models for router/policy configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.router.policy import 
    >>>
    >>> # Create with validation
    >>> obj = (
    ...     seq-num=1,
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

class PolicyInputDevice(BaseModel):
    """
    Child table model for input-device.
    
    Incoming interface name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="Interface name.")  # datasource: ['system.interface.name']
class PolicySrc(BaseModel):
    """
    Child table model for src.
    
    Source IP and mask (x.x.x.x/x).
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    subnet: str | None = Field(max_length=79, default="", description="IP and mask.")
class PolicySrcaddr(BaseModel):
    """
    Child table model for srcaddr.
    
    Source address name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="Address/group name.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name']
class PolicyDst(BaseModel):
    """
    Child table model for dst.
    
    Destination IP and mask (x.x.x.x/x).
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    subnet: str | None = Field(max_length=79, default="", description="IP and mask.")
class PolicyDstaddr(BaseModel):
    """
    Child table model for dstaddr.
    
    Destination address name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="Address/group name.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name']
class PolicyInternetServiceId(BaseModel):
    """
    Child table model for internet-service-id.
    
    Destination Internet Service ID.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=0, le=4294967295, default=0, description="Destination Internet Service ID.")  # datasource: ['firewall.internet-service.id']
class PolicyInternetServiceCustom(BaseModel):
    """
    Child table model for internet-service-custom.
    
    Custom Destination Internet Service name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Custom Destination Internet Service name.")  # datasource: ['firewall.internet-service-custom.name']
class PolicyInternetServiceFortiguard(BaseModel):
    """
    Child table model for internet-service-fortiguard.
    
    FortiGuard Destination Internet Service name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="FortiGuard Destination Internet Service name.")  # datasource: ['firewall.internet-service-fortiguard.name']
class PolicyUsers(BaseModel):
    """
    Child table model for users.
    
    List of users.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="User name.")  # datasource: ['user.local.name']
class PolicyGroups(BaseModel):
    """
    Child table model for groups.
    
    List of user groups.
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

class PolicyModel(BaseModel):
    """
    Pydantic model for router/policy configuration.
    
    Configure IPv4 routing policies.
    
    Validation Rules:        - seq_num: min=1 max=65535 pattern=        - input_device: pattern=        - input_device_negate: pattern=        - src: pattern=        - srcaddr: pattern=        - src_negate: pattern=        - dst: pattern=        - dstaddr: pattern=        - dst_negate: pattern=        - action: pattern=        - protocol: min=0 max=255 pattern=        - start_port: min=0 max=65535 pattern=        - end_port: min=0 max=65535 pattern=        - start_source_port: min=0 max=65535 pattern=        - end_source_port: min=0 max=65535 pattern=        - gateway: pattern=        - output_device: max_length=35 pattern=        - tos: pattern=        - tos_mask: pattern=        - status: pattern=        - comments: max_length=255 pattern=        - internet_service_id: pattern=        - internet_service_custom: pattern=        - internet_service_fortiguard: pattern=        - users: pattern=        - groups: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    seq_num: int | None = Field(ge=1, le=65535, default=0, description="Sequence number(1-65535).")    
    input_device: list[InputDevice] = Field(default=None, description="Incoming interface name.")    
    input_device_negate: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable negation of input device match.")    
    src: list[Src] = Field(default=None, description="Source IP and mask (x.x.x.x/x).")    
    srcaddr: list[Srcaddr] = Field(default=None, description="Source address name.")    
    src_negate: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable negating source address match.")    
    dst: list[Dst] = Field(default=None, description="Destination IP and mask (x.x.x.x/x).")    
    dstaddr: list[Dstaddr] = Field(default=None, description="Destination address name.")    
    dst_negate: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable negating destination address match.")    
    action: Literal["deny", "permit"] | None = Field(default="permit", description="Action of the policy route.")    
    protocol: int | None = Field(ge=0, le=255, default=0, description="Protocol number (0 - 255).")    
    start_port: int | None = Field(ge=0, le=65535, default=0, description="Start destination port number (0 - 65535).")    
    end_port: int | None = Field(ge=0, le=65535, default=65535, description="End destination port number (0 - 65535).")    
    start_source_port: int | None = Field(ge=0, le=65535, default=0, description="Start source port number (0 - 65535).")    
    end_source_port: int | None = Field(ge=0, le=65535, default=65535, description="End source port number (0 - 65535).")    
    gateway: str | None = Field(default="0.0.0.0", description="IP address of the gateway.")    
    output_device: str | None = Field(max_length=35, default="", description="Outgoing interface name.")  # datasource: ['system.interface.name']    
    tos: str | None = Field(default="", description="Type of service bit pattern.")    
    tos_mask: str | None = Field(default="", description="Type of service evaluated bits.")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable this policy route.")    
    comments: str | None = Field(max_length=255, default=None, description="Optional comments.")    
    internet_service_id: list[InternetServiceId] = Field(default=None, description="Destination Internet Service ID.")    
    internet_service_custom: list[InternetServiceCustom] = Field(default=None, description="Custom Destination Internet Service name.")    
    internet_service_fortiguard: list[InternetServiceFortiguard] = Field(default=None, description="FortiGuard Destination Internet Service name.")    
    users: list[Users] = Field(default=None, description="List of users.")    
    groups: list[Groups] = Field(default=None, description="List of user groups.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('output_device')
    @classmethod
    def validate_output_device(cls, v: Any) -> Any:
        """
        Validate output_device field.
        
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
    "PolicyModel",    "PolicyInputDevice",    "PolicySrc",    "PolicySrcaddr",    "PolicyDst",    "PolicyDstaddr",    "PolicyInternetServiceId",    "PolicyInternetServiceCustom",    "PolicyInternetServiceFortiguard",    "PolicyUsers",    "PolicyGroups",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:35.342325Z
# ============================================================================