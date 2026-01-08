# Refactoring Overloads - Deduplication Guide

## Problem

Every generated endpoint class repeats ~20-30 `@overload` decorators for CRUD operations:
- 6 overloads for `get()`
- 4 overloads for `post()`
- 4 overloads for `put()`
- 4 overloads for `delete()`

This creates:
- **Massive code duplication** across hundreds of files
- **Maintenance burden** - changes must be replicated everywhere
- **Larger file sizes** - affects load time and repository size

## Solution

Use **Protocol inheritance** to define overloads once, inherit everywhere.

### Benefits

✅ **Autocomplete preserved** - IDEs see inherited overloads  
✅ **Type checking works** - mypy/pyright respect protocol overloads  
✅ **Zero runtime cost** - protocols are compile-time only  
✅ **90% less code** - overloads defined once in `_protocols.py`  
✅ **Easier maintenance** - change overloads in one place  

## Implementation

### Step 1: Create Protocol Definitions

**File: `packages/fortios/hfortix_fortios/_protocols.py`** (already created)

```python
from typing import Protocol, overload, Literal, Any

class GetProtocol(Protocol):
    @overload
    def get(self, name: str, ..., response_mode: Literal["object"]) -> FortiObject: ...
    @overload
    def get(self, name: None, ..., response_mode: Literal["object"]) -> list[FortiObject]: ...
    # ... all other overloads
```

### Step 2: Update Generated Classes

**BEFORE** (87 lines of overloads):
```python
class Profile(MetadataMixin):
    # Overload for response_mode="object" with mkey provided (single object)
    @overload
    def get(
        self,
        name: str,
        filter: list[str] | None = None,
        count: int | None = None,
        start: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: Literal[False] = False,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> FortiObject: ...
    
    # Overload for response_mode="object" without mkey (list of objects)
    @overload
    def get(
        self,
        name: None = None,
        # ... 15 more lines
    ) -> list[FortiObject]: ...
    
    # ... 4 more overloads for get()
    # ... 4 overloads for post()
    # ... 4 overloads for put()
    # ... 4 overloads for delete()
    
    def get(self, name: str | None = None, ...):  # Actual implementation
        # Implementation code
```

**AFTER** (no overloads needed):
```python
from hfortix_fortios._protocols import GetProtocol, PostProtocol, PutProtocol, DeleteProtocol

class Profile(GetProtocol, PostProtocol, PutProtocol, DeleteProtocol, MetadataMixin):
    """Profile Operations."""
    
    # No @overload decorators needed - inherited from protocols!
    
    def get(self, name: str | None = None, ...):  # Actual implementation
        """Retrieve voip/profile configuration."""
        # Implementation code (unchanged)
        
    def post(self, payload_dict: dict[str, Any] | None = None, ...):
        """Create new voip/profile object."""
        # Implementation code (unchanged)
        
    def put(self, payload_dict: dict[str, Any] | None = None, ...):
        """Update existing voip/profile object."""
        # Implementation code (unchanged)
        
    def delete(self, name: str | None = None, ...):
        """Delete voip/profile object."""
        # Implementation code (unchanged)
```

### Step 3: Alternative - Use Combined Protocol

Even simpler:
```python
from hfortix_fortios._protocols import CRUDEndpoint

class Profile(CRUDEndpoint, MetadataMixin):
    """Profile Operations."""
    
    def get(self, name: str | None = None, ...):
        # Implementation
    
    def post(self, payload_dict: dict[str, Any] | None = None, ...):
        # Implementation
        
    # etc.
```

## Important Notes

### Protocols vs. ABC/Mixin

**Why Protocol instead of ABC or Mixin?**

```python
# ❌ ABC/Mixin approach - requires implementing abstract methods
class CRUDMixin(ABC):
    @abstractmethod
    def get(self, ...): ...  # Must implement in subclass
    
# ✅ Protocol approach - just defines interface
class GetProtocol(Protocol):
    @overload
    def get(self, ...): ...  # No implementation needed
```

Protocols are **structural typing** - they just say "if a class has this method signature, it matches this protocol". Perfect for our use case.

### Overload Parameters Must Match

The protocol overloads must have **compatible** parameter names with the actual implementation, but:
- ✅ Implementation can add endpoint-specific parameters
- ✅ Protocol provides the common parameters

Example:
```python
# Protocol defines common parameters
class PostProtocol(Protocol):
    @overload
    def post(self, payload_dict: dict | None = None, vdom: str | None = None, ...): ...

# Implementation can add specific parameters
class FirewallPolicy(PostProtocol):
    def post(
        self, 
        payload_dict: dict | None = None,
        # Endpoint-specific parameters:
        policyid: int | None = None,
        srcintf: str | None = None,
        dstintf: str | None = None,
        # Common parameters:
        vdom: str | None = None,
        **kwargs
    ):
        # Implementation
```

### Endpoint-Specific Overloads

Some endpoints may need **additional overloads** beyond the common ones:

```python
class SpecialEndpoint(CRUDEndpoint, MetadataMixin):
    """Endpoint with special overloads."""
    
    # Inherits common CRUD overloads from CRUDEndpoint
    
    # Add endpoint-specific overload
    @overload
    def get(self, name: str, special_param: Literal[True]) -> SpecialObject: ...
    
    def get(self, name: str | None = None, special_param: bool = False, ...):
        # Implementation handles both common and special cases
```

Type checkers will see **both** the inherited overloads and the class-specific ones.

## Generator Changes

Update your endpoint generator to:

1. **Import protocols** at the top:
   ```python
   from hfortix_fortios._protocols import CRUDEndpoint
   ```

2. **Inherit from CRUDEndpoint**:
   ```python
   class {ClassName}(CRUDEndpoint, MetadataMixin):
   ```

3. **Remove all `@overload` decorators** for standard CRUD methods

4. **Keep only the implementation** methods

## Testing

After refactoring:

```bash
# Type check still works
cd packages/fortios
mypy hfortix_fortios/

# Tests still pass
pytest

# IDE autocomplete still works
# (Open any file and test `fgt.api.cmdb.voip_profile.get(` - should see all overloads)
```

## Migration Strategy

### Option 1: Gradual Migration

1. Create `_protocols.py` ✅ (done)
2. Pick one endpoint, update it to use protocols
3. Test thoroughly
4. Update generator to use protocols for new files
5. Optionally: Bulk update existing files

### Option 2: Generator-Only

1. Create `_protocols.py` ✅ (done)
2. Update generator immediately
3. All **new** generated files use protocols
4. Leave existing files as-is (they still work)

## File Size Comparison

**Before** (with repeated overloads):
```
profile.py: 949 lines
  - ~87 lines of overloads
  - ~862 lines of actual code
```

**After** (with protocol inheritance):
```
profile.py: ~862 lines (9% smaller)
  - 0 lines of overloads (inherited)
  - ~862 lines of actual code
  
_protocols.py: ~300 lines (shared across ALL endpoints)
```

For 500 endpoints:
- **Before**: 500 × 87 = 43,500 lines of duplicate overloads
- **After**: 1 × 300 = 300 lines of shared overloads
- **Savings**: 43,200 lines (99.3% reduction)

## Advanced: Parameter-Specific Protocols

For endpoints with different parameter sets:

```python
# _protocols.py
from typing import TypeVar, Generic

MKeyT = TypeVar('MKeyT', bound=str | int)

class GetWithMKey(Protocol[MKeyT]):
    @overload
    def get(self, name: MKeyT, ...) -> FortiObject: ...
    @overload
    def get(self, name: None, ...) -> list[FortiObject]: ...
```

## Questions?

- **Q: Does this affect runtime performance?**  
  A: No. Protocols are purely type-checking constructs. Zero runtime overhead.

- **Q: Will my IDE still show autocomplete?**  
  A: Yes! Modern IDEs (VSCode, PyCharm) respect protocol overloads.

- **Q: Can I mix protocols and local overloads?**  
  A: Yes! Add endpoint-specific overloads on top of inherited ones.

- **Q: What if mypy doesn't see the inherited overloads?**  
  A: Make sure you're using mypy 0.990+ which has full Protocol support.

## Recommendation

✅ **Use `CRUDEndpoint` protocol for all generated endpoints**

This gives you:
- Maximum code reduction
- Consistent type hints
- Easy maintenance
- Full IDE support
