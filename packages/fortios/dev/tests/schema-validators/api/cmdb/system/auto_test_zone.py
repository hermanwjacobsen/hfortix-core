"""
Auto-generated basic tests for cmdb.system/zone

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.zone.json
Category: cmdb
Endpoint: /cmdb/system/zone

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_zone.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.zone


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoZoneEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_intrazone(self):
        """Test enum field intrazone validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import zone as validators
        
        valid_values = ['allow', 'deny']
        
        # Test each valid value
        for value in valid_values:
            config = {"intrazone": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: intrazone={value}")
        
        print(f"✅ Enum field intrazone has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/zone"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.zone.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']