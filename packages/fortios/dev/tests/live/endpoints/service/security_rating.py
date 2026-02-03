#!/usr/bin/env python
"""Tests for service/security-rating API endpoints.

Tests the Security Rating report endpoint which provides security posture
assessment including PSIRT advisories and configuration insights.
"""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from fgtclient import fgt


# ============================================================================
# SECURITY RATING REPORT TESTS
# ============================================================================

def test_security_rating_report_global_psirt():
    """Test: Get global PSIRT security rating report."""
    result = fgt.api.service.security_rating.report.get(scope="global", type="psirt")
    assert result.http_status == "success"
    assert "results" in result.raw


def test_security_rating_report_global_insight():
    """Test: Get global insight security rating report."""
    result = fgt.api.service.security_rating.report.get(scope="global", type="insight")
    assert result.http_status == "success"
    assert "results" in result.raw


def test_security_rating_report_vdom_psirt():
    """Test: Get VDOM PSIRT security rating report."""
    result = fgt.api.service.security_rating.report.get(scope="vdom", type="psirt")
    assert result.http_status == "success"
    assert "results" in result.raw


def test_security_rating_report_vdom_insight():
    """Test: Get VDOM insight security rating report."""
    result = fgt.api.service.security_rating.report.get(scope="vdom", type="insight")
    assert result.http_status == "success"
    assert "results" in result.raw


# ============================================================================
# MAIN - Direct execution
# ============================================================================

if __name__ == "__main__":
    print("Testing service/security-rating API endpoints...")
    print("=" * 60)
    print()
    
    test_security_rating_report_global_psirt()
    print("✓ test_security_rating_report_global_psirt passed")
    
    test_security_rating_report_global_insight()
    print("✓ test_security_rating_report_global_insight passed")
    
    test_security_rating_report_vdom_psirt()
    print("✓ test_security_rating_report_vdom_psirt passed")
    
    test_security_rating_report_vdom_insight()
    print("✓ test_security_rating_report_vdom_insight passed")
    
    print()
    print("=" * 60)
    print("✓ All 4 tests passed!")
    print()
    print("Note: The /recommendations endpoint requires Security Fabric")
    print("      configuration and returns 424 on standalone FortiGates.")
