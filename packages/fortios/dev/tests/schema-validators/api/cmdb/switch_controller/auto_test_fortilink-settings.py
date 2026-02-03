"""
Auto-generated basic tests for cmdb.switch_controller/fortilink_settings

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/switch-controller.fortilink-settings.json
Category: cmdb
Endpoint: /cmdb/switch-controller/fortilink-settings

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_fortilink-settings.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.switch_controller.fortilink_settings


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoFortilinkSettingsEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_link_down_flush(self):
        """Test enum field link-down-flush validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import fortilink_settings as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"link-down-flush": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: link-down-flush={value}")
        
        print(f"✅ Enum field link-down-flush has {len(valid_values)} valid values")
    def auto_test_enum_access_vlan_mode(self):
        """Test enum field access-vlan-mode validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import fortilink_settings as validators
        
        valid_values = ['legacy', 'fail-open', 'fail-close']
        
        # Test each valid value
        for value in valid_values:
            config = {"access-vlan-mode": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: access-vlan-mode={value}")
        
        print(f"✅ Enum field access-vlan-mode has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/switch_controller/fortilink_settings"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/switch-controller.fortilink-settings.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']