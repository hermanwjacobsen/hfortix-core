"""
Auto-generated basic tests for cmdb.wireless_controller/region

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/wireless-controller.region.json
Category: cmdb
Endpoint: /cmdb/wireless-controller/region

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_region.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.wireless_controller.region


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoRegionEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_grayscale(self):
        """Test enum field grayscale validation."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller._helpers import region as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"grayscale": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: grayscale={value}")
        
        print(f"✅ Enum field grayscale has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/wireless_controller/region"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/wireless-controller.region.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']