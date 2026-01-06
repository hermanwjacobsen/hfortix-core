"""
Pydantic Models for CMDB - log/fortianalyzer3/setting

Runtime validation models for log/fortianalyzer3/setting configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.log.fortianalyzer3.setting import 
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
# Child Table Models
# ============================================================================

class SettingSerial(BaseModel):
    """
    Child table model for serial.
    
    Serial numbers of the FortiAnalyzer.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Serial Number.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class SettingSsl_min_proto_versionEnum(str, Enum):
    """Allowed values for ssl_min_proto_version field."""
    DEFAULT = "default"    SSLV3 = "SSLv3"    TLSV1 = "TLSv1"    TLSV1_1 = "TLSv1-1"    TLSV1_2 = "TLSv1-2"    TLSV1_3 = "TLSv1-3"
class SettingUpload_optionEnum(str, Enum):
    """Allowed values for upload_option field."""
    STORE_AND_UPLOAD = "store-and-upload"    REALTIME = "realtime"    1_MINUTE = "1-minute"    5_MINUTE = "5-minute"

# ============================================================================
# Main Model
# ============================================================================

class SettingModel(BaseModel):
    """
    Pydantic model for log/fortianalyzer3/setting configuration.
    
    Global FortiAnalyzer settings.
    
    Validation Rules:        - status: pattern=        - ips_archive: pattern=        - server: max_length=127 pattern=        - alt_server: max_length=127 pattern=        - fallback_to_primary: pattern=        - certificate_verification: pattern=        - serial: pattern=        - server_cert_ca: max_length=79 pattern=        - preshared_key: max_length=63 pattern=        - access_config: pattern=        - hmac_algorithm: pattern=        - enc_algorithm: pattern=        - ssl_min_proto_version: pattern=        - conn_timeout: min=1 max=3600 pattern=        - monitor_keepalive_period: min=1 max=120 pattern=        - monitor_failure_retry_period: min=1 max=86400 pattern=        - certificate: max_length=35 pattern=        - source_ip: max_length=63 pattern=        - upload_option: pattern=        - upload_interval: pattern=        - upload_day: pattern=        - upload_time: pattern=        - reliable: pattern=        - priority: pattern=        - max_log_rate: min=0 max=100000 pattern=        - interface_select_method: pattern=        - interface: max_length=15 pattern=        - vrf_select: min=0 max=511 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable logging to FortiAnalyzer.")    
    ips_archive: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable IPS packet archive logging.")    
    server: str = Field(max_length=127, default="", description="The remote FortiAnalyzer.")    
    alt_server: str | None = Field(max_length=127, default="", description="Alternate FortiAnalyzer.")    
    fallback_to_primary: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable this FortiGate unit to fallback to the primary FortiAnalyzer when it is available.")    
    certificate_verification: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable identity verification of FortiAnalyzer by use of certificate.")    
    serial: list[Serial] = Field(default=None, description="Serial numbers of the FortiAnalyzer.")    
    server_cert_ca: str | None = Field(max_length=79, default="", description="Mandatory CA on FortiGate in certificate chain of server.")  # datasource: ['certificate.ca.name', 'vpn.certificate.ca.name']    
    preshared_key: str | None = Field(max_length=63, default="", description="Preshared-key used for auto-authorization on FortiAnalyzer.")    
    access_config: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable FortiAnalyzer access to configuration and data.")    
    hmac_algorithm: Literal["sha256"] | None = Field(default="sha256", description="OFTP login hash algorithm.")    
    enc_algorithm: Literal["high-medium", "high", "low"] | None = Field(default="high", description="Configure the level of SSL protection for secure communication with FortiAnalyzer.")    
    ssl_min_proto_version: SslMinProtoVersionEnum | None = Field(default="default", description="Minimum supported protocol version for SSL/TLS connections (default is to follow system global setting).")    
    conn_timeout: int | None = Field(ge=1, le=3600, default=10, description="FortiAnalyzer connection time-out in seconds (for status and log buffer).")    
    monitor_keepalive_period: int | None = Field(ge=1, le=120, default=5, description="Time between OFTP keepalives in seconds (for status and log buffer).")    
    monitor_failure_retry_period: int | None = Field(ge=1, le=86400, default=5, description="Time between FortiAnalyzer connection retries in seconds (for status and log buffer).")    
    certificate: str | None = Field(max_length=35, default="", description="Certificate used to communicate with FortiAnalyzer.")  # datasource: ['certificate.local.name']    
    source_ip: str | None = Field(max_length=63, default="", description="Source IPv4 or IPv6 address used to communicate with FortiAnalyzer.")    
    upload_option: UploadOptionEnum | None = Field(default="5-minute", description="Enable/disable logging to hard disk and then uploading to FortiAnalyzer.")    
    upload_interval: Literal["daily", "weekly", "monthly"] | None = Field(default="daily", description="Frequency to upload log files to FortiAnalyzer.")    
    upload_day: str | None = Field(default="", description="Day of week (month) to upload logs.")    
    upload_time: str | None = Field(default="", description="Time to upload logs (hh:mm).")    
    reliable: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable reliable logging to FortiAnalyzer.")    
    priority: Literal["default", "low"] | None = Field(default="default", description="Set log transmission priority.")    
    max_log_rate: int | None = Field(ge=0, le=100000, default=0, description="FortiAnalyzer maximum log rate in MBps (0 = unlimited).")    
    interface_select_method: Literal["auto", "sdwan", "specify"] | None = Field(default="auto", description="Specify how to select outgoing interface to reach server.")    
    interface: str = Field(max_length=15, default="", description="Specify outgoing interface to reach server.")  # datasource: ['system.interface.name']    
    vrf_select: int | None = Field(ge=0, le=511, default=0, description="VRF ID used for connection to server.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('server_cert_ca')
    @classmethod
    def validate_server_cert_ca(cls, v: Any) -> Any:
        """
        Validate server_cert_ca field.
        
        Datasource: ['certificate.ca.name', 'vpn.certificate.ca.name']
        
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
    "SettingModel",    "SettingSerial",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:35.158765Z
# ============================================================================