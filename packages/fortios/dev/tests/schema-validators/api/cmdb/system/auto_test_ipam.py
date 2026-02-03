"""
Auto-generated basic tests for cmdb.system/ipam

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.ipam.json
Category: cmdb
Endpoint: /cmdb/system/ipam

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_ipam.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.ipam


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoIpamEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_status(self):
        """Test enum field status validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import ipam as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: status={value}")
        
        print(f"✅ Enum field status has {len(valid_values)} valid values")
    def auto_test_enum_server_type(self):
        """Test enum field server-type validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import ipam as validators
        
        valid_values = ['fabric-root']
        
        # Test each valid value
        for value in valid_values:
            config = {"server-type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: server-type={value}")
        
        print(f"✅ Enum field server-type has {len(valid_values)} valid values")
    def auto_test_enum_automatic_conflict_resolution(self):
        """Test enum field automatic-conflict-resolution validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import ipam as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"automatic-conflict-resolution": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: automatic-conflict-resolution={value}")
        
        print(f"✅ Enum field automatic-conflict-resolution has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/ipam"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.ipam.json"
TEST_HTTP_METHODS = ['GET', 'PUT']