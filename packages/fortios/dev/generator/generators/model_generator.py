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
        self.env.filters["title_words"] = self._title_words  # Python's str.title() behavior
    
    def _title_words(self, s: str) -> str:
        """
        Title-case a string like Python's str.title().
        
        Jinja's builtin 'title' filter only capitalizes the first letter,
        but Python's str.title() capitalizes after every non-alpha character.
        
        Args:
            s: Input string
            
        Returns:
            Title-cased string (e.g., 'ldb_method' -> 'Ldb_Method')
        """
        return s.title() if s else s
    
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
            Enum member name (e.g., "ACCEPT", "DENY", "V_1" for numeric values)
        """
        # Convert to uppercase, replace special chars with underscores
        enum_name = value.upper().replace("-", "_").replace(" ", "_").replace(".", "_").replace("+", "_PLUS")
        # Remove any remaining non-alphanumeric chars
        enum_name = "".join(c if c.isalnum() or c == "_" else "" for c in enum_name)
        # Prefix with 'V_' if starts with a digit (Python identifiers can't start with numbers)
        if enum_name and enum_name[0].isdigit():
            enum_name = f"V_{enum_name}"
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
            # Convert endpoint_path to valid Python attribute chain
            # e.g., "user/tacacs+" -> "user.tacacs_plus_"
            # e.g., "switch-controller/lldp" -> "switch_controller.lldp"
            endpoint_path = check['endpoint_path']
            # Replace + with _plus_, hyphens with underscores, then replace / with .
            python_path = endpoint_path.replace("+", "_plus_").replace("-", "_").replace("/", ".")
            lines.append(f"{line_indent}{keyword} await client.api.cmdb.{python_path}.exists(value):")
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
        
        # Check if this is a list type (child table)
        # Complex fields have children but are NOT lists (they're single objects)
        pydantic_type = field_info.get("pydantic_type", "")
        is_list = field_info.get("is_list", False) or (field_info.get("children") is not None and "list[" in pydantic_type)
        
        # Check if field uses an enum type
        uses_enum = field_info.get("uses_enum", False)
        enum_class_name = field_info.get("enum_class_name")
        
        # For list types, always use default_factory=list (ignore any default value)
        if is_list:
            if not field_info.get("required", False):
                constraints.append("default_factory=list")
        else:
            # Add default value for non-list fields
            default_value = field_info.get("default_value")
            python_type = field_info.get("python_type", "str")
            if default_value is not None and default_value != "":
                if uses_enum and enum_class_name and isinstance(default_value, str):
                    # Convert string default to enum member reference for mypy compatibility
                    enum_member = self._to_enum_name("", default_value)
                    constraints.append(f'default={enum_class_name}.{enum_member}')
                elif isinstance(default_value, str):
                    # Handle type mismatch: if field is int but default is string (e.g., "unspecified")
                    # use None as default instead since the string isn't a valid int value
                    if python_type == "int":
                        constraints.append("default=None")
                    else:
                        # Escape quotes and newlines in default string value
                        escaped_value = default_value.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n').replace('\r', '')
                        constraints.append(f'default="{escaped_value}"')
                elif isinstance(default_value, bool):
                    constraints.append(f'default={str(default_value)}')
                else:
                    constraints.append(f"default={default_value}")
            elif not field_info.get("required", False):
                constraints.append("default=None")
        
        # Add serialization alias if the field name was modified (e.g., list -> list_)
        # This ensures the model serializes to the original API field name
        if field_info.get("needs_alias", False):
            api_name = field_info.get("api_name", field_info.get("name", ""))
            constraints.append(f'serialization_alias="{api_name}"')
        
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
            "field_validator": False,
        }
        
        def check_field(field):
            """Check a single field for import needs."""
            nonlocal needs
            
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
            
            # Check for datasource (needs field_validator)
            if getattr(field, 'datasource', None):
                needs["field_validator"] = True
            
            # Check for optional (non-required fields)
            if not getattr(field, 'required', False):
                needs["optional"] = True
        
        def check_children_recursively(children_dict):
            """Recursively check all child fields including deeply nested ones."""
            for child_field in children_dict.values():
                check_field(child_field)
                # Recursively check nested children
                nested_children = getattr(child_field, 'children', None)
                if nested_children:
                    check_children_recursively(nested_children)
        
        # Check all top-level fields
        for field in schema.fields.values():
            check_field(field)
            
            # Also check child table fields recursively
            children = getattr(field, 'children', None)
            if children:
                check_children_recursively(children)
        
        return needs
    
    def _prepare_field_info(self, field_name: str, field: Any, class_prefix: str = "", child_table_name: str = "") -> dict:
        """
        Convert FieldMetadata to template-friendly dict.
        
        Args:
            field_name: Name of the field
            field: FieldMetadata object
            class_prefix: Prefix for class names (e.g., schema.class_name)
            child_table_name: Name of child table if this is a child table field
            
        Returns:
            Dict with processed field information
        """
        # Generate Python-safe field name
        import keyword
        import re
        # Python built-in names that shouldn't be used as field names
        PYTHON_BUILTINS = {
            'list', 'dict', 'set', 'tuple', 'str', 'int', 'float', 'bool',
            'type', 'object', 'id', 'hash', 'len', 'range', 'map', 'filter',
            'input', 'print', 'open', 'file', 'format', 'bytes', 'bytearray',
            'complex', 'frozenset', 'property', 'classmethod', 'staticmethod',
            'super', 'vars', 'dir', 'globals', 'locals', 'exec', 'eval',
            'compile', 'repr', 'ascii', 'bin', 'hex', 'oct', 'ord', 'chr',
            'any', 'all', 'min', 'max', 'sum', 'abs', 'round', 'pow', 'divmod',
            'sorted', 'reversed', 'enumerate', 'zip', 'next', 'iter', 'slice',
            'callable', 'isinstance', 'issubclass', 'hasattr', 'getattr', 'setattr', 'delattr',
        }
        # Remove angle brackets, replace hyphens and spaces with underscores
        python_name = field_name.replace("<", "").replace(">", "").replace("-", "_").replace(" ", "_")
        # Remove any other non-alphanumeric characters (except underscores)
        python_name = re.sub(r'[^a-zA-Z0-9_]', '', python_name)
        # Track if we need to add an alias (name was modified beyond just hyphen->underscore)
        needs_alias = False
        original_api_name = field_name  # The original API field name for serialization
        # Add suffix if it's a Python keyword or builtin
        if keyword.iskeyword(python_name) or python_name in PYTHON_BUILTINS:
            python_name = python_name + "_"
            needs_alias = True
        # Prefix with underscore if starts with digit
        if python_name and python_name[0].isdigit():
            python_name = "_" + python_name
            needs_alias = True
        
        # Determine Pydantic type
        field_type = getattr(field, 'type', 'string')
        pydantic_type = self._to_python_type(field_type)
        base_python_type = pydantic_type  # Store base type before modifications
        
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
            # Deduplicate options while preserving order (schema may have duplicates)
            if options:
                seen = set()
                unique_options = []
                for opt in options:
                    if opt not in seen:
                        seen.add(opt)
                        unique_options.append(opt)
                options = unique_options
        
        # Wrap in Optional if not required
        required = getattr(field, 'required', False)
        if not required and pydantic_type != "Any":
            pydantic_type = f"{pydantic_type} | None"
        
        # Override with Literal for small enums (< 4 values)
        uses_enum = False
        enum_class_name = None
        if options and not self._should_use_enum(options):
            values_str = ", ".join(f'"{v}"' for v in options)
            pydantic_type = f"Literal[{values_str}]"
            if not required:
                pydantic_type = f"{pydantic_type} | None"
        
        # Override with Enum class for large enums (>= 4 values)
        elif options and self._should_use_enum(options):
            # Build full enum class name with prefixes
            # For child table fields: {ClassPrefix}{ChildTableName}{FieldName}Enum
            # For main fields: {ClassPrefix}{FieldName}Enum
            child_prefix = ""
            if child_table_name:
                child_prefix = child_table_name.title().replace('-', '').replace('_', '')
            enum_name = f"{class_prefix}{child_prefix}{python_name.title().replace('_', '')}Enum"
            # Ensure enum name doesn't start with a digit
            if enum_name and enum_name[0].isdigit():
                enum_name = "V" + enum_name
            pydantic_type = enum_name
            uses_enum = True
            enum_class_name = enum_name
            if not required:
                pydantic_type = f"{pydantic_type} | None"
        
        # Handle lists - distinguish between child tables and multi-select options
        is_list = getattr(field, 'is_list', False)
        children = getattr(field, 'children', None)
        field_category = getattr(field, 'category', None)
        
        # Only generate child model reference if there are actual nested children
        # (true child tables), not for multi-select option fields
        if children:
            # Check if this is a 'complex' (single object) or 'table' (list) field
            # For nested children, include the parent path in the class name
            # e.g., api-gateway.quic becomes WebProxyApiGatewayQuic
            import re
            if child_table_name:
                # Build class name from parent path + this field name
                full_path = f"{child_table_name}.{field_name}"
                # Sanitize: remove <>, (), replace - and space with _
                sanitized_path = re.sub(r'[<>()]', '', full_path)
                sanitized_path = sanitized_path.replace('-', '_').replace(' ', '_')
                path_parts = sanitized_path.split('.')
                child_model_name = class_prefix + ''.join(
                    part.title().replace('_', '') for part in path_parts
                )
            else:
                # Top-level child table, just use class_prefix + field name
                child_model_name = f"{class_prefix}{python_name.title().replace('_', '')}"
            # Ensure class name doesn't start with a digit
            if child_model_name and child_model_name[0].isdigit():
                child_model_name = "V" + child_model_name
            
            # Determine if this is a single object (complex) or list (table)
            if field_category == 'complex':
                # Complex fields are single nested objects, not lists
                pydantic_type = f"{child_model_name} | None"
            else:
                # Table fields are lists of items
                pydantic_type = f"list[{child_model_name}]"
        elif is_list and options:
            # Multi-select option field - wrap existing enum/literal type in list
            # The pydantic_type already has the enum or Literal type from above
            # Remove the " | None" suffix if present, wrap in list, then add back
            if pydantic_type.endswith(" | None"):
                inner_type = pydantic_type[:-7]  # Remove " | None"
                pydantic_type = f"list[{inner_type}]"
            else:
                pydantic_type = f"list[{pydantic_type}]"
        elif is_list and not options:
            # Simple list without enum (e.g., list of strings)
            # Keep original base type but wrap in list
            base_type = self._to_python_type(getattr(field, 'type', 'string'))
            pydantic_type = f"list[{base_type}]"
        
        return {
            "name": field_name,
            "python_name": python_name,
            "pydantic_type": pydantic_type,
            "python_type": base_python_type,  # Base Python type (e.g., "int", "str") before Optional/Literal/Enum modifications
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
            "uses_enum": uses_enum,
            "enum_class_name": enum_class_name,
            "needs_alias": needs_alias,
            "api_name": original_api_name,
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
            
            # Generate method name - use proper Python identifier
            python_field = field_name.replace('-', '_').replace('+', '_plus_').replace(' ', '_')
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
    
    def _collect_all_child_tables(
        self, 
        fields: dict, 
        class_prefix: str, 
        parent_prefix: str = ""
    ) -> dict:
        """
        Recursively collect all child tables at all nesting levels.
        
        Args:
            fields: Dict of field name -> FieldMetadata
            class_prefix: The main schema class name prefix (e.g., "WebProxy")
            parent_prefix: Parent table name prefix for nested tables (e.g., "api-gateway")
            
        Returns:
            Dict mapping full child table names to their metadata
            Example: {
                "api-gateway": {"fields": {...}, "help": "...", "class_name": "WebProxyApiGateway"},
                "api-gateway.quic": {"fields": {...}, "help": "...", "class_name": "WebProxyApiGatewayQuic"},
            }
        """
        child_tables = {}
        
        for name, field in fields.items():
            children = getattr(field, 'children', None)
            if children:
                # Build the full path for this child table
                full_path = f"{parent_prefix}.{name}" if parent_prefix else name
                
                # Build the class name: ClassPrefix + all parent names + this name
                # e.g., "WebProxy" + "ApiGateway" + "Quic" = "WebProxyApiGatewayQuic"
                # Sanitize path: remove special chars like <>, replace - and space with _
                import re
                sanitized_path = re.sub(r'[<>()]', '', full_path)
                sanitized_path = sanitized_path.replace('-', '_').replace(' ', '_')
                path_parts = sanitized_path.split('.')
                class_name = class_prefix + ''.join(
                    part.title().replace('_', '') for part in path_parts
                )
                
                # Prepare child fields for template
                child_fields = {
                    child_name: self._prepare_field_info(
                        child_name, child_field,
                        class_prefix=class_prefix,
                        child_table_name=full_path.replace('.', '_')  # Use full path for enum naming
                    )
                    for child_name, child_field in children.items()
                }
                
                child_tables[full_path] = {
                    "fields": child_fields,
                    "help": getattr(field, 'help', ''),
                    "class_name": class_name,
                }
                
                # Recursively collect nested child tables
                nested_tables = self._collect_all_child_tables(
                    children, class_prefix, full_path
                )
                child_tables.update(nested_tables)
        
        return child_tables

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
        
        # Prepare fields for template - include class prefix for type references
        prepared_fields = {
            name: self._prepare_field_info(name, field, class_prefix=schema.class_name)
            for name, field in schema.fields.items()
        }
        
        # Collect all child tables recursively (including nested children)
        child_tables = self._collect_all_child_tables(schema.fields, schema.class_name)
        
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
