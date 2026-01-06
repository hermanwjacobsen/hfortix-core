"""
Pydantic Models for CMDB - firewall/address

Runtime validation models for firewall/address configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.firewall.address import 
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
from uuid import UUID

# ============================================================================
# Child Table Models
# ============================================================================

class AddressMacaddr(BaseModel):
    """
    Child table model for macaddr.
    
    Multiple MAC address ranges.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    macaddr: str = Field(max_length=127, default="", description="MAC address ranges <start>[-<end>] separated by space.")
class AddressFssoGroup(BaseModel):
    """
    Child table model for fsso-group.
    
    FSSO group(s).
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=511, default="", description="FSSO group name.")  # datasource: ['user.adgrp.name']
class AddressSsoAttributeValue(BaseModel):
    """
    Child table model for sso-attribute-value.
    
    RADIUS attributes value.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=511, default="", description="RADIUS attribute value.")
class AddressList(BaseModel):
    """
    Child table model for list.
    
    IP address list.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    ip: str = Field(max_length=35, default="", description="IP.")
class AddressTagging(BaseModel):
    """
    Child table model for tagging.
    
    Config object tagging.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=63, default="", description="Tagging entry name.")    
    category: str | None = Field(max_length=63, default="", description="Tag category.")  # datasource: ['system.object-tagging.category']    
    tags: list[Tags] = Field(default=None, description="Tags.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class AddressTypeEnum(str, Enum):
    """Allowed values for type field."""
    IPMASK = "ipmask"    IPRANGE = "iprange"    FQDN = "fqdn"    GEOGRAPHY = "geography"    WILDCARD = "wildcard"    DYNAMIC = "dynamic"    INTERFACE_SUBNET = "interface-subnet"    MAC = "mac"    ROUTE_TAG = "route-tag"
class AddressSub_typeEnum(str, Enum):
    """Allowed values for sub_type field."""
    SDN = "sdn"    CLEARPASS_SPT = "clearpass-spt"    FSSO = "fsso"    RSSO = "rsso"    EMS_TAG = "ems-tag"    FORTIVOICE_TAG = "fortivoice-tag"    FORTINAC_TAG = "fortinac-tag"    SWC_TAG = "swc-tag"    DEVICE_IDENTIFICATION = "device-identification"    EXTERNAL_RESOURCE = "external-resource"    OBSOLETE = "obsolete"
class AddressClearpass_sptEnum(str, Enum):
    """Allowed values for clearpass_spt field."""
    UNKNOWN = "unknown"    HEALTHY = "healthy"    QUARANTINE = "quarantine"    CHECKUP = "checkup"    TRANSIENT = "transient"    INFECTED = "infected"

# ============================================================================
# Main Model
# ============================================================================

class AddressModel(BaseModel):
    """
    Pydantic model for firewall/address configuration.
    
    Configure IPv4 addresses.
    
    Validation Rules:        - name: max_length=79 pattern=        - uuid: pattern=        - subnet: pattern=        - type: pattern=        - route_tag: min=1 max=4294967295 pattern=        - sub_type: pattern=        - clearpass_spt: pattern=        - macaddr: pattern=        - start_ip: pattern=        - end_ip: pattern=        - fqdn: max_length=255 pattern=        - country: max_length=2 pattern=        - wildcard_fqdn: max_length=255 pattern=        - cache_ttl: min=0 max=86400 pattern=        - wildcard: pattern=        - sdn: max_length=35 pattern=        - fsso_group: pattern=        - sso_attribute_value: pattern=        - interface: max_length=35 pattern=        - tenant: max_length=35 pattern=        - organization: max_length=35 pattern=        - epg_name: max_length=255 pattern=        - subnet_name: max_length=255 pattern=        - sdn_tag: max_length=15 pattern=        - policy_group: max_length=15 pattern=        - obj_tag: max_length=255 pattern=        - obj_type: pattern=        - tag_detection_level: max_length=15 pattern=        - tag_type: max_length=63 pattern=        - hw_vendor: max_length=35 pattern=        - hw_model: max_length=35 pattern=        - os: max_length=35 pattern=        - sw_version: max_length=35 pattern=        - comment: max_length=255 pattern=        - associated_interface: max_length=35 pattern=        - color: min=0 max=32 pattern=        - filter: max_length=2047 pattern=        - sdn_addr_type: pattern=        - node_ip_only: pattern=        - obj_id: max_length=255 pattern=        - list: pattern=        - tagging: pattern=        - allow_routing: pattern=        - passive_fqdn_learning: pattern=        - fabric_object: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=79, default="", description="Address name.")    
    uuid: str | None = Field(default="00000000-0000-0000-0000-000000000000", description="Universally Unique Identifier (UUID; automatically assigned but can be manually reset).")    
    subnet: Any = Field(default="0.0.0.0 0.0.0.0", description="IP address and subnet mask of address.")    
    type: TypeEnum | None = Field(default="ipmask", description="Type of address.")    
    route_tag: int | None = Field(ge=1, le=4294967295, default=0, description="route-tag address.")    
    sub_type: SubTypeEnum | None = Field(default="sdn", description="Sub-type of address.")    
    clearpass_spt: ClearpassSptEnum | None = Field(default="unknown", description="SPT (System Posture Token) value.")    
    macaddr: list[Macaddr] = Field(default=None, description="Multiple MAC address ranges.")    
    start_ip: str | None = Field(default="0.0.0.0", description="First IP address (inclusive) in the range for the address.")    
    end_ip: str | None = Field(default="0.0.0.0", description="Final IP address (inclusive) in the range for the address.")    
    fqdn: str | None = Field(max_length=255, default="", description="Fully Qualified Domain Name address.")    
    country: str | None = Field(max_length=2, default="", description="IP addresses associated to a specific country.")    
    wildcard_fqdn: str | None = Field(max_length=255, default="", description="Fully Qualified Domain Name with wildcard characters.")    
    cache_ttl: int | None = Field(ge=0, le=86400, default=0, description="Defines the minimal TTL of individual IP addresses in FQDN cache measured in seconds.")    
    wildcard: Any = Field(default="0.0.0.0 0.0.0.0", description="IP address and wildcard netmask.")    
    sdn: str | None = Field(max_length=35, default="", description="SDN.")  # datasource: ['system.sdn-connector.name']    
    fsso_group: list[FssoGroup] = Field(default=None, description="FSSO group(s).")    
    sso_attribute_value: list[SsoAttributeValue] = Field(default=None, description="RADIUS attributes value.")    
    interface: str = Field(max_length=35, default="", description="Name of interface whose IP address is to be used.")  # datasource: ['system.interface.name']    
    tenant: str | None = Field(max_length=35, default="", description="Tenant.")    
    organization: str | None = Field(max_length=35, default="", description="Organization domain name (Syntax: organization/domain).")    
    epg_name: str | None = Field(max_length=255, default="", description="Endpoint group name.")    
    subnet_name: str | None = Field(max_length=255, default="", description="Subnet name.")    
    sdn_tag: str | None = Field(max_length=15, default="", description="SDN Tag.")    
    policy_group: str | None = Field(max_length=15, default="", description="Policy group name.")    
    obj_tag: str | None = Field(max_length=255, default="", description="Tag of dynamic address object.")    
    obj_type: Literal["ip", "mac"] | None = Field(default="ip", description="Object type.")    
    tag_detection_level: str | None = Field(max_length=15, default="", description="Tag detection level of dynamic address object.")    
    tag_type: str | None = Field(max_length=63, default="", description="Tag type of dynamic address object.")    
    hw_vendor: str | None = Field(max_length=35, default="", description="Dynamic address matching hardware vendor.")    
    hw_model: str | None = Field(max_length=35, default="", description="Dynamic address matching hardware model.")    
    os: str | None = Field(max_length=35, default="", description="Dynamic address matching operating system.")    
    sw_version: str | None = Field(max_length=35, default="", description="Dynamic address matching software version.")    
    comment: str | None = Field(max_length=255, default=None, description="Comment.")    
    associated_interface: str | None = Field(max_length=35, default="", description="Network interface associated with address.")  # datasource: ['system.interface.name', 'system.zone.name']    
    color: int | None = Field(ge=0, le=32, default=0, description="Color of icon on the GUI.")    
    filter: str = Field(max_length=2047, description="Match criteria filter.")    
    sdn_addr_type: Literal["private", "public", "all"] | None = Field(default="private", description="Type of addresses to collect.")    
    node_ip_only: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable collection of node addresses only in Kubernetes.")    
    obj_id: str | None = Field(max_length=255, default=None, description="Object ID for NSX.")    
    list: list[List] = Field(default=None, description="IP address list.")    
    tagging: list[Tagging] = Field(default=None, description="Config object tagging.")    
    allow_routing: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable use of this address in routing configurations.")    
    passive_fqdn_learning: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable passive learning of FQDNs.  When enabled, the FortiGate learns, trusts, and saves FQDNs from endpoint DNS queries (default = enable).")    
    fabric_object: Literal["enable", "disable"] | None = Field(default="disable", description="Security Fabric global object setting.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('sdn')
    @classmethod
    def validate_sdn(cls, v: Any) -> Any:
        """
        Validate sdn field.
        
        Datasource: ['system.sdn-connector.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
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
    @field_validator('associated_interface')
    @classmethod
    def validate_associated_interface(cls, v: Any) -> Any:
        """
        Validate associated_interface field.
        
        Datasource: ['system.interface.name', 'system.zone.name']
        
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
    "AddressModel",    "AddressMacaddr",    "AddressFssoGroup",    "AddressSsoAttributeValue",    "AddressList",    "AddressTagging",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:36.097833Z
# ============================================================================