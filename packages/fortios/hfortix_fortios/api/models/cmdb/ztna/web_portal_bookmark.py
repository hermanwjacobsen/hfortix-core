"""
Pydantic Models for CMDB - ztna/web_portal_bookmark

Runtime validation models for ztna/web_portal_bookmark configuration.
Generated from FortiOS schema version unknown.

Example Usage:
    >>> from hfortix_fortios.models.cmdb.ztna.web_portal_bookmark import 
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

from pydantic import BaseModel, Field
from typing import Any, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class WebPortalBookmarkUsers(BaseModel):
    """
    Child table model for users.
    
    User name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="User name.")  # datasource: ['user.local.name', 'user.certificate.name']
class WebPortalBookmarkGroups(BaseModel):
    """
    Child table model for groups.
    
    User groups.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Group name.")  # datasource: ['user.group.name']
class WebPortalBookmarkBookmarks(BaseModel):
    """
    Child table model for bookmarks.
    
    Bookmark table.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=35, default="", description="Bookmark name.")    
    apptype: ApptypeEnum = Field(default="web", description="Application type.")    
    url: str = Field(max_length=128, description="URL parameter.")    
    host: str = Field(max_length=128, description="Host name/IP parameter.")    
    folder: str = Field(max_length=128, description="Network shared file folder parameter.")    
    domain: str | None = Field(max_length=128, default=None, description="Login domain.")    
    description: str | None = Field(max_length=128, default=None, description="Description.")    
    keyboard_layout: KeyboardLayoutEnum | None = Field(default="en-us", description="Keyboard layout.")    
    security: SecurityEnum | None = Field(default="any", description="Security mode for RDP connection (default = any).")    
    send_preconnection_id: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable sending of preconnection ID.")    
    preconnection_id: int | None = Field(ge=0, le=4294967295, default=0, description="The numeric ID of the RDP source (0-4294967295).")    
    preconnection_blob: str | None = Field(max_length=511, default=None, description="An arbitrary string which identifies the RDP source.")    
    load_balancing_info: str | None = Field(max_length=511, default=None, description="The load balancing information or cookie which should be provided to the connection broker.")    
    restricted_admin: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable restricted admin mode for RDP.")    
    port: int | None = Field(ge=0, le=65535, default=0, description="Remote port.")    
    logon_user: str | None = Field(max_length=35, default=None, description="Logon user.")    
    logon_password: Any = Field(max_length=128, default=None, description="Logon password.")    
    color_depth: Literal["32", "16", "8"] | None = Field(default="16", description="Color depth per pixel.")    
    sso: Literal["disable", "enable"] | None = Field(default="disable", description="Single sign-on.")    
    width: int | None = Field(ge=0, le=65535, default=0, description="Screen width (range from 0 - 65535, default = 0).")    
    height: int | None = Field(ge=0, le=65535, default=0, description="Screen height (range from 0 - 65535, default = 0).")    
    vnc_keyboard_layout: VncKeyboardLayoutEnum | None = Field(default="default", description="Keyboard layout.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class WebPortalBookmarkModel(BaseModel):
    """
    Pydantic model for ztna/web_portal_bookmark configuration.
    
    Configure ztna web-portal bookmark.
    
    Validation Rules:        - name: max_length=35 pattern=        - users: pattern=        - groups: pattern=        - bookmarks: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=35, default="", description="Bookmark name.")    
    users: list[Users] = Field(default=None, description="User name.")    
    groups: list[Groups] = Field(default=None, description="User groups.")    
    bookmarks: list[Bookmarks] = Field(default=None, description="Bookmark table.")    
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
    "WebPortalBookmarkModel",    "WebPortalBookmarkUsers",    "WebPortalBookmarkGroups",    "WebPortalBookmarkBookmarks",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-06T20:14:35.714616Z
# ============================================================================