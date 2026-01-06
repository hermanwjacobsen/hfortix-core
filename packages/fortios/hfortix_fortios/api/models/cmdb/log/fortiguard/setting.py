"""
Pydantic Models for CMDB - log/fortiguard/setting

Runtime validation models for log/fortiguard/setting configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.log.fortiguard.setting import 
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
from enum import Enum

# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class SettingUpload_optionEnum(str, Enum):
    """Allowed values for upload_option field."""
    STORE_AND_UPLOAD = "store-and-upload"    REALTIME = "realtime"    1_MINUTE = "1-minute"    5_MINUTE = "5-minute"
class SettingSsl_min_proto_versionEnum(str, Enum):
    """Allowed values for ssl_min_proto_version field."""
    DEFAULT = "default"    SSLV3 = "SSLv3"    TLSV1 = "TLSv1"    TLSV1_1 = "TLSv1-1"    TLSV1_2 = "TLSv1-2"    TLSV1_3 = "TLSv1-3"

# ============================================================================
# Main Model
# ============================================================================

class SettingModel(BaseModel):
    """
    Pydantic model for log/fortiguard/setting configuration.
    
    Configure logging to FortiCloud.
    
    Validation Rules:        - status: pattern=        - upload_option: pattern=        - upload_interval: pattern=        - upload_day: pattern=        - upload_time: pattern=        - priority: pattern=        - max_log_rate: min=0 max=100000 pattern=        - access_config: pattern=        - enc_algorithm: pattern=        - ssl_min_proto_version: pattern=        - conn_timeout: min=1 max=3600 pattern=        - source_ip: pattern=        - interface_select_method: pattern=        - interface: max_length=15 pattern=        - vrf_select: min=0 max=511 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable logging to FortiCloud.")    
    upload_option: UploadOptionEnum | None = Field(default="5-minute", description="Configure how log messages are sent to FortiCloud.")    
    upload_interval: Literal["daily", "weekly", "monthly"] | None = Field(default="daily", description="Frequency of uploading log files to FortiCloud.")    
    upload_day: str | None = Field(default="", description="Day of week to roll logs.")    
    upload_time: str | None = Field(default="", description="Time of day to roll logs (hh:mm).")    
    priority: Literal["default", "low"] | None = Field(default="default", description="Set log transmission priority.")    
    max_log_rate: int | None = Field(ge=0, le=100000, default=0, description="FortiCloud maximum log rate in MBps (0 = unlimited).")    
    access_config: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable FortiCloud access to configuration and data.")    
    enc_algorithm: Literal["high-medium", "high", "low"] | None = Field(default="high", description="Configure the level of SSL protection for secure communication with FortiCloud.")    
    ssl_min_proto_version: SslMinProtoVersionEnum | None = Field(default="default", description="Minimum supported protocol version for SSL/TLS connections (default is to follow system global setting).")    
    conn_timeout: int | None = Field(ge=1, le=3600, default=10, description="FortiGate Cloud connection timeout in seconds.")    
    source_ip: str | None = Field(default="0.0.0.0", description="Source IP address used to connect FortiCloud.")    
    interface_select_method: Literal["auto", "sdwan", "specify"] | None = Field(default="auto", description="Specify how to select outgoing interface to reach server.")    
    interface: str = Field(max_length=15, default="", description="Specify outgoing interface to reach server.")  # datasource: ['system.interface.name']    
    vrf_select: int | None = Field(ge=0, le=511, default=0, description="VRF ID used for connection to server.")    
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
    "SettingModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:35.223527Z
# ============================================================================