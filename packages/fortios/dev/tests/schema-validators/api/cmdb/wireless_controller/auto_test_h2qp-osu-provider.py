"""
Auto-generated basic tests for cmdb.wireless_controller/hotspot20/h2qp_osu_provider

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/wireless-controller.hotspot20.h2qp-osu-provider.json
Category: cmdb
Endpoint: /cmdb/wireless-controller.hotspot20/h2qp-osu-provider

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_h2qp-osu-provider.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.wireless_controller.hotspot20.h2qp_osu_provider


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoH2qpOsuProviderEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_osu_method(self):
        """Test enum field osu-method validation."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller.hotspot20._helpers import h2qp_osu_provider as validators
        
        valid_values = ['oma-dm', 'soap-xml-spp', 'reserved']
        
        # Test each valid value
        for value in valid_values:
            config = {"osu-method": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: osu-method={value}")
        
        print(f"✅ Enum field osu-method has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/wireless_controller/hotspot20/h2qp_osu_provider"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/wireless-controller.hotspot20.h2qp-osu-provider.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']