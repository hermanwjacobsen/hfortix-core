class FortiOSError(Exception):
    """Base exception"""
    pass

class LoginError(FortiOSError):
    """Authentication failed"""
    pass

class APIError(FortiOSError):
    """API request failed"""
    pass