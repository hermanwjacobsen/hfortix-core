# Naming Collision Solution

## The Problem

When FortiOS has endpoints like:
- `/monitor/azure/application-list` (main endpoint)
- `/monitor/azure/application-list/refresh` (sub-endpoint)

Python's import system creates a collision:
- `application_list.py` (module file)
- `application_list/` (package directory)

**Python ALWAYS imports the package, shadowing the module!**

## The Solution: Universal `_base` Suffix

For **any** endpoint that has sub-endpoints, we use the `_base` suffix pattern:

### File Structure
```
monitor/azure/
  ├── application_list_base.py      # Base class with main endpoint methods
  └── application_list/
      ├── __init__.py                # Wrapper: class ApplicationList(ApplicationListBase)
      └── refresh.py                 # Sub-endpoint
```

### Code Pattern
```python
# application_list_base.py
class ApplicationList:
    def __init__(self, client):
        self._client = client
    
    def get(self, ...):
        # Main endpoint implementation
        pass

# application_list/__init__.py  
from ..application_list_base import ApplicationList as ApplicationListBase
from .refresh import Refresh

class ApplicationList(ApplicationListBase):
    def __init__(self, client):
        super().__init__(client)  # Get base methods (get, etc.)
        self.refresh = Refresh(client)  # Add sub-endpoints
```

## Why This Works

✅ **No Name Collisions**: `application_list_base.py` ≠ `application_list/`  
✅ **Simple**: Standard Python inheritance pattern  
✅ **Predictable**: Same approach every time  
✅ **Maintainable**: Generator logic is straightforward  
✅ **Extensible**: Easy to add more sub-endpoints  

## Generator Implementation

1. **Endpoint Generator** (`endpoint_generator.py`):
   - Detects if endpoint will have sub-endpoints
   - Uses `_base.py` suffix automatically
   
2. **Init Generator** (`regenerate_init_files.py`):
   - Finds `_base.py` + matching directory
   - Generates wrapper `__init__.py` with inheritance

## For Future Developers

If you see `something_base.py` + `something/` directory:
- The `_base.py` file contains the main class
- The `something/__init__.py` inherits from base and adds sub-endpoints
- This pattern prevents Python import shadowing
- **Do NOT** create files and directories with the same name!
