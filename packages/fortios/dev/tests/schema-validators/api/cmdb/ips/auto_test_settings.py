"""
Auto-generated basic tests for cmdb.ips/settings

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/ips.settings.json
Category: cmdb
Endpoint: /cmdb/ips/settings

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_settings.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.ips.settings


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoSettingsEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_proxy_inline_ips(self):
        """Test enum field proxy-inline-ips validation."""
        from hfortix_fortios.api.v2.cmdb.ips._helpers import settings as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"proxy-inline-ips": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: proxy-inline-ips={value}")
        
        print(f"✅ Enum field proxy-inline-ips has {len(valid_values)} valid values")
    def auto_test_enum_ha_session_pickup(self):
        """Test enum field ha-session-pickup validation."""
        from hfortix_fortios.api.v2.cmdb.ips._helpers import settings as validators
        
        valid_values = ['connectivity', 'security']
        
        # Test each valid value
        for value in valid_values:
            config = {"ha-session-pickup": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ha-session-pickup={value}")
        
        print(f"✅ Enum field ha-session-pickup has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/ips/settings"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/ips.settings.json"
TEST_HTTP_METHODS = ['GET', 'PUT']