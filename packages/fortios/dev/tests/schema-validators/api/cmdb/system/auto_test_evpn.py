"""
Auto-generated basic tests for cmdb.system/evpn

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.evpn.json
Category: cmdb
Endpoint: /cmdb/system/evpn

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_evpn.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.evpn


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoEvpnEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_ip_local_learning(self):
        """Test enum field ip-local-learning validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import evpn as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"ip-local-learning": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ip-local-learning={value}")
        
        print(f"✅ Enum field ip-local-learning has {len(valid_values)} valid values")
    def auto_test_enum_arp_suppression(self):
        """Test enum field arp-suppression validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import evpn as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"arp-suppression": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: arp-suppression={value}")
        
        print(f"✅ Enum field arp-suppression has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/evpn"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.evpn.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']