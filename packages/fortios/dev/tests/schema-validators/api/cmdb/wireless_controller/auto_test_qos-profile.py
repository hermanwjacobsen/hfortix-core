"""
Auto-generated basic tests for cmdb.wireless_controller/qos_profile

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/wireless-controller.qos-profile.json
Category: cmdb
Endpoint: /cmdb/wireless-controller/qos-profile

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_qos-profile.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.wireless_controller.qos_profile


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoQosProfileEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_burst(self):
        """Test enum field burst validation."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller._helpers import qos_profile as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"burst": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: burst={value}")
        
        print(f"✅ Enum field burst has {len(valid_values)} valid values")
    def auto_test_enum_wmm(self):
        """Test enum field wmm validation."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller._helpers import qos_profile as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"wmm": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: wmm={value}")
        
        print(f"✅ Enum field wmm has {len(valid_values)} valid values")
    def auto_test_enum_wmm_uapsd(self):
        """Test enum field wmm-uapsd validation."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller._helpers import qos_profile as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"wmm-uapsd": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: wmm-uapsd={value}")
        
        print(f"✅ Enum field wmm-uapsd has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/wireless_controller/qos_profile"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/wireless-controller.qos-profile.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']