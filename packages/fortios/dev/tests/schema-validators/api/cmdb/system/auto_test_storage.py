"""
Auto-generated basic tests for cmdb.system/storage

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.storage.json
Category: cmdb
Endpoint: /cmdb/system/storage

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_storage.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.storage


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoStorageEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_status(self):
        """Test enum field status validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import storage as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: status={value}")
        
        print(f"✅ Enum field status has {len(valid_values)} valid values")
    def auto_test_enum_media_status(self):
        """Test enum field media-status validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import storage as validators
        
        valid_values = ['enable', 'disable', 'fail']
        
        # Test each valid value
        for value in valid_values:
            config = {"media-status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: media-status={value}")
        
        print(f"✅ Enum field media-status has {len(valid_values)} valid values")
    def auto_test_enum_usage(self):
        """Test enum field usage validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import storage as validators
        
        valid_values = ['log', 'wanopt']
        
        # Test each valid value
        for value in valid_values:
            config = {"usage": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: usage={value}")
        
        print(f"✅ Enum field usage has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/storage"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.storage.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']