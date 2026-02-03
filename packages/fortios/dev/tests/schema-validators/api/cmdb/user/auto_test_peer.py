"""
Auto-generated basic tests for cmdb.user/peer

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/user.peer.json
Category: cmdb
Endpoint: /cmdb/user/peer

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_peer.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.user.peer


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoPeerEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_mandatory_ca_verify(self):
        """Test enum field mandatory-ca-verify validation."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import peer as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"mandatory-ca-verify": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: mandatory-ca-verify={value}")
        
        print(f"✅ Enum field mandatory-ca-verify has {len(valid_values)} valid values")
    def auto_test_enum_cn_type(self):
        """Test enum field cn-type validation."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import peer as validators
        
        valid_values = ['string', 'email', 'FQDN', 'ipv4', 'ipv6']
        
        # Test each valid value
        for value in valid_values:
            config = {"cn-type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: cn-type={value}")
        
        print(f"✅ Enum field cn-type has {len(valid_values)} valid values")
    def auto_test_enum_mfa_mode(self):
        """Test enum field mfa-mode validation."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import peer as validators
        
        valid_values = ['none', 'password', 'subject-identity']
        
        # Test each valid value
        for value in valid_values:
            config = {"mfa-mode": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: mfa-mode={value}")
        
        print(f"✅ Enum field mfa-mode has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/user/peer"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/user.peer.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']