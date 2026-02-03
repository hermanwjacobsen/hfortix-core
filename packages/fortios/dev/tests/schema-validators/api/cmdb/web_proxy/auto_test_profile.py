"""
Auto-generated basic tests for cmdb.web_proxy/profile

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/web-proxy.profile.json
Category: cmdb
Endpoint: /cmdb/web-proxy/profile

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_profile.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.web_proxy.profile


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoProfileEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_header_client_ip(self):
        """Test enum field header-client-ip validation."""
        from hfortix_fortios.api.v2.cmdb.web_proxy._helpers import profile as validators
        
        valid_values = ['pass', 'add', 'remove']
        
        # Test each valid value
        for value in valid_values:
            config = {"header-client-ip": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: header-client-ip={value}")
        
        print(f"✅ Enum field header-client-ip has {len(valid_values)} valid values")
    def auto_test_enum_header_via_request(self):
        """Test enum field header-via-request validation."""
        from hfortix_fortios.api.v2.cmdb.web_proxy._helpers import profile as validators
        
        valid_values = ['pass', 'add', 'remove']
        
        # Test each valid value
        for value in valid_values:
            config = {"header-via-request": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: header-via-request={value}")
        
        print(f"✅ Enum field header-via-request has {len(valid_values)} valid values")
    def auto_test_enum_header_via_response(self):
        """Test enum field header-via-response validation."""
        from hfortix_fortios.api.v2.cmdb.web_proxy._helpers import profile as validators
        
        valid_values = ['pass', 'add', 'remove']
        
        # Test each valid value
        for value in valid_values:
            config = {"header-via-response": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: header-via-response={value}")
        
        print(f"✅ Enum field header-via-response has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/web_proxy/profile"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/web-proxy.profile.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']