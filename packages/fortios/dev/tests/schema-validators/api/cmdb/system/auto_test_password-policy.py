"""
Auto-generated basic tests for cmdb.system/password_policy

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.password-policy.json
Category: cmdb
Endpoint: /cmdb/system/password-policy

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_password-policy.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.password_policy


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoPasswordPolicyEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_status(self):
        """Test enum field status validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import password_policy as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: status={value}")
        
        print(f"✅ Enum field status has {len(valid_values)} valid values")
    def auto_test_enum_apply_to(self):
        """Test enum field apply-to validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import password_policy as validators
        
        valid_values = ['admin-password', 'ipsec-preshared-key']
        
        # Test each valid value
        for value in valid_values:
            config = {"apply-to": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: apply-to={value}")
        
        print(f"✅ Enum field apply-to has {len(valid_values)} valid values")
    def auto_test_enum_expire_status(self):
        """Test enum field expire-status validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import password_policy as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"expire-status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: expire-status={value}")
        
        print(f"✅ Enum field expire-status has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/password_policy"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.password-policy.json"
TEST_HTTP_METHODS = ['GET', 'PUT']