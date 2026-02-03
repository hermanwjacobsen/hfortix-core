# POST/PUT/DELETE Return Type Fix - Complete

## Problem

POST/PUT/DELETE methods in **ObjectMode** classes were returning `RuleObject` by default instead of `MutationResponse`. This caused type errors when users tried to access mutation response fields like `status` and `http_status`.

### User Report
```python
# Client initialized without explicit response_mode (defaults to object mode)
fg = FortiOS(host="192.168.1.99", token="token")

# POST/PUT/DELETE were returning RuleObject instead of MutationResponse
post_result = fg.api.cmdb.authentication.rule.post(name="new_rule", status="enable")
post_result["status"]  # ❌ Error: not in RuleObject
post_result["http_status"]  # ❌ Error: not in RuleObject
# Pylance showed: (variable) post_result: RuleObject
```

### Root Cause

In the **ObjectMode** class template, POST/PUT/DELETE had:

```python
# BEFORE (WRONG):
def post(..., response_mode: Literal["object"] | None = ..., **kwargs) -> RuleObject: ...
```

This meant when `response_mode` was not passed (default behavior), it would match `None` and return `RuleObject`. But POST/PUT/DELETE don't actually return object data from the FortiOS API - they return status responses like `{"status": "success", "http_status": 200}`.

## Solution

Changed the **ObjectMode** class to have POST/PUT/DELETE return `MutationResponse` by default, and only return `RuleObject` when explicitly requested with `response_mode="object"`:

### Template Changes

**Before:**
```jinja
{% if schema.capabilities.crud.create %}
    # POST - Dict mode override
    @overload
    def post(..., response_mode: Literal["dict"] = ..., **kwargs) -> MutationResponse: ...
    
    # POST - Object mode (default for ObjectMode class)
    def post(..., response_mode: Literal["object"] | None = ..., **kwargs) -> RuleObject: ...
{% endif %}
```

**After:**
```jinja
{% if schema.capabilities.crud.create %}
    # raw_json=True returns RawAPIResponse for POST
    @overload
    def post(..., *, raw_json: Literal[True], **kwargs) -> RawAPIResponse: ...
    
    # POST - Dict mode override
    @overload
    def post(..., response_mode: Literal["dict"] = ..., **kwargs) -> MutationResponse: ...
    
    # POST - Object mode override (requires explicit response_mode="object")
    @overload
    def post(..., *, response_mode: Literal["object"], **kwargs) -> RuleObject: ...
    
    # POST - Default for ObjectMode (returns MutationResponse like DictMode)
    def post(..., response_mode: None = ..., **kwargs) -> MutationResponse: ...
{% endif %}
```

### Key Changes

1. **Added `raw_json=True` overload** (highest priority): Returns `RawAPIResponse`
2. **Modified object mode overload**: Changed from `response_mode: Literal["object"] | None` to `*, response_mode: Literal["object"]` (keyword-only, requires explicit value)
3. **New default implementation**: `response_mode: None = ...` returns `MutationResponse`

### Overload Resolution Order

Now POST/PUT/DELETE in ObjectMode match in this order:

1. **Most specific**: `raw_json=True` → `RawAPIResponse`
2. **Explicit dict mode**: `response_mode="dict"` → `MutationResponse`  
3. **Explicit object mode**: `response_mode="object"` → `RuleObject`
4. **Default**: `response_mode=None` or not passed → `MutationResponse` ✅

## Results

### After Fix
```python
# Client in object mode
fg = FortiOS(host="192.168.1.99", token="token")

# Default behavior (no response_mode) - NOW RETURNS MutationResponse ✅
post_result = fg.api.cmdb.authentication.rule.post(name="new_rule", status="enable")
post_result["status"]  # ✅ Works - MutationResponse has status field
post_result["http_status"]  # ✅ Works - MutationResponse has http_status field
post_result["nonexistent"]  # ❌ Shows error - not in MutationResponse
# Pylance shows: (variable) post_result: MutationResponse

# Explicit object mode - returns RuleObject
post_obj = fg.api.cmdb.authentication.rule.post(
    name="new_rule", 
    status="enable",
    response_mode="object"  # Explicit request for object
)
post_obj.name  # ✅ Works - RuleObject has name attribute
post_obj.status  # ✅ Works - RuleObject has status attribute
# Pylance shows: (variable) post_obj: RuleObject
```

### Type Checking Verified

All mutation methods now correctly return `MutationResponse` by default:

✅ **POST**: `post_result["status"]` works, `post_result["nonexistent"]` shows error  
✅ **PUT**: `put_result["status"]` works, `put_result["nonexistent"]` shows error  
✅ **DELETE**: `delete_result["status"]` works, `delete_result["nonexistent"]` shows error  

## Files Updated

1. **Template**: `.dev/generator/templates/endpoint_class.pyi.j2`
   - Modified ObjectMode POST/PUT/DELETE overload structure
   - Added object mode override with keyword-only `response_mode`
   - Changed default implementation to return `MutationResponse`

2. **Generated stubs**: All 1,064 endpoint `.pyi` files regenerated

## Why This Makes Sense

**POST/PUT/DELETE vs GET**:
- **GET**: Returns actual object data → mode classes make sense
  - DictMode: Returns `TypedDict` by default
  - ObjectMode: Returns `FortiObject` by default
  
- **POST/PUT/DELETE**: Return API status responses, not object data → mode classes should behave the same
  - DictMode: Returns `MutationResponse` by default ✅
  - ObjectMode: NOW also returns `MutationResponse` by default ✅

**When to get objects from mutations**:
- Must explicitly request with `response_mode="object"`
- Implementation would need to fetch the object after mutation (not default API behavior)

## Backward Compatibility

This is a **type-only change** - it only affects type inference, not runtime behavior. The actual `.py` implementation was always returning `MutationResponse` for mutations.

Users who were relying on `RuleObject` return type from POST/PUT/DELETE without explicit `response_mode="object"` will now see type errors, which is correct because the API was never returning object data by default.

## Summary

✅ ObjectMode POST/PUT/DELETE now return `MutationResponse` by default (matching DictMode)  
✅ `response_mode="object"` still works for those who want object data  
✅ `raw_json=True` returns `RawAPIResponse` for all methods  
✅ Type inference is now correct for all mutation operations  
✅ All 1,064 endpoints updated with correct types  

The fix ensures that type hints accurately reflect the actual FortiOS API behavior: mutations return status responses, not object data.
