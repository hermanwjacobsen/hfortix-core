# Code Generator Fix Summary - January 6, 2026

## Problem
42 monitor endpoint tests were failing with `AttributeError: 'X' object has no attribute 'get'`

Example: `ApplicationList` object had no `get` method.

## Root Cause
The code generator was creating **naming conflicts** when an endpoint had both:
1. A base endpoint file (e.g., `application_list.py`) 
2. A subdirectory with action endpoints (e.g., `application_list/refresh.py`)

Python's import system prioritized the **directory** over the **.py file**, causing circular import issues.

## Solution - 3-Part Fix

### 1. **Renamed Base Files to `*_base.py` Pattern**
- Changed: `application_list.py` → `application_list_base.py`
- Applied to all 21 affected endpoints
- This prevents Python package/module naming conflicts

### 2. **Updated Generator Templates** 
Fixed `.dev/generator/generators/regenerate_init_files.py`:

**Before:**
```python
# This caused circular import!
from ..application_list import ApplicationList as ApplicationListBase
```

**After:**
```python
# Clean import from _base.py file
from ..application_list_base import ApplicationList as ApplicationListBase
```

### 3. **Verified Endpoint Generator Logic**
The main generator (`.dev/generator/generators/endpoint_generator.py`) already had correct logic:
- Detects when endpoints will have subdirectories
- Automatically uses `_base.py` naming for those endpoints
- This was working correctly all along!

## Affected Endpoints (21 total)
All monitor category endpoints with action sub-endpoints:

```
monitor/azure/application_list
monitor/extender_controller/extender
monitor/firewall/gtp
monitor/firewall/multicast_policy
monitor/firewall/per_ip_shaper
monitor/router/lookup
monitor/system/botnet
monitor/system/dhcp
monitor/system/ha_peer
monitor/system/modem
monitor/system/usb_log
monitor/firewall/acl6
monitor/system/time
monitor/user/proxy
monitor/utm/blacklisted_certificates
monitor/wanopt/webcache
monitor/wanopt/peer_stats
monitor/webfilter/category_quota
monitor/webfilter/malicious_urls
monitor/webfilter/override
monitor/wifi/rogue_ap
```

## File Structure (Example: application_list)

### Before (Broken):
```
monitor/azure/
  ├── application_list.py          # Base class with get() method
  └── application_list/             # Directory (shadows the .py file!)
      ├── __init__.py               # Tried to import from ..application_list (circular!)
      └── refresh.py                # Action endpoint
```

### After (Fixed):
```
monitor/azure/
  ├── application_list_base.py     # Base class with get() method
  └── application_list/            # Directory (no conflict)
      ├── __init__.py              # from ..application_list_base import ApplicationList
      └── refresh.py               # Action endpoint
```

## Generated `__init__.py` Structure

```python
"""FortiOS CMDB - ApplicationList category"""

from ..application_list_base import ApplicationList as ApplicationListBase
from .refresh import Refresh

__all__ = [
    "ApplicationList",
    "Refresh",
]


class ApplicationList(ApplicationListBase):
    """ApplicationList endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """ApplicationList endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        super().__init__(client)  # Initialize base class with GET methods
        self.refresh = Refresh(client)
```

## Benefits of This Pattern

✅ **No circular imports** - `_base.py` files can't be shadowed by directories  
✅ **Clear inheritance** - Wrapper classes explicitly inherit from base  
✅ **Predictable** - Same pattern for all endpoints with sub-actions  
✅ **Standard Python** - Follows common base class naming conventions  
✅ **Future-proof** - Generator automatically handles this for new endpoints

## Regeneration Commands

```bash
cd /app/dev/classes/fortinet/.dev/generator

# Regenerate specific category
python generate.py --category monitor

# Regenerate all categories
python generate.py --all

# Regenerate specific endpoint
python generate.py --endpoint monitor.azure.application-list
```

## Test Results
- **Before**: 42 failures (AttributeError: 'X' object has no attribute 'get')
- **After**: All tests pass or skip (feature not enabled on test server)

## Files Modified

### Generator Code:
- `.dev/generator/generators/regenerate_init_files.py` - Fixed import pattern (line 86)

### Generated Code (All 21 endpoints):
- Renamed 21 `*.py` files to `*_base.py`
- Renamed 21 `*.pyi` files to `*_base.pyi`  
- Regenerated 21 `__init__.py` wrapper files with correct imports

## Key Takeaway
**Don't fix generated code manually - fix the generator!** This ensures:
1. Consistent patterns across all endpoints
2. Future endpoints are generated correctly
3. Regeneration doesn't break existing fixes
