#!/usr/bin/env python3
"""
LOG Endpoint Generator

Special generator for LOG category endpoints that have path parameters.
Unlike CMDB/Monitor/Service endpoints, LOG endpoints use parameterized paths like:
  /log/disk/{type}/archive-download
  /log/disk/event/{subtype}/raw

This generator creates nested classes for each parameter value to provide
a clean, type-safe API:
  fgt.api.log.disk.ips.archive.get()
  fgt.api.log.disk.event.vpn.get()
"""

from pathlib import Path
from typing import Dict, List, Set, Any
import json
from utils.naming import to_class_name


class LogEndpointGenerator:
    """Generator for LOG category endpoints with path parameters."""
    
    def __init__(self, swagger_docs_dir: Path, output_dir: Path):
        """
        Initialize LOG endpoint generator.
        
        Args:
            swagger_docs_dir: Directory containing Swagger/OpenAPI docs
            output_dir: Base output directory for generated files
        """
        self.swagger_docs_dir = swagger_docs_dir
        self.output_dir = output_dir
        self.log_dir = output_dir / "log"
        
    def generate_all(self) -> Dict[str, int]:
        """
        Generate all LOG endpoints.
        
        Returns:
            Dict with counts: {'disk': 15, 'memory': 12, ...}
        """
        # Clean up old files first
        print(f"\n🧹 Cleaning up old LOG files...")
        self._cleanup_old_files()
        
        log_swagger_dir = self.swagger_docs_dir / "log"
        
        if not log_swagger_dir.exists():
            print(f"⚠️  LOG Swagger directory not found: {log_swagger_dir}")
            return {}
        
        # Find all LOG Swagger files
        swagger_files = list(log_swagger_dir.glob("*.json"))
        
        print(f"\n🔍 Found {len(swagger_files)} LOG Swagger files")
        
        stats = {}
        subcategories = []
        
        for swagger_file in sorted(swagger_files):
            # Extract subcategory from filename
            # e.g., "FortiOS 7.6 FortiOS 7.6.5 Log API disk.json" -> "disk"
            filename = swagger_file.stem
            if " disk" in filename.lower():
                subcategory = "disk"
            elif " memory" in filename.lower():
                subcategory = "memory"
            elif " fortianalyzer" in filename.lower():
                subcategory = "fortianalyzer"
            elif " forticloud" in filename.lower():
                subcategory = "forticloud"
            elif " search" in filename.lower():
                subcategory = "search"
            else:
                print(f"⚠️  Unknown LOG subcategory in: {filename}")
                continue
            
            subcategories.append(subcategory)
            print(f"\n📋 Processing {subcategory}...")
            count = self._generate_subcategory(swagger_file, subcategory)
            stats[subcategory] = count
        
        # Generate __init__.py and .pyi
        print(f"\n📝 Generating __init__.py and __init__.pyi...")
        self._generate_init(subcategories)
        self._generate_init_pyi(subcategories)
        
        # Generate .pyi stubs for each subcategory
        print(f"\n📝 Generating .pyi stubs...")
        self._generate_pyi_stubs(subcategories)
        
        # Generate tests
        print(f"\n🧪 Generating tests...")
        self._generate_tests(subcategories)
            
        return stats
    
    def _cleanup_old_files(self):
        """Remove old generated LOG files."""
        if not self.log_dir.exists():
            return
        
        import shutil
        
        # Remove all .py and .pyi files except __pycache__
        for file in self.log_dir.glob("*.py"):
            if file.name != "__pycache__":
                file.unlink()
                print(f"  🗑️  Removed {file.name}")
        
        for file in self.log_dir.glob("*.pyi"):
            file.unlink()
            print(f"  🗑️  Removed {file.name}")
        
        # Remove old subdirectories (disk/, memory/, etc.)
        for item in self.log_dir.iterdir():
            if item.is_dir() and item.name not in ('__pycache__', '_helpers'):
                shutil.rmtree(item)
                print(f"  🗑️  Removed directory {item.name}/")
    
    def _generate_subcategory(self, swagger_file: Path, subcategory: str) -> int:
        """Generate endpoints for a LOG subcategory."""
        with open(swagger_file) as f:
            swagger = json.load(f)
        
        paths = swagger.get('paths', {})
        
        # Analyze paths to find structure
        path_structure = self._analyze_paths(paths)
        
        # Generate the main class file
        output_file = self.log_dir / f"{subcategory}.py"
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        content = self._generate_class_file(subcategory, path_structure, paths)
        output_file.write_text(content)
        
        print(f"  ✅ Generated {output_file}")
        
        return len(paths)
    
    def _analyze_paths(self, paths: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze Swagger paths to extract structure.
        
        Returns structure like:
        {
            'event': {
                'param_name': 'subtype',
                'param_values': ['vpn', 'user', 'system', ...],
                'endpoints': {
                    'raw': '/disk/event/{subtype}/raw',
                    '': '/disk/event/{subtype}'
                }
            },
            'ips': {
                'param_name': 'type',
                'is_value': True,
                'endpoints': {
                    'archive': '/disk/{type}/archive',
                    'raw': '/disk/{type}/raw'
                }
            }
        }
        """
        structure = {}
        
        for path, methods in paths.items():
            # Skip root path
            if path == f"/{path.split('/')[1]}":
                continue
            
            parts = path.strip('/').split('/')
            
            # Check if path has parameters
            if '{' in path:
                # Extract parameter info from GET method
                get_method = methods.get('get', {})
                params = get_method.get('parameters', [])
                
                # Find path parameter
                path_param = None
                for param in params:
                    if param.get('in') == 'path':
                        path_param = param
                        break
                
                if not path_param:
                    continue
                
                param_name = path_param.get('name')
                param_values = path_param.get('enum', [])
                
                # Determine the group (what comes before the parameter)
                param_idx = parts.index(f'{{{param_name}}}')
                
                if param_idx > 1:
                    # e.g., /disk/event/{subtype} -> group is 'event'
                    group = parts[param_idx - 1]
                    endpoint_name = '/'.join(parts[param_idx + 1:]) or ''
                    
                    if group not in structure:
                        structure[group] = {
                            'param_name': param_name,
                            'param_values': set(),
                            'endpoints': {}
                        }
                    
                    structure[group]['param_values'].update(param_values)
                    structure[group]['endpoints'][endpoint_name] = path
                else:
                    # e.g., /disk/{type}/archive -> each type value becomes a group
                    endpoint_name = '/'.join(parts[param_idx + 1:])
                    
                    for value in param_values:
                        py_name = value.replace('-', '_')
                        
                        if py_name not in structure:
                            structure[py_name] = {
                                'param_name': param_name,
                                'param_value': value,
                                'is_value': True,
                                'endpoints': {}
                            }
                        
                        structure[py_name]['endpoints'][endpoint_name] = path
            else:
                # No parameters - direct endpoint
                # e.g., /disk or /search/abort
                if len(parts) > 1:
                    endpoint_name = parts[-1]
                    if 'direct' not in structure:
                        structure['direct'] = {'endpoints': {}}
                    structure['direct']['endpoints'][endpoint_name] = path
        
        # Convert sets to sorted lists
        for group in structure.values():
            if 'param_values' in group:
                group['param_values'] = sorted(group['param_values'])
        
        return structure
    
    def _generate_class_file(self, subcategory: str, structure: Dict[str, Any], paths: Dict[str, Any]) -> str:
        """Generate the Python class file for a LOG subcategory."""
        class_name = to_class_name(subcategory)
        
        lines = []
        lines.append('"""')
        lines.append(f'FortiOS LOG API - {class_name}')
        lines.append('')
        lines.append(f'Log query endpoints for {subcategory} logs.')
        lines.append('')
        lines.append('Note: LOG endpoints are read-only (GET only) and return log data.')
        lines.append('They accept path parameters that are represented as nested classes.')
        lines.append('')
        lines.append('Example Usage:')
        
        # Add usage examples based on structure
        if 'event' in structure:
            lines.append(f'    >>> fgt.api.log.{subcategory}.event.vpn.get(rows=100)')
        if 'traffic' in structure:
            lines.append(f'    >>> fgt.api.log.{subcategory}.traffic.forward.get(rows=50)')
        
        lines.append('"""')
        lines.append('')
        lines.append('from __future__ import annotations')
        lines.append('')
        lines.append('from typing import TYPE_CHECKING, Any, Union')
        lines.append('')
        lines.append('if TYPE_CHECKING:')
        lines.append('    from collections.abc import Coroutine')
        lines.append('    from hfortix_core.http.interface import IHTTPClient')
        lines.append('')
        lines.append('')
        
        # Generate main class
        lines.append(f'class {class_name}:')
        lines.append(f'    """{class_name} log operations."""')
        lines.append('')
        lines.append('    def __init__(self, client: "IHTTPClient"):')
        lines.append(f'        """Initialize {class_name} endpoint."""')
        lines.append('        self._client = client')
        
        # Add attributes for each group
        for group_name, group_data in sorted(structure.items()):
            if group_name == 'direct':
                continue  # Handle direct endpoints separately
            
            attr_name = group_name
            group_class_name = f'{class_name}{to_class_name(group_name)}'
            lines.append(f'        self.{attr_name} = {group_class_name}(client)')
        
        lines.append('')
        
        # Add direct get() method if there's a root endpoint
        root_path = f"/{subcategory}"
        if root_path in paths:
            lines.append('    def get(self, **kwargs: Any) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:')
            lines.append(f'        """Get {subcategory} log information."""')
            lines.append(f'        return self._client.get("log", "/log{root_path}", **kwargs)')
            lines.append('')
        
        # Generate nested classes
        for group_name, group_data in sorted(structure.items()):
            if group_name == 'direct':
                continue
            
            self._add_group_class(lines, class_name, group_name, group_data, subcategory)
        
        return '\n'.join(lines)
    
    def _add_group_class(self, lines: List[str], parent_class: str, group_name: str, 
                         group_data: Dict[str, Any], subcategory: str):
        """Add a nested class for a parameter group."""
        group_class_name = f'{parent_class}{to_class_name(group_name)}'
        
        lines.append('')
        lines.append(f'class {group_class_name}:')
        
        if 'is_value' in group_data:
            # This is a concrete value class (e.g., Ips, AppCtrl)
            value = group_data['param_value']
            lines.append(f'    """{group_class_name} log operations (type={value})."""')
        elif 'param_values' in group_data:
            # This is a category class with sub-values (e.g., Event, Traffic)
            lines.append(f'    """{group_class_name} log operations."""')
        
        lines.append('')
        lines.append('    def __init__(self, client: "IHTTPClient"):')
        lines.append(f'        """Initialize {group_class_name}."""')
        lines.append('        self._client = client')
        
        # Add attributes for parameter values
        if 'param_values' in group_data:
            for value in group_data['param_values']:
                attr_name = value.replace('-', '_')
                value_class_name = f'{group_class_name}{to_class_name(value)}'
                lines.append(f'        self.{attr_name} = {value_class_name}(client, "{value}")')
        
        # Add attributes for sub-endpoints
        if 'endpoints' in group_data:
            for endpoint_name, path in group_data['endpoints'].items():
                if endpoint_name and endpoint_name != 'raw':
                    attr_name = endpoint_name.replace('-', '_')
                    endpoint_class_name = f'{group_class_name}{to_class_name(endpoint_name)}'
                    
                    if 'is_value' in group_data:
                        lines.append(f'        self.{attr_name} = {endpoint_class_name}(client, "{group_data["param_value"]}")')
                    else:
                        # This shouldn't happen in normal LOG API structure
                        pass
        
        lines.append('')
        
        # Add get() method if there's a direct endpoint for this group
        if 'is_value' in group_data:
            # Concrete value - has actual endpoints
            param_name = group_data['param_name']
            param_value = group_data['param_value']
            
            for endpoint_name, path_template in group_data['endpoints'].items():
                if not endpoint_name or endpoint_name == 'raw':
                    # This is the main GET endpoint
                    path = path_template.replace(f'{{{param_name}}}', param_value)
                    lines.append('    def get(self, **kwargs: Any) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:')
                    lines.append(f'        """Get {group_name} logs."""')
                    lines.append(f'        return self._client.get("log", "/log{path}", **kwargs)')
                    lines.append('')
                    break
        
        # Generate sub-classes for parameter values
        if 'param_values' in group_data:
            param_name = group_data['param_name']
            
            for value in group_data['param_values']:
                value_class_name = f'{group_class_name}{to_class_name(value)}'
                
                lines.append('')
                lines.append(f'class {value_class_name}:')
                lines.append(f'    """{group_name} logs for {value}."""')
                lines.append('')
                lines.append(f'    def __init__(self, client: "IHTTPClient", subtype: str):')
                lines.append(f'        """Initialize {value_class_name}."""')
                lines.append('        self._client = client')
                lines.append('        self._subtype = subtype')
                lines.append('')
                lines.append('    def get(self, **kwargs: Any) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:')
                lines.append(f'        """Get {value} {group_name} logs."""')
                
                # Find the path template
                for endpoint_name, path_template in group_data['endpoints'].items():
                    if not endpoint_name or endpoint_name == 'raw':
                        path = path_template.replace(f'{{{param_name}}}', f'{{self._subtype}}')
                        lines.append(f'        return self._client.get("log", f"/log{path}", **kwargs)')
                        break
                
                lines.append('')
        
        # Generate endpoint sub-classes (like Archive)
        if 'is_value' in group_data:
            param_value = group_data['param_value']
            param_name = group_data['param_name']
            
            for endpoint_name, path_template in group_data['endpoints'].items():
                if endpoint_name and endpoint_name != 'raw':
                    endpoint_class_name = f'{group_class_name}{to_class_name(endpoint_name)}'
                    path = path_template.replace(f'{{{param_name}}}', param_value)
                    
                    lines.append('')
                    lines.append(f'class {endpoint_class_name}:')
                    lines.append(f'    """{endpoint_name} operations for {group_name}."""')
                    lines.append('')
                    lines.append(f'    def __init__(self, client: "IHTTPClient", type_value: str):')
                    lines.append(f'        """Initialize {endpoint_class_name}."""')
                    lines.append('        self._client = client')
                    lines.append('        self._type = type_value')
                    lines.append('')
                    lines.append('    def get(self, **kwargs: Any) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:')
                    lines.append(f'        """Get {endpoint_name} for {{self._type}}."""')
                    lines.append(f'        return self._client.get("log", "/log{path}", **kwargs)')
                    lines.append('')
    
    def _generate_init(self, subcategories: List[str]):
        """Generate __init__.py for LOG category."""
        lines = [
            '"""LOG API - Auto-generated __init__ file."""',
            '',
            'from typing import TYPE_CHECKING',
            '',
        ]
        
        # Import all subcategory classes
        for subcat in sorted(subcategories):
            class_name = to_class_name(subcat)
            lines.append(f'from .{subcat} import {class_name}')
        
        lines.extend([
            '',
            'if TYPE_CHECKING:',
            '    from hfortix_core.http.interface import IHTTPClient',
            '',
            '',
            'class Log:',
            '    """Container for LOG endpoints."""',
            '',
            '    def __init__(self, client: "IHTTPClient"):',
            '        """Initialize LOG category."""',
        ])
        
        # Add all subcategory attributes
        for subcat in sorted(subcategories):
            class_name = to_class_name(subcat)
            lines.append(f'        self.{subcat} = {class_name}(client)')
        
        lines.append('')
        
        init_file = self.log_dir / "__init__.py"
        init_file.write_text('\n'.join(lines))
        print(f"  ✅ Generated {init_file}")
    
    def _generate_init_pyi(self, subcategories: List[str]):
        """Generate __init__.pyi stub file for LOG category."""
        lines = [
            '"""Type stubs for LOG category."""',
            '',
            'from typing import TYPE_CHECKING',
            '',
        ]
        
        # Import all subcategory classes
        for subcat in sorted(subcategories):
            class_name = to_class_name(subcat)
            lines.append(f'from .{subcat} import {class_name} as {class_name}')
        
        lines.extend([
            '',
            'if TYPE_CHECKING:',
            '    from hfortix_core.http.interface import IHTTPClient',
            '',
            '',
            'class Log:',
            '    """Container for LOG endpoints."""',
            '',
        ])
        
        # Add all subcategory attributes with type hints
        for subcat in sorted(subcategories):
            class_name = to_class_name(subcat)
            lines.append(f'    {subcat}: {class_name}')
        
        lines.extend([
            '',
            '    def __init__(self, client: IHTTPClient) -> None: ...',
            '',
        ])
        
        init_pyi_file = self.log_dir / "__init__.pyi"
        init_pyi_file.write_text('\n'.join(lines))
        print(f"  ✅ Generated {init_pyi_file}")
    
    def _generate_pyi_stubs(self, subcategories: List[str]):
        """Generate .pyi stub files for each LOG subcategory."""
        for subcat in sorted(subcategories):
            py_file = self.log_dir / f"{subcat}.py"
            pyi_file = self.log_dir / f"{subcat}.pyi"
            
            if not py_file.exists():
                print(f"  ⚠️  Skipping {subcat}.pyi - source file not found")
                continue
            
            # Read the .py file to extract class structure
            content = py_file.read_text()
            
            # Generate stub with same structure but type hints only
            lines = [
                '"""Type stubs for LOG endpoint."""',
                '',
                'from __future__ import annotations',
                '',
                'from typing import TYPE_CHECKING, Any',
                '',
                'if TYPE_CHECKING:',
                '    from hfortix_core.http.interface import IHTTPClient',
                '',
                '',
            ]
            
            # Extract class definitions and their structure
            import re
            
            # Find all class definitions
            class_pattern = re.compile(r'^class (\w+):$', re.MULTILINE)
            classes = class_pattern.findall(content)
            
            # For each class, extract its __init__ attributes and methods
            for class_name in classes:
                # Find the class block
                class_start = content.find(f'class {class_name}:')
                if class_start == -1:
                    continue
                
                # Find next class or end of file
                next_class = len(content)
                for other_class in classes:
                    if other_class != class_name:
                        pos = content.find(f'\nclass {other_class}:', class_start + 1)
                        if pos != -1 and pos < next_class:
                            next_class = pos
                
                class_block = content[class_start:next_class]
                
                # Write class stub
                lines.append(f'class {class_name}:')
                lines.append(f'    """Type stub for {class_name}."""')
                lines.append('')
                
                # Extract attributes from __init__ method (self.attr = ...)
                attr_pattern = re.compile(r'self\.([a-z_][a-z0-9_]*)\s*=\s*(\w+)\(', re.MULTILINE)
                attributes = []
                for match in attr_pattern.finditer(class_block):
                    attr_name = match.group(1)
                    attr_class = match.group(2)
                    # Skip _client and _type etc (private attributes)
                    if not attr_name.startswith('_'):
                        attributes.append((attr_name, attr_class))
                
                # Add attributes with type hints
                for attr_name, attr_class in attributes:
                    lines.append(f'    {attr_name}: {attr_class}')
                
                if attributes:
                    lines.append('')
                
                # Add __init__
                lines.append('    def __init__(self, client: IHTTPClient) -> None: ...')
                
                # Extract method definitions (get, post, put, delete)
                # Use simpler pattern since signatures can span multiple lines
                method_pattern = re.compile(r'def (get|post|put|delete)\(', re.MULTILINE)
                methods = set(method_pattern.findall(class_block))
                
                # Add methods
                for method in sorted(methods):
                    lines.append(f'    def {method}(self, **kwargs: Any) -> dict[str, Any]: ...')
                
                lines.append('')
            
            pyi_file.write_text('\n'.join(lines))
            print(f"  ✅ Generated {pyi_file}")
    
    def _generate_tests(self, subcategories: List[str]):
        """Generate basic tests for LOG endpoints."""
        # Find the workspace root by going up from output_dir
        # output_dir is: packages/fortios/hfortix_fortios/api/v2
        workspace_root = self.output_dir.parent.parent.parent.parent.parent
        test_dir = workspace_root / ".tests" / "pytests" / "api" / "log"
        test_dir.mkdir(parents=True, exist_ok=True)
        
        # Clean up old test directories if they exist
        for item in test_dir.iterdir():
            if item.is_dir():
                import shutil
                shutil.rmtree(item)
                print(f"  🗑️  Removed old test dir {item.name}/")
        
        for subcat in sorted(subcategories):
            test_file = test_dir / f"test_{subcat}.py"
            
            lines = [
                '"""',
                f'Auto-generated tests for LOG {subcat} endpoint.',
                '',
                'These are basic smoke tests to verify:',
                '  1. Endpoint class can be imported',
                '  2. Nested classes exist',
                '  3. Basic structure is correct',
                '',
                'Note: These tests do NOT make actual API calls.',
                '      They only verify the generated code structure.',
                '"""',
                '',
                'import pytest',
                'from unittest.mock import Mock, MagicMock',
                '',
                f'from hfortix_fortios.api.v2.log.{subcat} import {to_class_name(subcat)}',
                '',
                '',
                f'class Test{to_class_name(subcat)}Structure:',
                f'    """Test {subcat} endpoint structure."""',
                '',
                '    @pytest.fixture',
                '    def mock_client(self):',
                '        """Create a mock HTTP client."""',
                '        client = Mock()',
                '        client.get = MagicMock(return_value={"status": "success"})',
                '        client.post = MagicMock(return_value={"status": "success"})',
                '        client.put = MagicMock(return_value={"status": "success"})',
                '        client.delete = MagicMock(return_value={"status": "success"})',
                '        return client',
                '',
                '    @pytest.fixture',
                f'    def {subcat}_endpoint(self, mock_client):',
                f'        """Create {subcat} endpoint instance."""',
                f'        return {to_class_name(subcat)}(mock_client)',
                '',
                f'    def test_import_{subcat}(self):',
                f'        """Test that {subcat} class can be imported."""',
                f'        from hfortix_fortios.api.v2.log.{subcat} import {to_class_name(subcat)}',
                f'        assert {to_class_name(subcat)} is not None',
                '',
                f'    def test_{subcat}_instantiation(self, {subcat}_endpoint):',
                '        """Test that endpoint can be instantiated."""',
                f'        assert {subcat}_endpoint is not None',
                f'        assert hasattr({subcat}_endpoint, "_client")',
                '',
                f'    def test_{subcat}_has_attributes(self, {subcat}_endpoint):',
                '        """Test that endpoint has expected nested attributes."""',
                '        # Get all attributes (excluding private/magic methods)',
                f'        attrs = [a for a in dir({subcat}_endpoint) if not a.startswith("_")]',
                '        ',
                '        # Should have at least some nested classes or methods',
                '        assert len(attrs) > 0, "Endpoint should have nested classes or methods"',
                '        ',
                '        # Print discovered structure for debugging',
                f'        print(f"\\nDiscovered {subcat} attributes: {{attrs}}")',
                '',
            ]
            
            test_file.write_text('\n'.join(lines))
            print(f"  ✅ Generated {test_file}")
    
    # Removed: _to_class_name - now using shared utils from utils.naming


if __name__ == "__main__":
    # Test the generator
    import sys
    from pathlib import Path
    
    base_dir = Path(__file__).parent.parent.parent.parent
    swagger_dir = base_dir / ".dev" / "generator" / "swagger"
    output_dir = base_dir / "packages" / "fortios" / "hfortix_fortios" / "api" / "v2"
    
    generator = LogEndpointGenerator(swagger_dir, output_dir)
    stats = generator.generate_all()
    
    print("\n" + "=" * 80)
    print("LOG Generation Summary:")
    print("=" * 80)
    for subcategory, count in sorted(stats.items()):
        print(f"  {subcategory:20} : {count:3} endpoints")
    print("=" * 80)
