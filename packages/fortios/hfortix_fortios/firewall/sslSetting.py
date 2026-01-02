"""Firewall SSL Setting Convenience Wrapper.

SSL/TLS Inspection Feature:
    FortiGate can inspect encrypted HTTPS/SSL traffic by acting as a
    man-in-the-middle
    proxy. These settings configure the global SSL/TLS inspection engine
    behavior,
    including cryptographic parameters, caching, and performance tuning.

Use Cases:
    - Configure SSL/TLS deep packet inspection globally
    - Tune SSL proxy performance (caching, queue thresholds)
    - Set cryptographic parameters (DH bits, cipher handling)
    - Optimize certificate caching for high-traffic environments
"""

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

from hfortix_fortios._helpers import (
    validate_enable_disable,
    validate_integer_range,
    validate_ssl_cipher_action,
    validate_ssl_dh_bits,
)

if TYPE_CHECKING:
    from collections.abc import Coroutine

    from hfortix_fortios.client import FortiOS


class SSLSetting:
    """
    Convenience wrapper for SSL/TLS proxy global settings.

    Configures FortiGate's SSL/TLS inspection engine for HTTPS traffic. SSL
    inspection
    allows FortiGate to decrypt, inspect, and re-encrypt SSL/TLS traffic to
    detect
    threats hidden in encrypted connections.

    **SSL/TLS Inspection Overview:**

    FortiGate's SSL proxy performs man-in-the-middle inspection to:

    - Decrypt HTTPS traffic for security scanning
    - Apply AV, DLP, IPS, and web filtering to encrypted traffic
    - Detect malware downloads over HTTPS
    - Block malicious SSL/TLS connections (C2 traffic, data exfiltration)
    - Monitor encrypted traffic for compliance

    **How SSL Inspection Works:**

    1. Client initiates HTTPS connection to server
    2. FortiGate intercepts connection
    3. FortiGate establishes SSL session with server (using server's real
    certificate)
    4. FortiGate presents re-signed certificate to client (signed by FortiGate
    CA)
    5. Client accepts FortiGate's certificate (if FortiGate CA is trusted)
    6. Traffic decrypted, inspected, and re-encrypted in both directions

    **Global Settings:**

    **Connection Settings:**

    - **proxy_connect_timeout**: Timeout for internal proxy process connections
    (1-60s)
    - **ssl_dh_bits**: Diffie-Hellman key size for DHE ciphers
    (768/1024/1536/2048)
    - **ssl_send_empty_frags**: Send empty fragments to prevent CBC IV attacks
    (SSL 3.0/TLS 1.0)
    - **no_matching_cipher_action**: What to do when no cipher match
    (bypass/drop)
    - **abbreviate_handshake**: Enable abbreviated SSL handshake for
    performance

    **Certificate Caching:**

    - **cert_manager_cache_timeout**: How long to cache re-signed certificates
    (24-720 hours)
    - **resigned_short_lived_certificate**: Enable/disable short-lived
    certificate optimization
    - **cert_cache_capacity**: Max cached host certificates (0-500, default
    200)
    - **cert_cache_timeout**: Certificate cache TTL (1-120 min, default 10)

    **Session Caching:**

    - **session_cache_capacity**: SSL session cache size (1-1000, obsolete)
    - **session_cache_timeout**: Session state cache TTL (1-60 min, default 20)

    **Performance Tuning:**

    - **kxp_queue_threshold**: Key exchange processor queue limit (0-512,
    default 16)
    - **ssl_queue_threshold**: SSL processor queue limit (0-512, default 32)

    When queues fill up, FortiGate offloads crypto operations to main CPU.

    **Security Considerations:**

    1. **Client Trust**: Clients must trust FortiGate's CA certificate to avoid
    warnings
    2. **Certificate Pinning**: Sites with cert pinning will fail inspection
    (use bypass)
    3. **Mutual TLS**: Client certificate auth requires special configuration
    4. **Performance**: SSL inspection is CPU-intensive, tune caching for your
    traffic

    **Best Practices:**

    - Use 2048-bit DH minimum for modern security
    - Enable cert caching to reduce CPU load
    - Monitor queue thresholds and CPU usage
    - Bypass inspection for trusted sites to improve performance
    - Distribute FortiGate CA to all client devices
    """

    def __init__(self, fortios_instance: "FortiOS") -> None:
        """Initialize the SSLSetting wrapper."""
        self._fgt = fortios_instance
        self._api = fortios_instance.api.cmdb.firewall.ssl.setting

    def get(
        self,
        vdom: Optional[str] = None,
        **kwargs: Any,
    ) -> Union[Dict[str, Any], "Coroutine[Any, Any, Dict[str, Any]]"]:
        """
        Get SSL proxy settings.

        Args:
            vdom: Virtual domain name
            **kwargs: Additional query parameters

        Returns:
            Dictionary containing SSL proxy settings

        Example:
            >>> # Get SSL proxy settings
            >>> settings = fgt.firewall.ssl_setting.get()
            >>> print(settings)
        """
        api_params: dict[str, Any] = {}
        if vdom:
            api_params["vdom"] = vdom
        api_params.update(kwargs)

        return self._api.get(**api_params)

    def update(
        self,
        proxy_connect_timeout: Optional[int] = None,
        ssl_dh_bits: Optional[str] = None,
        ssl_send_empty_frags: Optional[str] = None,
        no_matching_cipher_action: Optional[str] = None,
        cert_manager_cache_timeout: Optional[int] = None,
        resigned_short_lived_certificate: Optional[str] = None,
        cert_cache_capacity: Optional[int] = None,
        cert_cache_timeout: Optional[int] = None,
        session_cache_capacity: Optional[int] = None,
        session_cache_timeout: Optional[int] = None,
        kxp_queue_threshold: Optional[int] = None,
        ssl_queue_threshold: Optional[int] = None,
        abbreviate_handshake: Optional[str] = None,
        vdom: Optional[str] = None,
        **kwargs: Any,
    ) -> Union[Dict[str, Any], "Coroutine[Any, Any, Dict[str, Any]]"]:
        """
        Update SSL proxy settings.

        Args:
            proxy_connect_timeout: Time limit to make internal connection
                to proxy process (1-60 sec, default=30)
            ssl_dh_bits: Diffie-Hellman (DH) prime bit-size for DHE-RSA
                negotiation (Options: 768, 1024, 1536, 2048, default=2048)
            ssl_send_empty_frags: Enable/disable sending empty fragments
                to avoid CBC IV attacks (SSL 3.0/TLS 1.0 only)
                (Options: enable, disable)
            no_matching_cipher_action: Action when no matching cipher
                found (Options: bypass, drop)
            cert_manager_cache_timeout: Certificate manager cache timeout
                (24-720 hours, default=72)
            resigned_short_lived_certificate: Enable/disable short-lived
                certificates (Options: enable, disable)
            cert_cache_capacity: Host certificate cache max capacity
                (0-500, default=200)
            cert_cache_timeout: Certificate cache timeout (1-120 min,
                default=10)
            session_cache_capacity: SSL session cache capacity
                (1-1000, default=500) (Obsolete)
            session_cache_timeout: SSL session state timeout (1-60 min,
                default=20)
            kxp_queue_threshold: Max CP KXP queue length. Full queue
                switches to main CPU (0-512, default=16)
            ssl_queue_threshold: Max CP SSL queue length. Full queue
                switches to main CPU (0-512, default=32)
            abbreviate_handshake: Enable/disable SSL abbreviated
                handshake (Options: enable, disable)
            vdom: Virtual domain name
            **kwargs: Additional parameters

        Returns:
            Dictionary containing API response

        Example:
            >>> # Update SSL proxy settings
            >>> result = fgt.firewall.ssl_setting.update(
            ...     ssl_dh_bits="2048",
            ...     cert_cache_capacity=300,
            ...     session_cache_timeout=30
            ... )
        """
        # Validate integer ranges
        validate_integer_range(
            proxy_connect_timeout, 1, 60, "proxy_connect_timeout"
        )
        validate_integer_range(
            cert_manager_cache_timeout, 24, 720, "cert_manager_cache_timeout"
        )
        validate_integer_range(
            cert_cache_capacity, 0, 500, "cert_cache_capacity"
        )
        validate_integer_range(
            cert_cache_timeout, 1, 120, "cert_cache_timeout"
        )
        validate_integer_range(
            session_cache_capacity, 0, 1000, "session_cache_capacity"
        )
        validate_integer_range(
            session_cache_timeout, 1, 60, "session_cache_timeout"
        )
        validate_integer_range(
            kxp_queue_threshold, 0, 512, "kxp_queue_threshold"
        )
        validate_integer_range(
            ssl_queue_threshold, 0, 512, "ssl_queue_threshold"
        )

        # Validate enum values
        validate_ssl_dh_bits(ssl_dh_bits)
        validate_enable_disable(ssl_send_empty_frags, "ssl_send_empty_frags")
        validate_ssl_cipher_action(no_matching_cipher_action)
        validate_enable_disable(
            resigned_short_lived_certificate,
            "resigned_short_lived_certificate",
        )
        validate_enable_disable(abbreviate_handshake, "abbreviate_handshake")

        data: dict[str, Any] = {}

        if proxy_connect_timeout is not None:
            data["proxy-connect-timeout"] = proxy_connect_timeout
        if ssl_dh_bits is not None:
            data["ssl-dh-bits"] = ssl_dh_bits
        if ssl_send_empty_frags is not None:
            data["ssl-send-empty-frags"] = ssl_send_empty_frags
        if no_matching_cipher_action is not None:
            data["no-matching-cipher-action"] = no_matching_cipher_action
        if cert_manager_cache_timeout is not None:
            data["cert-manager-cache-timeout"] = cert_manager_cache_timeout
        if resigned_short_lived_certificate is not None:
            data["resigned-short-lived-certificate"] = (
                resigned_short_lived_certificate
            )
        if cert_cache_capacity is not None:
            data["cert-cache-capacity"] = cert_cache_capacity
        if cert_cache_timeout is not None:
            data["cert-cache-timeout"] = cert_cache_timeout
        if session_cache_capacity is not None:
            data["session-cache-capacity"] = session_cache_capacity
        if session_cache_timeout is not None:
            data["session-cache-timeout"] = session_cache_timeout
        if kxp_queue_threshold is not None:
            data["kxp-queue-threshold"] = kxp_queue_threshold
        if ssl_queue_threshold is not None:
            data["ssl-queue-threshold"] = ssl_queue_threshold
        if abbreviate_handshake is not None:
            data["abbreviate-handshake"] = abbreviate_handshake

        api_params: dict[str, Any] = {}
        if vdom:
            api_params["vdom"] = vdom
        api_params.update(kwargs)

        return self._api.put(data, **api_params)
