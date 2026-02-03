#!/usr/bin/env python3
"""
Test Generator for FortiOS API Endpoints

Generates basic automated tests for:
- GET operations (auto_test_get_*)
- Validator functions (auto_test_validator_*)

Usage:
    python generate_tests.py cmdb firewall/policy
    python generate_tests.py cmdb firewall.service/custom
"""

import argparse
import json
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))
# Add generator root to path for utils module
sys.path.insert(0, str(Path(__file__).parent.parent))

from schema_management.schema_parser import SchemaParser, EndpointSchema
from utils.naming import kebab_to_snake
from jinja2 import Environment, FileSystemLoader


class TestGenerator:
    """Generate pytest test files from schemas."""
    
    def __init__(self, template_dir: Path):
        """
        Initialize test generator.
        
        Args:
            template_dir: Directory containing Jinja2 templates
        """
        self.env = Environment(
            loader=FileSystemLoader(str(template_dir)),
            trim_blocks=True,
            lstrip_blocks=True,
        )
        # Add custom filters - use shared kebab_to_snake from utils.naming
        self.env.filters['kebab_to_snake'] = kebab_to_snake
        self.env.filters['path_to_attribute'] = self._path_to_attribute
        self.env.filters['is_python_keyword'] = self._is_python_keyword
        self.env.filters['is_python_builtin'] = self._is_python_builtin
        self.env.filters['safe_identifier'] = self._safe_identifier
    
    # Python builtins that conflict as METHOD names (not module names)
    # These are methods like .list(), .clear(), .update() that shadow dict/class methods
    # NOTE: This is different from module names - 'license' as a module is fine,
    # but 'list' as a method on a class would shadow the list() builtin
    PYTHON_BUILTIN_METHODS = frozenset({
        # Common dict/object methods that conflict when used as method names
        'list', 'dict', 'set', 'get', 'update', 'pop', 'clear', 'copy',
        'keys', 'values', 'items', 'format', 'filter',
    })

    # Removed _kebab_to_snake - now using shared function from utils.naming
    
    @classmethod
    def _safe_identifier(cls, value: str, is_method: bool = False) -> str:
        """
        Convert a single name to a safe Python identifier.
        
        Args:
            value: The identifier to make safe
            is_method: If True, also check against PYTHON_BUILTIN_METHODS
        
        Handles:
        - Hyphens -> underscores
        - Plus signs -> _plus
        - Leading digits -> prepend 'x'
        - Python keywords -> append '_'
        - Python builtin methods (if is_method=True) -> append '_'
        """
        import keyword
        
        # Replace special characters
        result = value.replace('-', '_').replace('+', '_plus')
        
        # Fix names that start with a digit by prepending 'x'
        if result and result[0].isdigit():
            result = f"x{result}"
        
        # Handle Python keywords (always)
        if keyword.iskeyword(result):
            result = f"{result}_"
        # Handle Python builtin methods (only for method names at end of path)
        elif is_method and result in cls.PYTHON_BUILTIN_METHODS:
            result = f"{result}_"
        
        return result
    
    @classmethod
    def _path_to_attribute(cls, value: str) -> str:
        """
        Convert schema path to Python attribute access path.
        
        Examples:
            'firewall/policy' -> 'firewall.policy'
            'firewall.ipmacbinding/setting' -> 'firewall.ipmacbinding.setting'
            'firewall.schedule/onetime' -> 'firewall.schedule.onetime'
            'vpn/ike/clear' -> 'vpn.ike.clear'  (clear is fine as attribute)
            'wifi/network/list' -> 'wifi.network.list'  (list is fine as attribute)
            'license/status' -> 'license.status'  (license is a module, not renamed)
            'system/global' -> 'system.global_'  (global is a KEYWORD, needs underscore)
        
        Rules:
            - Dots stay as dots (they represent nested modules)
            - Slashes become dots (they represent attribute access)
            - Hyphens become underscores (Python identifier compatibility)
            - Plus signs become '_plus'
            - Only Python KEYWORDS get underscore suffix (global, class, import, etc.)
            - Python builtins (list, filter, set) do NOT need underscore for attributes
        """
        # Split by dots and slashes to get individual parts
        # First replace slashes with dots, then split
        value = value.replace('/', '.')
        parts = value.split('.')
        
        # Apply safe_identifier to each part
        # is_method=False means builtins won't get underscore suffix
        safe_parts = []
        for part in parts:
            safe_parts.append(cls._safe_identifier(part, is_method=False))
        
        return '.'.join(safe_parts)
    
    @staticmethod
    def _is_python_keyword(value: str) -> bool:
        """Check if a value is a Python reserved keyword."""
        import keyword
        return keyword.iskeyword(value)
    
    @classmethod
    def _is_python_builtin(cls, value: str) -> bool:
        """Check if a value is a Python builtin method that needs underscore suffix."""
        # Convert to snake_case first to match how it would appear in code
        safe_value = value.replace('-', '_').replace('+', '_plus')
        return safe_value in cls.PYTHON_BUILTIN_METHODS
    
    def generate(self, schema: EndpointSchema, output_dir: Path) -> Path | None:
        """
        Generate test file from schema.
        
        Args:
            schema: Parsed endpoint schema
            output_dir: Base output directory for tests
            
        Returns:
            Path to generated test file (or None if skipped)
        """
        # Skip empty or invalid schemas
        if not schema.path or schema.path.strip() == "":
            return None
            
        # Skip metadata/version endpoints that would create invalid Python syntax
        # Example: v7.6 creates fgt.api.v7.6.index which is invalid (dots in numbers)
        if "." in schema.category or any(c.isdigit() and "." in schema.category for c in schema.category):
            return None
        
        # Skip schemas from dot-notation directories (duplicates of slash notation)
        # Example: skip schemas from 'switch-controller.qos/' in favor of 'switch-controller/qos/'
        # These create duplicate endpoints like qos_qos_policy vs qos/qos_policy
        if schema.source_file:
            source_path = Path(schema.source_file)
            # Get the path relative to the schemas directory
            # E.g., cmdb/switch-controller.qos/qos-policy.json
            try:
                # Find the part after v7.6 (or similar version)
                parts = source_path.parts
                if 'v7.6' in parts or 'v7.4' in parts or 'v7.2' in parts:
                    version_idx = next(i for i, p in enumerate(parts) if p.startswith('v7.'))
                    # Check directories between version and filename for dots
                    for part in parts[version_idx+1:-1]:  # Skip version and filename
                        if '.' in part and '-' in part:  # e.g., 'switch-controller.qos'
                            return None
            except (ValueError, StopIteration):
                pass
        
        # Skip deeply nested LOG endpoints (more than 2 levels deep)
        # These don't map cleanly to Python attributes
        # Example: log/disk/virus/archive -> fgt.api.log.disk.virus.archive (but virus doesn't have archive attr)
        # Also skip log/search/* as these require special handling
        if schema.category == "log":
            # Skip log/search/* endpoints (not yet properly generated)
            if schema.path.startswith("search/"):
                return None
            path_depth = len(schema.path.split("/"))
            if path_depth > 2:  # Allow log/disk/event, but skip log/disk/virus/archive
                return None
        
        # Build output path
        # schema.path is like "firewall/policy" or "firewall/ssh_setting"
        path_parts = schema.path.split("/")
        
        # Create directory structure: {output_dir}/.tests/pytests/api/{category}/{first_part}/
        # Convert hyphens to underscores for Python package names
        safe_first_part = path_parts[0].replace("-", "_")
        test_dir = output_dir / ".tests" / "pytests" / "api" / schema.category / safe_first_part
        test_dir.mkdir(parents=True, exist_ok=True)
        
        # Generate test file: auto_test_{endpoint_name}.py
        test_file = test_dir / f"auto_test_{schema.name}.py"
        
        # Load template
        template = self.env.get_template("test_basic.py.j2")
        
        # Extract test data from schema
        test_data = self._extract_test_data(schema)
        
        # Extract HTTP methods from schema source file (if available)
        # Also check if this is a category-only endpoint (no actual methods)
        http_methods = self._extract_http_methods(schema)
        
        # Check if this is a category endpoint (container only, no direct API methods)
        is_category_only = self._is_category_endpoint(schema)
        
        # Skip test generation entirely for category-only endpoints (wrappers with no methods)
        if is_category_only:
            return None
        
        # Additionally, check if endpoint class file exists and is a wrapper directory
        # Example: monitor/system/firmware/ is a directory with __init__.py that wraps sub-endpoints
        if self._is_wrapper_directory(schema):
            return None
        
        # Render template
        content = template.render(
            schema=schema,
            test_data=test_data,
            http_methods=http_methods,
        )
        
        # Write file
        test_file.write_text(content)
        
        return test_file
    
    def _extract_http_methods(self, schema: EndpointSchema) -> list[str]:
        """
        Extract HTTP methods from schema metadata.
        
        Args:
            schema: Parsed endpoint schema
            
        Returns:
            List of HTTP methods (e.g., ['GET'], ['POST'], ['GET', 'POST'])
        """
        # Try to load the source schema file to get metadata
        if schema.source_file:
            try:
                import json
                from pathlib import Path
                
                source_path = Path(schema.source_file)
                if source_path.exists():
                    with open(source_path) as f:
                        schema_data = json.load(f)
                        # Check top-level http_methods first (new schema format)
                        methods = schema_data.get('http_methods', [])
                        if methods:
                            return [m.upper() for m in methods]
                        # Fallback to _metadata for older schemas
                        metadata = schema_data.get('_metadata', {})
                        methods = metadata.get('http_methods', [])
                        if methods:
                            return [m.upper() for m in methods]
            except Exception:
                pass
        
        # Default based on category
        if schema.category == 'cmdb':
            return ['GET', 'POST', 'PUT', 'DELETE']
        elif schema.category in ['monitor', 'service']:
            return ['GET']  # Default to GET for monitor/service
        elif schema.category == 'log':
            return ['GET']
        
        return ['GET']
    
    def _is_category_endpoint(self, schema: EndpointSchema) -> bool:
        """
        Check if this is a category-only endpoint (container with no direct API methods).
        
        Category endpoints have sub-actions but don't themselves have GET/POST/etc methods.
        Example: monitor/firewall/acl (has acl/clear_counters but no direct GET)
        
        Key indicators:
        - path is null
        - results is null  
        - children is {} (empty dict, not null)
        
        Args:
            schema: Parsed endpoint schema
            
        Returns:
            True if this is a category endpoint, False otherwise
        """
        # Try to load the source schema file to check for path and results fields
        if schema.source_file:
            try:
                import json
                from pathlib import Path
                
                source_path = Path(schema.source_file)
                if source_path.exists():
                    with open(source_path) as f:
                        schema_data = json.load(f)
                        
                        # Category endpoints have path=null AND results=null
                        # Regular endpoints have path="..." AND results={...}
                        path = schema_data.get('path')
                        results = schema_data.get('results')
                        children = schema_data.get('children')
                        
                        # If both path and results are null, it's a category endpoint
                        if path is None and results is None:
                            return True
                        
                        # If children is an empty dict (not null) and results is null
                        if isinstance(children, dict) and len(children) == 0 and results is None:
                            return True
                            
            except Exception:
                pass
        
        return False
    
    def _is_wrapper_directory(self, schema: EndpointSchema) -> bool:
        """
        Check if this endpoint is implemented as a wrapper directory (not a direct endpoint).
        
        Wrapper directories contain __init__.py with a wrapper class that exposes sub-endpoints
        as attributes, but the wrapper itself doesn't have get/post/etc methods.
        
        Example:
            monitor/system/firmware/ -> directory with __init__.py
                Contains: Firmware class with self.upgrade = Upgrade(client)
                Does NOT have: get(), post(), etc.
        
        Args:
            schema: Parsed endpoint schema
            
        Returns:
            True if this is a wrapper directory, False otherwise
        """
        from pathlib import Path
        
        # Reconstruct the expected output file path for this endpoint
        # Base: packages/fortios/hfortix_fortios/api/v2/{category}/{path}
        base_dir = Path(__file__).parent.parent.parent.parent / "packages" / "fortios" / "hfortix_fortios" / "api" / "v2"
        
        # Convert path to filesystem path (replace / with directory separator)
        path_parts = schema.path.split("/") if schema.path else []
        if not path_parts:
            return False
        
        # Build expected path
        category_dir = base_dir / schema.category
        endpoint_path = category_dir / Path(*path_parts)
        
        # Check if it's a directory (not a .py file)
        if endpoint_path.is_dir():
            # Check if __init__.py exists (wrapper pattern)
            init_file = endpoint_path / "__init__.py"
            if init_file.exists():
                # It's a wrapper directory - skip test generation
                return True
        
        return False
    
    def _extract_test_data(self, schema: EndpointSchema) -> dict:
        """
        Extract test data from schema.
        
        Args:
            schema: Parsed endpoint schema
            
        Returns:
            Dictionary with test data
        """
        # Get required fields with metadata
        required_fields = []
        for field_name in schema.required_fields:
            if field_name in schema.fields:
                field = schema.fields[field_name]
                # Generate sample value
                if field.type == "option" and field.options:
                    sample_value = f'"{field.options[0]}"'
                elif field.type == "integer":
                    sample_value = str(field.default if field.default is not None else 1)
                elif field.type == "string":
                    sample_value = f'"test_{field_name}"'
                else:
                    sample_value = f'"{field.default}"' if field.default else '""'
                
                required_fields.append({
                    "name": field_name,
                    "type": field.type,
                    "sample_value": sample_value,
                })
        
        # Get fields with defaults
        default_fields = {
            name: field.default
            for name, field in schema.fields.items()
            if field.default is not None
        }
        
        # Get enum fields with metadata
        enum_fields = []
        for name, field in schema.fields.items():
            if field.options:
                enum_fields.append({
                    "name": name,
                    "type": field.type,
                    "options": field.options,
                })
        
        # Build minimal valid payload for POST tests
        # Use required fields + defaults
        minimal_payload = {}
        
        for field_name in schema.required_fields:
            if field_name not in schema.fields:
                continue
                
            field = schema.fields[field_name]
            
            # Generate sample value based on type
            if field.type == "option" and field.options:
                # Use first option
                minimal_payload[field_name] = field.options[0]
            elif field.type == "string":
                if field.datasource:
                    # Reference field - use common value
                    minimal_payload[field_name] = [{"name": "all"}]
                else:
                    minimal_payload[field_name] = f"test_{field_name}"
            elif field.type == "integer":
                minimal_payload[field_name] = field.default if field.default is not None else 0
            elif field.category == "table":
                # Table field - use list with minimal object
                minimal_payload[field_name] = [{"name": "default"}]
            else:
                # Generic default
                minimal_payload[field_name] = field.default if field.default is not None else ""
        
        # Add some common defaults that are often required
        if "status" not in minimal_payload and "status" in schema.fields:
            minimal_payload["status"] = "enable"
        
        if "name" not in minimal_payload and "name" in schema.fields and schema.mkey != "name":
            minimal_payload["name"] = f"auto_test_{schema.name}"
        
        return {
            "required_fields": required_fields,
            "default_fields": default_fields,
            "enum_fields": enum_fields,
            "minimal_payload": minimal_payload,
            "mkey": schema.mkey,
            "mkey_type": schema.mkey_type,
        }


def main():
    parser = argparse.ArgumentParser(
        description="Generate pytest tests from FortiOS schemas",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python generate_tests.py cmdb firewall/policy
  python generate_tests.py cmdb firewall.service/custom
        """
    )
    
    parser.add_argument("category", help="API category (cmdb, monitor, log, service)")
    parser.add_argument("endpoint", help="Endpoint path (e.g., firewall/policy)")
    parser.add_argument("--schema-file", help="Path to schema JSON file")
    parser.add_argument("--output-dir", help="Base output directory (default: project root)")
    
    args = parser.parse_args()
    
    print(f"🧪 Generating tests for {args.category}.{args.endpoint}\n")
    
    # Paths
    base_dir = Path(__file__).parent
    if args.output_dir:
        output_dir = Path(args.output_dir)
    else:
        output_dir = base_dir.parent.parent  # Go up to project root
    
    template_dir = base_dir / "templates"
    
    # Load schema
    if args.schema_file:
        schema_file = Path(args.schema_file)
    else:
        # Try to find in schemas directory
        schema_name = args.endpoint.split("/")[-1].replace("-", "_")
        schema_dir = base_dir.parent / "schemas" / args.category / args.endpoint.split("/")[0]
        schema_file = schema_dir / f"{schema_name}.json"
    
    if not schema_file.exists():
        print(f"❌ Schema file not found: {schema_file}")
        print(f"   Generate schema first with: python download_schemas.py {args.category} {args.endpoint}")
        sys.exit(1)
    
    print(f"📂 Schema: {schema_file}")
    
    # Parse schema
    schema_dict = json.loads(schema_file.read_text())
    
    # Add metadata if not present
    if "_metadata" not in schema_dict:
        schema_dict = {
            "_metadata": {
                "category": args.category,
                "endpoint_path": args.endpoint,
            },
            "results": schema_dict
        }
    
    schema = SchemaParser.parse(schema_dict, str(schema_file))
    
    print(f"📊 Parsed schema:")
    print(f"   Category: {schema.category}")
    print(f"   Name: {schema.name}")
    print(f"   Path: {schema.path}")
    print(f"   Required fields: {len(schema.required_fields)}")
    print()
    
    # Generate tests
    print("✨ Generating tests...")
    test_gen = TestGenerator(template_dir)
    test_file = test_gen.generate(schema, output_dir)
    
    if test_file:
        print(f"   ✅ {test_file}")
        print()
        
        print("✅ Test generation complete!")
        print(f"\n📄 Generated file:")
        print(f"   {test_file}")
        print(f"\n🧪 Run tests:")
        print(f"   cd {output_dir}")
        print(f"   pytest {test_file.relative_to(output_dir)} -v")
    else:
        print("   ⏭️  Skipped (invalid schema or unsupported structure)")


if __name__ == "__main__":
    main()
