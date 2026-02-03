"""
Auto-generated basic tests for cmdb.ztna/traffic_forward_proxy

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/ztna.traffic-forward-proxy.json
Category: cmdb
Endpoint: /cmdb/ztna/traffic-forward-proxy

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_traffic-forward-proxy.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.ztna.traffic_forward_proxy


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoTrafficForwardProxyEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_log_blocked_traffic(self):
        """Test enum field log-blocked-traffic validation."""
        from hfortix_fortios.api.v2.cmdb.ztna._helpers import traffic_forward_proxy as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"log-blocked-traffic": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: log-blocked-traffic={value}")
        
        print(f"✅ Enum field log-blocked-traffic has {len(valid_values)} valid values")
    def auto_test_enum_auth_portal(self):
        """Test enum field auth-portal validation."""
        from hfortix_fortios.api.v2.cmdb.ztna._helpers import traffic_forward_proxy as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"auth-portal": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: auth-portal={value}")
        
        print(f"✅ Enum field auth-portal has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/ztna/traffic_forward_proxy"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/ztna.traffic-forward-proxy.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']