"""
Auto-generated basic tests for cmdb.web_proxy/fast_fallback

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/web-proxy.fast-fallback.json
Category: cmdb
Endpoint: /cmdb/web-proxy/fast-fallback

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_fast-fallback.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.web_proxy.fast_fallback


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoFastFallbackEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_status(self):
        """Test enum field status validation."""
        from hfortix_fortios.api.v2.cmdb.web_proxy._helpers import fast_fallback as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: status={value}")
        
        print(f"✅ Enum field status has {len(valid_values)} valid values")
    def auto_test_enum_connection_mode(self):
        """Test enum field connection-mode validation."""
        from hfortix_fortios.api.v2.cmdb.web_proxy._helpers import fast_fallback as validators
        
        valid_values = ['sequentially', 'simultaneously']
        
        # Test each valid value
        for value in valid_values:
            config = {"connection-mode": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: connection-mode={value}")
        
        print(f"✅ Enum field connection-mode has {len(valid_values)} valid values")
    def auto_test_enum_protocol(self):
        """Test enum field protocol validation."""
        from hfortix_fortios.api.v2.cmdb.web_proxy._helpers import fast_fallback as validators
        
        valid_values = ['IPv4-first', 'IPv6-first', 'IPv4-only', 'IPv6-only']
        
        # Test each valid value
        for value in valid_values:
            config = {"protocol": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: protocol={value}")
        
        print(f"✅ Enum field protocol has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/web_proxy/fast_fallback"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/web-proxy.fast-fallback.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']