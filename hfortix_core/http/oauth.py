"""
OAuth 2.0 Authentication for FortiCloud Services

Provides OAuth token acquisition for Fortinet Cloud services including:
- FortiCare Asset Management
- FortiManager Cloud
- FortiAnalyzer Cloud
- FortiGate Cloud
- And other FortiCloud services

Authentication Endpoint:
    https://customerapiauth.fortinet.com/api/v1/oauth/token/
"""

from __future__ import annotations

import logging
from typing import Optional

import httpx

logger = logging.getLogger("hfortix.http.oauth")

__all__ = ["FortiCloudAuth", "get_oauth_token"]


class FortiCloudAuth:
    """
    FortiCloud OAuth 2.0 Authentication Helper.
    
    Handles OAuth token acquisition from FortiCloud authentication API
    for various Fortinet cloud services.
    
    Supported Services:
        - assetmanagement: FortiCare Asset Management
        - FortiManager: FortiManager Cloud
        - FortiAnalyzer: FortiAnalyzer Cloud
        - fortigatecloud: FortiGate Cloud
        - fortipresence: FortiPresence Cloud
        - And more...
    
    Example:
        >>> from hfortix_core.http.oauth import FortiCloudAuth
        >>> 
        >>> auth = FortiCloudAuth(
        ...     api_id="your_api_id",
        ...     password="your_password",
        ...     client_id="assetmanagement"
        ... )
        >>> token = auth.get_token()
        >>> print(f"Token: {token[:20]}...")
    """
    
    DEFAULT_AUTH_URL = "https://customerapiauth.fortinet.com/api/v1/oauth/token/"
    
    def __init__(
        self,
        api_id: str,
        password: str,
        client_id: str = "assetmanagement",
        auth_url: Optional[str] = None,
    ):
        """
        Initialize FortiCloud authentication helper.
        
        Args:
            api_id: FortiCloud API ID (username)
            password: FortiCloud API password
            client_id: Client ID for the service (default: assetmanagement)
            auth_url: Authentication URL (default: FortiCloud OAuth endpoint)
        
        Raises:
            ValueError: If api_id or password is empty
        """
        if not api_id:
            raise ValueError("api_id cannot be empty")
        if not password:
            raise ValueError("password cannot be empty")
        
        self.api_id = api_id
        self.password = password
        self.client_id = client_id
        self.auth_url = auth_url or self.DEFAULT_AUTH_URL
        self._token: Optional[str] = None
        
        logger.debug(
            f"Initialized FortiCloudAuth for client_id={client_id}, "
            f"auth_url={self.auth_url}"
        )
    
    def get_token(self, force_refresh: bool = False) -> str:
        """
        Get OAuth access token.
        
        Requests a new OAuth token from FortiCloud authentication API.
        Caches the token for reuse unless force_refresh is True.
        
        Args:
            force_refresh: Force request new token even if cached (default: False)
        
        Returns:
            OAuth access token string
        
        Raises:
            httpx.HTTPError: If authentication request fails
            KeyError: If response doesn't contain access_token
        
        Example:
            >>> auth = FortiCloudAuth(api_id="...", password="...")
            >>> token = auth.get_token()
        """
        if self._token and not force_refresh:
            logger.debug("Using cached OAuth token")
            return self._token
        
        logger.info(f"Requesting OAuth token for client_id={self.client_id}")
        
        # Prepare request payload
        payload = {
            "username": self.api_id,
            "password": self.password,
            "client_id": self.client_id,
            "grant_type": "password",
        }
        
        try:
            # Request OAuth token
            with httpx.Client() as client:
                response = client.post(
                    self.auth_url,
                    json=payload,
                    headers={"Content-Type": "application/json"},
                    timeout=10.0,
                )
                response.raise_for_status()
            
            # Extract and cache token
            data = response.json()
            self._token = data["access_token"]
            
            logger.info("Successfully obtained OAuth token")
            logger.debug(f"Token: {self._token[:20]}...")
            
            return self._token
            
        except httpx.HTTPStatusError as e:
            logger.error(
                f"OAuth authentication failed: {e.response.status_code} - "
                f"{e.response.text}"
            )
            raise
        except KeyError as e:
            logger.error(f"Invalid OAuth response: missing {e}")
            raise
        except Exception as e:
            logger.error(f"OAuth token request failed: {e}")
            raise
    
    def clear_token(self) -> None:
        """
        Clear cached token.
        
        Use this to force a new token request on the next get_token() call.
        """
        logger.debug("Clearing cached OAuth token")
        self._token = None
    
    def __repr__(self) -> str:
        """String representation."""
        return (
            f"FortiCloudAuth(client_id='{self.client_id}', "
            f"has_token={self._token is not None})"
        )


def get_oauth_token(
    api_id: str,
    password: str,
    client_id: str = "assetmanagement",
    auth_url: Optional[str] = None,
) -> str:
    """
    Convenience function to get OAuth token.
    
    This is a simplified wrapper around FortiCloudAuth for one-time
    token acquisition without needing to manage the auth object.
    
    Args:
        api_id: FortiCloud API ID (username)
        password: FortiCloud API password
        client_id: Client ID for the service (default: assetmanagement)
        auth_url: Authentication URL (default: FortiCloud OAuth endpoint)
    
    Returns:
        OAuth access token string
    
    Raises:
        httpx.HTTPError: If authentication request fails
        KeyError: If response doesn't contain access_token
    
    Example:
        >>> from hfortix_core.http.oauth import get_oauth_token
        >>> 
        >>> token = get_oauth_token(
        ...     api_id="your_api_id",
        ...     password="your_password",
        ...     client_id="assetmanagement"
        ... )
        >>> print(f"Token: {token}")
    """
    auth = FortiCloudAuth(
        api_id=api_id,
        password=password,
        client_id=client_id,
        auth_url=auth_url,
    )
    return auth.get_token()
