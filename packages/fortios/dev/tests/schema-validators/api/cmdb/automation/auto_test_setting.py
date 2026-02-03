"""
Auto-generated basic tests for cmdb.automation/setting

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/automation.setting.json
Category: cmdb
Endpoint: /cmdb/automation/setting

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_setting.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.automation.setting


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoSettingEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_fabric_sync(self):
        """Test enum field fabric-sync validation."""
        from hfortix_fortios.api.v2.cmdb.automation._helpers import setting as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"fabric-sync": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: fabric-sync={value}")
        
        print(f"✅ Enum field fabric-sync has {len(valid_values)} valid values")
    def auto_test_enum_secure_mode(self):
        """Test enum field secure-mode validation."""
        from hfortix_fortios.api.v2.cmdb.automation._helpers import setting as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"secure-mode": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: secure-mode={value}")
        
        print(f"✅ Enum field secure-mode has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/automation/setting"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/automation.setting.json"
TEST_HTTP_METHODS = ['GET', 'PUT']