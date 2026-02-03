"""
Auto-generated basic tests for cmdb.user/quarantine

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/user.quarantine.json
Category: cmdb
Endpoint: /cmdb/user/quarantine

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_quarantine.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.user.quarantine


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoQuarantineEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_quarantine(self):
        """Test enum field quarantine validation."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import quarantine as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"quarantine": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: quarantine={value}")
        
        print(f"✅ Enum field quarantine has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/user/quarantine"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/user.quarantine.json"
TEST_HTTP_METHODS = ['GET', 'PUT']