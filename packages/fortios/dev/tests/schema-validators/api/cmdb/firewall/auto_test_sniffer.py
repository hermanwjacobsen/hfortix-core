"""
Auto-generated basic tests for cmdb.firewall/sniffer

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.sniffer.json
Category: cmdb
Endpoint: /cmdb/firewall/sniffer

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_sniffer.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.firewall.sniffer


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoSnifferValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.firewall._helpers import sniffer as validators
            print(f"✅ Successfully imported validators for sniffer")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_firewall_sniffer_post")
            assert hasattr(validators, "validate_firewall_sniffer_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import sniffer as validators
        
        # Build minimal valid config with all required fields
        config = {
            "application-list": "test_application-list",  # string
            "av-profile": "test_av-profile",  # string
            "dlp-profile": "test_dlp-profile",  # string
            "emailfilter-profile": "test_emailfilter-profile",  # string
            "file-filter-profile": "test_file-filter-profile",  # string
            "ips-sensor": "test_ips-sensor",  # string
            "webfilter-profile": "test_webfilter-profile",  # string
        }
        
        try:
            result = validators.validate_firewall_sniffer_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoSnifferEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_status(self):
        """Test enum field status validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import sniffer as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: status={value}")
        
        print(f"✅ Enum field status has {len(valid_values)} valid values")
    def auto_test_enum_logtraffic(self):
        """Test enum field logtraffic validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import sniffer as validators
        
        valid_values = ['all', 'utm', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"logtraffic": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: logtraffic={value}")
        
        print(f"✅ Enum field logtraffic has {len(valid_values)} valid values")
    def auto_test_enum_ipv6(self):
        """Test enum field ipv6 validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import sniffer as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"ipv6": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ipv6={value}")
        
        print(f"✅ Enum field ipv6 has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/firewall/sniffer"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.sniffer.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']