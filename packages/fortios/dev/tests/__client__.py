import sys
import os
from pathlib import Path

# Add local packages to path FIRST (before pip installed versions)
# This ensures we test against local development code, not installed packages
# Path: packages/fortios/dev/tests/__client__.py
# Go up to workspace root: tests -> dev -> fortios -> packages -> root
repo_root = Path(__file__).parent.parent.parent.parent.parent
sys.path.insert(0, str(repo_root / "packages" / "core" / "src"))
sys.path.insert(0, str(repo_root / "packages" / "fortios" / "src"))


from hfortix_fortios import FortiOS

# Verify we're using local code
import hfortix_fortios
print(f"🔍 Using FortiOS from: {hfortix_fortios.__file__}")

# Load configuration from environment variables
FORTIGATE_HOST = os.getenv("FORTIGATE_HOST", "192.168.1.99")
FORTIGATE_TOKEN = os.getenv("FORTIGATE_TOKEN", "3f8a1c9d2e7b40561938c7f2d0e5b6a1")
FORTIGATE_PORT = int(os.getenv("FORTIGATE_PORT", "443"))
FORTIGATE_VDOM = os.getenv("FORTIGATE_VDOM", "test")

# Disable circuit breaker for testing by setting a very high threshold
# This allows tests to run without being blocked by protective circuit breaker
fgt: FortiOS = FortiOS(
    host=FORTIGATE_HOST, 
    token=FORTIGATE_TOKEN, 
    port=FORTIGATE_PORT, 
    verify=False, 
    error_mode="return", 
    vdom=FORTIGATE_VDOM,  # Use test VDOM for testing (super_admin token has access to all VDOMs)
    circuit_breaker_threshold=99999999,  # Effectively disable circuit breaker for tests
    circuit_breaker_timeout=1  # Short timeout if it does trigger
)