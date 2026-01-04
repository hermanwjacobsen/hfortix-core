from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class DataplanPayload(TypedDict, total=False):
    """
    Type hints for extension_controller/dataplan payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
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


class Dataplan:
    """
    FortiExtender dataplan configuration.
    
    Path: extension_controller/dataplan
    Category: cmdb
    Primary Key: name
    """
    
    def get(
        self,
        name: str | None = ...,
        filter: str | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
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
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
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
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> Union[bool, Coroutine[Any, Any, bool]]: ...
    
    def set(
        self,
        payload_dict: DataplanPayload | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
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