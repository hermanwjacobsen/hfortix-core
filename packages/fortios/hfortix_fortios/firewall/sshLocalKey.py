"""Firewall SSH Local Key Convenience Wrapper.

SSH Proxy Feature:
    FortiGate can inspect encrypted SSH traffic by acting as a
        man-in-the-middle
    proxy. Local keys are the SSH keypairs that FortiGate uses to authenticate
    itself as an SSH server when proxying client connections.

Use Cases:
    - SSH traffic inspection with host-based authentication
    - Transparent SSH proxy where FortiGate impersonates the destination server
    - SSH access proxy for secure remote access
"""

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

from hfortix_fortios._helpers import validate_string_length

if TYPE_CHECKING:
    from collections.abc import Coroutine

    from hfortix_fortios.client import FortiOS


class SSHLocalKey:
    """
    Convenience wrapper for SSH proxy local keys.

    Manages SSH host keypairs that FortiGate uses when acting as an SSH server
    during proxy/inspection operations. These are the keys presented to clients
    when FortiGate intercepts SSH connections.

    **SSH Proxy Overview:**

    FortiGate's SSH proxy performs man-in-the-middle inspection of SSH traffic
    to:

    - Decrypt and inspect SSH session content
    - Apply DLP policies to SSH file transfers (SCP/SFTP)
    - Log SSH commands for audit and compliance
    - Detect malware and threats in SSH traffic

    **Local Key Purpose:**

    When a client connects to an SSH server through FortiGate proxy:

    1. Client initiates SSH connection
    2. FortiGate intercepts and presents this local key as if it were the
    server
    3. Client authenticates FortiGate using this key (must be in client's
    known_hosts)
    4. FortiGate establishes separate connection to real server
    5. Traffic flows through FortiGate for inspection

    **Key Types Supported:**

    - RSA (2048-bit or higher recommended)
    - DSA (legacy, not recommended)
    - ECDSA (256, 384, 521-bit curves)
    - ED25519 (modern, recommended)

    **Key Management:**

    - **Auto-generated**: FortiGate creates a keypair automatically
    (recommended)
    - **User-provided**: Import existing private/public key (PEM format,
    password-protected)

    **Security Note:**

    Private keys must be password-protected. The public key from this keypair
    should be added to SSH clients' known_hosts to prevent MITM warnings.
    """

    def __init__(self, fortios_instance: "FortiOS") -> None:
        """Initialize the SSHLocalKey wrapper."""
        self._fgt = fortios_instance
        self._api = fortios_instance.api.cmdb.firewall.ssh.local_key

    def get(
        self,
        name: Optional[str] = None,
        vdom: Optional[str] = None,
        **kwargs: Any,
    ) -> Union[Dict[str, Any], "Coroutine[Any, Any, Dict[str, Any]]"]:
        """
        Get SSH local key(s).

        Args:
            name: Key name to retrieve. If None, returns all keys.
            vdom: Virtual domain name
            **kwargs: Additional query parameters

        Returns:
            Dictionary containing key configuration(s)

        Example:
            >>> # Get all SSH local keys
            >>> keys = fgt.firewall.ssh_local_key.get()
            >>>
            >>> # Get specific key
            >>> key = fgt.firewall.ssh_local_key.get(name="my-key")
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
        private_key: Optional[str] = None,
        public_key: Optional[str] = None,
        password: Optional[str] = None,
        vdom: Optional[str] = None,
        **kwargs: Any,
    ) -> Union[Dict[str, Any], "Coroutine[Any, Any, Dict[str, Any]]"]:
        """
        Create a new SSH local key.

        Args:
            name: Key name
            private_key: SSH proxy private key (PEM format, encrypted
                with password)
            public_key: SSH proxy public key
            password: Password for SSH private key
            vdom: Virtual domain name
            **kwargs: Additional parameters

        Returns:
            Dictionary containing API response

        Example:
            >>> # Create SSH local key with auto-generated keypair
            >>> result = fgt.firewall.ssh_local_key.create(
            ...     name="auto-key"
            ... )
            >>>
            >>> # Create SSH local key with user-provided keys
            >>> result = fgt.firewall.ssh_local_key.create(
            ...     name="custom-key",
            ...     private_key="-----BEGIN RSA PRIVATE KEY-----\\n...",
            ...     public_key="ssh-rsa AAAAB3NzaC1yc2EA...",
            ...     password="mypassword"
            ... )
        """
        # Validate inputs
        validate_string_length(name, 35, "name")

        data: dict[str, Any] = {
            "name": name,
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
        private_key: Optional[str] = None,
        public_key: Optional[str] = None,
        password: Optional[str] = None,
        vdom: Optional[str] = None,
        **kwargs: Any,
    ) -> Union[Dict[str, Any], "Coroutine[Any, Any, Dict[str, Any]]"]:
        """
        Update an existing SSH local key.

        Args:
            name: Key name to update
            private_key: SSH proxy private key (PEM format, encrypted
                with password)
            public_key: SSH proxy public key
            password: Password for SSH private key
            vdom: Virtual domain name
            **kwargs: Additional parameters

        Returns:
            Dictionary containing API response

        Example:
            >>> # Update SSH local key password
            >>> result = fgt.firewall.ssh_local_key.update(
            ...     name="my-key",
            ...     password="newpassword"
            ... )
        """
        # Validate inputs
        validate_string_length(name, 35, "name")

        data: dict[str, Any] = {}

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
        Delete an SSH local key.

        Args:
            name: Key name to delete
            vdom: Virtual domain name
            **kwargs: Additional parameters

        Returns:
            Dictionary containing API response

        Example:
            >>> # Delete SSH local key
            >>> result = fgt.firewall.ssh_local_key.delete(name="my-key")
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
        Check if an SSH local key exists.

        Args:
            name: Key name to check
            vdom: Virtual domain name
            **kwargs: Additional parameters

        Returns:
            True if key exists, False otherwise

        Example:
            >>> if fgt.firewall.ssh_local_key.exists(name="my-key"):
            ...     print("Key exists")
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
