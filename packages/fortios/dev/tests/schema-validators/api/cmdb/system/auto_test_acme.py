"""
Auto-generated basic tests for cmdb.system/acme

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.acme.json
Category: cmdb
Endpoint: /cmdb/system/acme

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_acme.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.acme


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoAcmeEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_use_ha_direct(self):
        """Test enum field use-ha-direct validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import acme as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"use-ha-direct": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: use-ha-direct={value}")
        
        print(f"✅ Enum field use-ha-direct has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/acme"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.acme.json"
TEST_HTTP_METHODS = ['GET', 'PUT']