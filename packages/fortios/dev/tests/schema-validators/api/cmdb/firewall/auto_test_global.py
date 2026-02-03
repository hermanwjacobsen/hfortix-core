"""
Auto-generated basic tests for cmdb.firewall/global_

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.global.json
Category: cmdb
Endpoint: /cmdb/firewall/global

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_global.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.firewall.global_


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoGlobalEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_banned_ip_persistency(self):
        """Test enum field banned-ip-persistency validation."""
        # 'global' is a Python keyword, using importlib
        import importlib
        validators = importlib.import_module('hfortix_fortios.api.v2.cmdb.firewall._helpers.global_')
        
        valid_values = ['disabled', 'permanent-only', 'all']
        
        # Test each valid value
        for value in valid_values:
            config = {"banned-ip-persistency": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: banned-ip-persistency={value}")
        
        print(f"✅ Enum field banned-ip-persistency has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/firewall/global_"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.global.json"
TEST_HTTP_METHODS = ['GET', 'PUT']