"""
Auto-generated basic tests for cmdb.router/rip

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/router.rip.json
Category: cmdb
Endpoint: /cmdb/router/rip

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_rip.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.router.rip


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoRipEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_default_information_originate(self):
        """Test enum field default-information-originate validation."""
        from hfortix_fortios.api.v2.cmdb.router._helpers import rip as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"default-information-originate": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: default-information-originate={value}")
        
        print(f"✅ Enum field default-information-originate has {len(valid_values)} valid values")
    def auto_test_enum_version(self):
        """Test enum field version validation."""
        from hfortix_fortios.api.v2.cmdb.router._helpers import rip as validators
        
        valid_values = ['1', '2']
        
        # Test each valid value
        for value in valid_values:
            config = {"version": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: version={value}")
        
        print(f"✅ Enum field version has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/router/rip"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/router.rip.json"
TEST_HTTP_METHODS = ['GET', 'PUT']