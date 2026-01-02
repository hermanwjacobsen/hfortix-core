"""Firewall SSH Host Key Convenience Wrapper.

SSH Proxy Feature:
    FortiGate can inspect encrypted SSH traffic by acting as a
    man-in-the-middle proxy. Host keys are used to verify the identity of
    SSH servers that clients connect to, similar to the ~/.ssh/known_hosts
    file.

Use Cases:
    - SSH traffic inspection for threat detection
    - Data Loss Prevention (DLP) in SSH sessions
    - Compliance monitoring of SSH connections
    - SSH access proxy for secure remote access
"""

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

from hfortix_fortios._helpers import (
    validate_port_number,
    validate_ssh_host_key_nid,
    validate_ssh_host_key_status,
    validate_ssh_host_key_type,
    validate_ssh_host_key_usage,
    validate_string_length,
)

if TYPE_CHECKING:
    from collections.abc import Coroutine

    from hfortix_fortios.client import FortiOS


class SSHHostKey:
    """
    Convenience wrapper for SSH proxy host public keys.

    Manages trusted SSH server public keys for SSH proxy/inspection. When
    FortiGate acts as an SSH proxy, it verifies remote SSH servers using
    these stored public keys, similar to how SSH clients use known_hosts
    files.

    **SSH Proxy Overview:**

    FortiGate's SSH proxy performs man-in-the-middle inspection of SSH
    traffic to:

    - Detect threats in encrypted SSH sessions
    - Apply DLP policies to SSH file transfers (SCP/SFTP)
    - Monitor and log SSH commands for compliance
    - Enforce security policies on SSH protocols

    **Host Key Trust Workflow:**

    1. Client initiates SSH connection through FortiGate
    2. FortiGate intercepts connection and verifies server's host key
    3. If key matches a trusted entry here, connection proceeds
    4. FortiGate establishes separate encrypted sessions with client and server
    5. Traffic inspection occurs in the middle

    **Key Management:**

    - **trusted**: Normal operation - connection allowed
    - **revoked**: Block connections to this server
    """

    def __init__(self, fortios_instance: "FortiOS") -> None:
        """Initialize the SSHHostKey wrapper."""
        self._fgt = fortios_instance
        self._api = fortios_instance.api.cmdb.firewall.ssh.host_key

    def get(
        self,
        name: Optional[str] = None,
        vdom: Optional[str] = None,
        **kwargs: Any,
    ) -> Union[Dict[str, Any], "Coroutine[Any, Any, Dict[str, Any]]"]:
        """
        Get SSH host key(s).

        Args:
            name: Host key name to retrieve. If None, returns all host keys.
            vdom: Virtual domain name
            **kwargs: Additional query parameters

        Returns:
            Dictionary containing host key configuration(s)

        Example:
            >>> # Get all SSH host keys
            >>> keys = fgt.firewall.ssh_host_key.get()
            >>>
            >>> # Get specific host key
            >>> key = fgt.firewall.ssh_host_key.get(name="server1")
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
        public_key: str,
        type: str = "RSA",
        status: str = "trusted",
        ip: Optional[str] = None,
        port: Optional[int] = None,
        hostname: Optional[str] = None,
        nid: Optional[str] = None,
        usage: Optional[str] = None,
        vdom: Optional[str] = None,
        **kwargs: Any,
    ) -> Union[Dict[str, Any], "Coroutine[Any, Any, Dict[str, Any]]"]:
        """
        Create a new SSH host key.

        Args:
            name: Host key name
            public_key: SSH public key
            type: Key type. Options: RSA, DSA, ECDSA, ED25519, RSA-CA, DSA-CA,
                  ECDSA-CA, ED25519-CA (default: RSA)
            status: Key status. Options: trusted, revoked (default: trusted)
            ip: IP address of SSH server
            port: Port of SSH server
            hostname: Hostname of SSH server
            nid: ECDSA key nid. Options: 256, 384, 521
            usage: Key usage. Options: transparent-proxy, access-proxy
            vdom: Virtual domain name
            **kwargs: Additional parameters

        Returns:
            Dictionary containing API response

        Example:
            >>> # Create SSH host key
            >>> result = fgt.firewall.ssh_host_key.create(
            ...     name="server1",
            ...     public_key="ssh-rsa AAAAB3NzaC1yc2EA...",
            ...     type="RSA",
            ...     ip="192.168.1.100",
            ...     port=22
            ... )
        """
        # Validate string lengths
        validate_string_length(name, 35, "name")
        validate_string_length(public_key, 32768, "public_key")
        validate_string_length(hostname, 255, "hostname")

        # Validate enum values
        validate_ssh_host_key_type(type)
        validate_ssh_host_key_status(status)
        validate_ssh_host_key_nid(nid)
        validate_ssh_host_key_usage(usage)

        # Validate port range
        validate_port_number(port, "port")

        data: dict[str, Any] = {
            "name": name,
            "public-key": public_key,
            "type": type,
            "status": status,
        }

        if ip is not None:
            data["ip"] = ip
        if port is not None:
            data["port"] = port
        if hostname is not None:
            data["hostname"] = hostname
        if nid is not None:
            data["nid"] = nid
        if usage is not None:
            data["usage"] = usage

        api_params: dict[str, Any] = {}
        if vdom:
            api_params["vdom"] = vdom
        api_params.update(kwargs)

        return self._api.post(data, **api_params)

    def update(
        self,
        name: str,
        public_key: Optional[str] = None,
        type: Optional[str] = None,
        status: Optional[str] = None,
        ip: Optional[str] = None,
        port: Optional[int] = None,
        hostname: Optional[str] = None,
        nid: Optional[str] = None,
        usage: Optional[str] = None,
        vdom: Optional[str] = None,
        **kwargs: Any,
    ) -> Union[Dict[str, Any], "Coroutine[Any, Any, Dict[str, Any]]"]:
        """
        Update an existing SSH host key.

        Args:
            name: Host key name to update
            public_key: SSH public key
            type: Key type. Options: RSA, DSA, ECDSA, ED25519, RSA-CA, DSA-CA,
                  ECDSA-CA, ED25519-CA
            status: Key status. Options: trusted, revoked
            ip: IP address of SSH server
            port: Port of SSH server
            hostname: Hostname of SSH server
            nid: ECDSA key nid. Options: 256, 384, 521
            usage: Key usage. Options: transparent-proxy, access-proxy
            vdom: Virtual domain name
            **kwargs: Additional parameters

        Returns:
            Dictionary containing API response

        Example:
            >>> # Update SSH host key status
            >>> result = fgt.firewall.ssh_host_key.update(
            ...     name="server1",
            ...     status="revoked"
            ... )
        """
        # Validate string lengths
        validate_string_length(name, 35, "name")
        validate_string_length(public_key, 32768, "public_key")
        validate_string_length(hostname, 255, "hostname")

        # Validate enum values
        validate_ssh_host_key_type(type)
        validate_ssh_host_key_status(status)
        validate_ssh_host_key_nid(nid)
        validate_ssh_host_key_usage(usage)

        # Validate port range
        validate_port_number(port, "port")

        data: dict[str, Any] = {}

        if public_key is not None:
            data["public-key"] = public_key
        if type is not None:
            data["type"] = type
        if status is not None:
            data["status"] = status
        if ip is not None:
            data["ip"] = ip
        if port is not None:
            data["port"] = port
        if hostname is not None:
            data["hostname"] = hostname
        if nid is not None:
            data["nid"] = nid
        if usage is not None:
            data["usage"] = usage

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
        Delete an SSH host key.

        Args:
            name: Host key name to delete
            vdom: Virtual domain name
            **kwargs: Additional parameters

        Returns:
            Dictionary containing API response

        Example:
            >>> # Delete SSH host key
            >>> result = fgt.firewall.ssh_host_key.delete(name="server1")
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
        Check if an SSH host key exists.

        Args:
            name: Host key name to check
            vdom: Virtual domain name
            **kwargs: Additional parameters

        Returns:
            True if host key exists, False otherwise

        Example:
            >>> if fgt.firewall.ssh_host_key.exists(name="server1"):
            ...     print("Host key exists")
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
