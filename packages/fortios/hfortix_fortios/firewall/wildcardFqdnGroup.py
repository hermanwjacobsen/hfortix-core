"""
Firewall Wildcard FQDN Group Convenience Wrapper

Provides simplified syntax for wildcard FQDN group operations with full
parameter support.

Wildcard FQDN groups allow grouping multiple wildcard FQDN addresses for
easier management and policy application.

Example:
    Instead of: fgt.api.cmdb.firewall.wildcard_fqdn.group.post(data)
    Use: fgt.firewall.wildcard_fqdn_group.create(
        name='social-media-group',
        member=['*.facebook.com', '*.twitter.com'],
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


def validate_wildcard_fqdn_group_name(
    name: Optional[str], operation: str = "operation"
) -> None:
    """Validate wildcard FQDN group name."""
    if not name:
        raise ValueError(
            f"Wildcard FQDN group name is required for {operation}"
        )
    validate_string_length(name, 79, "Wildcard FQDN group name")


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


class WildcardFqdnGroup:
    """
    Convenience wrapper for wildcard FQDN group operations.

    Manages groups of wildcard FQDN addresses for simplified policy
    management.

    **Use Cases:**
    - Group related wildcard FQDNs (social media, streaming, etc.)
    - Simplify firewall policy configuration
    - Manage multiple domain patterns as a single object

    **Examples:**

    Create wildcard FQDN group:
        >>> fgt.firewall.wildcard_fqdn_group.create(
        ...     name='social-media',
        ...     member=['fb-domains', 'twitter-domains', 'linkedin'],
        ...     color=3,
        ...     comment='All social media services'
        ... )

    Add member to group:
        >>> fgt.firewall.wildcard_fqdn_group.add_member(
        ...     group_name='social-media',
        ...     member='instagram-domains'
        ... )

    Remove member from group:
        >>> fgt.firewall.wildcard_fqdn_group.remove_member(
        ...     group_name='social-media',
        ...     member='linkedin'
        ... )

    Get all groups:
        >>> groups = fgt.firewall.wildcard_fqdn_group.get()

    Delete group:
        >>> fgt.firewall.wildcard_fqdn_group.delete(name='social-media')
    """

    def __init__(self, fortios_instance: "FortiOS"):
        """
        Initialize WildcardFqdnGroup wrapper.

        Args:
            fortios_instance: FortiOS client instance
        """
        self.fgt = fortios_instance
        self.logger = logging.getLogger(__name__)

    # NOTE: The following methods (create, update, delete) are currently
    # non-functional due to FortiOS API limitations. While wildcard FQDN
    # groups can be created via CLI, the REST API returns HTTP 500 error
    # -3 "Entry not found" on POST/PUT/DELETE operations. This appears to
    # be a known limitation in certain FortiOS versions. Use CLI commands
    # for write operations until API support is added.
    #
    # CLI commands:
    #   config firewall wildcard-fqdn group
    #     edit "name"
    #       set member "member1" "member2"
    #       set comment "description"
    #     next
    #   end
    #
    # The get(), exists(), and other read operations work correctly via API.

    def create(
        self,
        name: str,
        member: Optional[Union[str, List[str], List[Dict[str, str]]]] = None,
        color: Optional[int] = None,
        comment: Optional[str] = None,
        visibility: Optional[str] = None,
        vdom: Optional[str] = None,
        **kwargs: Any,
    ) -> Union[Dict[str, Any], "Coroutine[Any, Any, Dict[str, Any]]"]:
        """
        Create a new wildcard FQDN group.

        **WARNING: This method is currently non-functional due to API
        limitations.** See class docstring for details and CLI
        workaround.

        Args:
            name: Group name (max 79 characters)
            member: Wildcard FQDN addresses (string, list of strings, or
                list of dicts). Accepts:
                - Single string: 'addr1'
                - List of strings: ['addr1', 'addr2']
                - List of dicts: [{'name': 'addr1'}, {'name': 'addr2'}]
            color: Color for GUI (0-32)
            comment: Comments (max 255 characters)
            visibility: Enable/disable visibility ('enable' or 'disable')
            vdom: Virtual domain name
            **kwargs: Additional parameters

        Returns:
            API response dictionary

        Raises:
            ValueError: If validation fails
            APIError: If API request fails (expected: HTTP 500 error -3)

        Example:
            >>> result = fgt.firewall.wildcard_fqdn_group.create(
            ...     name='streaming-services',
            ...     member=['netflix', 'hulu', 'disney-plus'],
            ...     color=8,
            ...     comment='Video streaming platforms'
            ... )
        """
        raise NotImplementedError(
            "Wildcard FQDN group creation is not supported via "
            "FortiOS REST API. Use CLI commands instead:\n"
            "  config firewall wildcard-fqdn group\n"
            '    edit "name"\n'
            '      set member "member1" "member2"\n'
            "    next\n"
            "  end"
        )
        # Original implementation commented out due to API limitation:
        # validate_wildcard_fqdn_group_name(name, "create")
        # if color is not None:
        #     validate_color(color)
        # validate_comment(comment)
        # validate_visibility(visibility)
        #
        # payload = build_cmdb_payload_normalized(
        #     name=name,
        #     member=normalize_member_list(member),
        #     color=color,
        #     comment=comment,
        #     visibility=visibility,
        #     **kwargs,
        # )
        #
        # return self.fgt.api.cmdb.firewall.wildcard_fqdn.group.post(
        #     data=payload, vdom=vdom
        # )

    def update(
        self,
        name: str,
        member: Optional[Union[str, List[str], List[Dict[str, str]]]] = None,
        color: Optional[int] = None,
        comment: Optional[str] = None,
        visibility: Optional[str] = None,
        vdom: Optional[str] = None,
        **kwargs: Any,
    ) -> Union[Dict[str, Any], "Coroutine[Any, Any, Dict[str, Any]]"]:
        """
        Update an existing wildcard FQDN group.

        **WARNING: This method is currently non-functional due to API
        limitations.** See class docstring for details and CLI
        workaround.

        Args:
            name: Group name to update
            member: Wildcard FQDN addresses to set (replaces existing)
            color: Color for GUI (0-32)
            comment: Comments (max 255 characters)
            visibility: Enable/disable visibility
            vdom: Virtual domain name
            **kwargs: Additional parameters

        Returns:
            API response dictionary

        Example:
            >>> result = fgt.firewall.wildcard_fqdn_group.update(
            ...     name='streaming-services',
            ...     comment='Updated streaming platforms',
            ...     color=12
            ... )
        """
        raise NotImplementedError(
            "Wildcard FQDN group updates are not supported via "
            "FortiOS REST API. Use CLI commands instead."
        )
        # Original implementation commented out due to API limitation:
        # validate_wildcard_fqdn_group_name(name, "update")
        # if color is not None:
        #     validate_color(color)
        # validate_comment(comment)
        # validate_visibility(visibility)
        #
        # payload = build_cmdb_payload_normalized(
        #     name=name,
        #     member=normalize_member_list(member),
        #     color=color,
        #     comment=comment,
        #     visibility=visibility,
        #     **kwargs,
        # )
        #
        # return self.fgt.api.cmdb.firewall.wildcard_fqdn.group.put(
        #     name=name, data=payload, vdom=vdom
        # )

    def delete(
        self, name: str, vdom: Optional[str] = None
    ) -> Union[Dict[str, Any], "Coroutine[Any, Any, Dict[str, Any]]"]:
        """
        Delete a wildcard FQDN group.

        **WARNING: This method is currently non-functional due to API
        limitations.** See class docstring for details and CLI
        workaround.

        Args:
            name: Group name to delete
            vdom: Virtual domain name

        Returns:
            API response dictionary

        Example:
            >>> result = fgt.firewall.wildcard_fqdn_group.delete(
            ...     name='streaming-services'
            ... )
        """
        raise NotImplementedError(
            "Wildcard FQDN group deletion is not supported via "
            "FortiOS REST API. Use CLI commands instead:\n"
            "  config firewall wildcard-fqdn group\n"
            '    delete "name"\n'
            "  end"
        )
        # Original implementation commented out due to API limitation:
        # validate_wildcard_fqdn_group_name(name, "delete")
        # return self.fgt.api.cmdb.firewall.wildcard_fqdn.group.delete(
        #     name=name, vdom=vdom
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
        Retrieve wildcard FQDN group(s).

        Args:
            name: Specific group name (optional)
            vdom: Virtual domain name
            **kwargs: Additional query parameters

        Returns:
            Single group dict if name specified, otherwise list of all

        Example:
            >>> # Get all groups
            >>> groups = fgt.firewall.wildcard_fqdn_group.get()
            >>> # Get specific group
            >>> group = fgt.firewall.wildcard_fqdn_group.get(
            ...     name='streaming-services'
            ... )
        """
        if name:
            validate_wildcard_fqdn_group_name(name, "get")
            return self.fgt.api.cmdb.firewall.wildcard_fqdn.group.get(
                name=name, vdom=vdom, **kwargs
            )
        return self.fgt.api.cmdb.firewall.wildcard_fqdn.group.get(
            vdom=vdom, **kwargs
        )

    def exists(self, name: str, vdom: Optional[str] = None) -> bool:
        """
        Check if a wildcard FQDN group exists.

        Args:
            name: Group name to check
            vdom: Virtual domain name

        Returns:
            True if group exists, False otherwise

        Example:
            >>> if fgt.firewall.wildcard_fqdn_group.exists(
            ...     'streaming-services'
            ... ):
            ...     print("Group exists")
        """
        validate_wildcard_fqdn_group_name(name, "exists")

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
        Get wildcard FQDN group data by name.

        Returns just the group data, not the full API response.

        Args:
            name: Group name
            vdom: Virtual domain name

        Returns:
            Group dictionary if found, None otherwise

        Example:
            >>> group = fgt.firewall.wildcard_fqdn_group.get_by_name(
            ...     'streaming-services'
            ... )
            >>> if group:
            ...     print(f"Members: {group['member']}")
        """
        validate_wildcard_fqdn_group_name(name, "get_by_name")

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

    def add_member(
        self,
        group_name: str,
        member: Union[str, List[str]],
        vdom: Optional[str] = None,
    ) -> Union[Dict[str, Any], "Coroutine[Any, Any, Dict[str, Any]]"]:
        """
        Add member(s) to a wildcard FQDN group.

        Fetches the current member list, adds the specified member(s),
        then updates the group with the combined list.

        Args:
            group_name: Name of the group
            member: Member(s) to add (string or list of strings)
            vdom: Virtual domain name

        Returns:
            API response dictionary

        Example:
            >>> result = fgt.firewall.wildcard_fqdn_group.add_member(
            ...     group_name='streaming-services',
            ...     member='prime-video'
            ... )
            >>> # Add multiple members
            >>> result = fgt.firewall.wildcard_fqdn_group.add_member(
            ...     group_name='streaming-services',
            ...     member=['apple-tv', 'peacock']
            ... )
        """
        validate_wildcard_fqdn_group_name(group_name, "add_member")

        # Get current group
        current = self.get_by_name(name=group_name, vdom=vdom)
        if not current:
            raise ValueError(f"Group '{group_name}' not found")

        # Get current members
        current_members = current.get("member", [])
        member_names = {
            m["name"] if isinstance(m, dict) else m for m in current_members
        }

        # Add new members
        new_members = [member] if isinstance(member, str) else member
        for m in new_members:
            member_names.add(m)

        # Update group
        return self.update(  # type: ignore
            name=group_name, member=list(member_names), vdom=vdom
        )

    def remove_member(
        self,
        group_name: str,
        member: Union[str, List[str]],
        vdom: Optional[str] = None,
    ) -> Union[Dict[str, Any], "Coroutine[Any, Any, Dict[str, Any]]"]:
        """
        Remove member(s) from a wildcard FQDN group.

        Fetches the current member list, removes the specified member(s),
        then updates the group with the remaining list.

        Args:
            group_name: Name of the group
            member: Member(s) to remove (string or list of strings)
            vdom: Virtual domain name

        Returns:
            API response dictionary

        Example:
            >>> result = fgt.firewall.wildcard_fqdn_group.remove_member(
            ...     group_name='streaming-services',
            ...     member='hulu'
            ... )
            >>> # Remove multiple members
            >>> result = fgt.firewall.wildcard_fqdn_group.remove_member(
            ...     group_name='streaming-services',
            ...     member=['netflix', 'disney-plus']
            ... )
        """
        validate_wildcard_fqdn_group_name(group_name, "remove_member")

        # Get current group
        current = self.get_by_name(name=group_name, vdom=vdom)
        if not current:
            raise ValueError(f"Group '{group_name}' not found")

        # Get current members
        current_members = current.get("member", [])
        member_names = {
            m["name"] if isinstance(m, dict) else m for m in current_members
        }

        # Remove members
        members_to_remove = [member] if isinstance(member, str) else member
        for m in members_to_remove:
            member_names.discard(m)

        # Update group
        return self.update(  # type: ignore
            name=group_name, member=list(member_names), vdom=vdom
        )
