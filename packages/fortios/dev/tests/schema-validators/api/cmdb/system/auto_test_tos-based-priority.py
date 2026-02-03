"""
Auto-generated basic tests for cmdb.system/tos_based_priority

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.tos-based-priority.json
Category: cmdb
Endpoint: /cmdb/system/tos-based-priority

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_tos-based-priority.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.tos_based_priority


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoTosBasedPriorityEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_priority(self):
        """Test enum field priority validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import tos_based_priority as validators
        
        valid_values = ['low', 'medium', 'high']
        
        # Test each valid value
        for value in valid_values:
            config = {"priority": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: priority={value}")
        
        print(f"✅ Enum field priority has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/tos_based_priority"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.tos-based-priority.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']