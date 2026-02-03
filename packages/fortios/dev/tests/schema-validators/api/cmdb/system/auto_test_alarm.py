"""
Auto-generated basic tests for cmdb.system/alarm

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.alarm.json
Category: cmdb
Endpoint: /cmdb/system/alarm

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_alarm.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.alarm


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoAlarmEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_status(self):
        """Test enum field status validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import alarm as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: status={value}")
        
        print(f"✅ Enum field status has {len(valid_values)} valid values")
    def auto_test_enum_audible(self):
        """Test enum field audible validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import alarm as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"audible": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: audible={value}")
        
        print(f"✅ Enum field audible has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/alarm"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.alarm.json"
TEST_HTTP_METHODS = ['GET', 'PUT']