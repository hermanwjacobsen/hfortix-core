"""
Pydantic Models for CMDB - firewall/sniffer

Runtime validation models for firewall/sniffer configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.firewall.sniffer import 
    >>>
    >>> # Create with validation
    >>> obj = (
    ...     id=1,
    ...     name="example",
    ... )
    >>>
    >>> # Validation happens automatically
    >>> # ValidationError raised if constraints violated
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from uuid import UUID

# ============================================================================
# Child Table Models
# ============================================================================

class SnifferIpThreatfeed(BaseModel):
    """
    Child table model for ip-threatfeed.
    
    Name of an existing IP threat feed.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Threat feed name.")  # datasource: ['system.external-resource.name']
class SnifferAnomaly(BaseModel):
    """
    Child table model for anomaly.
    
    Configuration method to edit Denial of Service (DoS) anomaly settings.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=63, default="", description="Anomaly name.")    
    status: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable this anomaly.")    
    log: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable anomaly logging.")    
    action: Literal["pass", "block"] | None = Field(default="pass", description="Action taken when the threshold is reached.")    
    quarantine: Literal["none", "attacker"] | None = Field(default="none", description="Quarantine method.")    
    quarantine_expiry: str | None = Field(default="5m", description="Duration of quarantine. (Format ###d##h##m, minimum 1m, maximum 364d23h59m, default = 5m). Requires quarantine set to attacker.")    
    quarantine_log: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable quarantine logging.")    
    threshold: int | None = Field(ge=1, le=2147483647, default=0, description="Anomaly threshold. Number of detected instances (packets per second or concurrent session number) that triggers the anomaly action.")    
    threshold(default): int | None = Field(ge=0, le=4294967295, default=0, description="Number of detected instances (packets per second or concurrent session number) which triggers action (1 - 2147483647, default = 1000). Note that each anomaly has a different threshold value assigned to it.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class SnifferModel(BaseModel):
    """
    Pydantic model for firewall/sniffer configuration.
    
    Configure sniffer.
    
    Validation Rules:        - id: min=0 max=9999 pattern=        - uuid: pattern=        - status: pattern=        - logtraffic: pattern=        - ipv6: pattern=        - non_ip: pattern=        - interface: max_length=35 pattern=        - host: max_length=63 pattern=        - port: max_length=63 pattern=        - protocol: max_length=63 pattern=        - vlan: max_length=63 pattern=        - application_list_status: pattern=        - application_list: max_length=47 pattern=        - ips_sensor_status: pattern=        - ips_sensor: max_length=47 pattern=        - dsri: pattern=        - av_profile_status: pattern=        - av_profile: max_length=47 pattern=        - webfilter_profile_status: pattern=        - webfilter_profile: max_length=47 pattern=        - emailfilter_profile_status: pattern=        - emailfilter_profile: max_length=47 pattern=        - dlp_profile_status: pattern=        - dlp_profile: max_length=47 pattern=        - ip_threatfeed_status: pattern=        - ip_threatfeed: pattern=        - file_filter_profile_status: pattern=        - file_filter_profile: max_length=47 pattern=        - ips_dos_status: pattern=        - anomaly: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    id: int | None = Field(ge=0, le=9999, default=0, description="Sniffer ID (0 - 9999).")    
    uuid: str | None = Field(default="00000000-0000-0000-0000-000000000000", description="Universally Unique Identifier (UUID; automatically assigned but can be manually reset).")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable the active status of the sniffer.")    
    logtraffic: Literal["all", "utm", "disable"] | None = Field(default="utm", description="Either log all sessions, only sessions that have a security profile applied, or disable all logging for this policy.")    
    ipv6: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable sniffing IPv6 packets.")    
    non_ip: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable sniffing non-IP packets.")    
    interface: str | None = Field(max_length=35, default="", description="Interface name that traffic sniffing will take place on.")  # datasource: ['system.interface.name']    
    host: str | None = Field(max_length=63, default="", description="Hosts to filter for in sniffer traffic (Format examples: 1.1.1.1, 2.2.2.0/24, 3.3.3.3/255.255.255.0, 4.4.4.0-4.4.4.240).")    
    port: str | None = Field(max_length=63, default="", description="Ports to sniff (Format examples: 10, :20, 30:40, 50-, 100-200).")    
    protocol: str | None = Field(max_length=63, default="", description="Integer value for the protocol type as defined by IANA (0 - 255).")    
    vlan: str | None = Field(max_length=63, default="", description="List of VLANs to sniff.")    
    application_list_status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable application control profile.")    
    application_list: str = Field(max_length=47, default="", description="Name of an existing application list.")  # datasource: ['application.list.name']    
    ips_sensor_status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable IPS sensor.")    
    ips_sensor: str = Field(max_length=47, default="", description="Name of an existing IPS sensor.")  # datasource: ['ips.sensor.name']    
    dsri: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable DSRI.")    
    av_profile_status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable antivirus profile.")    
    av_profile: str = Field(max_length=47, default="", description="Name of an existing antivirus profile.")  # datasource: ['antivirus.profile.name']    
    webfilter_profile_status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable web filter profile.")    
    webfilter_profile: str = Field(max_length=47, default="", description="Name of an existing web filter profile.")  # datasource: ['webfilter.profile.name']    
    emailfilter_profile_status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable emailfilter.")    
    emailfilter_profile: str = Field(max_length=47, default="", description="Name of an existing email filter profile.")  # datasource: ['emailfilter.profile.name']    
    dlp_profile_status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable DLP profile.")    
    dlp_profile: str = Field(max_length=47, default="", description="Name of an existing DLP profile.")  # datasource: ['dlp.profile.name']    
    ip_threatfeed_status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable IP threat feed.")    
    ip_threatfeed: list[IpThreatfeed] = Field(default=None, description="Name of an existing IP threat feed.")    
    file_filter_profile_status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable file filter.")    
    file_filter_profile: str = Field(max_length=47, default="", description="Name of an existing file-filter profile.")  # datasource: ['file-filter.profile.name']    
    ips_dos_status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable IPS DoS anomaly detection.")    
    anomaly: list[Anomaly] = Field(default=None, description="Configuration method to edit Denial of Service (DoS) anomaly settings.")    
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
    @field_validator('application_list')
    @classmethod
    def validate_application_list(cls, v: Any) -> Any:
        """
        Validate application_list field.
        
        Datasource: ['application.list.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('ips_sensor')
    @classmethod
    def validate_ips_sensor(cls, v: Any) -> Any:
        """
        Validate ips_sensor field.
        
        Datasource: ['ips.sensor.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('av_profile')
    @classmethod
    def validate_av_profile(cls, v: Any) -> Any:
        """
        Validate av_profile field.
        
        Datasource: ['antivirus.profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('webfilter_profile')
    @classmethod
    def validate_webfilter_profile(cls, v: Any) -> Any:
        """
        Validate webfilter_profile field.
        
        Datasource: ['webfilter.profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('emailfilter_profile')
    @classmethod
    def validate_emailfilter_profile(cls, v: Any) -> Any:
        """
        Validate emailfilter_profile field.
        
        Datasource: ['emailfilter.profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('dlp_profile')
    @classmethod
    def validate_dlp_profile(cls, v: Any) -> Any:
        """
        Validate dlp_profile field.
        
        Datasource: ['dlp.profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('file_filter_profile')
    @classmethod
    def validate_file_filter_profile(cls, v: Any) -> Any:
        """
        Validate file_filter_profile field.
        
        Datasource: ['file-filter.profile.name']
        
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
    "SnifferModel",    "SnifferIpThreatfeed",    "SnifferAnomaly",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:33.205691Z
# ============================================================================