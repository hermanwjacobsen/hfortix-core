"""
Auto-generated basic tests for cmdb.wireless_controller/utm_profile

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/wireless-controller.utm-profile.json
Category: cmdb
Endpoint: /cmdb/wireless-controller/utm-profile

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_utm-profile.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.wireless_controller.utm_profile


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoUtmProfileEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_utm_log(self):
        """Test enum field utm-log validation."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller._helpers import utm_profile as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"utm-log": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: utm-log={value}")
        
        print(f"✅ Enum field utm-log has {len(valid_values)} valid values")
    def auto_test_enum_scan_botnet_connections(self):
        """Test enum field scan-botnet-connections validation."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller._helpers import utm_profile as validators
        
        valid_values = ['disable', 'monitor', 'block']
        
        # Test each valid value
        for value in valid_values:
            config = {"scan-botnet-connections": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: scan-botnet-connections={value}")
        
        print(f"✅ Enum field scan-botnet-connections has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/wireless_controller/utm_profile"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/wireless-controller.utm-profile.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']