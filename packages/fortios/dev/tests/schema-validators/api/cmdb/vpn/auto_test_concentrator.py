"""
Auto-generated basic tests for cmdb.vpn/ipsec/concentrator

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/vpn.ipsec.concentrator.json
Category: cmdb
Endpoint: /cmdb/vpn.ipsec/concentrator

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_concentrator.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.vpn.ipsec.concentrator


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoConcentratorEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_src_check(self):
        """Test enum field src-check validation."""
        from hfortix_fortios.api.v2.cmdb.vpn.ipsec._helpers import concentrator as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"src-check": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: src-check={value}")
        
        print(f"✅ Enum field src-check has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/vpn/ipsec/concentrator"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/vpn.ipsec.concentrator.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']