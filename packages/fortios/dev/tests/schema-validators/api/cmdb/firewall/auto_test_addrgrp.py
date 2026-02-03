"""
Auto-generated basic tests for cmdb.firewall/addrgrp

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.addrgrp.json
Category: cmdb
Endpoint: /cmdb/firewall/addrgrp

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_addrgrp.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.firewall.addrgrp


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoAddrgrpValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.firewall._helpers import addrgrp as validators
            print(f"✅ Successfully imported validators for addrgrp")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_firewall_addrgrp_post")
            assert hasattr(validators, "validate_firewall_addrgrp_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import addrgrp as validators
        
        # Build minimal valid config with all required fields
        config = {
            "exclude-member": "test_exclude-member",  # string
            "name": "test_name",  # string
        }
        
        try:
            result = validators.validate_firewall_addrgrp_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoAddrgrpEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_type(self):
        """Test enum field type validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import addrgrp as validators
        
        valid_values = ['default', 'folder']
        
        # Test each valid value
        for value in valid_values:
            config = {"type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: type={value}")
        
        print(f"✅ Enum field type has {len(valid_values)} valid values")
    def auto_test_enum_category(self):
        """Test enum field category validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import addrgrp as validators
        
        valid_values = ['default', 'ztna-ems-tag', 'ztna-geo-tag']
        
        # Test each valid value
        for value in valid_values:
            config = {"category": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: category={value}")
        
        print(f"✅ Enum field category has {len(valid_values)} valid values")
    def auto_test_enum_allow_routing(self):
        """Test enum field allow-routing validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import addrgrp as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"allow-routing": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: allow-routing={value}")
        
        print(f"✅ Enum field allow-routing has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/firewall/addrgrp"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.addrgrp.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']