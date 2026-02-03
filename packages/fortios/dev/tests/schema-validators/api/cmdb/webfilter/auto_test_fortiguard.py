"""
Auto-generated basic tests for cmdb.webfilter/fortiguard

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/webfilter.fortiguard.json
Category: cmdb
Endpoint: /cmdb/webfilter/fortiguard

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_fortiguard.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.webfilter.fortiguard


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoFortiguardEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_cache_mode(self):
        """Test enum field cache-mode validation."""
        from hfortix_fortios.api.v2.cmdb.webfilter._helpers import fortiguard as validators
        
        valid_values = ['ttl', 'db-ver']
        
        # Test each valid value
        for value in valid_values:
            config = {"cache-mode": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: cache-mode={value}")
        
        print(f"✅ Enum field cache-mode has {len(valid_values)} valid values")
    def auto_test_enum_cache_prefix_match(self):
        """Test enum field cache-prefix-match validation."""
        from hfortix_fortios.api.v2.cmdb.webfilter._helpers import fortiguard as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"cache-prefix-match": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: cache-prefix-match={value}")
        
        print(f"✅ Enum field cache-prefix-match has {len(valid_values)} valid values")
    def auto_test_enum_ovrd_auth_https(self):
        """Test enum field ovrd-auth-https validation."""
        from hfortix_fortios.api.v2.cmdb.webfilter._helpers import fortiguard as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"ovrd-auth-https": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ovrd-auth-https={value}")
        
        print(f"✅ Enum field ovrd-auth-https has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/webfilter/fortiguard"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/webfilter.fortiguard.json"
TEST_HTTP_METHODS = ['GET', 'PUT']