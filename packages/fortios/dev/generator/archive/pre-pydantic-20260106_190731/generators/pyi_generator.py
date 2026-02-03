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

    # Removed: _kebab_to_snake - now using shared utils from utils.naming

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
        }
        return type_map.get(fortios_type, 'str')

    def generate_endpoint_stub(
        self,
        schema: EndpointSchema,
        output_path: Path,
    ) -> None:
        """
        Generate .pyi stub file for an endpoint class.

        Args:
            schema: Endpoint schema definition
            output_path: Path where .pyi file should be written
        """
        template = self.env.get_template('endpoint_class.pyi.j2')
        
        # Prepare template context
        context = {
            'schema': schema,
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
    ) -> None:
        """
        Generate __init__.pyi stub for a category directory.

        Args:
            category_name: Category name (e.g., 'firewall', 'system')
            endpoints: List of dicts with 'module_name' and 'class_name' keys
            output_path: Path where __init__.pyi should be written
        
        Example:
            endpoints = [
                {'module_name': 'address', 'class_name': 'Address'},
                {'module_name': 'policy', 'class_name': 'Policy'},
            ]
        """
        from datetime import datetime, timezone
        
        template = self.env.get_template('category_init.pyi.j2')
        
        # Sort endpoints by module name for consistency
        sorted_endpoints = sorted(endpoints, key=lambda x: x['module_name'])
        
        # Prepare template context
        context = {
            'category_name': category_name,
            'endpoints': sorted_endpoints,
            'generation_timestamp': datetime.now(timezone.utc).isoformat(),
        }
        
        # Render template
        content = template.render(context)
        
        # Write to file
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(content, encoding='utf-8')
        
        logger.info(f"Generated category stub: {output_path}")

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
