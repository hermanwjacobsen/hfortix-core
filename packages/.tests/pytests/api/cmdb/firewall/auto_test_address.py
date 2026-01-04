"""
Auto-generated basic tests for cmdb.firewall/address

Generated from schema: /app/dev/classes/fortinet/.dev/schemas/v7.6/cmdb/firewall/address.json
Category: cmdb
Endpoint: /cmdb/firewall/address

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_address.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt


class TestAutoAddressGet:
    """Auto-generated GET operation tests."""
    
    def auto_test_get_list_all(self):
        """Test GET - list all address items."""
        result = fgt.api.cmdb.firewall.address.get()
        
        # Verify response
        assert result is not None
        # CMDB endpoints return list
        assert isinstance(result, list)
        print(f"✅ Retrieved {len(result)} address items")
        
        # If items exist, verify structure
        if len(result) > 0:
            item = result[0]
            assert "name" in item
            print(f"   First item name: {item.get('name', 'N/A')}")
    
    def auto_test_get_specific_item(self):
        """Test GET - retrieve specific address by name."""
        # First get all items to find one to test with
        all_items = fgt.api.cmdb.firewall.address.get()
        
        if not all_items or len(all_items) == 0:
            pytest.skip("No existing address items to test with")
        
        # Get first item's name
        mkey_value = all_items[0]["name"]
        
        # Get specific item
        result = fgt.api.cmdb.firewall.address.get(name=mkey_value)
        
        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0]["name"] == mkey_value
        print(f"✅ Retrieved address name={mkey_value}")
    
    def auto_test_get_with_vdom(self):
        """Test GET - with vdom parameter."""
        result = fgt.api.cmdb.firewall.address.get(vdom="root")
        
        assert result is not None
        print(f"✅ GET with vdom=root successful")
    
    def auto_test_get_with_filters(self):
        """Test GET - with filter parameters."""
        # Test with common filter options
        result = fgt.api.cmdb.firewall.address.get(
            filter="",  # No filter (get all)
            format="name|name",  # Limit fields
        )
        
        assert result is not None
        print(f"✅ GET with filters successful")


class TestAutoAddressExists:
    """Auto-generated exists() tests."""
    
    def auto_test_exists_method(self):
        """Test exists() helper method."""
        # Get existing items
        all_items = fgt.api.cmdb.firewall.address.get()
        
        if all_items and len(all_items) > 0:
            # Test with existing item
            mkey_value = all_items[0]["name"]
            exists = fgt.api.cmdb.firewall.address.exists(name=mkey_value)
            assert exists is True
            print(f"✅ exists(name={mkey_value}) = True")
            
            # Test with non-existing item (hopefully)
            non_existing = "nonexistent_auto_test_item_12345"
            exists = fgt.api.cmdb.firewall.address.exists(name=non_existing)
            assert exists is False
            print(f"✅ exists(name={non_existing}) = False")
        else:
            pytest.skip("No existing address items to test exists() with")


class TestAutoAddressValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.firewall._helpers.address import (
                validate_firewall_address_get,
                validate_firewall_address_post,
                validate_firewall_address_put,
                REQUIRED_FIELDS,
            )
            print("✅ Validators imported successfully")
            assert REQUIRED_FIELDS is not None
            print(f"   Required fields: {REQUIRED_FIELDS}")
        except ImportError as e:
            pytest.skip(f"Validators not available: {e}")
    
    def auto_test_validator_required_fields(self):
        """Test required fields validation."""
        try:
            from hfortix_fortios.api.v2.cmdb.firewall._helpers.address import (
                validate_required_fields,
                REQUIRED_FIELDS,
            )
            
            # Test with empty payload (should fail)
            is_valid, error = validate_required_fields({})
            assert is_valid is False
            assert error is not None
            print(f"✅ Empty payload validation failed correctly: {error}")
            
            # Test with all required fields (should pass)
            payload = {'interface': [{'name': 'all'}], 'filter': ''}
            is_valid, error = validate_required_fields(payload)
            if not is_valid:
                print(f"⚠️  Validation failed: {error}")
                print(f"   Payload: {payload}")
                print(f"   Required: {REQUIRED_FIELDS}")
            # Note: May still fail if payload needs adjustment
            
        except ImportError as e:
            pytest.skip(f"Validators not available: {e}")
    
    def auto_test_validator_get(self):
        """Test GET validator."""
        try:
            from hfortix_fortios.api.v2.cmdb.firewall._helpers.address import (
                validate_firewall_address_get,
            )
            
            # GET with no params should be valid
            is_valid, error = validate_firewall_address_get()
            assert is_valid is True
            assert error is None
            print("✅ GET validator passed with no params")
            
            # GET with common params
            is_valid, error = validate_firewall_address_get(
                vdom="root",
                filter="",
            )
            assert is_valid is True
            print("✅ GET validator passed with vdom and filter")
            
        except ImportError as e:
            pytest.skip(f"Validators not available: {e}")
    
    def auto_test_validator_enum_type(self):
        """Test enum validation for type field."""
        try:
            from hfortix_fortios.api.v2.cmdb.firewall._helpers.address import (
                VALID_BODY_TYPE,
            )
            
            # Verify enum values are defined
            assert VALID_BODY_TYPE is not None
            assert len(VALID_BODY_TYPE) > 0
            print(f"✅ Enum type has {len(VALID_BODY_TYPE)} valid values")
            
            # Verify expected values are in enum
            expected = ['ipmask', 'iprange', 'fqdn', 'geography', 'wildcard', 'dynamic', 'interface-subnet', 'mac', 'route-tag']
            for value in expected:
                assert value in VALID_BODY_TYPE
            print(f"   Valid values: {VALID_BODY_TYPE}")
            
        except (ImportError, AttributeError) as e:
            pytest.skip(f"Enum validation not available: {e}")
    def auto_test_validator_enum_sub_type(self):
        """Test enum validation for sub-type field."""
        try:
            from hfortix_fortios.api.v2.cmdb.firewall._helpers.address import (
                VALID_BODY_SUB_TYPE,
            )
            
            # Verify enum values are defined
            assert VALID_BODY_SUB_TYPE is not None
            assert len(VALID_BODY_SUB_TYPE) > 0
            print(f"✅ Enum sub-type has {len(VALID_BODY_SUB_TYPE)} valid values")
            
            # Verify expected values are in enum
            expected = ['sdn', 'clearpass-spt', 'fsso', 'rsso', 'ems-tag', 'fortivoice-tag', 'fortinac-tag', 'swc-tag', 'device-identification', 'external-resource', 'obsolete']
            for value in expected:
                assert value in VALID_BODY_SUB_TYPE
            print(f"   Valid values: {VALID_BODY_SUB_TYPE}")
            
        except (ImportError, AttributeError) as e:
            pytest.skip(f"Enum validation not available: {e}")
    def auto_test_validator_enum_clearpass_spt(self):
        """Test enum validation for clearpass-spt field."""
        try:
            from hfortix_fortios.api.v2.cmdb.firewall._helpers.address import (
                VALID_BODY_CLEARPASS_SPT,
            )
            
            # Verify enum values are defined
            assert VALID_BODY_CLEARPASS_SPT is not None
            assert len(VALID_BODY_CLEARPASS_SPT) > 0
            print(f"✅ Enum clearpass-spt has {len(VALID_BODY_CLEARPASS_SPT)} valid values")
            
            # Verify expected values are in enum
            expected = ['unknown', 'healthy', 'quarantine', 'checkup', 'transient', 'infected']
            for value in expected:
                assert value in VALID_BODY_CLEARPASS_SPT
            print(f"   Valid values: {VALID_BODY_CLEARPASS_SPT}")
            
        except (ImportError, AttributeError) as e:
            pytest.skip(f"Enum validation not available: {e}")
    def auto_test_validator_enum_obj_type(self):
        """Test enum validation for obj-type field."""
        try:
            from hfortix_fortios.api.v2.cmdb.firewall._helpers.address import (
                VALID_BODY_OBJ_TYPE,
            )
            
            # Verify enum values are defined
            assert VALID_BODY_OBJ_TYPE is not None
            assert len(VALID_BODY_OBJ_TYPE) > 0
            print(f"✅ Enum obj-type has {len(VALID_BODY_OBJ_TYPE)} valid values")
            
            # Verify expected values are in enum
            expected = ['ip', 'mac']
            for value in expected:
                assert value in VALID_BODY_OBJ_TYPE
            print(f"   Valid values: {VALID_BODY_OBJ_TYPE}")
            
        except (ImportError, AttributeError) as e:
            pytest.skip(f"Enum validation not available: {e}")
    def auto_test_validator_enum_sdn_addr_type(self):
        """Test enum validation for sdn-addr-type field."""
        try:
            from hfortix_fortios.api.v2.cmdb.firewall._helpers.address import (
                VALID_BODY_SDN_ADDR_TYPE,
            )
            
            # Verify enum values are defined
            assert VALID_BODY_SDN_ADDR_TYPE is not None
            assert len(VALID_BODY_SDN_ADDR_TYPE) > 0
            print(f"✅ Enum sdn-addr-type has {len(VALID_BODY_SDN_ADDR_TYPE)} valid values")
            
            # Verify expected values are in enum
            expected = ['private', 'public', 'all']
            for value in expected:
                assert value in VALID_BODY_SDN_ADDR_TYPE
            print(f"   Valid values: {VALID_BODY_SDN_ADDR_TYPE}")
            
        except (ImportError, AttributeError) as e:
            pytest.skip(f"Enum validation not available: {e}")
    def auto_test_validator_enum_node_ip_only(self):
        """Test enum validation for node-ip-only field."""
        try:
            from hfortix_fortios.api.v2.cmdb.firewall._helpers.address import (
                VALID_BODY_NODE_IP_ONLY,
            )
            
            # Verify enum values are defined
            assert VALID_BODY_NODE_IP_ONLY is not None
            assert len(VALID_BODY_NODE_IP_ONLY) > 0
            print(f"✅ Enum node-ip-only has {len(VALID_BODY_NODE_IP_ONLY)} valid values")
            
            # Verify expected values are in enum
            expected = ['enable', 'disable']
            for value in expected:
                assert value in VALID_BODY_NODE_IP_ONLY
            print(f"   Valid values: {VALID_BODY_NODE_IP_ONLY}")
            
        except (ImportError, AttributeError) as e:
            pytest.skip(f"Enum validation not available: {e}")
    def auto_test_validator_enum_allow_routing(self):
        """Test enum validation for allow-routing field."""
        try:
            from hfortix_fortios.api.v2.cmdb.firewall._helpers.address import (
                VALID_BODY_ALLOW_ROUTING,
            )
            
            # Verify enum values are defined
            assert VALID_BODY_ALLOW_ROUTING is not None
            assert len(VALID_BODY_ALLOW_ROUTING) > 0
            print(f"✅ Enum allow-routing has {len(VALID_BODY_ALLOW_ROUTING)} valid values")
            
            # Verify expected values are in enum
            expected = ['enable', 'disable']
            for value in expected:
                assert value in VALID_BODY_ALLOW_ROUTING
            print(f"   Valid values: {VALID_BODY_ALLOW_ROUTING}")
            
        except (ImportError, AttributeError) as e:
            pytest.skip(f"Enum validation not available: {e}")
    def auto_test_validator_enum_fabric_object(self):
        """Test enum validation for fabric-object field."""
        try:
            from hfortix_fortios.api.v2.cmdb.firewall._helpers.address import (
                VALID_BODY_FABRIC_OBJECT,
            )
            
            # Verify enum values are defined
            assert VALID_BODY_FABRIC_OBJECT is not None
            assert len(VALID_BODY_FABRIC_OBJECT) > 0
            print(f"✅ Enum fabric-object has {len(VALID_BODY_FABRIC_OBJECT)} valid values")
            
            # Verify expected values are in enum
            expected = ['enable', 'disable']
            for value in expected:
                assert value in VALID_BODY_FABRIC_OBJECT
            print(f"   Valid values: {VALID_BODY_FABRIC_OBJECT}")
            
        except (ImportError, AttributeError) as e:
            pytest.skip(f"Enum validation not available: {e}")


# Summary of auto-generated tests:
# ✅ GET list all
# ✅ GET specific item (if mkey exists)
# ✅ GET with vdom
# ✅ GET with filters (CMDB only)
# ✅ exists() method (CMDB only)
# ✅ Validator imports
# ✅ Required fields validation
# ✅ GET validator
# ✅ Enum validators (for each enum field)
#
# For comprehensive CRUD testing, create manual tests in test_address.py
# including POST, PUT, DELETE operations with cleanup fixtures.