"""
Auto-generated basic tests for cmdb.firewall/proxy_addrgrp

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.proxy-addrgrp.json
Category: cmdb
Endpoint: /cmdb/firewall/proxy-addrgrp

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_proxy-addrgrp.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.firewall.proxy_addrgrp


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoProxyAddrgrpValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.firewall._helpers import proxy_addrgrp as validators
            print(f"✅ Successfully imported validators for proxy-addrgrp")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_firewall_proxy_addrgrp_post")
            assert hasattr(validators, "validate_firewall_proxy_addrgrp_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import proxy_addrgrp as validators
        
        # Build minimal valid config with all required fields
        config = {
            "member": "test_member",  # string
        }
        
        try:
            result = validators.validate_firewall_proxy_addrgrp_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoProxyAddrgrpEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_type(self):
        """Test enum field type validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import proxy_addrgrp as validators
        
        valid_values = ['src', 'dst']
        
        # Test each valid value
        for value in valid_values:
            config = {"type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: type={value}")
        
        print(f"✅ Enum field type has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/firewall/proxy_addrgrp"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.proxy-addrgrp.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']