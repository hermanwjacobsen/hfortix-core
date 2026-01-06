"""
Pydantic Models for CMDB - system/csf

Runtime validation models for system/csf configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.system.csf import 
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

class CsfTrustedList(BaseModel):
    """
    Child table model for trusted-list.
    
    Pre-authorized and blocked security fabric nodes.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=35, default="", description="Name.")    
    authorization_type: Literal["serial", "certificate"] | None = Field(default="serial", description="Authorization type.")    
    serial: str | None = Field(max_length=19, default="", description="Serial.")    
    certificate: str | None = Field(max_length=32767, default=None, description="Certificate.")    
    action: Literal["accept", "deny"] | None = Field(default="accept", description="Security fabric authorization action.")    
    ha_members: list[HaMembers] = Field(max_length=19, default="", description="HA members.")    
    downstream_authorization: Literal["enable", "disable"] | None = Field(default="disable", description="Trust authorizations by this node's administrator.")    
    index: int | None = Field(ge=1, le=1024, default=0, description="Index of the downstream in tree.")
class CsfFabricConnector(BaseModel):
    """
    Child table model for fabric-connector.
    
    Fabric connector configuration.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    serial: str | None = Field(max_length=19, default="", description="Serial.")    
    accprofile: str | None = Field(max_length=35, default="", description="Override access profile.")  # datasource: ['system.accprofile.name']    
    configuration_write_access: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable downstream device write access to configuration.")    
    vdom: list[Vdom] = Field(default=None, description="Virtual domains that the connector has access to. If none are set, the connector will only have access to the VDOM that it joins the Security Fabric through.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class CsfModel(BaseModel):
    """
    Pydantic model for system/csf configuration.
    
    Add this FortiGate to a Security Fabric or set up a new Security Fabric on this FortiGate.
    
    Validation Rules:        - status: pattern=        - uid: max_length=35 pattern=        - upstream: max_length=255 pattern=        - source_ip: pattern=        - upstream_interface_select_method: pattern=        - upstream_interface: max_length=15 pattern=        - upstream_port: min=1 max=65535 pattern=        - group_name: max_length=35 pattern=        - group_password: max_length=128 pattern=        - accept_auth_by_cert: pattern=        - log_unification: pattern=        - authorization_request_type: pattern=        - certificate: max_length=35 pattern=        - fabric_workers: min=1 max=4 pattern=        - downstream_access: pattern=        - legacy_authentication: pattern=        - downstream_accprofile: max_length=35 pattern=        - configuration_sync: pattern=        - fabric_object_unification: pattern=        - saml_configuration_sync: pattern=        - trusted_list: pattern=        - fabric_connector: pattern=        - forticloud_account_enforcement: pattern=        - file_mgmt: pattern=        - file_quota: min=0 max=4294967295 pattern=        - file_quota_warning: min=1 max=99 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    status: Literal["enable", "disable"] = Field(default="disable", description="Enable/disable Security Fabric.")    
    uid: str | None = Field(max_length=35, default="", description="Unique ID of the current CSF node")    
    upstream: str | None = Field(max_length=255, default="", description="IP/FQDN of the FortiGate upstream from this FortiGate in the Security Fabric.")    
    source_ip: str | None = Field(default="0.0.0.0", description="Source IP address for communication with the upstream FortiGate.")    
    upstream_interface_select_method: Literal["auto", "sdwan", "specify"] | None = Field(default="auto", description="Specify how to select outgoing interface to reach server.")    
    upstream_interface: str = Field(max_length=15, default="", description="Specify outgoing interface to reach server.")  # datasource: ['system.interface.name']    
    upstream_port: int | None = Field(ge=1, le=65535, default=8013, description="The port number to use to communicate with the FortiGate upstream from this FortiGate in the Security Fabric (default = 8013).")    
    group_name: str | None = Field(max_length=35, default="", description="Security Fabric group name. All FortiGates in a Security Fabric must have the same group name.")    
    group_password: Any = Field(max_length=128, default=None, description="Security Fabric group password. For legacy authentication, fabric members must have the same group password.")    
    accept_auth_by_cert: Literal["disable", "enable"] | None = Field(default="enable", description="Accept connections with unknown certificates and ask admin for approval.")    
    log_unification: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable broadcast of discovery messages for log unification.")    
    authorization_request_type: Literal["serial", "certificate"] | None = Field(default="serial", description="Authorization request type.")    
    certificate: str | None = Field(max_length=35, default="", description="Certificate.")  # datasource: ['certificate.local.name']    
    fabric_workers: int | None = Field(ge=1, le=4, default=2, description="Number of worker processes for Security Fabric daemon.")    
    downstream_access: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable downstream device access to this device's configuration and data.")    
    legacy_authentication: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable legacy authentication.")    
    downstream_accprofile: str = Field(max_length=35, default="", description="Default access profile for requests from downstream devices.")  # datasource: ['system.accprofile.name']    
    configuration_sync: Literal["default", "local"] = Field(default="default", description="Configuration sync mode.")    
    fabric_object_unification: Literal["default", "local"] | None = Field(default="default", description="Fabric CMDB Object Unification.")    
    saml_configuration_sync: Literal["default", "local"] | None = Field(default="default", description="SAML setting configuration synchronization.")    
    trusted_list: list[TrustedList] = Field(default=None, description="Pre-authorized and blocked security fabric nodes.")    
    fabric_connector: list[FabricConnector] = Field(default=None, description="Fabric connector configuration.")    
    forticloud_account_enforcement: Literal["enable", "disable"] | None = Field(default="enable", description="Fabric FortiCloud account unification.")    
    file_mgmt: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable Security Fabric daemon file management.")    
    file_quota: int | None = Field(ge=0, le=4294967295, default=0, description="Maximum amount of memory that can be used by the daemon files (in bytes).")    
    file_quota_warning: int | None = Field(ge=1, le=99, default=90, description="Warn when the set percentage of quota has been used.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('upstream_interface')
    @classmethod
    def validate_upstream_interface(cls, v: Any) -> Any:
        """
        Validate upstream_interface field.
        
        Datasource: ['system.interface.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('certificate')
    @classmethod
    def validate_certificate(cls, v: Any) -> Any:
        """
        Validate certificate field.
        
        Datasource: ['certificate.local.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('downstream_accprofile')
    @classmethod
    def validate_downstream_accprofile(cls, v: Any) -> Any:
        """
        Validate downstream_accprofile field.
        
        Datasource: ['system.accprofile.name']
        
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
    "CsfModel",    "CsfTrustedList",    "CsfFabricConnector",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:35.274442Z
# ============================================================================