# Generic request() Method - Quick Start Guide

## Overview

The new `request()` method allows you to execute FortiGate API calls using the exact JSON format from the FortiGate GUI's **API preview** feature. This makes it incredibly easy to test and implement API calls.

## Usage

### Basic Example

```python
from hfortix import FortiOS

fgt = FortiOS(host="192.168.1.99", token="your-api-token")

# Copy this JSON directly from FortiGate GUI API preview
config = {
    "method": "POST",
    "url": "/api/v2/cmdb/firewall/address",
    "params": {
        "vdom": "test"
    },
    "data": {
        "name": "test999999",
        "subnet": "192.168.1.0/24",
        "color": "0"
    }
}

# Execute the request
result = fgt.request(config)
```

## Supported Operations

### 1. CREATE (POST)

```python
config = {
    "method": "POST",
    "url": "/api/v2/cmdb/firewall/address",
    "params": {"vdom": "root"},
    "data": {
        "name": "my-host",
        "subnet": "10.0.0.10/32"
    }
}
result = fgt.request(config)
```

### 2. READ (GET)

```python
# Get all addresses
config = {
    "method": "GET",
    "url": "/api/v2/cmdb/firewall/address",
    "params": {"vdom": "root"}
}
result = fgt.request(config)

# Get specific address
config = {
    "method": "GET",
    "url": "/api/v2/cmdb/firewall/address/my-host",
    "params": {"vdom": "root"}
}
result = fgt.request(config)
```

### 3. UPDATE (PUT)

```python
config = {
    "method": "PUT",
    "url": "/api/v2/cmdb/firewall/address/my-host",
    "params": {"vdom": "root"},
    "data": {
        "comment": "Updated via API",
        "color": "10"
    }
}
result = fgt.request(config)
```

### 4. DELETE

```python
config = {
    "method": "DELETE",
    "url": "/api/v2/cmdb/firewall/address/my-host",
    "params": {"vdom": "root"}
}
result = fgt.request(config)
```

## How to Get JSON from FortiGate GUI

1. **Navigate** to any configuration page in FortiGate GUI
2. **Click** the object you want to create/modify
3. **Click** the "API Preview" button (usually in top-right corner)
4. **Copy** the JSON configuration shown
5. **Paste** it directly into your Python code as the `config` parameter

## Parameters

- **config** (dict, required): The API request configuration
  - `method`: HTTP method (GET, POST, PUT, DELETE)
  - `url`: Full API URL path (e.g., `/api/v2/cmdb/firewall/address`)
  - `params`: Optional query parameters (datasource, vdom, etc.)
  - `data`: Request body for POST/PUT operations

- **raw_json** (bool, optional): Default `False`
  - `False`: Returns only the results data
  - `True`: Returns full API response with metadata

## Complete CRUD Example

```python
from hfortix import FortiOS

fgt = FortiOS(host="192.168.1.99", token="your-api-token")

# 1. CREATE
create_config = {
    "method": "POST",
    "url": "/api/v2/cmdb/firewall/address",
    "params": {"vdom": "root"},
    "data": {
        "name": "webserver",
        "subnet": "203.0.113.10/32",
        "comment": "Production web server"
    }
}
fgt.request(create_config)

# 2. READ
read_config = {
    "method": "GET",
    "url": "/api/v2/cmdb/firewall/address/webserver",
    "params": {"vdom": "root"}
}
address = fgt.request(read_config)
print(address)

# 3. UPDATE
update_config = {
    "method": "PUT",
    "url": "/api/v2/cmdb/firewall/address/webserver",
    "params": {"vdom": "root"},
    "data": {
        "comment": "Updated: Production web server (primary)"
    }
}
fgt.request(update_config)

# 4. DELETE
delete_config = {
    "method": "DELETE",
    "url": "/api/v2/cmdb/firewall/address/webserver",
    "params": {"vdom": "root"}
}
fgt.request(delete_config)
```

## Error Handling

The method validates:
- ✓ Required fields (method, url)
- ✓ Valid HTTP methods (GET, POST, PUT, DELETE)
- ✓ Correct URL format (must start with `/api/v2/`)
- ✓ Required data for POST/PUT operations

```python
# This will raise ValueError
config = {
    "method": "POST",
    "url": "/api/v2/cmdb/firewall/address",
    # Missing 'data' field - will raise error
}
fgt.request(config)  # ValueError: POST requests require 'data' field
```

## Running Tests

The comprehensive test suite validates all functionality:

```bash
# Run tests (requires pytest)
cd .dev/pytests
python3 other/request-module.py

# Or with pytest
pytest other/request-module.py -v
```

## Benefits

1. **Zero Translation** - Copy JSON directly from GUI, no manual conversion
2. **Quick Testing** - Test API calls in GUI, then paste to code
3. **Universal** - Works with all FortiOS API endpoints
4. **Simple** - Single method for all CRUD operations
5. **Validated** - Automatic validation of request format

## Files Modified

- **`packages/fortios/hfortix_fortios/client.py`**: Added `request()` method (line ~960)
- **`.dev/pytests/other/request-module.py`**: Complete test suite with CRUD examples

## Next Steps

1. Test with your FortiGate using the examples above
2. Use GUI API preview to generate JSON for complex configurations
3. Run the test suite to validate functionality
4. Check out other endpoints in FortiOS API documentation
