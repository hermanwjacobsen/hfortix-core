"""
Auto-generated basic tests for cmdb.ztna/web_portal

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/ztna.web-portal.json
Category: cmdb
Endpoint: /cmdb/ztna/web-portal

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_web-portal.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.ztna.web_portal


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoWebPortalEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_log_blocked_traffic(self):
        """Test enum field log-blocked-traffic validation."""
        from hfortix_fortios.api.v2.cmdb.ztna._helpers import web_portal as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"log-blocked-traffic": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: log-blocked-traffic={value}")
        
        print(f"✅ Enum field log-blocked-traffic has {len(valid_values)} valid values")
    def auto_test_enum_auth_portal(self):
        """Test enum field auth-portal validation."""
        from hfortix_fortios.api.v2.cmdb.ztna._helpers import web_portal as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"auth-portal": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: auth-portal={value}")
        
        print(f"✅ Enum field auth-portal has {len(valid_values)} valid values")
    def auto_test_enum_display_bookmark(self):
        """Test enum field display-bookmark validation."""
        from hfortix_fortios.api.v2.cmdb.ztna._helpers import web_portal as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"display-bookmark": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: display-bookmark={value}")
        
        print(f"✅ Enum field display-bookmark has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/ztna/web_portal"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/ztna.web-portal.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']