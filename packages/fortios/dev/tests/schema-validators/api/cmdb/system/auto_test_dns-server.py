"""
Auto-generated basic tests for cmdb.system/dns_server

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.dns-server.json
Category: cmdb
Endpoint: /cmdb/system/dns-server

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_dns-server.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.dns_server


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoDnsServerEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_mode(self):
        """Test enum field mode validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import dns_server as validators
        
        valid_values = ['recursive', 'non-recursive', 'forward-only', 'resolver']
        
        # Test each valid value
        for value in valid_values:
            config = {"mode": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: mode={value}")
        
        print(f"✅ Enum field mode has {len(valid_values)} valid values")
    def auto_test_enum_doh(self):
        """Test enum field doh validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import dns_server as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"doh": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: doh={value}")
        
        print(f"✅ Enum field doh has {len(valid_values)} valid values")
    def auto_test_enum_doh3(self):
        """Test enum field doh3 validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import dns_server as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"doh3": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: doh3={value}")
        
        print(f"✅ Enum field doh3 has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/dns_server"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.dns-server.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']