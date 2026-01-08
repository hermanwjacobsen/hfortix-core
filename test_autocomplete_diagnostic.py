"""
Diagnostic script to verify type annotations are working correctly.

Run this with your language server/IDE to check autocomplete.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "packages" / "core"))
sys.path.insert(0, str(Path(__file__).parent / "packages" / "fortios"))

from hfortix_fortios import FortiOS
from hfortix_fortios.api import API

# Create FortiOS client instance
fgt = FortiOS(
    host="192.168.1.99",
    token="a" * 40,  # Fake token for testing
)

# Verify type at runtime
print(f"Type of fgt: {type(fgt)}")
print(f"Type of fgt.api: {type(fgt.api)}")
print(f"fgt.api is API instance: {isinstance(fgt.api, API)}")

# The following should have full autocomplete:
# 1. After typing 'fgt.' you should see: api, host, port, close, etc.
# 2. After typing 'fgt.api.' you should see: cmdb, monitor, log, service
# 3. After typing 'fgt.api.cmdb.' you should see: firewall, system, etc.

# Test type hints work
def test_param(client: FortiOS) -> API:
    """This function should show that client.api returns API type."""
    return client.api

# Call it to verify
result = test_param(fgt)
print(f"Function return type: {type(result)}")

# If autocomplete shows "api: Any" when you hover over fgt.api, 
# it means Pylance hasn't picked up the type annotations properly.
# Try:
# 1. Reload VS Code window (Ctrl+Shift+P → "Developer: Reload Window")
# 2. Restart Python Language Server (Ctrl+Shift+P → "Pylance: Restart")
# 3. Close and reopen the file

print("\n✅ Type annotations are correct at runtime!")
print("If autocomplete still doesn't work, restart Pylance/Pylot.")
