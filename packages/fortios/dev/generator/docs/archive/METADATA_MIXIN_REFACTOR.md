# Metadata Mixin Refactoring

## Overview

Refactored duplicate metadata helper methods from all endpoint classes into a shared `MetadataMixin` base class.

## Problem

Every generated endpoint class (e.g., `Settings`, `Policy`, etc.) had identical implementations of 7 metadata helper methods:
- `help()`
- `fields()`
- `field_info()`
- `validate_field()`
- `required_fields()`
- `defaults()`
- `schema()`

This resulted in:
- **~200 lines of duplicate code** per endpoint class
- Maintenance burden across hundreds of endpoint files
- Inconsistency risk when updating method signatures

## Solution

Created `MetadataMixin` base class in `hfortix_fortios/_helpers/metadata_mixin.py` that:
1. Provides all 7 metadata helper methods as class methods
2. Uses dynamic import based on `_helper_module_name` class attribute
3. Allows each endpoint class to specify its own helper module

## Changes Made

### 1. Created MetadataMixin
**File:** `packages/fortios/hfortix_fortios/_helpers/metadata_mixin.py`

```python
class MetadataMixin:
    """Mixin providing metadata helper methods for FortiOS API endpoint classes."""
    
    _helper_module_name: str = ""
    
    @classmethod
    def _get_helper_module(cls) -> ModuleType:
        """Get the helper module for this endpoint class."""
        # ... dynamically imports ._helpers.{_helper_module_name}
    
    @classmethod
    def help(cls, field_name: str | None = None) -> str:
        """Get help text for endpoint or specific field."""
        # ... implementation using _get_helper_module()
    
    # ... other 6 methods
```

### 2. Updated Generator Template
**File:** `.dev/generator/templates/endpoint_class.py.j2`

**Before:**
```python
class {{ schema.class_name }}:
    """{{ schema.class_name }} Operations."""
    
    # ... 200+ lines of metadata methods
```

**After:**
```python
from hfortix_fortios._helpers.metadata_mixin import MetadataMixin

class {{ schema.class_name }}(MetadataMixin):
    """{{ schema.class_name }} Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "{{ schema.file_name }}"
    
    # ... only CRUD methods (get, post, put, delete, etc.)
```

**Removed:** ~200 lines of metadata helper method implementations per endpoint

### 3. Updated _helpers __init__.py
**File:** `packages/fortios/hfortix_fortios/_helpers/__init__.py`

Added export:
```python
from hfortix_fortios._helpers.metadata_mixin import MetadataMixin

__all__ = [
    # ...
    "MetadataMixin",
    # ...
]
```

### 4. Updated Example Endpoint
**File:** `packages/fortios/hfortix_fortios/api/v2/cmdb/antivirus/settings.py`

Converted to use the mixin as proof of concept:
```python
from hfortix_fortios._helpers.metadata_mixin import MetadataMixin

class Settings(MetadataMixin):
    _helper_module_name = "settings"
    # ... CRUD methods only (removed all metadata methods)
```

## Benefits

### Code Reduction
- **Before:** ~200 lines of metadata methods per endpoint × hundreds of endpoints
- **After:** Single shared implementation in MetadataMixin (~300 lines total)
- **Savings:** Thousands of lines of duplicate code eliminated

### Maintainability
- Single source of truth for metadata method implementations
- Changes to method signatures only need to be made once
- Consistent behavior across all endpoints

### Backward Compatibility
- All existing code continues to work without changes
- Method signatures remain identical
- Return types unchanged

### Performance
- Minimal overhead (dynamic import is cached by Python)
- Methods only import helper module when called
- No runtime performance impact

## Usage

Endpoint classes automatically inherit all metadata methods:

```python
from hfortix_fortios import FortiOS

fgt = FortiOS(host="192.168.1.99", token="token")

# All these methods work the same as before
Settings.help()                              # Endpoint info
Settings.help("machine-learning-detection")  # Field info
Settings.fields()                            # List of field names
Settings.fields(detailed=True)               # Detailed field metadata
Settings.field_info("field-name")            # Single field metadata
Settings.validate_field("field-name", "val") # Field validation
Settings.required_fields()                   # List of required fields
Settings.defaults()                          # Dict of default values
Settings.schema()                            # Complete schema info
```

## Migration Path

### For New Code Generation
The updated template automatically generates endpoints with MetadataMixin inheritance.

### For Existing Endpoint Files
**Option 1: Regenerate all endpoints** (Recommended)
```bash
cd .dev/generator
python generate.py --all --version 7.6.5
```

**Option 2: Gradual migration**
1. New endpoints automatically use mixin
2. Old endpoints continue to work with embedded methods
3. Regenerate endpoints as needed

## Testing

Verified with `Settings` class:
```python
from packages.fortios.hfortix_fortios.api.v2.cmdb.antivirus.settings import Settings

Settings.help()           # ✅ Works
Settings.fields()         # ✅ Works
Settings.schema()         # ✅ Works
# ... all 7 methods tested and working
```

## Implementation Notes

### Why Class Methods Instead of Static Methods?
Using `@classmethod` allows us to access `cls._helper_module_name` to determine which helper module to import. Static methods don't have access to the class.

### Helper Module Structure
Each endpoint still has its own `_helpers/<endpoint_name>.py` file with:
- `get_schema_info()`
- `get_field_metadata(field_name)`
- `get_all_fields()`
- `validate_field_value(field_name, value)`
- `REQUIRED_FIELDS`
- `FIELDS_WITH_DEFAULTS`
- `DEPRECATED_FIELDS` (optional)

The mixin just provides a consistent interface to access these.

### Type Stubs (.pyi files)
The `.pyi` template already declares the method signatures, so type checking remains accurate even though methods are inherited from the mixin.

## Related Files

- `packages/fortios/hfortix_fortios/_helpers/metadata_mixin.py` - Mixin implementation
- `.dev/generator/templates/endpoint_class.py.j2` - Updated template
- `packages/fortios/hfortix_fortios/_helpers/__init__.py` - Export added
- `packages/fortios/hfortix_fortios/api/v2/cmdb/antivirus/settings.py` - Example conversion

## Future Enhancements

Potential improvements:
1. Cache helper module imports to avoid repeated imports
2. Add type hints to mixin methods
3. Consider additional common methods that could be moved to mixin
4. Generate API documentation from mixin methods

---

**Status:** ✅ Implemented and tested  
**Date:** January 6, 2026  
**Impact:** All endpoint classes (when regenerated)
