#!/usr/bin/env python3
"""
Docstring Enhancement Module

Generates rich, detailed docstrings from schema metadata including:
- Field descriptions and help text
- Example values
- Validation constraints
- Related endpoints
- Common patterns
- Performance tips
"""

from typing import Any


class DocstringEnhancer:
    """Enhance docstrings with rich metadata from schemas."""
    
    @staticmethod
    def get_literal_type(field_info: dict[str, Any]) -> str | None:
        """
        Extract Literal type from field metadata.
        
        Args:
            field_info: Field information from schema
            
        Returns:
            Literal type string or None
            
        Examples:
            >>> get_literal_type({"validation": {"allowed_values": ["accept", "deny"]}})
            "Literal['accept', 'deny']"
        """
        # Check pydantic_type first
        pydantic_type = field_info.get("pydantic_type", "")
        if pydantic_type and pydantic_type.startswith("Literal["):
            return pydantic_type
        
        # Check validation.allowed_values
        validation = field_info.get("validation", {})
        allowed_values = validation.get("allowed_values", [])
        if allowed_values:
            quoted = [f"'{v}'" for v in allowed_values]
            return f"Literal[{', '.join(quoted)}]"
        
        # Check options (now a list of strings after schema parser fix)
        options = field_info.get("options", [])
        if options:
            # Options are now already extracted as strings (not dicts)
            if isinstance(options, list) and len(options) > 0:
                if isinstance(options[0], dict):
                    # Old format - extract names
                    values = [opt["name"] for opt in options if "name" in opt]
                else:
                    # New format - already strings
                    values = options
                
                if values:
                    quoted = [f"'{v}'" for v in values]
                    return f"Literal[{', '.join(quoted)}]"
        
        return None
    
    @staticmethod
    def enhance_parameter_doc(
        param_name: str,
        field_info: dict[str, Any],
        indent: str = "            "
    ) -> str:
        """
        Create enhanced parameter documentation.
        
        Args:
            param_name: Parameter name
            field_info: Field metadata from schema
            indent: Indentation for multiline docs
            
        Returns:
            Enhanced parameter documentation string
        """
        parts = []
        
        # Parameter name and type
        help_text = field_info.get("help", "")
        if help_text:
            parts.append(f"{param_name}: {help_text}")
        else:
            parts.append(f"{param_name}: Configuration parameter")
        
        # Example if available
        example = field_info.get("example")
        if example:
            parts.append(f"{indent}Example: {example}")
        
        # Validation constraints
        validation = field_info.get("validation", {})
        
        # Length constraints
        max_length = validation.get("max_length")
        if max_length:
            parts.append(f"{indent}Max length: {max_length}")
        
        # Numeric range
        min_val = validation.get("min")
        max_val = validation.get("max")
        if min_val is not None or max_val is not None:
            if min_val is not None and max_val is not None:
                parts.append(f"{indent}Range: {min_val} to {max_val}")
            elif min_val is not None:
                parts.append(f"{indent}Min: {min_val}")
            elif max_val is not None:
                parts.append(f"{indent}Max: {max_val}")
        
        # Allowed values (for enums)
        allowed_values = validation.get("allowed_values", [])
        if allowed_values and len(allowed_values) <= 10:
            values_str = ", ".join(allowed_values)
            parts.append(f"{indent}Valid values: {values_str}")
        
        # Datasource (foreign key reference)
        datasource = field_info.get("datasource")
        if datasource:
            parts.append(f"{indent}References: {datasource}")
        
        return "\n".join(parts)
    
    @staticmethod
    def generate_method_examples(
        method: str,
        endpoint_path: str,
        category: str,
        mkey: str | None,
        fields: dict[str, Any],
        indent: str = "            "
    ) -> list[str]:
        """
        Generate practical code examples for method.
        
        Args:
            method: HTTP method (GET, POST, PUT, DELETE)
            endpoint_path: Endpoint path (e.g., "firewall/policy")
            category: API category (cmdb, monitor, etc.)
            mkey: Primary key field name
            fields: Field definitions
            indent: Indentation
            
        Returns:
            List of example strings
        """
        examples = []
        python_path = endpoint_path.replace('/', '.').replace('-', '_')
        
        if method == "GET":
            # List all
            examples.append(
                f">>> # Get all objects\n"
                f"{indent}>>> result = fgt.api.{category}.{python_path}.get()\n"
                f"{indent}>>> print(f\"Found {{len(result['results'])}} objects\")"
            )
            
            # Get specific
            if mkey:
                mkey_snake = mkey.replace('-', '_')
                mkey_type = fields.get(mkey, {}).get("python_type", "str")
                example_val = "1" if mkey_type == "int" else "'my-object'"
                examples.append(
                    f">>> # Get specific object\n"
                    f"{indent}>>> result = fgt.api.{category}.{python_path}.get({mkey_snake}={example_val})"
                )
            
            # Filtered query
            examples.append(
                f">>> # Filter results\n"
                f"{indent}>>> result = fgt.api.{category}.{python_path}.get(\n"
                f"{indent}...     filter=[\"status==enable\"]\n"
                f"{indent}... )"
            )
        
        elif method == "POST":
            # Find 2-3 simple required/common fields for example
            sample_fields = {}
            for fname, finfo in list(fields.items())[:5]:
                if fname == mkey or finfo.get("required"):
                    example = finfo.get("example")
                    if example:
                        sample_fields[fname.replace('-', '_')] = repr(example)
                if len(sample_fields) >= 3:
                    break
            
            if sample_fields:
                field_lines = ",\n".join([
                    f"{indent}...     {k}={v}"
                    for k, v in sample_fields.items()
                ])
                examples.append(
                    f">>> # Create new object\n"
                    f"{indent}>>> result = fgt.api.{category}.{python_path}.create(\n"
                    f"{field_lines}\n"
                    f"{indent}... )"
                )
        
        elif method == "PUT":
            if mkey:
                mkey_snake = mkey.replace('-', '_')
                examples.append(
                    f">>> # Update object\n"
                    f"{indent}>>> result = fgt.api.{category}.{python_path}.update(\n"
                    f"{indent}...     {mkey_snake}=1,\n"
                    f"{indent}...     comment='Updated via API'\n"
                    f"{indent}... )"
                )
        
        elif method == "DELETE":
            if mkey:
                mkey_snake = mkey.replace('-', '_')
                examples.append(
                    f">>> # Delete object\n"
                    f"{indent}>>> result = fgt.api.{category}.{python_path}.delete({mkey_snake}=1)"
                )
        
        return examples
    
    @staticmethod
    def generate_common_patterns(
        endpoint_path: str,
        category: str,
        has_mkey: bool
    ) -> list[str]:
        """
        Generate common usage patterns section.
        
        Args:
            endpoint_path: Endpoint path
            category: API category
            has_mkey: Whether endpoint has primary key
            
        Returns:
            List of pattern examples
        """
        python_path = endpoint_path.replace('/', '.').replace('-', '_')
        patterns = []
        
        if has_mkey:
            # Idempotent creation
            patterns.append(
                "Idempotent Creation:\n"
                f"            >>> if not fgt.api.{category}.{python_path}.exists(name='obj'):\n"
                f"            ...     fgt.api.{category}.{python_path}.create(name='obj', ...)"
            )
            
            # Safe deletion
            patterns.append(
                "Safe Deletion:\n"
                f"            >>> if fgt.api.{category}.{python_path}.exists(name='obj'):\n"
                f"            ...     fgt.api.{category}.{python_path}.delete(name='obj')"
            )
            
            # Bulk operations
            patterns.append(
                "Bulk Operations:\n"
                f"            >>> for item in items:\n"
                f"            ...     try:\n"
                f"            ...         fgt.api.{category}.{python_path}.create(**item)\n"
                f"            ...     except DuplicateResourceError:\n"
                f"            ...         fgt.api.{category}.{python_path}.update(**item)"
            )
        
        return patterns
    
    @staticmethod
    def add_performance_tips(
        method: str,
        is_readonly: bool = False,
        has_child_tables: bool = False
    ) -> list[str]:
        """
        Generate performance tips for method.
        
        Args:
            method: HTTP method
            is_readonly: Whether endpoint is read-only reference data
            has_child_tables: Whether object has child tables
            
        Returns:
            List of performance tips
        """
        tips = []
        
        if method == "GET":
            if is_readonly:
                tips.append("Readonly reference data is automatically cached (24hr TTL)")
            
            if has_child_tables:
                tips.append(
                    "Use format parameter to fetch only needed fields:\n"
                    "                format=['name', 'status']  # Faster for large tables"
                )
            
            tips.append(
                "Use count format for existence checks:\n"
                "                action='count'  # Returns count only, not data"
            )
        
        elif method == "POST":
            tips.append("Typical response time: 50-200ms")
            tips.append("Rate limit: ~100 requests/second")
            tips.append("For bulk operations (>10 items), consider batching")
        
        return tips


if __name__ == "__main__":
    # Test
    enhancer = DocstringEnhancer()
    
    # Test Literal extraction
    field_info = {
        "validation": {
            "allowed_values": ["accept", "deny", "ipsec"]
        }
    }
    print(enhancer.get_literal_type(field_info))
    # Output: Literal['accept', 'deny', 'ipsec']
