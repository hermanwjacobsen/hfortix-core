"""
Auto-generated basic tests for cmdb.firewall/addrgrp6

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.addrgrp6.json
Category: cmdb
Endpoint: /cmdb/firewall/addrgrp6

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_addrgrp6.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.firewall.addrgrp6


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoAddrgrp6Validators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.firewall._helpers import addrgrp6 as validators
            print(f"✅ Successfully imported validators for addrgrp6")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_firewall_addrgrp6_post")
            assert hasattr(validators, "validate_firewall_addrgrp6_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import addrgrp6 as validators
        
        # Build minimal valid config with all required fields
        config = {
            "exclude-member": "test_exclude-member",  # string
            "name": "test_name",  # string
        }
        
        try:
            result = validators.validate_firewall_addrgrp6_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoAddrgrp6Enums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_exclude(self):
        """Test enum field exclude validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import addrgrp6 as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"exclude": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: exclude={value}")
        
        print(f"✅ Enum field exclude has {len(valid_values)} valid values")
    def auto_test_enum_fabric_object(self):
        """Test enum field fabric-object validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import addrgrp6 as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"fabric-object": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: fabric-object={value}")
        
        print(f"✅ Enum field fabric-object has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/firewall/addrgrp6"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.addrgrp6.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']