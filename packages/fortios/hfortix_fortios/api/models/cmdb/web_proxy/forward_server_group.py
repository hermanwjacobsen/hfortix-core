"""
Pydantic Models for CMDB - web_proxy/forward_server_group

Runtime validation models for web_proxy/forward_server_group configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.web_proxy.forward_server_group import 
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

# ============================================================================
# Child Table Models
# ============================================================================

class ForwardServerGroupServerList(BaseModel):
    """
    Child table model for server-list.
    
    Add web forward servers to a list to form a server group. Optionally assign weights to each server.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=63, default="", description="Forward server name.")  # datasource: ['web-proxy.forward-server.name']    
    weight: int | None = Field(ge=1, le=100, default=10, description="Optionally assign a weight of the forwarding server for weighted load balancing (1 - 100, default = 10).")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class ForwardServerGroupModel(BaseModel):
    """
    Pydantic model for web_proxy/forward_server_group configuration.
    
    Configure a forward server group consisting or multiple forward servers. Supports failover and load balancing.
    
    Validation Rules:        - name: max_length=63 pattern=        - affinity: pattern=        - ldb_method: pattern=        - group_down_option: pattern=        - server_list: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=63, default="", description="Configure a forward server group consisting one or multiple forward servers. Supports failover and load balancing.")    
    affinity: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable affinity, attaching a source-ip's traffic to the assigned forwarding server until the forward-server-affinity-timeout is reached (under web-proxy global).")    
    ldb_method: Literal["weighted", "least-session", "active-passive"] | None = Field(default="weighted", description="Load balance method: weighted or least-session.")    
    group_down_option: Literal["block", "pass"] | None = Field(default="block", description="Action to take when all of the servers in the forward server group are down: block sessions until at least one server is back up or pass sessions to their destination.")    
    server_list: list[ServerList] = Field(default=None, description="Add web forward servers to a list to form a server group. Optionally assign weights to each server.")    
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
    "ForwardServerGroupModel",    "ForwardServerGroupServerList",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:33.747655Z
# ============================================================================