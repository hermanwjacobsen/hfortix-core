"""
Pydantic Models for CMDB - icap/profile

Runtime validation models for icap/profile configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.icap.profile import 
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

class ProfileIcapHeaders(BaseModel):
    """
    Child table model for icap-headers.
    
    Configure ICAP forwarded request headers.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="HTTP forwarded header ID.")    
    name: str | None = Field(max_length=79, default="", description="HTTP forwarded header name.")    
    content: str | None = Field(max_length=255, default="", description="HTTP header content.")    
    base64_encoding: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable use of base64 encoding of HTTP content.")
class ProfileRespmodForwardRules(BaseModel):
    """
    Child table model for respmod-forward-rules.
    
    ICAP response mode forward rules.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=63, default="", description="Address name.")    
    host: str = Field(max_length=79, default="", description="Address object for the host.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name', 'firewall.proxy-address.name']    
    header_group: list[HeaderGroup] = Field(default=None, description="HTTP header group.")    
    action: Literal["forward", "bypass"] | None = Field(default="forward", description="Action to be taken for ICAP server.")    
    http_resp_status_code: list[HttpRespStatusCode] = Field(default=None, description="HTTP response status code.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class ProfileMethodsEnum(str, Enum):
    """Allowed values for methods field."""
    DELETE = "delete"    GET = "get"    HEAD = "head"    OPTIONS = "options"    POST = "post"    PUT = "put"    TRACE = "trace"    CONNECT = "connect"    OTHER = "other"

# ============================================================================
# Main Model
# ============================================================================

class ProfileModel(BaseModel):
    """
    Pydantic model for icap/profile configuration.
    
    Configure ICAP profiles.
    
    Validation Rules:        - replacemsg_group: max_length=35 pattern=        - name: max_length=47 pattern=        - comment: max_length=255 pattern=        - request: pattern=        - response: pattern=        - file_transfer: pattern=        - streaming_content_bypass: pattern=        - ocr_only: pattern=        - 204_size_limit: min=1 max=10 pattern=        - 204_response: pattern=        - preview: pattern=        - preview_data_length: min=0 max=4096 pattern=        - request_server: max_length=63 pattern=        - response_server: max_length=63 pattern=        - file_transfer_server: max_length=63 pattern=        - request_failure: pattern=        - response_failure: pattern=        - file_transfer_failure: pattern=        - request_path: max_length=127 pattern=        - response_path: max_length=127 pattern=        - file_transfer_path: max_length=127 pattern=        - methods: pattern=        - response_req_hdr: pattern=        - respmod_default_action: pattern=        - icap_block_log: pattern=        - chunk_encap: pattern=        - extension_feature: pattern=        - scan_progress_interval: min=5 max=30 pattern=        - timeout: min=30 max=3600 pattern=        - icap_headers: pattern=        - respmod_forward_rules: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    replacemsg_group: str | None = Field(max_length=35, default="", description="Replacement message group.")  # datasource: ['system.replacemsg-group.name']    
    name: str | None = Field(max_length=47, default="", description="ICAP profile name.")    
    comment: str | None = Field(max_length=255, default=None, description="Comment.")    
    request: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable whether an HTTP request is passed to an ICAP server.")    
    response: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable whether an HTTP response is passed to an ICAP server.")    
    file_transfer: list[FileTransfer] = Field(default="", description="Configure the file transfer protocols to pass transferred files to an ICAP server as REQMOD.")    
    streaming_content_bypass: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable bypassing of ICAP server for streaming content.")    
    ocr_only: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable this FortiGate unit to submit only OCR interested content to the ICAP server.")    
    204_size_limit: int | None = Field(ge=1, le=10, default=1, description="204 response size limit to be saved by ICAP client in megabytes (1 - 10, default = 1 MB).")    
    204_response: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable allowance of 204 response from ICAP server.")    
    preview: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable preview of data to ICAP server.")    
    preview_data_length: int | None = Field(ge=0, le=4096, default=0, description="Preview data length to be sent to ICAP server.")    
    request_server: str = Field(max_length=63, default="", description="ICAP server to use for an HTTP request.")  # datasource: ['icap.server.name', 'icap.server-group.name']    
    response_server: str = Field(max_length=63, default="", description="ICAP server to use for an HTTP response.")  # datasource: ['icap.server.name', 'icap.server-group.name']    
    file_transfer_server: str = Field(max_length=63, default="", description="ICAP server to use for a file transfer.")  # datasource: ['icap.server.name', 'icap.server-group.name']    
    request_failure: Literal["error", "bypass"] | None = Field(default="error", description="Action to take if the ICAP server cannot be contacted when processing an HTTP request.")    
    response_failure: Literal["error", "bypass"] | None = Field(default="error", description="Action to take if the ICAP server cannot be contacted when processing an HTTP response.")    
    file_transfer_failure: Literal["error", "bypass"] | None = Field(default="error", description="Action to take if the ICAP server cannot be contacted when processing a file transfer.")    
    request_path: str | None = Field(max_length=127, default="", description="Path component of the ICAP URI that identifies the HTTP request processing service.")    
    response_path: str | None = Field(max_length=127, default="", description="Path component of the ICAP URI that identifies the HTTP response processing service.")    
    file_transfer_path: str | None = Field(max_length=127, default="", description="Path component of the ICAP URI that identifies the file transfer processing service.")    
    methods: list[Methods] = Field(default="delete get head options post put trace connect other", description="The allowed HTTP methods that will be sent to ICAP server for further processing.")    
    response_req_hdr: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable addition of req-hdr for ICAP response modification (respmod) processing.")    
    respmod_default_action: Literal["forward", "bypass"] | None = Field(default="forward", description="Default action to ICAP response modification (respmod) processing.")    
    icap_block_log: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable UTM log when infection found (default = disable).")    
    chunk_encap: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable chunked encapsulation (default = disable).")    
    extension_feature: list[ExtensionFeature] = Field(default="", description="Enable/disable ICAP extension features.")    
    scan_progress_interval: int | None = Field(ge=5, le=30, default=10, description="Scan progress interval value.")    
    timeout: int | None = Field(ge=30, le=3600, default=30, description="Time (in seconds) that ICAP client waits for the response from ICAP server.")    
    icap_headers: list[IcapHeaders] = Field(default=None, description="Configure ICAP forwarded request headers.")    
    respmod_forward_rules: list[RespmodForwardRules] = Field(default=None, description="ICAP response mode forward rules.")    
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
    @field_validator('request_server')
    @classmethod
    def validate_request_server(cls, v: Any) -> Any:
        """
        Validate request_server field.
        
        Datasource: ['icap.server.name', 'icap.server-group.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('response_server')
    @classmethod
    def validate_response_server(cls, v: Any) -> Any:
        """
        Validate response_server field.
        
        Datasource: ['icap.server.name', 'icap.server-group.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('file_transfer_server')
    @classmethod
    def validate_file_transfer_server(cls, v: Any) -> Any:
        """
        Validate file_transfer_server field.
        
        Datasource: ['icap.server.name', 'icap.server-group.name']
        
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
    "ProfileModel",    "ProfileIcapHeaders",    "ProfileRespmodForwardRules",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:33.861174Z
# ============================================================================