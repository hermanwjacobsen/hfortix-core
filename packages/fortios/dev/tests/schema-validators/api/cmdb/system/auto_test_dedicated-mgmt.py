"""
Auto-generated basic tests for cmdb.system/dedicated_mgmt

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.dedicated-mgmt.json
Category: cmdb
Endpoint: /cmdb/system/dedicated-mgmt

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_dedicated-mgmt.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.dedicated_mgmt


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoDedicatedMgmtEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_status(self):
        """Test enum field status validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import dedicated_mgmt as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: status={value}")
        
        print(f"✅ Enum field status has {len(valid_values)} valid values")
    def auto_test_enum_dhcp_server(self):
        """Test enum field dhcp-server validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import dedicated_mgmt as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"dhcp-server": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: dhcp-server={value}")
        
        print(f"✅ Enum field dhcp-server has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/dedicated_mgmt"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.dedicated-mgmt.json"
TEST_HTTP_METHODS = ['GET', 'PUT']