"""
Auto-generated tests for LOG disk endpoint.

These are basic smoke tests to verify:
  1. Endpoint class can be imported
  2. Methods exist and are callable
  3. Basic structure is correct

Note: These tests do NOT make actual API calls.
      They only verify the generated code structure.
"""

import pytest
from unittest.mock import Mock, MagicMock

from packages.fortios.hfortix_fortios.api.v2.log.disk import Disk


class TestDiskStructure:
    """Test disk endpoint structure."""

    @pytest.fixture
    def mock_client(self):
        """Create a mock HTTP client."""
        client = Mock()
        client.get = MagicMock(return_value={"status": "success"})
        client.post = MagicMock(return_value={"status": "success"})
        return client

    @pytest.fixture
    def disk_endpoint(self, mock_client):
        """Create disk endpoint instance."""
        return Disk(mock_client)

    def test_import_disk(self):
        """Test that disk class can be imported."""
        from packages.fortios.hfortix_fortios.api.v2.log.disk import Disk
        assert Disk is not None

    def test_disk_has_get_method(self, disk_endpoint):
        """Test that endpoint has get() method."""
        assert hasattr(disk_endpoint, "get")
        assert callable(getattr(disk_endpoint, "get"))

    def test_disk_structure(self, disk_endpoint, mock_client):
        """Test endpoint structure and method calls."""
        # Call get() - should not raise
        result = disk_endpoint.get()
        
        # Verify mock was called
        assert mock_client.get.called or mock_client.post.called
