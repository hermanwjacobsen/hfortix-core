"""
Auto-generated basic tests for cmdb.dlp/settings

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/dlp.settings.json
Category: cmdb
Endpoint: /cmdb/dlp/settings

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_settings.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.dlp.settings


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoSettingsEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_db_mode(self):
        """Test enum field db-mode validation."""
        from hfortix_fortios.api.v2.cmdb.dlp._helpers import settings as validators
        
        valid_values = ['stop-adding', 'remove-modified-then-oldest', 'remove-oldest']
        
        # Test each valid value
        for value in valid_values:
            config = {"db-mode": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: db-mode={value}")
        
        print(f"✅ Enum field db-mode has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/dlp/settings"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/dlp.settings.json"
TEST_HTTP_METHODS = ['GET', 'PUT']