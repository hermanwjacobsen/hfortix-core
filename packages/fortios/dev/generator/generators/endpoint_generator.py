"""
Endpoint Generator

Generates API endpoint class files (.py) from FortiOS schemas.
Uses the same naming and structure as existing codebase.
"""

from pathlib import Path
from typing import Any

from jinja2 import Environment, FileSystemLoader

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
from schema_management.schema_parser import EndpointSchema
from utils.naming import snake_to_kebab, kebab_to_snake, fix_api_path
from .docstring_enhancer import DocstringEnhancer


class EndpointGenerator:
    """Generates API endpoint class files."""
    
    def __init__(self, template_dir: Path):
        """
        Initialize endpoint generator.
        
        Args:
            template_dir: Directory containing Jinja2 templates
        """
        self.env = Environment(
            loader=FileSystemLoader(str(template_dir)),
            trim_blocks=True,
            lstrip_blocks=True,
        )
        
        # Initialize docstring enhancer
        self.docstring_enhancer = DocstringEnhancer()
        
        # Add custom filters - use shared utility functions
        self.env.filters["snake_to_kebab"] = snake_to_kebab
        self.env.filters["kebab_to_snake"] = kebab_to_snake
        self.env.filters["to_python_type"] = self._to_python_type
        self.env.filters["api_path_fix"] = fix_api_path
        self.env.filters["get_literal_type"] = self._get_literal_type
        self.env.filters["get_python_type_with_literal"] = self._get_python_type_with_literal
        
    # Removed: _snake_to_kebab, _kebab_to_snake, _api_path_fix - now using shared utils from utils.naming
    
    @staticmethod
    def _to_python_type(fortios_type: str) -> str:
        """Convert FortiOS type to Python type hint."""
        type_map = {
            "string": "str",
            "integer": "int",
            "option": "str",  # Will be refined with Literal in .pyi
            "var-string": "str",
            "ipv4-address": "str",
            "ipv4-address-any": "str",
            "ipv4-classnet": "str",
            "ipv4-netmask": "str",
            "ipv6-address": "str",
            "ipv6-network": "str",
            "ipv6-prefix": "str",
            "mac-address": "str",
            "uuid": "str",
            "user": "str",
            "array": "list[str]",  # Array type defaults to list of strings
        }
        return type_map.get(fortios_type, "Any")
    
    def _get_literal_type(self, field_info: dict) -> str | None:
        """
        Extract Literal type from field metadata.
        
        Args:
            field_info: Field information dict with pydantic_type or allowed_values
            
        Returns:
            Literal type string or None
        """
        return self.docstring_enhancer.get_literal_type(field_info)
    
    def _get_python_type_with_literal(self, field_info: Any) -> str:
        """
        Get Python type annotation with Literal support.
        
        Args:
            field_info: Field information (FieldMetadata object or dict)
            
        Returns:
            Type annotation string (e.g., 'Literal["accept", "deny"]' or 'str')
        """
        # Convert FieldMetadata to dict if needed
        if hasattr(field_info, '__dict__'):
            field_dict = field_info.__dict__
        elif isinstance(field_info, dict):
            field_dict = field_info
        else:
            # Fallback to Any for unknown types
            return "Any"
        
        # Check for Literal type first (via options attribute or dict key)
        options = None
        if isinstance(field_info, dict):
            options = field_info.get('options')
        elif hasattr(field_info, 'options'):
            options = getattr(field_info, 'options', None)
        
        if options:
            # Extract option names
            option_names = []
            for opt in options:
                if isinstance(opt, dict):
                    option_names.append(opt.get('name', ''))
                else:
                    option_names.append(str(opt))
            
            # Filter out empty strings
            option_names = [n for n in option_names if n]
            
            if option_names:
                # Create Literal type
                quoted_options = [f'"{opt}"' for opt in option_names]
                return f"Literal[{', '.join(quoted_options)}]"
        
        # Fall back to standard type mapping
        if isinstance(field_info, dict):
            field_type = field_dict.get("type", "string")
        elif hasattr(field_info, 'type'):
            field_type = getattr(field_info, 'type', 'string')
        else:
            field_type = field_dict.get("type", "string")
        
        return self._to_python_type(field_type)
    
    def _collect_literal_types(self, schema: EndpointSchema) -> bool:
        """
        Check if any fields in schema have Literal types.
        
        Args:
            schema: Endpoint schema
            
        Returns:
            True if Literal import is needed
        """
        for field in schema.fields.values():
            # Convert field to dict for checking
            if hasattr(field, '__dict__'):
                field_dict = field.__dict__
            elif isinstance(field, dict):
                field_dict = field
            else:
                continue
                
            if self._get_literal_type(field_dict):
                return True
        return False
    
    def _extract_http_methods(self, schema: EndpointSchema) -> list[str]:
        """
        Extract HTTP methods from schema metadata.
        
        Args:
            schema: Parsed endpoint schema
            
        Returns:
            List of HTTP methods (e.g., ['GET'], ['POST'], ['GET', 'POST', 'PUT', 'DELETE'])
        
        Note:
            - Read-only endpoints: Only GET is supported
            - CMDB endpoints: Determined by mkey presence
              * With mkey (table) → Full CRUD: GET POST PUT DELETE
              * Without mkey (singleton) → GET PUT only
            - Monitor/Service/Log: Use schema.http_method field (GET or POST)
        """
        # Check if endpoint is read-only (e.g., internet-service reference tables)
        if schema.readonly:
            return ['GET']
        
        # Determine methods based on category
        if schema.category == 'cmdb':
            # Check if endpoint has a primary key (mkey)
            # Tables with mkey support full CRUD operations
            # Singletons without mkey only support GET/PUT (no POST/DELETE)
            if schema.mkey:
                # Table endpoint - full CRUD
                return ['GET', 'POST', 'PUT', 'DELETE']
            else:
                # Singleton endpoint - GET and PUT only (no create/delete)
                return ['GET', 'PUT']
        elif schema.category in ['monitor', 'service', 'log']:
            # Use the http_method from schema (can be GET or POST)
            # Monitor endpoints can be:
            # - GET: Data retrieval (e.g., /monitor/firewall/policy)
            # - POST: Actions (e.g., /monitor/firewall/policy/clear-counters)
            http_method = getattr(schema, 'http_method', 'GET')
            return [http_method] if http_method else ['GET']
        else:
            return ['GET']
    
    def generate(
        self,
        schema: EndpointSchema,
        output_dir: Path,
        generator_version: str = "0.5.0",
        will_have_subdir: bool = False,
        schema_data: dict[str, Any] | None = None,
    ) -> Path:
        """
        Generate API endpoint class file.
        
        Args:
            schema: Parsed schema
            output_dir: Base output directory (e.g., packages/fortios/hfortix_fortios/api/v2)
            generator_version: Version of generator
            will_have_subdir: If True, this endpoint will have action subdirectories, use _base naming
            schema_data: Raw schema dict (for table field extraction)
            
        Returns:
            Path to generated file
        """
        # Import the schema parser here to avoid circular imports
        from schema_management.schema_parser import SchemaParser
        
        # Extract HTTP methods from schema metadata
        http_methods = self._extract_http_methods(schema)
        
        # Collect Literal types needed for imports
        literal_types_needed = self._collect_literal_types(schema)
        
        # Extract table fields metadata if schema_data provided
        table_fields_metadata = {}
        multivalue_option_fields = {}
        disable_auto_normalize = False
        if schema_data:
            table_fields_metadata = SchemaParser.extract_table_fields_metadata(schema_data)
            multivalue_option_fields = SchemaParser.extract_multivalue_option_fields(schema_data)
            # Check if this endpoint has unitary fields that conflict with auto-normalization
            # (e.g., DoS-policy has 'interface' as a string, not a list)
            disable_auto_normalize = SchemaParser.has_unitary_list_field_conflict(schema_data)
        
        # Load template
        template = self.env.get_template("endpoint_class.py.j2")
        
        # Prepare template context
        context = {
            "schema": schema,
            "http_methods": http_methods,
            "generator_version": generator_version,
            "generation_timestamp": self._get_timestamp(),
            "literal_types_needed": literal_types_needed,
            "docstring_enhancer": self.docstring_enhancer,
            "table_fields_metadata": table_fields_metadata,  # ← NEW
            "multivalue_option_fields": multivalue_option_fields,  # ← NEW: space-separated multi-value fields
            "query_params": schema.query_params,  # ← ADD query parameters from schema
            "disable_auto_normalize": disable_auto_normalize,  # ← NEW: disable auto-normalization for unitary conflicts
        }
        
        # Render template
        rendered = template.render(**context)
        
        # Determine output path
        # Structure: output_dir/cmdb/firewall/ssh_setting.py
        # Convert category name to Python-safe identifier (replace hyphens with underscores)
        safe_category = schema.category.replace("-", "_")
        category_dir = output_dir / safe_category
        
        # Create subdirectories for nested paths
        # Note: schema.path is already normalized (dots converted to slashes) by schema_parser
        if "/" in schema.path:
            parts = schema.path.split("/")
            # Convert hyphens to underscores for Python package names
            safe_parts = [p.replace("-", "_") for p in parts[:-1]]
            endpoint_dir = category_dir / "/".join(safe_parts)
            endpoint_filename = parts[-1].replace("-", "_")
        else:
            endpoint_dir = category_dir
            endpoint_filename = schema.path.replace("-", "_")
        
        endpoint_dir.mkdir(parents=True, exist_ok=True)
        
        # Use schema.file_name for the actual filename (handles underscores)
        base_filename = schema.file_name
        output_file = endpoint_dir / f"{base_filename}.py"
        
        # Handle naming conflicts: if we know this endpoint will have action subdirectories,
        # ALWAYS use _base suffix for consistency and to avoid Python import shadowing
        # 
        # Pattern:
        #   Simple endpoint:  address.py → Class directly accessible
        #   Parent endpoint:  application_list_base.py + application_list/__init__.py → Inherited class
        # 
        # This approach:
        #   ✅ No name collisions (package dirs can't shadow _base.py files)
        #   ✅ Simple & predictable (same pattern every time)
        #   ✅ Clean separation (base class vs wrapper with sub-endpoints)
        #   ✅ Standard Python pattern (inheritance is well understood)
        conflict_dir = endpoint_dir / base_filename
        if will_have_subdir or (conflict_dir.exists() and conflict_dir.is_dir()):
            print(f"    📁 Endpoint will have sub-endpoints: using {base_filename}_base.py")
            output_file = endpoint_dir / f"{base_filename}_base.py"
        
        # Write file
        with open(output_file, "w") as f:
            f.write(rendered)
        
        return output_file
    
    @staticmethod
    def _get_timestamp() -> str:
        """Get current UTC timestamp."""
        from datetime import datetime, timezone
        return datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
