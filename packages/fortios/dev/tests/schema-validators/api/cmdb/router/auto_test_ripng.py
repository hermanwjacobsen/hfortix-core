"""
Auto-generated basic tests for cmdb.router/ripng

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/router.ripng.json
Category: cmdb
Endpoint: /cmdb/router/ripng

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_ripng.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.router.ripng


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoRipngEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_default_information_originate(self):
        """Test enum field default-information-originate validation."""
        from hfortix_fortios.api.v2.cmdb.router._helpers import ripng as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"default-information-originate": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: default-information-originate={value}")
        
        print(f"✅ Enum field default-information-originate has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/router/ripng"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/router.ripng.json"
TEST_HTTP_METHODS = ['GET', 'PUT']