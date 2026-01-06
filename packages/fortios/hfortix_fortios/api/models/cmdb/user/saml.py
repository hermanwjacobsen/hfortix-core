"""
Pydantic Models for CMDB - user/saml

Runtime validation models for user/saml configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.user.saml import 
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
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class SamlScim_user_attr_typeEnum(str, Enum):
    """Allowed values for scim_user_attr_type field."""
    USER_NAME = "user-name"    DISPLAY_NAME = "display-name"    EXTERNAL_ID = "external-id"    EMAIL = "email"
class SamlUser_claim_typeEnum(str, Enum):
    """Allowed values for user_claim_type field."""
    EMAIL = "email"    GIVEN_NAME = "given-name"    NAME = "name"    UPN = "upn"    COMMON_NAME = "common-name"    EMAIL_ADFS_1X = "email-adfs-1x"    GROUP = "group"    UPN_ADFS_1X = "upn-adfs-1x"    ROLE = "role"    SUR_NAME = "sur-name"    PPID = "ppid"    NAME_IDENTIFIER = "name-identifier"    AUTHENTICATION_METHOD = "authentication-method"    DENY_ONLY_GROUP_SID = "deny-only-group-sid"    DENY_ONLY_PRIMARY_SID = "deny-only-primary-sid"    DENY_ONLY_PRIMARY_GROUP_SID = "deny-only-primary-group-sid"    GROUP_SID = "group-sid"    PRIMARY_GROUP_SID = "primary-group-sid"    PRIMARY_SID = "primary-sid"    WINDOWS_ACCOUNT_NAME = "windows-account-name"
class SamlGroup_claim_typeEnum(str, Enum):
    """Allowed values for group_claim_type field."""
    EMAIL = "email"    GIVEN_NAME = "given-name"    NAME = "name"    UPN = "upn"    COMMON_NAME = "common-name"    EMAIL_ADFS_1X = "email-adfs-1x"    GROUP = "group"    UPN_ADFS_1X = "upn-adfs-1x"    ROLE = "role"    SUR_NAME = "sur-name"    PPID = "ppid"    NAME_IDENTIFIER = "name-identifier"    AUTHENTICATION_METHOD = "authentication-method"    DENY_ONLY_GROUP_SID = "deny-only-group-sid"    DENY_ONLY_PRIMARY_SID = "deny-only-primary-sid"    DENY_ONLY_PRIMARY_GROUP_SID = "deny-only-primary-group-sid"    GROUP_SID = "group-sid"    PRIMARY_GROUP_SID = "primary-group-sid"    PRIMARY_SID = "primary-sid"    WINDOWS_ACCOUNT_NAME = "windows-account-name"

# ============================================================================
# Main Model
# ============================================================================

class SamlModel(BaseModel):
    """
    Pydantic model for user/saml configuration.
    
    SAML server entry configuration.
    
    Validation Rules:        - name: max_length=35 pattern=        - cert: max_length=35 pattern=        - entity_id: max_length=255 pattern=        - single_sign_on_url: max_length=255 pattern=        - single_logout_url: max_length=255 pattern=        - idp_entity_id: max_length=255 pattern=        - idp_single_sign_on_url: max_length=255 pattern=        - idp_single_logout_url: max_length=255 pattern=        - idp_cert: max_length=35 pattern=        - scim_client: max_length=35 pattern=        - scim_user_attr_type: pattern=        - scim_group_attr_type: pattern=        - user_name: max_length=255 pattern=        - group_name: max_length=255 pattern=        - digest_method: pattern=        - require_signed_resp_and_asrt: pattern=        - limit_relaystate: pattern=        - clock_tolerance: min=0 max=300 pattern=        - adfs_claim: pattern=        - user_claim_type: pattern=        - group_claim_type: pattern=        - reauth: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=35, default="", description="SAML server entry name.")    
    cert: str | None = Field(max_length=35, default="", description="Certificate to sign SAML messages.")  # datasource: ['vpn.certificate.local.name']    
    entity_id: str = Field(max_length=255, default="", description="SP entity ID.")    
    single_sign_on_url: str = Field(max_length=255, default="", description="SP single sign-on URL.")    
    single_logout_url: str | None = Field(max_length=255, default="", description="SP single logout URL.")    
    idp_entity_id: str = Field(max_length=255, default="", description="IDP entity ID.")    
    idp_single_sign_on_url: str = Field(max_length=255, default="", description="IDP single sign-on URL.")    
    idp_single_logout_url: str | None = Field(max_length=255, default="", description="IDP single logout url.")    
    idp_cert: str = Field(max_length=35, default="", description="IDP Certificate name.")  # datasource: ['vpn.certificate.remote.name']    
    scim_client: str | None = Field(max_length=35, default="", description="SCIM client name.")  # datasource: ['user.scim.name']    
    scim_user_attr_type: ScimUserAttrTypeEnum | None = Field(default="user-name", description="User attribute type used to match SCIM users (default = user-name).")    
    scim_group_attr_type: Literal["display-name", "external-id"] | None = Field(default="display-name", description="Group attribute type used to match SCIM groups (default = display-name).")    
    user_name: str | None = Field(max_length=255, default="", description="User name in assertion statement.")    
    group_name: str | None = Field(max_length=255, default="", description="Group name in assertion statement.")    
    digest_method: Literal["sha1", "sha256"] | None = Field(default="sha1", description="Digest method algorithm.")    
    require_signed_resp_and_asrt: Literal["enable", "disable"] | None = Field(default="disable", description="Require both response and assertion from IDP to be signed when FGT acts as SP (default = disable).")    
    limit_relaystate: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable limiting of relay-state parameter when it exceeds SAML 2.0 specification limits (80 bytes).")    
    clock_tolerance: int | None = Field(ge=0, le=300, default=15, description="Clock skew tolerance in seconds (0 - 300, default = 15, 0 = no tolerance).")    
    adfs_claim: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable ADFS Claim for user/group attribute in assertion statement (default = disable).")    
    user_claim_type: UserClaimTypeEnum | None = Field(default="upn", description="User name claim in assertion statement.")    
    group_claim_type: GroupClaimTypeEnum | None = Field(default="group", description="Group claim in assertion statement.")    
    reauth: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable signalling of IDP to force user re-authentication (default = disable).")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('cert')
    @classmethod
    def validate_cert(cls, v: Any) -> Any:
        """
        Validate cert field.
        
        Datasource: ['vpn.certificate.local.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('idp_cert')
    @classmethod
    def validate_idp_cert(cls, v: Any) -> Any:
        """
        Validate idp_cert field.
        
        Datasource: ['vpn.certificate.remote.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('scim_client')
    @classmethod
    def validate_scim_client(cls, v: Any) -> Any:
        """
        Validate scim_client field.
        
        Datasource: ['user.scim.name']
        
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
    "SamlModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:34.038598Z
# ============================================================================