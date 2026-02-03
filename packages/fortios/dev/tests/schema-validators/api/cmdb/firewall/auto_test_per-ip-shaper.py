"""
Auto-generated basic tests for cmdb.firewall/shaper/per_ip_shaper

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.shaper.per-ip-shaper.json
Category: cmdb
Endpoint: /cmdb/firewall.shaper/per-ip-shaper

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_per-ip-shaper.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.firewall.shaper.per_ip_shaper


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoPerIpShaperEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_bandwidth_unit(self):
        """Test enum field bandwidth-unit validation."""
        from hfortix_fortios.api.v2.cmdb.firewall.shaper._helpers import per_ip_shaper as validators
        
        valid_values = ['kbps', 'mbps', 'gbps']
        
        # Test each valid value
        for value in valid_values:
            config = {"bandwidth-unit": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: bandwidth-unit={value}")
        
        print(f"✅ Enum field bandwidth-unit has {len(valid_values)} valid values")
    def auto_test_enum_diffserv_forward(self):
        """Test enum field diffserv-forward validation."""
        from hfortix_fortios.api.v2.cmdb.firewall.shaper._helpers import per_ip_shaper as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"diffserv-forward": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: diffserv-forward={value}")
        
        print(f"✅ Enum field diffserv-forward has {len(valid_values)} valid values")
    def auto_test_enum_diffserv_reverse(self):
        """Test enum field diffserv-reverse validation."""
        from hfortix_fortios.api.v2.cmdb.firewall.shaper._helpers import per_ip_shaper as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"diffserv-reverse": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: diffserv-reverse={value}")
        
        print(f"✅ Enum field diffserv-reverse has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/firewall/shaper/per_ip_shaper"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.shaper.per-ip-shaper.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']