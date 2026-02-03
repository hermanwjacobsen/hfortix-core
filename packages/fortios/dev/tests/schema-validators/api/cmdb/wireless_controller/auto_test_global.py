"""
Auto-generated basic tests for cmdb.wireless_controller/global_

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/wireless-controller.global.json
Category: cmdb
Endpoint: /cmdb/wireless-controller/global

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_global.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.wireless_controller.global_


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoGlobalEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_image_download(self):
        """Test enum field image-download validation."""
        # 'global' is a Python keyword, using importlib
        import importlib
        validators = importlib.import_module('hfortix_fortios.api.v2.cmdb.wireless_controller._helpers.global_')
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"image-download": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: image-download={value}")
        
        print(f"✅ Enum field image-download has {len(valid_values)} valid values")
    def auto_test_enum_rolling_wtp_upgrade(self):
        """Test enum field rolling-wtp-upgrade validation."""
        # 'global' is a Python keyword, using importlib
        import importlib
        validators = importlib.import_module('hfortix_fortios.api.v2.cmdb.wireless_controller._helpers.global_')
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"rolling-wtp-upgrade": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: rolling-wtp-upgrade={value}")
        
        print(f"✅ Enum field rolling-wtp-upgrade has {len(valid_values)} valid values")
    def auto_test_enum_control_message_offload(self):
        """Test enum field control-message-offload validation."""
        # 'global' is a Python keyword, using importlib
        import importlib
        validators = importlib.import_module('hfortix_fortios.api.v2.cmdb.wireless_controller._helpers.global_')
        
        valid_values = ['ebp-frame', 'aeroscout-tag', 'ap-list', 'sta-list', 'sta-cap-list', 'stats', 'aeroscout-mu', 'sta-health', 'spectral-analysis']
        
        # Test each valid value
        for value in valid_values:
            config = {"control-message-offload": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: control-message-offload={value}")
        
        print(f"✅ Enum field control-message-offload has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/wireless_controller/global_"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/wireless-controller.global.json"
TEST_HTTP_METHODS = ['GET', 'PUT']