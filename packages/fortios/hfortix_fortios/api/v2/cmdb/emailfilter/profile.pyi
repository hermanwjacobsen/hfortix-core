from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class ProfilePayload(TypedDict, total=False):
    """
    Type hints for emailfilter/profile payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
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


class Profile:
    """
    Configure Email Filter profiles.
    
    Path: emailfilter/profile
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
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        feature_set: Literal["flow", "proxy"] | None = ...,
        replacemsg_group: str | None = ...,
        spam_log: Literal["disable", "enable"] | None = ...,
        spam_log_fortiguard_response: Literal["disable", "enable"] | None = ...,
        spam_filtering: Literal["enable", "disable"] | None = ...,
        external: Literal["enable", "disable"] | None = ...,
        options: Literal["bannedword", "spambal", "spamfsip", "spamfssubmit", "spamfschksum", "spamfsurl", "spamhelodns", "spamraddrdns", "spamrbl", "spamhdrcheck", "spamfsphish"] | None = ...,
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
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
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
        options: Literal["bannedword", "spambal", "spamfsip", "spamfssubmit", "spamfschksum", "spamfsurl", "spamhelodns", "spamraddrdns", "spamrbl", "spamhdrcheck", "spamfsphish"] | None = ...,
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
        payload_dict: ProfilePayload | None = ...,
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