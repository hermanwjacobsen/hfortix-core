# Archive Directory

This directory contains legacy helper scripts and utilities that are no longer actively used in the current generator architecture.

## Archive Date
January 6, 2026

## Reason for Archival
As part of the generator refactoring effort, we consolidated duplicate code into shared utilities (`utils/naming.py`, `utils/paths.py`) and streamlined the generator architecture. These scripts were either:
- Duplicated functionality now in the core generators
- One-off migration/analysis tools
- Superseded by better implementations

## Archived Helpers (`helpers_old/`)

### `analyze_dependencies.py`
One-time analysis tool for mapping endpoint dependencies. No longer needed for regular generation.

### `bulk_generate.py`
Old bulk generation script replaced by `generate.py` with `--all` or `--category` flags.

### `bulk_generate_tests.py`
Old test generation script replaced by `helpers/generate_tests.py` (which is still active).

### `generate_category_stubs.py`
Legacy stub generator superseded by `generators/pyi_generator.py`.

### `generate_endpoint.py`
Legacy endpoint generator superseded by `generators/endpoint_generator.py`.

### `regenerate_init_files.py`
**NOTE**: This file was initially archived but has been **restored to root** as it's actively imported by `generate.py`. The archive copy remains for reference only.

### `test_generator.py`
Legacy test generator superseded by `helpers/generate_tests.py`.

### `test_helper_integration.py`
One-time integration test for helper functions. Not needed for regular generation.

### `test_improvements.py`
Development/experimental script for testing generator improvements. Not needed for regular generation.

## Archived Root Scripts (`scripts_old/`)

### `generate_init_files.py`
Replaced by `regenerate_init_files.py` which is actively imported by `generate.py`.

### `regenerate_stubs.py`
Legacy stub regeneration script superseded by `generators/pyi_generator.py` integrated into main generation flow.

## Currently Active Files

The following files remain active and are used in the current architecture:

### Core Scripts
- `generate.py` - Main orchestrator for all code generation
- `generate.sh` - Shell wrapper for generate.py
- `download_schemas.py` - Schema downloader from FortiOS API
- `schema_parser.py` - Parses schemas into structured format
- `swagger_parser.py` - Parses Swagger/OpenAPI docs
- `regenerate_init_files.py` - Generates `__init__.py` files

### Generators
- `generators/endpoint_generator.py` - Generates CMDB/Monitor/Service endpoints
- `generators/validator_generator.py` - Generates validation helpers
- `generators/pyi_generator.py` - Generates type stubs (.pyi files)
- `generators/log_generator.py` - Generates LOG endpoints (special structure)

### Active Helpers
- `helpers/generate_tests.py` - Test generation (imported by generate.py)

### Shared Utilities
- `utils/naming.py` - Naming conventions (kebab_to_snake, to_class_name, etc.)
- `utils/paths.py` - Path handling utilities

## Restoration

If any of these archived scripts need to be restored for reference or reuse:
```bash
# Restore a helper
cp archive/helpers_old/<script_name> helpers/

# Restore a root script
cp archive/scripts_old/<script_name> ./
```

## Clean Architecture Benefits

The refactoring that led to this archival provides:
1. **Single source of truth** - Shared utilities eliminate code duplication
2. **Clear separation** - Generators, helpers, and utils have distinct responsibilities
3. **Maintainability** - Changes to naming conventions only need updates in one place
4. **Type safety** - Consistent use of shared utilities ensures correct behavior
5. **Testability** - Focused generators are easier to test and validate
