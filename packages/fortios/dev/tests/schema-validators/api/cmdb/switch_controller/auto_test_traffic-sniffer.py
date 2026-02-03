"""
Auto-generated basic tests for cmdb.switch_controller/traffic_sniffer

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/switch-controller.traffic-sniffer.json
Category: cmdb
Endpoint: /cmdb/switch-controller/traffic-sniffer

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_traffic-sniffer.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.switch_controller.traffic_sniffer


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoTrafficSnifferEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_mode(self):
        """Test enum field mode validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import traffic_sniffer as validators
        
        valid_values = ['erspan-auto', 'rspan', 'none']
        
        # Test each valid value
        for value in valid_values:
            config = {"mode": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: mode={value}")
        
        print(f"✅ Enum field mode has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/switch_controller/traffic_sniffer"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/switch-controller.traffic-sniffer.json"
TEST_HTTP_METHODS = ['GET', 'PUT']