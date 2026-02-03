#!/usr/bin/env python3
"""
FortiOS API Code Generator

Main orchestrator that uses existing schemas to generate code.
Designed to be regenerable for any FortiOS version.

Supported Categories:
    - cmdb:    Configuration endpoints (full CRUD with schemas)
    - monitor: Monitoring endpoints (GET/POST, some have schemas)
    - service: Service endpoints (if schemas available)
    - log:     Log endpoints with path parameters (uses specialized generator)

Usage:
    python generate.py                                     # Auto-detect latest, generate all
    python generate.py --version 7.6.5                     # Specific version, all categories
    python generate.py --category cmdb                     # Auto-detect latest, one category
    python generate.py --endpoint cmdb.firewall.policy --version 7.6.5
    python generate.py --all --version 7.6.5
    python generate.py --list-versions                     # Show available versions
    
Note: Schemas must exist in /schema/{version}/ directory
"""

import argparse
import json
import sys
import time
from pathlib import Path
from collections.abc import Sequence

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from schema_management.schema_parser import SchemaParser
from schema_management.swagger_parser import SwaggerParser
from generators.endpoint_generator import EndpointGenerator
from generators.validator_generator import ValidatorGenerator
from generators.pyi_generator import PYIGenerator
from generators.model_generator import ModelGenerator
from generators.log_generator import LogEndpointGenerator
from generators.regenerate_init_files import regenerate_category_init
from helpers.generate_tests import TestGenerator
from helpers.relationship_analyzer import RelationshipAnalyzer


def get_available_versions(schema_dir: Path) -> list[str]:
    """
    Get list of available FortiOS versions from schema directory.
    
    Args:
        schema_dir: Base schema directory
        
    Returns:
        Sorted list of version strings (newest first)
    """
    if not schema_dir.exists():
        return []
    
    versions = []
    for item in schema_dir.iterdir():
        if item.is_dir() and not item.name.startswith('.'):
            # Valid version format: X.Y or X.Y.Z
            parts = item.name.split('.')
            if len(parts) in (2, 3) and all(p.isdigit() for p in parts):
                versions.append(item.name)
    
    # Sort by version tuple (newest first)
    versions.sort(key=lambda v: tuple(map(int, v.split('.'))), reverse=True)
    return versions


def get_latest_version(schema_dir: Path) -> str | None:
    """
    Auto-detect latest FortiOS version from schema directory.
    
    Args:
        schema_dir: Base schema directory
        
    Returns:
        Latest version string or None if no versions found
    """
    versions = get_available_versions(schema_dir)
    return versions[0] if versions else None


class CodeGenerator:
    """Main code generator orchestrator - Uses existing schemas only."""
    
    def __init__(
        self,
        fortios_version: str,
        output_dir: Path,
        template_dir: Path,
        schema_dir: Path,
        swagger_docs_dir: Path | None = None,
        stubs_dir: Path | None = None,
    ):
        """
        Initialize code generator.
        
        Args:
            fortios_version: FortiOS version (e.g., "7.6.5") - must match existing schema directory
            output_dir: Output directory for generated code
            template_dir: Template directory
            schema_dir: Schema storage directory (must exist with schemas)
            swagger_docs_dir: Swagger documentation directory (optional, for LOG category)
            stubs_dir: Separate directory for .pyi stub files (optional)
        """
        self.schema_dir = schema_dir / fortios_version
        if not self.schema_dir.exists():
            raise ValueError(
                f"Schema directory not found: {self.schema_dir}\n"
                f"Available versions: {[d.name for d in schema_dir.iterdir() if d.is_dir()]}"
            )
        self.endpoint_gen = EndpointGenerator(template_dir)
        self.validator_gen = ValidatorGenerator(template_dir)
        self.pyi_gen = PYIGenerator(template_dir, output_dir, stubs_dir=stubs_dir)
        self.model_gen = ModelGenerator(template_dir)
        self.log_gen = LogEndpointGenerator(
            swagger_docs_dir=swagger_docs_dir or Path(__file__).parent / "schema_management" / "swagger",
            output_dir=output_dir,  # Don't add /log here, generator handles it
            stubs_dir=stubs_dir  # Pass stubs_dir for .pyi file generation
        )
        self.test_gen = TestGenerator(template_dir)
        self.output_dir = output_dir
        self.stubs_dir = stubs_dir
        self._py_typed_created = False  # Track if we've created the marker file
    
    def _regenerate_category_inits(self):
        """Regenerate __init__.py files for all categories (cmdb, monitor, service) after generation."""
        
        # Use the same logic as regenerate_init_files.py to handle wrappers correctly
        def process_subdirectories(parent_dir: Path, base: Path, skip_set: set):
            """Recursively process subdirectories, skipping wrapper subdirectories."""
            subdirs = [d for d in parent_dir.iterdir() if d.is_dir() and not d.name.startswith("_")]
            for subdir in subdirs:
                # CRITICAL: Skip wrapper subdirectories entirely - don't regenerate OR recurse
                if subdir.name in skip_set:
                    continue
                
                # This is NOT a wrapper, so regenerate its __init__.py normally
                wrapper_subdirs_child = regenerate_category_init(subdir, base) or set()
                
                # Merge child wrapper subdirs with parent skip set
                combined_skip_set = skip_set | wrapper_subdirs_child
                process_subdirectories(subdir, base, combined_skip_set)  # Recurse with combined skip set
        
        # Regenerate for main categories
        categories = ['cmdb', 'monitor', 'service']
        
        total_categories = 0
        for cat in categories:
            category_dir = self.output_dir / cat
            if not category_dir.exists():
                continue
            
            # Find all category directories
            category_subdirs = [d for d in category_dir.iterdir() if d.is_dir() and not d.name.startswith("_")]
            
            # First, regenerate the top-level category __init__.py (cmdb, monitor, service)
            regenerate_category_init(category_dir, self.output_dir)
            
            for subdir in sorted(category_subdirs):
                wrapper_subdirs = regenerate_category_init(subdir, category_dir) or set()
                
                # Process subdirectories recursively, skipping wrappers
                process_subdirectories(subdir, category_dir, wrapper_subdirs)
            
            total_categories += len(category_subdirs)
        
        if total_categories > 0:
            print(f"✅ Regenerated {total_categories} category __init__.py files (with wrapper support)")

    
    def _print_module_summary(self, results: list[tuple[Path, Path, Path | None]]):
        """
        Print a summary of generated endpoints with their module paths and available methods.
        
        Args:
            results: List of (endpoint_file, validator_file, test_file) tuples (test_file can be None)
        """
        if not results:
            return
        
        print(f"\n{'='*80}")
        print("📋 GENERATED ENDPOINTS SUMMARY")
        print(f"{'='*80}\n")
        
        # Group by category
        from collections import defaultdict
        by_category = defaultdict(list)
        
        for endpoint_file, validator_file, test_file in results:
            # Extract module path from file
            # e.g., packages/fortios/hfortix_fortios/api/v2/cmdb/firewall/policy.py
            # -> fgt.api.cmdb.firewall.policy
            rel_path = endpoint_file.relative_to(self.output_dir)
            parts = rel_path.with_suffix('').parts
            
            # Build module path
            module_path = f"fgt.api.{'.'.join(parts)}"
            
            # Get category (first part)
            category = parts[0] if parts else "unknown"
            
            by_category[category].append(module_path)
        
        # Print summary by category
        for category in sorted(by_category.keys()):
            endpoints = sorted(by_category[category])
            print(f"📁 {category.upper()} ({len(endpoints)} endpoints)")
            print(f"{'-'*80}")
            
            for module_path in endpoints:
                print(f"\n  🐍 {module_path}")
                print(f"     Methods:")
                for method in ['get()', 'post()', 'put()', 'delete()', 'exists()', 'set()']:
                    print(f"       • {module_path}.{method}")
            
            print()  # Blank line between categories
        
        print(f"{'='*80}")
        print(f"✅ Total: {len(results)} endpoints generated")
        print(f"{'='*80}\n")
    
    def _generate_subcategory_stubs(self, category_dir: Path):
        """Generate __init__.pyi stubs for all subcategories recursively."""
        import re
        
        # Process all subdirectories (but skip _helpers, __pycache__, etc.)
        subdirs = [
            d for d in category_dir.iterdir()
            if d.is_dir() and not d.name.startswith('_')
        ]
        
        for subdir in subdirs:
            init_py = subdir / '__init__.py'
            
            # Determine where to write .pyi file (inline or stubs package)
            if self.stubs_dir:
                rel_path = subdir.relative_to(self.output_dir)
                init_pyi = self.stubs_dir / rel_path / '__init__.pyi'
            else:
                init_pyi = subdir / '__init__.pyi'
            
            if not init_py.exists():
                continue
            
            # Read __init__.py to extract info
            content = init_py.read_text()
            
            # Extract class name
            class_match = re.search(r'class (\w+):', content)
            if not class_match:
                continue
            
            class_name = class_match.group(1)
            
            # Parse all imports
            endpoint_imports = []  # [(module, class_name)]
            package_imports = []   # [package_name]
            
            # Find "from .module import Class" style imports
            direct_imports = re.findall(r'from \.(\w+) import (\w+)', content)
            for module_name, class_name_import in direct_imports:
                endpoint_imports.append((module_name, class_name_import))
            
            # Find "from . import package" style imports
            package_pattern = re.findall(r'from \. import (\w+)', content)
            package_imports.extend(package_pattern)
            
            # Extract attribute assignments (self.attr = ...)
            attr_pattern = re.compile(r'(?:self\.(\w+)|setattr\(self, [\'"](\w+)[\'"]\s*,)\s*=?\s*(?:(\w+)\.)?(\w+)\(', re.MULTILINE)
            attributes = []
            for match in attr_pattern.finditer(content):
                attr_name = match.group(1) or match.group(2)  # Handle both self.x and setattr
                namespace = match.group(3)  # Could be a module namespace
                attr_class = match.group(4)
                if attr_name and attr_class:
                    attributes.append((attr_name, attr_class, namespace))
            
            # Generate .pyi stub
            lines = [
                f'"""Type stubs for {subdir.name.upper()} category."""',
                '',
                'from __future__ import annotations',
                '',
                'from typing import TYPE_CHECKING',
                '',
                'if TYPE_CHECKING:',
                '    from hfortix_core.http.interface import IHTTPClient',
            ]
            
            # Import endpoint classes
            for module_name, class_name_import in sorted(set(endpoint_imports)):
                lines.append(f'    from .{module_name} import {class_name_import}')
            
            # Import package classes from subcategories (not just the module)
            for pkg in sorted(set(package_imports)):
                pkg_class = ''.join(p.capitalize() for p in pkg.replace('-', '_').split('_'))
                lines.append(f'    from .{pkg} import {pkg_class}')
            
            lines.extend([
                '',
                '',
                f'class {class_name}:',
                f'    """Type stub for {class_name}."""',
                '',
            ])
            
            # Add attributes with proper types (use classes directly, not module.Class)
            for attr_name, attr_class, namespace in attributes:
                # Always use the class name directly for proper autocomplete
                lines.append(f'    {attr_name}: {attr_class}')
            
            lines.extend([
                '',
                '    def __init__(self, client: IHTTPClient) -> None: ...',
                '',
            ])
            
            init_pyi.write_text('\n'.join(lines))
            print(f"  ✅ Generated {subdir.relative_to(self.output_dir)}/__init__.pyi")
            
            # Recurse into subdirectories
            self._generate_subcategory_stubs(subdir)
    
    def _generate_toplevel_stubs(self):
        """Generate __init__.pyi stubs for category-level and v2-level."""
        # Generate category-level __init__.pyi files (cmdb, monitor, service)
        # Note: LOG category is handled by log_generator
        for category in ['cmdb', 'monitor', 'service']:
            category_dir = self.output_dir / category
            if not category_dir.exists():
                continue
            
            init_py = category_dir / '__init__.py'
            
            # Determine where to write .pyi file (inline or stubs package)
            if self.stubs_dir:
                init_pyi = self.stubs_dir / category / '__init__.pyi'
            else:
                init_pyi = category_dir / '__init__.pyi'
            
            if not init_py.exists():
                continue
            
            # Read __init__.py to extract subcategories
            content = init_py.read_text()
            
            # Extract imports and class attributes
            import re
            
            # Try multi-line import first (CMDB style: from . import (subcat1, subcat2, ...))
            from_imports = re.findall(r'from \. import \(([^)]+)\)', content, re.DOTALL)
            if from_imports:
                # Multi-line import
                subcategories = [
                    s.strip().rstrip(',') 
                    for s in from_imports[0].split('\n') 
                    if s.strip() and not s.strip().startswith('#')
                ]
            else:
                # Single-line imports (Monitor style: from .azure import Azure)
                direct_imports = re.findall(r'from \.(\w+) import (\w+)', content)
                subcategories = [module_name for module_name, _ in direct_imports]
            
            # Extract class name
            class_match = re.search(r'class (\w+):', content)
            if not class_match:
                continue
            
            class_name = class_match.group(1)
            
            # Extract attribute assignments (self.subcategory = ...)
            # Pattern matches: self.firewall = firewall.Firewall(client)
            # Captures: attr_name='firewall', module='firewall', class='Firewall'
            attr_pattern = re.compile(r'self\.(\w+)\s*=\s*(\w+)\.(\w+)\(', re.MULTILINE)
            attributes = []
            for match in attr_pattern.finditer(content):
                attr_name = match.group(1)
                module_name = match.group(2)
                attr_class = match.group(3)
                attributes.append((attr_name, module_name, attr_class))
            
            # Generate .pyi stub
            lines = [
                f'"""Type stubs for {category.upper()} category."""',
                '',
                'from __future__ import annotations',
                '',
                'from typing import TYPE_CHECKING',
                '',
            ]
            
            # Build proper imports based on actual __init__.py
            # Need to distinguish between:
            # 1. Subcategory packages (from . import subcat) - these are for nested categories
            # 2. Endpoint classes (from .module import Class) - these are actual endpoints
            
            # Parse all imports more carefully
            endpoint_imports = []  # [(module, class_name)]
            package_imports = []   # [package_name]
            
            # Find "from .module import Class" style imports
            direct_imports = re.findall(r'from \.(\w+) import (\w+)', content)
            for module_name, class_name_import in direct_imports:
                endpoint_imports.append((module_name, class_name_import))
            
            # Find "from . import package" style imports
            package_pattern = re.findall(r'from \. import (\w+)', content)
            package_imports.extend(package_pattern)
            
            lines.append('')
            lines.append('if TYPE_CHECKING:')
            lines.append('    from hfortix_core.http.interface import IHTTPClient')
            
            # Import endpoint classes
            for module_name, class_name_import in sorted(set(endpoint_imports)):
                lines.append(f'    from .{module_name} import {class_name_import}')
            
            # Import packages (subcategories)
            for pkg in sorted(set(package_imports)):
                pkg_class = ''.join(p.capitalize() for p in pkg.replace('-', '_').split('_'))
                lines.append(f'    from . import {pkg}')
            
            lines.extend([
                '',
                '',
                f'class {class_name}:',
                f'    """Type stub for {class_name}."""',
                '',
            ])
            
            # Add attributes with proper types
            for attr_name, module_name, attr_class in attributes:
                # All attributes should use module.Class notation since they follow
                # the pattern: self.firewall = firewall.Firewall(client)
                lines.append(f'    {attr_name}: {module_name}.{attr_class}')
            
            lines.extend([
                '',
                '    def __init__(self, client: IHTTPClient) -> None: ...',
                '',
            ])
            
            init_pyi.write_text('\n'.join(lines))
            print(f"  ✅ Generated {category}/__init__.pyi")
            
            # Now generate stubs for all subcategories (like firewall, system, etc.)
            print(f"  📝 Generating subcategory stubs for {category}...")
            self._generate_subcategory_stubs(category_dir)
        
        # Generate v2-level __init__.pyi
        if self.stubs_dir:
            v2_init_pyi = self.stubs_dir / '__init__.pyi'
        else:
            v2_init_pyi = self.output_dir / '__init__.pyi'
            
        v2_lines = [
            '"""Type stubs for FortiOS API v2."""',
            '',
            'from .cmdb import CMDB as CMDB',
            'from .monitor import Monitor as Monitor',
            'from .service import Service as Service',
            'from .log import Log as Log',
            '',
            '__all__ = [',
            '    "CMDB",',
            '    "Monitor",',
            '    "Service",',
            '    "Log",',
            ']',
            '',
        ]
        v2_init_pyi.write_text('\n'.join(v2_lines))
        print(f"  ✅ Generated v2/__init__.pyi")
    
    def generate_endpoint(self, endpoint_path: str) -> tuple[Path, Path, Path]:
        """
        Generate code for a single endpoint.
        
        Args:
            endpoint_path: Endpoint path (e.g., "cmdb.firewall.policy")
            
        Returns:
            Tuple of (endpoint_file_path, validator_file_path, test_file_path)
        """
        print(f"📝 Generating {endpoint_path}...")
        
        # Parse endpoint path 
        # Format can be: "cmdb.firewall.policy" OR "cmdb.firewall.ipmacbinding/setting"
        # We need to extract category (first part) and keep the rest preserving . and /
        parts = endpoint_path.split(".", 1)  # Split only on first dot
        category = parts[0]
        
        if len(parts) > 1:
            # Keep the path as-is, preserving both . and / 
            # e.g., "firewall.ipmacbinding/setting" stays as "firewall.ipmacbinding/setting"
            # e.g., "firewall.policy" becomes "firewall/policy"
            path_part = parts[1]
            
            # Only convert dots to slashes if there's no slash already
            if "/" in path_part:
                # Path has mixed format, keep as-is
                path = path_part
            else:
                # Path has only dots, convert to slashes
                path = path_part.replace(".", "/")
        else:
            path = ""
        
        # Find schema file from existing schemas
        print(f"  � Loading schema from disk...")
        
        # Try different filename formats
        # 1. dot notation: cmdb/firewall.policy.json
        # 2. slash notation: cmdb/firewall/policy.json
        schema_candidates = [
            self.schema_dir / category / f"{path.replace('/', '.')}.json",
            self.schema_dir / category / f"{path}.json",
        ]
        
        schema_file = None
        for candidate in schema_candidates:
            if candidate.exists():
                schema_file = candidate
                break
        
        if not schema_file:
            raise RuntimeError(
                f"Schema not found for {endpoint_path}\n"
                f"Tried: {[str(c) for c in schema_candidates]}"
            )
        
        # Load and parse schema
        print(f"  🔍 Parsing schema...")
        with open(schema_file) as f:
            schema_json = json.load(f)
        schema = SchemaParser.parse(schema_json, str(schema_file))
        
        # Generate endpoint class
        print(f"  ✨ Generating endpoint class...")
        endpoint_file = self.endpoint_gen.generate(schema, self.output_dir)
        print(f"     ✅ {endpoint_file}")
        
        # Generate endpoint .pyi stub
        print(f"  ✨ Generating endpoint stub...")
        if self.stubs_dir:
            # Calculate stub path relative to stubs directory
            # endpoint_file is like: .../fortios/hfortix_fortios/api/v2/cmdb/system/admin.py
            # We want: .../fortios-stubs/hfortix_fortios-stubs/api/v2/cmdb/system/admin.pyi
            rel_path = endpoint_file.relative_to(self.output_dir)
            endpoint_pyi = self.stubs_dir / rel_path.with_suffix('.pyi')
        else:
            endpoint_pyi = endpoint_file.with_suffix('.pyi')
        self.pyi_gen.generate_endpoint_stub(schema, endpoint_pyi)
        print(f"     ✅ {endpoint_pyi}")
        
        # Generate validator
        print(f"  ✨ Generating validator...")
        validator_file = self.validator_gen.generate(schema, self.output_dir)
        print(f"     ✅ {validator_file}")
        
        # Generate validator .pyi stub
        print(f"  ✨ Generating validator stub...")
        if self.stubs_dir:
            # Same calculation for validator stub
            rel_path = validator_file.relative_to(self.output_dir)
            validator_pyi = self.stubs_dir / rel_path.with_suffix('.pyi')
        else:
            validator_pyi = validator_file.with_suffix('.pyi')
        # Extract enum constants from validator generator and convert to dict format
        enum_constants_list = self.validator_gen._extract_enum_constants(schema)
        enum_constants = {
            item["constant_name"]: item["options"]
            for item in enum_constants_list
        }
        self.pyi_gen.generate_validator_stub(schema, enum_constants, validator_pyi)
        print(f"     ✅ {validator_pyi}")
        
        # Generate Pydantic model
        print(f"  ✨ Generating Pydantic model...")
        # Models go in: output_dir/../models/cmdb/firewall/policy.py
        models_dir = self.output_dir.parent / "models"
        model_file = self.model_gen.generate(schema, models_dir)
        print(f"     ✅ {model_file}")
        
        # Generate test
        print(f"  ✨ Generating test...")
        # Pass workspace root (6 levels up from api/v2 dir: api -> hfortix_fortios -> src -> fortios -> packages -> root)
        workspace_root = self.output_dir.parent.parent.parent.parent.parent.parent
        test_file = self.test_gen.generate(schema, workspace_root)
        print(f"     ✅ {test_file}")
        
        # Create py.typed marker on first generation
        if not self._py_typed_created:
            print(f"  ✨ Creating py.typed marker...")
            self.pyi_gen.create_py_typed_marker()
            self._py_typed_created = True
            print(f"     ✅ py.typed marker created")
        
        return endpoint_file, validator_file, test_file  # type: ignore
    
    def generate_category(self, category: str) -> list[tuple[Path, Path]]:
        """
        Generate code for all endpoints in a category.
        
        Args:
            category: Category name (cmdb, monitor, log, service)
            
        Returns:
            List of generated file tuples
        """
        print(f"📁 Generating category: {category}")
        
        # LOG category: Use improved specialized generator
        if category.lower() == "log":
            print(f"  ℹ️  Using improved LOG generator with modern structure")
            stats = self.log_gen.generate_all()
            print(f"✅ Generated LOG category with {sum(stats.values())} total endpoints")
            # Generate top-level __init__.pyi stubs
            print(f"\n📝 Generating top-level __init__.pyi stubs...")
            self._generate_toplevel_stubs()
            return []
        
        # Use existing local schemas only
        print(f"  📂 Using existing local schemas...")
        category_dir = self.schema_dir / category
        if not category_dir.exists():
            raise ValueError(
                f"No schemas found in {category_dir}\n"
                f"Schema directory must contain {category}/ subdirectory"
            )
        
        # Find all existing schema files
        schema_files = list(category_dir.rglob('*.json'))
        
        # Filter out build artifact files at category root level only
        # (index.json, metadata.json in category root are NOT API schemas)
        # Note: subdirectory files like monitor/ips/metadata.json ARE valid schemas
        schema_files = [
            f for f in schema_files 
            if not (f.parent == category_dir and f.name in ('index.json', 'metadata.json', '.schema_index.json', '.download_metadata.json'))
        ]
        
        print(f"  📋 Found {len(schema_files)} existing schemas")

        # Analyze relationships for CMDB category (to get reverse dependencies)
        reverse_deps_map = {}
        if category.lower() == "cmdb":
            print(f"  🔗 Analyzing endpoint relationships...")
            analyzer = RelationshipAnalyzer(self.schema_dir)
            reverse_deps_map = analyzer.analyze_all_schemas()
            print(f"     ✅ Found reverse dependencies for {len(reverse_deps_map)} endpoints")

        # Pre-scan schemas to identify which base endpoints will have subdirectories
        # This prevents creating both "override.py" and "override_base.py" files
        endpoints_with_subdirs = set()
        all_endpoints = set()
        
        for schema_file in schema_files:
            # Get the relative path from category directory
            rel_path = schema_file.relative_to(self.schema_dir / category)
            filename = rel_path.stem  # e.g., "firewall.policy" or "wifi.rogue_ap.clear_all"
            
            # Add to all endpoints set
            all_endpoints.add(filename)
            
            # Check if this filename contains more dots than just category separator
            # Examples:
            #   "firewall.policy" -> 1 dot, is base endpoint
            #   "firewall.policy.reset" -> 2 dots, has action, base is "firewall.policy"
            #   "wifi.rogue_ap.clear_all" -> 2 dots, has action, base is "wifi.rogue_ap"
            parts = filename.split('.')
            if len(parts) > 1:  # Has at least one dot
                # Everything except the last part is the base endpoint
                base_endpoint = '.'.join(parts[:-1])
                # This base endpoint will have a subdirectory
                endpoints_with_subdirs.add(base_endpoint)
        
        # Generate code for each schema
        results = []
        for schema_file in schema_files:
            # Parse endpoint path from file
            # e.g., schema/7.6.5/cmdb/firewall.policy.json -> cmdb.firewall.policy
            rel_path = Path(schema_file).relative_to(self.schema_dir)
            endpoint_path = str(rel_path.with_suffix("")).replace("/", ".")
            
            # Load and parse
            with open(schema_file) as f:
                schema_json = json.load(f)
            schema = SchemaParser.parse(schema_json, str(schema_file))
            
            # Check if this endpoint will have a subdirectory
            # Construct the endpoint identifier to check (e.g., "webfilter.override")
            rel_path = Path(schema_file).relative_to(self.schema_dir / category)
            endpoint_identifier = str(rel_path.with_suffix("")).replace("/", ".")
            will_have_subdir = endpoint_identifier in endpoints_with_subdirs
            
            # Generate
            print(f"  ✨ {endpoint_path}")
            endpoint_file = self.endpoint_gen.generate(schema, self.output_dir, will_have_subdir=will_have_subdir)
            
            # Generate endpoint .pyi stub (respect stubs_dir)
            if self.stubs_dir:
                rel_path = endpoint_file.relative_to(self.output_dir)
                endpoint_pyi = self.stubs_dir / rel_path.with_suffix('.pyi')
            else:
                endpoint_pyi = endpoint_file.with_suffix('.pyi')
            
            # Get reverse dependencies for this endpoint (if available)
            endpoint_full_path = schema.full_path if hasattr(schema, 'full_path') else None
            reverse_deps = reverse_deps_map.get(endpoint_full_path, []) if endpoint_full_path else []
            
            self.pyi_gen.generate_endpoint_stub(schema, endpoint_pyi, reverse_deps=reverse_deps)
            
            validator_file = self.validator_gen.generate(schema, self.output_dir)
            
            # Generate validator .pyi stub (respect stubs_dir)
            if self.stubs_dir:
                rel_path = validator_file.relative_to(self.output_dir)
                validator_pyi = self.stubs_dir / rel_path.with_suffix('.pyi')
            else:
                validator_pyi = validator_file.with_suffix('.pyi')
            enum_constants_list = self.validator_gen._extract_enum_constants(schema)
            enum_constants = {item["constant_name"]: item["options"] for item in enum_constants_list}
            self.pyi_gen.generate_validator_stub(schema, enum_constants, validator_pyi)
            
            # Generate Pydantic model
            models_dir = self.output_dir.parent / "models"
            model_file = self.model_gen.generate(schema, models_dir)
            
            workspace_root = self.output_dir.parent.parent.parent.parent.parent.parent
            test_file = self.test_gen.generate(schema, workspace_root)
            
            results.append((endpoint_file, validator_file, test_file))
        
        # Create py.typed marker after category generation
        if results and not self._py_typed_created:
            print(f"  ✨ Creating py.typed marker...")
            self.pyi_gen.create_py_typed_marker()
            self._py_typed_created = True
        
        # Generate category-level __init__.pyi files
        if results:
            self._generate_category_stubs(category, schema_files)
            # Generate top-level category __init__.pyi
            self._generate_toplevel_stubs()
        
        print(f"✅ Generated {len(results)} endpoints in {category}")
        return results
    
    def _generate_category_stubs(self, category: str, schema_files: Sequence[Path | str]) -> None:
        """
        Generate __init__.pyi stubs for all subcategories.
        
        Args:
            category: Main category (e.g., 'cmdb')
            schema_files: List of schema file paths
        """
        # Group endpoints by subcategory (e.g., firewall, system, etc.)
        from collections import defaultdict
        subcategories = defaultdict(list)
        
        for schema_file in schema_files:
            # Parse category path from schema file
            # schema/7.6.5/cmdb/firewall.address.json -> firewall
            rel_path = Path(schema_file).relative_to(self.schema_dir)
            parts = rel_path.parts
            
            if len(parts) >= 2:
                subcategory = parts[0]  # cmdb, monitor, etc.
                if len(parts) >= 3:
                    # Has subcategory (e.g., firewall, system)
                    subcategory_name = parts[1]
                    endpoint_name = parts[-1].replace('.json', '')
                    
                    # Convert endpoint name to class name
                    class_name = self._endpoint_to_class_name(endpoint_name)
                    
                    subcategories[subcategory_name].append({
                        'module_name': endpoint_name,
                        'class_name': class_name,
                    })
        
        # Generate __init__.pyi for each subcategory
        for subcategory_name, endpoints in subcategories.items():
            # Determine where to write .pyi file (inline or stubs package)
            if self.stubs_dir:
                output_path = self.stubs_dir / category / subcategory_name / '__init__.pyi'
            else:
                output_path = self.output_dir / category / subcategory_name / '__init__.pyi'
            
            self.pyi_gen.generate_category_init_stub(
                subcategory_name,
                endpoints,
                output_path
            )
            print(f"     ✅ {category}/{subcategory_name}/__init__.pyi ({len(endpoints)} endpoints)")
    
    @staticmethod
    def _endpoint_to_class_name(endpoint_name: str) -> str:
        """Convert endpoint name to class name (snake_case -> CamelCase)."""
        parts = endpoint_name.replace('-', '_').split('_')
        return ''.join(p.capitalize() for p in parts)
    
    def generate_from_file(self, file_path: Path, max_errors_display: int = 10) -> list[tuple[Path, Path, Path]]:
        """
        Generate code for endpoints listed in a file.
        
        Supports:
            - JSON file (.json): Uses endpoints_all.json format with flat_list
            - Text file (.txt): One endpoint per line (format: category.endpoint/path)
        
        Args:
            file_path: Path to endpoints file
            max_errors_display: Maximum number of errors to display (0 = all errors)
            
        Returns:
            List of generated file tuples
        """
        print(f"📋 Generating from file: {file_path}")
        
        # Generate LOG category first (uses special generator)
        print("\n📁 Generating LOG category...")
        log_stats = self.log_gen.generate_all()
        print(f"✅ Generated LOG category with {sum(log_stats.values())} total endpoints")
        
        endpoints = []
        
        if file_path.suffix == ".json":
            # Load JSON file
            with open(file_path) as f:
                data = json.load(f)
            
            # Extract endpoints from flat_list
            if "flat_list" in data:
                endpoints = [item["full_path"] for item in data["flat_list"]]
                print(f"  📊 Found {len(endpoints)} endpoints in JSON")
            else:
                print("❌ Error: JSON file must contain 'flat_list' key")
                print("   Use .dev/endpoints_all.json format")
                return []
        
        else:  # Text file
            # Try to detect category from filename (e.g., endpoints_cmdb.txt -> cmdb)
            detected_category = None
            if file_path.stem.startswith("endpoints_"):
                category_part = file_path.stem[len("endpoints_"):]
                if category_part in ["cmdb", "monitor", "log", "service"]:
                    detected_category = category_part
                    print(f"  🔍 Detected category from filename: {detected_category}")
            
            with open(file_path) as f:
                for line in f:
                    line = line.strip()
                    # Skip comments and empty lines
                    if line and not line.startswith("#"):
                        # If endpoint doesn't have category prefix and we detected one, add it
                        if detected_category:
                            # Check if line already starts with the category
                            if not line.startswith(f"{detected_category}."):
                                # Add category prefix
                                # Keep the line format as-is (with / or .)
                                endpoint = f"{detected_category}.{line}"
                            else:
                                endpoint = line
                        else:
                            endpoint = line
                        
                        endpoints.append(endpoint)
            print(f"  📊 Found {len(endpoints)} endpoints in text file")
        
        # Filter out log endpoints - they're handled by log_generator
        original_count = len(endpoints)
        endpoints = [ep for ep in endpoints if not ep.startswith("log.")]
        log_count = original_count - len(endpoints)
        
        if log_count > 0:
            print(f"  ℹ️  Filtered out {log_count} log endpoints (handled by log_generator)")
        
        # Generate each endpoint
        results = []
        failed = []
        
        for i, endpoint in enumerate(endpoints, 1):
            try:
                print(f"\n  [{i}/{len(endpoints)}] Generating: {endpoint}")
                endpoint_file, validator_file, test_file = self.generate_endpoint(endpoint)
                results.append((endpoint_file, validator_file, test_file))
                
                # Small delay to avoid overwhelming the API
                time.sleep(0.2)  # 200ms delay
                
            except Exception as e:
                print(f"    ❌ Failed: {e}")
                failed.append((endpoint, str(e)))
        
        # Summary
        print(f"\n{'='*80}")
        print(f"✅ Successfully generated: {len(results)}/{len(endpoints)} endpoints")
        
        if failed:
            print(f"❌ Failed: {len(failed)} endpoints")
            print("\nFailed endpoints:")
            
            # Determine how many errors to show
            if max_errors_display == 0:
                # Show all errors
                errors_to_show = failed
            else:
                # Show limited number of errors
                errors_to_show = failed[:max_errors_display]
            
            for endpoint, error in errors_to_show:
                print(f"  - {endpoint}: {error}")
            
            if max_errors_display > 0 and len(failed) > max_errors_display:
                print(f"  ... and {len(failed) - max_errors_display} more")
        
        # Regenerate __init__.py files for all affected categories
        print(f"\n🔄 Regenerating __init__.py files...")
        self._regenerate_category_inits()
        
        # Generate top-level __init__.pyi stubs
        print(f"\n📝 Generating top-level __init__.pyi stubs...")
        self._generate_toplevel_stubs()
        
        # Print module path summary
        if results:
            self._print_module_summary(results)
        
        return results
    
    def generate_all(self) -> list[tuple[Path, Path]]:
        """
        Generate code for all endpoints.
        
        Returns:
            List of generated file tuples
        """
        print("🚀 Generating ALL endpoints...")
        
        # Generate LOG category first (uses special generator)
        print("\n📁 Generating LOG category...")
        log_stats = self.log_gen.generate_all()
        print(f"✅ Generated LOG category with {sum(log_stats.values())} total endpoints")
        
        # Use existing local schemas only
        schema_files = []
        print("\n  📂 Using existing local schemas...")
        for category in ["cmdb", "monitor", "service"]:
            category_dir = self.schema_dir / category
            if category_dir.exists():
                category_schemas = list(category_dir.rglob('*.json'))
                
                # Filter out build artifact files at category root level only
                # (index.json, metadata.json in category root are NOT API schemas)
                # Note: subdirectory files like monitor/ips/metadata.json ARE valid schemas
                category_schemas = [
                    f for f in category_schemas 
                    if not (f.parent == category_dir and f.name in ('index.json', 'metadata.json', '.schema_index.json', '.download_metadata.json'))
                ]
                
                schema_files.extend(category_schemas)
                print(f"  📋 Found {len(category_schemas)} schemas in {category}")
            else:
                print(f"  ⏭️  Skipping {category} (directory not found)")
        
        print(f"\n📊 Total: {len(schema_files)} schemas to generate from")
        if not schema_files:
            raise ValueError("No schemas found! Check that schema directory contains cmdb/monitor/service subdirectories")

        # Pre-scan schemas to identify which base endpoints will have subdirectories
        # This prevents creating both "override.py" and "override_base.py" files
        endpoints_with_subdirs = set()
        all_endpoints = set()
        
        for schema_file in schema_files:
            # Get the relative path from schema directory (includes category)
            rel_path = Path(schema_file).relative_to(self.schema_dir)
            # Extract category (first part)
            category = rel_path.parts[0]
            # Get remaining path relative to category
            rel_to_category = Path(schema_file).relative_to(self.schema_dir / category)
            filename = rel_to_category.stem  # e.g., "firewall.policy" or "wifi.rogue_ap.clear_all"
            
            # Add to all endpoints set (with category prefix for uniqueness)
            endpoint_identifier = f"{category}.{filename}"
            all_endpoints.add(endpoint_identifier)
            
            # Check if this filename contains more dots than just category separator
            # Examples:
            #   "firewall.policy" -> 1 dot, is base endpoint
            #   "firewall.policy.reset" -> 2 dots, has action, base is "firewall.policy"
            #   "wifi.rogue_ap.clear_all" -> 2 dots, has action, base is "wifi.rogue_ap"
            parts = filename.split('.')
            if len(parts) > 1:  # Has at least one dot
                # Everything except the last part is the base endpoint
                base_endpoint = '.'.join(parts[:-1])
                # Store with category prefix
                endpoints_with_subdirs.add(f"{category}.{base_endpoint}")
        
        print(f"  🔍 Detected {len(endpoints_with_subdirs)} base endpoints with sub-endpoints")

        # Generate code for each schema
        results = []
        for schema_file in schema_files:
            # Parse endpoint path from file
            # schema/7.6.5/cmdb/firewall.policy.json -> cmdb.firewall.policy
            rel_path = Path(schema_file).relative_to(self.schema_dir)
            endpoint_path = str(rel_path.with_suffix("")).replace("/", ".")
            
            # Load and parse
            with open(schema_file) as f:
                schema_json = json.load(f)
            schema = SchemaParser.parse(schema_json, str(schema_file))
            
            # Check if this endpoint will have a subdirectory
            will_have_subdir = endpoint_path in endpoints_with_subdirs
            
            # Generate endpoint class
            print(f"  ✨ {endpoint_path}")
            endpoint_file = self.endpoint_gen.generate(schema, self.output_dir, will_have_subdir=will_have_subdir)
            
            # Generate endpoint .pyi stub (respect stubs_dir)
            if self.stubs_dir:
                rel_path = endpoint_file.relative_to(self.output_dir)
                endpoint_pyi = self.stubs_dir / rel_path.with_suffix('.pyi')
            else:
                endpoint_pyi = endpoint_file.with_suffix('.pyi')
            self.pyi_gen.generate_endpoint_stub(schema, endpoint_pyi)
            
            # Generate validator
            validator_file = self.validator_gen.generate(schema, self.output_dir)
            
            # Generate validator .pyi stub (respect stubs_dir)
            if self.stubs_dir:
                rel_path = validator_file.relative_to(self.output_dir)
                validator_pyi = self.stubs_dir / rel_path.with_suffix('.pyi')
            else:
                validator_pyi = validator_file.with_suffix('.pyi')
            enum_constants_list = self.validator_gen._extract_enum_constants(schema)
            enum_constants = {
                item["constant_name"]: item["options"]
                for item in enum_constants_list
            }
            self.pyi_gen.generate_validator_stub(schema, enum_constants, validator_pyi)
            
            # Generate Pydantic model
            models_dir = self.output_dir.parent / "models"
            model_file = self.model_gen.generate(schema, models_dir)
            
            # Generate test
            workspace_root = self.output_dir.parent.parent.parent.parent.parent.parent
            test_file = self.test_gen.generate(schema, workspace_root)
            
            results.append((endpoint_file, validator_file))
        
        # Create py.typed marker
        if not self._py_typed_created:
            self.pyi_gen.create_py_typed_marker()
            self._py_typed_created = True
        
        # Regenerate __init__.py files for all categories
        print(f"\n📝 Regenerating __init__.py files...")
        self._regenerate_category_inits()
        
        # Generate top-level __init__.pyi stubs
        print(f"\n📝 Generating top-level __init__.pyi stubs...")
        self._generate_toplevel_stubs()
        
        print(f"✅ Generated {len(results)} total endpoints")
        return results


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Generate FortiOS API code from schemas",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Auto-detect latest version and generate all (DEFAULT)
  python generate.py
  
  # List available versions
  python generate.py --list-versions
  
  # Generate all with specific version
  python generate.py --version 7.6.5
  
  # Generate single category
  python generate.py --category cmdb
  
  # Generate single endpoint
  python generate.py --endpoint cmdb.firewall.policy --version 7.6.5
  
  # Generate from endpoint list (JSON or text file)
  python generate.py --from-file .dev/endpoints_all.json
        """,
    )
    
    # List versions option
    parser.add_argument(
        "--list-versions",
        action="store_true",
        help="List available FortiOS versions and exit",
    )
    
    # FortiOS version
    parser.add_argument(
        "--version",
        default=None,  # Will auto-detect if not specified
        help="FortiOS version (must match schema directory). Auto-detects latest if not specified.",
    )
    
    # Generation scope
    group = parser.add_mutually_exclusive_group(required=False)  # Not required anymore - defaults to --all
    group.add_argument(
        "--endpoint",
        help="Generate single endpoint (e.g., cmdb.firewall.policy)",
    )
    group.add_argument(
        "--category",
        help="Generate all endpoints in category (cmdb, monitor, log, service)",
    )
    group.add_argument(
        "--all",
        action="store_true",
        help="Generate all endpoints (default if no other option specified)",
    )
    group.add_argument(
        "--from-file",
        type=Path,
        help="Generate from endpoint list file (.txt or .json). Use .dev/endpoints_all.json or .dev/endpoints_master.txt",
    )
    
    # Paths
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).parent.parent.parent / "src" / "hfortix_fortios" / "api" / "v2",
        help="Output directory for generated code",
    )
    parser.add_argument(
        "--template-dir",
        type=Path,
        default=Path(__file__).parent / "templates",
        help="Template directory",
    )
    parser.add_argument(
        "--schema-dir",
        type=Path,
        default=Path(__file__).parent.parent / "schema",
        help="Schema storage directory (schema_dir/VERSION/ will be used based on --version)",
    )
    parser.add_argument(
        "--max-errors",
        type=int,
        default=10,
        help="Maximum number of errors to display at end (0 = show all errors, default: 10)",
    )
    
    args = parser.parse_args()
    
    # Handle --list-versions
    if args.list_versions:
        schema_dir = args.schema_dir
        versions = get_available_versions(schema_dir)
        if versions:
            print("Available FortiOS versions:")
            for version in versions:
                print(f"  - {version}")
            latest = versions[0]
            print(f"\nLatest: {latest}")
        else:
            print(f"No versions found in {schema_dir}")
        sys.exit(0)
    
    # Auto-detect version if not specified
    if args.version is None:
        args.version = get_latest_version(args.schema_dir)
        if args.version is None:
            print(f"❌ No FortiOS versions found in {args.schema_dir}")
            print("Run with --list-versions to see available versions")
            sys.exit(1)
        print(f"ℹ️  Auto-detected latest version: {args.version}")
    
    # Default to --all if no action specified
    if not any([args.endpoint, args.category, args.all, args.from_file]):
        args.all = True
        print("ℹ️  No action specified, defaulting to --all")
    
    # Determine Swagger docs directory (now in generator/schema_management/swagger/)
    base_dir = Path(__file__).parent
    swagger_docs_dir = base_dir / "schema_management" / "swagger"
    if not swagger_docs_dir.exists():
        swagger_docs_dir = None
        print("ℹ️  Swagger docs not found - will only use API schemas")
    
    # INLINE STUBS: Place .pyi files alongside .py files for better IDE support
    # Separate stubs package disabled - IDE autocomplete works better with inline stubs
    stubs_dir = None
    print("ℹ️  Using inline stubs - .pyi files will be placed alongside .py files for better IDE autocomplete")
    
    # Create generator
    generator = CodeGenerator(
        fortios_version=args.version,
        output_dir=args.output_dir,
        template_dir=args.template_dir,
        schema_dir=args.schema_dir,
        swagger_docs_dir=swagger_docs_dir,
        stubs_dir=stubs_dir,
    )
    
    # Generate
    try:
        if args.endpoint:
            generator.generate_endpoint(args.endpoint)
            generator._regenerate_category_inits()
        elif args.category:
            generator.generate_category(args.category)
            generator._regenerate_category_inits()
        elif args.all:
            generator.generate_all()
            # _regenerate_category_inits called inside generate_all()
        elif args.from_file:
            generator.generate_from_file(args.from_file, max_errors_display=args.max_errors)
            # _regenerate_category_inits called inside generate_from_file()
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    
    print("\n✨ Generation complete!")


if __name__ == "__main__":
    main()
