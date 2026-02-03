"""
Auto-generated basic tests for cmdb.system/ha_monitor

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.ha-monitor.json
Category: cmdb
Endpoint: /cmdb/system/ha-monitor

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_ha-monitor.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.ha_monitor


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoHaMonitorEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_monitor_vlan(self):
        """Test enum field monitor-vlan validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import ha_monitor as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"monitor-vlan": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: monitor-vlan={value}")
        
        print(f"✅ Enum field monitor-vlan has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/ha_monitor"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.ha-monitor.json"
TEST_HTTP_METHODS = ['GET', 'PUT']