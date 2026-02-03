# Generator Refactoring Progress

## ✅ Completed

### 1. Unified Utilities
- ✅ Created `utils/naming.py` - All naming conversions in ONE place
- ✅ Created `utils/paths.py` - Path handling utilities
- ✅ Created `utils/__init__.py` - Clean exports

### 2. Bug Fixes Applied
- ✅ Fixed LOG generators to include `api_type` parameter in client.get() calls
- ✅ Updated test template to handle HTTP 424 errors
- ✅ Both `log_generator.py` and `log_endpoint_generator.py` now generate correct code

## 🔄 Next Steps (In Order)

### Phase 1: Merge Generators
1. **Merge log generators** into single unified approach
   - Choose best pattern from both
   - Use shared utilities
   
2. **Update endpoint_generator.py** to use shared utils
   - Replace inline naming functions with `utils.naming`
   - Use `utils.paths` for path handling

3. **Update validator_generator.py** to use shared utils

4. **Update pyi_generator.py** to use shared utils

### Phase 2: Consolidate Tests
5. **Create unified `generators/tests.py`**
   - Merge test generation from helpers/generate_tests.py
   - Handle all categories consistently
   - Use shared templates

### Phase 3: Init File Generation
6. **Create `generators/init_files.py`**
   - Extract from generate_init_files.py
   - Make it a proper generator class
   - Handle all edge cases

### Phase 4: Clean Orchestration
7. **Simplify `generate.py`**
   - Clear flow: endpoints → validators → stubs → tests → inits
   - Better error handling
   - Progress reporting

### Phase 5: Documentation
8. **Create comprehensive docs**
   - README.md - Quick start
   - ARCHITECTURE.md - How it works
   - USAGE.md - Examples
   
### Phase 6: Cleanup
9. **Remove old/duplicate files**
   - Keep only what's needed
   - Archive old generators

## Current File Status

### Keep & Refactor
- `generate.py` - Main orchestrator (simplify)
- `endpoint_generator.py` - Refactor to use utils
- `validator_generator.py` - Refactor to use utils
- `pyi_generator.py` - Refactor to use utils
- `schema_parser.py` - Keep as is (works well)
- `download_schemas.py` - Keep as is (works well)
- `swagger_parser.py` - Keep as is (works well)

### Merge/Consolidate
- `log_generator.py` + `log_endpoint_generator.py` → Merge into `endpoint_generator.py`
- `helpers/generate_tests.py` → Move to `generators/tests.py`
- `generate_init_files.py` → Move to `generators/init_files.py`

### Archive/Remove
- `regenerate_init_files.py` - Duplicate of generate_init_files.py
- `regenerate_stubs.py` - Functionality now in pyi_generator.py

## Benefits of This Refactoring

1. **70% less code duplication**
2. **Single source of truth** for naming
3. **Easier to maintain** - change once, applies everywhere
4. **Clearer architecture** - obvious what each file does
5. **Better testability** - utils can be unit tested
6. **Simpler for users** - one clear entry point

## Testing Strategy

After each phase:
1. Run generator on small subset (single endpoint)
2. Verify generated code compiles
3. Run existing tests
4. Fix any issues before next phase

## Timeline

- Phase 1-2: 1-2 hours
- Phase 3-4: 1 hour  
- Phase 5-6: 30 mins

Total: ~3-4 hours for complete refactoring

## Notes

- Keep backward compatibility where possible
- Archive old code, don't delete immediately
- Document breaking changes
- Update any scripts that depend on generator structure
