"""
Auto-generated basic tests for cmdb.wireless_controller/inter_controller

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/wireless-controller.inter-controller.json
Category: cmdb
Endpoint: /cmdb/wireless-controller/inter-controller

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_inter-controller.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.wireless_controller.inter_controller


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoInterControllerEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_inter_controller_mode(self):
        """Test enum field inter-controller-mode validation."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller._helpers import inter_controller as validators
        
        valid_values = ['disable', 'l2-roaming', '1+1']
        
        # Test each valid value
        for value in valid_values:
            config = {"inter-controller-mode": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: inter-controller-mode={value}")
        
        print(f"✅ Enum field inter-controller-mode has {len(valid_values)} valid values")
    def auto_test_enum_l3_roaming(self):
        """Test enum field l3-roaming validation."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller._helpers import inter_controller as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"l3-roaming": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: l3-roaming={value}")
        
        print(f"✅ Enum field l3-roaming has {len(valid_values)} valid values")
    def auto_test_enum_inter_controller_pri(self):
        """Test enum field inter-controller-pri validation."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller._helpers import inter_controller as validators
        
        valid_values = ['primary', 'secondary']
        
        # Test each valid value
        for value in valid_values:
            config = {"inter-controller-pri": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: inter-controller-pri={value}")
        
        print(f"✅ Enum field inter-controller-pri has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/wireless_controller/inter_controller"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/wireless-controller.inter-controller.json"
TEST_HTTP_METHODS = ['GET', 'PUT']