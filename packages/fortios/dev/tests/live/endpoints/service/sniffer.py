#!/usr/bin/env python
"""Tests for service/sniffer API endpoints.

Note: These tests must run serially (not in parallel) because they all
use the same sniffer resource on the FortiGate.
"""

import sys
import time
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from fgtclient import fgt


VDOM = "test"
SNIFFER_NAME = "sniffer1"

# Mark all tests in this module to run in the same worker (serially)
pytestmark = pytest.mark.xdist_group(mkey="sniffer")


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_sniffer_status(name: str) -> str | None:
    """Get the status of a specific sniffer by name.
    
    Returns: 'running', 'finished', 'stopped', or None if not found.
    """
    sniffer_list = fgt.api.service.sniffer.list.get()
    results = sniffer_list.raw.get('results', [])
    for sniffer in results:
        if sniffer.get('mkey') == name:
            return sniffer.get('status')
    return None


def ensure_sniffer_stopped(name: str, vdom: str = VDOM):
    """Ensure a sniffer is stopped before proceeding."""
    status = get_sniffer_status(name)
    if status == 'running':
        fgt.api.service.sniffer.stop.post(vdom=vdom, mkey=name)
        time.sleep(1)


def cleanup_sniffer(name: str, vdom: str = VDOM):
    """Stop and delete a sniffer capture data if it exists.
    
    Note: The sniffer configuration always exists - this deletes the capture data.
    """
    status = get_sniffer_status(name)
    
    # Stop if running
    if status == 'running':
        try:
            fgt.api.service.sniffer.stop.post(vdom=vdom, mkey=name)
            time.sleep(1)
            status = get_sniffer_status(name)  # Re-check after stop
        except Exception:
            pass
    
    # Only delete if finished (has capture data)
    if status == 'finished':
        try:
            fgt.api.service.sniffer.delete.post(vdom=vdom, mkey=name)
        except Exception:
            pass


# ============================================================================
# FIXTURES
# ============================================================================

@pytest.fixture
def clean_sniffer():
    """Fixture to ensure sniffer is cleaned up before and after test."""
    cleanup_sniffer(SNIFFER_NAME)
    yield
    cleanup_sniffer(SNIFFER_NAME)


# ============================================================================
# TESTS
# ============================================================================

def test_sniffer_list():
    """Test: List all active sniffers."""
    result = fgt.api.service.sniffer.list.get()
    assert result.http_status == "success"
    assert 'results' in result.raw


def test_sniffer_start(clean_sniffer):
    """Test: Start a packet capture."""
    result = fgt.api.service.sniffer.start.post(vdom=VDOM, mkey=SNIFFER_NAME)
    assert result.http_status == "success"
    assert result.raw.get('results', {}).get('status') == 'success'
    
    # Verify it's running
    status = get_sniffer_status(SNIFFER_NAME)
    assert status == 'running'


def test_sniffer_stop(clean_sniffer):
    """Test: Stop a packet capture."""
    # Start first
    fgt.api.service.sniffer.start.post(vdom=VDOM, mkey=SNIFFER_NAME)
    time.sleep(1)
    
    # Now stop
    result = fgt.api.service.sniffer.stop.post(vdom=VDOM, mkey=SNIFFER_NAME)
    assert result.http_status == "success"
    
    # Verify it's stopped/finished
    time.sleep(1)
    status = get_sniffer_status(SNIFFER_NAME)
    assert status in ('stopped', 'finished', None)


def test_sniffer_delete(clean_sniffer):
    """Test: Delete a packet capture."""
    # Start and stop first to create a capture
    fgt.api.service.sniffer.start.post(vdom=VDOM, mkey=SNIFFER_NAME)
    time.sleep(2)
    fgt.api.service.sniffer.stop.post(vdom=VDOM, mkey=SNIFFER_NAME)
    time.sleep(1)
    
    # Now delete
    result = fgt.api.service.sniffer.delete.post(vdom=VDOM, mkey=SNIFFER_NAME)
    assert result.http_status == "success"


def test_sniffer_download(clean_sniffer):
    """Test: Download a packet capture file."""
    # Start capture
    fgt.api.service.sniffer.start.post(vdom=VDOM, mkey=SNIFFER_NAME)
    time.sleep(3)  # Capture some packets
    
    # Stop capture
    fgt.api.service.sniffer.stop.post(vdom=VDOM, mkey=SNIFFER_NAME)
    time.sleep(1)
    
    # Download
    result = fgt.api.service.sniffer.download.post(vdom=VDOM, mkey=SNIFFER_NAME)
    assert result.http_status == "success"
    assert 'content' in result.raw
    assert result.raw.get('content_type') == 'application/vnd.tcpdump.pcap'
    
    # Verify pcap magic header (0xd4c3b2a1 or 0xa1b2c3d4)
    content = result.raw.get('content', b'')
    assert len(content) > 0
    pcap_magic = content[:4]
    assert pcap_magic in (b'\xd4\xc3\xb2\xa1', b'\xa1\xb2\xc3\xd4')


def test_sniffer_full_workflow(clean_sniffer):
    """Test: Complete sniffer workflow - list, start, stop, download, delete."""
    # 1. List (verify clean state)
    list_result = fgt.api.service.sniffer.list.get()
    assert list_result.http_status == "success"
    
    # 2. Start
    start_result = fgt.api.service.sniffer.start.post(vdom=VDOM, mkey=SNIFFER_NAME)
    assert start_result.http_status == "success"
    
    # 3. Verify running
    time.sleep(1)
    assert get_sniffer_status(SNIFFER_NAME) == 'running'
    
    # 4. Capture packets
    time.sleep(3)
    
    # 5. Stop
    stop_result = fgt.api.service.sniffer.stop.post(vdom=VDOM, mkey=SNIFFER_NAME)
    assert stop_result.http_status == "success"
    time.sleep(1)
    
    # 6. Download
    download_result = fgt.api.service.sniffer.download.post(vdom=VDOM, mkey=SNIFFER_NAME)
    assert download_result.http_status == "success"
    assert download_result.raw.get('content_type') == 'application/vnd.tcpdump.pcap'
    
    # 7. Delete
    delete_result = fgt.api.service.sniffer.delete.post(vdom=VDOM, mkey=SNIFFER_NAME)
    assert delete_result.http_status == "success"


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    # Pre-cleanup
    cleanup_sniffer(SNIFFER_NAME)
    print("Testing service/sniffer API endpoints...")
    print("=" * 60)

    
    test_sniffer_list()
    print("✓ test_sniffer_list passed")
    
    cleanup_sniffer(SNIFFER_NAME)
    test_sniffer_start(None)
    print("✓ test_sniffer_start passed")
    
    cleanup_sniffer(SNIFFER_NAME)
    test_sniffer_stop(None)
    print("✓ test_sniffer_stop passed")
    
    cleanup_sniffer(SNIFFER_NAME)
    test_sniffer_delete(None)
    print("✓ test_sniffer_delete passed")
    
    cleanup_sniffer(SNIFFER_NAME)
    test_sniffer_download(None)
    print("✓ test_sniffer_download passed")
    
    cleanup_sniffer(SNIFFER_NAME)
    test_sniffer_full_workflow(None)
    print("✓ test_sniffer_full_workflow passed")
    
    # Final cleanup
    cleanup_sniffer(SNIFFER_NAME)
    
    print("\n" + "=" * 60)
    print("✓ All 6 tests passed!")