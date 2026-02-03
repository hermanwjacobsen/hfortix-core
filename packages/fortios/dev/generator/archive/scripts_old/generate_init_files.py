#!/usr/bin/env python3
"""Generate __init__.py files for all API v2 categories and subcategories.

This script handles:
1. Top-level categories (cmdb, monitor, service, log)
2. Nested subcategories with mixed files and subdirectories
3. Naming conflicts (e.g., when parameter 'client' conflicts with module 'client')
"""

from pathlib import Path
import re

def to_pascal_case(name: str) -> str:
    """Convert snake_case or kebab-case to PascalCase."""
    words = re.sub(r'[-_]', ' ', name).split()
    return ''.join(word.capitalize() for word in words)


def generate_subcategory_init(subcat_dir: Path, class_name: str):
    """Generate __init__.py for a subcategory (handles nested structure).
    
    Args:
        subcat_dir: Path to subcategory directory
        class_name: PascalCase class name for this subcategory
    """
    # Find subdirectories (further nesting) and .py files (endpoints)
    subdirs = sorted([d for d in subcat_dir.iterdir() 
                     if d.is_dir() and not d.name.startswith('_')])
    
    py_files = sorted([f for f in subcat_dir.glob("*.py") 
                      if f.name != "__init__.py" and not f.name.endswith("_base.py")])
    
    imports = []
    class_attrs = []
    exports = []
    
    # Track reserved names to avoid conflicts
    reserved_names = {'client'}  # Parameter name
    
    # Handle subdirectories (nested categories)
    for subdir in subdirs:
        module_name = subdir.name
        sub_class_name = to_pascal_case(module_name)
        
        # Check for naming conflict
        if module_name in reserved_names:
            # Use alias to avoid conflict
            import_alias = f"{module_name}_module"
            imports.append(f"from . import {module_name} as {import_alias}")
            class_attrs.append(f"        self.{module_name} = {import_alias}.{sub_class_name}(client)")
        else:
            imports.append(f"from . import {module_name}")
            class_attrs.append(f"        self.{module_name} = {module_name}.{sub_class_name}(client)")
        
        exports.append(f'    "{sub_class_name}",')
    
    # Handle .py files (direct endpoints)
    for py_file in py_files:
        module_name = py_file.stem
        endpoint_class_name = to_pascal_case(module_name)
        
        # Check for naming conflict
        if module_name in reserved_names:
            import_alias = f"{module_name}_module"
            imports.append(f"from . import {module_name} as {import_alias}")
            class_attrs.append(f"        self.{module_name} = {import_alias}.{endpoint_class_name}(client)")
        else:
            imports.append(f"from . import {module_name}")
            class_attrs.append(f"        self.{module_name} = {module_name}.{endpoint_class_name}(client)")
        
        exports.append(f'    "{endpoint_class_name}",')
    
    if not imports:
        # Empty subcategory, create minimal __init__.py
        content = f'''"""FortiOS {class_name} - {subcat_dir.name} endpoints"""

__all__ = ["{class_name}"]


class {class_name}:
    """{class_name} endpoints."""
    
    def __init__(self, client):
        """{class_name} endpoints.
        
        Args:
            client: HTTP client instance
        """
        pass
'''
    else:
        exports_with_class = [f'    "{class_name}",'] + exports
        
        content = f'''"""FortiOS {class_name} - {subcat_dir.name} endpoints"""

{chr(10).join(imports)}

__all__ = [
{chr(10).join(sorted(set(exports_with_class)))}
]


class {class_name}:
    """{class_name} endpoints."""
    
    def __init__(self, client):
        """{class_name} endpoints.
        
        Args:
            client: HTTP client instance
        """
{chr(10).join(class_attrs)}
'''
    
    init_file = subcat_dir / "__init__.py"
    with open(init_file, "w") as f:
        f.write(content)
    
    return len(subdirs) + len(py_files)


def generate_category_init(category_dir: Path, category_name: str, class_name: str):
    """Generate __init__.py for a top-level category (cmdb, monitor, service).
    
    Args:
        category_dir: Path to category directory
        category_name: Name for documentation (e.g., "cmdb")
        class_name: Exact class name to use (e.g., "CMDB", "Monitor")
    """
    # Find all subdirectories (subcategories)
    subdirs = sorted([d for d in category_dir.iterdir() 
                     if d.is_dir() and not d.name.startswith('_')])
    
    imports = []
    class_attrs = []
    exports = []
    
    for subdir in subdirs:
        module_name = subdir.name
        sub_class_name = to_pascal_case(module_name)
        
        imports.append(f"from . import {module_name}")
        class_attrs.append(f"        self.{module_name} = {module_name}.{sub_class_name}(client)")
        exports.append(f'    "{sub_class_name}",')
    
    exports_with_class = [f'    "{class_name}",'] + exports
    
    content = f'''"""FortiOS {class_name} - {category_name} category endpoints"""

{chr(10).join(imports)}

__all__ = [
{chr(10).join(sorted(exports_with_class))}
]


class {class_name}:
    """{class_name} endpoints wrapper for {category_name} category."""
    
    def __init__(self, client):
        """{class_name} endpoints.
        
        Args:
            client: HTTP client instance
        """
{chr(10).join(class_attrs)}
'''
    
    init_file = category_dir / "__init__.py"
    with open(init_file, "w") as f:
        f.write(content)
    
    return len(subdirs)


def generate_log_init(log_dir: Path):
    """Generate __init__.py for log category (flat structure with .py files)."""
    # Find all .py files (excluding __init__.py)
    py_files = sorted([f for f in log_dir.glob("*.py") if f.name != "__init__.py"])
    
    imports = []
    class_attrs = []
    exports = []
    
    for py_file in py_files:
        module_name = py_file.stem
        class_name = to_pascal_case(module_name)
        
        imports.append(f"from . import {module_name}")
        class_attrs.append(f"        self.{module_name} = {module_name}.{class_name}(client)")
        exports.append(f'    "{class_name}",')
    
    exports_with_class = ['    "Log",'] + exports
    
    content = f'''"""FortiOS Log - log category endpoints"""

{chr(10).join(imports)}

__all__ = [
{chr(10).join(sorted(exports_with_class))}
]


class Log:
    """Log endpoints wrapper for log category."""
    
    def __init__(self, client):
        """Log endpoints.
        
        Args:
            client: HTTP client instance
        """
{chr(10).join(class_attrs)}
'''
    
    init_file = log_dir / "__init__.py"
    with open(init_file, "w") as f:
        f.write(content)
    
    return len(py_files)


def generate_all_init_files(base_dir: Path):
    """Generate all __init__.py files for API v2."""
    print("=" * 80)
    print("Generating __init__.py files for API v2")
    print("=" * 80)
    
    total_modules = 0
    total_generated = 0
    
    # Top-level categories with subdirectory structure
    categories = [
        ("cmdb", "cmdb", "CMDB"),
        ("monitor", "monitor", "Monitor"),
        ("service", "service", "Service"),
    ]
    
    for category_dir_name, category_name, class_name in categories:
        category_dir = base_dir / category_dir_name
        if not category_dir.exists():
            print(f"⚠️  Skipping {category_name} (directory not found)")
            continue
        
        print(f"\n📁 {class_name} ({category_dir.name}/)")
        
        # Generate subcategory __init__.py files
        subdirs = sorted([d for d in category_dir.iterdir() 
                         if d.is_dir() and not d.name.startswith('_')])
        
        for subdir in subdirs:
            sub_class_name = to_pascal_case(subdir.name)
            count = generate_subcategory_init(subdir, sub_class_name)
            total_modules += count
            total_generated += 1
            print(f"   ✅ {subdir.name}/ → {sub_class_name} ({count} items)")
        
        # Generate category __init__.py
        count = generate_category_init(category_dir, category_name, class_name)
        total_generated += 1
        print(f"   ✅ __init__.py → {class_name} ({count} subcategories)")
    
    # Log category (flat structure)
    log_dir = base_dir / "log"
    if log_dir.exists():
        print(f"\n📁 Log (log/)")
        count = generate_log_init(log_dir)
        total_modules += count
        total_generated += 1
        print(f"   ✅ __init__.py → Log ({count} endpoints)")
    
    print("\n" + "=" * 80)
    print(f"✅ Generated {total_generated} __init__.py files")
    print(f"   Total modules/endpoints processed: {total_modules}")
    print("=" * 80)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        base_dir = Path(sys.argv[1])
    else:
        # Default to the v2 API directory
        script_dir = Path(__file__).parent
        repo_root = script_dir.parent.parent
        base_dir = repo_root / "packages/fortios/hfortix_fortios/api/v2"
    
    if not base_dir.exists():
        print(f"❌ Error: Directory not found: {base_dir}")
        sys.exit(1)
    
    generate_all_init_files(base_dir)
