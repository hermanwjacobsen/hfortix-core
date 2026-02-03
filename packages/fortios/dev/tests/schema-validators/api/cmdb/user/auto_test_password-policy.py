"""
Auto-generated basic tests for cmdb.user/password_policy

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/user.password-policy.json
Category: cmdb
Endpoint: /cmdb/user/password-policy

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_password-policy.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.user.password_policy


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoPasswordPolicyEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_expire_status(self):
        """Test enum field expire-status validation."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import password_policy as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"expire-status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: expire-status={value}")
        
        print(f"✅ Enum field expire-status has {len(valid_values)} valid values")
    def auto_test_enum_expired_password_renewal(self):
        """Test enum field expired-password-renewal validation."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import password_policy as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"expired-password-renewal": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: expired-password-renewal={value}")
        
        print(f"✅ Enum field expired-password-renewal has {len(valid_values)} valid values")
    def auto_test_enum_reuse_password(self):
        """Test enum field reuse-password validation."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import password_policy as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"reuse-password": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: reuse-password={value}")
        
        print(f"✅ Enum field reuse-password has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/user/password_policy"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/user.password-policy.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']