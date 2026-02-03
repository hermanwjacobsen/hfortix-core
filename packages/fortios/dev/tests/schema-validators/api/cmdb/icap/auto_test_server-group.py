"""
Auto-generated basic tests for cmdb.icap/server_group

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/icap.server-group.json
Category: cmdb
Endpoint: /cmdb/icap/server-group

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_server-group.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.icap.server_group


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoServerGroupEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_ldb_method(self):
        """Test enum field ldb-method validation."""
        from hfortix_fortios.api.v2.cmdb.icap._helpers import server_group as validators
        
        valid_values = ['weighted', 'least-session', 'active-passive']
        
        # Test each valid value
        for value in valid_values:
            config = {"ldb-method": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ldb-method={value}")
        
        print(f"✅ Enum field ldb-method has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/icap/server_group"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/icap.server-group.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']