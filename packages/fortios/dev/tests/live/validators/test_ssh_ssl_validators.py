import sys
from pathlib import Path

# Add pytest directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from hfortix_fortios._helpers.validators import (
    validate_ssh_host_key_type,
    validate_ssh_host_key_status,
    validate_ssh_host_key_nid,
    validate_ssh_host_key_usage,
    validate_ssh_source,
    validate_ssl_dh_bits,
    validate_ssl_cipher_action,
)


def test_validate_ssh_host_key_type():
    """Test: Validate SSH host key type"""
    # Valid key types
    validate_ssh_host_key_type("RSA")
    validate_ssh_host_key_type("DSA")
    validate_ssh_host_key_type("ECDSA")
    validate_ssh_host_key_type("ED25519")
    validate_ssh_host_key_type("RSA-CA")
    validate_ssh_host_key_type("DSA-CA")
    validate_ssh_host_key_type("ECDSA-CA")
    validate_ssh_host_key_type("ED25519-CA")
    validate_ssh_host_key_type(None)  # Optional field
    
    # Invalid key types
    try:
        validate_ssh_host_key_type("invalid")
        assert False, "Should raise ValueError for invalid key type"
    except ValueError as e:
        assert "must be one of" in str(e)


def test_validate_ssh_host_key_status():
    """Test: Validate SSH host key status"""
    # Valid statuses
    validate_ssh_host_key_status("trusted")
    validate_ssh_host_key_status("revoked")
    validate_ssh_host_key_status(None)  # Optional field
    
    # Invalid statuses
    try:
        validate_ssh_host_key_status("invalid")
        assert False, "Should raise ValueError for invalid status"
    except ValueError as e:
        assert "must be one of" in str(e)


def test_validate_ssh_host_key_nid():
    """Test: Validate SSH ECDSA key NID"""
    # Valid NIDs
    validate_ssh_host_key_nid("256")
    validate_ssh_host_key_nid("384")
    validate_ssh_host_key_nid("521")
    validate_ssh_host_key_nid(None)  # Optional field
    
    # Invalid NIDs
    try:
        validate_ssh_host_key_nid("512")
        assert False, "Should raise ValueError for invalid NID"
    except ValueError as e:
        assert "must be one of" in str(e)
    
    try:
        validate_ssh_host_key_nid("invalid")
        assert False, "Should raise ValueError for non-numeric NID"
    except ValueError:
        pass


def test_validate_ssh_host_key_usage():
    """Test: Validate SSH host key usage"""
    # Valid usages
    validate_ssh_host_key_usage("transparent-proxy")
    validate_ssh_host_key_usage("access-proxy")
    validate_ssh_host_key_usage(None)  # Optional field
    
    # Invalid usages
    try:
        validate_ssh_host_key_usage("invalid")
        assert False, "Should raise ValueError for invalid usage"
    except ValueError as e:
        assert "must be one of" in str(e)


def test_validate_ssh_source():
    """Test: Validate SSH local CA/key source type"""
    # Valid sources
    validate_ssh_source("built-in")
    validate_ssh_source("user")
    validate_ssh_source(None)  # Optional field
    
    # Invalid sources
    try:
        validate_ssh_source("invalid")
        assert False, "Should raise ValueError for invalid source"
    except ValueError as e:
        assert "must be" in str(e)


def test_validate_ssl_dh_bits():
    """Test: Validate SSL Diffie-Hellman bits"""
    # Valid DH bits
    validate_ssl_dh_bits("768")
    validate_ssl_dh_bits("1024")
    validate_ssl_dh_bits("1536")
    validate_ssl_dh_bits("2048")
    validate_ssl_dh_bits(None)  # Optional field
    
    # Invalid DH bits
    try:
        validate_ssl_dh_bits("512")
        assert False, "Should raise ValueError for invalid DH bits"
    except ValueError as e:
        assert "must be one of" in str(e)
    
    try:
        validate_ssl_dh_bits("4096")
        assert False, "Should raise ValueError for unsupported DH bits"
    except ValueError:
        pass


def test_validate_ssl_cipher_action():
    """Test: Validate SSL no-matching-cipher action"""
    # Valid actions
    validate_ssl_cipher_action("bypass")
    validate_ssl_cipher_action("drop")
    validate_ssl_cipher_action(None)  # Optional field
    
    # Invalid actions
    try:
        validate_ssl_cipher_action("invalid")
        assert False, "Should raise ValueError for invalid action"
    except ValueError as e:
        assert "must be" in str(e)


if __name__ == "__main__":
    test_validate_ssh_host_key_type()
    print("✓ test_validate_ssh_host_key_type passed")
    
    test_validate_ssh_host_key_status()
    print("✓ test_validate_ssh_host_key_status passed")
    
    test_validate_ssh_host_key_nid()
    print("✓ test_validate_ssh_host_key_nid passed")
    
    test_validate_ssh_host_key_usage()
    print("✓ test_validate_ssh_host_key_usage passed")
    
    test_validate_ssh_source()
    print("✓ test_validate_ssh_source passed")
    
    test_validate_ssl_dh_bits()
    print("✓ test_validate_ssl_dh_bits passed")
    
    test_validate_ssl_cipher_action()
    print("✓ test_validate_ssl_cipher_action passed")
    
    print("\n✓ All SSH/SSL proxy validator tests passed!")
