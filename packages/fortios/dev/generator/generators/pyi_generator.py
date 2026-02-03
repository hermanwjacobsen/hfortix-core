"""
Generator for Python type stub (.pyi) files.

Creates inline .pyi files alongside .py files for:
- IDE autocomplete (payload dict fields)
- Type checking (enum Literal types)
- Better error detection
- Self-documenting API
"""

import logging
import sys
from pathlib import Path
from typing import Any

from jinja2 import Environment, FileSystemLoader

sys.path.insert(0, str(Path(__file__).parent.parent))
from schema_management.schema_parser import EndpointSchema
from utils.naming import kebab_to_snake

# Content endpoints registry - endpoints that return binary/text content
# Format: "api_type.module.endpoint" e.g., "monitor.system.config_revision.file"
CONTENT_ENDPOINTS = {
    "monitor.system.config_revision.file",
    # Add more as discovered through testing
}

logger = logging.getLogger(__name__)


class PYIGenerator:
    """Generate .pyi stub files for type hints."""

    def __init__(self, template_dir: Path, output_dir: Path, stubs_dir: Path | None = None):
        """
        Initialize PYI generator.

        Args:
            template_dir: Directory containing .pyi.j2 templates
            output_dir: Root directory for generated .pyi files (deprecated, use stubs_dir)
            stubs_dir: Directory for separate stub package (e.g., packages/fortios-stubs/hfortix_fortios-stubs/)
                      If provided, all .pyi files go here instead of alongside .py files
        """
        self.template_dir = template_dir
        self.output_dir = stubs_dir if stubs_dir else output_dir
        self.env = Environment(
            loader=FileSystemLoader(str(template_dir)),
            trim_blocks=True,
            lstrip_blocks=True,
        )
        
        # Register custom filters
        self._register_filters()

    def _register_filters(self) -> None:
        """Register custom Jinja2 filters."""
        self.env.filters['kebab_to_snake'] = kebab_to_snake  # Use shared utility
        self.env.filters['to_python_type'] = self._to_python_type
        self.env.filters['format_endpoint_link'] = self._format_endpoint_link
        self.env.filters['format_relationship_section'] = self._format_relationship_section
        self.env.filters['sanitize_comment'] = self._sanitize_comment
        self.env.filters['sanitize_default'] = self._sanitize_default
        self.env.filters['to_class_name'] = self._to_class_name

    @staticmethod
    def _sanitize_default(value: Any, max_length: int = 40) -> str:
        """Sanitize a default value for display in a comment.
        
        Replaces newlines, truncates long values.
        """
        if value is None:
            return ""
        text = str(value).replace('\n', ' ').replace('\r', '')
        if len(text) > max_length:
            text = text[:max_length] + "..."
        return text

    @staticmethod
    def _to_class_name(name: str) -> str:
        """Convert snake_case or kebab-case to PascalCase for class names.
        
        Examples:
            file_filter -> FileFilter
            endpoint_control -> EndpointControl
            diameter-filter -> DiameterFilter
        """
        # First convert to snake_case to normalize
        snake = kebab_to_snake(name)
        # Split on underscores and capitalize each part
        parts = snake.split('_')
        return ''.join(p.capitalize() for p in parts if p)

    @staticmethod
    def _sanitize_comment(text: str | None, max_length: int = 80) -> str:
        """
        Sanitize help text for use in Python comments.
        
        - Truncates to max_length characters
        - Ensures truncation doesn't break in middle of parentheses or brackets
        - Removes newlines
        - Escapes any problematic characters
        
        Args:
            text: The help text to sanitize
            max_length: Maximum length of the comment
            
        Returns:
            Sanitized comment text safe for Python
        """
        if not text:
            return ""
        
        # Replace newlines with spaces
        text = text.replace('\n', ' ').replace('\r', '')
        
        # Truncate but ensure we don't break in middle of parentheses
        if len(text) > max_length:
            text = text[:max_length]
            
            # Count open/close parens and brackets
            open_parens = text.count('(') - text.count(')')
            open_brackets = text.count('[') - text.count(']')
            
            # If unbalanced, truncate before the last opening
            if open_parens > 0:
                last_open = text.rfind('(')
                if last_open > 0:
                    text = text[:last_open].rstrip()
            
            if open_brackets > 0:
                last_open = text.rfind('[')
                if last_open > 0:
                    text = text[:last_open].rstrip()
        
        return text.rstrip()

    # Removed: _kebab_to_snake - now using shared utils from utils.naming
    
    @staticmethod
    def _format_endpoint_link(endpoint_path: str) -> str:
        """
        Format endpoint path as Sphinx cross-reference link.
        
        Args:
            endpoint_path: e.g., 'firewall/address' or 'vpn.ipsec/phase1'
            
        Returns:
            RST formatted cross-reference for use in docstrings
            
        Examples:
            'firewall/address' -> ':class:`~.firewall.address.AddressEndpoint`'
            'vpn.ipsec/phase1' -> ':class:`~.vpn.ipsec.phase1.Phase1Endpoint`'
        """
        # Convert path to module structure
        # firewall/address -> firewall.address
        # vpn.ipsec/phase1 -> vpn.ipsec.phase1
        module_path = endpoint_path.replace('/', '.')
        
        # Get class name from last segment
        # firewall/address -> Address
        # vpn.ipsec/phase1 -> Phase1
        last_segment = endpoint_path.split('/')[-1]
        class_name = kebab_to_snake(last_segment).title().replace('_', '') + 'Endpoint'
        
        # Return RST cross-reference
        # ~ means show only the last component in rendered docs
        return f':class:`~.{module_path}.{class_name}`'
    
    @staticmethod
    def _format_relationship_section(
        schema: EndpointSchema,
        reverse_deps: list[dict] | None = None,
        max_deps: int = 10,
        max_reverse: int = 5
    ) -> str:
        """
        Format relationship section for endpoint docstring.
        
        Args:
            schema: Endpoint schema with relationship data
            reverse_deps: Optional reverse dependency map {endpoint: [{"endpoint": ..., "fields": [...]}]}
            max_deps: Maximum forward dependencies to show
            max_reverse: Maximum reverse dependencies to show
            
        Returns:
            Formatted RST section for inclusion in docstring
        """
        lines = []
        
        # Forward dependencies (what this endpoint uses)
        relationships = getattr(schema, 'relationships', {})
        if isinstance(relationships, dict):
            datasources = relationships.get('datasources', {})
            references = relationships.get('references', [])
            
            if references:
                lines.append('**Related Resources:**')
                lines.append('')
                lines.append('    Dependencies (resources this endpoint references):')
                
                # Group by endpoint and show which fields use it
                endpoint_fields = {}
                for field_name, ds_list in datasources.items():
                    if isinstance(ds_list, list):
                        for ds in ds_list:
                            if isinstance(ds, dict):
                                endpoint = ds.get('endpoint', '')
                                if endpoint:
                                    if endpoint not in endpoint_fields:
                                        endpoint_fields[endpoint] = []
                                    endpoint_fields[endpoint].append(field_name)
                
                # Show top N dependencies with field info
                shown = 0
                for endpoint in references[:max_deps]:
                    shown += 1
                    link = PYIGenerator._format_endpoint_link(endpoint)
                    fields = endpoint_fields.get(endpoint, [])
                    if fields:
                        fields_str = ', '.join(sorted(set(fields))[:3])
                        if len(fields) > 3:
                            fields_str += f', +{len(fields) - 3} more'
                        lines.append(f'        - {link} (via: {fields_str})')
                    else:
                        lines.append(f'        - {link}')
                
                if len(references) > max_deps:
                    lines.append(f'        - ... and {len(references) - max_deps} more dependencies')
                
                lines.append('')
        
        # Reverse dependencies (what uses this endpoint)
        if reverse_deps:
            lines.append('    Referenced By (endpoints that use this resource):')
            
            shown = 0
            for dep in reverse_deps[:max_reverse]:
                shown += 1
                endpoint = dep.get('endpoint', '')
                fields = dep.get('fields', [])
                link = PYIGenerator._format_endpoint_link(endpoint)
                
                if fields:
                    fields_str = ', '.join(sorted(fields)[:3])
                    if len(fields) > 3:
                        fields_str += f', +{len(fields) - 3} more'
                    lines.append(f'        - {link} (fields: {fields_str})')
                else:
                    lines.append(f'        - {link}')
            
            if len(reverse_deps) > max_reverse:
                lines.append(f'        - ... and {len(reverse_deps) - max_reverse} more endpoints')
            
            lines.append('')
            lines.append('    ⚠️  **Warning:** Deleting resources may break endpoints that reference them.')
            lines.append('        Use ``datasource=true`` query parameter to check usage before deletion.')
            lines.append('')
        
        return '\n'.join(lines) if lines else ''

    @staticmethod
    def _to_python_type(fortios_type: str) -> str:
        """Convert FortiOS type to Python type."""
        type_map = {
            'integer': 'int',
            'string': 'str',
            'option': 'str',
            'var-string': 'str',
            'ipv4-address': 'str',
            'ipv4-address-multicast': 'str',
            'ipv6-address': 'str',
            'ipv4-classnet': 'str',
            'ipv4-classnet-host': 'str',
            'ipv6-network': 'str',
            'mac-address': 'str',
            'uuid': 'str',
            'datetime': 'str',
            'user': 'str',
            'array': 'list[Any]',  # Generic array type
            'boolean': 'bool',
        }
        return type_map.get(fortios_type, 'str')

    def generate_endpoint_stub(
        self,
        schema: EndpointSchema,
        output_path: Path,
        reverse_deps: list[dict] | None = None,
    ) -> None:
        """
        Generate .pyi stub file for an endpoint class.

        Args:
            schema: Endpoint schema definition
            output_path: Path where .pyi file should be written
            reverse_deps: Optional list of reverse dependencies (what uses this endpoint)
        """
        template = self.env.get_template('endpoint_class.pyi.j2')
        
        # Format relationship section
        rel_section = self._format_relationship_section(schema, reverse_deps)
        
        # Build endpoint path for content endpoint lookup
        # Format: "api_type.module.path" e.g., "monitor.system.config_revision.file"
        api_type = getattr(schema, 'category', 'cmdb')  # category holds cmdb/monitor/service
        endpoint_path = schema.path.replace('/', '.').replace('-', '_')
        content_endpoint_key = f"{api_type}.{endpoint_path}"
        is_content_endpoint = content_endpoint_key in CONTENT_ENDPOINTS
        
        # Prepare template context
        context = {
            'schema': schema,
            'reverse_deps': reverse_deps or [],
            'relationship_section': rel_section,
            'query_params': schema.query_params,  # Add query parameters for service/monitor endpoints
            'is_content_endpoint': is_content_endpoint,  # For ContentResponse return type
        }
        
        # Render template
        content = template.render(context)
        
        # Write to file
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(content, encoding='utf-8')
        
        logger.debug(f"Generated endpoint stub: {output_path}")

    def generate_validator_stub(
        self,
        schema: EndpointSchema,
        enum_constants: dict[str, list[str]],
        output_path: Path,
    ) -> None:
        """
        Generate .pyi stub file for a validator helper module.

        Args:
            schema: Endpoint schema definition
            enum_constants: Enum constant name -> values mapping
            output_path: Path where .pyi file should be written
        """
        template = self.env.get_template('validator.pyi.j2')
        
        # Prepare template context
        context = {
            'schema': schema,
            'enum_constants': enum_constants,
        }
        
        # Render template
        content = template.render(context)
        
        # Write to file
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(content, encoding='utf-8')
        
        logger.debug(f"Generated validator stub: {output_path}")

    def generate_category_init_stub(
        self,
        category_name: str,
        endpoints: list[dict[str, str]],
        output_path: Path,
        subcategories: list[dict[str, Any]] | None = None,
    ) -> None:
        """
        Generate __init__.pyi stub for a category directory.

        Args:
            category_name: Category name (e.g., 'firewall', 'system')
            endpoints: List of dicts with 'module_name' and 'class_name' keys
            output_path: Path where __init__.pyi should be written
            subcategories: Optional list of subcategory dicts with 'attr_name', 'module_name', 'class_name', 'has_mode_classes'
        
        Example:
            endpoints = [
                {'module_name': 'address', 'class_name': 'Address'},
                {'module_name': 'policy', 'class_name': 'Policy'},
            ]
            subcategories = [
                {
                    'attr_name': 'service',
                    'module_name': 'service',
                    'class_name': 'Service',
                    'has_mode_classes': True
                },
            ]
        """
        from datetime import datetime, timezone
        
        template = self.env.get_template('category_init.pyi.j2')
        
        # Sort endpoints by module name for consistency
        sorted_endpoints = sorted(endpoints, key=lambda x: x['module_name'])
        
        # Sort subcategories by attr_name for consistency
        sorted_subcategories = sorted(subcategories or [], key=lambda x: x['attr_name'])
        
        # Prepare template context
        context = {
            'category_name': category_name,
            'endpoints': sorted_endpoints,
            'subcategories': sorted_subcategories,
            'generation_timestamp': datetime.now(timezone.utc).isoformat(),
        }
        
        # Render template
        content = template.render(context)
        
        # Write to file
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(content, encoding='utf-8')
        
        logger.info(f"Generated category stub: {output_path}")

    def generate_toplevel_init_stub(
        self,
        category_name: str,
        subcategories: list[dict[str, Any]],
        output_path: Path,
    ) -> None:
        """
        Generate __init__.pyi stub for a top-level category (CMDB, Monitor, Service).

        Args:
            category_name: Category name (e.g., 'cmdb', 'monitor', 'service')
            subcategories: List of dicts with subcategory info
            output_path: Path where __init__.pyi should be written
        
        Example:
            subcategories = [
                {
                    'attr_name': 'firewall',
                    'module_name': 'firewall',
                    'class_name': 'Firewall',
                    'has_mode_classes': True
                },
            ]
        """
        from datetime import datetime, timezone
        
        template = self.env.get_template('toplevel_init.pyi.j2')
        
        # Sort subcategories by attr_name for consistency
        sorted_subcategories = sorted(subcategories, key=lambda x: x['attr_name'])
        
        # Prepare template context
        context = {
            'category_name': category_name,
            'subcategories': sorted_subcategories,
            'generation_timestamp': datetime.now(timezone.utc).isoformat(),
        }
        
        # Render template
        content = template.render(context)
        
        # Write to file
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(content, encoding='utf-8')
        
        logger.info(f"Generated top-level category stub: {output_path}")

    @staticmethod
    def _class_to_module(class_name: str) -> str:
        """Convert class name to module name (CamelCase -> snake_case)."""
        # Simple implementation: just lowercase for now
        # More sophisticated version would handle CamelCase properly
        result = []
        for i, char in enumerate(class_name):
            if char.isupper() and i > 0:
                result.append('_')
            result.append(char.lower())
        return ''.join(result)

    def create_py_typed_marker(self) -> None:
        """
        Create py.typed marker file for PEP 561 compliance.
        
        This tells type checkers that the package includes inline type information.
        The marker goes in the package root (parent of api/v2).
        """
        # Go up from api/v2 to package root
        package_root = self.output_dir.parent.parent
        marker_path = package_root / 'py.typed'
        marker_path.parent.mkdir(parents=True, exist_ok=True)
        marker_path.write_text('', encoding='utf-8')
        logger.info(f"Created py.typed marker: {marker_path}")
