"""
Auto-generated basic tests for cmdb.switch_controller/x802_1x_settings

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/switch-controller.802-1X-settings.json
Category: cmdb
Endpoint: /cmdb/switch-controller/802-1X-settings

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_802-1X-settings.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.switch_controller.x802_1x_settings


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoX8021xSettingsEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_link_down_auth(self):
        """Test enum field link-down-auth validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import x802_1x_settings as validators
        
        valid_values = ['set-unauth', 'no-action']
        
        # Test each valid value
        for value in valid_values:
            config = {"link-down-auth": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: link-down-auth={value}")
        
        print(f"✅ Enum field link-down-auth has {len(valid_values)} valid values")
    def auto_test_enum_mab_reauth(self):
        """Test enum field mab-reauth validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import x802_1x_settings as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"mab-reauth": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: mab-reauth={value}")
        
        print(f"✅ Enum field mab-reauth has {len(valid_values)} valid values")
    def auto_test_enum_mac_username_delimiter(self):
        """Test enum field mac-username-delimiter validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import x802_1x_settings as validators
        
        valid_values = ['colon', 'hyphen', 'none', 'single-hyphen']
        
        # Test each valid value
        for value in valid_values:
            config = {"mac-username-delimiter": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: mac-username-delimiter={value}")
        
        print(f"✅ Enum field mac-username-delimiter has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/switch_controller/x802_1x_settings"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/switch-controller.802-1X-settings.json"
TEST_HTTP_METHODS = ['GET', 'PUT']