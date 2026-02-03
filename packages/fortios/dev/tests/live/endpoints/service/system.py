#!/usr/bin/env python
"""Tests for service/system API endpoints.

Tests system-level service endpoints including fabric synchronization
and administrative status checks.
"""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from fgtclient import fgt


# ============================================================================
# SYSTEM SERVICE TESTS
# ============================================================================

def test_system_fabric_time_in_sync():
    """Test: Check if fabric time is synchronized."""
    result = fgt.api.service.system.fabric_time_in_sync.get()
    assert result.http_status == "success"


def test_system_fabric_admin_lockout_exists_on_firmware_update():
    """Test: Check admin lockout status on firmware update."""
    result = fgt.api.service.system.fabric_admin_lockout_exists_on_firmware_update.get()
    assert result.http_status == "success"


# ============================================================================
# MAIN - Direct execution
# ============================================================================

if __name__ == "__main__":
    print("Testing service/system API endpoints...")
    print("=" * 60)
    print()
    
    test_system_fabric_time_in_sync()
    print("✓ test_system_fabric_time_in_sync passed")
    
    test_system_fabric_admin_lockout_exists_on_firmware_update()
    print("✓ test_system_fabric_admin_lockout_exists_on_firmware_update passed")
    
    print()
    print("=" * 60)
    print("✓ All 2 tests passed!")
    print()
