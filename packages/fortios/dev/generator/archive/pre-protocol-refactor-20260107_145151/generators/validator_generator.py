"""
Validator Generator

Generates validation helper files (_helpers/{endpoint}.py) from FortiOS schemas.
Implements two-stage validation pattern from v0.4.3.
"""

from pathlib import Path
from typing import Any

from jinja2 import Environment, FileSystemLoader

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
from schema_management.schema_parser import EndpointSchema
from utils.naming import snake_to_kebab, kebab_to_snake, to_constant_name


class ValidatorGenerator:
    """Generates validation helper files."""
    
    def __init__(self, template_dir: Path):
        """
        Initialize validator generator.
        
        Args:
            template_dir: Directory containing Jinja2 templates
        """
        self.env = Environment(
            loader=FileSystemLoader(str(template_dir)),
            trim_blocks=True,
            lstrip_blocks=True,
        )
        
        # Add custom filters - use shared utility functions
        self.env.filters["snake_to_kebab"] = snake_to_kebab
        self.env.filters["kebab_to_snake"] = kebab_to_snake
        self.env.filters["to_constant_name"] = to_constant_name
        
    # Removed: _snake_to_kebab, _kebab_to_snake, _to_constant_name - now using shared utils from utils.naming
    
    def generate(
        self,
        schema: EndpointSchema,
        output_dir: Path,
        generator_version: str = "0.5.0",
    ) -> Path:
        """
        Generate validation helper file.
        
        Args:
            schema: Parsed schema
            output_dir: Base output directory (e.g., packages/fortios/hfortix_fortios/api/v2)
            generator_version: Version of generator
            
        Returns:
            Path to generated file
        """
        # Load template
        template = self.env.get_template("validator.py.j2")
        
        # Prepare template context
        context = {
            "schema": schema,
            "generator_version": generator_version,
            "generation_timestamp": self._get_timestamp(),
            "required_fields": self._extract_required_fields(schema),
            "fields_with_defaults": self._extract_defaults(schema),
            "enum_constants": self._extract_enum_constants(schema),
            "deprecated_fields": self._extract_deprecated_fields(schema),
            "all_fields": list(schema.fields.values()),  # Add all fields for documentation
        }
        
        # Render template
        rendered = template.render(**context)
        
        # Determine output path
        # Structure: output_dir/cmdb/firewall/_helpers/ssh_setting.py
        category_dir = output_dir / schema.category
        
        # Create subdirectories for nested paths
        if "/" in schema.path:
            parts = schema.path.split("/")
            # Convert hyphens to underscores for Python package names
            safe_parts = [p.replace("-", "_") for p in parts[:-1]]
            endpoint_dir = category_dir / "/".join(safe_parts) / "_helpers"
        else:
            endpoint_dir = category_dir / "_helpers"
        
        endpoint_dir.mkdir(parents=True, exist_ok=True)
        
        # Use schema.file_name for the actual filename (handles underscores)
        output_file = endpoint_dir / f"{schema.file_name}.py"
        
        # Write file
        with open(output_file, "w") as f:
            f.write(rendered)
        
        return output_file
    
    def _extract_required_fields(self, schema: EndpointSchema) -> list[dict[str, Any]]:
        """
        Extract required fields from schema, filtering out FALSE POSITIVES.
        
        FortiOS schemas incorrectly mark many fields as required. This method
        filters out obvious false positives:
        1. Fields with NON-EMPTY default values (empty string "" doesn't count)
        2. Specialized feature fields (wanopt, rtp, vpn, nat64, nat46, ztna, ssl-ssh)
        
        Note: This still may not be 100% accurate (conditional requirements like
        srcaddr vs srcaddr6), but it's better than blindly trusting the schema.
        """
        required = []
        specialized_keywords = ['wanopt', 'rtp', 'vpn', 'ztna', 'ssl-ssh', 'nat64', 'nat46']
        
        for field_name, field in schema.fields.items():
            if not field.required:
                continue
                
            # Filter 1: Skip fields with NON-EMPTY default values
            # Empty string "" or None means "no meaningful default"
            if field.default is not None and field.default != "":
                continue
                
            # Filter 2: Skip specialized feature fields (false positive)
            if any(keyword in field.name.lower() for keyword in specialized_keywords):
                continue
            
            # This field passed the filters - likely truly required
            required.append({
                "name": field.name,
                "python_name": field.name.replace("-", "_"),
                "help": field.help,
            })
        
        return required
    
    def _extract_defaults(self, schema: EndpointSchema) -> dict[str, Any]:
        """Extract fields with default values."""
        defaults = {}
        for field_name, field in schema.fields.items():
            if field.default is not None:
                defaults[field.name] = field.default
        return defaults
    
    def _extract_enum_constants(self, schema: EndpointSchema) -> list[dict[str, Any]]:
        """Extract enum constants for validation."""
        import re
        enums = []
        for field_name, field in schema.fields.items():
            if field.options:
                # Replace all non-alphanumeric characters with underscores for valid Python identifiers
                safe_name = re.sub(r'[^a-zA-Z0-9]', '_', field.name)
                constant_name = f"VALID_BODY_{safe_name.upper()}"
                enums.append({
                    "constant_name": constant_name,
                    "field_name": field.name,
                    "python_name": field.name.replace("-", "_"),
                    "options": field.options,  # Changed from 'values' to 'options'
                })
        return enums
    
    def _extract_deprecated_fields(self, schema: EndpointSchema) -> dict[str, dict[str, str]]:
        """
        Extract deprecated fields from schema.
        
        Returns:
            Dict mapping field names to deprecation info:
            {
                "field_name": {
                    "reason": "...",
                    "alternative": "...",
                    "removal_version": "..."
                }
            }
        """
        deprecated = {}
        for field_name, field in schema.fields.items():
            if field.deprecated:
                deprecated[field.name] = {}
                if field.deprecation_reason:
                    deprecated[field.name]["reason"] = field.deprecation_reason
                if field.alternative:
                    deprecated[field.name]["alternative"] = field.alternative
                # Could add removal_version if available in schema
        return deprecated
    
    @staticmethod
    def _get_timestamp() -> str:
        """Get current UTC timestamp."""
        from datetime import datetime, timezone
        return datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
