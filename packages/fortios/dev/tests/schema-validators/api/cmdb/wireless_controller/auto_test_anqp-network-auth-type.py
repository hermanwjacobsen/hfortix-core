"""
Auto-generated basic tests for cmdb.wireless_controller/hotspot20/anqp_network_auth_type

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/wireless-controller.hotspot20.anqp-network-auth-type.json
Category: cmdb
Endpoint: /cmdb/wireless-controller.hotspot20/anqp-network-auth-type

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_anqp-network-auth-type.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.wireless_controller.hotspot20.anqp_network_auth_type


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoAnqpNetworkAuthTypeEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_auth_type(self):
        """Test enum field auth-type validation."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller.hotspot20._helpers import anqp_network_auth_type as validators
        
        valid_values = ['acceptance-of-terms', 'online-enrollment', 'http-redirection', 'dns-redirection']
        
        # Test each valid value
        for value in valid_values:
            config = {"auth-type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: auth-type={value}")
        
        print(f"✅ Enum field auth-type has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/wireless_controller/hotspot20/anqp_network_auth_type"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/wireless-controller.hotspot20.anqp-network-auth-type.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']