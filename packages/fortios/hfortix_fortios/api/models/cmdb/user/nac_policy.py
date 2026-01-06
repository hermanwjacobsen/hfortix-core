"""
Pydantic Models for CMDB - user/nac_policy

Runtime validation models for user/nac_policy configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.user.nac_policy import 
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

class NacPolicySeverity(BaseModel):
    """
    Child table model for severity.
    
    NAC policy matching devices vulnerability severity lists.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    severity_num: int = Field(ge=0, le=4, default=0, description="Enter multiple severity levels, where 0 = Info, 1 = Low, ..., 4 = Critical")
class NacPolicySwitchGroup(BaseModel):
    """
    Child table model for switch-group.
    
    List of managed FortiSwitch groups on which NAC policy can be applied.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Managed FortiSwitch group name from available options.")  # datasource: ['switch-controller.switch-group.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class NacPolicyCategoryEnum(str, Enum):
    """Allowed values for category field."""
    DEVICE = "device"    FIREWALL_USER = "firewall-user"    EMS_TAG = "ems-tag"    FORTIVOICE_TAG = "fortivoice-tag"    VULNERABILITY = "vulnerability"

# ============================================================================
# Main Model
# ============================================================================

class NacPolicyModel(BaseModel):
    """
    Pydantic model for user/nac_policy configuration.
    
    Configure NAC policy matching pattern to identify matching NAC devices.
    
    Validation Rules:        - name: max_length=63 pattern=        - description: max_length=63 pattern=        - category: pattern=        - status: pattern=        - match_type: pattern=        - match_period: min=0 max=120 pattern=        - match_remove: pattern=        - mac: max_length=17 pattern=        - hw_vendor: max_length=15 pattern=        - type: max_length=15 pattern=        - family: max_length=31 pattern=        - os: max_length=31 pattern=        - hw_version: max_length=15 pattern=        - sw_version: max_length=15 pattern=        - host: max_length=64 pattern=        - user: max_length=64 pattern=        - src: max_length=15 pattern=        - user_group: max_length=35 pattern=        - ems_tag: max_length=79 pattern=        - fortivoice_tag: max_length=79 pattern=        - severity: pattern=        - switch_fortilink: max_length=15 pattern=        - switch_group: pattern=        - switch_mac_policy: max_length=63 pattern=        - firewall_address: max_length=79 pattern=        - ssid_policy: max_length=35 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=63, default="", description="NAC policy name.")    
    description: str | None = Field(max_length=63, default="", description="Description for the NAC policy matching pattern.")    
    category: CategoryEnum | None = Field(default="device", description="Category of NAC policy.")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable NAC policy.")    
    match_type: Literal["dynamic", "override"] | None = Field(default="dynamic", description="Match and retain the devices based on the type.")    
    match_period: int | None = Field(ge=0, le=120, default=0, description="Number of days the matched devices will be retained (0 - always retain)")    
    match_remove: Literal["default", "link-down"] | None = Field(default="default", description="Options to remove the matched override devices.")    
    mac: str | None = Field(max_length=17, default="", description="NAC policy matching MAC address.")    
    hw_vendor: str | None = Field(max_length=15, default="", description="NAC policy matching hardware vendor.")    
    type: str | None = Field(max_length=15, default="", description="NAC policy matching type.")    
    family: str | None = Field(max_length=31, default="", description="NAC policy matching family.")    
    os: str | None = Field(max_length=31, default="", description="NAC policy matching operating system.")    
    hw_version: str | None = Field(max_length=15, default="", description="NAC policy matching hardware version.")    
    sw_version: str | None = Field(max_length=15, default="", description="NAC policy matching software version.")    
    host: str | None = Field(max_length=64, default="", description="NAC policy matching host.")    
    user: str | None = Field(max_length=64, default="", description="NAC policy matching user.")    
    src: str | None = Field(max_length=15, default="", description="NAC policy matching source.")    
    user_group: str | None = Field(max_length=35, default="", description="NAC policy matching user group.")  # datasource: ['user.group.name']    
    ems_tag: str | None = Field(max_length=79, default="", description="NAC policy matching EMS tag.")  # datasource: ['firewall.address.name']    
    fortivoice_tag: str | None = Field(max_length=79, default="", description="NAC policy matching FortiVoice tag.")  # datasource: ['firewall.address.name']    
    severity: list[Severity] = Field(default=None, description="NAC policy matching devices vulnerability severity lists.")    
    switch_fortilink: str | None = Field(max_length=15, default="", description="FortiLink interface for which this NAC policy belongs to.")  # datasource: ['system.interface.name']    
    switch_group: list[SwitchGroup] = Field(default=None, description="List of managed FortiSwitch groups on which NAC policy can be applied.")    
    switch_mac_policy: str | None = Field(max_length=63, default="", description="Switch MAC policy action to be applied on the matched NAC policy.")  # datasource: ['switch-controller.mac-policy.name']    
    firewall_address: str | None = Field(max_length=79, default="", description="Dynamic firewall address to associate MAC which match this policy.")  # datasource: ['firewall.address.name']    
    ssid_policy: str | None = Field(max_length=35, default="", description="SSID policy to be applied on the matched NAC policy.")  # datasource: ['wireless-controller.ssid-policy.name']    
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
    @field_validator('ems_tag')
    @classmethod
    def validate_ems_tag(cls, v: Any) -> Any:
        """
        Validate ems_tag field.
        
        Datasource: ['firewall.address.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('fortivoice_tag')
    @classmethod
    def validate_fortivoice_tag(cls, v: Any) -> Any:
        """
        Validate fortivoice_tag field.
        
        Datasource: ['firewall.address.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('switch_fortilink')
    @classmethod
    def validate_switch_fortilink(cls, v: Any) -> Any:
        """
        Validate switch_fortilink field.
        
        Datasource: ['system.interface.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('switch_mac_policy')
    @classmethod
    def validate_switch_mac_policy(cls, v: Any) -> Any:
        """
        Validate switch_mac_policy field.
        
        Datasource: ['switch-controller.mac-policy.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('firewall_address')
    @classmethod
    def validate_firewall_address(cls, v: Any) -> Any:
        """
        Validate firewall_address field.
        
        Datasource: ['firewall.address.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('ssid_policy')
    @classmethod
    def validate_ssid_policy(cls, v: Any) -> Any:
        """
        Validate ssid_policy field.
        
        Datasource: ['wireless-controller.ssid-policy.name']
        
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
    "NacPolicyModel",    "NacPolicySeverity",    "NacPolicySwitchGroup",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:34.809532Z
# ============================================================================