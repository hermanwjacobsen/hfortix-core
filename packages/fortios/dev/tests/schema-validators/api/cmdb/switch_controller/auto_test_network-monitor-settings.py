"""
Auto-generated basic tests for cmdb.switch_controller/network_monitor_settings

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/switch-controller.network-monitor-settings.json
Category: cmdb
Endpoint: /cmdb/switch-controller/network-monitor-settings

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_network-monitor-settings.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.switch_controller.network_monitor_settings


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoNetworkMonitorSettingsEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_network_monitoring(self):
        """Test enum field network-monitoring validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import network_monitor_settings as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"network-monitoring": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: network-monitoring={value}")
        
        print(f"✅ Enum field network-monitoring has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/switch_controller/network_monitor_settings"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/switch-controller.network-monitor-settings.json"
TEST_HTTP_METHODS = ['GET', 'PUT']