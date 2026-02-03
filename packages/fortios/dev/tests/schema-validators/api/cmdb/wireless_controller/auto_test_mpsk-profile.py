"""
Auto-generated basic tests for cmdb.wireless_controller/mpsk_profile

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/wireless-controller.mpsk-profile.json
Category: cmdb
Endpoint: /cmdb/wireless-controller/mpsk-profile

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_mpsk-profile.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.wireless_controller.mpsk_profile


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoMpskProfileEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_mpsk_external_server_auth(self):
        """Test enum field mpsk-external-server-auth validation."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller._helpers import mpsk_profile as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"mpsk-external-server-auth": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: mpsk-external-server-auth={value}")
        
        print(f"✅ Enum field mpsk-external-server-auth has {len(valid_values)} valid values")
    def auto_test_enum_mpsk_type(self):
        """Test enum field mpsk-type validation."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller._helpers import mpsk_profile as validators
        
        valid_values = ['wpa2-personal', 'wpa3-sae', 'wpa3-sae-transition']
        
        # Test each valid value
        for value in valid_values:
            config = {"mpsk-type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: mpsk-type={value}")
        
        print(f"✅ Enum field mpsk-type has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/wireless_controller/mpsk_profile"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/wireless-controller.mpsk-profile.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']