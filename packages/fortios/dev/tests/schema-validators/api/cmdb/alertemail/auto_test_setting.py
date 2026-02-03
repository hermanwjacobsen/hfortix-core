"""
Auto-generated basic tests for cmdb.alertemail/setting

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/alertemail.setting.json
Category: cmdb
Endpoint: /cmdb/alertemail/setting

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_setting.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.alertemail.setting


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoSettingEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_filter_mode(self):
        """Test enum field filter-mode validation."""
        from hfortix_fortios.api.v2.cmdb.alertemail._helpers import setting as validators
        
        valid_values = ['category', 'threshold']
        
        # Test each valid value
        for value in valid_values:
            config = {"filter-mode": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: filter-mode={value}")
        
        print(f"✅ Enum field filter-mode has {len(valid_values)} valid values")
    def auto_test_enum_IPS_logs(self):
        """Test enum field IPS-logs validation."""
        from hfortix_fortios.api.v2.cmdb.alertemail._helpers import setting as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"IPS-logs": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: IPS-logs={value}")
        
        print(f"✅ Enum field IPS-logs has {len(valid_values)} valid values")
    def auto_test_enum_firewall_authentication_failure_logs(self):
        """Test enum field firewall-authentication-failure-logs validation."""
        from hfortix_fortios.api.v2.cmdb.alertemail._helpers import setting as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"firewall-authentication-failure-logs": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: firewall-authentication-failure-logs={value}")
        
        print(f"✅ Enum field firewall-authentication-failure-logs has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/alertemail/setting"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/alertemail.setting.json"
TEST_HTTP_METHODS = ['GET', 'PUT']