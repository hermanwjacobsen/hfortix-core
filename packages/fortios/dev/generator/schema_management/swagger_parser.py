#!/usr/bin/env python3
"""
Swagger/OpenAPI Schema Parser for FortiOS

Parses Swagger documentation to extract endpoint information
when API schemas are not available (e.g., for action endpoints).

Usage:
    parser = SwaggerParser('/path/to/swagger/docs')
    endpoint_info = parser.get_endpoint_info('monitor', 'firewall/multicast-policy/clear_counters')
"""

import json
from pathlib import Path
from typing import Any, Optional


class SwaggerParser:
    """Parse FortiOS Swagger/OpenAPI documentation."""
    
    def __init__(self, swagger_docs_dir: Path):
        """
        Initialize Swagger parser.
        
        Args:
            swagger_docs_dir: Directory containing Swagger JSON files
        """
        self.swagger_docs_dir = Path(swagger_docs_dir)
        self._cache: dict[str, dict] = {}  # Cache loaded Swagger files
        
    def _load_swagger_file(self, category: str) -> Optional[dict]:
        """
        Load Swagger file for a category.
        
        Args:
            category: API category (cmdb, monitor, log, service)
            
        Returns:
            Parsed Swagger JSON or None if not found
        """
        # Check cache first
        if category in self._cache:
            return self._cache[category]
        
        category_dir = self.swagger_docs_dir / category
        if not category_dir.exists():
            return None
        
        # Find Swagger files (they have long names like "FortiOS 7.6 FortiOS 7.6.5 Monitor API firewall.json")
        swagger_files = list(category_dir.glob("*.json"))
        
        # Combine all Swagger files for this category
        combined_paths = {}
        for swagger_file in swagger_files:
            try:
                with open(swagger_file) as f:
                    data = json.load(f)
                    paths = data.get('paths', {})
                    combined_paths.update(paths)
            except Exception as e:
                print(f"⚠️  Failed to load {swagger_file.name}: {e}")
                continue
        
        if combined_paths:
            self._cache[category] = {'paths': combined_paths}
            return self._cache[category]
        
        return None
    
    def get_endpoint_info(
        self,
        category: str,
        endpoint_path: str,
    ) -> Optional[dict[str, Any]]:
        """
        Get endpoint information from Swagger docs.
        
        Args:
            category: API category (cmdb, monitor, log, service)
            endpoint_path: Endpoint path (e.g., "firewall/multicast-policy/clear_counters")
            
        Returns:
            Dictionary with endpoint info:
            {
                'path': '/firewall/multicast-policy/clear_counters',
                'methods': ['post'],
                'summary': 'Reset traffic statistics...',
                'parameters': [...],
                'is_action': True
            }
            Returns None if endpoint not found in Swagger
        """
        swagger_data = self._load_swagger_file(category)
        if not swagger_data:
            return None
        
        # Build the full path (Swagger paths start with /)
        # Strip trailing slashes from endpoint_path for consistency
        endpoint_path = endpoint_path.rstrip("/")
        full_path = f"/{endpoint_path}"
        
        paths = swagger_data.get('paths', {})
        
        # Try exact match first
        if full_path in paths:
            endpoint_data = paths[full_path]
        # Try with trailing slash
        elif f"{full_path}/" in paths:
            endpoint_data = paths[f"{full_path}/"]
            full_path = f"{full_path}/"
        # Try converting first slash to dot (e.g., firewall/schedule -> firewall.schedule)
        # This handles cases like /firewall.schedule/group in Swagger
        elif "/" in endpoint_path:
            parts = endpoint_path.split("/", 1)
            if len(parts) == 2:
                dotted_path = f"/{parts[0]}.{parts[1]}"
                if dotted_path in paths:
                    endpoint_data = paths[dotted_path]
                    full_path = dotted_path
                elif f"{dotted_path}/" in paths:
                    endpoint_data = paths[f"{dotted_path}/"]
                    full_path = f"{dotted_path}/"
                else:
                    return None
            else:
                return None
        else:
            return None
        
        # Extract HTTP methods
        methods = [
            method.upper()
            for method in endpoint_data.keys()
            if method in ['get', 'post', 'put', 'delete', 'patch']
        ]
        
        # Get primary operation (prefer POST for action endpoints, GET for data endpoints)
        primary_method = 'post' if 'post' in endpoint_data else list(endpoint_data.keys())[0]
        operation = endpoint_data.get(primary_method, {})
        
        # Determine if this is an action endpoint (POST-only, no GET)
        is_action = 'post' in methods and 'get' not in methods
        
        return {
            'path': full_path,
            'methods': methods,
            'summary': operation.get('summary', ''),
            'description': operation.get('description', ''),
            'parameters': operation.get('parameters', []),
            'is_action': is_action,
            'primary_method': primary_method.upper(),
        }
    
    def create_minimal_schema(
        self,
        category: str,
        endpoint_path: str,
        endpoint_info: dict[str, Any],
    ) -> dict[str, Any]:
        """
        Create a minimal schema from Swagger endpoint info.
        
        This is used when the API doesn't provide a schema (e.g., for action endpoints).
        
        Args:
            category: API category
            endpoint_path: Endpoint path
            endpoint_info: Endpoint info from get_endpoint_info()
            
        Returns:
            Minimal schema compatible with our schema parser
        """
        endpoint_name = Path(endpoint_path).name
        
        # Extract parameters/fields from Swagger
        children = {}
        parameters = endpoint_info.get('parameters', [])
        
        for param in parameters:
            # Skip if param is not a dict (might be a string reference)
            if not isinstance(param, dict):
                continue
                
            # Look for body parameters with schema
            if param.get('in') == 'body' and 'schema' in param:
                schema = param['schema']
                
                # Skip if schema is a string reference (like '#/definitions/...')
                if not isinstance(schema, dict):
                    continue
                    
                schema_props = schema.get('properties', {})
                for prop_name, prop_info in schema_props.items():
                    children[prop_name] = {
                        "name": prop_name,
                        "type": prop_info.get('type', 'string'),
                        "help": prop_info.get('description', ''),
                        "required": param.get('required', False),
                        "category": "unitary",
                    }
        
        # Build minimal schema
        schema = {
            "name": endpoint_name,
            "category": "action" if endpoint_info['is_action'] else "table",
            "help": endpoint_info.get('summary', f"Endpoint: {endpoint_path}"),
            "readonly": 'get' in [m.lower() for m in endpoint_info['methods']] and len(endpoint_info['methods']) == 1,
            "children": children,
            "mkey": None,
            "mkey_type": None,
            "_metadata": {
                "source": "swagger",
                "category": category,
                "endpoint_path": endpoint_path,
                "full_endpoint": f"{category}.{endpoint_path.replace('/', '.')}",
                "is_action_endpoint": endpoint_info['is_action'],
                "http_methods": endpoint_info['methods'],
                "note": "Generated from Swagger documentation (no API schema available)"
            }
        }
        
        return schema
    
    def list_all_endpoints(self, category: str) -> list[str]:
        """
        List all endpoints in a category from Swagger docs.
        
        Args:
            category: API category
            
        Returns:
            List of endpoint paths (without leading /)
        """
        swagger_data = self._load_swagger_file(category)
        if not swagger_data:
            return []
        
        paths = swagger_data.get('paths', {})
        
        # Remove leading / and filter out parameter paths like {mkey}
        endpoints = []
        for path in paths.keys():
            # Skip paths with path parameters
            if '{' in path:
                continue
            
            # Remove leading /
            clean_path = path.lstrip('/')
            endpoints.append(clean_path)
        
        return sorted(endpoints)
