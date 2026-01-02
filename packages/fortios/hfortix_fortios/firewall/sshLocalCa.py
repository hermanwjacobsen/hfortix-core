"""Firewall SSH Local CA Convenience Wrapper.

SSH Proxy Feature:
    FortiGate can inspect encrypted SSH traffic by acting as a
        man-in-the-middle
    proxy. Local CAs provide the certificate authority keys that FortiGate uses
    to sign temporary certificates during SSH session interception.

Use Cases:
    - SSH traffic inspection with certificate-based authentication
    - Transparent SSH proxy for client certificate validation
    - SSH access proxy with custom CA for enterprise environments
"""

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

from hfortix_fortios._helpers import (
    validate_ssh_source,
    validate_string_length,
)

if TYPE_CHECKING:
    from collections.abc import Coroutine

    from hfortix_fortios.client import FortiOS


class SSHLocalCA:
    """
    Convenience wrapper for SSH proxy local certificate authority.

    Manages Certificate Authority (CA) keys for SSH proxy certificate
    operations.
    When FortiGate performs SSH inspection with certificate-based
    authentication,
    it uses these CA keys to sign temporary certificates presented to clients.

    **SSH Proxy Overview:**

    FortiGate's SSH proxy performs man-in-the-middle inspection of SSH traffic
    to:

    - Inspect SSH sessions using certificate authentication
    - Validate client certificates against trusted CAs
    - Apply security policies to certificate-based SSH connections
    - Monitor SSH traffic for compliance and threat detection

    **Local CA Purpose:**

    The Local CA is used when FortiGate needs to:

    1. **Act as SSH Server to Client**: FortiGate presents a certificate signed
    by
       this CA to the SSH client during the handshake
    2. **Sign User Certificates**: For SSH access proxy scenarios, FortiGate
    can
       sign user certificates on-the-fly
    3. **Trust Anchor**: Clients configure this CA as trusted to accept
    FortiGate's
       proxy certificates

    **Source Types:**

    - **built-in**: FortiGate generates and manages the key pair automatically
    - **user**: Import your own CA private/public key (PEM format, encrypted
    with password)

    **Security Note:**

    The private key must be password-protected. This CA should be distributed
    to
    SSH clients that will accept FortiGate's proxy certificates.
    """

    def __init__(self, fortios_instance: "FortiOS") -> None:
        """Initialize the SSHLocalCA wrapper."""
        self._fgt = fortios_instance
        self._api = fortios_instance.api.cmdb.firewall.ssh.local_ca

    def get(
        self,
        name: Optional[str] = None,
        vdom: Optional[str] = None,
        **kwargs: Any,
    ) -> Union[Dict[str, Any], "Coroutine[Any, Any, Dict[str, Any]]"]:
        """
        Get SSH local CA(s).

        Args:
            name: CA name to retrieve. If None, returns all CAs.
            vdom: Virtual domain name
            **kwargs: Additional query parameters

        Returns:
            Dictionary containing CA configuration(s)

        Example:
            >>> # Get all SSH local CAs
            >>> cas = fgt.firewall.ssh_local_ca.get()
            >>>
            >>> # Get specific CA
            >>> ca = fgt.firewall.ssh_local_ca.get(name="my-ca")
        """
        api_params: dict[str, Any] = {}
        if vdom:
            api_params["vdom"] = vdom
        api_params.update(kwargs)

        if name is not None:
            return self._api.get(name, **api_params)
        return self._api.get(**api_params)

    def create(
        self,
        name: str,
        source: str = "built-in",
        private_key: Optional[str] = None,
        public_key: Optional[str] = None,
        password: Optional[str] = None,
        vdom: Optional[str] = None,
        **kwargs: Any,
    ) -> Union[Dict[str, Any], "Coroutine[Any, Any, Dict[str, Any]]"]:
        """
        Create a new SSH local CA.

        Args:
            name: CA name
            source: CA source type. Options: built-in, user
                (default: built-in)
            private_key: SSH proxy private key (PEM format, encrypted
                with password)
            public_key: SSH proxy public key
            password: Password for SSH private key
            vdom: Virtual domain name
            **kwargs: Additional parameters

        Returns:
            Dictionary containing API response

        Example:
            >>> # Create SSH local CA with built-in key generation
            >>> result = fgt.firewall.ssh_local_ca.create(
            ...     name="my-ca",
            ...     source="built-in"
            ... )
            >>>
            >>> # Create SSH local CA with user-provided keys
            >>> result = fgt.firewall.ssh_local_ca.create(
            ...     name="custom-ca",
            ...     source="user",
            ...     private_key="-----BEGIN RSA PRIVATE KEY-----\\n...",
            ...     public_key="ssh-rsa AAAAB3NzaC1yc2EA...",
            ...     password="mypassword"
            ... )
        """
        # Validate inputs
        validate_string_length(name, 35, "name")
        validate_ssh_source(source)

        data: dict[str, Any] = {
            "name": name,
            "source": source,
        }

        if private_key is not None:
            data["private-key"] = private_key
        if public_key is not None:
            data["public-key"] = public_key
        if password is not None:
            data["password"] = password

        api_params: dict[str, Any] = {}
        if vdom:
            api_params["vdom"] = vdom
        api_params.update(kwargs)

        return self._api.post(data, **api_params)

    def update(
        self,
        name: str,
        source: Optional[str] = None,
        private_key: Optional[str] = None,
        public_key: Optional[str] = None,
        password: Optional[str] = None,
        vdom: Optional[str] = None,
        **kwargs: Any,
    ) -> Union[Dict[str, Any], "Coroutine[Any, Any, Dict[str, Any]]"]:
        """
        Update an existing SSH local CA.

        Args:
            name: CA name to update
            source: CA source type. Options: built-in, user
            private_key: SSH proxy private key (PEM format, encrypted
                with password)
            public_key: SSH proxy public key
            password: Password for SSH private key
            vdom: Virtual domain name
            **kwargs: Additional parameters

        Returns:
            Dictionary containing API response

        Example:
            >>> # Update SSH local CA password
            >>> result = fgt.firewall.ssh_local_ca.update(
            ...     name="my-ca",
            ...     password="newpassword"
            ... )
        """
        # Validate inputs
        validate_string_length(name, 35, "name")
        validate_ssh_source(source)

        data: dict[str, Any] = {}

        if source is not None:
            data["source"] = source
        if private_key is not None:
            data["private-key"] = private_key
        if public_key is not None:
            data["public-key"] = public_key
        if password is not None:
            data["password"] = password

        api_params: dict[str, Any] = {}
        if vdom:
            api_params["vdom"] = vdom
        api_params.update(kwargs)

        return self._api.put(name, data, **api_params)

    def delete(
        self,
        name: str,
        vdom: Optional[str] = None,
        **kwargs: Any,
    ) -> Union[Dict[str, Any], "Coroutine[Any, Any, Dict[str, Any]]"]:
        """
        Delete an SSH local CA.

        Args:
            name: CA name to delete
            vdom: Virtual domain name
            **kwargs: Additional parameters

        Returns:
            Dictionary containing API response

        Example:
            >>> # Delete SSH local CA
            >>> result = fgt.firewall.ssh_local_ca.delete(name="my-ca")
        """
        api_params: dict[str, Any] = {}
        if vdom:
            api_params["vdom"] = vdom
        api_params.update(kwargs)

        return self._api.delete(name, **api_params)

    def exists(
        self,
        name: str,
        vdom: Optional[str] = None,
        **kwargs: Any,
    ) -> Union[bool, "Coroutine[Any, Any, bool]"]:
        """
        Check if an SSH local CA exists.

        Args:
            name: CA name to check
            vdom: Virtual domain name
            **kwargs: Additional parameters

        Returns:
            True if CA exists, False otherwise

        Example:
            >>> if fgt.firewall.ssh_local_ca.exists(name="my-ca"):
            ...     print("CA exists")
        """
        api_params: dict[str, Any] = {}
        if vdom:
            api_params["vdom"] = vdom
        api_params.update(kwargs)

        try:
            self._api.get(name, **api_params)
            return True
        except Exception:
            return False
