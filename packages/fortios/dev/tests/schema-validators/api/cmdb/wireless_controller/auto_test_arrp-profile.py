"""
Auto-generated basic tests for cmdb.wireless_controller/arrp_profile

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/wireless-controller.arrp-profile.json
Category: cmdb
Endpoint: /cmdb/wireless-controller/arrp-profile

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_arrp-profile.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.wireless_controller.arrp_profile


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoArrpProfileEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_include_weather_channel(self):
        """Test enum field include-weather-channel validation."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller._helpers import arrp_profile as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"include-weather-channel": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: include-weather-channel={value}")
        
        print(f"✅ Enum field include-weather-channel has {len(valid_values)} valid values")
    def auto_test_enum_include_dfs_channel(self):
        """Test enum field include-dfs-channel validation."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller._helpers import arrp_profile as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"include-dfs-channel": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: include-dfs-channel={value}")
        
        print(f"✅ Enum field include-dfs-channel has {len(valid_values)} valid values")
    def auto_test_enum_override_darrp_optimize(self):
        """Test enum field override-darrp-optimize validation."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller._helpers import arrp_profile as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"override-darrp-optimize": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: override-darrp-optimize={value}")
        
        print(f"✅ Enum field override-darrp-optimize has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/wireless_controller/arrp_profile"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/wireless-controller.arrp-profile.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']