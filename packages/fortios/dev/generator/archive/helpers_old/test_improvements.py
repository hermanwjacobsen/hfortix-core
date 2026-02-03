"""
Smoke tests for improvements #6, #9, #13

Tests the three new features:
- #6: Readonly endpoint exists() method
- #9: Field deprecation warnings
- #13: TTL caching for readonly endpoints
"""

import sys
from pathlib import Path

# Add packages to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'packages/fortios'))
sys.path.insert(0, str(Path(__file__).parent.parent / 'packages/core'))


def test_readonly_caching():
    """Test #13: TTL caching for readonly endpoints."""
    print("🧪 Testing #13: Readonly caching...")
    
    from hfortix_core.cache import TTLCache, readonly_cache
    
    # Test basic cache operations
    cache = TTLCache[dict](default_ttl=60)
    
    # Set and get
    test_data = {"results": [{"id": "1", "name": "test"}]}
    cache.set("test_key", test_data)
    
    retrieved = cache.get("test_key")
    assert retrieved == test_data, "Cache retrieval failed"
    
    # Test expiration
    cache.set("expire_key", {"data": "value"}, ttl=0.001)  # 1ms TTL
    import time
    time.sleep(0.002)
    expired = cache.get("expire_key")
    assert expired is None, "Expired entry should return None"
    
    # Test global readonly_cache exists
    assert readonly_cache is not None, "Global readonly_cache not initialized"
    
    print("✅ Caching works correctly")


def test_deprecation_warnings():
    """Test #9: Field deprecation warnings."""
    print("\n🧪 Testing #9: Deprecation warnings...")
    
    from hfortix_core import check_deprecated_fields, warn_deprecated_field
    import warnings
    
    # Test warning emission
    deprecated_fields = {
        "old_field": {
            "reason": "No longer supported",
            "alternative": "new_field",
        }
    }
    
    payload = {"old_field": "value", "other_field": "data"}
    
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        check_deprecated_fields(
            payload=payload,
            deprecated_fields=deprecated_fields,
            endpoint="firewall/policy"
        )
        
        assert len(w) == 1, f"Expected 1 warning, got {len(w)}"
        assert "old_field" in str(w[0].message), "Warning doesn't mention field"
        assert "deprecated" in str(w[0].message).lower(), "Warning doesn't say deprecated"
    
    print("✅ Deprecation warnings work correctly")


def test_readonly_exists_implementation():
    """Test #6: Readonly endpoint exists() method."""
    print("\n🧪 Testing #6: Readonly exists() implementation...")
    
    # Check that generated readonly endpoint has proper exists() implementation
    from pathlib import Path
    
    # Try both relative and absolute paths
    base_path = Path(__file__).parent.parent
    endpoint_file = base_path / 'packages/fortios/hfortix_fortios/api/v2/cmdb/system/geoip_country.py'
    
    if not endpoint_file.exists():
        # Try absolute path
        endpoint_file = Path('/app/dev/classes/fortinet/packages/fortios/hfortix_fortios/api/v2/cmdb/system/geoip_country.py')
    
    if not endpoint_file.exists():
        print(f"⚠️  geoip_country endpoint not found at {endpoint_file}")
        return True
    
    with open(endpoint_file) as f:
        content = f.read()
    
    # Verify readonly-specific exists() logic
    assert "For readonly endpoints, check by fetching all items and scanning" in content, \
        "Missing readonly exists() comment"
    assert "response = self.get(vdom=vdom, raw_json=True)" in content, \
        "Readonly exists() should call get() without identifier"
    assert 'any(' in content and 'for item in results' in content, \
        "Readonly exists() should scan results list"
    
    print("✅ Readonly exists() properly implemented")


def test_generated_endpoint_structure():
    """Test that generated endpoints have all new features."""
    print("\n🧪 Testing generated endpoint structure...")
    
    from pathlib import Path
    
    # Try both relative and absolute paths
    base_path = Path(__file__).parent.parent
    endpoint_file = base_path / 'packages/fortios/hfortix_fortios/api/v2/cmdb/system/geoip_country.py'
    helper_file = base_path / 'packages/fortios/hfortix_fortios/api/v2/cmdb/system/_helpers/geoip_country.py'
    
    if not endpoint_file.exists():
        endpoint_file = Path('/app/dev/classes/fortinet/packages/fortios/hfortix_fortios/api/v2/cmdb/system/geoip_country.py')
        helper_file = Path('/app/dev/classes/fortinet/packages/fortios/hfortix_fortios/api/v2/cmdb/system/_helpers/geoip_country.py')
    
    if not endpoint_file.exists():
        print(f"⚠️  Endpoint file not found at {endpoint_file}, skipping")
        return True
    
    with open(endpoint_file) as f:
        endpoint_content = f.read()
    
    # Check cache import for readonly endpoints
    assert "from hfortix_core.cache import readonly_cache" in endpoint_content, \
        "Missing cache import in readonly endpoint"
    
    # Check caching logic
    assert "cache_key = f" in endpoint_content, \
        "Missing cache key generation"
    assert "cached_data = readonly_cache.get" in endpoint_content, \
        "Missing cache get operation"
    assert "readonly_cache.set" in endpoint_content, \
        "Missing cache set operation"
    
    with open(helper_file) as f:
        helper_content = f.read()
    
    # Check DEPRECATED_FIELDS constant
    assert "DEPRECATED_FIELDS = {" in helper_content, \
        "Missing DEPRECATED_FIELDS constant in helper"
    
    print("✅ Generated endpoints have all new features")

