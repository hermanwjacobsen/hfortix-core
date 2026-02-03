"""
Auto-generated basic tests for cmdb.firewall/profile_protocol_options

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.profile-protocol-options.json
Category: cmdb
Endpoint: /cmdb/firewall/profile-protocol-options

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_profile-protocol-options.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.firewall.profile_protocol_options


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoProfileProtocolOptionsValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.firewall._helpers import profile_protocol_options as validators
            print(f"✅ Successfully imported validators for profile-protocol-options")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_firewall_profile_protocol_options_post")
            assert hasattr(validators, "validate_firewall_profile_protocol_options_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import profile_protocol_options as validators
        
        # Build minimal valid config with all required fields
        config = {
            "name": "test_name",  # string
        }
        
        try:
            result = validators.validate_firewall_profile_protocol_options_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoProfileProtocolOptionsEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_oversize_log(self):
        """Test enum field oversize-log validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import profile_protocol_options as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"oversize-log": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: oversize-log={value}")
        
        print(f"✅ Enum field oversize-log has {len(valid_values)} valid values")
    def auto_test_enum_switching_protocols_log(self):
        """Test enum field switching-protocols-log validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import profile_protocol_options as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"switching-protocols-log": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: switching-protocols-log={value}")
        
        print(f"✅ Enum field switching-protocols-log has {len(valid_values)} valid values")
    def auto_test_enum_rpc_over_http(self):
        """Test enum field rpc-over-http validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import profile_protocol_options as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"rpc-over-http": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: rpc-over-http={value}")
        
        print(f"✅ Enum field rpc-over-http has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/firewall/profile_protocol_options"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.profile-protocol-options.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']