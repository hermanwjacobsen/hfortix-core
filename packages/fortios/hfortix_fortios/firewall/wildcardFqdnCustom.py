"""
Firewall Wildcard FQDN Custom Address Convenience Wrapper

Provides simplified syntax for wildcard FQDN address operations with
full parameter support.

Wildcard FQDN addresses allow pattern matching for domain names using
wildcards (*) for flexible filtering.

Example:
    Instead of: fgt.api.cmdb.firewall.wildcard_fqdn.custom.post(data)
    Use: fgt.firewall.wildcard_fqdn_custom.create(
        name='social-media',
        wildcard_fqdn='*.facebook.com',
        ...
    )
"""

import logging
from typing import (
    TYPE_CHECKING,
    Any,
    Coroutine,
    Dict,
    List,
    Optional,
    Union,
)

from hfortix_fortios._helpers import validate_string_length

if TYPE_CHECKING:
    from hfortix_fortios.client import FortiOS


def validate_wildcard_fqdn_name(
    name: Optional[str], operation: str = "operation"
) -> None:
    """Validate wildcard FQDN name."""
    if not name:
        raise ValueError(f"Wildcard FQDN name is required for {operation}")
    validate_string_length(name, 79, "Wildcard FQDN name")


def validate_wildcard_fqdn(wildcard_fqdn: Optional[str]) -> None:
    """Validate wildcard FQDN pattern."""
    if wildcard_fqdn is not None:
        validate_string_length(wildcard_fqdn, 255, "wildcard_fqdn")


def validate_comment(comment: Optional[str]) -> None:
    """Validate comment parameter."""
    if comment is not None:
        validate_string_length(comment, 255, "comment")


def validate_visibility(visibility: Optional[str]) -> None:
    """Validate visibility parameter."""
    if visibility is not None and visibility not in ["enable", "disable"]:
        raise ValueError(
            f"Invalid visibility '{visibility}'. "
            f"Must be 'enable' or 'disable'"
        )


class WildcardFqdnCustom:
    """
    Convenience wrapper for wildcard FQDN custom address operations.

    Manages wildcard FQDN addresses for pattern-based domain filtering.
    Supports wildcards (*) for flexible domain matching.

    **Use Cases:**
    - Block all subdomains of a domain (*.facebook.com)
    - Allow specific service patterns (*.cdn.example.com)
    - Create flexible content filtering rules

    **Examples:**

    Create wildcard FQDN address:
        >>> fgt.firewall.wildcard_fqdn_custom.create(
        ...     name='social-media',
        ...     wildcard_fqdn='*.facebook.com',
        ...     color=2,
        ...     comment='Block Facebook services'
        ... )

    Update wildcard FQDN:
        >>> fgt.firewall.wildcard_fqdn_custom.update(
        ...     name='social-media',
        ...     wildcard_fqdn='*.meta.com',
        ...     comment='Updated for Meta rebrand'
        ... )

    Get all wildcard FQDNs:
        >>> addresses = fgt.firewall.wildcard_fqdn_custom.get()

    Delete wildcard FQDN:
        >>> fgt.firewall.wildcard_fqdn_custom.delete(name='social-media')
    """

    def __init__(self, fortios_instance: "FortiOS"):
        """
        Initialize WildcardFqdnCustom wrapper.

        Args:
            fortios_instance: FortiOS client instance
        """
        self.fgt = fortios_instance
        self.logger = logging.getLogger(__name__)

    # NOTE: The following methods (create, update, delete) are currently
    # non-functional due to FortiOS API limitations. While wildcard FQDN
    # custom addresses can be created via CLI, the REST API returns HTTP
    # 500 error -3 "Entry not found" on POST/PUT/DELETE operations. This
    # appears to be a known limitation in certain FortiOS versions. Use
    # CLI commands for write operations until API support is added.
    #
    # CLI commands:
    #   config firewall wildcard-fqdn custom
    #     edit "name"
    #       set wildcard-fqdn "*.example.com"
    #       set comment "description"
    #     next
    #   end
    #
    # The get(), exists(), and other read operations work correctly via API.

    def create(
        self,
        name: str,
        wildcard_fqdn: Optional[str] = None,
        color: Optional[int] = None,
        comment: Optional[str] = None,
        visibility: Optional[str] = None,
        vdom: Optional[str] = None,
        scope: Optional[str] = None,
        **kwargs: Any,
    ) -> Union[Dict[str, Any], "Coroutine[Any, Any, Dict[str, Any]]"]:
        """
        Create a new wildcard FQDN custom address.

        **WARNING: This method is currently non-functional due to API
        limitations.** See class docstring for details and CLI
        workaround.

        Args:
            name: Address name (max 79 characters)
            wildcard_fqdn: Wildcard FQDN pattern (e.g., *.example.com)
            color: Color for GUI (0-32)
            comment: Comments (max 255 characters)
            visibility: Enable/disable visibility ('enable' or 'disable')
            vdom: Virtual domain name
            scope: Scope for global objects ('global' or 'vdom')
            **kwargs: Additional parameters

        Returns:
            API response dictionary

        Raises:
            ValueError: If validation fails
            APIError: If API request fails (expected: HTTP 500 error -3)

        Example:
            >>> result = fgt.firewall.wildcard_fqdn_custom.create(
            ...     name='cdn-services',
            ...     wildcard_fqdn='*.cdn.example.com',
            ...     color=5,
            ...     comment='CDN endpoints',
            ...     scope='global'
            ... )
        """
        raise NotImplementedError(
            "Wildcard FQDN custom address creation is not supported "
            "via FortiOS REST API. Use CLI commands instead:\n"
            "  config firewall wildcard-fqdn custom\n"
            '    edit "name"\n'
            '      set wildcard-fqdn "*.example.com"\n'
            "    next\n"
            "  end"
        )
        # Original implementation commented out due to API limitation:
        # validate_wildcard_fqdn_name(name, "create")
        # validate_wildcard_fqdn(wildcard_fqdn)
        # if color is not None:
        #     validate_color(color)
        # validate_comment(comment)
        # validate_visibility(visibility)
        #
        # payload = build_cmdb_payload_normalized(
        #     name=name,
        #     wildcard_fqdn=wildcard_fqdn,
        #     color=color,
        #     comment=comment,
        #     visibility=visibility,
        #     **kwargs,
        # )
        #
        # return self.fgt.api.cmdb.firewall.wildcard_fqdn.custom.post(
        #     data=payload, vdom=vdom, scope=scope
        # )

    def update(
        self,
        name: str,
        wildcard_fqdn: Optional[str] = None,
        color: Optional[int] = None,
        comment: Optional[str] = None,
        visibility: Optional[str] = None,
        vdom: Optional[str] = None,
        scope: Optional[str] = None,
        **kwargs: Any,
    ) -> Union[Dict[str, Any], "Coroutine[Any, Any, Dict[str, Any]]"]:
        """
        Update an existing wildcard FQDN custom address.

        **WARNING: This method is currently non-functional due to API
        limitations.** See class docstring for details and CLI
        workaround.

        Args:
            name: Address name to update
            wildcard_fqdn: Wildcard FQDN pattern
            color: Color for GUI (0-32)
            comment: Comments (max 255 characters)
            visibility: Enable/disable visibility
            vdom: Virtual domain name
            scope: Scope for global objects ('global' or 'vdom')
            **kwargs: Additional parameters

        Returns:
            API response dictionary

        Example:
            >>> result = fgt.firewall.wildcard_fqdn_custom.update(
            ...     name='cdn-services',
            ...     comment='Updated CDN endpoints',
            ...     color=10,
            ...     scope='global'
            ... )
        """
        raise NotImplementedError(
            "Wildcard FQDN custom address updates are not supported "
            "via FortiOS REST API. Use CLI commands instead."
        )
        # Original implementation commented out due to API limitation:
        # validate_wildcard_fqdn_name(name, "update")
        # validate_wildcard_fqdn(wildcard_fqdn)
        # if color is not None:
        #     validate_color(color)
        # validate_comment(comment)
        # validate_visibility(visibility)
        #
        # payload = build_cmdb_payload_normalized(
        #     name=name,
        #     wildcard_fqdn=wildcard_fqdn,
        #     color=color,
        #     comment=comment,
        #     visibility=visibility,
        #     **kwargs,
        # )
        #
        # return self.fgt.api.cmdb.firewall.wildcard_fqdn.custom.put(
        #     name=name, data=payload, vdom=vdom, scope=scope
        # )

    def delete(
        self,
        name: str,
        vdom: Optional[str] = None,
        scope: Optional[str] = None,
    ) -> Union[Dict[str, Any], "Coroutine[Any, Any, Dict[str, Any]]"]:
        """
        Delete a wildcard FQDN custom address.

        **WARNING: This method is currently non-functional due to API
        limitations.** See class docstring for details and CLI
        workaround.

        Args:
            name: Address name to delete
            vdom: Virtual domain name
            scope: Scope for global objects ('global' or 'vdom')

        Returns:
            API response dictionary

        Example:
            >>> result = fgt.firewall.wildcard_fqdn_custom.delete(
            ...     name='cdn-services',
            ...     scope='global'
            ... )
        """
        raise NotImplementedError(
            "Wildcard FQDN custom address deletion is not supported "
            "via FortiOS REST API. Use CLI commands instead:\n"
            "  config firewall wildcard-fqdn custom\n"
            '    delete "name"\n'
            "  end"
        )
        # Original implementation commented out due to API limitation:
        # validate_wildcard_fqdn_name(name, "delete")
        # return self.fgt.api.cmdb.firewall.wildcard_fqdn.custom.delete(
        #     name=name, vdom=vdom, scope=scope
        # )

    def get(
        self,
        name: Optional[str] = None,
        vdom: Optional[str] = None,
        **kwargs: Any,
    ) -> Union[
        Dict[str, Any],
        List[Dict[str, Any]],
        "Coroutine[Any, Any, Union[Dict[str, Any], List[Dict[str, Any]]]]",
    ]:
        """
        Retrieve wildcard FQDN custom address(es).

        Args:
            name: Specific address name (optional)
            vdom: Virtual domain name
            **kwargs: Additional query parameters

        Returns:
            Single address dict if name specified, otherwise list of all

        Example:
            >>> # Get all addresses
            >>> addresses = fgt.firewall.wildcard_fqdn_custom.get()
            >>> # Get specific address
            >>> addr = fgt.firewall.wildcard_fqdn_custom.get(
            ...     name='cdn-services'
            ... )
        """
        if name:
            validate_wildcard_fqdn_name(name, "get")
            return self.fgt.api.cmdb.firewall.wildcard_fqdn.custom.get(
                name=name, vdom=vdom, **kwargs
            )
        return self.fgt.api.cmdb.firewall.wildcard_fqdn.custom.get(
            vdom=vdom, **kwargs
        )

    def exists(self, name: str, vdom: Optional[str] = None) -> bool:
        """
        Check if a wildcard FQDN custom address exists.

        Args:
            name: Address name to check
            vdom: Virtual domain name

        Returns:
            True if address exists, False otherwise

        Example:
            >>> if fgt.firewall.wildcard_fqdn_custom.exists('cdn-services'):
            ...     print("Address exists")
        """
        validate_wildcard_fqdn_name(name, "exists")

        try:
            result = self.get(name=name, vdom=vdom)
            # Handle both list and dict responses
            if isinstance(result, list):
                return len(result) > 0
            elif isinstance(result, dict):
                results = result.get("results", [])
                return len(results) > 0
            return False
        except Exception:
            return False

    def get_by_name(
        self, name: str, vdom: Optional[str] = None
    ) -> Optional[Dict[str, Any]]:
        """
        Get wildcard FQDN custom address data by name.

        Returns just the address data, not the full API response.

        Args:
            name: Address name
            vdom: Virtual domain name

        Returns:
            Address dictionary if found, None otherwise

        Example:
            >>> addr = fgt.firewall.wildcard_fqdn_custom.get_by_name(
            ...     'cdn-services'
            ... )
            >>> if addr:
            ...     print(f"Pattern: {addr['wildcard-fqdn']}")
        """
        validate_wildcard_fqdn_name(name, "get_by_name")

        try:
            result = self.get(name=name, vdom=vdom)

            if isinstance(result, dict):
                if "results" in result:
                    results = result["results"]
                    return results[0] if results else None
                else:
                    return result
            elif isinstance(result, list):
                return result[0] if result else None
            return None
        except Exception:
            return None
