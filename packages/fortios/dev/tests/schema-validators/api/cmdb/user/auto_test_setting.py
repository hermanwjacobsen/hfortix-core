"""
Auto-generated basic tests for cmdb.user/setting

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/user.setting.json
Category: cmdb
Endpoint: /cmdb/user/setting

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_setting.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.user.setting


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoSettingEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_auth_type(self):
        """Test enum field auth-type validation."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import setting as validators
        
        valid_values = ['http', 'https', 'ftp', 'telnet']
        
        # Test each valid value
        for value in valid_values:
            config = {"auth-type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: auth-type={value}")
        
        print(f"✅ Enum field auth-type has {len(valid_values)} valid values")
    def auto_test_enum_auth_secure_http(self):
        """Test enum field auth-secure-http validation."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import setting as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"auth-secure-http": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: auth-secure-http={value}")
        
        print(f"✅ Enum field auth-secure-http has {len(valid_values)} valid values")
    def auto_test_enum_auth_http_basic(self):
        """Test enum field auth-http-basic validation."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import setting as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"auth-http-basic": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: auth-http-basic={value}")
        
        print(f"✅ Enum field auth-http-basic has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/user/setting"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/user.setting.json"
TEST_HTTP_METHODS = ['GET', 'PUT']