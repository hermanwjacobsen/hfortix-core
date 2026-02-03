# Schema Override System

## Overview

The schema override system provides a flexible way to manually correct schema metadata that cannot be auto-detected from FortiOS API documentation. This is necessary because some metadata (like scope information) is missing or incorrect in the raw API responses.

## Why Overrides?

Schema files in `schema/` directory are **auto-generated** and not tracked by git. Manual edits to these files would be lost when schemas are regenerated. The override system solves this by:

1. **Persistence**: Overrides are stored in `schema_overrides.json`, which IS tracked by git
2. **Transparency**: Each override includes a reason explaining why it's needed
3. **Flexibility**: System supports overriding any schema field (scope, readonly, vdom_scope, etc.)
4. **Automatic**: Overrides are applied automatically during schema parsing

## Override File Structure

The `schema_overrides.json` file has this structure:

```json
{
  "overrides": {
    "monitor": {
      "system/config-script": {
        "scope": "global",
        "reason": "Configuration scripts operate at global scope..."
      }
    },
    "cmdb": {},
    "service": {},
    "log": {}
  }
}
```

### Supported Fields

You can override these fields in `EndpointSchema`:

- **`scope`**: Endpoint scope (`"global"`, `"vdom"`, or `"unknown"`)
- **`scope_options`**: List of valid scope options (`["global"]`, `["vdom"]`, or `["global", "vdom"]`)
- **`readonly`**: Whether endpoint is read-only (`true` or `false`)
- **`capabilities`**: Full capabilities object - deep merged with existing (see below)
- **`vdom_scope`**: Shorthand for `capabilities.features.vdom_scope` (`true` or `false`)
- **`response_fields`**: Define response field structure for monitor/service endpoints
- **`query_params`**: Add or override query parameters by HTTP method (GET, POST, etc.)
- Additional fields can be added as needed

### Path Matching

Overrides match endpoints by their API path. The system tries both:
- `api_path`: Original API path (e.g., `"system/config-script"`)
- `path`: Normalized Python path (e.g., `"system/config_script"`)

## Adding New Overrides

1. Edit `.dev/generator/schema_management/schema_overrides.json`
2. Add entry under the appropriate category (`monitor`, `cmdb`, `service`, `log`)
3. Use the endpoint's API path as the key
4. Specify the field(s) to override and include a `reason`

### Example: Simple Scope Override

```json
{
  "overrides": {
    "monitor": {
      "system/example-endpoint": {
        "scope": "global",
        "readonly": true,
        "reason": "This endpoint operates at global scope and is read-only"
      }
    }
  }
}
```

### Example: Adding Response Fields to Monitor Endpoints

Many monitor endpoints return data but lack schema definitions for the response structure. You can add response field definitions via overrides:

```json
{
  "overrides": {
    "monitor": {
      "system/status": {
        "response_fields": {
          "version": {
            "type": "string",
            "help": "FortiOS version string",
            "required": true
          },
          "serial": {
            "type": "string", 
            "help": "Device serial number",
            "required": true
          },
          "hostname": {
            "type": "string",
            "help": "Configured hostname",
            "required": false
          }
        },
        "reason": "Monitor endpoint lacks response field definitions in API schema"
      }
    }
  }
}
```

The response fields use the same format as regular schema fields, supporting:
- `type`: Field type (string, integer, option, etc.)
- `help`: Description text
- `required`: Whether field is always present
- `options`: Enum values for option types
- `children`: Nested object structure
- `default`: Default value
- All other `FieldMetadata` attributes

### Example: Adding Query Parameters

You can also add or override query parameters that aren't documented in the schema:

```json
{
  "overrides": {
    "cmdb": {
      "firewall/policy": {
        "query_params": {
          "GET": {
            "policyid": {
              "type": "integer",
              "required": false,
              "description": "Filter results by specific policy ID"
            },
            "format": {
              "type": "string",
              "required": false,
              "description": "Output format",
              "allowed_values": ["json", "xml"]
            }
          }
        },
        "reason": "Additional query parameters not in auto-generated schema"
      }
    }
  }
}
```

### Example: Comprehensive Capabilities Override

The capabilities object contains metadata about what the endpoint supports. You can override any part of it:

**Capabilities Structure:**
- `endpoint_type`: "collection" | "singleton" | "action"
- `crud`: create, read, update, delete flags
- `actions`: move, clone flags
- `features`: filtering, pagination, vdom_scope, etc.
- `limits`: max_table_size_vdom, max_table_size_global

**Example Override:**

```json
{
  "overrides": {
    "cmdb": {
      "system/admin": {
        "capabilities": {
          "endpoint_type": "collection",
          "crud": {
            "create": true,
            "read": true,
            "update": true,
            "delete": true
          },
          "actions": {
            "move": false,
            "clone": false
          },
          "features": {
            "filtering": true,
            "pagination": true,
            "vdom_scope": false,
            "member_tables": 2
          },
          "limits": {
            "max_table_size_global": 256
          }
        },
        "reason": "Admin endpoint has incorrect capabilities in auto-generated schema"
      }
    }
  }
}
```

The `capabilities` object is **deep-merged**, meaning:
- New sections (e.g., adding `limits`) are added
- Existing dict sections (e.g., `features`, `crud`) are merged with your updates
- You only need to specify the fields you want to change
- Non-dict sections are replaced entirely

**Example: Partial Override (only change what you need):**

```json
{
  "capabilities": {
    "features": {
      "vdom_scope": false,
      "filtering": false
    }
  }
}
```

This will only update `features.vdom_scope` and `features.filtering`, leaving all other capabilities unchanged.

### Example: Read-Only Reference Table

Mark geography and other reference tables as read-only:

```json
{
  "overrides": {
    "cmdb": {
      "system/geography/country": {
        "readonly": true,
        "reason": "Geography reference tables are read-only - cannot be modified"
      }
    }
  }
}
```

## How It Works

1. **Loading**: Overrides are loaded once when `SchemaParser` module is imported
2. **Parsing**: When parsing a schema, the system checks for matching overrides
3. **Application**: If found, override values replace the parsed values
4. **Logging**: Override application is logged to console for transparency

### Code Flow

```python
# In schema_parser.py
schema = EndpointSchema(...)  # Create schema from parsed JSON

# Apply overrides automatically
if not hasattr(SchemaParser, '_overrides_cache'):
    SchemaParser._overrides_cache = SchemaParser.load_overrides()
schema = SchemaParser.apply_overrides(schema, SchemaParser._overrides_cache)

return schema
```

## Testing Overrides

Test that your override works:

```python
import json
from schema_management.schema_parser import SchemaParser

# Load schema
with open('schema/7.6.5/monitor/system.config-script.json') as f:
    schema_json = json.load(f)

# Parse (overrides applied automatically)
schema = SchemaParser.parse(schema_json, 'schema/7.6.5/monitor/system.config-script.json')

# Verify override worked
print(f'Scope: {schema.scope}')  # Should be "global" if override applied
```

## Current Overrides

See `schema_overrides.json` for the current list of overrides. As of this writing:

- **system/config-script** endpoints (4 total): `scope` corrected from `"unknown"` to `"global"`

## Future Extensions

The override system is designed to be extensible. You can add support for:

- Field-level overrides (e.g., mark specific fields as required)
- Validation rule overrides (e.g., custom min/max values)
- Deprecation information
- Custom query parameter definitions
- Relationship mappings

To add a new override type, simply:
1. Add the field to the override JSON
2. Update `SchemaParser.apply_overrides()` to handle the new field
