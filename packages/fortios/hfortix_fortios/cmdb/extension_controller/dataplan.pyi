from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class DataplanPayload(TypedDict, total=False):
    """
    Type hints for extension_controller/dataplan payload fields.
    
    FortiExtender dataplan configuration.
    
    **Usage:**
        payload: DataplanPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # FortiExtender data plan name.
    modem_id: NotRequired[Literal["modem1", "modem2", "all"]]  # Dataplan's modem specifics, if any.
    type: Literal["carrier", "slot", "iccid", "generic"]  # Type preferences configuration.
    slot: Literal["sim1", "sim2"]  # SIM slot configuration.
    iccid: str  # ICCID configuration.
    carrier: str  # Carrier configuration.
    apn: NotRequired[str]  # APN configuration.
    auth_type: NotRequired[Literal["none", "pap", "chap"]]  # Authentication type.
    username: str  # Username.
    password: str  # Password.
    pdn: NotRequired[Literal["ipv4-only", "ipv6-only", "ipv4-ipv6"]]  # PDN type.
    signal_threshold: NotRequired[int]  # Signal threshold. Specify the range between 50 - 100, where 
    signal_period: NotRequired[int]  # Signal period (600 to 18000 seconds).
    capacity: NotRequired[int]  # Capacity in MB (0 - 102400000).
    monthly_fee: NotRequired[int]  # Monthly fee of dataplan (0 - 100000, in local currency).
    billing_date: NotRequired[int]  # Billing day of the month (1 - 31).
    overage: NotRequired[Literal["disable", "enable"]]  # Enable/disable dataplan overage detection.
    preferred_subnet: NotRequired[int]  # Preferred subnet mask (0 - 32).
    private_network: NotRequired[Literal["disable", "enable"]]  # Enable/disable dataplan private network support.


class DataplanObject(FortiObject[DataplanPayload]):
    """Typed FortiObject for extension_controller/dataplan with IDE autocomplete support."""
    
    # FortiExtender data plan name.
    name: str
    # Dataplan's modem specifics, if any.
    modem_id: Literal["modem1", "modem2", "all"]
    # Type preferences configuration.
    type: Literal["carrier", "slot", "iccid", "generic"]
    # SIM slot configuration.
    slot: Literal["sim1", "sim2"]
    # ICCID configuration.
    iccid: str
    # Carrier configuration.
    carrier: str
    # APN configuration.
    apn: str
    # Authentication type.
    auth_type: Literal["none", "pap", "chap"]
    # Username.
    username: str
    # Password.
    password: str
    # PDN type.
    pdn: Literal["ipv4-only", "ipv6-only", "ipv4-ipv6"]
    # Signal threshold. Specify the range between 50 - 100, where 50/100 means -50/-10
    signal_threshold: int
    # Signal period (600 to 18000 seconds).
    signal_period: int
    # Capacity in MB (0 - 102400000).
    capacity: int
    # Monthly fee of dataplan (0 - 100000, in local currency).
    monthly_fee: int
    # Billing day of the month (1 - 31).
    billing_date: int
    # Enable/disable dataplan overage detection.
    overage: Literal["disable", "enable"]
    # Preferred subnet mask (0 - 32).
    preferred_subnet: int
    # Enable/disable dataplan private network support.
    private_network: Literal["disable", "enable"]
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> DataplanPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Dataplan:
    """
    FortiExtender dataplan configuration.
    
    Path: extension_controller/dataplan
    Category: cmdb
    Primary Key: name
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey provided)
    @overload
    def get(
        self,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        *,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> DataplanObject: ...
    
    # List of objects (no mkey provided - most specific for list returns)
    # For singleton endpoints (no mkey), returns single object; for table endpoints, returns list
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> list[DataplanObject]: ...
    
    @overload
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True],
        *,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Dict mode with mkey provided (single dict)
    @overload
    def get(
        self,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Dict mode without mkey (returns dict with results array)
    @overload
    def get(
        self,
        name: None = None,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Default overload for dict mode
    @overload
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], list[dict[str, Any]]]: ...
    
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: str | None = ...,
        **kwargs: Any,
    ) -> DataplanObject | list[DataplanObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: DataplanPayload | None = ...,
        name: str | None = ...,
        modem_id: Literal["modem1", "modem2", "all"] | None = ...,
        type: Literal["carrier", "slot", "iccid", "generic"] | None = ...,
        slot: Literal["sim1", "sim2"] | None = ...,
        iccid: str | None = ...,
        carrier: str | None = ...,
        apn: str | None = ...,
        auth_type: Literal["none", "pap", "chap"] | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        pdn: Literal["ipv4-only", "ipv6-only", "ipv4-ipv6"] | None = ...,
        signal_threshold: int | None = ...,
        signal_period: int | None = ...,
        capacity: int | None = ...,
        monthly_fee: int | None = ...,
        billing_date: int | None = ...,
        overage: Literal["disable", "enable"] | None = ...,
        preferred_subnet: int | None = ...,
        private_network: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> DataplanObject: ...
    
    @overload
    def post(
        self,
        payload_dict: DataplanPayload | None = ...,
        name: str | None = ...,
        modem_id: Literal["modem1", "modem2", "all"] | None = ...,
        type: Literal["carrier", "slot", "iccid", "generic"] | None = ...,
        slot: Literal["sim1", "sim2"] | None = ...,
        iccid: str | None = ...,
        carrier: str | None = ...,
        apn: str | None = ...,
        auth_type: Literal["none", "pap", "chap"] | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        pdn: Literal["ipv4-only", "ipv6-only", "ipv4-ipv6"] | None = ...,
        signal_threshold: int | None = ...,
        signal_period: int | None = ...,
        capacity: int | None = ...,
        monthly_fee: int | None = ...,
        billing_date: int | None = ...,
        overage: Literal["disable", "enable"] | None = ...,
        preferred_subnet: int | None = ...,
        private_network: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: DataplanPayload | None = ...,
        name: str | None = ...,
        modem_id: Literal["modem1", "modem2", "all"] | None = ...,
        type: Literal["carrier", "slot", "iccid", "generic"] | None = ...,
        slot: Literal["sim1", "sim2"] | None = ...,
        iccid: str | None = ...,
        carrier: str | None = ...,
        apn: str | None = ...,
        auth_type: Literal["none", "pap", "chap"] | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        pdn: Literal["ipv4-only", "ipv6-only", "ipv4-ipv6"] | None = ...,
        signal_threshold: int | None = ...,
        signal_period: int | None = ...,
        capacity: int | None = ...,
        monthly_fee: int | None = ...,
        billing_date: int | None = ...,
        overage: Literal["disable", "enable"] | None = ...,
        preferred_subnet: int | None = ...,
        private_network: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: DataplanPayload | None = ...,
        name: str | None = ...,
        modem_id: Literal["modem1", "modem2", "all"] | None = ...,
        type: Literal["carrier", "slot", "iccid", "generic"] | None = ...,
        slot: Literal["sim1", "sim2"] | None = ...,
        iccid: str | None = ...,
        carrier: str | None = ...,
        apn: str | None = ...,
        auth_type: Literal["none", "pap", "chap"] | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        pdn: Literal["ipv4-only", "ipv6-only", "ipv4-ipv6"] | None = ...,
        signal_threshold: int | None = ...,
        signal_period: int | None = ...,
        capacity: int | None = ...,
        monthly_fee: int | None = ...,
        billing_date: int | None = ...,
        overage: Literal["disable", "enable"] | None = ...,
        preferred_subnet: int | None = ...,
        private_network: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: DataplanPayload | None = ...,
        name: str | None = ...,
        modem_id: Literal["modem1", "modem2", "all"] | None = ...,
        type: Literal["carrier", "slot", "iccid", "generic"] | None = ...,
        slot: Literal["sim1", "sim2"] | None = ...,
        iccid: str | None = ...,
        carrier: str | None = ...,
        apn: str | None = ...,
        auth_type: Literal["none", "pap", "chap"] | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        pdn: Literal["ipv4-only", "ipv6-only", "ipv4-ipv6"] | None = ...,
        signal_threshold: int | None = ...,
        signal_period: int | None = ...,
        capacity: int | None = ...,
        monthly_fee: int | None = ...,
        billing_date: int | None = ...,
        overage: Literal["disable", "enable"] | None = ...,
        preferred_subnet: int | None = ...,
        private_network: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> DataplanObject: ...
    
    @overload
    def put(
        self,
        payload_dict: DataplanPayload | None = ...,
        name: str | None = ...,
        modem_id: Literal["modem1", "modem2", "all"] | None = ...,
        type: Literal["carrier", "slot", "iccid", "generic"] | None = ...,
        slot: Literal["sim1", "sim2"] | None = ...,
        iccid: str | None = ...,
        carrier: str | None = ...,
        apn: str | None = ...,
        auth_type: Literal["none", "pap", "chap"] | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        pdn: Literal["ipv4-only", "ipv6-only", "ipv4-ipv6"] | None = ...,
        signal_threshold: int | None = ...,
        signal_period: int | None = ...,
        capacity: int | None = ...,
        monthly_fee: int | None = ...,
        billing_date: int | None = ...,
        overage: Literal["disable", "enable"] | None = ...,
        preferred_subnet: int | None = ...,
        private_network: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: DataplanPayload | None = ...,
        name: str | None = ...,
        modem_id: Literal["modem1", "modem2", "all"] | None = ...,
        type: Literal["carrier", "slot", "iccid", "generic"] | None = ...,
        slot: Literal["sim1", "sim2"] | None = ...,
        iccid: str | None = ...,
        carrier: str | None = ...,
        apn: str | None = ...,
        auth_type: Literal["none", "pap", "chap"] | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        pdn: Literal["ipv4-only", "ipv6-only", "ipv4-ipv6"] | None = ...,
        signal_threshold: int | None = ...,
        signal_period: int | None = ...,
        capacity: int | None = ...,
        monthly_fee: int | None = ...,
        billing_date: int | None = ...,
        overage: Literal["disable", "enable"] | None = ...,
        preferred_subnet: int | None = ...,
        private_network: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: DataplanPayload | None = ...,
        name: str | None = ...,
        modem_id: Literal["modem1", "modem2", "all"] | None = ...,
        type: Literal["carrier", "slot", "iccid", "generic"] | None = ...,
        slot: Literal["sim1", "sim2"] | None = ...,
        iccid: str | None = ...,
        carrier: str | None = ...,
        apn: str | None = ...,
        auth_type: Literal["none", "pap", "chap"] | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        pdn: Literal["ipv4-only", "ipv6-only", "ipv4-ipv6"] | None = ...,
        signal_threshold: int | None = ...,
        signal_period: int | None = ...,
        capacity: int | None = ...,
        monthly_fee: int | None = ...,
        billing_date: int | None = ...,
        overage: Literal["disable", "enable"] | None = ...,
        preferred_subnet: int | None = ...,
        private_network: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> DataplanObject: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: DataplanPayload | None = ...,
        name: str | None = ...,
        modem_id: Literal["modem1", "modem2", "all"] | None = ...,
        type: Literal["carrier", "slot", "iccid", "generic"] | None = ...,
        slot: Literal["sim1", "sim2"] | None = ...,
        iccid: str | None = ...,
        carrier: str | None = ...,
        apn: str | None = ...,
        auth_type: Literal["none", "pap", "chap"] | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        pdn: Literal["ipv4-only", "ipv6-only", "ipv4-ipv6"] | None = ...,
        signal_threshold: int | None = ...,
        signal_period: int | None = ...,
        capacity: int | None = ...,
        monthly_fee: int | None = ...,
        billing_date: int | None = ...,
        overage: Literal["disable", "enable"] | None = ...,
        preferred_subnet: int | None = ...,
        private_network: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Helper methods
    @staticmethod
    def help(field_name: str | None = ...) -> str: ...
    
    @staticmethod
    def fields(detailed: bool = ...) -> Union[list[str], list[dict[str, Any]]]: ...
    
    @staticmethod
    def field_info(field_name: str) -> dict[str, Any]: ...
    
    @staticmethod
    def validate_field(name: str, value: Any) -> bool: ...
    
    @staticmethod
    def required_fields() -> list[str]: ...
    
    @staticmethod
    def defaults() -> dict[str, Any]: ...
    
    @staticmethod
    def schema() -> dict[str, Any]: ...


__all__ = [
    "Dataplan",
    "DataplanPayload",
    "DataplanObject",
]