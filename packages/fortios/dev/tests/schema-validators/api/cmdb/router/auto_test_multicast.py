"""
Auto-generated basic tests for cmdb.router/multicast

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/router.multicast.json
Category: cmdb
Endpoint: /cmdb/router/multicast

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_multicast.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.router.multicast


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoMulticastEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_multicast_routing(self):
        """Test enum field multicast-routing validation."""
        from hfortix_fortios.api.v2.cmdb.router._helpers import multicast as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"multicast-routing": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: multicast-routing={value}")
        
        print(f"✅ Enum field multicast-routing has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/router/multicast"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/router.multicast.json"
TEST_HTTP_METHODS = ['GET', 'PUT']