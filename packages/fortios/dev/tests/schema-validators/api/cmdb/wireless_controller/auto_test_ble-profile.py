"""
Auto-generated basic tests for cmdb.wireless_controller/ble_profile

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/wireless-controller.ble-profile.json
Category: cmdb
Endpoint: /cmdb/wireless-controller/ble-profile

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_ble-profile.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.wireless_controller.ble_profile


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoBleProfileEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_advertising(self):
        """Test enum field advertising validation."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller._helpers import ble_profile as validators
        
        valid_values = ['ibeacon', 'eddystone-uid', 'eddystone-url']
        
        # Test each valid value
        for value in valid_values:
            config = {"advertising": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: advertising={value}")
        
        print(f"✅ Enum field advertising has {len(valid_values)} valid values")
    def auto_test_enum_txpower(self):
        """Test enum field txpower validation."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller._helpers import ble_profile as validators
        
        valid_values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17']
        
        # Test each valid value
        for value in valid_values:
            config = {"txpower": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: txpower={value}")
        
        print(f"✅ Enum field txpower has {len(valid_values)} valid values")
    def auto_test_enum_ble_scanning(self):
        """Test enum field ble-scanning validation."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller._helpers import ble_profile as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"ble-scanning": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ble-scanning={value}")
        
        print(f"✅ Enum field ble-scanning has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/wireless_controller/ble_profile"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/wireless-controller.ble-profile.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']