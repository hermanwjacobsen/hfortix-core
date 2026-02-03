# Generator Update: Top-Level Mode Classes

## Summary

Updated the code generator to automatically create mode-specific classes (`DictMode`/`ObjectMode`) for top-level API categories (CMDB, MONITOR, SERVICE).

## Changes Made

### 1. New Template: `toplevel_init.pyi.j2`
- **Location**: `.dev/generator/templates/toplevel_init.pyi.j2`
- **Purpose**: Generate `__init__.pyi` files for top-level categories with mode-specific classes
- **Features**:
  - Creates `CMDBDictMode`, `CMDBObjectMode` classes (and similar for MONITOR, SERVICE)
  - Smart handling: Uses mode-specific classes where available, falls back to base class otherwise
  - Adds helpful comments for subcategories without mode classes

### 2. Updated `PYIGenerator`
- **Location**: `.dev/generator/generators/pyi_generator.py`
- **New Method**: `generate_toplevel_init_stub()`
- **Function**: Renders the top-level template with subcategory information

### 3. Updated `_generate_toplevel_stubs()`
- **Location**: `.dev/generator/generate.py`
- **Changes**:
  - Replaced hardcoded string building with template-based approach
  - Detects which subcategories have mode classes by checking their `__init__.pyi` files
  - Passes structured data to template instead of generating strings manually

## How It Works

### Detection of Mode Classes

The generator checks each subcategory's `__init__.pyi` file to see if it has mode-specific classes:

```python
# Check if this subcategory has mode-specific classes
subcat_init_pyi = category_dir / module_name / '__init__.pyi'
has_mode_classes = False

if subcat_init_pyi.exists():
    subcat_content = subcat_init_pyi.read_text()
    if f'{class_name}DictMode' in subcat_content:
        has_mode_classes = True
```

### Template Logic

The template conditionally uses mode classes or base classes:

```jinja2
{% if subcategory.has_mode_classes %}
    firewall: firewall.FirewallDictMode
{% else %}
    diameter_filter: diameter_filter.DiameterFilter  # No mode classes yet
{% endif %}
```

## Example Output

### CMDB __init__.pyi (Generated)

```python
class CMDBDictMode:
    """CMDB API category for dict response mode."""
    
    firewall: firewall.FirewallDictMode              # Has mode classes ✅
    system: system.SystemDictMode                    # Has mode classes ✅
    diameter_filter: diameter_filter.DiameterFilter  # No mode classes yet ⏳
    ftp_proxy: ftp_proxy.FtpProxy                   # No mode classes yet ⏳
    ...

class CMDBObjectMode:
    """CMDB API category for object response mode."""
    
    firewall: firewall.FirewallObjectMode            # Has mode classes ✅
    system: system.SystemObjectMode                  # Has mode classes ✅
    diameter_filter: diameter_filter.DiameterFilter  # No mode classes yet ⏳
    ftp_proxy: ftp_proxy.FtpProxy                   # No mode classes yet ⏳
    ...
```

## Type Inference Chain

With these changes, the complete type flow works:

```python
FortiOS(response_mode="object")
  ↓ __new__ returns FortiOSObjectMode
  ↓ .api returns APIObjectMode
  ↓ .cmdb returns CMDBObjectMode          # ✅ Now generated automatically
  ↓ .firewall returns FirewallObjectMode
  ↓ .policy returns PolicyObjectMode
  ↓ .get() returns list[PolicyObject]     # ✅ Fully typed!
```

## Benefits

1. **No Manual Edits**: Top-level `__init__.pyi` files are now generated automatically
2. **Future-Proof**: Running the generator won't overwrite manual changes
3. **Graceful Degradation**: Works with subcategories that don't have mode classes yet
4. **Clear Documentation**: Comments indicate which subcategories need mode classes
5. **Type Safety**: Full type propagation from client to endpoints

## Migration Path

As more subcategories get mode-specific classes generated:

1. Subcategory templates generate `FirewallDictMode`/`FirewallObjectMode`
2. Top-level generator automatically detects them
3. CMDB `__init__.pyi` regenerated with proper mode class references
4. No manual intervention required!

## Testing

Verified with test files:
- ✅ `test_iteration_fix.py` - No errors
- ✅ `test_client_mode_propagation.py` - No errors
- ✅ `test_autocomplete.py` - All expected errors show correctly

## Statistics

- **Top-level categories updated**: 3 (CMDB, MONITOR, SERVICE)
- **Subcategories with mode classes**: ~30+ (firewall, system, antivirus, etc.)
- **Subcategories without mode classes**: ~10 (diameter_filter, ftp_proxy, etc.)
- **Total endpoints**: 1,064

## Next Steps

The remaining subcategories without mode classes can be added gradually:
- `diameter_filter`
- `endpoint_control`
- `ethernet_oam`
- `extension_controller`
- `file_filter`
- `ftp_proxy`
- `sctp_filter`
- `switch_controller`
- `virtual_patch`
- `web_proxy`
- `wireless_controller`

As each gets mode classes, the top-level generator will automatically use them!
