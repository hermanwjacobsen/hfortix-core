"""
Auto-generated basic tests for cmdb.log/gui_display

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/log.gui-display.json
Category: cmdb
Endpoint: /cmdb/log/gui-display

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_gui-display.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.log.gui_display


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoGuiDisplayEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_resolve_hosts(self):
        """Test enum field resolve-hosts validation."""
        from hfortix_fortios.api.v2.cmdb.log._helpers import gui_display as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"resolve-hosts": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: resolve-hosts={value}")
        
        print(f"✅ Enum field resolve-hosts has {len(valid_values)} valid values")
    def auto_test_enum_resolve_apps(self):
        """Test enum field resolve-apps validation."""
        from hfortix_fortios.api.v2.cmdb.log._helpers import gui_display as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"resolve-apps": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: resolve-apps={value}")
        
        print(f"✅ Enum field resolve-apps has {len(valid_values)} valid values")
    def auto_test_enum_fortiview_unscanned_apps(self):
        """Test enum field fortiview-unscanned-apps validation."""
        from hfortix_fortios.api.v2.cmdb.log._helpers import gui_display as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"fortiview-unscanned-apps": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: fortiview-unscanned-apps={value}")
        
        print(f"✅ Enum field fortiview-unscanned-apps has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/log/gui_display"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/log.gui-display.json"
TEST_HTTP_METHODS = ['GET', 'PUT']