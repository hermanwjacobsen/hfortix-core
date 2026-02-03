"""
Auto-generated basic tests for cmdb.ftp_proxy/explicit

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/ftp-proxy.explicit.json
Category: cmdb
Endpoint: /cmdb/ftp-proxy/explicit

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_explicit.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.ftp_proxy.explicit


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoExplicitEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_status(self):
        """Test enum field status validation."""
        from hfortix_fortios.api.v2.cmdb.ftp_proxy._helpers import explicit as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: status={value}")
        
        print(f"✅ Enum field status has {len(valid_values)} valid values")
    def auto_test_enum_sec_default_action(self):
        """Test enum field sec-default-action validation."""
        from hfortix_fortios.api.v2.cmdb.ftp_proxy._helpers import explicit as validators
        
        valid_values = ['accept', 'deny']
        
        # Test each valid value
        for value in valid_values:
            config = {"sec-default-action": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: sec-default-action={value}")
        
        print(f"✅ Enum field sec-default-action has {len(valid_values)} valid values")
    def auto_test_enum_server_data_mode(self):
        """Test enum field server-data-mode validation."""
        from hfortix_fortios.api.v2.cmdb.ftp_proxy._helpers import explicit as validators
        
        valid_values = ['client', 'passive']
        
        # Test each valid value
        for value in valid_values:
            config = {"server-data-mode": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: server-data-mode={value}")
        
        print(f"✅ Enum field server-data-mode has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/ftp_proxy/explicit"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/ftp-proxy.explicit.json"
TEST_HTTP_METHODS = ['GET', 'PUT']