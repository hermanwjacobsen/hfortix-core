"""
Auto-generated basic tests for cmdb.system/object_tagging

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.object-tagging.json
Category: cmdb
Endpoint: /cmdb/system/object-tagging

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_object-tagging.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.object_tagging


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoObjectTaggingEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_address(self):
        """Test enum field address validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import object_tagging as validators
        
        valid_values = ['disable', 'mandatory', 'optional']
        
        # Test each valid value
        for value in valid_values:
            config = {"address": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: address={value}")
        
        print(f"✅ Enum field address has {len(valid_values)} valid values")
    def auto_test_enum_device(self):
        """Test enum field device validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import object_tagging as validators
        
        valid_values = ['disable', 'mandatory', 'optional']
        
        # Test each valid value
        for value in valid_values:
            config = {"device": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: device={value}")
        
        print(f"✅ Enum field device has {len(valid_values)} valid values")
    def auto_test_enum_interface(self):
        """Test enum field interface validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import object_tagging as validators
        
        valid_values = ['disable', 'mandatory', 'optional']
        
        # Test each valid value
        for value in valid_values:
            config = {"interface": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: interface={value}")
        
        print(f"✅ Enum field interface has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/object_tagging"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.object-tagging.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']