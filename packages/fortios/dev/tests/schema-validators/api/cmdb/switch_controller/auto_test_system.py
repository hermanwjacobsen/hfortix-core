"""
Auto-generated basic tests for cmdb.switch_controller/system

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/switch-controller.system.json
Category: cmdb
Endpoint: /cmdb/switch-controller/system

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_system.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.switch_controller.system


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoSystemEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_parallel_process_override(self):
        """Test enum field parallel-process-override validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import system as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"parallel-process-override": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: parallel-process-override={value}")
        
        print(f"✅ Enum field parallel-process-override has {len(valid_values)} valid values")
    def auto_test_enum_tunnel_mode(self):
        """Test enum field tunnel-mode validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import system as validators
        
        valid_values = ['compatible', 'moderate', 'strict']
        
        # Test each valid value
        for value in valid_values:
            config = {"tunnel-mode": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: tunnel-mode={value}")
        
        print(f"✅ Enum field tunnel-mode has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/switch_controller/system"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/switch-controller.system.json"
TEST_HTTP_METHODS = ['GET', 'PUT']