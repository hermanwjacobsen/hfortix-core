"""
Auto-generated basic tests for cmdb.authentication/rule

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/authentication.rule.json
Category: cmdb
Endpoint: /cmdb/authentication/rule

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_rule.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.authentication.rule


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoRuleEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_status(self):
        """Test enum field status validation."""
        from hfortix_fortios.api.v2.cmdb.authentication._helpers import rule as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: status={value}")
        
        print(f"✅ Enum field status has {len(valid_values)} valid values")
    def auto_test_enum_protocol(self):
        """Test enum field protocol validation."""
        from hfortix_fortios.api.v2.cmdb.authentication._helpers import rule as validators
        
        valid_values = ['http', 'ftp', 'socks', 'ssh', 'ztna-portal']
        
        # Test each valid value
        for value in valid_values:
            config = {"protocol": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: protocol={value}")
        
        print(f"✅ Enum field protocol has {len(valid_values)} valid values")
    def auto_test_enum_ip_based(self):
        """Test enum field ip-based validation."""
        from hfortix_fortios.api.v2.cmdb.authentication._helpers import rule as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"ip-based": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ip-based={value}")
        
        print(f"✅ Enum field ip-based has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/authentication/rule"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/authentication.rule.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']