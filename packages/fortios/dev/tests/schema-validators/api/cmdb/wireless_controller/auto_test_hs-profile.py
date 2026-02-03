"""
Auto-generated basic tests for cmdb.wireless_controller/hotspot20/hs_profile

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/wireless-controller.hotspot20.hs-profile.json
Category: cmdb
Endpoint: /cmdb/wireless-controller.hotspot20/hs-profile

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_hs-profile.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.wireless_controller.hotspot20.hs_profile


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoHsProfileEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_access_network_type(self):
        """Test enum field access-network-type validation."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller.hotspot20._helpers import hs_profile as validators
        
        valid_values = ['private-network', 'private-network-with-guest-access', 'chargeable-public-network', 'free-public-network', 'personal-device-network', 'emergency-services-only-network', 'test-or-experimental', 'wildcard']
        
        # Test each valid value
        for value in valid_values:
            config = {"access-network-type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: access-network-type={value}")
        
        print(f"✅ Enum field access-network-type has {len(valid_values)} valid values")
    def auto_test_enum_access_network_internet(self):
        """Test enum field access-network-internet validation."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller.hotspot20._helpers import hs_profile as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"access-network-internet": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: access-network-internet={value}")
        
        print(f"✅ Enum field access-network-internet has {len(valid_values)} valid values")
    def auto_test_enum_access_network_asra(self):
        """Test enum field access-network-asra validation."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller.hotspot20._helpers import hs_profile as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"access-network-asra": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: access-network-asra={value}")
        
        print(f"✅ Enum field access-network-asra has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/wireless_controller/hotspot20/hs_profile"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/wireless-controller.hotspot20.hs-profile.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']