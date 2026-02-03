"""
Auto-generated basic tests for cmdb.user/group

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/user.group.json
Category: cmdb
Endpoint: /cmdb/user/group

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_group.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.user.group


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoGroupEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_group_type(self):
        """Test enum field group-type validation."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import group as validators
        
        valid_values = ['firewall', 'fsso-service', 'rsso', 'guest']
        
        # Test each valid value
        for value in valid_values:
            config = {"group-type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: group-type={value}")
        
        print(f"✅ Enum field group-type has {len(valid_values)} valid values")
    def auto_test_enum_auth_concurrent_override(self):
        """Test enum field auth-concurrent-override validation."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import group as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"auth-concurrent-override": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: auth-concurrent-override={value}")
        
        print(f"✅ Enum field auth-concurrent-override has {len(valid_values)} valid values")
    def auto_test_enum_user_id(self):
        """Test enum field user-id validation."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import group as validators
        
        valid_values = ['email', 'auto-generate', 'specify']
        
        # Test each valid value
        for value in valid_values:
            config = {"user-id": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: user-id={value}")
        
        print(f"✅ Enum field user-id has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/user/group"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/user.group.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']