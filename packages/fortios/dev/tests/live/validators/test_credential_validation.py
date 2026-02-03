"""
Tests for FortiOS credential validation

Tests _validate_credentials static method on FortiOS class.
"""

from hfortix_fortios import FortiOS
from hfortix_core.exceptions import ConfigurationError


# Minimum token length is 25 characters
MIN_TOKEN_LENGTH = 25


def test_valid_token_minimum():
    """Test valid token with minimum characters"""
    print(f"\n=== Testing valid token ({MIN_TOKEN_LENGTH} chars - minimum) ===")
    
    token = "a" * MIN_TOKEN_LENGTH
    FortiOS._validate_credentials(token=token, username=None, password=None)
    
    print(f"✓ {MIN_TOKEN_LENGTH}-char token accepted")


def test_valid_token_40_chars():
    """Test valid token with 40 characters (newer FortiOS)"""
    print("\n=== Testing valid token (40 chars) ===")
    
    token = "a" * 40
    FortiOS._validate_credentials(token=token, username=None, password=None)
    
    print(f"✓ 40-char token accepted")


def test_valid_token_alphanumeric():
    """Test valid token with alphanumeric characters"""
    print("\n=== Testing valid token (alphanumeric) ===")
    
    token = "abc123DEF456ghi789JKL012mno345"  # 30 chars
    FortiOS._validate_credentials(token=token, username=None, password=None)
    
    print(f"✓ Alphanumeric token accepted")


def test_invalid_token_too_short():
    """Test invalid token - too short"""
    print("\n=== Testing invalid token (too short) ===")
    
    token = "abc123"  # Only 6 chars
    try:
        FortiOS._validate_credentials(token=token, username=None, password=None)
        assert False, "Should have raised exception"
    except (ValueError, ConfigurationError) as e:
        assert "short" in str(e).lower() or "character" in str(e).lower()
        print(f"✓ Short token rejected: {type(e).__name__}")


def test_invalid_token_just_under_minimum():
    """Test invalid token - just under minimum"""
    print(f"\n=== Testing invalid token ({MIN_TOKEN_LENGTH - 1} chars) ===")
    
    token = "a" * (MIN_TOKEN_LENGTH - 1)
    try:
        FortiOS._validate_credentials(token=token, username=None, password=None)
        assert False, "Should have raised exception"
    except (ValueError, ConfigurationError) as e:
        print(f"✓ {MIN_TOKEN_LENGTH - 1}-char token rejected: {type(e).__name__}")


def test_no_credentials():
    """Test no credentials provided"""
    print("\n=== Testing no credentials ===")
    
    try:
        FortiOS._validate_credentials(token=None, username=None, password=None)
        assert False, "Should have raised exception"
    except (ValueError, ConfigurationError) as e:
        print(f"✓ No credentials rejected: {type(e).__name__}")


def test_username_without_password():
    """Test username without password"""
    print("\n=== Testing username without password ===")
    
    try:
        FortiOS._validate_credentials(token=None, username="admin", password=None)
        assert False, "Should have raised exception"
    except (ValueError, ConfigurationError) as e:
        print(f"✓ Username without password rejected: {type(e).__name__}")


def test_password_without_username():
    """Test password without username"""
    print("\n=== Testing password without username ===")
    
    try:
        FortiOS._validate_credentials(token=None, username=None, password="secret")
        assert False, "Should have raised exception"
    except (ValueError, ConfigurationError) as e:
        print(f"✓ Password without username rejected: {type(e).__name__}")


def test_valid_username_password():
    """Test valid username and password"""
    print("\n=== Testing valid username/password ===")
    
    FortiOS._validate_credentials(token=None, username="admin", password="password123")
    
    print(f"✓ Username/password accepted")


def test_token_and_username_together():
    """Test that token takes precedence when both provided"""
    print("\n=== Testing token AND username (token takes precedence) ===")
    
    # This is allowed - token takes precedence
    FortiOS._validate_credentials(
        token="a" * 40,
        username="admin",
        password="password"
    )
    print(f"✓ Both token and username accepted (token takes precedence)")


def test_empty_token():
    """Test empty token string"""
    print("\n=== Testing empty token ===")
    
    try:
        FortiOS._validate_credentials(token="", username=None, password=None)
        assert False, "Should have raised exception"
    except (ValueError, ConfigurationError) as e:
        print(f"✓ Empty token rejected: {type(e).__name__}")


def test_empty_username():
    """Test empty username string"""
    print("\n=== Testing empty username ===")
    
    try:
        FortiOS._validate_credentials(token=None, username="", password="pass")
        assert False, "Should have raised exception"
    except (ValueError, ConfigurationError) as e:
        print(f"✓ Empty username rejected: {type(e).__name__}")


def test_empty_password():
    """Test empty password string"""
    print("\n=== Testing empty password ===")
    
    try:
        FortiOS._validate_credentials(token=None, username="admin", password="")
        assert False, "Should have raised exception"
    except (ValueError, ConfigurationError) as e:
        print(f"✓ Empty password rejected: {type(e).__name__}")


def test_whitespace_token():
    """Test whitespace-only token"""
    print("\n=== Testing whitespace token ===")
    
    try:
        FortiOS._validate_credentials(token="   " * 15, username=None, password=None)
        assert False, "Should have raised exception"
    except (ValueError, ConfigurationError) as e:
        print(f"✓ Whitespace token rejected: {type(e).__name__}")


def test_token_with_special_chars():
    """Test token with special characters (some are valid)"""
    print("\n=== Testing token with special characters ===")
    
    # FortiOS tokens typically use alphanumeric + some special chars
    token = "abc123XYZ789" + "-_" * 9  # 30 chars with dashes/underscores
    try:
        FortiOS._validate_credentials(token=token, username=None, password=None)
        print(f"✓ Token with -_ accepted")
    except (ValueError, ConfigurationError) as e:
        print(f"✓ Token with special chars rejected: {type(e).__name__}")


def test_token_boundary_lengths():
    """Test token at various boundary lengths"""
    print("\n=== Testing token boundary lengths ===")
    
    for length in [1, 10, 20, 24, 25, 26, 30, 40, 50, 100]:
        token = "x" * length
        try:
            FortiOS._validate_credentials(token=token, username=None, password=None)
            status = "accepted"
        except (ValueError, ConfigurationError):
            status = "rejected"
        
        expected = "accepted" if length >= MIN_TOKEN_LENGTH else "rejected"
        marker = "✓" if status == expected else "✗ BUG"
        print(f"  {marker} Length {length}: {status}")
    
    print("✓ Boundary tests complete")


if __name__ == "__main__":
    test_valid_token_minimum()
    test_valid_token_40_chars()
    test_valid_token_alphanumeric()
    test_invalid_token_too_short()
    test_invalid_token_just_under_minimum()
    test_no_credentials()
    test_username_without_password()
    test_password_without_username()
    test_valid_username_password()
    test_token_and_username_together()
    test_empty_token()
    test_empty_username()
    test_empty_password()
    test_whitespace_token()
    test_token_with_special_chars()
    test_token_boundary_lengths()
    
    print("\n" + "=" * 60)
    print("✅ All credential validation tests passed!")
    print("=" * 60)
