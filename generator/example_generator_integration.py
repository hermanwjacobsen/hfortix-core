#!/usr/bin/env python3
"""
Example: How to integrate field override updates into your code generator

This shows how to call the field override updater as part of the code
generation workflow.
"""

from pathlib import Path
import sys

# Add generator to path
sys.path.insert(0, str(Path(__file__).parent))

from update_field_overrides import update_from_schemas


def generate_fortios_api():
    """
    Example main generator function.
    
    This would be your actual code generator that creates:
    - API endpoint files
    - Type stubs (.pyi files)
    - Helper modules
    - Models
    - etc.
    """
    print("Generating FortiOS API code...")
    print("  - Endpoint files")
    print("  - Type stubs")
    print("  - Helper modules")
    print("  - Models")
    print("✓ API code generation complete")


def main():
    """
    Example generator workflow with field override integration.
    """
    print("=" * 80)
    print("FORTIOS API CODE GENERATOR")
    print("=" * 80)
    print()
    
    # Step 1: Verify schemas exist
    schema_path = Path(__file__).parent.parent / 'schema' / '7.6.5'
    if not schema_path.exists():
        print(f"❌ Error: Schema directory not found: {schema_path}")
        print("   Please download/generate schemas first")
        return 1
    
    print(f"✓ Found schemas at: {schema_path}")
    print()
    
    # Step 2: Update field overrides from schemas
    print("Step 1: Updating field overrides from schemas...")
    print("-" * 80)
    success = update_from_schemas(
        schema_base_path=schema_path,
        verbose=True
    )
    
    if not success:
        print("❌ Failed to update field overrides")
        return 1
    
    print()
    
    # Step 3: Generate API code
    print("Step 2: Generating API code...")
    print("-" * 80)
    generate_fortios_api()
    print()
    
    # Step 4: Success
    print("=" * 80)
    print("✅ GENERATION COMPLETE")
    print("=" * 80)
    print()
    print("Next steps:")
    print("  1. Run tests: python3 test_underscore_preservation.py")
    print("  2. Review changes: git diff")
    print("  3. Commit: git add . && git commit -m 'Regenerate API code'")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
