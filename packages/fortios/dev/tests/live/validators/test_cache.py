"""
Tests for hfortix_core cache utilities.

Tests TTLCache class and CacheEntry.
"""

import time
from hfortix_core.cache import TTLCache, CacheEntry


# ============================================================================
# CacheEntry tests
# ============================================================================

def test_cache_entry_creation():
    """Test creating a cache entry."""
    entry = CacheEntry("test_value", ttl_seconds=60)
    assert entry.value == "test_value"
    assert entry.expiry > time.time()
    print("✅ CacheEntry - creation")


def test_cache_entry_not_expired():
    """Test cache entry is not expired immediately."""
    entry = CacheEntry("value", ttl_seconds=60)
    assert entry.is_expired() is False
    print("✅ CacheEntry - not expired")


def test_cache_entry_expired():
    """Test cache entry expires after TTL."""
    entry = CacheEntry("value", ttl_seconds=0.01)  # 10ms TTL
    time.sleep(0.02)  # Wait 20ms
    assert entry.is_expired() is True
    print("✅ CacheEntry - expired")


# ============================================================================
# TTLCache basic tests
# ============================================================================

def test_ttl_cache_creation():
    """Test creating a TTL cache."""
    cache = TTLCache(default_ttl=3600)
    assert cache.default_ttl == 3600
    assert len(cache) == 0
    print("✅ TTLCache - creation")


def test_ttl_cache_set_get():
    """Test setting and getting values."""
    cache = TTLCache(default_ttl=60)
    cache.set("key1", "value1")
    result = cache.get("key1")
    assert result == "value1"
    print("✅ TTLCache - set and get")


def test_ttl_cache_get_missing():
    """Test getting a non-existent key returns None."""
    cache = TTLCache(default_ttl=60)
    result = cache.get("nonexistent")
    assert result is None
    print("✅ TTLCache - get missing key")


def test_ttl_cache_custom_ttl():
    """Test setting value with custom TTL."""
    cache = TTLCache(default_ttl=3600)
    cache.set("short_lived", "value", ttl=0.01)  # 10ms TTL
    
    # Should exist immediately
    assert cache.get("short_lived") == "value"
    
    # Wait for expiry
    time.sleep(0.02)
    
    # Should be expired and return None
    assert cache.get("short_lived") is None
    print("✅ TTLCache - custom TTL")


def test_ttl_cache_invalidate():
    """Test invalidating a cache entry."""
    cache = TTLCache(default_ttl=60)
    cache.set("key1", "value1")
    
    # Verify it exists
    assert cache.get("key1") == "value1"
    
    # Invalidate
    cache.invalidate("key1")
    
    # Should be gone
    assert cache.get("key1") is None
    print("✅ TTLCache - invalidate")


def test_ttl_cache_invalidate_missing():
    """Test invalidating a non-existent key doesn't raise."""
    cache = TTLCache(default_ttl=60)
    # Should not raise
    cache.invalidate("nonexistent")
    print("✅ TTLCache - invalidate missing key")


def test_ttl_cache_clear():
    """Test clearing all cache entries."""
    cache = TTLCache(default_ttl=60)
    cache.set("key1", "value1")
    cache.set("key2", "value2")
    cache.set("key3", "value3")
    
    assert len(cache) == 3
    
    cache.clear()
    
    assert len(cache) == 0
    assert cache.get("key1") is None
    assert cache.get("key2") is None
    assert cache.get("key3") is None
    print("✅ TTLCache - clear")


def test_ttl_cache_cleanup():
    """Test cleaning up expired entries."""
    cache = TTLCache(default_ttl=60)
    
    # Add some entries with short TTL
    cache.set("short1", "v1", ttl=0.01)
    cache.set("short2", "v2", ttl=0.01)
    cache.set("long", "v3", ttl=60)
    
    assert len(cache) == 3
    
    # Wait for short TTLs to expire
    time.sleep(0.02)
    
    # Cleanup
    removed = cache.cleanup()
    
    # Should have removed 2 entries
    assert removed == 2
    assert len(cache) == 1
    assert cache.get("long") == "v3"
    print("✅ TTLCache - cleanup")


def test_ttl_cache_len():
    """Test len() returns count of entries."""
    cache = TTLCache(default_ttl=60)
    assert len(cache) == 0
    
    cache.set("key1", "value1")
    assert len(cache) == 1
    
    cache.set("key2", "value2")
    assert len(cache) == 2
    print("✅ TTLCache - len")


def test_ttl_cache_contains():
    """Test 'in' operator checks existence and expiry."""
    cache = TTLCache(default_ttl=60)
    cache.set("key1", "value1")
    cache.set("short", "value2", ttl=0.01)
    
    assert "key1" in cache
    assert "short" in cache
    assert "nonexistent" not in cache
    
    # Wait for short to expire
    time.sleep(0.02)
    
    assert "short" not in cache
    print("✅ TTLCache - contains")


def test_ttl_cache_overwrite():
    """Test overwriting an existing key."""
    cache = TTLCache(default_ttl=60)
    cache.set("key1", "value1")
    cache.set("key1", "value2")
    
    assert cache.get("key1") == "value2"
    print("✅ TTLCache - overwrite")


def test_ttl_cache_different_types():
    """Test caching different data types."""
    cache = TTLCache(default_ttl=60)
    
    # String
    cache.set("string", "hello")
    assert cache.get("string") == "hello"
    
    # Integer
    cache.set("int", 42)
    assert cache.get("int") == 42
    
    # Dict
    cache.set("dict", {"name": "test", "value": 123})
    assert cache.get("dict") == {"name": "test", "value": 123}
    
    # List
    cache.set("list", [1, 2, 3])
    assert cache.get("list") == [1, 2, 3]
    
    # None - Note: caching None is problematic because get() returns None for missing keys
    # This is a known limitation - don't cache None values if you need to distinguish
    cache.set("none", None)
    # get() returns None, but we can't distinguish from "not found"
    assert cache.get("none") is None
    
    print("✅ TTLCache - different types")


def test_ttl_cache_expired_on_get():
    """Test that expired entries are removed on get."""
    cache = TTLCache(default_ttl=60)
    cache.set("short", "value", ttl=0.01)
    
    # Entry exists initially
    assert len(cache) == 1
    
    time.sleep(0.02)
    
    # Get should remove expired entry and return None
    result = cache.get("short")
    assert result is None
    assert len(cache) == 0
    print("✅ TTLCache - expired on get")


def run_all_tests():
    """Run all cache tests."""
    print("\n" + "=" * 60)
    print("CACHE TESTS")
    print("=" * 60 + "\n")

    # CacheEntry tests
    test_cache_entry_creation()
    test_cache_entry_not_expired()
    test_cache_entry_expired()

    # TTLCache tests
    test_ttl_cache_creation()
    test_ttl_cache_set_get()
    test_ttl_cache_get_missing()
    test_ttl_cache_custom_ttl()
    test_ttl_cache_invalidate()
    test_ttl_cache_invalidate_missing()
    test_ttl_cache_clear()
    test_ttl_cache_cleanup()
    test_ttl_cache_len()
    test_ttl_cache_contains()
    test_ttl_cache_overwrite()
    test_ttl_cache_different_types()
    test_ttl_cache_expired_on_get()

    print("\n" + "=" * 60)
    print("ALL CACHE TESTS PASSED!")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    run_all_tests()
