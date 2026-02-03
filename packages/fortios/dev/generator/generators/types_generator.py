#!/usr/bin/env python3
"""
TypedDict and Response Type Generator

Generates TypedDict classes for:
1. Request payloads (for each endpoint)
2. Standard FortiOS response types
3. Extracts Literal types for enum fields

This provides IDE autocomplete and type checking for all API interactions.
"""

from pathlib import Path
from typing import Any
import json


class TypesGenerator:
    """Generate TypedDict classes and Literal types from schemas."""
    
    def __init__(self):
        """Initialize the types generator."""
        pass
    
    def generate_response_types(self, output_path: Path) -> None:
        """
        Generate standard FortiOS response type models.
        
        Creates a module with TypedDict classes for all API responses.
        
        Args:
            output_path: Path to write the types module (e.g., hfortix_fortios/types.py)
        """
        content = '''"""
FortiOS API Response Types

TypedDict classes for FortiOS API responses to provide IDE autocomplete
and type checking.

Auto-generated - DO NOT EDIT
"""

from typing import TypedDict, NotRequired, Literal, Any


class FortiOSSuccessResponse(TypedDict):
    """
    Standard successful response from FortiOS API.
    
    Examples:
        >>> result = fgt.api.cmdb.firewall.address.get(name="web-server")
        >>> result["status"]  # IDE autocompletes!
        'success'
        >>> result["http_status"]
        200
    """
    http_method: str
    """HTTP method used (GET, POST, PUT, DELETE)"""
    
    results: list[dict[str, Any]] | dict[str, Any]
    """Response data - list for collection queries, dict for single items"""
    
    vdom: str
    """Virtual domain name"""
    
    path: str
    """API endpoint path"""
    
    name: NotRequired[str]
    """Object name (only present for single object queries)"""
    
    status: Literal["success"]
    """Response status - always 'success' for this type"""
    
    http_status: int
    """HTTP status code (200 for success)"""
    
    build: int
    """FortiOS build number"""
    
    version: str
    """FortiOS version string (e.g., 'v7.6.5')"""
    
    serial: str
    """Device serial number"""


class FortiOSErrorResponse(TypedDict):
    """
    Error response from FortiOS API.
    
    Examples:
        >>> try:
        ...     result = fgt.api.cmdb.firewall.address.get(name="nonexistent")
        ... except ResourceNotFoundError as e:
        ...     print(e.response["error"])  # IDE autocompletes!
        ...     404
    """
    http_method: str
    """HTTP method used"""
    
    error: int
    """Error code (e.g., -3 for object not found)"""
    
    message: NotRequired[str]
    """Human-readable error message"""
    
    http_status: int
    """HTTP status code (4xx or 5xx)"""
    
    status: NotRequired[Literal["error"]]
    """Response status - 'error' when present"""
    
    vdom: NotRequired[str]
    """Virtual domain name"""
    
    path: NotRequired[str]
    """API endpoint path"""


class FortiOSResponse(TypedDict):
    """
    Generic FortiOS API response (success or error).
    
    Use this when the response could be either success or error.
    For better type safety, use FortiOSSuccessResponse or FortiOSErrorResponse.
    
    Examples:
        >>> result: FortiOSResponse = fgt.api.cmdb.firewall.address.get()
        >>> if result.get("status") == "success":
        ...     # Type narrowed to success response
        ...     items = result["results"]
    """
    http_method: str
    results: NotRequired[list[dict[str, Any]] | dict[str, Any]]
    vdom: NotRequired[str]
    path: NotRequired[str]
    name: NotRequired[str]
    status: NotRequired[Literal["success", "error"]]
    http_status: int
    error: NotRequired[int]
    message: NotRequired[str]
    build: NotRequired[int]
    version: NotRequired[str]
    serial: NotRequired[str]


# Common Literal types used across multiple endpoints
ActionType = Literal["accept", "deny", "ipsec"]
"""Common firewall policy action types"""

StatusType = Literal["enable", "disable"]
"""Common enable/disable status"""

LogSeverity = Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]
"""Syslog severity levels"""

ScheduleType = Literal["onetime", "recurring"]
"""Schedule types"""

ProtocolType = Literal["tcp", "udp", "icmp", "icmpv6", "ip", "sctp"]
"""Common IP protocol types"""


__all__ = [
    "FortiOSSuccessResponse",
    "FortiOSErrorResponse", 
    "FortiOSResponse",
    "ActionType",
    "StatusType",
    "LogSeverity",
    "ScheduleType",
    "ProtocolType",
]
'''
        
        # Ensure parent directory exists
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Write the file
        output_path.write_text(content)
        print(f"✅ Generated response types: {output_path}")
    
    def extract_literal_type(self, field_info: dict[str, Any]) -> str | None:
        """
        Extract Literal type definition from field info.
        
        Args:
            field_info: Field information from schema
            
        Returns:
            Literal type string (e.g., "Literal['enable', 'disable']") or None
        """
        # Check if pydantic_type already has Literal
        pydantic_type = field_info.get("pydantic_type", "")
        if pydantic_type.startswith("Literal["):
            return pydantic_type
        
        # Check for allowed_values in validation
        validation = field_info.get("validation", {})
        allowed_values = validation.get("allowed_values", [])
        
        if allowed_values:
            # Format as Literal type
            quoted_values = [f"'{v}'" for v in allowed_values]
            return f"Literal[{', '.join(quoted_values)}]"
        
        # Check options field (alternative format)
        options = field_info.get("options", [])
        if options:
            values = [opt["name"] for opt in options if "name" in opt]
            if values:
                quoted_values = [f"'{v}'" for v in values]
                return f"Literal[{', '.join(quoted_values)}]"
        
        return None
    
    def generate_payload_typeddict(
        self,
        endpoint_name: str,
        schema: dict[str, Any],
        operation: str = "POST"
    ) -> str:
        """
        Generate TypedDict class for endpoint payload.
        
        Args:
            endpoint_name: Endpoint name (e.g., "FirewallPolicy")
            schema: Complete endpoint schema
            operation: HTTP operation (POST, PUT)
            
        Returns:
            Python code for TypedDict class
        """
        fields = schema.get("fields", {})
        mkey = schema.get("mkey", "")
        
        # Class name
        class_name = f"{endpoint_name}{operation.capitalize()}Payload"
        
        # Build field definitions
        field_defs = []
        required_fields = []
        
        for field_name, field_info in fields.items():
            # Skip readonly fields
            if field_info.get("readonly", False):
                continue
            
            python_name = field_info.get("python_name", field_name)
            
            # Get type
            pydantic_type = field_info.get("pydantic_type", "Any")
            python_type = field_info.get("python_type", "Any")
            
            # Use Literal if available
            literal_type = self.extract_literal_type(field_info)
            if literal_type:
                field_type = literal_type
            else:
                field_type = pydantic_type if pydantic_type != "Any" else python_type
            
            # Handle optional/required
            is_required = field_info.get("required", False)
            
            # For POST, mkey is usually required
            if operation == "POST" and field_name == mkey:
                is_required = True
            
            # Build field definition with documentation
            help_text = field_info.get("help", "")
            example = field_info.get("example", "")
            
            # Build docstring
            doc_parts = []
            if help_text:
                doc_parts.append(help_text)
            if example:
                doc_parts.append(f"Example: {example}")
            
            docstring = " - ".join(doc_parts) if doc_parts else ""
            
            if is_required:
                field_defs.append(f'    {python_name}: {field_type}')
                required_fields.append(python_name)
            else:
                field_defs.append(f'    {python_name}: NotRequired[{field_type}]')
            
            if docstring:
                field_defs.append(f'    """{docstring}"""')
            field_defs.append("")  # Blank line
        
        # Generate class
        code_parts = [
            f"class {class_name}(TypedDict, total=False):",
            f'    """',
            f'    Type-safe payload for {endpoint_name} {operation} operation.',
            f'    ',
            f'    Required fields: {", ".join(required_fields) if required_fields else "None"}',
            f'    """',
            "",
        ]
        
        if field_defs:
            code_parts.extend(field_defs)
        else:
            code_parts.append("    pass")
        
        return "\n".join(code_parts)
    
    def generate_endpoint_types(
        self,
        schema: dict[str, Any],
        output_path: Path
    ) -> None:
        """
        Generate TypedDict classes for a specific endpoint.
        
        Creates payload types for POST and PUT operations.
        
        Args:
            schema: Complete endpoint schema
            output_path: Where to write the types (e.g., _helpers/types.py)
        """
        endpoint_name = schema.get("class_name", "Unknown")
        
        # Generate header
        content = f'''"""
Type definitions for {endpoint_name}

Auto-generated TypedDict classes for type-safe API operations.
"""

from typing import TypedDict, NotRequired, Literal, Any


'''
        
        # Generate POST payload
        if "POST" in schema.get("http_methods", []):
            content += self.generate_payload_typeddict(endpoint_name, schema, "POST")
            content += "\n\n"
        
        # Generate PUT payload
        if "PUT" in schema.get("http_methods", []):
            content += self.generate_payload_typeddict(endpoint_name, schema, "PUT")
            content += "\n\n"
        
        # Write file
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(content)
        print(f"  📝 Generated types: {output_path.name}")


if __name__ == "__main__":
    # Test generation
    gen = TypesGenerator()
    
    # Generate response types
    output_dir = Path(__file__).parents[3] / "packages" / "fortios" / "hfortix_fortios"
    gen.generate_response_types(output_dir / "types.py")
    
    print("✅ Response types generated successfully")
