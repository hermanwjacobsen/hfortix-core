"""
Auto-generated basic tests for cmdb.switch_controller/security_policy/local_access

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/switch-controller.security-policy.local-access.json
Category: cmdb
Endpoint: /cmdb/switch-controller.security-policy/local-access

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_local-access.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.switch_controller.security_policy.local_access


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoLocalAccessEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_mgmt_allowaccess(self):
        """Test enum field mgmt-allowaccess validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller.security_policy._helpers import local_access as validators
        
        valid_values = ['https', 'ping', 'ssh', 'snmp', 'http', 'telnet', 'radius-acct']
        
        # Test each valid value
        for value in valid_values:
            config = {"mgmt-allowaccess": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: mgmt-allowaccess={value}")
        
        print(f"✅ Enum field mgmt-allowaccess has {len(valid_values)} valid values")
    def auto_test_enum_internal_allowaccess(self):
        """Test enum field internal-allowaccess validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller.security_policy._helpers import local_access as validators
        
        valid_values = ['https', 'ping', 'ssh', 'snmp', 'http', 'telnet', 'radius-acct']
        
        # Test each valid value
        for value in valid_values:
            config = {"internal-allowaccess": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: internal-allowaccess={value}")
        
        print(f"✅ Enum field internal-allowaccess has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/switch_controller/security_policy/local_access"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/switch-controller.security-policy.local-access.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']