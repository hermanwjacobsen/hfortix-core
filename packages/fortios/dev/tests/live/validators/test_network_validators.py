import sys
from pathlib import Path

# Add pytest directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from hfortix_fortios._helpers.validators import (
    validate_mac_address,
    validate_ip_address,
    validate_ipv6_address,
    validate_ip_network,
    validate_port_number,
)


def test_validate_mac_address():
    """Test: Validate MAC address format"""
    # Valid MAC addresses
    validate_mac_address("00:11:22:33:44:55")
    validate_mac_address("AA:BB:CC:DD:EE:FF")
    validate_mac_address("00:00:00:00:00:00")  # Wildcard allowed by default
    
    # Invalid MAC addresses
    try:
        validate_mac_address("invalid")
        assert False, "Should raise ValueError for invalid format"
    except ValueError:
        pass
    
    try:
        validate_mac_address("00:11:22:33:44")  # Too short
        assert False, "Should raise ValueError for incomplete MAC"
    except ValueError:
        pass
    
    try:
        validate_mac_address("00:11:22:33:44:55:66")  # Too long
        assert False, "Should raise ValueError for too many octets"
    except ValueError:
        pass
    
    # Wildcard not allowed
    try:
        validate_mac_address("00:00:00:00:00:00", allow_wildcard=False)
        assert False, "Should raise ValueError for wildcard when not allowed"
    except ValueError:
        pass


def test_validate_ip_address():
    """Test: Validate IPv4 address format"""
    # Valid IP addresses
    validate_ip_address("192.168.1.1")
    validate_ip_address("10.0.0.1")
    validate_ip_address("0.0.0.0")  # Wildcard allowed by default
    validate_ip_address("255.255.255.255")
    
    # Invalid IP addresses
    try:
        validate_ip_address("invalid")
        assert False, "Should raise ValueError for invalid format"
    except ValueError:
        pass
    
    try:
        validate_ip_address("256.1.1.1")  # Out of range
        assert False, "Should raise ValueError for out of range"
    except ValueError:
        pass
    
    try:
        validate_ip_address("192.168.1")  # Incomplete
        assert False, "Should raise ValueError for incomplete IP"
    except ValueError:
        pass
    
    # Wildcard not allowed
    try:
        validate_ip_address("0.0.0.0", allow_wildcard=False)
        assert False, "Should raise ValueError for wildcard when not allowed"
    except ValueError:
        pass


def test_validate_ipv6_address():
    """Test: Validate IPv6 address format"""
    # Valid IPv6 addresses
    validate_ipv6_address("2001:db8::1")
    validate_ipv6_address("::1")  # Loopback
    validate_ipv6_address("::")  # Wildcard allowed by default
    validate_ipv6_address("fe80::1")
    validate_ipv6_address("2001:0db8:0000:0000:0000:0000:0000:0001")  # Full notation
    
    # Invalid IPv6 addresses
    try:
        validate_ipv6_address("invalid")
        assert False, "Should raise ValueError for invalid format"
    except ValueError:
        pass
    
    try:
        validate_ipv6_address("192.168.1.1")  # IPv4 address
        assert False, "Should raise ValueError for IPv4 address"
    except ValueError:
        pass
    
    # Wildcard not allowed
    try:
        validate_ipv6_address("::", allow_wildcard=False)
        assert False, "Should raise ValueError for wildcard when not allowed"
    except ValueError:
        pass


def test_validate_ip_network():
    """Test: Validate IP network/subnet in CIDR notation"""
    # Valid IPv4 networks
    validate_ip_network("192.168.1.0/24")
    validate_ip_network("10.0.0.0/8")
    validate_ip_network("172.16.0.0/12")
    validate_ip_network("0.0.0.0/0")
    validate_ip_network("192.168.1.0/32")  # Single host
    
    # Valid IPv6 networks
    validate_ip_network("2001:db8::/32", version=6)
    validate_ip_network("::/0", version=6)
    validate_ip_network("fe80::/10", version=6)
    
    # Invalid networks
    try:
        validate_ip_network("invalid")
        assert False, "Should raise ValueError for invalid format"
    except ValueError:
        pass
    
    try:
        validate_ip_network("192.168.1.0/33")  # Invalid CIDR (> 32)
        assert False, "Should raise ValueError for invalid CIDR"
    except ValueError:
        pass
    
    try:
        validate_ip_network("256.1.1.1/24")  # Invalid IP
        assert False, "Should raise ValueError for invalid IP in network"
    except ValueError:
        pass


def test_validate_port_number():
    """Test: Validate port number is within valid range"""
    # Valid ports
    validate_port_number(22, "ssh_port")
    validate_port_number(80, "http_port")
    validate_port_number(443, "https_port")
    validate_port_number(0, "port")  # Min value
    validate_port_number(65535, "port")
    validate_port_number(None, "port")
    
    # Invalid ports
    try:
        validate_port_number(-1, "port")
        assert False, "Should raise ValueError for negative port"
    except ValueError:
        pass
    
    try:
        validate_port_number(4294967296, "port")  # Beyond max
        assert False, "Should raise ValueError for port > max"
    except ValueError:
        pass


if __name__ == "__main__":
    test_validate_mac_address()
    print("✓ test_validate_mac_address passed")
    
    test_validate_ip_address()
    print("✓ test_validate_ip_address passed")
    
    test_validate_ipv6_address()
    print("✓ test_validate_ipv6_address passed")
    
    test_validate_ip_network()
    print("✓ test_validate_ip_network passed")
    
    test_validate_port_number()
    print("✓ test_validate_port_number passed")
    
    print("\n✓ All network validator tests passed!")
