"""
Auto-generated basic tests for cmdb.system/console

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.console.json
Category: cmdb
Endpoint: /cmdb/system/console

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_console.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.console


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoConsoleEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_output(self):
        """Test enum field output validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import console as validators
        
        valid_values = ['standard', 'more']
        
        # Test each valid value
        for value in valid_values:
            config = {"output": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: output={value}")
        
        print(f"✅ Enum field output has {len(valid_values)} valid values")
    def auto_test_enum_login(self):
        """Test enum field login validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import console as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"login": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: login={value}")
        
        print(f"✅ Enum field login has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/console"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.console.json"
TEST_HTTP_METHODS = ['GET', 'PUT']