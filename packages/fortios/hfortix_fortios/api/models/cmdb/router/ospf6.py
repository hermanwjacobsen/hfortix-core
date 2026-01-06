"""
Pydantic Models for CMDB - router/ospf6

Runtime validation models for router/ospf6 configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.router.ospf6 import 
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

class Ospf6Area(BaseModel):
    """
    Child table model for area.
    
    OSPF6 area configuration.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: str | None = Field(default="0.0.0.0", description="Area entry IP address.")    
    default_cost: int | None = Field(ge=0, le=16777215, default=10, description="Summary default cost of stub or NSSA area.")    
    nssa_translator_role: Literal["candidate", "never", "always"] | None = Field(default="candidate", description="NSSA translator role type.")    
    stub_type: Literal["no-summary", "summary"] | None = Field(default="summary", description="Stub summary setting.")    
    type: Literal["regular", "nssa", "stub"] | None = Field(default="regular", description="Area type setting.")    
    nssa_default_information_originate: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable originate type 7 default into NSSA area.")    
    nssa_default_information_originate_metric: int | None = Field(ge=0, le=16777214, default=10, description="OSPFv3 default metric.")    
    nssa_default_information_originate_metric_type: Literal["1", "2"] | None = Field(default="2", description="OSPFv3 metric type for default routes.")    
    nssa_redistribution: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable redistribute into NSSA area.")    
    authentication: Literal["none", "ah", "esp"] | None = Field(default="none", description="Authentication mode.")    
    key_rollover_interval: int | None = Field(ge=300, le=216000, default=300, description="Key roll-over interval.")    
    ipsec_auth_alg: IpsecAuthAlgEnum | None = Field(default="md5", description="Authentication algorithm.")    
    ipsec_enc_alg: IpsecEncAlgEnum | None = Field(default="null", description="Encryption algorithm.")    
    ipsec_keys: list[IpsecKeys] = Field(default=None, description="IPsec authentication and encryption keys.")    
    range: list[Range] = Field(default=None, description="OSPF6 area range configuration.")    
    virtual_link: list[VirtualLink] = Field(default=None, description="OSPF6 virtual link configuration.")
class Ospf6Ospf6Interface(BaseModel):
    """
    Child table model for ospf6-interface.
    
    OSPF6 interface configuration.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=35, default="", description="Interface entry name.")    
    area_id: str = Field(default="0.0.0.0", description="A.B.C.D, in IPv4 address format.")    
    interface: str = Field(max_length=15, default="", description="Configuration interface name.")  # datasource: ['system.interface.name']    
    retransmit_interval: int | None = Field(ge=1, le=65535, default=5, description="Retransmit interval.")    
    transmit_delay: int | None = Field(ge=1, le=65535, default=1, description="Transmit delay.")    
    cost: int | None = Field(ge=0, le=65535, default=0, description="Cost of the interface, value range from 0 to 65535, 0 means auto-cost.")    
    priority: int | None = Field(ge=0, le=255, default=1, description="Priority.")    
    dead_interval: int | None = Field(ge=1, le=65535, default=0, description="Dead interval.")    
    hello_interval: int | None = Field(ge=1, le=65535, default=0, description="Hello interval.")    
    status: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable OSPF6 routing on this interface.")    
    network_type: NetworkTypeEnum | None = Field(default="broadcast", description="Network type.")    
    bfd: Literal["global", "enable", "disable"] | None = Field(default="global", description="Enable/disable Bidirectional Forwarding Detection (BFD).")    
    mtu: int | None = Field(ge=576, le=65535, default=0, description="MTU for OSPFv3 packets.")    
    mtu_ignore: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable ignoring MTU field in DBD packets.")    
    authentication: AuthenticationEnum | None = Field(default="area", description="Authentication mode.")    
    key_rollover_interval: int | None = Field(ge=300, le=216000, default=300, description="Key roll-over interval.")    
    ipsec_auth_alg: IpsecAuthAlgEnum | None = Field(default="md5", description="Authentication algorithm.")    
    ipsec_enc_alg: IpsecEncAlgEnum | None = Field(default="null", description="Encryption algorithm.")    
    ipsec_keys: list[IpsecKeys] = Field(default=None, description="IPsec authentication and encryption keys.")    
    neighbor: list[Neighbor] = Field(default=None, description="OSPFv3 neighbors are used when OSPFv3 runs on non-broadcast media.")
class Ospf6Redistribute(BaseModel):
    """
    Child table model for redistribute.
    
    Redistribute configuration.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=35, default="", description="Redistribute name.")    
    status: Literal["enable", "disable"] | None = Field(default="disable", description="Status.")    
    metric: int | None = Field(ge=0, le=16777214, default=0, description="Redistribute metric setting.")    
    routemap: str | None = Field(max_length=35, default="", description="Route map name.")  # datasource: ['router.route-map.name']    
    metric_type: Literal["1", "2"] | None = Field(default="2", description="Metric type.")
class Ospf6PassiveInterface(BaseModel):
    """
    Child table model for passive-interface.
    
    Passive interface configuration.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Passive interface name.")  # datasource: ['system.interface.name']
class Ospf6SummaryAddress(BaseModel):
    """
    Child table model for summary-address.
    
    IPv6 address summary configuration.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="Summary address entry ID.")    
    prefix6: str = Field(default="::/0", description="IPv6 prefix.")    
    advertise: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable advertise status.")    
    tag: int | None = Field(ge=0, le=4294967295, default=0, description="Tag value.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class Ospf6Model(BaseModel):
    """
    Pydantic model for router/ospf6 configuration.
    
    Configure IPv6 OSPF.
    
    Validation Rules:        - abr_type: pattern=        - auto_cost_ref_bandwidth: min=1 max=1000000 pattern=        - default_information_originate: pattern=        - log_neighbour_changes: pattern=        - default_information_metric: min=1 max=16777214 pattern=        - default_information_metric_type: pattern=        - default_information_route_map: max_length=35 pattern=        - default_metric: min=1 max=16777214 pattern=        - router_id: pattern=        - spf_timers: pattern=        - bfd: pattern=        - restart_mode: pattern=        - restart_period: min=1 max=3600 pattern=        - restart_on_topology_change: pattern=        - area: pattern=        - ospf6_interface: pattern=        - redistribute: pattern=        - passive_interface: pattern=        - summary_address: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    abr_type: Literal["cisco", "ibm", "standard"] | None = Field(default="standard", description="Area border router type.")    
    auto_cost_ref_bandwidth: int | None = Field(ge=1, le=1000000, default=1000, description="Reference bandwidth in terms of megabits per second.")    
    default_information_originate: Literal["enable", "always", "disable"] | None = Field(default="disable", description="Enable/disable generation of default route.")    
    log_neighbour_changes: Literal["enable", "disable"] | None = Field(default="enable", description="Log OSPFv3 neighbor changes.")    
    default_information_metric: int | None = Field(ge=1, le=16777214, default=10, description="Default information metric.")    
    default_information_metric_type: Literal["1", "2"] | None = Field(default="2", description="Default information metric type.")    
    default_information_route_map: str | None = Field(max_length=35, default="", description="Default information route map.")  # datasource: ['router.route-map.name']    
    default_metric: int | None = Field(ge=1, le=16777214, default=10, description="Default metric of redistribute routes.")    
    router_id: str = Field(default="0.0.0.0", description="A.B.C.D, in IPv4 address format.")    
    spf_timers: str | None = Field(default="", description="SPF calculation frequency.")    
    bfd: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable Bidirectional Forwarding Detection (BFD).")    
    restart_mode: Literal["none", "graceful-restart"] | None = Field(default="none", description="OSPFv3 restart mode (graceful or none).")    
    restart_period: int | None = Field(ge=1, le=3600, default=120, description="Graceful restart period in seconds.")    
    restart_on_topology_change: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable continuing graceful restart upon topology change.")    
    area: list[Area] = Field(default=None, description="OSPF6 area configuration.")    
    ospf6_interface: list[Ospf6Interface] = Field(default=None, description="OSPF6 interface configuration.")    
    redistribute: list[Redistribute] = Field(default=None, description="Redistribute configuration.")    
    passive_interface: list[PassiveInterface] = Field(default=None, description="Passive interface configuration.")    
    summary_address: list[SummaryAddress] = Field(default=None, description="IPv6 address summary configuration.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('default_information_route_map')
    @classmethod
    def validate_default_information_route_map(cls, v: Any) -> Any:
        """
        Validate default_information_route_map field.
        
        Datasource: ['router.route-map.name']
        
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
    "Ospf6Model",    "Ospf6Area",    "Ospf6Ospf6Interface",    "Ospf6Redistribute",    "Ospf6PassiveInterface",    "Ospf6SummaryAddress",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:34.260023Z
# ============================================================================