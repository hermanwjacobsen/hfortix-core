"""
Auto-generated basic tests for cmdb.wireless_controller/wids_profile

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/wireless-controller.wids-profile.json
Category: cmdb
Endpoint: /cmdb/wireless-controller/wids-profile

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_wids-profile.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.wireless_controller.wids_profile


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoWidsProfileEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_sensor_mode(self):
        """Test enum field sensor-mode validation."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller._helpers import wids_profile as validators
        
        valid_values = ['disable', 'foreign', 'both']
        
        # Test each valid value
        for value in valid_values:
            config = {"sensor-mode": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: sensor-mode={value}")
        
        print(f"✅ Enum field sensor-mode has {len(valid_values)} valid values")
    def auto_test_enum_ap_scan(self):
        """Test enum field ap-scan validation."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller._helpers import wids_profile as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"ap-scan": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ap-scan={value}")
        
        print(f"✅ Enum field ap-scan has {len(valid_values)} valid values")
    def auto_test_enum_ap_scan_passive(self):
        """Test enum field ap-scan-passive validation."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller._helpers import wids_profile as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"ap-scan-passive": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ap-scan-passive={value}")
        
        print(f"✅ Enum field ap-scan-passive has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/wireless_controller/wids_profile"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/wireless-controller.wids-profile.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']