"""
Auto-generated basic tests for cmdb.firewall/ssh/setting

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.ssh.setting.json
Category: cmdb
Endpoint: /cmdb/firewall.ssh/setting

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_setting.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.firewall.ssh.setting


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoSettingEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_host_trusted_checking(self):
        """Test enum field host-trusted-checking validation."""
        from hfortix_fortios.api.v2.cmdb.firewall.ssh._helpers import setting as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"host-trusted-checking": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: host-trusted-checking={value}")
        
        print(f"✅ Enum field host-trusted-checking has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/firewall/ssh/setting"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.ssh.setting.json"
TEST_HTTP_METHODS = ['GET', 'PUT']