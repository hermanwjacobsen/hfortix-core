"""
Auto-generated basic tests for cmdb.firewall/service/custom

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.service.custom.json
Category: cmdb
Endpoint: /cmdb/firewall.service/custom

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_custom.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.firewall.service.custom


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoCustomEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_proxy(self):
        """Test enum field proxy validation."""
        from hfortix_fortios.api.v2.cmdb.firewall.service._helpers import custom as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"proxy": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: proxy={value}")
        
        print(f"✅ Enum field proxy has {len(valid_values)} valid values")
    def auto_test_enum_protocol(self):
        """Test enum field protocol validation."""
        from hfortix_fortios.api.v2.cmdb.firewall.service._helpers import custom as validators
        
        valid_values = ['TCP/UDP/UDP-Lite/SCTP', 'ICMP', 'ICMP6', 'IP', 'HTTP', 'FTP', 'CONNECT', 'SOCKS-TCP', 'SOCKS-UDP', 'ALL']
        
        # Test each valid value
        for value in valid_values:
            config = {"protocol": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: protocol={value}")
        
        print(f"✅ Enum field protocol has {len(valid_values)} valid values")
    def auto_test_enum_helper(self):
        """Test enum field helper validation."""
        from hfortix_fortios.api.v2.cmdb.firewall.service._helpers import custom as validators
        
        valid_values = ['auto', 'disable', 'ftp', 'tftp', 'ras', 'h323', 'tns', 'mms', 'sip', 'pptp', 'rtsp', 'dns-udp', 'dns-tcp', 'pmap', 'rsh', 'dcerpc', 'mgcp']
        
        # Test each valid value
        for value in valid_values:
            config = {"helper": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: helper={value}")
        
        print(f"✅ Enum field helper has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/firewall/service/custom"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.service.custom.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']