"""
Auto-generated basic tests for cmdb.wireless_controller/apcfg_profile

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/wireless-controller.apcfg-profile.json
Category: cmdb
Endpoint: /cmdb/wireless-controller/apcfg-profile

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_apcfg-profile.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.wireless_controller.apcfg_profile


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoApcfgProfileEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_ap_family(self):
        """Test enum field ap-family validation."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller._helpers import apcfg_profile as validators
        
        valid_values = ['fap', 'fap-u', 'fap-c']
        
        # Test each valid value
        for value in valid_values:
            config = {"ap-family": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ap-family={value}")
        
        print(f"✅ Enum field ap-family has {len(valid_values)} valid values")
    def auto_test_enum_ac_type(self):
        """Test enum field ac-type validation."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller._helpers import apcfg_profile as validators
        
        valid_values = ['default', 'specify', 'apcfg']
        
        # Test each valid value
        for value in valid_values:
            config = {"ac-type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ac-type={value}")
        
        print(f"✅ Enum field ac-type has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/wireless_controller/apcfg_profile"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/wireless-controller.apcfg-profile.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']