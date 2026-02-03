import sys
from pathlib import Path

# Add pytest directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from hfortix_fortios._helpers.validation import (
    validate_required_fields,
    validate_enum_field,
    validate_query_parameter,
    validate_multiple_enums,
    validate_multiple_query_params,
)


def test_validate_required_fields_from_validation():
    """Test: Validate required fields with descriptions"""
    field_descriptions = {
        'name': 'Object name',
        'subnet': 'Network subnet in CIDR notation',
        'interface': 'Network interface name'
    }
    
    # Valid case - all fields present
    payload = {'name': 'test', 'subnet': '10.0.0.0/24'}
    is_valid, error = validate_required_fields(
        payload, 
        ['name', 'subnet'], 
        field_descriptions
    )
    assert is_valid == True
    assert error is None
    
    # Invalid case - missing field
    is_valid, error = validate_required_fields(
        payload, 
        ['name', 'subnet', 'interface'], 
        field_descriptions
    )
    assert is_valid == False
    assert error is not None
    assert 'interface' in error
    assert 'Missing required field' in error


def test_validate_enum_field():
    """Test: Validate enum field value"""
    field_descriptions = {
        'status': 'Enable/disable entry',
        'type': 'Object type'
    }
    
    # Valid enum value
    is_valid, error = validate_enum_field(
        field_name='status',
        value='enable',
        valid_values=['enable', 'disable'],
        field_descriptions=field_descriptions
    )
    assert is_valid == True
    assert error is None
    
    # Invalid enum value
    is_valid, error = validate_enum_field(
        field_name='status',
        value='invalid',
        valid_values=['enable', 'disable'],
        field_descriptions=field_descriptions
    )
    assert is_valid == False
    assert error is not None
    assert 'Invalid value' in error
    assert 'status' in error
    assert 'invalid' in error
    assert 'enable' in error
    assert 'disable' in error


def test_validate_query_parameter():
    """Test: Validate query parameter value"""
    # Valid query parameter
    is_valid, error = validate_query_parameter(
        param_name='action',
        value='default',
        valid_values=['default', 'schema']
    )
    assert is_valid == True
    assert error is None
    
    # None value (allowed)
    is_valid, error = validate_query_parameter(
        param_name='action',
        value=None,
        valid_values=['default', 'schema']
    )
    assert is_valid == True
    assert error is None
    
    # Empty string (allowed)
    is_valid, error = validate_query_parameter(
        param_name='action',
        value='',
        valid_values=['default', 'schema']
    )
    assert is_valid == True
    assert error is None
    
    # Invalid query parameter
    is_valid, error = validate_query_parameter(
        param_name='action',
        value='invalid',
        valid_values=['default', 'schema']
    )
    assert is_valid == False
    assert error is not None
    assert 'Invalid query parameter' in error
    assert 'action' in error
    assert 'invalid' in error


def test_validate_multiple_enums():
    """Test: Validate multiple enum fields at once"""
    field_descriptions = {
        'status': 'Enable/disable status',
        'type': 'Object type',
        'action': 'Action to perform'
    }
    
    enum_fields = {
        'status': ['enable', 'disable'],
        'type': ['iprange', 'subnet', 'fqdn'],
        'action': ['accept', 'deny']
    }
    
    # All valid enum values
    payload = {
        'status': 'enable',
        'type': 'subnet',
        'action': 'accept'
    }
    is_valid, error = validate_multiple_enums(
        payload,
        enum_fields,
        field_descriptions
    )
    assert is_valid == True
    assert error is None
    
    # One invalid enum value
    payload = {
        'status': 'enable',
        'type': 'invalid_type',
        'action': 'accept'
    }
    is_valid, error = validate_multiple_enums(
        payload,
        enum_fields,
        field_descriptions
    )
    assert is_valid == False
    assert error is not None
    assert 'type' in error
    assert 'invalid_type' in error
    
    # Field not in payload (should be valid - optional field)
    payload = {
        'status': 'enable'
    }
    is_valid, error = validate_multiple_enums(
        payload,
        enum_fields,
        field_descriptions
    )
    assert is_valid == True
    assert error is None


def test_validate_multiple_query_params():
    """Test: Validate multiple query parameters at once"""
    valid_params = {
        'action': ['default', 'schema'],
        'format': ['json', 'xml'],
        'vdom': ['root', 'global']
    }
    
    # All valid query parameters
    params = {
        'action': 'schema',
        'format': 'json',
        'vdom': 'root'
    }
    is_valid, error = validate_multiple_query_params(
        params,
        valid_params
    )
    assert is_valid == True
    assert error is None
    
    # One invalid query parameter
    params = {
        'action': 'schema',
        'format': 'invalid_format',
        'vdom': 'root'
    }
    is_valid, error = validate_multiple_query_params(
        params,
        valid_params
    )
    assert is_valid == False
    assert error is not None
    assert 'format' in error
    assert 'invalid_format' in error
    
    # Param not in params dict (should be valid - optional param)
    params = {
        'action': 'schema'
    }
    is_valid, error = validate_multiple_query_params(
        params,
        valid_params
    )
    assert is_valid == True
    assert error is None


if __name__ == "__main__":
    test_validate_required_fields_from_validation()
    print("✓ test_validate_required_fields_from_validation passed")
    
    test_validate_enum_field()
    print("✓ test_validate_enum_field passed")
    
    test_validate_query_parameter()
    print("✓ test_validate_query_parameter passed")
    
    test_validate_multiple_enums()
    print("✓ test_validate_multiple_enums passed")
    
    test_validate_multiple_query_params()
    print("✓ test_validate_multiple_query_params passed")
    
    print("\n✓ All endpoint validation tests passed!")
