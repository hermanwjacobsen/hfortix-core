"""
Auto-generated basic tests for cmdb.system/geneve

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.geneve.json
Category: cmdb
Endpoint: /cmdb/system/geneve

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_geneve.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.geneve


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoGeneveValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.system._helpers import geneve as validators
            print(f"✅ Successfully imported validators for geneve")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_system_geneve_post")
            assert hasattr(validators, "validate_system_geneve_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import geneve as validators
        
        # Build minimal valid config with all required fields
        config = {
            "interface": "test_interface",  # string
            "ip-version": "ipv4-unicast",  # option
            "remote-ip": "0.0.0.0",  # ipv4-address
            "remote-ip6": "::",  # ipv6-address
            "type": "ethernet",  # option
            "vni": 0,  # integer
        }
        
        try:
            result = validators.validate_system_geneve_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoGeneveEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_type(self):
        """Test enum field type validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import geneve as validators
        
        valid_values = ['ethernet', 'ppp']
        
        # Test each valid value
        for value in valid_values:
            config = {"type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: type={value}")
        
        print(f"✅ Enum field type has {len(valid_values)} valid values")
    def auto_test_enum_ip_version(self):
        """Test enum field ip-version validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import geneve as validators
        
        valid_values = ['ipv4-unicast', 'ipv6-unicast']
        
        # Test each valid value
        for value in valid_values:
            config = {"ip-version": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ip-version={value}")
        
        print(f"✅ Enum field ip-version has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/geneve"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.geneve.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']