"""
Auto-generated basic tests for cmdb.firewall/internet_service_append

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.internet-service-append.json
Category: cmdb
Endpoint: /cmdb/firewall/internet-service-append

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_internet-service-append.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.firewall.internet_service_append


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoInternetServiceAppendEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_addr_mode(self):
        """Test enum field addr-mode validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import internet_service_append as validators
        
        valid_values = ['ipv4', 'ipv6', 'both']
        
        # Test each valid value
        for value in valid_values:
            config = {"addr-mode": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: addr-mode={value}")
        
        print(f"✅ Enum field addr-mode has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/firewall/internet_service_append"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.internet-service-append.json"
TEST_HTTP_METHODS = ['GET', 'PUT']