from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class ProfilePayload(TypedDict, total=False):
    """
    Type hints for emailfilter/profile payload fields.
    
    Configure Email Filter profiles.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.emailfilter.block-allow-list.BlockAllowListEndpoint` (via: spam-bal-table)
        - :class:`~.emailfilter.bword.BwordEndpoint` (via: spam-bword-table)
        - :class:`~.emailfilter.dnsbl.DnsblEndpoint` (via: spam-rbl-table)
        - :class:`~.emailfilter.iptrust.IptrustEndpoint` (via: spam-iptrust-table)
        - :class:`~.emailfilter.mheader.MheaderEndpoint` (via: spam-mheader-table)
        - :class:`~.system.replacemsg-group.ReplacemsgGroupEndpoint` (via: replacemsg-group)

    **Usage:**
        payload: ProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Profile name.
    comment: NotRequired[str]  # Comment.
    feature_set: NotRequired[Literal["flow", "proxy"]]  # Flow/proxy feature set.
    replacemsg_group: NotRequired[str]  # Replacement message group.
    spam_log: NotRequired[Literal["disable", "enable"]]  # Enable/disable spam logging for email filtering.
    spam_log_fortiguard_response: NotRequired[Literal["disable", "enable"]]  # Enable/disable logging FortiGuard spam response.
    spam_filtering: NotRequired[Literal["enable", "disable"]]  # Enable/disable spam filtering.
    external: NotRequired[Literal["enable", "disable"]]  # Enable/disable external Email inspection.
    options: NotRequired[Literal["bannedword", "spambal", "spamfsip", "spamfssubmit", "spamfschksum", "spamfsurl", "spamhelodns", "spamraddrdns", "spamrbl", "spamhdrcheck", "spamfsphish"]]  # Options.
    imap: NotRequired[str]  # IMAP.
    pop3: NotRequired[str]  # POP3.
    smtp: NotRequired[str]  # SMTP.
    mapi: NotRequired[str]  # MAPI.
    msn_hotmail: NotRequired[str]  # MSN Hotmail.
    yahoo_mail: NotRequired[str]  # Yahoo! Mail.
    gmail: NotRequired[str]  # Gmail.
    other_webmails: NotRequired[str]  # Other supported webmails.
    spam_bword_threshold: NotRequired[int]  # Spam banned word threshold.
    spam_bword_table: NotRequired[int]  # Anti-spam banned word table ID.
    spam_bal_table: NotRequired[int]  # Anti-spam block/allow list table ID.
    spam_mheader_table: NotRequired[int]  # Anti-spam MIME header table ID.
    spam_rbl_table: NotRequired[int]  # Anti-spam DNSBL table ID.
    spam_iptrust_table: NotRequired[int]  # Anti-spam IP trust table ID.

# Nested classes for table field children


# Response TypedDict for GET returns (all fields present in API response)
class ProfileResponse(TypedDict):
    """
    Type hints for emailfilter/profile API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    comment: str
    feature_set: Literal["flow", "proxy"]
    replacemsg_group: str
    spam_log: Literal["disable", "enable"]
    spam_log_fortiguard_response: Literal["disable", "enable"]
    spam_filtering: Literal["enable", "disable"]
    external: Literal["enable", "disable"]
    options: Literal["bannedword", "spambal", "spamfsip", "spamfssubmit", "spamfschksum", "spamfsurl", "spamhelodns", "spamraddrdns", "spamrbl", "spamhdrcheck", "spamfsphish"]
    imap: str
    pop3: str
    smtp: str
    mapi: str
    msn_hotmail: str
    yahoo_mail: str
    gmail: str
    other_webmails: str
    spam_bword_threshold: int
    spam_bword_table: int
    spam_bal_table: int
    spam_mheader_table: int
    spam_rbl_table: int
    spam_iptrust_table: int


@final
class ProfileObject:
    """Typed FortiObject for emailfilter/profile with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Profile name.
    name: str
    # Comment.
    comment: str
    # Flow/proxy feature set.
    feature_set: Literal["flow", "proxy"]
    # Replacement message group.
    replacemsg_group: str
    # Enable/disable spam logging for email filtering.
    spam_log: Literal["disable", "enable"]
    # Enable/disable logging FortiGuard spam response.
    spam_log_fortiguard_response: Literal["disable", "enable"]
    # Enable/disable spam filtering.
    spam_filtering: Literal["enable", "disable"]
    # Enable/disable external Email inspection.
    external: Literal["enable", "disable"]
    # Options.
    options: Literal["bannedword", "spambal", "spamfsip", "spamfssubmit", "spamfschksum", "spamfsurl", "spamhelodns", "spamraddrdns", "spamrbl", "spamhdrcheck", "spamfsphish"]
    # IMAP.
    imap: str
    # POP3.
    pop3: str
    # SMTP.
    smtp: str
    # MAPI.
    mapi: str
    # MSN Hotmail.
    msn_hotmail: str
    # Yahoo! Mail.
    yahoo_mail: str
    # Gmail.
    gmail: str
    # Other supported webmails.
    other_webmails: str
    # Spam banned word threshold.
    spam_bword_threshold: int
    # Anti-spam banned word table ID.
    spam_bword_table: int
    # Anti-spam block/allow list table ID.
    spam_bal_table: int
    # Anti-spam MIME header table ID.
    spam_mheader_table: int
    # Anti-spam DNSBL table ID.
    spam_rbl_table: int
    # Anti-spam IP trust table ID.
    spam_iptrust_table: int
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> ProfilePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Profile:
    """
    Configure Email Filter profiles.
    
    Path: emailfilter/profile
    Category: cmdb
    Primary Key: name
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey/name provided as positional arg)
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
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ProfileObject: ...
    
    # Single object (mkey/name provided as keyword arg)
    @overload
    def get(
        self,
        *,
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
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ProfileObject: ...
    
    # List of objects (no mkey/name provided) - keyword-only signature
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
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> list[ProfileObject]: ...
    
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
        raw_json: Literal[True] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Dict mode with mkey provided as positional arg (single dict)
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
    ) -> ProfileResponse: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
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
    ) -> ProfileResponse: ...
    
    # Dict mode - list of dicts (no mkey/name provided) - keyword-only signature
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
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> list[ProfileResponse]: ...
    
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
    ) -> ProfileObject | list[ProfileObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        feature_set: Literal["flow", "proxy"] | None = ...,
        replacemsg_group: str | None = ...,
        spam_log: Literal["disable", "enable"] | None = ...,
        spam_log_fortiguard_response: Literal["disable", "enable"] | None = ...,
        spam_filtering: Literal["enable", "disable"] | None = ...,
        external: Literal["enable", "disable"] | None = ...,
        options: Literal["bannedword", "spambal", "spamfsip", "spamfssubmit", "spamfschksum", "spamfsurl", "spamhelodns", "spamraddrdns", "spamrbl", "spamhdrcheck", "spamfsphish"] | list[str] | None = ...,
        imap: str | None = ...,
        pop3: str | None = ...,
        smtp: str | None = ...,
        mapi: str | None = ...,
        msn_hotmail: str | None = ...,
        yahoo_mail: str | None = ...,
        gmail: str | None = ...,
        other_webmails: str | None = ...,
        spam_bword_threshold: int | None = ...,
        spam_bword_table: int | None = ...,
        spam_bal_table: int | None = ...,
        spam_mheader_table: int | None = ...,
        spam_rbl_table: int | None = ...,
        spam_iptrust_table: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ProfileObject: ...
    
    @overload
    def post(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        feature_set: Literal["flow", "proxy"] | None = ...,
        replacemsg_group: str | None = ...,
        spam_log: Literal["disable", "enable"] | None = ...,
        spam_log_fortiguard_response: Literal["disable", "enable"] | None = ...,
        spam_filtering: Literal["enable", "disable"] | None = ...,
        external: Literal["enable", "disable"] | None = ...,
        options: Literal["bannedword", "spambal", "spamfsip", "spamfssubmit", "spamfschksum", "spamfsurl", "spamhelodns", "spamraddrdns", "spamrbl", "spamhdrcheck", "spamfsphish"] | list[str] | None = ...,
        imap: str | None = ...,
        pop3: str | None = ...,
        smtp: str | None = ...,
        mapi: str | None = ...,
        msn_hotmail: str | None = ...,
        yahoo_mail: str | None = ...,
        gmail: str | None = ...,
        other_webmails: str | None = ...,
        spam_bword_threshold: int | None = ...,
        spam_bword_table: int | None = ...,
        spam_bal_table: int | None = ...,
        spam_mheader_table: int | None = ...,
        spam_rbl_table: int | None = ...,
        spam_iptrust_table: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        feature_set: Literal["flow", "proxy"] | None = ...,
        replacemsg_group: str | None = ...,
        spam_log: Literal["disable", "enable"] | None = ...,
        spam_log_fortiguard_response: Literal["disable", "enable"] | None = ...,
        spam_filtering: Literal["enable", "disable"] | None = ...,
        external: Literal["enable", "disable"] | None = ...,
        options: Literal["bannedword", "spambal", "spamfsip", "spamfssubmit", "spamfschksum", "spamfsurl", "spamhelodns", "spamraddrdns", "spamrbl", "spamhdrcheck", "spamfsphish"] | list[str] | None = ...,
        imap: str | None = ...,
        pop3: str | None = ...,
        smtp: str | None = ...,
        mapi: str | None = ...,
        msn_hotmail: str | None = ...,
        yahoo_mail: str | None = ...,
        gmail: str | None = ...,
        other_webmails: str | None = ...,
        spam_bword_threshold: int | None = ...,
        spam_bword_table: int | None = ...,
        spam_bal_table: int | None = ...,
        spam_mheader_table: int | None = ...,
        spam_rbl_table: int | None = ...,
        spam_iptrust_table: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        feature_set: Literal["flow", "proxy"] | None = ...,
        replacemsg_group: str | None = ...,
        spam_log: Literal["disable", "enable"] | None = ...,
        spam_log_fortiguard_response: Literal["disable", "enable"] | None = ...,
        spam_filtering: Literal["enable", "disable"] | None = ...,
        external: Literal["enable", "disable"] | None = ...,
        options: Literal["bannedword", "spambal", "spamfsip", "spamfssubmit", "spamfschksum", "spamfsurl", "spamhelodns", "spamraddrdns", "spamrbl", "spamhdrcheck", "spamfsphish"] | list[str] | None = ...,
        imap: str | None = ...,
        pop3: str | None = ...,
        smtp: str | None = ...,
        mapi: str | None = ...,
        msn_hotmail: str | None = ...,
        yahoo_mail: str | None = ...,
        gmail: str | None = ...,
        other_webmails: str | None = ...,
        spam_bword_threshold: int | None = ...,
        spam_bword_table: int | None = ...,
        spam_bal_table: int | None = ...,
        spam_mheader_table: int | None = ...,
        spam_rbl_table: int | None = ...,
        spam_iptrust_table: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        feature_set: Literal["flow", "proxy"] | None = ...,
        replacemsg_group: str | None = ...,
        spam_log: Literal["disable", "enable"] | None = ...,
        spam_log_fortiguard_response: Literal["disable", "enable"] | None = ...,
        spam_filtering: Literal["enable", "disable"] | None = ...,
        external: Literal["enable", "disable"] | None = ...,
        options: Literal["bannedword", "spambal", "spamfsip", "spamfssubmit", "spamfschksum", "spamfsurl", "spamhelodns", "spamraddrdns", "spamrbl", "spamhdrcheck", "spamfsphish"] | list[str] | None = ...,
        imap: str | None = ...,
        pop3: str | None = ...,
        smtp: str | None = ...,
        mapi: str | None = ...,
        msn_hotmail: str | None = ...,
        yahoo_mail: str | None = ...,
        gmail: str | None = ...,
        other_webmails: str | None = ...,
        spam_bword_threshold: int | None = ...,
        spam_bword_table: int | None = ...,
        spam_bal_table: int | None = ...,
        spam_mheader_table: int | None = ...,
        spam_rbl_table: int | None = ...,
        spam_iptrust_table: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ProfileObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        feature_set: Literal["flow", "proxy"] | None = ...,
        replacemsg_group: str | None = ...,
        spam_log: Literal["disable", "enable"] | None = ...,
        spam_log_fortiguard_response: Literal["disable", "enable"] | None = ...,
        spam_filtering: Literal["enable", "disable"] | None = ...,
        external: Literal["enable", "disable"] | None = ...,
        options: Literal["bannedword", "spambal", "spamfsip", "spamfssubmit", "spamfschksum", "spamfsurl", "spamhelodns", "spamraddrdns", "spamrbl", "spamhdrcheck", "spamfsphish"] | list[str] | None = ...,
        imap: str | None = ...,
        pop3: str | None = ...,
        smtp: str | None = ...,
        mapi: str | None = ...,
        msn_hotmail: str | None = ...,
        yahoo_mail: str | None = ...,
        gmail: str | None = ...,
        other_webmails: str | None = ...,
        spam_bword_threshold: int | None = ...,
        spam_bword_table: int | None = ...,
        spam_bal_table: int | None = ...,
        spam_mheader_table: int | None = ...,
        spam_rbl_table: int | None = ...,
        spam_iptrust_table: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        feature_set: Literal["flow", "proxy"] | None = ...,
        replacemsg_group: str | None = ...,
        spam_log: Literal["disable", "enable"] | None = ...,
        spam_log_fortiguard_response: Literal["disable", "enable"] | None = ...,
        spam_filtering: Literal["enable", "disable"] | None = ...,
        external: Literal["enable", "disable"] | None = ...,
        options: Literal["bannedword", "spambal", "spamfsip", "spamfssubmit", "spamfschksum", "spamfsurl", "spamhelodns", "spamraddrdns", "spamrbl", "spamhdrcheck", "spamfsphish"] | list[str] | None = ...,
        imap: str | None = ...,
        pop3: str | None = ...,
        smtp: str | None = ...,
        mapi: str | None = ...,
        msn_hotmail: str | None = ...,
        yahoo_mail: str | None = ...,
        gmail: str | None = ...,
        other_webmails: str | None = ...,
        spam_bword_threshold: int | None = ...,
        spam_bword_table: int | None = ...,
        spam_bal_table: int | None = ...,
        spam_mheader_table: int | None = ...,
        spam_rbl_table: int | None = ...,
        spam_iptrust_table: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        feature_set: Literal["flow", "proxy"] | None = ...,
        replacemsg_group: str | None = ...,
        spam_log: Literal["disable", "enable"] | None = ...,
        spam_log_fortiguard_response: Literal["disable", "enable"] | None = ...,
        spam_filtering: Literal["enable", "disable"] | None = ...,
        external: Literal["enable", "disable"] | None = ...,
        options: Literal["bannedword", "spambal", "spamfsip", "spamfssubmit", "spamfschksum", "spamfsurl", "spamhelodns", "spamraddrdns", "spamrbl", "spamhdrcheck", "spamfsphish"] | list[str] | None = ...,
        imap: str | None = ...,
        pop3: str | None = ...,
        smtp: str | None = ...,
        mapi: str | None = ...,
        msn_hotmail: str | None = ...,
        yahoo_mail: str | None = ...,
        gmail: str | None = ...,
        other_webmails: str | None = ...,
        spam_bword_threshold: int | None = ...,
        spam_bword_table: int | None = ...,
        spam_bal_table: int | None = ...,
        spam_mheader_table: int | None = ...,
        spam_rbl_table: int | None = ...,
        spam_iptrust_table: int | None = ...,
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
    ) -> ProfileObject: ...
    
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
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        feature_set: Literal["flow", "proxy"] | None = ...,
        replacemsg_group: str | None = ...,
        spam_log: Literal["disable", "enable"] | None = ...,
        spam_log_fortiguard_response: Literal["disable", "enable"] | None = ...,
        spam_filtering: Literal["enable", "disable"] | None = ...,
        external: Literal["enable", "disable"] | None = ...,
        options: Literal["bannedword", "spambal", "spamfsip", "spamfssubmit", "spamfschksum", "spamfsurl", "spamhelodns", "spamraddrdns", "spamrbl", "spamhdrcheck", "spamfsphish"] | list[str] | None = ...,
        imap: str | None = ...,
        pop3: str | None = ...,
        smtp: str | None = ...,
        mapi: str | None = ...,
        msn_hotmail: str | None = ...,
        yahoo_mail: str | None = ...,
        gmail: str | None = ...,
        other_webmails: str | None = ...,
        spam_bword_threshold: int | None = ...,
        spam_bword_table: int | None = ...,
        spam_bal_table: int | None = ...,
        spam_mheader_table: int | None = ...,
        spam_rbl_table: int | None = ...,
        spam_iptrust_table: int | None = ...,
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
    "Profile",
    "ProfilePayload",
    "ProfileObject",
]