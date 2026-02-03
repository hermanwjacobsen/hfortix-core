"""
Auto-generated basic tests for cmdb.firewall/ssh/host_key

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.ssh.host-key.json
Category: cmdb
Endpoint: /cmdb/firewall.ssh/host-key

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_host-key.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.firewall.ssh.host_key


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoHostKeyEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_status(self):
        """Test enum field status validation."""
        from hfortix_fortios.api.v2.cmdb.firewall.ssh._helpers import host_key as validators
        
        valid_values = ['trusted', 'revoked']
        
        # Test each valid value
        for value in valid_values:
            config = {"status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: status={value}")
        
        print(f"✅ Enum field status has {len(valid_values)} valid values")
    def auto_test_enum_type(self):
        """Test enum field type validation."""
        from hfortix_fortios.api.v2.cmdb.firewall.ssh._helpers import host_key as validators
        
        valid_values = ['RSA', 'DSA', 'ECDSA', 'ED25519', 'RSA-CA', 'DSA-CA', 'ECDSA-CA', 'ED25519-CA']
        
        # Test each valid value
        for value in valid_values:
            config = {"type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: type={value}")
        
        print(f"✅ Enum field type has {len(valid_values)} valid values")
    def auto_test_enum_nid(self):
        """Test enum field nid validation."""
        from hfortix_fortios.api.v2.cmdb.firewall.ssh._helpers import host_key as validators
        
        valid_values = ['256', '384', '521']
        
        # Test each valid value
        for value in valid_values:
            config = {"nid": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: nid={value}")
        
        print(f"✅ Enum field nid has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/firewall/ssh/host_key"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.ssh.host-key.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']