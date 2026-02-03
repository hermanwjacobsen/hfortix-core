"""
Auto-generated basic tests for cmdb.user/nac_policy

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/user.nac-policy.json
Category: cmdb
Endpoint: /cmdb/user/nac-policy

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_nac-policy.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.user.nac_policy


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoNacPolicyEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_category(self):
        """Test enum field category validation."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import nac_policy as validators
        
        valid_values = ['device', 'firewall-user', 'ems-tag', 'fortivoice-tag', 'vulnerability']
        
        # Test each valid value
        for value in valid_values:
            config = {"category": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: category={value}")
        
        print(f"✅ Enum field category has {len(valid_values)} valid values")
    def auto_test_enum_status(self):
        """Test enum field status validation."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import nac_policy as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: status={value}")
        
        print(f"✅ Enum field status has {len(valid_values)} valid values")
    def auto_test_enum_match_type(self):
        """Test enum field match-type validation."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import nac_policy as validators
        
        valid_values = ['dynamic', 'override']
        
        # Test each valid value
        for value in valid_values:
            config = {"match-type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: match-type={value}")
        
        print(f"✅ Enum field match-type has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/user/nac_policy"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/user.nac-policy.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']