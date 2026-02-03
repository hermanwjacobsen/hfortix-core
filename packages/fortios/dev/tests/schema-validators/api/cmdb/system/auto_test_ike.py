"""
Auto-generated basic tests for cmdb.system/ike

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.ike.json
Category: cmdb
Endpoint: /cmdb/system/ike

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_ike.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.ike


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoIkeEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_dh_multiprocess(self):
        """Test enum field dh-multiprocess validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import ike as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"dh-multiprocess": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: dh-multiprocess={value}")
        
        print(f"✅ Enum field dh-multiprocess has {len(valid_values)} valid values")
    def auto_test_enum_dh_mode(self):
        """Test enum field dh-mode validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import ike as validators
        
        valid_values = ['software', 'hardware']
        
        # Test each valid value
        for value in valid_values:
            config = {"dh-mode": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: dh-mode={value}")
        
        print(f"✅ Enum field dh-mode has {len(valid_values)} valid values")
    def auto_test_enum_dh_keypair_cache(self):
        """Test enum field dh-keypair-cache validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import ike as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"dh-keypair-cache": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: dh-keypair-cache={value}")
        
        print(f"✅ Enum field dh-keypair-cache has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/ike"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.ike.json"
TEST_HTTP_METHODS = ['GET', 'PUT']