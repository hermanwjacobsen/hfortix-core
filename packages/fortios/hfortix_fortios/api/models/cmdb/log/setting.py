"""
Pydantic Models for CMDB - log/setting

Runtime validation models for log/setting configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.log.setting import 
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

class SettingCustomLogFields(BaseModel):
    """
    Child table model for custom-log-fields.
    
    Custom fields to append to all log messages.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    field_id: str | None = Field(max_length=35, default="", description="Custom log field.")  # datasource: ['log.custom-field.id']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class SettingModel(BaseModel):
    """
    Pydantic model for log/setting configuration.
    
    Configure general log settings.
    
    Validation Rules:        - resolve_ip: pattern=        - resolve_port: pattern=        - log_user_in_upper: pattern=        - fwpolicy_implicit_log: pattern=        - fwpolicy6_implicit_log: pattern=        - extended_log: pattern=        - local_in_allow: pattern=        - local_in_deny_unicast: pattern=        - local_in_deny_broadcast: pattern=        - local_in_policy_log: pattern=        - local_out: pattern=        - local_out_ioc_detection: pattern=        - daemon_log: pattern=        - neighbor_event: pattern=        - brief_traffic_format: pattern=        - user_anonymize: pattern=        - expolicy_implicit_log: pattern=        - log_policy_comment: pattern=        - faz_override: pattern=        - syslog_override: pattern=        - rest_api_set: pattern=        - rest_api_get: pattern=        - rest_api_performance: pattern=        - long_live_session_stat: pattern=        - extended_utm_log: pattern=        - zone_name: pattern=        - web_svc_perf: pattern=        - custom_log_fields: pattern=        - anonymization_hash: max_length=32 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    resolve_ip: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable adding resolved domain names to traffic logs if possible.")    
    resolve_port: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable adding resolved service names to traffic logs.")    
    log_user_in_upper: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable logs with user-in-upper.")    
    fwpolicy_implicit_log: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable implicit firewall policy logging.")    
    fwpolicy6_implicit_log: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable implicit firewall policy6 logging.")    
    extended_log: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable extended traffic logging.")    
    local_in_allow: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable local-in-allow logging.")    
    local_in_deny_unicast: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable local-in-deny-unicast logging.")    
    local_in_deny_broadcast: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable local-in-deny-broadcast logging.")    
    local_in_policy_log: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable local-in-policy logging.")    
    local_out: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable local-out logging.")    
    local_out_ioc_detection: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable local-out traffic IoC detection. Requires local-out to be enabled.")    
    daemon_log: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable daemon logging.")    
    neighbor_event: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable neighbor event logging.")    
    brief_traffic_format: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable brief format traffic logging.")    
    user_anonymize: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable anonymizing user names in log messages.")    
    expolicy_implicit_log: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable proxy firewall implicit policy logging.")    
    log_policy_comment: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable inserting policy comments into traffic logs.")    
    faz_override: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable override FortiAnalyzer settings.")    
    syslog_override: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable override Syslog settings.")    
    rest_api_set: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable REST API POST/PUT/DELETE request logging.")    
    rest_api_get: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable REST API GET request logging.")    
    rest_api_performance: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable REST API memory and performance stats in rest-api-get/set logs.")    
    long_live_session_stat: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable long-live-session statistics logging.")    
    extended_utm_log: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable extended UTM logging.")    
    zone_name: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable zone name logging.")    
    web_svc_perf: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable web-svc performance logging.")    
    custom_log_fields: list[CustomLogFields] = Field(default=None, description="Custom fields to append to all log messages.")    
    anonymization_hash: str | None = Field(max_length=32, default="", description="User name anonymization hash salt.")    
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
    "SettingModel",    "SettingCustomLogFields",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:32.841331Z
# ============================================================================