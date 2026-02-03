#!/usr/bin/env python3
"""
Regenerate __init__.py files for all CMDB categories

Scans the generated endpoint files and updates __init__.py to import them all.
"""

from pathlib import Path
import re


def snake_to_camel(snake_str: str) -> str:
    """
    Convert snake_case to PascalCase.
    Matches schema_parser.py behavior: 'dot1p_map' -> 'Dot1pMap', '802_1X' -> '8021x'
    
    Special cases:
    - 'cmdb' -> 'CMDB' (API type)
    - 'monitor' -> 'Monitor' (API type)
    - 'log' -> 'Log' (API type)
    - 'service' -> 'Service' (API type)
    - 'x3g_modem_custom' -> 'X3gModemCustom' (keep x prefix, capitalize each part)
    - 'x5g_modem' -> 'X5gModem' (keep x prefix, capitalize each part)
    """
    # Special handling for top-level API types
    api_type_mapping = {
        'cmdb': 'CMDB',
        'monitor': 'Monitor',
        'log': 'Log',
        'service': 'Service',
    }
    
    if snake_str in api_type_mapping:
        return api_type_mapping[snake_str]
    
    # Standard conversion: just capitalize each component
    # This matches schema_parser.py's class_name property logic
    components = snake_str.split('_')
    return ''.join(component.capitalize() for component in components)


def _generate_subdir_wrapper_init(subdir: Path, base_module_name: str, class_name: str):
    """
    Generate a wrapper __init__.py for a subdirectory that has a corresponding _base file.
    
    This creates a wrapper class that inherits from the base class (with GET methods)
    and adds action methods from the subdirectory's endpoint files.
    
    Args:
        subdir: Path to the subdirectory (e.g., .../firewall/policy/)
        base_module_name: Name of the base module (e.g., 'policy_base')
        class_name: Name of the class to create (e.g., 'Policy')
    
    Example:
        For monitor/firewall/policy/ with policy_base.py:
        - Imports Policy from ..policy_base
        - Creates wrapper Policy class that inherits from base
        - Adds clear_counters, reset, update_global_label as attributes
    """
    # Find all Python endpoint files in the subdirectory (exclude __init__.py, _helpers, etc.)
    action_files = [
        f for f in subdir.glob("*.py")
        if f.name != "__init__.py" and not f.name.startswith("_")
    ]
    
    if not action_files:
        # No action files, just use base class directly
        return
    
    # Build imports for action classes
    action_imports = []
    action_attrs = []
    
    for action_file in sorted(action_files):
        action_module = action_file.stem
        action_class = snake_to_camel(action_module)
        action_imports.append(f"from .{action_module} import {action_class}")
        action_attrs.append((action_module, action_class))
    
    # Generate __init__.py content
    init_content = f'"""FortiOS CMDB - {class_name} category"""\n\n'
    
    # Import base class from parent directory
    init_content += f"from ..{base_module_name} import {class_name} as {class_name}Base\n"
    
    # Import action classes
    init_content += "\n".join(action_imports) + "\n\n"
    
    # Add __all__
    all_exports = [action_class for _, action_class in action_attrs]
    all_exports.append(class_name)
    init_content += f"__all__ = [\n"
    for exp in sorted(all_exports):
        init_content += f'    "{exp}",\n'
    init_content += "]\n\n\n"
    
    # Add wrapper class that inherits from base
    init_content += f"class {class_name}({class_name}Base):\n"
    init_content += f'    """{class_name} endpoints wrapper for CMDB API."""\n\n'
    init_content += f"    def __init__(self, client):\n"
    init_content += f'        """{class_name} endpoints.\n        \n'
    init_content += "        Args:\n"
    init_content += "            client: HTTP client instance for API communication\n"
    init_content += '        """\n'
    init_content += "        super().__init__(client)  # Initialize base class with GET methods\n"
    
    # Add action endpoint attributes
    for action_module, action_class in sorted(action_attrs):
        init_content += f"        self.{action_module} = {action_class}(client)\n"
    
    # Write file
    init_file = subdir / "__init__.py"
    init_file.write_text(init_content)
    print(f"      ✨ Generated wrapper {subdir.name}/__init__.py (inherits from {base_module_name}, {len(action_attrs)} actions)")


def regenerate_category_init(category_dir: Path, base_dir: Path):
    """Regenerate __init__.py for a category directory.
    
    Args:
        category_dir: The category directory to process
        base_dir: The base API directory for relative path display
    """
    
    # Python reserved keywords that need special import handling
    RESERVED_KEYWORDS = {'global', 'class', 'def', 'import', 'from', 'return', 'if', 'elif', 'else', 'for', 'while'}
    
    # Find all Python files (exclude __init__.py and __pycache__)
    endpoint_files = [
        f for f in category_dir.glob("*.py")
        if f.name != "__init__.py" and not f.name.startswith("_")
    ]
    
    # Find all subdirectories (exclude __pycache__ and _helpers)
    subdirectories = [
        d for d in category_dir.iterdir()
        if d.is_dir() and not d.name.startswith("_")
    ]
    
    if not endpoint_files and not subdirectories:
        return
    
    # Get category name
    category_name = category_dir.name
    class_name = snake_to_camel(category_name)
    
    # Build imports and attributes
    imports = []
    attributes = []
    subdirectory_namespaces = []
    needs_importlib = False
    
    # Track subdirectory names to skip them in file processing
    subdir_names = {d.name for d in subdirectories}
    
    # Track _base files that have corresponding subdirectories
    # These need special handling to create wrapper classes that inherit from base
    base_files_with_subdirs = {}
    for ep_file in endpoint_files:
        if ep_file.stem.endswith('_base'):
            base_name = ep_file.stem[:-5]  # Remove '_base' suffix
            if base_name in subdir_names:
                base_files_with_subdirs[base_name] = ep_file.stem  # e.g., {'policy': 'policy_base'}
    
    # Process subdirectories first - they become namespace classes
    for subdir in sorted(subdirectories):
        subdir_name = subdir.name
        
        # Convert hyphens to underscores for Python attribute names
        # e.g., 'custom-field' -> 'custom_field'
        attr_name = subdir_name.replace('-', '_')
        
        # Skip subdirectories that would conflict with the 'client' parameter
        if attr_name == 'client':
            # Use an alias to avoid conflict
            subdir_class_name = snake_to_camel(attr_name)
            if '-' in subdir_name:
                needs_importlib = True
                subdirectory_namespaces.append((subdir_name, attr_name, subdir_class_name, True, True))  # (dir_name, attr_name, class_name, use_importlib, is_subdir)
            else:
                imports.append(f"from . import {subdir_name} as {attr_name}_ns")
                subdirectory_namespaces.append((attr_name, subdir_class_name, True))  # True = use alias
        else:
            subdir_class_name = snake_to_camel(attr_name)
            # Import the subdirectory as a module
            # Handle hyphenated directory names by using importlib
            if '-' in subdir_name:
                imports.append(f"# Hyphenated directory: {subdir_name} -> {attr_name}")
                needs_importlib = True
                subdirectory_namespaces.append((subdir_name, attr_name, subdir_class_name, True, True))  # (dir_name, attr_name, class_name, use_importlib, is_subdir)
            else:
                imports.append(f"from . import {subdir_name}")
                subdirectory_namespaces.append((subdir_name, attr_name, subdir_class_name, False, False))  # (dir_name, attr_name, class_name, use_importlib, is_subdir)
        
        # If this subdirectory has a corresponding _base file, generate a wrapper __init__.py
        if subdir_name in base_files_with_subdirs:
            _generate_subdir_wrapper_init(
                subdir,
                base_files_with_subdirs[subdir_name],
                subdir_class_name
            )
    
    # Process endpoint files
    for ep_file in sorted(endpoint_files):
        module_name = ep_file.stem  # filename without .py
        
        # Skip if there's a subdirectory with the same name (subdirectory takes precedence)
        if module_name in subdir_names:
            continue
        
        # Skip _base files if there's a subdirectory (e.g., skip fsw_firmware_base.py if fsw_firmware/ exists)
        if module_name.endswith('_base'):
            base_name = module_name[:-5]
            if base_name in subdir_names:
                continue
        
        # Strip _base suffix for class name derivation ONLY if it ends with _base
        # This handles files like policy_base.py which have class Policy (not PolicyBase)
        if module_name.endswith('_base'):
            class_base_name = module_name[:-5]  # Remove '_base' suffix
        else:
            class_base_name = module_name
        class_name_ep = snake_to_camel(class_base_name)
        
        # Check if module name starts with a digit or is a reserved keyword
        needs_special_import = False
        if module_name and module_name[0].isdigit():
            needs_special_import = True
            needs_importlib = True
            imports.append(f"# Cannot use 'from .{module_name}' - starts with digit, using importlib")
        elif module_name in RESERVED_KEYWORDS:
            needs_special_import = True
            needs_importlib = True
            imports.append(f"# Cannot use 'from .{module_name}' - reserved keyword, using importlib")
        else:
            imports.append(f"from .{module_name} import {class_name_ep}")
        
        attributes.append((module_name, class_name_ep, needs_special_import))
    
    # Generate __init__.py content
    init_content = f'"""FortiOS CMDB - {class_name} category"""\n\n'
    
    # Add importlib if needed
    if needs_importlib:
        init_content += "import importlib\n"
    
    # Add imports
    init_content += "\n".join(imports) + "\n\n"
    
    # Add __all__
    all_exports = [class_name_ep for _, class_name_ep, _ in attributes]
    # Handle different subdirectory tuple formats
    for subdir_info in subdirectory_namespaces:
        if len(subdir_info) == 5:  # New format with hyphenated directories
            _, _, subdir_class_name, _, _ = subdir_info
        elif len(subdir_info) == 3:  # Old format with alias
            _, subdir_class_name, _ = subdir_info
        else:  # Very old format
            _, subdir_class_name = subdir_info
        all_exports.append(subdir_class_name)
    all_exports.append(class_name)
    init_content += f"__all__ = [\n"
    for exp in sorted(all_exports):
        init_content += f'    "{exp}",\n'
    init_content += "]\n\n\n"
    
    # Add wrapper class
    init_content += f"class {class_name}:\n"
    init_content += f'    """{class_name} endpoints wrapper for CMDB API."""\n\n'
    init_content += f"    def __init__(self, client):\n"
    init_content += f'        """{class_name} endpoints.\n        \n'
    init_content += "        Args:\n"
    init_content += "            client: HTTP client instance for API communication\n"
    init_content += '        """\n'
    
    # Add subdirectory namespace assignments FIRST
    for subdir_info in sorted(subdirectory_namespaces):
        if len(subdir_info) == 5:  # New format with hyphenated directories
            dir_name, attr_name, subdir_class_name, use_importlib_flag, is_subdir = subdir_info
            
            # Check if attr_name starts with a digit (need setattr)
            needs_setattr = attr_name and attr_name[0].isdigit()
            
            if use_importlib_flag:
                # Use importlib for hyphenated directory names
                init_content += f"        _mod = importlib.import_module('.{dir_name}', package=__package__)\n"
                if needs_setattr:
                    init_content += f"        setattr(self, '{attr_name}', _mod.{subdir_class_name}(client))\n"
                else:
                    init_content += f"        self.{attr_name} = _mod.{subdir_class_name}(client)\n"
            else:
                if needs_setattr:
                    init_content += f"        setattr(self, '{attr_name}', {dir_name}.{subdir_class_name}(client))\n"
                else:
                    init_content += f"        self.{attr_name} = {dir_name}.{subdir_class_name}(client)\n"
        elif len(subdir_info) == 3:  # Old format with alias flag
            subdir_name, subdir_class_name, uses_alias = subdir_info
            # Check if subdir_name starts with a digit
            needs_setattr = subdir_name and subdir_name[0].isdigit()
            
            if uses_alias:
                if needs_setattr:
                    init_content += f"        setattr(self, '{subdir_name}', {subdir_name}_ns.{subdir_class_name}(client))\n"
                else:
                    init_content += f"        self.{subdir_name} = {subdir_name}_ns.{subdir_class_name}(client)\n"
            else:
                if needs_setattr:
                    init_content += f"        setattr(self, '{subdir_name}', {subdir_name}.{subdir_class_name}(client))\n"
                else:
                    init_content += f"        self.{subdir_name} = {subdir_name}.{subdir_class_name}(client)\n"
        else:  # Very old format (backward compat)
            subdir_name, subdir_class_name = subdir_info
            needs_setattr = subdir_name and subdir_name[0].isdigit()
            if needs_setattr:
                init_content += f"        setattr(self, '{subdir_name}', {subdir_name}.{subdir_class_name}(client))\n"
            else:
                init_content += f"        self.{subdir_name} = {subdir_name}.{subdir_class_name}(client)\n"
    
    # Add endpoint assignments
    for module_name, class_name_ep, needs_special_import in sorted(attributes):
        # Strip _base suffix for attribute name ONLY if it ends with _base
        # So policy_base.py creates self.policy, not self.policy_base
        if module_name.endswith('_base'):
            attr_name = module_name[:-5]
        else:
            attr_name = module_name
        
        if needs_special_import:
            # Use importlib to dynamically import reserved keywords or modules starting with digits
            # Also use setattr since we can't do self.global = ... or self.802 = ...
            init_content += f"        _mod = importlib.import_module('.{module_name}', package=__package__)\n"
            init_content += f"        setattr(self, '{attr_name}', _mod.{class_name_ep}(client))\n"
        else:
            init_content += f"        self.{attr_name} = {class_name_ep}(client)\n"
    
    # Write file
    init_file = category_dir / "__init__.py"
    init_file.write_text(init_content)
    total_items = len(attributes) + len(subdirectory_namespaces)
    print(f"  ✅ {category_dir.relative_to(base_dir)}/__init__.py ({len(attributes)} endpoints, {len(subdirectory_namespaces)} subdirs)")


if __name__ == "__main__":
    # Base directory - resolve from script location
    script_path = Path(__file__).resolve()
    # From .dev/generator/helpers/regenerate_init_files.py go up 4 levels to fortinet root
    fortinet_root = script_path.parent.parent.parent.parent
    api_base = fortinet_root / "packages" / "fortios" / "hfortix_fortios" / "api" / "v2"
    
    print(f"🔍 Fortinet root: {fortinet_root}")
    print(f"🔍 API base: {api_base}\n")
    
    # Process all API types
    api_types = ["cmdb", "monitor", "log", "service"]
    total_categories = 0
    
    for api_type in api_types:
        base_dir = api_base / api_type
        
        if not base_dir.exists():
            print(f"⚠️  Skipping {api_type} - directory does not exist")
            continue
        
        print(f"\n🔄 Regenerating __init__.py files in: {base_dir}\n")
        
        # Find all category directories
        category_dirs = [d for d in base_dir.iterdir() if d.is_dir() and not d.name.startswith("_")]
        
        # First, regenerate the top-level API type __init__.py (cmdb, monitor, log, service)
        regenerate_category_init(base_dir, api_base)
        
        for category_dir in sorted(category_dirs):
            regenerate_category_init(category_dir, base_dir)
            
            # Also process subdirectories recursively
            def process_subdirectories(parent_dir: Path, base: Path):
                subdirs = [d for d in parent_dir.iterdir() if d.is_dir() and not d.name.startswith("_")]
                for subdir in subdirs:
                    regenerate_category_init(subdir, base)
                    process_subdirectories(subdir, base)  # Recurse
            
            process_subdirectories(category_dir, base_dir)
        
        total_categories += len(category_dirs)
        print(f"✅ Regenerated {len(category_dirs)} {api_type} category __init__.py files")
    
    print(f"\n✅ Total: Regenerated {total_categories} category __init__.py files across all API types")
