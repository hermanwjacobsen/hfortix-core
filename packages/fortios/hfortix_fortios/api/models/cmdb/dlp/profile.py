"""
Pydantic Models for CMDB - dlp/profile

Runtime validation models for dlp/profile configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.dlp.profile import 
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

class ProfileRule(BaseModel):
    """
    Child table model for rule.
    
    Set up DLP rules for this profile.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="ID.")    
    name: str | None = Field(max_length=35, default="", description="Filter name.")    
    severity: SeverityEnum | None = Field(default="medium", description="Select the severity or threat level that matches this filter.")    
    type: Literal["file", "message"] | None = Field(default="file", description="Select whether to check the content of messages (an email message) or files (downloaded files or email attachments).")    
    proto: list[Proto] = Field(default="", description="Check messages or files over one or more of these protocols.")    
    filter_by: FilterByEnum | None = Field(default="none", description="Select the type of content to match.")    
    file_size: int | None = Field(ge=0, le=4193280, default=0, description="Match files greater than or equal to this size (KB).")    
    sensitivity: list[Sensitivity] = Field(description="Select a DLP file pattern sensitivity to match.")    
    match_percentage: int | None = Field(ge=1, le=100, default=10, description="Percentage of fingerprints in the fingerprint databases designated with the selected sensitivity to match.")    
    file_type: int | None = Field(ge=0, le=4294967295, default=0, description="Select the number of a DLP file pattern table to match.")  # datasource: ['dlp.filepattern.id']    
    sensor: list[Sensor] = Field(description="Select DLP sensors.")    
    label: str = Field(max_length=35, default="", description="Select DLP label.")  # datasource: ['dlp.label.name']    
    archive: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable DLP archiving.")    
    action: ActionEnum | None = Field(default="allow", description="Action to take with content that this DLP profile matches.")    
    expiry: str | None = Field(default="5m", description="Quarantine duration in days, hours, minutes (format = dddhhmm).")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class ProfileFull_archive_protoEnum(str, Enum):
    """Allowed values for full_archive_proto field."""
    SMTP = "smtp"    POP3 = "pop3"    IMAP = "imap"    HTTP_GET = "http-get"    HTTP_POST = "http-post"    FTP = "ftp"    NNTP = "nntp"    MAPI = "mapi"    SSH = "ssh"    CIFS = "cifs"
class ProfileSummary_protoEnum(str, Enum):
    """Allowed values for summary_proto field."""
    SMTP = "smtp"    POP3 = "pop3"    IMAP = "imap"    HTTP_GET = "http-get"    HTTP_POST = "http-post"    FTP = "ftp"    NNTP = "nntp"    MAPI = "mapi"    SSH = "ssh"    CIFS = "cifs"

# ============================================================================
# Main Model
# ============================================================================

class ProfileModel(BaseModel):
    """
    Pydantic model for dlp/profile configuration.
    
    Configure DLP profiles.
    
    Validation Rules:        - name: max_length=47 pattern=        - comment: max_length=255 pattern=        - feature_set: pattern=        - replacemsg_group: max_length=35 pattern=        - rule: pattern=        - dlp_log: pattern=        - extended_log: pattern=        - nac_quar_log: pattern=        - full_archive_proto: pattern=        - summary_proto: pattern=        - fortidata_error_action: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str = Field(max_length=47, default="", description="Name of the DLP profile.")    
    comment: str | None = Field(max_length=255, default=None, description="Comment.")    
    feature_set: Literal["flow", "proxy"] | None = Field(default="flow", description="Flow/proxy feature set.")    
    replacemsg_group: str | None = Field(max_length=35, default="", description="Replacement message group used by this DLP profile.")  # datasource: ['system.replacemsg-group.name']    
    rule: list[Rule] = Field(default=None, description="Set up DLP rules for this profile.")    
    dlp_log: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable DLP logging.")    
    extended_log: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable extended logging for data loss prevention.")    
    nac_quar_log: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable NAC quarantine logging.")    
    full_archive_proto: list[FullArchiveProto] = Field(default="", description="Protocols to always content archive.")    
    summary_proto: list[SummaryProto] = Field(default="", description="Protocols to always log summary.")    
    fortidata_error_action: Literal["log-only", "block", "ignore"] | None = Field(default="block", description="Action to take if FortiData query fails.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('replacemsg_group')
    @classmethod
    def validate_replacemsg_group(cls, v: Any) -> Any:
        """
        Validate replacemsg_group field.
        
        Datasource: ['system.replacemsg-group.name']
        
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
    "ProfileModel",    "ProfileRule",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:35.640455Z
# ============================================================================