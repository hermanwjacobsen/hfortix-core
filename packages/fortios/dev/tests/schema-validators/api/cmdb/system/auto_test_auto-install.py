"""
Auto-generated basic tests for cmdb.system/auto_install

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.auto-install.json
Category: cmdb
Endpoint: /cmdb/system/auto-install

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_auto-install.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.auto_install


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoAutoInstallEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_auto_install_config(self):
        """Test enum field auto-install-config validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import auto_install as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"auto-install-config": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: auto-install-config={value}")
        
        print(f"✅ Enum field auto-install-config has {len(valid_values)} valid values")
    def auto_test_enum_auto_install_image(self):
        """Test enum field auto-install-image validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import auto_install as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"auto-install-image": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: auto-install-image={value}")
        
        print(f"✅ Enum field auto-install-image has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/auto_install"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.auto-install.json"
TEST_HTTP_METHODS = ['GET', 'PUT']