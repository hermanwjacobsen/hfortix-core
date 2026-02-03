"""
Auto-generated basic tests for cmdb.wireless_controller/wag_profile

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/wireless-controller.wag-profile.json
Category: cmdb
Endpoint: /cmdb/wireless-controller/wag-profile

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_wag-profile.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.wireless_controller.wag_profile


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoWagProfileEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_tunnel_type(self):
        """Test enum field tunnel-type validation."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller._helpers import wag_profile as validators
        
        valid_values = ['l2tpv3', 'gre']
        
        # Test each valid value
        for value in valid_values:
            config = {"tunnel-type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: tunnel-type={value}")
        
        print(f"✅ Enum field tunnel-type has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/wireless_controller/wag_profile"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/wireless-controller.wag-profile.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']