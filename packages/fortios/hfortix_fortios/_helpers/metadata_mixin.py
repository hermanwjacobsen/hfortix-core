"""
Metadata Mixin for FortiOS API Endpoints

Provides common metadata helper methods for all endpoint classes.
Each endpoint class inherits these methods and imports from their own
_helpers.<endpoint_name> module for endpoint-specific data.
"""

from __future__ import annotations

from typing import Any, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from types import ModuleType


class MetadataMixin:
    """
    Mixin providing metadata helper methods for FortiOS API endpoint classes.
    
    This mixin provides a standardized interface for accessing schema metadata,
    field information, validation, and other introspection capabilities.
    
    Each endpoint class that inherits this mixin must define a class attribute:
        _helper_module_name: str  # Name of the helper module (e.g., "settings")
    
    The corresponding helper module at `_helpers.<endpoint_name>` must provide:
    - get_schema_info()
    - get_field_metadata(field_name)
    - get_all_fields()
    - validate_field_value(field_name, value)
    - REQUIRED_FIELDS
    - FIELDS_WITH_DEFAULTS
    - DEPRECATED_FIELDS (optional)
    """

    # Subclasses must define this
    _helper_module_name: str = ""

    @classmethod
    def _get_helper_module(cls) -> ModuleType:
        """Get the helper module for this endpoint class."""
        from importlib import import_module
        
        if not cls._helper_module_name:
            raise NotImplementedError(
                f"{cls.__name__} must define _helper_module_name class attribute"
            )
        
        # Determine the package based on the class's module
        package = cls.__module__.rsplit('.', 1)[0]
        return import_module(f"._helpers.{cls._helper_module_name}", package=package)

    @classmethod
    def help(cls, field_name: str | None = None) -> str:
        """
        Get help text for endpoint or specific field.

        Args:
            field_name: Optional field name to get help for. If None, shows endpoint help.

        Returns:
            Formatted help text

        Examples:
            >>> # Get endpoint information
            >>> print(Settings.help())
            
            >>> # Get field information
            >>> print(Settings.help("machine-learning-detection"))
        """
        helper_module = cls._get_helper_module()
        get_schema_info = getattr(helper_module, 'get_schema_info')
        get_field_metadata = getattr(helper_module, 'get_field_metadata')

        if field_name is None:
            # Endpoint help
            info = get_schema_info()
            lines = [
                f"Endpoint: {info['endpoint']}",
                f"Category: {info['category']}",
                f"Help: {info.get('help', 'N/A')}",
                "",
                f"Total Fields: {info['total_fields']}",
                f"Required Fields: {info['required_fields_count']}",
                f"Fields with Defaults: {info['fields_with_defaults_count']}",
            ]
            if 'mkey' in info:
                lines.append(f"\nPrimary Key: {info['mkey']} ({info['mkey_type']})")
            return "\n".join(lines)
        
        # Field help
        meta = get_field_metadata(field_name)
        if meta is None:
            return f"Unknown field: {field_name}"

        lines = [
            f"Field: {meta['name']}",
            f"Type: {meta['type']}",
        ]
        if 'description' in meta:
            lines.append(f"Description: {meta['description']}")
        lines.append(f"Required: {'Yes' if meta.get('required', False) else 'No'}")
        if 'default' in meta:
            lines.append(f"Default: {meta['default']}")
        if 'options' in meta:
            lines.append(f"Options: {', '.join(meta['options'])}")
        if 'constraints' in meta:
            constraints = meta['constraints']
            if 'min' in constraints or 'max' in constraints:
                min_val = constraints.get('min', '?')
                max_val = constraints.get('max', '?')
                lines.append(f"Range: {min_val} - {max_val}")
            if 'max_length' in constraints:
                lines.append(f"Max Length: {constraints['max_length']}")

        return "\n".join(lines)

    @classmethod
    def fields(cls, detailed: bool = False) -> Union[list[str], dict[str, dict]]:
        """
        Get list of all field names or detailed field information.

        Args:
            detailed: If True, return dict with field metadata

        Returns:
            List of field names or dict of field metadata

        Examples:
            >>> # Simple list
            >>> fields = Settings.fields()
            >>> print(f"Available fields: {len(fields)}")
            
            >>> # Detailed info
            >>> fields = Settings.fields(detailed=True)
            >>> for name, meta in fields.items():
            ...     print(f"{name}: {meta['type']}")
        """
        helper_module = cls._get_helper_module()
        get_all_fields = getattr(helper_module, 'get_all_fields')
        get_field_metadata = getattr(helper_module, 'get_field_metadata')

        field_names = get_all_fields()

        if not detailed:
            return field_names

        # Build detailed dict
        detailed_fields = {}
        for fname in field_names:
            meta = get_field_metadata(fname)
            if meta:
                detailed_fields[fname] = meta

        return detailed_fields

    @classmethod
    def field_info(cls, field_name: str) -> dict[str, Any] | None:
        """
        Get complete metadata for a specific field.

        Args:
            field_name: Name of the field

        Returns:
            Field metadata dict or None if field doesn't exist

        Examples:
            >>> info = Settings.field_info("machine-learning-detection")
            >>> print(f"Type: {info['type']}")
            >>> if 'options' in info:
            ...     print(f"Options: {info['options']}")
        """
        helper_module = cls._get_helper_module()
        get_field_metadata = getattr(helper_module, 'get_field_metadata')

        return get_field_metadata(field_name)

    @classmethod
    def validate_field(cls, field_name: str, value: Any) -> tuple[bool, str | None]:
        """
        Validate a field value against its constraints.

        Args:
            field_name: Name of the field
            value: Value to validate

        Returns:
            Tuple of (is_valid, error_message)

        Examples:
            >>> is_valid, error = Settings.validate_field("machine-learning-detection", "test")
            >>> if not is_valid:
            ...     print(f"Validation error: {error}")
        """
        helper_module = cls._get_helper_module()
        validate_field_value = getattr(helper_module, 'validate_field_value')

        return validate_field_value(field_name, value)

    @classmethod
    def required_fields(cls) -> list[str]:
        """
        Get list of required field names.

        Note: Due to FortiOS schema quirks, some fields may be conditionally required.
        Always test with the actual API for authoritative requirements.

        Returns:
            List of required field names

        Examples:
            >>> required = Settings.required_fields()
            >>> print(f"Required fields: {', '.join(required)}")
        """
        helper_module = cls._get_helper_module()
        REQUIRED_FIELDS = getattr(helper_module, 'REQUIRED_FIELDS')

        return REQUIRED_FIELDS.copy()

    @classmethod
    def defaults(cls) -> dict[str, Any]:
        """
        Get all fields with default values.

        Returns:
            Dict mapping field names to default values

        Examples:
            >>> defaults = Settings.defaults()
            >>> print(f"Fields with defaults: {len(defaults)}")
            >>> # Use as starting point for payload
            >>> payload = defaults.copy()
            >>> payload['name'] = 'my-custom-name'
        """
        helper_module = cls._get_helper_module()
        FIELDS_WITH_DEFAULTS = getattr(helper_module, 'FIELDS_WITH_DEFAULTS')

        return FIELDS_WITH_DEFAULTS.copy()

    @classmethod
    def schema(cls) -> dict[str, Any]:
        """
        Get complete schema information for this endpoint.

        Returns:
            Schema metadata dict containing endpoint info, field counts, and primary key

        Examples:
            >>> schema = Settings.schema()
            >>> print(f"Endpoint: {schema['endpoint']}")
            >>> print(f"Total fields: {schema['total_fields']}")
            >>> print(f"Primary key: {schema.get('mkey', 'N/A')}")
        """
        helper_module = cls._get_helper_module()
        get_schema_info = getattr(helper_module, 'get_schema_info')

        return get_schema_info()
