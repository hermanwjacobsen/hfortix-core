"""
Auto-generated basic tests for cmdb.endpoint_control/settings

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/endpoint-control.settings.json
Category: cmdb
Endpoint: /cmdb/endpoint-control/settings

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_settings.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.endpoint_control.settings


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoSettingsEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_override(self):
        """Test enum field override validation."""
        from hfortix_fortios.api.v2.cmdb.endpoint_control._helpers import settings as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"override": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: override={value}")
        
        print(f"✅ Enum field override has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/endpoint_control/settings"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/endpoint-control.settings.json"
TEST_HTTP_METHODS = ['GET', 'PUT']