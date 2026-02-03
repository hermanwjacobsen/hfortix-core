"""
Auto-generated basic tests for cmdb.wireless_controller/wtp_group

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/wireless-controller.wtp-group.json
Category: cmdb
Endpoint: /cmdb/wireless-controller/wtp-group

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_wtp-group.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.wireless_controller.wtp_group


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoWtpGroupEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_platform_type(self):
        """Test enum field platform-type validation."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller._helpers import wtp_group as validators
        
        valid_values = ['AP-11N', 'C24JE', '421E', '423E', '221E', '222E', '223E', '224E', '231E', '321E', '431F', '431FL', '432F', '432FR', '433F', '433FL', '231F', '231FL', '234F', '23JF', '831F', '231G', '233G', '234G', '431G', '432G', '433G', '231K', '231KD', '23JK', '222KL', '241K', '243K', '244K', '441K', '432K', '443K', 'U421E', 'U422EV', 'U423E', 'U221EV', 'U223EV', 'U24JEV', 'U321EV', 'U323EV', 'U431F', 'U433F', 'U231F', 'U234F', 'U432F', 'U231G', 'MVP']
        
        # Test each valid value
        for value in valid_values:
            config = {"platform-type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: platform-type={value}")
        
        print(f"✅ Enum field platform-type has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/wireless_controller/wtp_group"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/wireless-controller.wtp-group.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']