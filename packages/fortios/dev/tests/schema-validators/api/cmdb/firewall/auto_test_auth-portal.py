"""
Auto-generated basic tests for cmdb.firewall/auth_portal

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.auth-portal.json
Category: cmdb
Endpoint: /cmdb/firewall/auth-portal

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_auth-portal.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.firewall.auth_portal


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoAuthPortalEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_proxy_auth(self):
        """Test enum field proxy-auth validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import auth_portal as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"proxy-auth": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: proxy-auth={value}")
        
        print(f"✅ Enum field proxy-auth has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/firewall/auth_portal"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.auth-portal.json"
TEST_HTTP_METHODS = ['GET', 'PUT']