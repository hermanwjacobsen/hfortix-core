"""
CMDB Endpoint Tests: log/custom-field
Tests custom log fields configuration (VDOM scope).

Endpoint Information:
- Path: /api/v2/cmdb/log/custom-field
- Scope: VDOM
- Type: Table endpoint (supports multiple entries)
- Operations: GET, POST, PUT, DELETE

Test Strategy:
- Create a new custom field entry
- Verify creation successful
- Update the custom field entry
- Verify update successful
- Delete the custom field entry
- Verify deletion successful
"""

import argparse
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(project_root))
from fgtclient import fgt


# Test data
TEST_FIELD_ID = "test_custom_field_001"
TEST_FIELD_NAME = "TestField"
TEST_FIELD_VALUE = "TestValue"
UPDATED_NAME = "UpdatedField"
UPDATED_VALUE = "UpdatedValue"


def test_cleanup_existing():
    """Clean up any existing test custom field"""
    print("\n0. Cleaning up any existing test custom field...")
    
    try:
        existing = fgt.api.cmdb.log.custom_field.get(id=TEST_FIELD_ID, vdom="test")
        if existing and existing.http_status == "success":
            print(f"   Found existing field '{TEST_FIELD_ID}', deleting...")
            fgt.api.cmdb.log.custom_field.delete(id=TEST_FIELD_ID, vdom="test")
            print("   ✓ Existing field deleted")
    except Exception:
        # Field doesn't exist, which is fine
        print("   ✓ No existing field to clean up")


def test_post_create():
    """Create a new custom field entry"""
    print(f"\n1. Creating custom field '{TEST_FIELD_ID}'...")
    
    result = fgt.api.cmdb.log.custom_field.post(
        id=TEST_FIELD_ID,
        name=TEST_FIELD_NAME,
        value=TEST_FIELD_VALUE,
        vdom="test"
    )
    
    assert result is not None, "Failed to create custom field"
    assert result.http_status == "success", f"Failed to create custom field: {result}"
    print(f"✓ Custom field created: id={TEST_FIELD_ID}, name={TEST_FIELD_NAME}, value={TEST_FIELD_VALUE}")


def test_get_verify_created():
    """Verify the custom field was created with correct values"""
    print(f"\n2. Verifying custom field '{TEST_FIELD_ID}' was created...")
    
    result = fgt.api.cmdb.log.custom_field.get(id=TEST_FIELD_ID, vdom="test")
    
    assert result is not None, "Failed to get custom field"
    assert result.http_status == "success", "Failed to get custom field"
    assert result.id == TEST_FIELD_ID, f"ID mismatch: expected {TEST_FIELD_ID}, got {result.id}"
    assert result.name == TEST_FIELD_NAME, f"Name mismatch: expected {TEST_FIELD_NAME}, got {result.name}"
    assert result.value == TEST_FIELD_VALUE, f"Value mismatch: expected {TEST_FIELD_VALUE}, got {result.value}"
    
    print(f"✓ Custom field verified: id={result.id}, name={result.name}, value={result.value}")


def test_put_update():
    """Update the custom field entry"""
    print(f"\n3. Updating custom field '{TEST_FIELD_ID}'...")
    
    result = fgt.api.cmdb.log.custom_field.put(
        id=TEST_FIELD_ID,
        name=UPDATED_NAME,
        value=UPDATED_VALUE,
        vdom="test"
    )
    
    assert result is not None, "Failed to update custom field"
    assert result.http_status == "success", "Failed to update custom field"
    print(f"✓ Custom field updated: name={UPDATED_NAME}, value={UPDATED_VALUE}")


def test_get_verify_updated():
    """Verify the custom field was updated correctly"""
    print(f"\n4. Verifying custom field '{TEST_FIELD_ID}' was updated...")
    
    result = fgt.api.cmdb.log.custom_field.get(id=TEST_FIELD_ID, vdom="test")
    
    assert result is not None, "Failed to get custom field"
    assert result.http_status == "success", "Failed to get custom field"
    assert result.id == TEST_FIELD_ID, f"ID mismatch: expected {TEST_FIELD_ID}, got {result.id}"
    assert result.name == UPDATED_NAME, f"Name mismatch: expected {UPDATED_NAME}, got {result.name}"
    assert result.value == UPDATED_VALUE, f"Value mismatch: expected {UPDATED_VALUE}, got {result.value}"
    
    print(f"✓ Updated values verified: name={result.name}, value={result.value}")


def test_delete():
    """Delete the custom field entry"""
    print(f"\n5. Deleting custom field '{TEST_FIELD_ID}'...")
    
    result = fgt.api.cmdb.log.custom_field.delete(id=TEST_FIELD_ID, vdom="test")
    
    assert result is not None, "Failed to delete custom field"
    assert result.http_status == "success", "Failed to delete custom field"
    print("✓ Custom field deleted")


def test_verify_deleted():
    """Verify the custom field was deleted"""
    print(f"\n6. Verifying custom field '{TEST_FIELD_ID}' was deleted...")
    
    try:
        result = fgt.api.cmdb.log.custom_field.get(id=TEST_FIELD_ID, vdom="test")
        # If we get here and status is success, the field still exists (shouldn't happen)
        if result and result.http_status == "success":
            raise AssertionError(f"Custom field still exists after deletion: {result.id}")
    except Exception as e:
        # Expecting an error since the field should not exist
        error_msg = str(e).lower()
        if "not found" in error_msg or "does not exist" in error_msg or "404" in error_msg:
            print("✓ Confirmed: Custom field no longer exists")
        else:
            # Re-raise if it's a different error
            raise


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run tests")
    parser.add_argument("--client", choices=["direct", "fmg_proxy"], default="direct",
                        help="Client to use: direct (default) or fmg_proxy")
    args = parser.parse_args()
    
    if args.client == "fmg_proxy":
        from fmgclient import fgt, fmg
        client_name = "FMG proxy"
    else:
        from fgtclient import fgt
        fmg = None
        client_name = "direct"
    
    print(f"Running tests with {client_name} client...")
    try:
        test_cleanup_existing()
        test_post_create()
        test_get_verify_created()
        test_put_update()
        test_get_verify_updated()
        test_delete()
        test_verify_deleted()
        print("\n" + "="*50)
        print("All log custom-field tests passed!")
        print("="*50)
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        # Attempt cleanup on failure
        try:
            fgt.api.cmdb.log.custom_field.delete(id=TEST_FIELD_ID, vdom="test")
            print("   (Cleanup: test field deleted)")
        except Exception:
            pass
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        # Attempt cleanup on failure
        try:
            fgt.api.cmdb.log.custom_field.delete(id=TEST_FIELD_ID, vdom="test")
            print("   (Cleanup: test field deleted)")
        except Exception:
            pass
        sys.exit(1)

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
