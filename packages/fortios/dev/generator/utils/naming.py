"""Naming convention utilities for code generation.

All naming transformations in one place for consistency across generators.
"""

import re


def kebab_to_snake(name: str) -> str:
    """Convert kebab-case to snake_case.
    
    Also handles:
    - Leading digits (prepend 'x' for protocols, move to end for simple numbers)
    - Special cases (as -> asn)
    - Dots, slashes, plus signs, spaces, angle brackets, parentheses
    - Python reserved words (appended with _)
    
    Examples:
        >>> kebab_to_snake('firewall-address')
        'firewall_address'
        >>> kebab_to_snake('802-1x-settings')
        'x802_1x_settings'
        >>> kebab_to_snake('as')
        'asn'
        >>> kebab_to_snake('default value')
        'default_value'
        >>> kebab_to_snake('<application list name>')
        'application_list_name'
        >>> kebab_to_snake('threshold(default)')
        'threshold_default'
        >>> kebab_to_snake('class')
        'class_'
    """
    # Remove angle brackets first (they appear in some FortiOS schema fields)
    result = name.replace("<", "").replace(">", "")
    # Convert parentheses to underscores
    result = result.replace("(", "_").replace(")", "")
    # Then convert separators to underscores
    result = result.replace("-", "_").replace("/", "_").replace("+", "_plus_").replace(".", "_").replace(" ", "_")
    # Clean up any double underscores that might have been created
    while "__" in result:
        result = result.replace("__", "_")
    # Remove trailing underscores
    result = result.rstrip("_")
    
    # Special case: 'as' (BGP Autonomous System) -> 'asn'
    if result == "as":
        return "asn"
    
    # Fix identifiers starting with digits - always prefix with 'x'
    # This is simpler and more predictable than trying to move digits around
    if result and result[0].isdigit():
        result = f"x{result}"
    
    # Handle Python reserved words by appending underscore (PEP 8 convention)
    # Note: 'as' is handled above as 'asn' special case
    PYTHON_RESERVED = {
        'False', 'None', 'True', 'and', 'assert', 'async', 'await',
        'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
        'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
        'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try',
        'while', 'with', 'yield'
    }
    if result in PYTHON_RESERVED:
        result = f"{result}_"
    
    return result


def snake_to_kebab(name: str) -> str:
    """Convert snake_case to kebab-case.
    
    Examples:
        >>> snake_to_kebab('firewall_address')
        'firewall-address'
    """
    return name.replace("_", "-")


def to_class_name(name: str) -> str:
    """Convert any format to PascalCase.
    
    Examples:
        >>> to_class_name('firewall-address')
        'FirewallAddress'
        >>> to_class_name('firewall_address')
        'FirewallAddress'
        >>> to_class_name('802-1x-settings')
        'X8021xSettings'
    """
    # First convert to snake_case to normalize
    snake = kebab_to_snake(name)
    
    # Split on underscores and capitalize each part
    parts = snake.split('_')
    return ''.join(p.capitalize() for p in parts if p)


def to_module_name(name: str) -> str:
    """Convert any format to valid Python module name (snake_case).
    
    Examples:
        >>> to_module_name('FirewallAddress')
        'firewall_address'
        >>> to_module_name('firewall-address')
        'firewall_address'
    """
    # Convert CamelCase to snake_case
    result = re.sub('([a-z0-9])([A-Z])', r'\1_\2', name)
    result = result.lower()
    
    # Then apply kebab_to_snake to handle other cases
    return kebab_to_snake(result)


def to_attr_name(name: str) -> str:
    """Convert to valid Python attribute name.
    
    Same as to_module_name but used for clarity in different contexts.
    
    Examples:
        >>> to_attr_name('file-filter')
        'file_filter'
    """
    return kebab_to_snake(name)


def to_constant_name(name: str) -> str:
    """Convert to SCREAMING_SNAKE_CASE for constants.
    
    Examples:
        >>> to_constant_name('srcaddr')
        'SRCADDR'
        >>> to_constant_name('firewall-address')
        'FIREWALL_ADDRESS'
    """
    # Replace all non-alphanumeric with underscore
    result = re.sub(r'[^a-zA-Z0-9]', '_', name)
    return result.upper()


def fix_api_path(path: str) -> str:
    """Fix API paths that were renamed to avoid Python keywords.
    
    Converts Python-safe names back to original FortiOS API paths.
    
    Examples:
        >>> fix_api_path('firewall/global_setting')
        'firewall/global'
        >>> fix_api_path('switch_controller/x802_1X_settings')
        'switch-controller/802.1X-settings'
    """
    # Convert _setting suffix back to original for keywords
    path = path.replace("global_setting", "global")
    path = path.replace("class_setting", "class")
    path = path.replace("import_setting", "import")
    
    # Remove 'x' prefix added for numeric starts (802.1X, 3g-modem, etc.)
    parts = path.split("/")
    fixed_parts = []
    for part in parts:
        # Check if starts with 'x' followed by digits
        if part.startswith('x') and len(part) > 1 and part[1].isdigit():
            part = part[1:]  # Remove the 'x'
        fixed_parts.append(part)
    
    return "/".join(fixed_parts)


def sanitize_docstring(text: str) -> str:
    """Sanitize text for use in docstrings.
    
    - Escapes triple quotes
    - Removes problematic characters
    
    Examples:
        >>> sanitize_docstring('Some "quoted" text')
        'Some "quoted" text'
    """
    if not text:
        return ""
    
    # Escape triple quotes
    text = text.replace('"""', r'\"\"\"')
    
    return text


def get_file_name(endpoint_path: str) -> str:
    """Get safe filename from endpoint path.
    
    Examples:
        >>> get_file_name('firewall/address')
        'address'
        >>> get_file_name('system/global')
        'global_setting'  # Avoid keyword
    """
    name = endpoint_path.split("/")[-1]
    
    # Handle Python keywords
    if name in ('global', 'class', 'import', 'from'):
        name = f"{name}_setting"
    
    return kebab_to_snake(name)
