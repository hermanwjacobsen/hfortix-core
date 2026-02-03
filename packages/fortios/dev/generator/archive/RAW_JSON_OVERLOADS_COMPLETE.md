# Raw JSON Overloads Implementation - Complete

## Summary

Successfully added `raw_json=True` parameter overloads to all endpoint methods in both DictMode and ObjectMode classes. This ensures that when `raw_json=True` is passed, Pylance correctly infers the return type as `RawAPIResponse` instead of the regular response type.

## Changes Made

### 1. Template Updates (`.dev/generator/templates/endpoint_class.pyi.j2`)

Added `raw_json=True` overloads for all CRUD methods in both mode classes:

#### DictMode Class
- **GET**: Added overload with `*, raw_json: Literal[True]` → `RawAPIResponse`
- **POST**: Added overload with `*, raw_json: Literal[True]` → `RawAPIResponse`
- **PUT**: Added overload with `*, raw_json: Literal[True]` → `RawAPIResponse`
- **DELETE**: Added overload with `*, raw_json: Literal[True]` → `RawAPIResponse`

#### ObjectMode Class
- **GET**: Added overload with `*, raw_json: Literal[True]` → `RawAPIResponse`
- **POST**: Added overload with `*, raw_json: Literal[True]` → `RawAPIResponse`
- **PUT**: Added overload with `*, raw_json: Literal[True]` → `RawAPIResponse`
- **DELETE**: Added overload with `*, raw_json: Literal[True]` → `RawAPIResponse`

### 2. Overload Pattern

Each method now has the following overload structure (most specific first):

```python
# 1. raw_json=True returns RawAPIResponse (MOST SPECIFIC - matches first)
@overload
def get(..., *, raw_json: Literal[True], **kwargs) -> RawAPIResponse: ...

# 2. Object mode override
@overload
def get(..., *, response_mode: Literal["object"], **kwargs) -> RuleObject: ...

# 3. Dict mode override  
@overload
def get(..., *, response_mode: Literal["dict"], **kwargs) -> RuleResponse: ...

# 4. Default implementation (uses class default mode)
def get(..., response_mode: Literal[...] | None = ..., **kwargs) -> ...: ...
```

### 3. Key Design Decisions

#### Why `*, raw_json: Literal[True]`?
- The `*` forces `raw_json` to be keyword-only, making overload resolution deterministic
- `Literal[True]` (not just `bool`) ensures the overload only matches when explicitly `raw_json=True`
- Without `Literal[True]`, Python can't narrow the type based on a bool value

#### Overload Order Matters
- Most specific overloads MUST come first
- `raw_json=True` is most specific (matches only when explicitly passed)
- `response_mode="object"/"dict"` are next (match when mode explicitly passed)
- Default implementation is last (matches everything else)

### 4. Files Regenerated

Ran the generator to regenerate all 1,064 endpoint stub files with the new overloads:
```bash
python3 .dev/generator/generate.py
```

Result: All endpoint `.pyi` files now have complete `raw_json=True` support.

## Type Checking Results

### Before Fix
```python
# Issue: raw_json=True didn't narrow return type
raw_get = rule.get(raw_json=True)
# Pylance thought this was RuleResponse, not RawAPIResponse
raw_get["http_status"]  # No autocomplete, no type checking
raw_get["nonexistent"]  # NO ERROR (incorrect!)
```

### After Fix
```python
# Success: raw_json=True narrows to RawAPIResponse
raw_get = rule.get(raw_json=True)
# Pylance knows this is RawAPIResponse
raw_get["http_status"]  # ✅ Autocomplete works
raw_get["http_method"]  # ✅ Autocomplete works
raw_get["results"]      # ✅ Autocomplete works
raw_get["nonexistent"]  # ❌ Error: "not a defined key in RawAPIResponse"
```

## Test Coverage

Added comprehensive tests in `test_type_hints_fix.py`:

```python
def test_raw_json_get():
    """Test that raw_json=True returns RawAPIResponse for GET"""
    raw_get = fgt.api.cmdb.authentication.rule.get(name="test", raw_json=True)
    assert raw_get['http_method'] == "GET"
    assert raw_get['http_status'] == 200
    assert raw_get['results'] is not None
    x = raw_get['nonexistent']  # ❌ Pylance error!

def test_raw_json_post():
    """Test that raw_json=True returns RawAPIResponse for POST"""
    raw_post = fgt.api.cmdb.authentication.rule.post(name="test", raw_json=True)
    assert raw_post['http_method'] == "POST"
    y = raw_post['nonexistent']  # ❌ Pylance error!

def test_raw_json_put():
    """Test that raw_json=True returns RawAPIResponse for PUT"""
    raw_put = fgt.api.cmdb.authentication.rule.put(name="test", raw_json=True)
    assert raw_put['http_method'] == "PUT"
    z = raw_put['nonexistent']  # ❌ Pylance error!

def test_raw_json_delete():
    """Test that raw_json=True returns RawAPIResponse for DELETE"""
    raw_delete = fgt.api.cmdb.authentication.rule.delete(name="test", raw_json=True)
    assert raw_delete['http_method'] == "DELETE"
    w = raw_delete['nonexistent']  # ❌ Pylance error!
```

All tests show proper type checking - nonexistent fields are flagged as errors.

## RawAPIResponse TypedDict Fields

The `RawAPIResponse` TypedDict includes:

**Common fields (all responses):**
- `http_method`: str
- `http_status`: int
- `status`: str
- `vdom`: str

**GET response fields:**
- `results`: Any
- `path`: str
- `name`: str
- `serial`: str
- `version`: str
- `build`: int

**Mutation response fields (POST/PUT/DELETE):**
- `revision`: str
- `mkey`: str

## Benefits

1. **Type Safety**: `raw_json=True` now properly narrows return type to `RawAPIResponse`
2. **Autocomplete**: IDE shows all available `RawAPIResponse` fields
3. **Error Detection**: Accessing nonexistent fields shows Pylance errors
4. **Consistency**: Works uniformly across all 1,064 endpoints
5. **All Methods**: GET, POST, PUT, DELETE all support `raw_json=True`
6. **Both Modes**: Works in both DictMode and ObjectMode classes

## Implementation Complete

✅ Template updated with raw_json overloads  
✅ All 1,064 endpoint files regenerated  
✅ Test coverage added for all CRUD methods  
✅ Type checking verified and working  
✅ No Python errors  
✅ Pylance correctly detects type errors  

The `raw_json=True` parameter now provides full type safety and IDE support across the entire hfortix-fortios library!
