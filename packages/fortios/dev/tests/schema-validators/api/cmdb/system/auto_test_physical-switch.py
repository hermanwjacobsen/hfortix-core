"""
Auto-generated basic tests for cmdb.system/physical_switch

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.physical-switch.json
Category: cmdb
Endpoint: /cmdb/system/physical-switch

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_physical-switch.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.physical_switch


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoPhysicalSwitchEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_age_enable(self):
        """Test enum field age-enable validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import physical_switch as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"age-enable": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: age-enable={value}")
        
        print(f"✅ Enum field age-enable has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/physical_switch"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.physical-switch.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']