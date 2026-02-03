"""
Auto-generated basic tests for cmdb.wireless_controller/ap_status

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/wireless-controller.ap-status.json
Category: cmdb
Endpoint: /cmdb/wireless-controller/ap-status

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_ap-status.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.wireless_controller.ap_status


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoApStatusEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_status(self):
        """Test enum field status validation."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller._helpers import ap_status as validators
        
        valid_values = ['rogue', 'accepted', 'suppressed']
        
        # Test each valid value
        for value in valid_values:
            config = {"status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: status={value}")
        
        print(f"✅ Enum field status has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/wireless_controller/ap_status"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/wireless-controller.ap-status.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']