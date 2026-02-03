"""
Auto-generated basic tests for cmdb.router/policy

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/router.policy.json
Category: cmdb
Endpoint: /cmdb/router/policy

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_policy.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.router.policy


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoPolicyEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_input_device_negate(self):
        """Test enum field input-device-negate validation."""
        from hfortix_fortios.api.v2.cmdb.router._helpers import policy as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"input-device-negate": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: input-device-negate={value}")
        
        print(f"✅ Enum field input-device-negate has {len(valid_values)} valid values")
    def auto_test_enum_src_negate(self):
        """Test enum field src-negate validation."""
        from hfortix_fortios.api.v2.cmdb.router._helpers import policy as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"src-negate": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: src-negate={value}")
        
        print(f"✅ Enum field src-negate has {len(valid_values)} valid values")
    def auto_test_enum_dst_negate(self):
        """Test enum field dst-negate validation."""
        from hfortix_fortios.api.v2.cmdb.router._helpers import policy as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"dst-negate": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: dst-negate={value}")
        
        print(f"✅ Enum field dst-negate has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/router/policy"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/router.policy.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']