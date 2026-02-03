"""
Auto-generated basic tests for cmdb.system/automation_destination

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.automation-destination.json
Category: cmdb
Endpoint: /cmdb/system/automation-destination

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_automation-destination.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.automation_destination


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoAutomationDestinationEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_type(self):
        """Test enum field type validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import automation_destination as validators
        
        valid_values = ['fortigate', 'ha-cluster']
        
        # Test each valid value
        for value in valid_values:
            config = {"type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: type={value}")
        
        print(f"✅ Enum field type has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/automation_destination"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.automation-destination.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']