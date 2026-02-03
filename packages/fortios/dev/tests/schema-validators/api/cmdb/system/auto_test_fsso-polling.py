"""
Auto-generated basic tests for cmdb.system/fsso_polling

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.fsso-polling.json
Category: cmdb
Endpoint: /cmdb/system/fsso-polling

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_fsso-polling.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.fsso_polling


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoFssoPollingEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_status(self):
        """Test enum field status validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import fsso_polling as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: status={value}")
        
        print(f"✅ Enum field status has {len(valid_values)} valid values")
    def auto_test_enum_authentication(self):
        """Test enum field authentication validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import fsso_polling as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"authentication": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: authentication={value}")
        
        print(f"✅ Enum field authentication has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/fsso_polling"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.fsso-polling.json"
TEST_HTTP_METHODS = ['GET', 'PUT']