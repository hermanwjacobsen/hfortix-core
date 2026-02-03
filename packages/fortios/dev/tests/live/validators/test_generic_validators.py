import sys
from pathlib import Path

# Add pytest directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from hfortix_fortios._helpers.validators import (
    validate_required_fields,
    validate_color,
    validate_status,
    validate_enable_disable,
    validate_string_length,
    validate_integer_range,
)


def test_validate_required_fields():
    """Test: Validate required fields are present"""
    # Valid case - all fields present
    payload = {'name': 'test', 'subnet': '10.0.0.0/24'}
    is_valid, missing = validate_required_fields(payload, ['name', 'subnet'])
    assert is_valid == True
    assert missing == []
    
    # Invalid case - missing field
    is_valid, missing = validate_required_fields(payload, ['name', 'subnet', 'interface'])
    assert is_valid == False
    assert 'interface' in missing


def test_validate_color():
    """Test: Validate color index (0-32)"""
    # Valid colors
    validate_color(0)
    validate_color(16)
    validate_color(32)
    
    # Invalid colors
    try:
        validate_color(-1)
        assert False, "Should raise ValueError for negative color"
    except ValueError:
        pass
    
    try:
        validate_color(33)
        assert False, "Should raise ValueError for color > 32"
    except ValueError:
        pass


def test_validate_status():
    """Test: Validate status field (enable/disable)"""
    # Valid status
    validate_status("enable")
    validate_status("disable")
    
    # Invalid status
    try:
        validate_status("invalid")
        assert False, "Should raise ValueError for invalid status"
    except ValueError:
        pass
    
    try:
        validate_status("enabled")
        assert False, "Should raise ValueError for 'enabled'"
    except ValueError:
        pass


def test_validate_enable_disable():
    """Test: Validate enable/disable value with field name"""
    # Valid values
    validate_enable_disable("enable", "test_field")
    validate_enable_disable("disable", "test_field")
    validate_enable_disable(None, "test_field")
    
    # Invalid value
    try:
        validate_enable_disable("on", "test_field")
        assert False, "Should raise ValueError for 'on'"
    except ValueError as e:
        assert "test_field" in str(e)


def test_validate_string_length():
    """Test: Validate string length does not exceed maximum"""
    # Valid lengths
    validate_string_length("test", 10, "name")
    validate_string_length("", 5, "name")
    validate_string_length(None, 10, "name")
    
    # Invalid length
    try:
        validate_string_length("very_long_string", 5, "name")
        assert False, "Should raise ValueError for string exceeding max length"
    except ValueError as e:
        assert "name" in str(e)
        assert "5" in str(e)


def test_validate_integer_range():
    """Test: Validate integer is within specified range"""
    # Valid ranges
    validate_integer_range(50, 1, 100, "timeout")
    validate_integer_range(1, 1, 100, "timeout")
    validate_integer_range(100, 1, 100, "timeout")
    validate_integer_range(None, 1, 100, "timeout")
    
    # Invalid ranges
    try:
        validate_integer_range(0, 1, 100, "timeout")
        assert False, "Should raise ValueError for value below minimum"
    except ValueError as e:
        assert "timeout" in str(e)
    
    try:
        validate_integer_range(150, 1, 100, "timeout")
        assert False, "Should raise ValueError for value above maximum"
    except ValueError as e:
        assert "timeout" in str(e)


if __name__ == "__main__":
    test_validate_required_fields()
    print("✓ test_validate_required_fields passed")
    
    test_validate_color()
    print("✓ test_validate_color passed")
    
    test_validate_status()
    print("✓ test_validate_status passed")
    
    test_validate_enable_disable()
    print("✓ test_validate_enable_disable passed")
    
    test_validate_string_length()
    print("✓ test_validate_string_length passed")
    
    test_validate_integer_range()
    print("✓ test_validate_integer_range passed")
    
    print("\n✓ All generic validator tests passed!")
