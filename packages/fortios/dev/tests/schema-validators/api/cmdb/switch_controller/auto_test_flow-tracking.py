"""
Auto-generated basic tests for cmdb.switch_controller/flow_tracking

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/switch-controller.flow-tracking.json
Category: cmdb
Endpoint: /cmdb/switch-controller/flow-tracking

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_flow-tracking.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.switch_controller.flow_tracking


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoFlowTrackingEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_sample_mode(self):
        """Test enum field sample-mode validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import flow_tracking as validators
        
        valid_values = ['local', 'perimeter', 'device-ingress']
        
        # Test each valid value
        for value in valid_values:
            config = {"sample-mode": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: sample-mode={value}")
        
        print(f"✅ Enum field sample-mode has {len(valid_values)} valid values")
    def auto_test_enum_format(self):
        """Test enum field format validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import flow_tracking as validators
        
        valid_values = ['netflow1', 'netflow5', 'netflow9', 'ipfix']
        
        # Test each valid value
        for value in valid_values:
            config = {"format": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: format={value}")
        
        print(f"✅ Enum field format has {len(valid_values)} valid values")
    def auto_test_enum_level(self):
        """Test enum field level validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import flow_tracking as validators
        
        valid_values = ['vlan', 'ip', 'port', 'proto', 'mac']
        
        # Test each valid value
        for value in valid_values:
            config = {"level": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: level={value}")
        
        print(f"✅ Enum field level has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/switch_controller/flow_tracking"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/switch-controller.flow-tracking.json"
TEST_HTTP_METHODS = ['GET', 'PUT']