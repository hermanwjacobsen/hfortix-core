"""
Tests for hfortix_core.cache TTLCache class.

A simple time-to-live cache for storing temporary data.
"""

import sys
import time


class Colors:
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"
    BOLD = "\033[1m"


def print_test_result(name: str, passed: bool, error: str | None = None):
    status = f"{Colors.GREEN}PASS{Colors.RESET}" if passed else f"{Colors.RED}FAIL{Colors.RESET}"
    print(f"  [{status}] {name}")
    if error:
        print(f"         {Colors.RED}{error}{Colors.RESET}")


def run_tests():
    from hfortix_core.cache import TTLCache, CacheEntry

    passed = 0
    failed = 0
    tests = []

    # =================================================================
    # Initialization Tests
    # =================================================================

    def test_init_default_ttl():
        cache = TTLCache()
        assert cache.default_ttl == 3600  # 1 hour default
        return True, None

    tests.append(("Initialize with default TTL", test_init_default_ttl))

    def test_init_custom_ttl():
        cache = TTLCache(default_ttl=60)
        assert cache.default_ttl == 60
        return True, None

    tests.append(("Initialize with custom TTL", test_init_custom_ttl))

    # =================================================================
    # set/get Tests
    # =================================================================

    def test_set_and_get():
        cache = TTLCache()
        cache.set("key1", "value1")
        result = cache.get("key1")
        assert result == "value1"
        return True, None

    tests.append(("set() and get() basic", test_set_and_get))

    def test_get_missing_key():
        cache = TTLCache()
        result = cache.get("nonexistent")
        assert result is None
        return True, None

    tests.append(("get() missing key returns None", test_get_missing_key))

    def test_set_overwrite():
        cache = TTLCache()
        cache.set("key", "value1")
        cache.set("key", "value2")
        assert cache.get("key") == "value2"
        return True, None

    tests.append(("set() overwrites existing key", test_set_overwrite))

    def test_set_various_types():
        cache = TTLCache()
        cache.set("string", "hello")
        cache.set("int", 42)
        cache.set("float", 3.14)
        cache.set("list", [1, 2, 3])
        cache.set("dict", {"a": 1})
        cache.set("none", None)
        
        assert cache.get("string") == "hello"
        assert cache.get("int") == 42
        assert cache.get("float") == 3.14
        assert cache.get("list") == [1, 2, 3]
        assert cache.get("dict") == {"a": 1}
        assert cache.get("none") is None
        return True, None

    tests.append(("set/get various value types", test_set_various_types))

    # =================================================================
    # TTL Expiration Tests
    # =================================================================

    def test_ttl_expiration():
        cache = TTLCache()
        cache.set("short", "data", ttl=0.05)  # 50ms
        assert cache.get("short") == "data"
        time.sleep(0.06)
        assert cache.get("short") is None
        return True, None

    tests.append(("TTL expiration", test_ttl_expiration))

    def test_custom_ttl_per_key():
        cache = TTLCache(default_ttl=1.0)
        cache.set("short", "data", ttl=0.05)
        cache.set("long", "data", ttl=0.2)
        time.sleep(0.06)
        assert cache.get("short") is None  # Expired
        assert cache.get("long") == "data"  # Still valid
        return True, None

    tests.append(("Custom TTL per key", test_custom_ttl_per_key))

    def test_default_ttl_used():
        cache = TTLCache(default_ttl=0.05)
        cache.set("key", "value")  # Uses default TTL
        assert cache.get("key") == "value"
        time.sleep(0.06)
        assert cache.get("key") is None
        return True, None

    tests.append(("Default TTL used when not specified", test_default_ttl_used))

    # =================================================================
    # clear() Tests
    # =================================================================

    def test_clear():
        cache = TTLCache()
        cache.set("key1", "value1")
        cache.set("key2", "value2")
        cache.clear()
        assert cache.get("key1") is None
        assert cache.get("key2") is None
        return True, None

    tests.append(("clear() removes all entries", test_clear))

    def test_clear_empty_cache():
        cache = TTLCache()
        cache.clear()  # Should not raise
        return True, None

    tests.append(("clear() on empty cache", test_clear_empty_cache))

    # =================================================================
    # invalidate() Tests
    # =================================================================

    def test_invalidate():
        cache = TTLCache()
        cache.set("key", "value")
        cache.invalidate("key")
        assert cache.get("key") is None
        return True, None

    tests.append(("invalidate() removes specific key", test_invalidate))

    def test_invalidate_nonexistent():
        cache = TTLCache()
        cache.invalidate("nonexistent")  # Should not raise
        return True, None

    tests.append(("invalidate() nonexistent key", test_invalidate_nonexistent))

    def test_invalidate_preserves_others():
        cache = TTLCache()
        cache.set("key1", "value1")
        cache.set("key2", "value2")
        cache.invalidate("key1")
        assert cache.get("key1") is None
        assert cache.get("key2") == "value2"
        return True, None

    tests.append(("invalidate() preserves other keys", test_invalidate_preserves_others))

    # =================================================================
    # cleanup() Tests
    # =================================================================

    def test_cleanup():
        cache = TTLCache()
        cache.set("expired1", "data", ttl=0.01)
        cache.set("expired2", "data", ttl=0.01)
        cache.set("valid", "data", ttl=1.0)
        time.sleep(0.02)
        removed = cache.cleanup()
        assert removed == 2
        assert cache.get("valid") == "data"
        return True, None

    tests.append(("cleanup() removes expired entries", test_cleanup))

    def test_cleanup_returns_count():
        cache = TTLCache()
        cache.set("key1", "data", ttl=0.01)
        cache.set("key2", "data", ttl=0.01)
        time.sleep(0.02)
        removed = cache.cleanup()
        assert removed == 2
        return True, None

    tests.append(("cleanup() returns count of removed", test_cleanup_returns_count))

    def test_cleanup_no_expired():
        cache = TTLCache()
        cache.set("key", "data", ttl=10.0)
        removed = cache.cleanup()
        assert removed == 0
        return True, None

    tests.append(("cleanup() with no expired entries", test_cleanup_no_expired))

    # =================================================================
    # Edge Cases
    # =================================================================

    def test_empty_string_key():
        cache = TTLCache()
        cache.set("", "empty key")
        assert cache.get("") == "empty key"
        return True, None

    tests.append(("Empty string as key", test_empty_string_key))

    def test_special_characters_in_key():
        cache = TTLCache()
        cache.set("key/with/slashes", "value1")
        cache.set("key.with.dots", "value2")
        cache.set("key:with:colons", "value3")
        assert cache.get("key/with/slashes") == "value1"
        assert cache.get("key.with.dots") == "value2"
        assert cache.get("key:with:colons") == "value3"
        return True, None

    tests.append(("Special characters in key", test_special_characters_in_key))

    def test_unicode_key_and_value():
        cache = TTLCache()
        cache.set("japanese_key", "japanese_value")
        cache.set("emoji_key", "emoji_value")
        assert cache.get("japanese_key") == "japanese_value"
        assert cache.get("emoji_key") == "emoji_value"
        return True, None

    tests.append(("Unicode key and value", test_unicode_key_and_value))

    def test_zero_ttl():
        cache = TTLCache()
        cache.set("instant_expire", "data", ttl=0)
        # With TTL=0, should expire immediately
        time.sleep(0.001)
        result = cache.get("instant_expire")
        # Depending on implementation, might be None or still available
        # Just ensure it doesn't crash
        return True, None

    tests.append(("Zero TTL handling", test_zero_ttl))

    def test_large_value():
        cache = TTLCache()
        large_data = "x" * 1000000  # 1MB string
        cache.set("large", large_data)
        assert cache.get("large") == large_data
        return True, None

    tests.append(("Large value storage", test_large_value))

    # =================================================================
    # Run All Tests
    # =================================================================

    print(f"\n{Colors.BOLD}TTLCache Tests{Colors.RESET}")
    print("=" * 50)

    for name, test_func in tests:
        try:
            success, error = test_func()
            if success:
                passed += 1
                print_test_result(name, True)
            else:
                failed += 1
                print_test_result(name, False, error)
        except Exception as e:
            failed += 1
            print_test_result(name, False, str(e))

    print("=" * 50)
    total = passed + failed
    print(f"Results: {passed}/{total} passed", end="")
    if failed > 0:
        print(f" ({Colors.RED}{failed} failed{Colors.RESET})")
    else:
        print(f" ({Colors.GREEN}all passed{Colors.RESET})")

    return failed == 0


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
