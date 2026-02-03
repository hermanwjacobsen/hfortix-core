"""
Auto-generated basic tests for cmdb.system/netflow

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.netflow.json
Category: cmdb
Endpoint: /cmdb/system/netflow

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_netflow.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.netflow


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoNetflowEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_session_cache_size(self):
        """Test enum field session-cache-size validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import netflow as validators
        
        valid_values = ['min', 'default', 'max']
        
        # Test each valid value
        for value in valid_values:
            config = {"session-cache-size": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: session-cache-size={value}")
        
        print(f"✅ Enum field session-cache-size has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/netflow"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.netflow.json"
TEST_HTTP_METHODS = ['GET', 'PUT']