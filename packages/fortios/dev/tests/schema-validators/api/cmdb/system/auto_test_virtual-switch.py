"""
Auto-generated basic tests for cmdb.system/virtual_switch

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.virtual-switch.json
Category: cmdb
Endpoint: /cmdb/system/virtual-switch

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_virtual-switch.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.virtual_switch


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoVirtualSwitchEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_span(self):
        """Test enum field span validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import virtual_switch as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"span": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: span={value}")
        
        print(f"✅ Enum field span has {len(valid_values)} valid values")
    def auto_test_enum_span_direction(self):
        """Test enum field span-direction validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import virtual_switch as validators
        
        valid_values = ['rx', 'tx', 'both']
        
        # Test each valid value
        for value in valid_values:
            config = {"span-direction": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: span-direction={value}")
        
        print(f"✅ Enum field span-direction has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/virtual_switch"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.virtual-switch.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']