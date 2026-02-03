"""
Pydantic Model Generator

Generates Pydantic BaseModel classes from FortiOS schemas for runtime validation.
Includes field constraints, nested models for child tables, and enum generation.
"""

from pathlib import Path
from typing import Any

from jinja2 import Environment, FileSystemLoader

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
from schema_management.schema_parser import EndpointSchema


class ModelGenerator:
    """Generates Pydantic model classes from schemas."""
    
    def __init__(self, template_dir: Path):
        """
        Initialize model generator.
        
        Args:
            template_dir: Directory containing Jinja2 templates
        """
        self.env = Environment(
            loader=FileSystemLoader(str(template_dir)),
            trim_blocks=True,
            lstrip_blocks=True,
        )
        
        # Add custom filters
        self.env.filters["get_pydantic_field"] = self._get_pydantic_field
        self.env.filters["should_use_enum"] = self._should_use_enum
        self.env.filters["to_enum_name"] = self._to_enum_name
        self.env.filters["get_imports_needed"] = self._get_imports_needed
        self.env.filters["generate_exists_checks"] = self._generate_exists_checks
    
    def _should_use_enum(self, allowed_values: list | None) -> bool:
        """
        Determine if we should use Enum vs Literal.
        
        Args:
            allowed_values: List of allowed values
            
        Returns:
            True if should use Enum (4+ values), False for Literal (2-3 values)
        """
        if not allowed_values:
            return False
        return len(allowed_values) >= 4
    
    def _to_enum_name(self, field_name: str, value: str) -> str:
        """
        Convert field value to Enum member name.
        
        Args:
            field_name: Field name
            value: Value string
            
        Returns:
            Enum member name (e.g., "ACCEPT", "DENY")
        """
        # Convert to uppercase, replace special chars with underscores
        enum_name = value.upper().replace("-", "_").replace(" ", "_").replace(".", "_")
        # Remove any remaining non-alphanumeric chars
        enum_name = "".join(c if c.isalnum() or c == "_" else "" for c in enum_name)
        return enum_name
    
    def _generate_exists_checks(self, endpoint_checks: list[dict], indent: str = "            ") -> str:
        """
        Generate properly indented if/elif exists() checks.
        
        Args:
            endpoint_checks: List of endpoint check dicts with 'endpoint_path' key
            indent: Indentation for continuation lines (elif statements)
            
        Returns:
            Multi-line string with properly indented if/elif statements
        """
        lines = []
        for i, check in enumerate(endpoint_checks):
            keyword = "if" if i == 0 else "elif"
            # First line has no indent (comes from template), subsequent lines need indent
            line_indent = "" if i == 0 else indent
            lines.append(f"{line_indent}{keyword} await client.api.cmdb.{check['endpoint_path']}.exists(value):")
            lines.append(f"{indent}    found = True")
        return "\n".join(lines)
    
    @staticmethod
    def _to_python_type(fortios_type: str) -> str:
        """Convert FortiOS type to Python type hint."""
        type_map = {
            "string": "str",
            "integer": "int",
            "option": "str",  # Will be refined with Literal or Enum
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
        }
        return type_map.get(fortios_type, "Any")
    
    def _get_pydantic_field(self, field_info: dict) -> str:
        """
        Generate Pydantic Field() definition with constraints.
        
        Args:
            field_info: Field metadata dict
            
        Returns:
            Field definition string
        """
        constraints = []
        
        # Parse validation constraints - skip None values
        validation = field_info.get("validation", {})
        
        if validation.get("min") is not None:
            constraints.append(f"ge={validation['min']}")
        if validation.get("max") is not None:
            constraints.append(f"le={validation['max']}")
        if validation.get("max_length") is not None:
            constraints.append(f"max_length={validation['max_length']}")
        if validation.get("pattern") is not None:
            pattern = validation['pattern'].replace('\\', '\\\\').replace('"', '\\"')
            constraints.append(f'pattern=r"{pattern}"')
        
        # Add default value
        default_value = field_info.get("default_value")
        if default_value is not None:
            if isinstance(default_value, str):
                # Escape quotes in default string value
                escaped_value = default_value.replace('\\', '\\\\').replace('"', '\\"')
                constraints.append(f'default="{escaped_value}"')
            elif isinstance(default_value, bool):
                constraints.append(f'default={str(default_value)}')
            else:
                constraints.append(f"default={default_value}")
        elif not field_info.get("required", False):
            constraints.append("default=None")
        
        # Add description - escape quotes and remove newlines
        help_text = field_info.get("help", "")
        if help_text:
            # Escape quotes and newlines in description
            help_text = help_text.replace('\\', '\\\\').replace('"', '\\"').replace('\n', ' ').replace('\r', '')
            constraints.append(f'description="{help_text}"')
        
        # Add datasource info as a comment (not in Field())
        datasource = field_info.get("datasource")
        datasource_comment = ""
        if datasource:
            datasource_comment = f"  # datasource: {datasource}"
        
        if constraints:
            return f"Field({', '.join(constraints)}){datasource_comment}"
        return f"Field(){datasource_comment}"
    
    def _get_imports_needed(self, schema: EndpointSchema) -> dict[str, bool]:
        """
        Determine which imports are needed for the model.
        
        Args:
            schema: Endpoint schema
            
        Returns:
            Dict of import flags (literal, enum, uuid, etc.)
        """
        needs = {
            "literal": False,
            "enum": False,
            "uuid": False,
            "list": False,
            "optional": False,
        }
        
        # Check all fields
        for field in schema.fields.values():
            # Check field type (FieldMetadata has 'type' attribute)
            field_type = getattr(field, 'type', '')
            
            # Check if it's a UUID type
            if 'uuid' in field_type.lower():
                needs["uuid"] = True
            
            # Check if it's a table (list type)
            if getattr(field, 'is_list', False) or getattr(field, 'children', None):
                needs["list"] = True
            
            # Check for enum (4+ allowed values means we use Enum instead of Literal)
            options = getattr(field, 'options', None)
            if options and self._should_use_enum(options):
                needs["enum"] = True
            elif options:
                # Less than 4 values, use Literal
                needs["literal"] = True
            
            # Check for optional (non-required fields)
            if not getattr(field, 'required', False):
                needs["optional"] = True
        
        return needs
    
    def _prepare_field_info(self, field_name: str, field: Any) -> dict:
        """
        Convert FieldMetadata to template-friendly dict.
        
        Args:
            field_name: Name of the field
            field: FieldMetadata object
            
        Returns:
            Dict with processed field information
        """
        # Generate Python-safe field name
        import keyword
        python_name = field_name.replace("-", "_")
        if keyword.iskeyword(python_name):
            python_name = python_name + "_"
        
        # Determine Pydantic type
        field_type = getattr(field, 'type', 'string')
        pydantic_type = self._to_python_type(field_type)
        
        # Get field options - handle both list[str] and list[dict]
        raw_options = getattr(field, 'options', None)
        options = None
        if raw_options:
            # Convert list of dicts to list of strings (extract 'name' key)
            if isinstance(raw_options, list) and len(raw_options) > 0:
                if isinstance(raw_options[0], dict) and 'name' in raw_options[0]:
                    options = [opt['name'] for opt in raw_options if isinstance(opt, dict) and 'name' in opt]
                elif isinstance(raw_options[0], str):
                    options = raw_options
                else:
                    options = raw_options
            else:
                options = raw_options
        
        # Wrap in Optional if not required
        required = getattr(field, 'required', False)
        if not required and pydantic_type != "Any":
            pydantic_type = f"{pydantic_type} | None"
        
        # Override with Literal for small enums (< 4 values)
        if options and not self._should_use_enum(options):
            values_str = ", ".join(f'"{v}"' for v in options)
            pydantic_type = f"Literal[{values_str}]"
            if not required:
                pydantic_type = f"{pydantic_type} | None"
        
        # Override with Enum class for large enums (>= 4 values)
        elif options and self._should_use_enum(options):
            enum_name = f"{python_name.title().replace('_', '')}Enum"
            pydantic_type = enum_name
            if not required:
                pydantic_type = f"{pydantic_type} | None"
        
        # Handle lists (child tables)
        is_list = getattr(field, 'is_list', False)
        children = getattr(field, 'children', None)
        if is_list or children:
            child_model_name = f"{python_name.title().replace('_', '')}"
            pydantic_type = f"list[{child_model_name}]"
        
        return {
            "name": field_name,
            "python_name": python_name,
            "pydantic_type": pydantic_type,
            "required": required,
            "default_value": getattr(field, 'default', None),
            "help": getattr(field, 'help', ''),
            "datasource": getattr(field, 'datasource', None),
            "readonly": False,  # TODO: Determine from schema if needed
            "validation": {
                "min": getattr(field, 'min_value', None),
                "max": getattr(field, 'max_value', None),
                "max_length": getattr(field, 'max_length', None),
            },
            "options": options,
            "enum_help": getattr(field, 'enum_help', None),
            "is_list": is_list,
            "children": children,
        }
    
    def _extract_datasource_fields(self, schema: EndpointSchema) -> dict[str, dict]:
        """
        Extract fields with datasource metadata for validation generation.
        
        Args:
            schema: Endpoint schema
            
        Returns:
            Dict mapping field paths to datasource metadata
            Example: {
                'srcintf': {
                    'field_path': 'srcintf.name',
                    'parent_field': 'srcintf',
                    'child_field': 'name',
                    'is_child_table': True,
                    'datasources': ['system.interface.name', 'system.zone.name']
                }
            }
        """
        datasource_fields = {}
        
        for field_name, field in schema.fields.items():
            # Check if field has children (child table)
            if field.children:
                for child_name, child_field in field.children.items():
                    datasource = getattr(child_field, 'datasource', None)
                    if datasource:
                        # Store by parent field name (e.g., 'srcintf')
                        datasource_fields[field_name] = {
                            'field_path': f"{field_name}.{child_name}",
                            'parent_field': field_name,
                            'child_field': child_name,
                            'is_child_table': True,
                            'datasources': datasource if isinstance(datasource, list) else [datasource],
                        }
            
            # Check if field itself has datasource (scalar field)
            else:
                datasource = getattr(field, 'datasource', None)
                if datasource:
                    datasource_fields[field_name] = {
                        'field_path': field_name,
                        'parent_field': field_name,
                        'child_field': None,
                        'is_child_table': False,
                        'datasources': datasource if isinstance(datasource, list) else [datasource],
                    }
        
        return datasource_fields
    
    def _generate_validation_methods(self, datasource_fields: dict) -> list[dict]:
        """
        Generate validation method metadata for template.
        
        Args:
            datasource_fields: Output from _extract_datasource_fields
            
        Returns:
            List of validation method definitions for template
        """
        validation_methods = []
        
        for field_name, metadata in datasource_fields.items():
            # Parse datasource endpoints
            endpoint_checks = []
            for ds in metadata['datasources']:
                # Parse datasource path (e.g., 'system.interface.name' -> 'system.interface')
                ds_parts = ds.split('.')
                endpoint_path = '.'.join(ds_parts[:-1])  # Remove '.name' suffix
                endpoint_display = endpoint_path.replace('.', '/')
                
                endpoint_checks.append({
                    'endpoint_path': endpoint_path,
                    'endpoint_display': endpoint_display,
                })
            
            # Generate method name
            python_field = field_name.replace('-', '_')
            method_name = f"validate_{python_field}_references"
            
            # Create validation method metadata
            validation_methods.append({
                'method_name': method_name,
                'field_name': field_name,
                'python_field': python_field,
                'child_field': metadata['child_field'],
                'is_child_table': metadata['is_child_table'],
                'endpoint_checks': endpoint_checks,
                'datasources': metadata['datasources'],
            })
        
        return validation_methods
    
    def generate(
        self,
        schema: EndpointSchema,
        output_dir: Path,
        generator_version: str = "0.6.0",
    ) -> Path:
        """
        Generate Pydantic model class file.
        
        Args:
            schema: Parsed schema
            output_dir: Base output directory (e.g., packages/fortios/hfortix_fortios/models)
            generator_version: Version of generator
            
        Returns:
            Path to generated model file
        """
        # Load template
        template = self.env.get_template("pydantic_model.py.j2")
        
        # Determine imports needed
        imports_needed = self._get_imports_needed(schema)
        
        # Prepare fields for template
        prepared_fields = {
            name: self._prepare_field_info(name, field)
            for name, field in schema.fields.items()
        }
        
        # Prepare child tables (fields with children)
        child_tables = {}
        for name, field in schema.fields.items():
            if field.children:
                child_fields = {
                    child_name: self._prepare_field_info(child_name, child_field)
                    for child_name, child_field in field.children.items()
                }
                child_tables[name] = {
                    "fields": child_fields,
                    "help": field.help,
                }
        
        # Extract datasource fields and generate validation methods
        datasource_fields = self._extract_datasource_fields(schema)
        validation_methods = self._generate_validation_methods(datasource_fields)
        
        # Check if we need async support (validation methods present)
        needs_async = len(validation_methods) > 0
        
        # Prepare template context
        context = {
            "schema": schema,
            "fields": prepared_fields,
            "child_tables": child_tables,
            "generator_version": generator_version,
            "generation_timestamp": self._get_timestamp(),
            "imports_needed": imports_needed,
            "validation_methods": validation_methods,
            "needs_async": needs_async,
        }
        
        # Render template
        rendered = template.render(**context)
        
        # Determine output path
        # Structure: output_dir/cmdb/firewall/policy.py
        safe_category = schema.category.replace("-", "_")
        category_dir = output_dir / safe_category
        
        # Create subdirectories for nested paths
        if "/" in schema.path:
            parts = schema.path.split("/")
            safe_parts = [p.replace("-", "_") for p in parts[:-1]]
            model_dir = category_dir / "/".join(safe_parts)
            model_filename = parts[-1].replace("-", "_")
        else:
            model_dir = category_dir
            model_filename = schema.path.replace("-", "_")
        
        model_dir.mkdir(parents=True, exist_ok=True)
        
        # Use schema.file_name for the actual filename
        output_file = model_dir / f"{schema.file_name}.py"
        
        # Write file
        with open(output_file, "w") as f:
            f.write(rendered)
        
        return output_file
    
    @staticmethod
    def _get_timestamp() -> str:
        """Get current UTC timestamp."""
        from datetime import datetime, timezone
        return datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
