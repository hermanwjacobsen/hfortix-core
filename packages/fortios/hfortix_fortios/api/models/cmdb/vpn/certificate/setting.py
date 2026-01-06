"""
Pydantic Models for CMDB - vpn/certificate/setting

Runtime validation models for vpn/certificate/setting configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.vpn.certificate.setting import 
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

class SettingCrlVerification(BaseModel):
    """
    Child table model for crl-verification.
    
    CRL verification options.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    expiry: Literal["ignore", "revoke"] | None = Field(default="ignore", description="CRL verification option when CRL is expired (default = ignore).")    
    leaf_crl_absence: Literal["ignore", "revoke"] | None = Field(default="ignore", description="CRL verification option when leaf CRL is absent (default = ignore).")    
    chain_crl_absence: Literal["ignore", "revoke"] | None = Field(default="ignore", description="CRL verification option when CRL of any certificate in chain is absent (default = ignore).")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class SettingSsl_min_proto_versionEnum(str, Enum):
    """Allowed values for ssl_min_proto_version field."""
    DEFAULT = "default"    SSLV3 = "SSLv3"    TLSV1 = "TLSv1"    TLSV1_1 = "TLSv1-1"    TLSV1_2 = "TLSv1-2"    TLSV1_3 = "TLSv1-3"

# ============================================================================
# Main Model
# ============================================================================

class SettingModel(BaseModel):
    """
    Pydantic model for vpn/certificate/setting configuration.
    
    VPN certificate setting.
    
    Validation Rules:        - ocsp_status: pattern=        - ocsp_option: pattern=        - proxy: max_length=127 pattern=        - proxy_port: min=1 max=65535 pattern=        - proxy_username: max_length=63 pattern=        - proxy_password: max_length=128 pattern=        - source_ip: max_length=63 pattern=        - ocsp_default_server: max_length=35 pattern=        - interface_select_method: pattern=        - interface: max_length=15 pattern=        - vrf_select: min=0 max=511 pattern=        - check_ca_cert: pattern=        - check_ca_chain: pattern=        - subject_match: pattern=        - subject_set: pattern=        - cn_match: pattern=        - cn_allow_multi: pattern=        - crl_verification: pattern=        - strict_ocsp_check: pattern=        - ssl_min_proto_version: pattern=        - cmp_save_extra_certs: pattern=        - cmp_key_usage_checking: pattern=        - cert_expire_warning: min=0 max=100 pattern=        - certname_rsa1024: max_length=35 pattern=        - certname_rsa2048: max_length=35 pattern=        - certname_rsa4096: max_length=35 pattern=        - certname_dsa1024: max_length=35 pattern=        - certname_dsa2048: max_length=35 pattern=        - certname_ecdsa256: max_length=35 pattern=        - certname_ecdsa384: max_length=35 pattern=        - certname_ecdsa521: max_length=35 pattern=        - certname_ed25519: max_length=35 pattern=        - certname_ed448: max_length=35 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    ocsp_status: Literal["enable", "mandatory", "disable"] | None = Field(default="disable", description="Enable/disable receiving certificates using the OCSP.")    
    ocsp_option: Literal["certificate", "server"] | None = Field(default="server", description="Specify whether the OCSP URL is from certificate or configured OCSP server.")    
    proxy: str | None = Field(max_length=127, default="", description="Proxy server FQDN or IP for OCSP/CA queries during certificate verification.")    
    proxy_port: int | None = Field(ge=1, le=65535, default=8080, description="Proxy server port (1 - 65535, default = 8080).")    
    proxy_username: str | None = Field(max_length=63, default="", description="Proxy server user name.")    
    proxy_password: Any = Field(max_length=128, default=None, description="Proxy server password.")    
    source_ip: str | None = Field(max_length=63, default="", description="Source IP address for dynamic AIA and OCSP queries.")    
    ocsp_default_server: str | None = Field(max_length=35, default="", description="Default OCSP server.")  # datasource: ['vpn.certificate.ocsp-server.name']    
    interface_select_method: Literal["auto", "sdwan", "specify"] | None = Field(default="auto", description="Specify how to select outgoing interface to reach server.")    
    interface: str = Field(max_length=15, default="", description="Specify outgoing interface to reach server.")  # datasource: ['system.interface.name']    
    vrf_select: int | None = Field(ge=0, le=511, default=0, description="VRF ID used for connection to server.")    
    check_ca_cert: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable verification of the user certificate and pass authentication if any CA in the chain is trusted (default = enable).")    
    check_ca_chain: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable verification of the entire certificate chain and pass authentication only if the chain is complete and all of the CAs in the chain are trusted (default = disable).")    
    subject_match: Literal["substring", "value"] | None = Field(default="substring", description="When searching for a matching certificate, control how to do RDN value matching with certificate subject name (default = substring).")    
    subject_set: Literal["subset", "superset"] | None = Field(default="subset", description="When searching for a matching certificate, control how to do RDN set matching with certificate subject name (default = subset).")    
    cn_match: Literal["substring", "value"] | None = Field(default="substring", description="When searching for a matching certificate, control how to do CN value matching with certificate subject name (default = substring).")    
    cn_allow_multi: Literal["disable", "enable"] | None = Field(default="enable", description="When searching for a matching certificate, allow multiple CN fields in certificate subject name (default = enable).")    
    crl_verification: list[CrlVerification] = Field(default=None, description="CRL verification options.")    
    strict_ocsp_check: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable strict mode OCSP checking.")    
    ssl_min_proto_version: SslMinProtoVersionEnum | None = Field(default="default", description="Minimum supported protocol version for SSL/TLS connections (default is to follow system global setting).")    
    cmp_save_extra_certs: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable saving extra certificates in CMP mode (default = disable).")    
    cmp_key_usage_checking: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable server certificate key usage checking in CMP mode (default = enable).")    
    cert_expire_warning: int | None = Field(ge=0, le=100, default=14, description="Number of days before a certificate expires to send a warning. Set to 0 to disable sending of the warning (0 - 100, default = 14).")    
    certname_rsa1024: str = Field(max_length=35, default="Fortinet_SSL_RSA1024", description="1024 bit RSA key certificate for re-signing server certificates for SSL inspection.")  # datasource: ['vpn.certificate.local.name']    
    certname_rsa2048: str = Field(max_length=35, default="Fortinet_SSL_RSA2048", description="2048 bit RSA key certificate for re-signing server certificates for SSL inspection.")  # datasource: ['vpn.certificate.local.name']    
    certname_rsa4096: str = Field(max_length=35, default="Fortinet_SSL_RSA4096", description="4096 bit RSA key certificate for re-signing server certificates for SSL inspection.")  # datasource: ['vpn.certificate.local.name']    
    certname_dsa1024: str = Field(max_length=35, default="Fortinet_SSL_DSA1024", description="1024 bit DSA key certificate for re-signing server certificates for SSL inspection.")  # datasource: ['vpn.certificate.local.name']    
    certname_dsa2048: str = Field(max_length=35, default="Fortinet_SSL_DSA2048", description="2048 bit DSA key certificate for re-signing server certificates for SSL inspection.")  # datasource: ['vpn.certificate.local.name']    
    certname_ecdsa256: str = Field(max_length=35, default="Fortinet_SSL_ECDSA256", description="256 bit ECDSA key certificate for re-signing server certificates for SSL inspection.")  # datasource: ['vpn.certificate.local.name']    
    certname_ecdsa384: str = Field(max_length=35, default="Fortinet_SSL_ECDSA384", description="384 bit ECDSA key certificate for re-signing server certificates for SSL inspection.")  # datasource: ['vpn.certificate.local.name']    
    certname_ecdsa521: str = Field(max_length=35, default="Fortinet_SSL_ECDSA521", description="521 bit ECDSA key certificate for re-signing server certificates for SSL inspection.")  # datasource: ['vpn.certificate.local.name']    
    certname_ed25519: str = Field(max_length=35, default="Fortinet_SSL_ED25519", description="253 bit EdDSA key certificate for re-signing server certificates for SSL inspection.")  # datasource: ['vpn.certificate.local.name']    
    certname_ed448: str = Field(max_length=35, default="Fortinet_SSL_ED448", description="456 bit EdDSA key certificate for re-signing server certificates for SSL inspection.")  # datasource: ['vpn.certificate.local.name']    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('ocsp_default_server')
    @classmethod
    def validate_ocsp_default_server(cls, v: Any) -> Any:
        """
        Validate ocsp_default_server field.
        
        Datasource: ['vpn.certificate.ocsp-server.name']
        
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
    @field_validator('certname_rsa1024')
    @classmethod
    def validate_certname_rsa1024(cls, v: Any) -> Any:
        """
        Validate certname_rsa1024 field.
        
        Datasource: ['vpn.certificate.local.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('certname_rsa2048')
    @classmethod
    def validate_certname_rsa2048(cls, v: Any) -> Any:
        """
        Validate certname_rsa2048 field.
        
        Datasource: ['vpn.certificate.local.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('certname_rsa4096')
    @classmethod
    def validate_certname_rsa4096(cls, v: Any) -> Any:
        """
        Validate certname_rsa4096 field.
        
        Datasource: ['vpn.certificate.local.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('certname_dsa1024')
    @classmethod
    def validate_certname_dsa1024(cls, v: Any) -> Any:
        """
        Validate certname_dsa1024 field.
        
        Datasource: ['vpn.certificate.local.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('certname_dsa2048')
    @classmethod
    def validate_certname_dsa2048(cls, v: Any) -> Any:
        """
        Validate certname_dsa2048 field.
        
        Datasource: ['vpn.certificate.local.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('certname_ecdsa256')
    @classmethod
    def validate_certname_ecdsa256(cls, v: Any) -> Any:
        """
        Validate certname_ecdsa256 field.
        
        Datasource: ['vpn.certificate.local.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('certname_ecdsa384')
    @classmethod
    def validate_certname_ecdsa384(cls, v: Any) -> Any:
        """
        Validate certname_ecdsa384 field.
        
        Datasource: ['vpn.certificate.local.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('certname_ecdsa521')
    @classmethod
    def validate_certname_ecdsa521(cls, v: Any) -> Any:
        """
        Validate certname_ecdsa521 field.
        
        Datasource: ['vpn.certificate.local.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('certname_ed25519')
    @classmethod
    def validate_certname_ed25519(cls, v: Any) -> Any:
        """
        Validate certname_ed25519 field.
        
        Datasource: ['vpn.certificate.local.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('certname_ed448')
    @classmethod
    def validate_certname_ed448(cls, v: Any) -> Any:
        """
        Validate certname_ed448 field.
        
        Datasource: ['vpn.certificate.local.name']
        
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
    "SettingModel",    "SettingCrlVerification",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:35.208258Z
# ============================================================================