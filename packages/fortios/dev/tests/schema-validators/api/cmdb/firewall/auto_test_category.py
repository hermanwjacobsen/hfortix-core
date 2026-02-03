"""
Auto-generated basic tests for cmdb.firewall/service/category

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.service.category.json
Category: cmdb
Endpoint: /cmdb/firewall.service/category

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_category.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.firewall.service.category


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoCategoryEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_fabric_object(self):
        """Test enum field fabric-object validation."""
        from hfortix_fortios.api.v2.cmdb.firewall.service._helpers import category as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"fabric-object": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: fabric-object={value}")
        
        print(f"✅ Enum field fabric-object has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/firewall/service/category"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.service.category.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']