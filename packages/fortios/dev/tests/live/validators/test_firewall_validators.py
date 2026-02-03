import sys
from pathlib import Path

# Add pytest directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from hfortix_fortios._helpers.validators import (
    validate_policy_id,
    validate_address_pairs,
    validate_seq_num,
)


def test_validate_policy_id():
    """Test: Validate policy ID is valid and within range"""
    # Valid policy IDs
    validate_policy_id(1, "delete")
    validate_policy_id(100, "update")
    validate_policy_id("500", "create")
    validate_policy_id(0, "operation")
    validate_policy_id(4294967295, "operation")  # Max value
    
    # Invalid policy IDs
    try:
        validate_policy_id(None, "delete")
        assert False, "Should raise ValueError for None policy_id"
    except ValueError as e:
        assert "required" in str(e)
    
    try:
        validate_policy_id("", "delete")
        assert False, "Should raise ValueError for empty string"
    except ValueError as e:
        assert "empty" in str(e)
    
    try:
        validate_policy_id("invalid", "delete")
        assert False, "Should raise ValueError for non-integer string"
    except ValueError as e:
        assert "valid integer" in str(e)
    
    try:
        validate_policy_id(-1, "delete")
        assert False, "Should raise ValueError for negative policy_id"
    except ValueError:
        pass
    
    try:
        validate_policy_id(4294967296, "delete")  # Beyond max
        assert False, "Should raise ValueError for policy_id > max"
    except ValueError:
        pass


def test_validate_address_pairs():
    """Test: Validate address pairs are complete"""
    # Valid pairs
    validate_address_pairs(
        srcaddr="10.0.0.1",
        dstaddr="192.168.1.1",
        srcaddr6=None,
        dstaddr6=None
    )
    
    validate_address_pairs(
        srcaddr=None,
        dstaddr=None,
        srcaddr6="2001:db8::1",
        dstaddr6="fe80::1"
    )
    
    validate_address_pairs(
        srcaddr="10.0.0.1",
        dstaddr="192.168.1.1",
        srcaddr6="2001:db8::1",
        dstaddr6="fe80::1"
    )
    
    # Invalid pairs - missing destination
    try:
        validate_address_pairs(
            srcaddr="10.0.0.1",
            dstaddr=None,
            srcaddr6=None,
            dstaddr6=None
        )
        assert False, "Should raise ValueError for IPv4 src without dst"
    except ValueError as e:
        assert "dstaddr" in str(e)
    
    # Invalid pairs - missing source
    try:
        validate_address_pairs(
            srcaddr=None,
            dstaddr="192.168.1.1",
            srcaddr6=None,
            dstaddr6=None
        )
        assert False, "Should raise ValueError for IPv4 dst without src"
    except ValueError as e:
        assert "srcaddr" in str(e)
    
    # Invalid pairs - no addresses at all
    try:
        validate_address_pairs(
            srcaddr=None,
            dstaddr=None,
            srcaddr6=None,
            dstaddr6=None
        )
        assert False, "Should raise ValueError for no address pairs"
    except ValueError as e:
        assert "At least one complete address pair" in str(e)
    
    # Invalid pairs - IPv6 missing destination
    try:
        validate_address_pairs(
            srcaddr=None,
            dstaddr=None,
            srcaddr6="2001:db8::1",
            dstaddr6=None
        )
        assert False, "Should raise ValueError for IPv6 src without dst"
    except ValueError as e:
        assert "dstaddr6" in str(e)


def test_validate_seq_num():
    """Test: Validate sequence number is valid and within range"""
    # Valid sequence numbers
    validate_seq_num(1, "update")
    validate_seq_num(100, "create")
    validate_seq_num("500", "delete")
    validate_seq_num(0, "operation")
    validate_seq_num(4294967295, "operation")  # Max value
    
    # Invalid sequence numbers
    try:
        validate_seq_num(None, "update")
        assert False, "Should raise ValueError for None seq_num"
    except ValueError as e:
        assert "required" in str(e)
    
    try:
        validate_seq_num("", "update")
        assert False, "Should raise ValueError for empty string"
    except ValueError as e:
        assert "empty" in str(e)
    
    try:
        validate_seq_num("invalid", "update")
        assert False, "Should raise ValueError for non-integer string"
    except ValueError as e:
        assert "valid integer" in str(e)
    
    try:
        validate_seq_num(-1, "update")
        assert False, "Should raise ValueError for negative seq_num"
    except ValueError:
        pass
    
    try:
        validate_seq_num(4294967296, "update")  # Beyond max
        assert False, "Should raise ValueError for seq_num > max"
    except ValueError:
        pass


if __name__ == "__main__":
    test_validate_policy_id()
    print("✓ test_validate_policy_id passed")
    
    test_validate_address_pairs()
    print("✓ test_validate_address_pairs passed")
    
    test_validate_seq_num()
    print("✓ test_validate_seq_num passed")
    
    print("\n✓ All firewall validator tests passed!")
