# Visual Comparison: Before vs After Refactoring

## Current State (WITH repeated overloads)

```python
from typing import overload, Literal, Any

class Profile(MetadataMixin):
    """Profile Operations."""
    
    # ❌ 87 lines of overloads for get() - REPEATED IN EVERY ENDPOINT
    @overload
    def get(self, name: str, ..., response_mode: Literal["object"] = ...) -> FortiObject: ...
    @overload
    def get(self, name: None = None, ..., response_mode: Literal["object"] = ...) -> list[FortiObject]: ...
    @overload
    def get(self, name: str, ..., response_mode: Literal["dict"] = ...) -> dict[str, Any]: ...
    @overload
    def get(self, name: None = None, ..., response_mode: Literal["dict"] = ...) -> dict[str, Any]: ...
    @overload
    def get(self, name: str | None = None, ...) -> dict[str, Any] | FortiObject | list[FortiObject]: ...
    @overload
    def get(self, name: str | None = None, ..., raw_json: Literal[True] = ...) -> dict[str, Any]: ...
    
    def get(self, name: str | None = None, ...):  # ✅ Actual implementation
        """Retrieve voip/profile configuration."""
        # ... implementation code
    
    # ❌ 67 lines of overloads for put() - REPEATED IN EVERY ENDPOINT
    @overload
    def put(self, payload_dict: dict | None = None, ..., response_mode: Literal["object"] = ...) -> FortiObject: ...
    @overload
    def put(self, payload_dict: dict | None = None, ..., response_mode: Literal["dict"] = ...) -> dict[str, Any]: ...
    @overload
    def put(self, payload_dict: dict | None = None, ..., raw_json: Literal[True] = ...) -> dict[str, Any]: ...
    @overload
    def put(self, payload_dict: dict | None = None, ...) -> dict[str, Any] | FortiObject: ...
    
    def put(self, payload_dict: dict | None = None, ...):  # ✅ Actual implementation
        """Update existing voip/profile object."""
        # ... implementation code
    
    # ❌ 67 lines of overloads for post() - REPEATED IN EVERY ENDPOINT
    @overload
    def post(self, payload_dict: dict | None = None, ..., response_mode: Literal["object"] = ...) -> FortiObject: ...
    @overload
    def post(self, payload_dict: dict | None = None, ..., response_mode: Literal["dict"] = ...) -> dict[str, Any]: ...
    @overload
    def post(self, payload_dict: dict | None = None, ..., raw_json: Literal[True] = ...) -> dict[str, Any]: ...
    @overload
    def post(self, payload_dict: dict | None = None, ...) -> dict[str, Any] | FortiObject: ...
    
    def post(self, payload_dict: dict | None = None, ...):  # ✅ Actual implementation
        """Create new voip/profile object."""
        # ... implementation code
    
    # ❌ 42 lines of overloads for delete() - REPEATED IN EVERY ENDPOINT
    @overload
    def delete(self, name: str, ..., response_mode: Literal["object"] = ...) -> FortiObject: ...
    @overload
    def delete(self, name: str, ..., response_mode: Literal["dict"] = ...) -> dict[str, Any]: ...
    @overload
    def delete(self, name: str, ..., raw_json: Literal[True] = ...) -> dict[str, Any]: ...
    @overload
    def delete(self, name: str, ...) -> dict[str, Any] | FortiObject: ...
    
    def delete(self, name: str | None = None, ...):  # ✅ Actual implementation
        """Delete voip/profile object."""
        # ... implementation code
```

**Total:** ~263 lines of overload boilerplate per endpoint  
**For 500 endpoints:** 131,500 lines of duplicate code! 🤯

---

## Refactored State (WITHOUT repeated overloads)

```python
from hfortix_fortios._protocols import CRUDEndpoint

class Profile(CRUDEndpoint, MetadataMixin):  # ✨ Inherits all overloads
    """Profile Operations."""
    
    # ✅ No overloads needed - all inherited from CRUDEndpoint!
    
    def get(self, name: str | None = None, ...):  # ✅ Implementation only
        """Retrieve voip/profile configuration."""
        # ... implementation code
    
    def put(self, payload_dict: dict | None = None, ...):  # ✅ Implementation only
        """Update existing voip/profile object."""
        # ... implementation code
    
    def post(self, payload_dict: dict | None = None, ...):  # ✅ Implementation only
        """Create new voip/profile object."""
        # ... implementation code
    
    def delete(self, name: str | None = None, ...):  # ✅ Implementation only
        """Delete voip/profile object."""
        # ... implementation code
```

**Total:** 0 lines of overload boilerplate per endpoint  
**For 500 endpoints:** 0 lines of duplicate code! ✨

---

## Side-by-Side File Size Comparison

### Before: `profile.py` (949 lines)
```
Lines   1-77:   Module docstring, imports, class definition
Lines  78-163:  ❌ GET overloads (87 lines)
Lines 164-305:  ✅ GET implementation, get_schema()
Lines 306-372:  ❌ PUT overloads (67 lines)
Lines 373-458:  ✅ PUT implementation
Lines 459-525:  ❌ POST overloads (67 lines)
Lines 526-609:  ✅ POST implementation
Lines 610-651:  ❌ DELETE overloads (42 lines)
Lines 652-721:  ✅ DELETE implementation
Lines 722-949:  ✅ exists(), set(), move(), clone()

Total: 949 lines (263 lines of overloads = 28% waste)
```

### After: `profile.py` (686 lines)
```
Lines   1-77:   Module docstring, imports, class definition
Lines  78-xxx:  ✅ GET implementation, get_schema() (no overloads)
Lines xxx-xxx:  ✅ PUT implementation (no overloads)
Lines xxx-xxx:  ✅ POST implementation (no overloads)
Lines xxx-xxx:  ✅ DELETE implementation (no overloads)
Lines xxx-xxx:  ✅ exists(), set(), move(), clone()

Total: 686 lines (0 lines of overloads = 0% waste)
```

**Per-file savings:** 263 lines (28% reduction)

---

## How Type Checkers See It

### Before (explicit overloads)
```python
class Profile:
    @overload
    def get(self, name: str, response_mode: Literal["object"]) -> FortiObject: ...
    def get(self, name: str | None = None, ...):
        pass

# Type checker sees: ✅ Overload defined locally
```

### After (inherited overloads)
```python
# _protocols.py
class GetProtocol(Protocol):
    @overload
    def get(self, name: str, response_mode: Literal["object"]) -> FortiObject: ...

# profile.py
class Profile(GetProtocol):
    def get(self, name: str | None = None, ...):
        pass

# Type checker sees: ✅ Overload inherited from protocol
```

**Result:** Identical type checking behavior! 🎉

---

## IDE Autocomplete Comparison

Both versions provide **identical autocomplete**:

```python
fgt.api.cmdb.voip_profile.get(
    # IDE shows:
    # - name: str | None
    # - filter: list[str] | None
    # - count: int | None
    # - start: int | None
    # - payload_dict: dict[str, Any] | None
    # - vdom: str | bool | None
    # - raw_json: bool = False
    # - response_mode: Literal["dict", "object"] | None
    # - **kwargs: Any
    # Returns: dict[str, Any] | FortiObject | list[FortiObject]
```

**No difference** - protocols provide the same type information to IDEs! ✨

---

## Migration Impact

### Files to Create
1. ✅ `packages/fortios/hfortix_fortios/_protocols.py` (done)

### Files to Modify
1. **Generator template** (one-time change)
   - Add `from hfortix_fortios._protocols import CRUDEndpoint`
   - Change `class {Name}(MetadataMixin):` to `class {Name}(CRUDEndpoint, MetadataMixin):`
   - Remove overload generation logic

2. **Existing endpoint files** (optional, gradual)
   - Can be done endpoint-by-endpoint
   - Or bulk update with script
   - Or leave as-is (old files still work)

### Testing Required
- ✅ Type checking: `mypy packages/fortios/hfortix_fortios/`
- ✅ Unit tests: `pytest packages/fortios/`
- ✅ IDE autocomplete: Manual verification in VSCode/PyCharm
- ✅ Runtime behavior: Protocols have zero runtime impact

---

## Recommendation

**Implement this refactoring immediately for:**

1. ✅ **New generated endpoints** - update generator template
2. ⏱️ **Existing endpoints** - gradually migrate or bulk update
3. 📚 **Documentation** - update to show protocol-based approach

**Expected results:**

- 🎯 90%+ reduction in overload boilerplate
- 🎯 Faster file generation
- 🎯 Easier maintenance (change overloads in one place)
- 🎯 Smaller repository size
- 🎯 **Zero impact on functionality, type checking, or autocomplete**
