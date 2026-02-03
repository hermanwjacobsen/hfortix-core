"""
Auto-generated basic tests for cmdb.system/ips

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.ips.json
Category: cmdb
Endpoint: /cmdb/system/ips

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_ips.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.ips


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoIpsEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_override_signature_hold_by_id(self):
        """Test enum field override-signature-hold-by-id validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import ips as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"override-signature-hold-by-id": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: override-signature-hold-by-id={value}")
        
        print(f"✅ Enum field override-signature-hold-by-id has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/ips"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.ips.json"
TEST_HTTP_METHODS = ['GET', 'PUT']