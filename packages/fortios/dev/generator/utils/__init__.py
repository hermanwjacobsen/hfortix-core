"""Shared utilities for code generation."""

from .naming import (
    to_class_name,
    to_module_name,
    to_constant_name,
    to_attr_name,
    kebab_to_snake,
    snake_to_kebab,
    fix_api_path,
)

from .paths import (
    get_output_path,
    get_category_dir,
    ensure_dir,
)

__all__ = [
    # Naming utilities
    "to_class_name",
    "to_module_name", 
    "to_constant_name",
    "to_attr_name",
    "kebab_to_snake",
    "snake_to_kebab",
    "fix_api_path",
    
    # Path utilities
    "get_output_path",
    "get_category_dir",
    "ensure_dir",
]
