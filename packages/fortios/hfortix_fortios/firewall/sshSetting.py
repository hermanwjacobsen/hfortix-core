"""Firewall SSH Setting Convenience Wrapper.

SSH Proxy Feature:
    FortiGate can inspect encrypted SSH traffic by acting as a
        man-in-the-middle
    proxy. These settings configure the global SSH proxy behavior, including
    which
    CAs and host keys to use for different SSH inspection scenarios.

Use Cases:
    - Configure SSH traffic inspection globally
    - Set trusted and untrusted CAs for SSH certificate validation
    - Assign host keys for different SSH proxy operations
    - Enable/disable host key trust checking
"""

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

from hfortix_fortios._helpers import (
    validate_enable_disable,
    validate_string_length,
)

if TYPE_CHECKING:
    from collections.abc import Coroutine

    from hfortix_fortios.client import FortiOS


class SSHSetting:
    """
    Convenience wrapper for SSH proxy global settings.

    Configures FortiGate's SSH proxy/inspection engine settings. This is the
    central
    configuration that ties together CAs, host keys, and trust policies for SSH
    traffic inspection.

    **SSH Proxy Overview:**

    FortiGate's SSH proxy performs man-in-the-middle inspection of SSH traffic
    to:

    - Decrypt and analyze SSH session content
    - Apply security policies (AV, DLP, IPS) to SSH traffic
    - Log SSH commands and file transfers for compliance
    - Detect threats hidden in encrypted SSH connections

    **Global Settings:**

    - **caname**: Primary CA for verifying SSH certificates (trusted)
    - **untrusted_caname**: Secondary CA for untrusted/revoked certificates
    - **hostkey_***: Different SSH host keys for various algorithms:

      - **rsa2048**: RSA 2048-bit key (most common)
      - **dsa1024**: DSA 1024-bit key (legacy)
      - **ecdsa256/384/521**: ECDSA keys with different curve sizes
      - **ed25519**: ED25519 key (modern, recommended)

    - **host_trusted_checking**: Enable/disable verification of server host
    keys

    **Configuration Workflow:**

    1. Create SSH local CA (if using certificate-based auth)
    2. Create SSH local keys for host key authentication
    3. Create SSH host keys for trusted servers
    4. Configure these global settings to use the created objects
    5. Apply SSH proxy policy in firewall rules

    **Trust Model:**

    - **Host Key Checking Enabled**: FortiGate validates server keys against
      ssh_host_key entries before allowing connections
    - **Host Key Checking Disabled**: FortiGate accepts any server key (less
    secure,
      but useful for dynamic environments)

    **Security Note:**

    SSH proxy requires clients to trust FortiGate's certificates/keys.
    Distribute
    the public keys/CAs to client systems to prevent MITM warnings.
    """

    def __init__(self, fortios_instance: "FortiOS") -> None:
        """Initialize the SSHSetting wrapper."""
        self._fgt = fortios_instance
        self._api = fortios_instance.api.cmdb.firewall.ssh.setting

    def get(
        self,
        vdom: Optional[str] = None,
        **kwargs: Any,
    ) -> Union[Dict[str, Any], "Coroutine[Any, Any, Dict[str, Any]]"]:
        """
        Get SSH proxy settings.

        Args:
            vdom: Virtual domain name
            **kwargs: Additional query parameters

        Returns:
            Dictionary containing SSH proxy settings

        Example:
            >>> # Get SSH proxy settings
            >>> settings = fgt.firewall.ssh_setting.get()
            >>> print(settings)
        """
        api_params: dict[str, Any] = {}
        if vdom:
            api_params["vdom"] = vdom
        api_params.update(kwargs)

        return self._api.get(**api_params)

    def update(
        self,
        caname: Optional[str] = None,
        untrusted_caname: Optional[str] = None,
        hostkey_rsa2048: Optional[str] = None,
        hostkey_dsa1024: Optional[str] = None,
        hostkey_ecdsa256: Optional[str] = None,
        hostkey_ecdsa384: Optional[str] = None,
        hostkey_ecdsa521: Optional[str] = None,
        hostkey_ed25519: Optional[str] = None,
        host_trusted_checking: Optional[str] = None,
        vdom: Optional[str] = None,
        **kwargs: Any,
    ) -> Union[Dict[str, Any], "Coroutine[Any, Any, Dict[str, Any]]"]:
        """
        Update SSH proxy settings.

        Args:
            caname: CA certificate used by SSH Inspection
            untrusted_caname: Untrusted CA certificate used by SSH Inspection
            hostkey_rsa2048: RSA certificate used by SSH proxy
            hostkey_dsa1024: DSA certificate used by SSH proxy
            hostkey_ecdsa256: ECDSA nid256 certificate used by SSH proxy
            hostkey_ecdsa384: ECDSA nid384 certificate used by SSH proxy
            hostkey_ecdsa521: ECDSA nid521 certificate used by SSH proxy
            hostkey_ed25519: ED25519 hostkey used by SSH proxy
            host_trusted_checking: Enable/disable host trusted checking
                                   (Options: enable, disable)
            vdom: Virtual domain name
            **kwargs: Additional parameters

        Returns:
            Dictionary containing API response

        Example:
            >>> # Update SSH proxy settings
            >>> result = fgt.firewall.ssh_setting.update(
            ...     caname="my-ca",
            ...     host_trusted_checking="enable",
            ...     hostkey_rsa2048="rsa-key"
            ... )
        """
        # Validate string lengths (max 35 chars for all string parameters)
        for param_name, value in [
            ("caname", caname),
            ("untrusted_caname", untrusted_caname),
            ("hostkey_rsa2048", hostkey_rsa2048),
            ("hostkey_dsa1024", hostkey_dsa1024),
            ("hostkey_ecdsa256", hostkey_ecdsa256),
            ("hostkey_ecdsa384", hostkey_ecdsa384),
            ("hostkey_ecdsa521", hostkey_ecdsa521),
            ("hostkey_ed25519", hostkey_ed25519),
        ]:
            validate_string_length(value, 35, param_name)

        # Validate enable/disable enum
        validate_enable_disable(host_trusted_checking, "host_trusted_checking")

        data: dict[str, Any] = {}

        if caname is not None:
            data["caname"] = caname
        if untrusted_caname is not None:
            data["untrusted-caname"] = untrusted_caname
        if hostkey_rsa2048 is not None:
            data["hostkey-rsa2048"] = hostkey_rsa2048
        if hostkey_dsa1024 is not None:
            data["hostkey-dsa1024"] = hostkey_dsa1024
        if hostkey_ecdsa256 is not None:
            data["hostkey-ecdsa256"] = hostkey_ecdsa256
        if hostkey_ecdsa384 is not None:
            data["hostkey-ecdsa384"] = hostkey_ecdsa384
        if hostkey_ecdsa521 is not None:
            data["hostkey-ecdsa521"] = hostkey_ecdsa521
        if hostkey_ed25519 is not None:
            data["hostkey-ed25519"] = hostkey_ed25519
        if host_trusted_checking is not None:
            data["host-trusted-checking"] = host_trusted_checking

        api_params: dict[str, Any] = {}
        if vdom:
            api_params["vdom"] = vdom
        api_params.update(kwargs)

        return self._api.put(data, **api_params)
