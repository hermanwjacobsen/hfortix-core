"""
Pydantic Models for CMDB - system/standalone_cluster

Runtime validation models for system/standalone_cluster configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.system.standalone_cluster import 
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

class StandaloneClusterClusterPeer(BaseModel):
    """
    Child table model for cluster-peer.
    
    Configure FortiGate Session Life Support Protocol (FGSP) session synchronization.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    sync_id: int | None = Field(ge=0, le=4294967295, default=0, description="Sync ID.")    
    peervd: str | None = Field(max_length=31, default="root", description="VDOM that contains the session synchronization link interface on the peer unit. Usually both peers would have the same peervd.")  # datasource: ['system.vdom.name']    
    peerip: str | None = Field(default="0.0.0.0", description="IP address of the interface on the peer unit that is used for the session synchronization link.")    
    syncvd: list[Syncvd] = Field(default=None, description="Sessions from these VDOMs are synchronized using this session synchronization configuration.")    
    down_intfs_before_sess_sync: list[DownIntfsBeforeSessSync] = Field(default=None, description="List of interfaces to be turned down before session synchronization is complete.")    
    hb_interval: int | None = Field(ge=1, le=20, default=2, description="Heartbeat interval (1 - 20 (100*ms). Increase to reduce false positives.")    
    hb_lost_threshold: int | None = Field(ge=1, le=60, default=10, description="Lost heartbeat threshold (1 - 60). Increase to reduce false positives.")    
    ipsec_tunnel_sync: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable IPsec tunnel synchronization.")    
    secondary_add_ipsec_routes: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable IKE route announcement on the backup unit.")    
    session_sync_filter: list[SessionSyncFilter] = Field(default=None, description="Add one or more filters if you only want to synchronize some sessions. Use the filter to configure the types of sessions to synchronize.")
class StandaloneClusterMonitorInterface(BaseModel):
    """
    Child table model for monitor-interface.
    
    Configure a list of interfaces on which to monitor itself. Monitoring is performed on the status of the interface.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Interface name.")  # datasource: ['system.interface.name']
class StandaloneClusterPingsvrMonitorInterface(BaseModel):
    """
    Child table model for pingsvr-monitor-interface.
    
    List of pingsvr monitor interface to check for remote IP monitoring.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Interface name.")  # datasource: ['system.interface.name']
class StandaloneClusterMonitorPrefix(BaseModel):
    """
    Child table model for monitor-prefix.
    
    Configure a list of routing prefixes to monitor.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=0, le=4294967295, default=0, description="ID.")    
    vdom: str = Field(max_length=31, default="", description="VDOM name.")  # datasource: ['system.vdom.name']    
    vrf: int | None = Field(ge=0, le=511, default=0, description="VRF ID.")    
    prefix: Any = Field(default="0.0.0.0 0.0.0.0", description="Prefix.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class StandaloneClusterModel(BaseModel):
    """
    Pydantic model for system/standalone_cluster configuration.
    
    Configure FortiGate Session Life Support Protocol (FGSP) cluster attributes.
    
    Validation Rules:        - standalone_group_id: min=0 max=255 pattern=        - group_member_id: min=0 max=15 pattern=        - layer2_connection: pattern=        - session_sync_dev: pattern=        - encryption: pattern=        - psksecret: pattern=        - asymmetric_traffic_control: pattern=        - cluster_peer: pattern=        - monitor_interface: pattern=        - pingsvr_monitor_interface: pattern=        - monitor_prefix: pattern=        - helper_traffic_bounce: pattern=        - utm_traffic_bounce: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    standalone_group_id: int | None = Field(ge=0, le=255, default=0, description="Cluster group ID (0 - 255). Must be the same for all members.")    
    group_member_id: int | None = Field(ge=0, le=15, default=0, description="Cluster member ID (0 - 15).")    
    layer2_connection: Literal["available", "unavailable"] | None = Field(default="unavailable", description="Indicate whether layer 2 connections are present among FGSP members.")    
    session_sync_dev: list[SessionSyncDev] = Field(default="", description="Offload session-sync process to kernel and sync sessions using connected interface(s) directly.")  # datasource: ['system.interface.name']    
    encryption: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable encryption when synchronizing sessions.")    
    psksecret: Any = Field(description="Pre-shared secret for session synchronization (ASCII string or hexadecimal encoded with a leading 0x).")    
    asymmetric_traffic_control: Literal["cps-preferred", "strict-anti-replay"] | None = Field(default="cps-preferred", description="Asymmetric traffic control mode.")    
    cluster_peer: list[ClusterPeer] = Field(default=None, description="Configure FortiGate Session Life Support Protocol (FGSP) session synchronization.")    
    monitor_interface: list[MonitorInterface] = Field(default=None, description="Configure a list of interfaces on which to monitor itself. Monitoring is performed on the status of the interface.")    
    pingsvr_monitor_interface: list[PingsvrMonitorInterface] = Field(default=None, description="List of pingsvr monitor interface to check for remote IP monitoring.")    
    monitor_prefix: list[MonitorPrefix] = Field(default=None, description="Configure a list of routing prefixes to monitor.")    
    helper_traffic_bounce: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable helper related traffic bounce.")    
    utm_traffic_bounce: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable UTM related traffic bounce.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('session_sync_dev')
    @classmethod
    def validate_session_sync_dev(cls, v: Any) -> Any:
        """
        Validate session_sync_dev field.
        
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
    "StandaloneClusterModel",    "StandaloneClusterClusterPeer",    "StandaloneClusterMonitorInterface",    "StandaloneClusterPingsvrMonitorInterface",    "StandaloneClusterMonitorPrefix",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:35.243686Z
# ============================================================================