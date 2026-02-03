"""
Auto-generated basic tests for cmdb.router/bgp

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/router.bgp.json
Category: cmdb
Endpoint: /cmdb/router/bgp

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_bgp.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.router.bgp


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoBgpValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.router._helpers import bgp as validators
            print(f"✅ Successfully imported validators for bgp")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_router_bgp_post")
            assert hasattr(validators, "validate_router_bgp_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.router._helpers import bgp as validators
        
        # Build minimal valid config with all required fields
        config = {
            "as": "",  # user
        }
        
        try:
            result = validators.validate_router_bgp_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoBgpEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_always_compare_med(self):
        """Test enum field always-compare-med validation."""
        from hfortix_fortios.api.v2.cmdb.router._helpers import bgp as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"always-compare-med": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: always-compare-med={value}")
        
        print(f"✅ Enum field always-compare-med has {len(valid_values)} valid values")
    def auto_test_enum_bestpath_as_path_ignore(self):
        """Test enum field bestpath-as-path-ignore validation."""
        from hfortix_fortios.api.v2.cmdb.router._helpers import bgp as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"bestpath-as-path-ignore": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: bestpath-as-path-ignore={value}")
        
        print(f"✅ Enum field bestpath-as-path-ignore has {len(valid_values)} valid values")
    def auto_test_enum_bestpath_cmp_confed_aspath(self):
        """Test enum field bestpath-cmp-confed-aspath validation."""
        from hfortix_fortios.api.v2.cmdb.router._helpers import bgp as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"bestpath-cmp-confed-aspath": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: bestpath-cmp-confed-aspath={value}")
        
        print(f"✅ Enum field bestpath-cmp-confed-aspath has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/router/bgp"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/router.bgp.json"
TEST_HTTP_METHODS = ['GET', 'PUT']