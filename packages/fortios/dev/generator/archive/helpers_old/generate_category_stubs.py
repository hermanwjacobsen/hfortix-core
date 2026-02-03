#!/usr/bin/env python3
"""
Generate __init__.pyi stub files for existing category directories.

Reads existing __init__.py files and creates corresponding .pyi stubs
for better IDE autocomplete and type checking.
"""

import re
from pathlib import Path
from datetime import datetime, timezone


def parse_init_py(init_file: Path) -> list[dict[str, str]]:
    """
    Parse __init__.py file to extract module and class imports.
    
    Args:
        init_file: Path to __init__.py
        
    Returns:
        List of dicts with 'module_name' and 'class_name'
    """
    endpoints = []
    
    with open(init_file) as f:
        for line in f:
            # Match: from .module_name import ClassName
            match = re.match(r'from\s+\.(\w+)\s+import\s+(\w+)', line.strip())
            if match:
                module_name = match.group(1)
                class_name = match.group(2)
                endpoints.append({
                    'module_name': module_name,
                    'class_name': class_name,
                })
    
    return endpoints


def generate_category_stub(category_name: str, endpoints: list[dict[str, str]]) -> str:
    """
    Generate __init__.pyi content.
    
    Args:
        category_name: Name of the category
        endpoints: List of endpoint dicts
        
    Returns:
        Content for __init__.pyi file
    """
    timestamp = datetime.now(timezone.utc).isoformat()
    
    lines = [
        '"""',
        f'Type stubs for {category_name} category.',
        '',
        'This file provides type hints for IDE autocomplete and type checking.',
        '',
        'Auto-generated - do not edit manually.',
        f'Last generated: {timestamp}',
        '"""',
        '',
        '# Import all endpoint classes',
    ]
    
    # Sort endpoints by module name
    sorted_endpoints = sorted(endpoints, key=lambda x: x['module_name'])
    
    # Add imports
    for endpoint in sorted_endpoints:
        lines.append(
            f"from .{endpoint['module_name']} import {endpoint['class_name']} as {endpoint['class_name']}"
        )
    
    lines.extend(['', '__all__ = ['])
    
    # Add __all__ entries
    for endpoint in sorted_endpoints:
        lines.append(f'    "{endpoint["class_name"]}",')
    
    lines.append(']')
    
    return '\n'.join(lines) + '\n'


def main():
    """Generate __init__.pyi stubs for all categories."""
    
    # Base directory
    base_dir = Path(__file__).parent.parent.parent / 'packages/fortios/hfortix_fortios/api/v2'
    
    if not base_dir.exists():
        print(f"❌ Base directory not found: {base_dir}")
        return
    
    print("🔍 Scanning for category directories...")
    
    # Find all categories (cmdb, monitor, log, service)
    categories = [d for d in base_dir.iterdir() if d.is_dir() and not d.name.startswith('_')]
    
    total_generated = 0
    
    for category_dir in categories:
        category_name = category_dir.name
        print(f"\n📁 Category: {category_name}")
        
        # Find all subcategories with __init__.py
        subcategories = [
            d for d in category_dir.iterdir() 
            if d.is_dir() and (d / '__init__.py').exists() and not d.name.startswith('_')
        ]
        
        for subcat_dir in subcategories:
            init_py = subcat_dir / '__init__.py'
            init_pyi = subcat_dir / '__init__.pyi'
            
            # Parse existing __init__.py
            endpoints = parse_init_py(init_py)
            
            if not endpoints:
                print(f"  ⏭️  {subcat_dir.name}: No imports found")
                continue
            
            # Generate __init__.pyi
            content = generate_category_stub(subcat_dir.name, endpoints)
            init_pyi.write_text(content, encoding='utf-8')
            
            print(f"  ✅ {subcat_dir.name}/__init__.pyi ({len(endpoints)} endpoints)")
            total_generated += 1
    
    print(f"\n✨ Generated {total_generated} category stub files")


if __name__ == '__main__':
    main()
