"""
Auto-generated basic tests for cmdb.wireless_controller/hotspot20/h2qp_wan_metric

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/wireless-controller.hotspot20.h2qp-wan-metric.json
Category: cmdb
Endpoint: /cmdb/wireless-controller.hotspot20/h2qp-wan-metric

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_h2qp-wan-metric.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.wireless_controller.hotspot20.h2qp_wan_metric


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoH2qpWanMetricEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_link_status(self):
        """Test enum field link-status validation."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller.hotspot20._helpers import h2qp_wan_metric as validators
        
        valid_values = ['up', 'down', 'in-test']
        
        # Test each valid value
        for value in valid_values:
            config = {"link-status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: link-status={value}")
        
        print(f"✅ Enum field link-status has {len(valid_values)} valid values")
    def auto_test_enum_symmetric_wan_link(self):
        """Test enum field symmetric-wan-link validation."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller.hotspot20._helpers import h2qp_wan_metric as validators
        
        valid_values = ['symmetric', 'asymmetric']
        
        # Test each valid value
        for value in valid_values:
            config = {"symmetric-wan-link": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: symmetric-wan-link={value}")
        
        print(f"✅ Enum field symmetric-wan-link has {len(valid_values)} valid values")
    def auto_test_enum_link_at_capacity(self):
        """Test enum field link-at-capacity validation."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller.hotspot20._helpers import h2qp_wan_metric as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"link-at-capacity": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: link-at-capacity={value}")
        
        print(f"✅ Enum field link-at-capacity has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/wireless_controller/hotspot20/h2qp_wan_metric"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/wireless-controller.hotspot20.h2qp-wan-metric.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']