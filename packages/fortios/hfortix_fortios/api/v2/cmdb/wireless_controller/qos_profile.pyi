""" - Type Stubs

Auto-generated stub file for type checking and IDE support.

Endpoint: wireless_controller/qos_profile
Category: cmdb
"""

from __future__ import annotations

from typing import (
    Any,
    ClassVar,
    Literal,
    TypedDict,
    overload,
)

from hfortix_fortios.models import (
    FortiObject,
    FortiObjectList,
)


# ================================================================
# TypedDict Payloads
# ================================================================

class QosProfileDscpwmmvoItem:
    """Nested item for dscp-wmm-vo field - supports attribute access."""
    id: int


class QosProfileDscpwmmviItem:
    """Nested item for dscp-wmm-vi field - supports attribute access."""
    id: int


class QosProfileDscpwmmbeItem:
    """Nested item for dscp-wmm-be field - supports attribute access."""
    id: int


class QosProfileDscpwmmbkItem:
    """Nested item for dscp-wmm-bk field - supports attribute access."""
    id: int


class QosProfilePayload(TypedDict, total=False):
    """Payload type for QosProfile operations."""
    name: str
    comment: str
    uplink: int
    downlink: int
    uplink_sta: int
    downlink_sta: int
    burst: Literal["enable", "disable"]
    wmm: Literal["enable", "disable"]
    wmm_uapsd: Literal["enable", "disable"]
    call_admission_control: Literal["enable", "disable"]
    call_capacity: int
    bandwidth_admission_control: Literal["enable", "disable"]
    bandwidth_capacity: int
    dscp_wmm_mapping: Literal["enable", "disable"]
    dscp_wmm_vo: str | list[str] | list[dict[str, Any]] | list[QosProfileDscpwmmvoItem]
    dscp_wmm_vi: str | list[str] | list[dict[str, Any]] | list[QosProfileDscpwmmviItem]
    dscp_wmm_be: str | list[str] | list[dict[str, Any]] | list[QosProfileDscpwmmbeItem]
    dscp_wmm_bk: str | list[str] | list[dict[str, Any]] | list[QosProfileDscpwmmbkItem]
    wmm_dscp_marking: Literal["enable", "disable"]
    wmm_vo_dscp: int
    wmm_vi_dscp: int
    wmm_be_dscp: int
    wmm_bk_dscp: int


# ================================================================
# Response Types (TypedDict for dict-style access)
# ================================================================

class QosProfileResponse(TypedDict, total=False):
    """Response type for QosProfile - use with .dict property for typed dict access."""
    name: str
    comment: str
    uplink: int
    downlink: int
    uplink_sta: int
    downlink_sta: int
    burst: Literal["enable", "disable"]
    wmm: Literal["enable", "disable"]
    wmm_uapsd: Literal["enable", "disable"]
    call_admission_control: Literal["enable", "disable"]
    call_capacity: int
    bandwidth_admission_control: Literal["enable", "disable"]
    bandwidth_capacity: int
    dscp_wmm_mapping: Literal["enable", "disable"]
    dscp_wmm_vo: list[QosProfileDscpwmmvoItem]
    dscp_wmm_vi: list[QosProfileDscpwmmviItem]
    dscp_wmm_be: list[QosProfileDscpwmmbeItem]
    dscp_wmm_bk: list[QosProfileDscpwmmbkItem]
    wmm_dscp_marking: Literal["enable", "disable"]
    wmm_vo_dscp: int
    wmm_vi_dscp: int
    wmm_be_dscp: int
    wmm_bk_dscp: int


# ================================================================
# Response Types (Class for attribute access)
# ================================================================


class QosProfileObject(FortiObject):
    """Typed FortiObject for QosProfile with field access."""
    name: str
    comment: str
    uplink: int
    downlink: int
    uplink_sta: int
    downlink_sta: int
    burst: Literal["enable", "disable"]
    wmm: Literal["enable", "disable"]
    wmm_uapsd: Literal["enable", "disable"]
    call_admission_control: Literal["enable", "disable"]
    call_capacity: int
    bandwidth_admission_control: Literal["enable", "disable"]
    bandwidth_capacity: int
    dscp_wmm_mapping: Literal["enable", "disable"]
    dscp_wmm_vo: list[QosProfileDscpwmmvoItem]
    dscp_wmm_vi: list[QosProfileDscpwmmviItem]
    dscp_wmm_be: list[QosProfileDscpwmmbeItem]
    dscp_wmm_bk: list[QosProfileDscpwmmbkItem]
    wmm_dscp_marking: Literal["enable", "disable"]
    wmm_vo_dscp: int
    wmm_vi_dscp: int
    wmm_be_dscp: int
    wmm_bk_dscp: int


# ================================================================
# Main Endpoint Class
# ================================================================

class QosProfile:
    """
    
    Endpoint: wireless_controller/qos_profile
    Category: cmdb
    MKey: name
    """
    
    # Class attributes for introspection
    endpoint: ClassVar[str] = ...
    path: ClassVar[str] = ...
    category: ClassVar[str] = ...
    mkey: ClassVar[str] = ...
    capabilities: ClassVar[dict[str, Any]] = ...
    
    def __init__(self, client: Any) -> None:
        """Initialize endpoint with HTTP client."""
        ...
    
    # ================================================================
    # GET Methods
    # ================================================================
    
    # CMDB with mkey - overloads for single vs list returns
    @overload
    def get(
        self,
        name: str,
        *,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> QosProfileObject: ...
    
    @overload
    def get(
        self,
        *,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> FortiObjectList[QosProfileObject]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...

    # ================================================================
    # POST Method
    # ================================================================
    
    def post(
        self,
        payload_dict: QosProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        uplink: int | None = ...,
        downlink: int | None = ...,
        uplink_sta: int | None = ...,
        downlink_sta: int | None = ...,
        burst: Literal["enable", "disable"] | None = ...,
        wmm: Literal["enable", "disable"] | None = ...,
        wmm_uapsd: Literal["enable", "disable"] | None = ...,
        call_admission_control: Literal["enable", "disable"] | None = ...,
        call_capacity: int | None = ...,
        bandwidth_admission_control: Literal["enable", "disable"] | None = ...,
        bandwidth_capacity: int | None = ...,
        dscp_wmm_mapping: Literal["enable", "disable"] | None = ...,
        dscp_wmm_vo: str | list[str] | list[dict[str, Any]] | list[QosProfileDscpwmmvoItem] | None = ...,
        dscp_wmm_vi: str | list[str] | list[dict[str, Any]] | list[QosProfileDscpwmmviItem] | None = ...,
        dscp_wmm_be: str | list[str] | list[dict[str, Any]] | list[QosProfileDscpwmmbeItem] | None = ...,
        dscp_wmm_bk: str | list[str] | list[dict[str, Any]] | list[QosProfileDscpwmmbkItem] | None = ...,
        wmm_dscp_marking: Literal["enable", "disable"] | None = ...,
        wmm_vo_dscp: int | None = ...,
        wmm_vi_dscp: int | None = ...,
        wmm_be_dscp: int | None = ...,
        wmm_bk_dscp: int | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> QosProfileObject: ...

    # ================================================================
    # PUT Method
    # ================================================================
    
    def put(
        self,
        payload_dict: QosProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        uplink: int | None = ...,
        downlink: int | None = ...,
        uplink_sta: int | None = ...,
        downlink_sta: int | None = ...,
        burst: Literal["enable", "disable"] | None = ...,
        wmm: Literal["enable", "disable"] | None = ...,
        wmm_uapsd: Literal["enable", "disable"] | None = ...,
        call_admission_control: Literal["enable", "disable"] | None = ...,
        call_capacity: int | None = ...,
        bandwidth_admission_control: Literal["enable", "disable"] | None = ...,
        bandwidth_capacity: int | None = ...,
        dscp_wmm_mapping: Literal["enable", "disable"] | None = ...,
        dscp_wmm_vo: str | list[str] | list[dict[str, Any]] | list[QosProfileDscpwmmvoItem] | None = ...,
        dscp_wmm_vi: str | list[str] | list[dict[str, Any]] | list[QosProfileDscpwmmviItem] | None = ...,
        dscp_wmm_be: str | list[str] | list[dict[str, Any]] | list[QosProfileDscpwmmbeItem] | None = ...,
        dscp_wmm_bk: str | list[str] | list[dict[str, Any]] | list[QosProfileDscpwmmbkItem] | None = ...,
        wmm_dscp_marking: Literal["enable", "disable"] | None = ...,
        wmm_vo_dscp: int | None = ...,
        wmm_vi_dscp: int | None = ...,
        wmm_be_dscp: int | None = ...,
        wmm_bk_dscp: int | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> QosProfileObject: ...

    # ================================================================
    # DELETE Method
    # ================================================================
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> FortiObject: ...

    # ================================================================
    # Utility Methods
    # ================================================================
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: QosProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        uplink: int | None = ...,
        downlink: int | None = ...,
        uplink_sta: int | None = ...,
        downlink_sta: int | None = ...,
        burst: Literal["enable", "disable"] | None = ...,
        wmm: Literal["enable", "disable"] | None = ...,
        wmm_uapsd: Literal["enable", "disable"] | None = ...,
        call_admission_control: Literal["enable", "disable"] | None = ...,
        call_capacity: int | None = ...,
        bandwidth_admission_control: Literal["enable", "disable"] | None = ...,
        bandwidth_capacity: int | None = ...,
        dscp_wmm_mapping: Literal["enable", "disable"] | None = ...,
        dscp_wmm_vo: str | list[str] | list[dict[str, Any]] | list[QosProfileDscpwmmvoItem] | None = ...,
        dscp_wmm_vi: str | list[str] | list[dict[str, Any]] | list[QosProfileDscpwmmviItem] | None = ...,
        dscp_wmm_be: str | list[str] | list[dict[str, Any]] | list[QosProfileDscpwmmbeItem] | None = ...,
        dscp_wmm_bk: str | list[str] | list[dict[str, Any]] | list[QosProfileDscpwmmbkItem] | None = ...,
        wmm_dscp_marking: Literal["enable", "disable"] | None = ...,
        wmm_vo_dscp: int | None = ...,
        wmm_vi_dscp: int | None = ...,
        wmm_be_dscp: int | None = ...,
        wmm_bk_dscp: int | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> FortiObject: ...
    
    # Helper methods
    @staticmethod
    def help(field_name: str | None = ...) -> str: ...
    
    @staticmethod
    def fields(detailed: bool = ...) -> list[str] | list[dict[str, Any]]: ...
    
    @staticmethod
    def field_info(field_name: str) -> FortiObject: ...
    
    @staticmethod
    def validate_field(name: str, value: Any) -> bool: ...
    
    @staticmethod
    def required_fields() -> list[str]: ...
    
    @staticmethod
    def defaults() -> FortiObject: ...
    
    @staticmethod
    def schema() -> FortiObject: ...


__all__ = [
    "QosProfile",
    "QosProfilePayload",
    "QosProfileResponse",
    "QosProfileObject",
]