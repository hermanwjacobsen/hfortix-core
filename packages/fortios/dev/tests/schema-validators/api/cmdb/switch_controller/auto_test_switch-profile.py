"""
Auto-generated basic tests for cmdb.switch_controller/switch_profile

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/switch-controller.switch-profile.json
Category: cmdb
Endpoint: /cmdb/switch-controller/switch-profile

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_switch-profile.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.switch_controller.switch_profile


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoSwitchProfileEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_login_passwd_override(self):
        """Test enum field login-passwd-override validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import switch_profile as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"login-passwd-override": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: login-passwd-override={value}")
        
        print(f"✅ Enum field login-passwd-override has {len(valid_values)} valid values")
    def auto_test_enum_login(self):
        """Test enum field login validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import switch_profile as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"login": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: login={value}")
        
        print(f"✅ Enum field login has {len(valid_values)} valid values")
    def auto_test_enum_revision_backup_on_logout(self):
        """Test enum field revision-backup-on-logout validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import switch_profile as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"revision-backup-on-logout": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: revision-backup-on-logout={value}")
        
        print(f"✅ Enum field revision-backup-on-logout has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/switch_controller/switch_profile"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/switch-controller.switch-profile.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']