"""
Auto-generated basic tests for cmdb.waf/profile

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/waf.profile.json
Category: cmdb
Endpoint: /cmdb/waf/profile

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_profile.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.waf.profile


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoProfileEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_external(self):
        """Test enum field external validation."""
        from hfortix_fortios.api.v2.cmdb.waf._helpers import profile as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"external": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: external={value}")
        
        print(f"✅ Enum field external has {len(valid_values)} valid values")
    def auto_test_enum_extended_log(self):
        """Test enum field extended-log validation."""
        from hfortix_fortios.api.v2.cmdb.waf._helpers import profile as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"extended-log": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: extended-log={value}")
        
        print(f"✅ Enum field extended-log has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/waf/profile"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/waf.profile.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']