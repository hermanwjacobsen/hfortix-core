from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class SshConfigPayload(TypedDict, total=False):
    """
    Type hints for system/ssh_config payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: SshConfigPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    ssh_kex_algo: NotRequired[Literal["diffie-hellman-group1-sha1", "diffie-hellman-group14-sha1", "diffie-hellman-group14-sha256", "diffie-hellman-group16-sha512", "diffie-hellman-group18-sha512", "diffie-hellman-group-exchange-sha1", "diffie-hellman-group-exchange-sha256", "curve25519-sha256@libssh.org", "ecdh-sha2-nistp256", "ecdh-sha2-nistp384", "ecdh-sha2-nistp521"]]  # Select one or more SSH kex algorithms.
    ssh_enc_algo: NotRequired[Literal["chacha20-poly1305@openssh.com", "aes128-ctr", "aes192-ctr", "aes256-ctr", "arcfour256", "arcfour128", "aes128-cbc", "3des-cbc", "blowfish-cbc", "cast128-cbc", "aes192-cbc", "aes256-cbc", "arcfour", "rijndael-cbc@lysator.liu.se", "aes128-gcm@openssh.com", "aes256-gcm@openssh.com"]]  # Select one or more SSH ciphers.
    ssh_mac_algo: NotRequired[Literal["hmac-md5", "hmac-md5-etm@openssh.com", "hmac-md5-96", "hmac-md5-96-etm@openssh.com", "hmac-sha1", "hmac-sha1-etm@openssh.com", "hmac-sha2-256", "hmac-sha2-256-etm@openssh.com", "hmac-sha2-512", "hmac-sha2-512-etm@openssh.com", "hmac-ripemd160", "hmac-ripemd160@openssh.com", "hmac-ripemd160-etm@openssh.com", "umac-64@openssh.com", "umac-128@openssh.com", "umac-64-etm@openssh.com", "umac-128-etm@openssh.com"]]  # Select one or more SSH MAC algorithms.
    ssh_hsk_algo: NotRequired[Literal["ssh-rsa", "ecdsa-sha2-nistp521", "ecdsa-sha2-nistp384", "ecdsa-sha2-nistp256", "rsa-sha2-256", "rsa-sha2-512", "ssh-ed25519"]]  # Select one or more SSH hostkey algorithms.
    ssh_hsk_override: NotRequired[Literal["disable", "enable"]]  # Enable/disable SSH host key override in SSH daemon.
    ssh_hsk_password: NotRequired[str]  # Password for ssh-hostkey.
    ssh_hsk: str  # Config SSH host key.


class SshConfig:
    """
    Configure SSH config.
    
    Path: system/ssh_config
    Category: cmdb
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
        payload_dict: SshConfigPayload | None = ...,
        ssh_kex_algo: Literal["diffie-hellman-group1-sha1", "diffie-hellman-group14-sha1", "diffie-hellman-group14-sha256", "diffie-hellman-group16-sha512", "diffie-hellman-group18-sha512", "diffie-hellman-group-exchange-sha1", "diffie-hellman-group-exchange-sha256", "curve25519-sha256@libssh.org", "ecdh-sha2-nistp256", "ecdh-sha2-nistp384", "ecdh-sha2-nistp521"] | None = ...,
        ssh_enc_algo: Literal["chacha20-poly1305@openssh.com", "aes128-ctr", "aes192-ctr", "aes256-ctr", "arcfour256", "arcfour128", "aes128-cbc", "3des-cbc", "blowfish-cbc", "cast128-cbc", "aes192-cbc", "aes256-cbc", "arcfour", "rijndael-cbc@lysator.liu.se", "aes128-gcm@openssh.com", "aes256-gcm@openssh.com"] | None = ...,
        ssh_mac_algo: Literal["hmac-md5", "hmac-md5-etm@openssh.com", "hmac-md5-96", "hmac-md5-96-etm@openssh.com", "hmac-sha1", "hmac-sha1-etm@openssh.com", "hmac-sha2-256", "hmac-sha2-256-etm@openssh.com", "hmac-sha2-512", "hmac-sha2-512-etm@openssh.com", "hmac-ripemd160", "hmac-ripemd160@openssh.com", "hmac-ripemd160-etm@openssh.com", "umac-64@openssh.com", "umac-128@openssh.com", "umac-64-etm@openssh.com", "umac-128-etm@openssh.com"] | None = ...,
        ssh_hsk_algo: Literal["ssh-rsa", "ecdsa-sha2-nistp521", "ecdsa-sha2-nistp384", "ecdsa-sha2-nistp256", "rsa-sha2-256", "rsa-sha2-512", "ssh-ed25519"] | None = ...,
        ssh_hsk_override: Literal["disable", "enable"] | None = ...,
        ssh_hsk_password: str | None = ...,
        ssh_hsk: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: SshConfigPayload | None = ...,
        ssh_kex_algo: Literal["diffie-hellman-group1-sha1", "diffie-hellman-group14-sha1", "diffie-hellman-group14-sha256", "diffie-hellman-group16-sha512", "diffie-hellman-group18-sha512", "diffie-hellman-group-exchange-sha1", "diffie-hellman-group-exchange-sha256", "curve25519-sha256@libssh.org", "ecdh-sha2-nistp256", "ecdh-sha2-nistp384", "ecdh-sha2-nistp521"] | None = ...,
        ssh_enc_algo: Literal["chacha20-poly1305@openssh.com", "aes128-ctr", "aes192-ctr", "aes256-ctr", "arcfour256", "arcfour128", "aes128-cbc", "3des-cbc", "blowfish-cbc", "cast128-cbc", "aes192-cbc", "aes256-cbc", "arcfour", "rijndael-cbc@lysator.liu.se", "aes128-gcm@openssh.com", "aes256-gcm@openssh.com"] | None = ...,
        ssh_mac_algo: Literal["hmac-md5", "hmac-md5-etm@openssh.com", "hmac-md5-96", "hmac-md5-96-etm@openssh.com", "hmac-sha1", "hmac-sha1-etm@openssh.com", "hmac-sha2-256", "hmac-sha2-256-etm@openssh.com", "hmac-sha2-512", "hmac-sha2-512-etm@openssh.com", "hmac-ripemd160", "hmac-ripemd160@openssh.com", "hmac-ripemd160-etm@openssh.com", "umac-64@openssh.com", "umac-128@openssh.com", "umac-64-etm@openssh.com", "umac-128-etm@openssh.com"] | None = ...,
        ssh_hsk_algo: Literal["ssh-rsa", "ecdsa-sha2-nistp521", "ecdsa-sha2-nistp384", "ecdsa-sha2-nistp256", "rsa-sha2-256", "rsa-sha2-512", "ssh-ed25519"] | None = ...,
        ssh_hsk_override: Literal["disable", "enable"] | None = ...,
        ssh_hsk_password: str | None = ...,
        ssh_hsk: str | None = ...,
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
        payload_dict: SshConfigPayload | None = ...,
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