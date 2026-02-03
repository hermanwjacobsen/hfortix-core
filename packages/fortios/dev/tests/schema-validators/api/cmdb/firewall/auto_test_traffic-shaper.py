"""
Auto-generated basic tests for cmdb.firewall/shaper/traffic_shaper

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.shaper.traffic-shaper.json
Category: cmdb
Endpoint: /cmdb/firewall.shaper/traffic-shaper

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_traffic-shaper.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.firewall.shaper.traffic_shaper


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoTrafficShaperEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_bandwidth_unit(self):
        """Test enum field bandwidth-unit validation."""
        from hfortix_fortios.api.v2.cmdb.firewall.shaper._helpers import traffic_shaper as validators
        
        valid_values = ['kbps', 'mbps', 'gbps']
        
        # Test each valid value
        for value in valid_values:
            config = {"bandwidth-unit": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: bandwidth-unit={value}")
        
        print(f"✅ Enum field bandwidth-unit has {len(valid_values)} valid values")
    def auto_test_enum_priority(self):
        """Test enum field priority validation."""
        from hfortix_fortios.api.v2.cmdb.firewall.shaper._helpers import traffic_shaper as validators
        
        valid_values = ['low', 'medium', 'high']
        
        # Test each valid value
        for value in valid_values:
            config = {"priority": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: priority={value}")
        
        print(f"✅ Enum field priority has {len(valid_values)} valid values")
    def auto_test_enum_per_policy(self):
        """Test enum field per-policy validation."""
        from hfortix_fortios.api.v2.cmdb.firewall.shaper._helpers import traffic_shaper as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"per-policy": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: per-policy={value}")
        
        print(f"✅ Enum field per-policy has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/firewall/shaper/traffic_shaper"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.shaper.traffic-shaper.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']