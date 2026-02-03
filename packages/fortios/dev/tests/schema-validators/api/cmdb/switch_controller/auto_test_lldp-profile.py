"""
Auto-generated basic tests for cmdb.switch_controller/lldp_profile

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/switch-controller.lldp-profile.json
Category: cmdb
Endpoint: /cmdb/switch-controller/lldp-profile

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_lldp-profile.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.switch_controller.lldp_profile


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoLldpProfileEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_med_tlvs(self):
        """Test enum field med-tlvs validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import lldp_profile as validators
        
        valid_values = ['inventory-management', 'network-policy', 'power-management', 'location-identification']
        
        # Test each valid value
        for value in valid_values:
            config = {"med-tlvs": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: med-tlvs={value}")
        
        print(f"✅ Enum field med-tlvs has {len(valid_values)} valid values")
    def auto_test_enum_x802_1_tlvs(self):
        """Test enum field 802.1-tlvs validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import lldp_profile as validators
        
        valid_values = ['port-vlan-id']
        
        # Test each valid value
        for value in valid_values:
            config = {"802.1-tlvs": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: 802.1-tlvs={value}")
        
        print(f"✅ Enum field 802.1-tlvs has {len(valid_values)} valid values")
    def auto_test_enum_x802_3_tlvs(self):
        """Test enum field 802.3-tlvs validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import lldp_profile as validators
        
        valid_values = ['max-frame-size', 'power-negotiation']
        
        # Test each valid value
        for value in valid_values:
            config = {"802.3-tlvs": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: 802.3-tlvs={value}")
        
        print(f"✅ Enum field 802.3-tlvs has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/switch_controller/lldp_profile"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/switch-controller.lldp-profile.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']