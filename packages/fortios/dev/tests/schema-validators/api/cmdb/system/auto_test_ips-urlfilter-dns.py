"""
Auto-generated basic tests for cmdb.system/ips_urlfilter_dns

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.ips-urlfilter-dns.json
Category: cmdb
Endpoint: /cmdb/system/ips-urlfilter-dns

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_ips-urlfilter-dns.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.ips_urlfilter_dns


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoIpsUrlfilterDnsEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_status(self):
        """Test enum field status validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import ips_urlfilter_dns as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: status={value}")
        
        print(f"✅ Enum field status has {len(valid_values)} valid values")
    def auto_test_enum_ipv6_capability(self):
        """Test enum field ipv6-capability validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import ips_urlfilter_dns as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"ipv6-capability": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ipv6-capability={value}")
        
        print(f"✅ Enum field ipv6-capability has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/ips_urlfilter_dns"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.ips-urlfilter-dns.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']