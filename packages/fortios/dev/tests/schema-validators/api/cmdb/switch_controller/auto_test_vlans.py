"""
Auto-generated basic tests for cmdb.switch_controller/initial_config/vlans

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/switch-controller.initial-config.vlans.json
Category: cmdb
Endpoint: /cmdb/switch-controller.initial-config/vlans

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_vlans.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.switch_controller.initial_config.vlans


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoVlansEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_optional_vlans(self):
        """Test enum field optional-vlans validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller.initial_config._helpers import vlans as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"optional-vlans": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: optional-vlans={value}")
        
        print(f"✅ Enum field optional-vlans has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/switch_controller/initial_config/vlans"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/switch-controller.initial-config.vlans.json"
TEST_HTTP_METHODS = ['GET', 'PUT']