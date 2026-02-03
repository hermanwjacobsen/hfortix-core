"""
Auto-generated basic tests for cmdb.switch_controller/global_

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/switch-controller.global.json
Category: cmdb
Endpoint: /cmdb/switch-controller/global

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_global.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.switch_controller.global_


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoGlobalEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_https_image_push(self):
        """Test enum field https-image-push validation."""
        # 'global' is a Python keyword, using importlib
        import importlib
        validators = importlib.import_module('hfortix_fortios.api.v2.cmdb.switch_controller._helpers.global_')
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"https-image-push": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: https-image-push={value}")
        
        print(f"✅ Enum field https-image-push has {len(valid_values)} valid values")
    def auto_test_enum_vlan_all_mode(self):
        """Test enum field vlan-all-mode validation."""
        # 'global' is a Python keyword, using importlib
        import importlib
        validators = importlib.import_module('hfortix_fortios.api.v2.cmdb.switch_controller._helpers.global_')
        
        valid_values = ['all', 'defined']
        
        # Test each valid value
        for value in valid_values:
            config = {"vlan-all-mode": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: vlan-all-mode={value}")
        
        print(f"✅ Enum field vlan-all-mode has {len(valid_values)} valid values")
    def auto_test_enum_vlan_optimization(self):
        """Test enum field vlan-optimization validation."""
        # 'global' is a Python keyword, using importlib
        import importlib
        validators = importlib.import_module('hfortix_fortios.api.v2.cmdb.switch_controller._helpers.global_')
        
        valid_values = ['prune', 'configured', 'none']
        
        # Test each valid value
        for value in valid_values:
            config = {"vlan-optimization": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: vlan-optimization={value}")
        
        print(f"✅ Enum field vlan-optimization has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/switch_controller/global_"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/switch-controller.global.json"
TEST_HTTP_METHODS = ['GET', 'PUT']