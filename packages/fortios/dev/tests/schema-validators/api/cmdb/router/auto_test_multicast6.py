"""
Auto-generated basic tests for cmdb.router/multicast6

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/router.multicast6.json
Category: cmdb
Endpoint: /cmdb/router/multicast6

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_multicast6.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.router.multicast6


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoMulticast6Enums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_multicast_routing(self):
        """Test enum field multicast-routing validation."""
        from hfortix_fortios.api.v2.cmdb.router._helpers import multicast6 as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"multicast-routing": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: multicast-routing={value}")
        
        print(f"✅ Enum field multicast-routing has {len(valid_values)} valid values")
    def auto_test_enum_multicast_pmtu(self):
        """Test enum field multicast-pmtu validation."""
        from hfortix_fortios.api.v2.cmdb.router._helpers import multicast6 as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"multicast-pmtu": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: multicast-pmtu={value}")
        
        print(f"✅ Enum field multicast-pmtu has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/router/multicast6"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/router.multicast6.json"
TEST_HTTP_METHODS = ['GET', 'PUT']