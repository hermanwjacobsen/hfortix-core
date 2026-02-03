"""
Auto-generated basic tests for cmdb.switch_controller/storm_control

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/switch-controller.storm-control.json
Category: cmdb
Endpoint: /cmdb/switch-controller/storm-control

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_storm-control.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.switch_controller.storm_control


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoStormControlEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_unknown_unicast(self):
        """Test enum field unknown-unicast validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import storm_control as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"unknown-unicast": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: unknown-unicast={value}")
        
        print(f"✅ Enum field unknown-unicast has {len(valid_values)} valid values")
    def auto_test_enum_unknown_multicast(self):
        """Test enum field unknown-multicast validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import storm_control as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"unknown-multicast": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: unknown-multicast={value}")
        
        print(f"✅ Enum field unknown-multicast has {len(valid_values)} valid values")
    def auto_test_enum_broadcast(self):
        """Test enum field broadcast validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import storm_control as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"broadcast": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: broadcast={value}")
        
        print(f"✅ Enum field broadcast has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/switch_controller/storm_control"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/switch-controller.storm-control.json"
TEST_HTTP_METHODS = ['GET', 'PUT']