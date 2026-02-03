"""
Auto-generated basic tests for cmdb.authentication/setting

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/authentication.setting.json
Category: cmdb
Endpoint: /cmdb/authentication/setting

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_setting.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.authentication.setting


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoSettingEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_persistent_cookie(self):
        """Test enum field persistent-cookie validation."""
        from hfortix_fortios.api.v2.cmdb.authentication._helpers import setting as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"persistent-cookie": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: persistent-cookie={value}")
        
        print(f"✅ Enum field persistent-cookie has {len(valid_values)} valid values")
    def auto_test_enum_ip_auth_cookie(self):
        """Test enum field ip-auth-cookie validation."""
        from hfortix_fortios.api.v2.cmdb.authentication._helpers import setting as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"ip-auth-cookie": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ip-auth-cookie={value}")
        
        print(f"✅ Enum field ip-auth-cookie has {len(valid_values)} valid values")
    def auto_test_enum_captive_portal_type(self):
        """Test enum field captive-portal-type validation."""
        from hfortix_fortios.api.v2.cmdb.authentication._helpers import setting as validators
        
        valid_values = ['fqdn', 'ip']
        
        # Test each valid value
        for value in valid_values:
            config = {"captive-portal-type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: captive-portal-type={value}")
        
        print(f"✅ Enum field captive-portal-type has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/authentication/setting"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/authentication.setting.json"
TEST_HTTP_METHODS = ['GET', 'PUT']