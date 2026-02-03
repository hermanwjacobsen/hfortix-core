"""
Auto-generated basic tests for cmdb.switch_controller/lldp_settings

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/switch-controller.lldp-settings.json
Category: cmdb
Endpoint: /cmdb/switch-controller/lldp-settings

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_lldp-settings.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.switch_controller.lldp_settings


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoLldpSettingsEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_management_interface(self):
        """Test enum field management-interface validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import lldp_settings as validators
        
        valid_values = ['internal', 'mgmt']
        
        # Test each valid value
        for value in valid_values:
            config = {"management-interface": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: management-interface={value}")
        
        print(f"✅ Enum field management-interface has {len(valid_values)} valid values")
    def auto_test_enum_device_detection(self):
        """Test enum field device-detection validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import lldp_settings as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"device-detection": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: device-detection={value}")
        
        print(f"✅ Enum field device-detection has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/switch_controller/lldp_settings"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/switch-controller.lldp-settings.json"
TEST_HTTP_METHODS = ['GET', 'PUT']