"""Path handling utilities for code generation."""

from pathlib import Path


def ensure_dir(path: Path) -> Path:
    """Ensure directory exists, create if needed.
    
    Args:
        path: Directory path to ensure
        
    Returns:
        The path (for chaining)
    """
    path.mkdir(parents=True, exist_ok=True)
    return path


def get_category_dir(output_dir: Path, category: str) -> Path:
    """Get category directory path.
    
    Args:
        output_dir: Base output directory
        category: Category name (cmdb, monitor, service, log)
        
    Returns:
        Path to category directory
    """
    return output_dir / category


def get_output_path(
    output_dir: Path,
    category: str,
    endpoint_path: str,
    file_name: str,
    suffix: str = ".py"
) -> Path:
    """Get output file path for generated code.
    
    Args:
        output_dir: Base output directory
        category: Category name
        endpoint_path: Endpoint path (e.g., 'firewall/address')
        file_name: File name (without extension)
        suffix: File extension (default: .py)
        
    Returns:
        Full path to output file
        
    Examples:
        >>> get_output_path(Path('/out'), 'cmdb', 'firewall/address', 'address')
        Path('/out/cmdb/firewall/address.py')
    """
    category_dir = get_category_dir(output_dir, category)
    
    # For nested paths (e.g., firewall/address)
    if "/" in endpoint_path:
        parts = endpoint_path.split("/")
        # Create subdirectory structure for parent path
        if len(parts) > 1:
            subdir = category_dir / "/".join(parts[:-1])
            ensure_dir(subdir)
            return subdir / f"{file_name}{suffix}"
    
    # For flat paths
    ensure_dir(category_dir)
    return category_dir / f"{file_name}{suffix}"


def get_helpers_dir(output_dir: Path, category: str, endpoint_path: str) -> Path:
    """Get _helpers directory for validators.
    
    Args:
        output_dir: Base output directory
        category: Category name
        endpoint_path: Endpoint path
        
    Returns:
        Path to _helpers directory
    """
    category_dir = get_category_dir(output_dir, category)
    
    if "/" in endpoint_path:
        parts = endpoint_path.split("/")[:-1]  # Exclude endpoint name
        if parts:
            helpers_dir = category_dir / "/".join(parts) / "_helpers"
        else:
            helpers_dir = category_dir / "_helpers"
    else:
        helpers_dir = category_dir / "_helpers"
    
    return ensure_dir(helpers_dir)


def resolve_naming_conflict(output_file: Path, base_name: str) -> Path:
    """Resolve naming conflicts between files and directories.
    
    If a directory exists with the same name as the file we want to create,
    append '_endpoint' to avoid conflicts.
    
    Args:
        output_file: Proposed output file path
        base_name: Base name (without extension)
        
    Returns:
        Resolved output file path
        
    Examples:
        If 'system/interface/' directory exists:
        >>> resolve_naming_conflict(Path('system/interface.py'), 'interface')
        Path('system/interface_endpoint.py')
    """
    parent_dir = output_file.parent
    conflict_dir = parent_dir / base_name
    
    if conflict_dir.exists() and conflict_dir.is_dir():
        # Naming conflict - append _endpoint
        new_name = f"{base_name}_endpoint{output_file.suffix}"
        return parent_dir / new_name
    
    return output_file
