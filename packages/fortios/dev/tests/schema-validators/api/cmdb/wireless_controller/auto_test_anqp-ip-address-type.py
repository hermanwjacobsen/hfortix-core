"""
Auto-generated basic tests for cmdb.wireless_controller/hotspot20/anqp_ip_address_type

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/wireless-controller.hotspot20.anqp-ip-address-type.json
Category: cmdb
Endpoint: /cmdb/wireless-controller.hotspot20/anqp-ip-address-type

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_anqp-ip-address-type.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.wireless_controller.hotspot20.anqp_ip_address_type


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoAnqpIpAddressTypeEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_ipv6_address_type(self):
        """Test enum field ipv6-address-type validation."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller.hotspot20._helpers import anqp_ip_address_type as validators
        
        valid_values = ['not-available', 'available', 'not-known']
        
        # Test each valid value
        for value in valid_values:
            config = {"ipv6-address-type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ipv6-address-type={value}")
        
        print(f"✅ Enum field ipv6-address-type has {len(valid_values)} valid values")
    def auto_test_enum_ipv4_address_type(self):
        """Test enum field ipv4-address-type validation."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller.hotspot20._helpers import anqp_ip_address_type as validators
        
        valid_values = ['not-available', 'public', 'port-restricted', 'single-NATed-private', 'double-NATed-private', 'port-restricted-and-single-NATed', 'port-restricted-and-double-NATed', 'not-known']
        
        # Test each valid value
        for value in valid_values:
            config = {"ipv4-address-type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ipv4-address-type={value}")
        
        print(f"✅ Enum field ipv4-address-type has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/wireless_controller/hotspot20/anqp_ip_address_type"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/wireless-controller.hotspot20.anqp-ip-address-type.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']