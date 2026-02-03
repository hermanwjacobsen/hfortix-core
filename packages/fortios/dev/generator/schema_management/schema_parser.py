"""
Schema Parser for FortiOS API Schemas

Parses FortiOS schema JSON and extracts structured metadata for code generation.

Supported Categories:
    - CMDB:    Configuration endpoints (full schemas with fields, mkey, etc.)
    - Monitor: Monitoring endpoints (limited/no schemas, may need manual definition)
    - Service: Service endpoints (if schemas available)

NOT Supported:
    - Log: Log endpoints use composition pattern (shared types across storage backends).
           These are manually implemented in api/v2/log/ directory.
           Future: Consider separate log-specific generator.

Edge Cases Handled:
    1. Dots in paths:   firewall.ssh/setting → firewall/ssh_setting.py
    2. Dashes in paths: casb/saas-application → casb/saas_application.py
    3. Normal paths:    firewall/policy → firewall/policy.py

Path Handling:
    - api_path: Preserved exactly for API calls (dots, dashes intact)
    - path:     Python file structure (dots/dashes → underscores, flat structure)
    - name:     Python class/file names (underscores only)
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any
import keyword
import re


def extract_allowed_values(description: str) -> list[str] | None:
    """
    Extract allowed values from description strings.
    
    Patterns supported:
    - ['value1', 'value2'] -> ['value1', 'value2']
    - [value1 | value2] -> ['value1', 'value2']
    - [value1 | value2*] -> ['value1', 'value2'] (asterisk indicates default)
    
    Returns:
        List of allowed values, or None if no pattern found.
    """
    if not description:
        return None
    
    # Pattern 1: ['value1', 'value2'] format
    match = re.search(r"\['([^']+)'(?:,\s*'([^']+)')*\]", description)
    if match:
        # Extract all quoted values
        values = re.findall(r"'([^']+)'", description)
        if values:
            return values
    
    # Pattern 2: [value1 | value2] format (with optional * for default)
    match = re.search(r"\[([^\]]+)\]", description)
    if match:
        content = match.group(1)
        if "|" in content:
            # Split by | and clean up
            values = []
            for part in content.split("|"):
                # Remove whitespace and asterisk (default indicator at start or end)
                value = part.strip().lstrip("*").rstrip("*").strip()
                if value:
                    values.append(value)
            if values:
                return values
    
    return None


@dataclass
class FieldMetadata:
    """Metadata for a single schema field."""
    name: str
    type: str  # string, integer, option, var-string, ipv4-address, etc.
    help: str
    required: bool = False
    default: Any = None
    options: list[str] | None = None  # For enums: ["enable", "disable"]
    enum_help: dict[str, str] | None = None  # Help text for each enum value
    min_value: int | None = None
    max_value: int | None = None
    max_length: int | None = None  # String max length (renamed from size)
    datasource: list[str] | None = None
    children: dict[str, "FieldMetadata"] | None = None  # Nested objects (tables)
    category: str | None = None  # For nested tables
    is_list: bool = False  # True for table fields
    deprecated: bool = False  # True if field is deprecated
    deprecation_reason: str | None = None  # Reason for deprecation
    alternative: str | None = None  # Suggested alternative field
    

@dataclass
class EndpointSchema:
    """Complete schema for an API endpoint."""
    # Endpoint identification
    category: str  # cmdb, monitor, log, service
    path: str  # firewall/address (for file structure)
    api_path: str  # firewall/address or firewall.ssh/setting (for API calls)
    name: str  # address or ssh_setting (for file naming)
    full_path: str  # firewall.address
    
    # Schema metadata
    mkey: str | None  # Primary key field name (e.g., "name", "policyid")
    mkey_type: str | None  # string, integer
    help: str
    readonly: bool = False  # True for read-only reference tables (e.g., geography)
    http_method: str = "GET"  # HTTP method (GET, POST, PUT, DELETE)
    
    # Fields
    fields: dict[str, FieldMetadata] = field(default_factory=dict)
    required_fields: list[str] = field(default_factory=list)
    defaults: dict[str, Any] = field(default_factory=dict)
    
    # Version metadata
    version: str = "unknown"
    schema_hash: str = ""
    
    # Capabilities metadata (from schema v1.7.0+)
    capabilities: dict[str, Any] = field(default_factory=dict)
    
    # Relationships metadata (from schema v1.7.0+)
    relationships: dict[str, Any] = field(default_factory=dict)
    
    # Query parameters metadata (from schema v1.7.0+)
    query_params: dict[str, Any] = field(default_factory=dict)
    
    # Response fields metadata (from schema v1.7.0+ for service/monitor endpoints)
    response_fields: dict[str, FieldMetadata] = field(default_factory=dict)
    
    # Scope metadata (from schema v1.7.0+)
    # scope: "global", "vdom", or "global-vdom"
    # scope_options: ["global"], ["vdom"], or ["global", "vdom"]
    scope: str = "vdom"  # Default to vdom scope
    scope_options: list[str] = field(default_factory=lambda: ["vdom"])
    
    # Source tracking
    source_file: str = ""
    downloaded_at: str = ""
    
    @property
    def is_global_only(self) -> bool:
        """Check if endpoint is global-only (no vdom parameter needed)."""
        return self.scope_options == ["global"]
    
    @property
    def class_name(self) -> str:
        """Generate class name from endpoint name."""
        # Convert "ssh_setting" -> "SshSetting", "policy" -> "Policy"
        # Also handles dashes: "DoS-policy" -> "DosPolicy"
        # Handle digit prefixes: "3g-modem" -> "Modem3g", "802-1X" -> "X8021x"
        # Handle plus signs: "tacacs+" -> "TacacsPlus"
        name_safe = self.name
        
        # Handle plus signs: tacacs+ -> tacacs_plus_
        name_safe = name_safe.replace("+", "_plus_")
        
        # Special handling for specific digit-prefixed names
        if name_safe == "3g-modem":
            return "Modem3g"
        elif name_safe == "5g-modem":
            return "Modem5g"
        elif name_safe.startswith("802-1"):
            # 802-1X -> X8021x, 802-1X-settings -> X8021xSettings
            name_safe = "x" + name_safe.replace("-", "_")
        else:
            # General case
            name_safe = name_safe.replace("-", "_")
        
        parts = name_safe.split("_")
        return "".join(p.capitalize() for p in parts)
    
    @property
    def file_name(self) -> str:
        """Generate file name from endpoint name."""
        # Returns name with underscores (dashes converted): "DoS-policy" -> "DoS_policy"
        # Handle digit prefixes: "3g-modem" -> "modem3g", "802-1X" -> "x802_1x"
        # Handle Python keywords: "global" -> "global_", "import" -> "import_"
        # NOTE: Python builtins like "list", "filter" do NOT need underscore suffix
        # for endpoint/attribute names - only keywords need it
        # Handle plus signs: "tacacs+" -> "tacacs_plus_"
        import keyword
        
        name_safe = self.name
        
        # Handle plus signs FIRST: tacacs+ -> tacacs_plus_
        name_safe = name_safe.replace("+", "_plus_")
        
        # Special handling for specific digit-prefixed names
        if name_safe == "3g-modem":
            return "modem3g"
        elif name_safe == "5g-modem":
            return "modem5g"
        elif name_safe.startswith("802-1"):
            # 802-1X -> x802_1x, 802-1X-settings -> x802_1x_settings
            name_safe = "x" + name_safe.replace("-", "_").lower()
        else:
            # General case: convert dashes to underscores
            name_safe = name_safe.replace("-", "_")
        
        # Handle Python keywords ONLY by appending underscore
        # Builtins (list, filter, dict) are fine as attribute names
        if keyword.iskeyword(name_safe):
            name_safe = name_safe + "_"
        
        return name_safe


class SchemaParser:
    """Parse FortiOS schema JSON into structured metadata."""
    
    @staticmethod
    def _convert_plus_to_underscore(name: str) -> str:
        """
        Convert plus signs to _plus_ in identifiers.
        
        Examples:
            tacacs+ -> tacacs_plus
            tacacs+accounting -> tacacs_plus_accounting
            log.tacacs+accounting -> log.tacacs_plus_accounting
        
        Args:
            name: The name to convert
            
        Returns:
            Name with + replaced by _plus_ (with underscores on both sides if needed)
        """
        if '+' not in name:
            return name
        
        # Replace + with _plus_, but handle edge cases
        result = []
        for i, char in enumerate(name):
            if char == '+':
                # Add underscore before plus if not already there and not at start
                if i > 0 and name[i-1] not in ('_', '.', '/'):
                    result.append('_')
                result.append('plus')
                # Add underscore after plus if not already there and not at end
                if i < len(name) - 1 and name[i+1] not in ('_', '.', '/'):
                    result.append('_')
            else:
                result.append(char)
        
        return ''.join(result)
    
    @staticmethod
    def _fix_python_keyword(name: str) -> str:
        """
        Fix Python reserved keywords and invalid identifiers.
        
        Examples:
            global -> global_setting
            class -> class_setting
            802_1X -> x802_1X (prepend x for numeric start)
        
        Args:
            name: The endpoint name to check
            
        Returns:
            Fixed name if it's a keyword or invalid, otherwise original name
        """
        # Fix names that start with a digit
        if name and name[0].isdigit():
            name = f"x{name}"
        
        # Fix Python reserved keywords
        if keyword.iskeyword(name):
            return f"{name}_setting"
        
        return name
    
    @staticmethod
    def _parse_v1_7(schema_json: dict[str, Any], source_file: str = "") -> EndpointSchema:
        """
        Parse new v1.7.0 schema format.
        
        New format has:
        - schema_version: "1.7.0"
        - fields: dict (instead of children)
        - python_type, pydantic_type already computed
        - class_name, python_module pre-computed
        - Richer metadata (examples, patterns, related_endpoints, etc.)
        
        Args:
            schema_json: Schema in v1.7.0 format
            source_file: Path to source JSON file
            
        Returns:
            Parsed endpoint schema
        """
        # Extract basic metadata - already computed in v1.7.0
        raw_path = schema_json.get("path", "")  # e.g., "firewall/policy" or "firewall.service/custom"
        
        # NORMALIZE PATH: Convert dots to slashes for proper Python package structure
        # Schema may have: "firewall.service/custom" -> normalize to "firewall/service/custom"
        # This ensures the generator creates proper nested directories instead of flat dirs with dots
        path = raw_path.replace(".", "/")  # firewall.service/custom -> firewall/service/custom
        
        # Also normalize digit-prefixed path segments: "system/3g-modem" -> "system/modem3g"
        # And plus signs: "log/tacacs+accounting" -> "log/tacacs_plus_accounting"
        import keyword
        path_parts = path.split("/")
        normalized_parts = []
        for part in path_parts:
            # Handle plus signs first
            part_clean = part.replace("+", "_plus_")
            
            # Special cases for specific names
            if part_clean == "3g-modem":
                part_clean = "modem3g"
            elif part_clean == "5g-modem":
                part_clean = "modem5g"
            elif part_clean.startswith("802-1"):
                part_clean = "x" + part_clean.replace("-", "_").lower()
            else:
                # General case: dashes to underscores
                part_clean = part_clean.replace("-", "_")
            
            # Handle Python keywords in path segments
            if keyword.iskeyword(part_clean):
                part_clean = part_clean + "_"
            
            normalized_parts.append(part_clean)
        path = "/".join(normalized_parts)

        
        api_path = raw_path  # Keep original for API calls (may have dots)
        name = schema_json.get("name", "")  # e.g., "policy" or "custom"
        
        # Determine category from source file path
        # New schema is organized as: schema/VERSION/CATEGORY/endpoint.name.json
        source_path = Path(source_file)
        category = "cmdb"  # default
        if source_path.parts:
            # Look for category in path: .../cmdb/firewall.policy.json
            for i, part in enumerate(source_path.parts):
                if part in ("cmdb", "monitor", "log", "service"):
                    category = part
                    break
        
        # Build full_path for code generation (e.g., "cmdb.firewall.policy")
        full_path = f"{category}.{path.replace('/', '.')}"
        
        # Get mkey info
        mkey = schema_json.get("mkey")
        mkey_type = schema_json.get("mkey_type")
        
        # Get help text
        help_text = schema_json.get("help", f"Configuration for {path}")
        
        # Check if readonly
        readonly = schema_json.get("readonly", False)
        
        # Determine HTTP method(s) from schema
        # Priority: http_methods (list) > request_method (str) > default "GET"
        http_methods_list = schema_json.get("http_methods", [])
        if http_methods_list:
            # Use the first method as the primary (usually the only one for monitor/action endpoints)
            http_method = http_methods_list[0] if isinstance(http_methods_list, list) else str(http_methods_list)
        else:
            # Fall back to request_method or default
            http_method = schema_json.get("request_method", "GET")
        
        # Parse fields from v1.7.0 format
        # Check both "fields" (CMDB) and "request_fields" (service/monitor)
        fields_data = schema_json.get("fields", {}) or schema_json.get("request_fields", {})
        fields = {}
        required_fields = schema_json.get("required_fields", [])
        defaults = {}
        
        for field_name, field_data in fields_data.items():
            field_meta = SchemaParser._parse_field_v1_7(field_name, field_data)
            
            # Extract allowed values from summary field (for Literal types)
            summary = field_data.get("summary", "")
            allowed_values = extract_allowed_values(summary)
            if allowed_values and not field_meta.options:
                # Set options if extracted from summary and not already set
                field_meta.options = allowed_values
            
            fields[field_name] = field_meta
            
            # Track defaults
            if field_meta.default is not None:
                defaults[field_name] = field_meta.default
        
        # Extract capabilities if present
        capabilities = schema_json.get("capabilities", {})
        
        # Extract query_params if present (v1.7.0+) and enhance with allowed_values
        raw_query_params = schema_json.get("query_params", {})
        query_params = {}
        for method, params in raw_query_params.items():
            query_params[method] = {}
            for param_name, param_info in params.items():
                # Copy the param info and add allowed_values from description
                enhanced_info = dict(param_info)
                description = param_info.get("description", "")
                param_type = param_info.get("type", "")
                
                # Only extract Literal values for non-array types
                # Arrays may have enum values in their description that apply to array items, not the array itself
                if param_type != "array":
                    allowed_values = extract_allowed_values(description)
                    if allowed_values:
                        enhanced_info["allowed_values"] = allowed_values
                query_params[method][param_name] = enhanced_info
        
        # Parse response_fields if present (v1.7.0+ for service/monitor endpoints)
        # These define the structure of the API response
        response_fields_data = schema_json.get("response_fields", {})
        response_fields = {}
        for field_name, field_data in response_fields_data.items():
            field_meta = SchemaParser._parse_field_v1_7(field_name, field_data)
            response_fields[field_name] = field_meta
        
        # Extract scope information (v1.7.0+)
        scope = schema_json.get("scope", "vdom")
        scope_options = schema_json.get("scope_options", ["vdom"])
        
        # Create endpoint schema
        schema = EndpointSchema(
            category=category,
            path=path,
            api_path=api_path,
            name=name,
            full_path=full_path,
            mkey=mkey,
            mkey_type=mkey_type,
            help=help_text,
            readonly=readonly,
            http_method=http_method,  # Derived from http_methods or request_method
            fields=fields,
            required_fields=required_fields,
            defaults=defaults,
            capabilities=capabilities,
            relationships=schema_json.get("relationships", {}),
            query_params=query_params,
            response_fields=response_fields,
            scope=scope,
            scope_options=scope_options,
            version=schema_json.get("schema_version", "1.7.0"),
            source_file=source_file,
            downloaded_at=schema_json.get("generated_at", ""),
        )
        
        # Apply any manual overrides (load once per module import)
        if not hasattr(SchemaParser, '_overrides_cache'):
            SchemaParser._overrides_cache = SchemaParser.load_overrides()
        schema = SchemaParser.apply_overrides(schema, SchemaParser._overrides_cache)
        
        return schema
    
    @staticmethod
    def _parse_field_v1_7(field_name: str, field_data: dict[str, Any]) -> FieldMetadata:
        """
        Parse a single field from v1.7.0 format.
        
        New format has pre-computed python_type, pydantic_type, validation, etc.
        
        Args:
            field_name: Field name
            field_data: Field metadata dict
            
        Returns:
            Parsed field metadata
        """
        # Basic field info
        field_type = field_data.get("type", "string")
        help_text = field_data.get("help", "")
        
        # In v1.7.0, required is a boolean on the field itself
        required = field_data.get("required", False)
        if isinstance(required, list):
            # Fallback if it's still in list format
            required = field_name in required
        
        # Get default value
        default = field_data.get("default_value")
        
        # Get options for enums - extract just the names
        options = None
        enum_help = None
        if "options" in field_data:
            raw_options = field_data["options"]
            if raw_options:
                options = []
                enum_help = {}
                for option in raw_options:
                    if isinstance(option, dict):
                        opt_name = option.get("name", option.get("value", ""))
                        options.append(opt_name)
                        enum_help[opt_name] = option.get("help", "")
                    else:
                        # Sometimes options are just strings
                        options.append(str(option))
        
        # Get validation constraints
        validation = field_data.get("validation", {})
        min_value = validation.get("min")
        max_value = validation.get("max")
        max_length = validation.get("max_length")
        
        # Get datasource
        datasource = field_data.get("datasource")
        
        # Check if this is a nested table/list
        category = field_data.get("category", "")
        is_list = category == "table" or field_data.get("multiple_values", False)
        
        # Parse nested children if present
        children = None
        if "children" in field_data or "fields" in field_data:
            children_data = field_data.get("children") or field_data.get("fields") or {}
            children = {}
            for child_name, child_data in children_data.items():
                children[child_name] = SchemaParser._parse_field_v1_7(child_name, child_data)
        
        # Deprecation info
        deprecated = field_data.get("deprecated", False)
        deprecation_reason = field_data.get("deprecation_reason")
        alternative = field_data.get("alternative")
        
        return FieldMetadata(
            name=field_name,
            type=field_type,
            help=help_text,
            required=required,
            default=default,
            options=options,
            enum_help=enum_help,
            min_value=min_value,
            max_value=max_value,
            max_length=max_length,
            datasource=datasource,
            children=children,
            category=category,
            is_list=is_list,
            deprecated=deprecated,
            deprecation_reason=deprecation_reason,
            alternative=alternative,
        )
    
    @staticmethod
    def parse(schema_json: dict[str, Any], source_file: str = "") -> EndpointSchema:
        """
        Parse schema JSON into EndpointSchema object.
        
        Supports both legacy v1.6.0 format and new v1.7.0 format.
        
        Args:
            schema_json: Raw schema from FortiGate (can be wrapped with metadata or raw)
            source_file: Path to source JSON file
            
        Returns:
            Parsed endpoint schema
        """
        # Check schema version - new v1.7.0 format has schema_version field
        schema_version = schema_json.get("schema_version", "")
        
        if schema_version and schema_version.startswith("1.7"):
            # New v1.7.0 format - direct parsing
            return SchemaParser._parse_v1_7(schema_json, source_file)
        
        # Legacy format - check if this is a wrapped schema (from downloader) or raw schema
        if "_metadata" in schema_json:
            # Wrapped format from downloader
            metadata = schema_json.get("_metadata", {})
            category = metadata.get("category", "unknown")
            endpoint_path = metadata.get("endpoint_path", "").rstrip("/")  # Strip trailing slashes
            results = schema_json.get("results", {})
            
            # Handle monitor/service endpoints that return data lists instead of schemas
            if isinstance(results, list):
                # This is a data response, not a schema
                # Create a minimal schema for read-only endpoints
                results = {
                    "name": endpoint_path.split("/")[-1],
                    "category": "table",
                    "help": f"Monitor endpoint for {endpoint_path}",
                    "readonly": True,
                    "children": {},
                    "mkey": None,
                    "mkey_type": None
                }
            
            # CRITICAL: Use results.path for API path (preserves dots like "switch-controller.qos")
            # while endpoint_path is just for file structure (uses slashes)
            api_path_prefix = results.get("path", "")  # e.g., "switch-controller.qos" or "firewall"
            endpoint_name = results.get("name", "")  # e.g., "qos-policy" or "address"
        else:
            # Raw schema format - extract from source_file path
            # e.g., /path/to/schema_firewall_policy.json or .dev/schemas/cmdb/firewall/policy.json
            source_path = Path(source_file)
            
            # Try to extract from filename
            if "schema_" in source_path.name:
                # schema_firewall_policy.json -> firewall/policy
                name_part = source_path.stem.replace("schema_", "")
                endpoint_path = name_part.replace("_", "/").rstrip("/")  # Strip trailing slashes
                category = "cmdb"  # Default assumption
            else:
                # Try to extract from directory structure
                parts = source_path.parts
                if "schemas" in parts:
                    idx = parts.index("schemas")
                    if len(parts) > idx + 2:
                        category = parts[idx + 1]
                        endpoint_path = "/".join(parts[idx + 2:]).replace(".json", "").rstrip("/")  # Strip trailing slashes
                    else:
                        category = "cmdb"
                        endpoint_path = source_path.stem
                else:
                    category = "cmdb"
                    endpoint_path = source_path.stem
            
            results = schema_json
        
        # Get mkey info
        mkey = results.get("mkey")
        mkey_type = results.get("mkey_type")
        
        # Check if endpoint is readonly (e.g., geography reference tables)
        readonly = results.get("readonly", False)
        
        # Get help text
        help_text = results.get("help", f"Configuration for {endpoint_path}")
        
        # Parse children (fields)
        children = results.get("children", {})
        fields = {}
        required_fields = []
        defaults = {}
        
        for field_name, field_data in children.items():
            field_meta = SchemaParser._parse_field(field_name, field_data)
            fields[field_name] = field_meta
            
            # Track required fields
            if field_meta.required:
                required_fields.append(field_name)
            
            # Track defaults
            if field_meta.default is not None:
                defaults[field_name] = field_meta.default
        
        # Build endpoint name from path
        # =============================================================================
        # Path Handling - Use results.path for CORRECT API paths!
        #
        # CRITICAL: results.path contains the correct API path (with dots preserved)
        # while _metadata.endpoint_path is for file structure only
        #
        # Build API path from results.path + results.name
        # =============================================================================
        
        # Extract API path prefix and endpoint name from schema
        api_path_prefix = schema_json.get("path", "").strip()
        endpoint_name = schema_json.get("name", "").strip()
        
        # If we have api_path_prefix and endpoint_name from results, use them!
        if api_path_prefix and endpoint_name:
            # We have the correct API path components from schema
            api_path = f"{api_path_prefix}/{endpoint_name}"
            
            # For file path, convert to Python-safe structure
            # If path has dots, keep directory structure
            if "." in api_path_prefix:
                # e.g., "switch-controller.qos" → "switch_controller/qos/qos_policy"
                # e.g., "system.snmp" → "system/snmp/mib_view"
                # e.g., "log.tacacs+accounting" → "log/tacacs_plus_accounting/filter"
                # Replace dots with slashes to keep directory structure
                path_prefix = api_path_prefix.replace(".", "/")  # "switch-controller/qos" or "system/snmp" or "log/tacacs+accounting"
                path_prefix = path_prefix.replace("-", "_")      # "switch_controller/qos" or "system/snmp" or "log/tacacs+accounting"
                path_prefix = SchemaParser._convert_plus_to_underscore(path_prefix) # "switch_controller/qos" or "system/snmp" or "log/tacacs_plus_accounting"
                
                endpoint_name_safe = endpoint_name.replace("-", "_")
                endpoint_name_safe = SchemaParser._convert_plus_to_underscore(endpoint_name_safe)
                endpoint_name_safe = SchemaParser._fix_python_keyword(endpoint_name_safe)
                
                # Keep directory structure: switch_controller/qos/qos_policy
                path = f"{path_prefix}/{endpoint_name_safe}"
                endpoint_name = endpoint_name_safe
            else:
                # Normal case: just convert dashes/plus
                path_parts = api_path_prefix.split("/")
                path_parts = [p.replace("-", "_") for p in path_parts]
                path_parts = [SchemaParser._convert_plus_to_underscore(p) for p in path_parts]
                path_parts = [SchemaParser._fix_python_keyword(p) for p in path_parts]
                
                endpoint_name_safe = endpoint_name.replace("-", "_")
                endpoint_name_safe = SchemaParser._convert_plus_to_underscore(endpoint_name_safe)
                endpoint_name_safe = SchemaParser._fix_python_keyword(endpoint_name_safe)
                
                path = "/".join(path_parts) + "/" + endpoint_name_safe if path_parts else endpoint_name_safe
                endpoint_name = endpoint_name_safe
        
        # Fallback: use old logic based on endpoint_path (for backwards compat)
        elif "." in endpoint_path and "/" in endpoint_path:
            # Edge case: firewall.ssh/setting
            # - api_path: "firewall.ssh/setting" (preserve dot for API)
            # - path: "firewall/ssh_setting" (FLAT - no subdirs, use underscore)
            # - name: "ssh_setting" (for file naming)
            parts = endpoint_path.split(".")
            category_part = parts[0]  # "firewall"
            subcategory_path = ".".join(parts[1:])  # "ssh/setting"
            
            # For file structure, KEEP FLAT - replace dot and slash with underscore
            endpoint_name = subcategory_path.replace("/", "_").replace("-", "_")
            endpoint_name = SchemaParser._convert_plus_to_underscore(endpoint_name)  # tacacs+accounting → tacacs_plus_accounting
            endpoint_name = SchemaParser._fix_python_keyword(endpoint_name)  # Fix keywords
            api_path = endpoint_path  # "firewall.ssh/setting" (preserve dot)
            path = f"{category_part}/{endpoint_name}"  # "firewall/ssh_setting" (flat)
        else:
            # Normal case: firewall/policy or casb/saas-application or system/3g-modem
            # Convert dashes to underscores for Python compatibility
            endpoint_name = endpoint_path.split("/")[-1] if "/" in endpoint_path else endpoint_path
            endpoint_name = endpoint_name.replace("-", "_")  # saas-application → saas_application
            endpoint_name = SchemaParser._convert_plus_to_underscore(endpoint_name)  # tacacs+ → tacacs_plus
            endpoint_name = SchemaParser._fix_python_keyword(endpoint_name)  # Fix keywords like 'global' and numeric starts
            api_path = endpoint_path  # Preserve original (with dashes) for API calls
            # Process each path component: convert dashes, plus signs, keywords, and numeric starts
            path_parts = []
            for p in endpoint_path.split("/"):
                p = p.replace("-", "_")  # 3g-modem → 3g_modem, tacacs+accounting → tacacs+accounting
                p = SchemaParser._convert_plus_to_underscore(p)  # tacacs+accounting → tacacs_plus_accounting
                p = SchemaParser._fix_python_keyword(p)  # 3g_modem → x3g_modem
                path_parts.append(p)
            path = "/".join(path_parts)
        
        full_endpoint = f"{category}.{endpoint_path.replace('/', '.')}"
        
        # Extract capabilities if present (v1.7.0+ schemas)
        capabilities = schema_json.get("capabilities", {})
        
        # Extract scope information (v1.7.0+ schemas)
        scope = schema_json.get("scope", "vdom")
        scope_options = schema_json.get("scope_options", ["vdom"])
        
        # Extract query_params if present (v1.7.0+ schemas) and enhance with allowed_values
        raw_query_params = schema_json.get("query_params", {})
        query_params = {}
        for method, params in raw_query_params.items():
            query_params[method] = {}
            for param_name, param_info in params.items():
                # Copy the param info and add allowed_values from description
                enhanced_info = dict(param_info)
                description = param_info.get("description", "")
                param_type = param_info.get("type", "")
                
                # Only extract Literal values for non-array types
                # Arrays may have enum values in their description that apply to array items, not the array itself
                if param_type != "array":
                    allowed_values = extract_allowed_values(description)
                    if allowed_values:
                        enhanced_info["allowed_values"] = allowed_values
                query_params[method][param_name] = enhanced_info
        
        # Build endpoint schema
        schema = EndpointSchema(
            category=category,
            path=path,
            api_path=api_path,
            name=endpoint_name,
            full_path=full_endpoint,
            mkey=mkey,
            mkey_type=mkey_type,
            help=help_text,
            readonly=readonly,
            http_method=results.get("http_method", "GET"),  # Extract HTTP method (GET, POST, etc.)
            fields=fields,
            required_fields=required_fields,
            defaults=defaults,
            capabilities=capabilities,
            query_params=query_params,
            scope=scope,
            scope_options=scope_options,
            downloaded_at=metadata.get("downloaded_at", "") if "_metadata" in schema_json else "",
            source_file=source_file,
        )
        
        # Apply any manual overrides (load once per module import)
        if not hasattr(SchemaParser, '_overrides_cache'):
            SchemaParser._overrides_cache = SchemaParser.load_overrides()
        schema = SchemaParser.apply_overrides(schema, SchemaParser._overrides_cache)
        
        return schema
    
    @staticmethod
    def _parse_field(name: str, field_data: dict[str, Any]) -> FieldMetadata:
        """
        Parse a single field from schema.
        
        Args:
            name: Field name
            field_data: Field data from schema
            
        Returns:
            FieldMetadata object
        """
        field_type = field_data.get("type", "string")
        help_text = field_data.get("help", "")
        required = field_data.get("required", False)
        default = field_data.get("default")
        category = field_data.get("category")
        
        # Parse enum values (for option type)
        options = None
        enum_help = None
        if "options" in field_data:
            options = []
            enum_help = {}
            for option in field_data["options"]:
                if isinstance(option, dict):
                    opt_name = option.get("name", option.get("value", ""))
                    options.append(opt_name)
                    enum_help[opt_name] = option.get("help", "")
                else:
                    # Sometimes options are just strings
                    options.append(str(option))
        
        # Parse constraints
        min_value = field_data.get("min-value")
        max_value = field_data.get("max-value")
        max_length = field_data.get("size")
        
        # Parse datasources (references to other tables)
        datasource = field_data.get("datasource")
        
        # Parse deprecation info (if available in schema)
        # Note: FortiOS schemas may not include explicit deprecation flags
        # This provides infrastructure for future support
        deprecated = field_data.get("deprecated", False)
        deprecation_reason = field_data.get("deprecation_reason")
        alternative = field_data.get("alternative")
        
        # Determine if this is a list/table
        is_list = category == "table"
        
        # Parse nested children (for table types)
        children = None
        if "children" in field_data:
            children = {}
            for child_name, child_data in field_data["children"].items():
                children[child_name] = SchemaParser._parse_field(child_name, child_data)
        
        return FieldMetadata(
            name=name,
            type=field_type,
            help=help_text,
            required=required,
            default=default,
            options=options,
            enum_help=enum_help,
            min_value=min_value,
            max_value=max_value,
            max_length=max_length,
            datasource=datasource,
            children=children,
            category=category,
            is_list=is_list,
            deprecated=deprecated,
            deprecation_reason=deprecation_reason,
            alternative=alternative,
        )
    
    @staticmethod
    def extract_dependencies(schema: EndpointSchema) -> dict[str, Any]:
        """
        Analyze field dependencies (e.g., type=ipmask requires subnet).
        
        This analyzes the schema to determine which fields are required
        based on the value of other fields.
        
        Args:
            schema: Parsed endpoint schema
            
        Returns:
            Dependency rules dictionary
        """
        dependencies = {}
        
        # Look for fields with options that might have dependencies
        # This is a simplified version - full implementation would need
        # more sophisticated analysis
        
        for field_name, field in schema.fields.items():
            if field.options and field_name in ["type", "mode", "method"]:
                # Commonly, "type" fields determine what other fields are required
                dependencies[field_name] = {}
                
        return dependencies
    
    @staticmethod
    def extract_conflicts(schema: EndpointSchema) -> list[list[str]]:
        """
        Analyze field conflicts (mutually exclusive groups).
        
        Args:
            schema: Parsed endpoint schema
            
        Returns:
            List of mutually exclusive field groups
        """
        conflicts = []
        
        # This is a placeholder - full implementation would need
        # sophisticated analysis of which fields can't coexist
        
        return conflicts

    @staticmethod
    def extract_table_fields_metadata(schema_data: dict[str, Any]) -> dict[str, dict[str, Any]]:
        """
        Extract metadata for table fields (for normalization support).
        
        Extracts mkey, required_fields, and generates examples for each table field.
        This metadata is used by the normalizer to support flexible input formats.
        
        Args:
            schema_data: Raw schema dictionary
            
        Returns:
            Dictionary mapping field names to their metadata:
            {
                "member": {
                    "mkey": "name",
                    "required_fields": ["name"],
                    "example": "[{'name': 'value'}]"
                },
                "realservers": {
                    "mkey": "id",
                    "required_fields": ["id", "ip"],
                    "example": "[{'id': 1, 'ip': '192.168.1.10'}]"
                }
            }
        """
        table_fields = {}
        
        fields = schema_data.get("fields", {})
        for field_name, field_info in fields.items():
            # Only process table fields
            if field_info.get("category") != "table":
                continue
            
            # Extract mkey
            mkey = field_info.get("mkey", "name")
            
            # Extract required children
            required_fields = []
            children = field_info.get("children", {})
            for child_name, child_info in children.items():
                if child_info.get("required", False):
                    required_fields.append(child_name)
            
            # If no required fields found, at least include the mkey
            if not required_fields:
                required_fields = [mkey]
            
            # Generate example from required fields
            example_parts = []
            for req_field in required_fields:
                child_info = children.get(req_field, {})
                child_type = child_info.get("type", "string")
                
                # Generate appropriate example value
                if req_field in ("id", "index", "seq-num", "priority") or child_type == "integer":
                    example_parts.append(f"'{req_field}': 1")
                elif req_field in ("ip", "ipaddr", "server", "extip") or child_type in ("ipv4-address", "ipv4-address-any"):
                    example_parts.append(f"'{req_field}': '192.168.1.10'")
                elif req_field in ("port", "port-num", "extport") or req_field.endswith("-port"):
                    example_parts.append(f"'{req_field}': 443")
                elif child_type == "option" and child_info.get("options"):
                    # Use first option as example
                    first_option = child_info["options"][0].get("name", "value")
                    example_parts.append(f"'{req_field}': '{first_option}'")
                else:
                    # Generic string example
                    example_parts.append(f"'{req_field}': 'value'")
            
            example = f"[{{{', '.join(example_parts)}}}]"
            
            # Convert field_name to snake_case to match template usage
            field_name_snake = field_name.replace('-', '_')
            
            table_fields[field_name_snake] = {
                "mkey": mkey,
                "required_fields": required_fields,
                "example": example
            }
        
        return table_fields

    @staticmethod
    def extract_multivalue_option_fields(schema_data: dict[str, Any]) -> dict[str, dict[str, Any]]:
        """
        Extract metadata for multi-value option fields (space-separated strings).
        
        These fields have options (enum values) but multiple_values=True, meaning
        the API returns/accepts space-separated strings like "monday tuesday wednesday"
        instead of lists.
        
        Args:
            schema_data: Raw schema dictionary
            
        Returns:
            Dictionary mapping field names to their metadata:
            {
                "day": {
                    "options": ["sunday", "monday", "tuesday", ...],
                    "normalizer": "normalize_day_field"  # or None for generic
                }
            }
        """
        multivalue_fields = {}
        
        fields = schema_data.get("fields", {})
        for field_name, field_info in fields.items():
            # Check for multi-value option fields
            # - Must have options (enum-like)
            # - Must have multiple_values=True
            # - Must NOT be a table field (those are handled separately)
            has_options = bool(field_info.get("options"))
            is_multivalue = field_info.get("multiple_values", False)
            is_table = field_info.get("category") == "table"
            
            if has_options and is_multivalue and not is_table:
                # Extract option names
                options = []
                for opt in field_info.get("options", []):
                    if isinstance(opt, dict):
                        options.append(opt.get("name", ""))
                    else:
                        options.append(str(opt))
                options = [o for o in options if o]
                
                # Convert field_name to snake_case
                field_name_snake = field_name.replace('-', '_')
                
                # Determine which normalizer to use
                # For now, only 'day' fields get the specialized normalizer
                if field_name_snake == "day" and set(options) <= {
                    "sunday", "monday", "tuesday", "wednesday", 
                    "thursday", "friday", "saturday", "none"
                }:
                    normalizer = "normalize_day_field"
                else:
                    # Generic space-separated string - no special normalizer yet
                    normalizer = None
                
                multivalue_fields[field_name_snake] = {
                    "options": options,
                    "normalizer": normalizer,
                }
        
        return multivalue_fields

    @staticmethod
    def has_unitary_list_field_conflict(schema_data: dict[str, Any]) -> bool:
        """
        Check if schema has fields that would be incorrectly auto-normalized.
        
        The build_api_payload() function auto-normalizes certain field names
        (like 'interface', 'srcintf', etc.) to list format [{'name': '...'}].
        However, some endpoints have these field names as unitary (string) fields,
        not table (list) fields. This would cause XSS errors from FortiOS.
        
        Args:
            schema_data: Raw schema dictionary
            
        Returns:
            True if auto_normalize should be disabled for this endpoint
        """
        # Fields that build_api_payload auto-normalizes
        COMMON_LIST_FIELDS = {
            "srcintf", "dstintf", "srcaddr", "dstaddr", "srcaddr6", "dstaddr6",
            "service", "poolname", "poolname6", "groups", "users", "fsso_groups",
            "member", "interface", "allowaccess", "device", "gateway", "nexthop",
            "destination", "source", "application", "category", "group", "user",
            "ca", "certificate", "dns_server",
        }
        
        fields = schema_data.get("fields", {})
        for field_name, field_info in fields.items():
            field_name_snake = field_name.replace('-', '_')
            
            # Check if this field name would be auto-normalized
            if field_name_snake in COMMON_LIST_FIELDS:
                # Check if it's actually a unitary field (string), not a table (list)
                category = field_info.get("category", "")
                if category == "unitary":
                    # This field would be incorrectly normalized!
                    return True
        
        return False

    @staticmethod
    def load_overrides(overrides_file: str | Path | None = None) -> dict[str, Any]:
        """
        Load schema overrides from JSON file.
        
        Overrides allow manual corrections to schema metadata that cannot be
        auto-detected from FortiOS API documentation (e.g., scope corrections,
        readonly flags, etc.).
        
        Args:
            overrides_file: Path to overrides JSON file. If None, looks for
                          schema_overrides.json in the same directory as this module.
        
        Returns:
            Dictionary of overrides organized by category and endpoint path
        """
        import json
        from pathlib import Path
        
        if overrides_file is None:
            # Default: schema_overrides.json in same directory as this module
            module_dir = Path(__file__).parent
            overrides_file = module_dir / "schema_overrides.json"
        else:
            overrides_file = Path(overrides_file)
        
        if not overrides_file.exists():
            # No overrides file - return empty dict
            return {}
        
        try:
            with open(overrides_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data.get("overrides", {})
        except Exception as e:
            # Log warning but don't fail - overrides are optional
            print(f"Warning: Failed to load schema overrides from {overrides_file}: {e}")
            return {}

    @staticmethod
    def apply_overrides(schema: EndpointSchema, overrides: dict[str, Any]) -> EndpointSchema:
        """
        Apply manual overrides to a parsed schema.
        
        This allows fixing schema metadata that cannot be auto-detected from
        the API documentation.
        
        Args:
            schema: Parsed endpoint schema
            overrides: Overrides dict from load_overrides()
        
        Returns:
            Schema with overrides applied
        """
        if not overrides:
            return schema
        
        # Get overrides for this endpoint's category
        category_overrides = overrides.get(schema.category, {})
        if not category_overrides:
            return schema
        
        # Get overrides for this specific endpoint path
        # Try both api_path (with dots/dashes) and path (normalized)
        endpoint_overrides = category_overrides.get(schema.api_path)
        if not endpoint_overrides:
            endpoint_overrides = category_overrides.get(schema.path)
        if not endpoint_overrides:
            return schema
        
        # Apply each override
        if "scope" in endpoint_overrides:
            schema.scope = endpoint_overrides["scope"]
        
        if "scope_options" in endpoint_overrides:
            schema.scope_options = endpoint_overrides["scope_options"]
        
        if "readonly" in endpoint_overrides:
            schema.readonly = endpoint_overrides["readonly"]
        
        if "capabilities" in endpoint_overrides:
            # Override or merge capabilities
            # Format: {"features": {"vdom_scope": true, "versioning": false}, "methods": ["GET", "POST"]}
            capabilities_override = endpoint_overrides["capabilities"]
            if not schema.capabilities:
                schema.capabilities = {}
            
            # Deep merge - update existing sections or add new ones
            for section, section_data in capabilities_override.items():
                if section not in schema.capabilities:
                    schema.capabilities[section] = section_data
                elif isinstance(section_data, dict):
                    # Merge dict sections (like "features")
                    if not isinstance(schema.capabilities[section], dict):
                        schema.capabilities[section] = {}
                    schema.capabilities[section].update(section_data)
                else:
                    # Replace non-dict sections (like lists)
                    schema.capabilities[section] = section_data
        
        if "vdom_scope" in endpoint_overrides:
            # Backwards compatibility: Update capabilities.features.vdom_scope
            if not schema.capabilities:
                schema.capabilities = {}
            if "features" not in schema.capabilities:
                schema.capabilities["features"] = {}
            schema.capabilities["features"]["vdom_scope"] = endpoint_overrides["vdom_scope"]
        
        if "response_fields" in endpoint_overrides:
            # Parse response field definitions
            # Format: {"field_name": {"type": "string", "help": "...", ...}}
            from schema_management.schema_parser import SchemaParser
            response_fields_data = endpoint_overrides["response_fields"]
            schema.response_fields = {}
            for field_name, field_data in response_fields_data.items():
                # Use _parse_field_v1_7 format for consistency
                schema.response_fields[field_name] = SchemaParser._parse_field_v1_7(field_name, field_data)
        
        if "query_params" in endpoint_overrides:
            # Override or extend query parameters
            # Format: {"GET": {"param_name": {"type": "string", "required": false, ...}}}
            query_params_override = endpoint_overrides["query_params"]
            if not schema.query_params:
                schema.query_params = {}
            # Merge with existing query params
            for method, params in query_params_override.items():
                if method not in schema.query_params:
                    schema.query_params[method] = {}
                schema.query_params[method].update(params)
        
        # Log the override application for transparency
        reason = endpoint_overrides.get("reason", "No reason provided")
        print(f"  ✓ Applied override to {schema.category}/{schema.api_path}: {reason}")
        
        return schema
