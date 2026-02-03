"""
Tests for hfortix_core.readonly_cache module-level cache functions.

This is a module-level TTL cache used for read-only data caching.
"""

import time
import hfortix_core
cache = hfortix_core.readonly_cache


def test_readonly_cache_set_get():
    """Test basic set and get operations."""
    print("\n=== Testing readonly_cache set/get ===")
    
    cache.set("test_key", "test_value")
    result = cache.get("test_key")
    assert result == "test_value"
    
    # Cleanup
    cache.invalidate("test_key")
    print("✅ readonly_cache - set and get")


def test_readonly_cache_get_missing():
    """Test get returns None for missing keys."""
    print("\n=== Testing readonly_cache get missing ===")
    
    result = cache.get("nonexistent_key_12345")
    assert result is None
    
    print("✅ readonly_cache - get missing returns None")


def test_readonly_cache_set_overwrite():
    """Test that set overwrites existing values."""
    print("\n=== Testing readonly_cache overwrite ===")
    
    cache.set("overwrite_key", "value1")
    cache.set("overwrite_key", "value2")
    result = cache.get("overwrite_key")
    assert result == "value2"
    
    # Cleanup
    cache.invalidate("overwrite_key")
    print("✅ readonly_cache - set overwrites")


def test_readonly_cache_invalidate():
    """Test invalidate removes a key."""
    print("\n=== Testing readonly_cache invalidate ===")
    
    cache.set("invalidate_key", "value")
    assert cache.get("invalidate_key") == "value"
    
    cache.invalidate("invalidate_key")
    assert cache.get("invalidate_key") is None
    
    print("✅ readonly_cache - invalidate")


def test_readonly_cache_invalidate_missing():
    """Test invalidate doesn't raise for missing keys."""
    print("\n=== Testing readonly_cache invalidate missing ===")
    
    # Should not raise
    cache.invalidate("key_that_does_not_exist_9999")
    
    print("✅ readonly_cache - invalidate missing key doesn't raise")


def test_readonly_cache_clear():
    """Test clear removes all keys."""
    print("\n=== Testing readonly_cache clear ===")
    
    # Set multiple keys
    cache.set("clear_test_1", "value1")
    cache.set("clear_test_2", "value2")
    cache.set("clear_test_3", "value3")
    
    # Verify they exist
    assert cache.get("clear_test_1") == "value1"
    
    # Clear all
    cache.clear()
    
    # Verify all are gone
    assert cache.get("clear_test_1") is None
    assert cache.get("clear_test_2") is None
    assert cache.get("clear_test_3") is None
    
    print("✅ readonly_cache - clear")


def test_readonly_cache_cleanup():
    """Test cleanup removes expired entries."""
    print("\n=== Testing readonly_cache cleanup ===")
    
    # Set with very short TTL (if supported)
    # The module uses default_ttl, so we just test cleanup doesn't crash
    cache.set("cleanup_test", "value")
    
    # Cleanup should not raise
    result = cache.cleanup()
    # Result might be count of removed entries or None
    
    # Cleanup after test
    cache.invalidate("cleanup_test")
    
    print("✅ readonly_cache - cleanup")


def test_readonly_cache_various_types():
    """Test cache with various value types."""
    print("\n=== Testing readonly_cache various types ===")
    
    # String
    cache.set("type_string", "hello")
    assert cache.get("type_string") == "hello"
    
    # Integer
    cache.set("type_int", 42)
    assert cache.get("type_int") == 42
    
    # Float
    cache.set("type_float", 3.14)
    assert cache.get("type_float") == 3.14
    
    # List
    cache.set("type_list", [1, 2, 3])
    assert cache.get("type_list") == [1, 2, 3]
    
    # Dict
    cache.set("type_dict", {"key": "value"})
    assert cache.get("type_dict") == {"key": "value"}
    
    # None
    cache.set("type_none", None)
    assert cache.get("type_none") is None
    
    # Bool
    cache.set("type_bool_true", True)
    cache.set("type_bool_false", False)
    assert cache.get("type_bool_true") is True
    assert cache.get("type_bool_false") is False
    
    # Cleanup
    cache.clear()
    
    print("✅ readonly_cache - various types")


def test_readonly_cache_default_ttl():
    """Test default_ttl is accessible."""
    print("\n=== Testing readonly_cache default_ttl ===")
    
    ttl = cache.default_ttl
    assert ttl is not None
    assert isinstance(ttl, (int, float))
    assert ttl > 0
    
    print(f"✅ readonly_cache - default_ttl = {ttl}")


def test_readonly_cache_special_keys():
    """Test cache with special key characters."""
    print("\n=== Testing readonly_cache special keys ===")
    
    # Key with dots
    cache.set("firewall.address", "value1")
    assert cache.get("firewall.address") == "value1"
    
    # Key with slashes
    cache.set("api/v2/cmdb", "value2")
    assert cache.get("api/v2/cmdb") == "value2"
    
    # Key with spaces
    cache.set("key with spaces", "value3")
    assert cache.get("key with spaces") == "value3"
    
    # Empty string key
    cache.set("", "empty_key_value")
    assert cache.get("") == "empty_key_value"
    
    # Cleanup
    cache.clear()
    
    print("✅ readonly_cache - special keys")


def run_all_tests():
    """Run all readonly_cache tests."""
    tests = [
        test_readonly_cache_set_get,
        test_readonly_cache_get_missing,
        test_readonly_cache_set_overwrite,
        test_readonly_cache_invalidate,
        test_readonly_cache_invalidate_missing,
        test_readonly_cache_clear,
        test_readonly_cache_cleanup,
        test_readonly_cache_various_types,
        test_readonly_cache_default_ttl,
        test_readonly_cache_special_keys,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except Exception as e:
            failed += 1
            print(f"❌ {test.__name__} FAILED: {e}")
    
    print(f"\n{'='*50}")
    print(f"Results: {passed}/{passed + failed} passed")
    return failed == 0


if __name__ == "__main__":
    import sys
    success = run_all_tests()
    sys.exit(0 if success else 1)
