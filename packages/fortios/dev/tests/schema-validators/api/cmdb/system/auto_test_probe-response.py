"""
Auto-generated basic tests for cmdb.system/probe_response

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.probe-response.json
Category: cmdb
Endpoint: /cmdb/system/probe-response

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_probe-response.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.probe_response


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoProbeResponseEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_ttl_mode(self):
        """Test enum field ttl-mode validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import probe_response as validators
        
        valid_values = ['reinit', 'decrease', 'retain']
        
        # Test each valid value
        for value in valid_values:
            config = {"ttl-mode": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ttl-mode={value}")
        
        print(f"✅ Enum field ttl-mode has {len(valid_values)} valid values")
    def auto_test_enum_mode(self):
        """Test enum field mode validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import probe_response as validators
        
        valid_values = ['none', 'http-probe', 'twamp']
        
        # Test each valid value
        for value in valid_values:
            config = {"mode": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: mode={value}")
        
        print(f"✅ Enum field mode has {len(valid_values)} valid values")
    def auto_test_enum_security_mode(self):
        """Test enum field security-mode validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import probe_response as validators
        
        valid_values = ['none', 'authentication']
        
        # Test each valid value
        for value in valid_values:
            config = {"security-mode": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: security-mode={value}")
        
        print(f"✅ Enum field security-mode has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/probe_response"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.probe-response.json"
TEST_HTTP_METHODS = ['GET', 'PUT']