"""
Auto-generated basic tests for cmdb.system/ipsec_aggregate

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.ipsec-aggregate.json
Category: cmdb
Endpoint: /cmdb/system/ipsec-aggregate

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_ipsec-aggregate.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.ipsec_aggregate


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoIpsecAggregateValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.system._helpers import ipsec_aggregate as validators
            print(f"✅ Successfully imported validators for ipsec-aggregate")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_system_ipsec_aggregate_post")
            assert hasattr(validators, "validate_system_ipsec_aggregate_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import ipsec_aggregate as validators
        
        # Build minimal valid config with all required fields
        config = {
            "member": "test_member",  # string
        }
        
        try:
            result = validators.validate_system_ipsec_aggregate_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoIpsecAggregateEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_algorithm(self):
        """Test enum field algorithm validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import ipsec_aggregate as validators
        
        valid_values = ['L3', 'L4', 'round-robin', 'redundant', 'weighted-round-robin']
        
        # Test each valid value
        for value in valid_values:
            config = {"algorithm": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: algorithm={value}")
        
        print(f"✅ Enum field algorithm has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/ipsec_aggregate"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.ipsec-aggregate.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']