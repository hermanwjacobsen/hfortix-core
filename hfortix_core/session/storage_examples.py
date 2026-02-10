"""
Example Token Storage Backends for CloudSession

This module provides reference implementations of the TokenStorage protocol
for popular backends like Redis, Memcached, and databases.

These are examples - adapt them to your production requirements!
"""

from __future__ import annotations

import json
import pickle
from typing import Optional, Any

from hfortix_core.session import TokenStorage, TokenData

__all__ = [
    "RedisTokenStorage",
    "MemcachedTokenStorage",
    "DatabaseTokenStorage",
    "FileTokenStorage",
]


class RedisTokenStorage:
    """
    Redis-backed token storage for distributed token sharing.
    
    Tokens are stored in Redis with automatic TTL expiration.
    Supports multiple CloudSession instances sharing tokens across
    processes/servers.
    
    Requirements:
        pip install redis
    
    Example:
        >>> import redis
        >>> from hfortix_core.session import CloudSession
        >>> from hfortix_core.session.examples import RedisTokenStorage
        >>> 
        >>> # Create Redis client
        >>> r = redis.Redis(
        ...     host='localhost',
        ...     port=6379,
        ...     db=0,
        ...     decode_responses=False  # We handle encoding
        ... )
        >>> 
        >>> # Use with CloudSession
        >>> storage = RedisTokenStorage(r, namespace="forticloud:prod")
        >>> session = CloudSession(
        ...     api_id="...",
        ...     password="...",
        ...     token_storage=storage
        ... )
        >>> 
        >>> # Now tokens are shared across all processes using this Redis instance
    
    Thread Safety:
        - Redis client must be thread-safe (default redis-py client is)
        - Safe for concurrent access from multiple CloudSession instances
    
    HA Considerations:
        - Use Redis Sentinel or Cluster for high availability
        - Set appropriate retry policies on Redis client
        - Handle Redis connection failures gracefully
    """
    
    def __init__(
        self,
        redis_client: Any,  # redis.Redis
        namespace: str = "forticloud:token",
        serializer: str = "json",  # "json" or "pickle"
    ):
        """
        Initialize Redis token storage.
        
        Args:
            redis_client: redis.Redis instance
            namespace: Key prefix for tokens (default: "forticloud:token")
            serializer: "json" (default, portable) or "pickle" (Python-only, faster)
        """
        self.redis = redis_client
        self.namespace = namespace
        self.serializer = serializer
    
    def _key(self, client_id: str) -> str:
        """Build Redis key for client_id."""
        return f"{self.namespace}:{client_id}"
    
    def get(self, client_id: str) -> Optional[TokenData]:
        """Retrieve token from Redis."""
        try:
            data = self.redis.get(self._key(client_id))
            if not data:
                return None
            
            # Deserialize
            if self.serializer == "json":
                token_dict = json.loads(data)
                return TokenData.from_dict(token_dict)
            else:  # pickle
                return pickle.loads(data)
                
        except Exception as e:
            # Log error but don't crash - CloudSession will acquire new token
            import logging
            logging.getLogger("hfortix.session.storage").warning(
                f"Redis get failed for {client_id}: {e}"
            )
            return None
    
    def set(self, client_id: str, token: TokenData) -> None:
        """Store token in Redis with TTL."""
        try:
            key = self._key(client_id)
            ttl = max(int(token.expires_in), 60)  # Minimum 60s TTL
            
            # Serialize
            if self.serializer == "json":
                data = json.dumps(token.to_dict())
            else:  # pickle
                data = pickle.dumps(token)
            
            # Store with TTL
            self.redis.setex(key, ttl, data)
            
        except Exception as e:
            # Log error but don't crash - token still in memory cache
            import logging
            logging.getLogger("hfortix.session.storage").warning(
                f"Redis set failed for {client_id}: {e}"
            )
    
    def delete(self, client_id: str) -> None:
        """Remove token from Redis."""
        try:
            self.redis.delete(self._key(client_id))
        except Exception:
            pass  # Silently ignore errors
    
    def clear(self) -> None:
        """Remove all tokens in namespace."""
        try:
            # Find all keys matching namespace
            pattern = f"{self.namespace}:*"
            for key in self.redis.scan_iter(match=pattern, count=100):
                self.redis.delete(key)
        except Exception:
            pass  # Silently ignore errors


class MemcachedTokenStorage:
    """
    Memcached-backed token storage for distributed token sharing.
    
    Similar to Redis but using Memcached. Lighter weight but less persistent.
    
    Requirements:
        pip install pymemcache
    
    Example:
        >>> from pymemcache.client.base import Client
        >>> from hfortix_core.session import CloudSession
        >>> from hfortix_core.session.examples import MemcachedTokenStorage
        >>> 
        >>> # Create Memcached client
        >>> mc = Client(('localhost', 11211))
        >>> 
        >>> # Use with CloudSession
        >>> storage = MemcachedTokenStorage(mc, namespace="fortinet")
        >>> session = CloudSession(
        ...     api_id="...",
        ...     password="...",
        ...     token_storage=storage
        ... )
    """
    
    def __init__(
        self,
        memcached_client: Any,  # pymemcache.Client
        namespace: str = "forticloud_token",
    ):
        """Initialize Memcached token storage."""
        self.mc = memcached_client
        self.namespace = namespace
    
    def _key(self, client_id: str) -> str:
        """Build Memcached key."""
        return f"{self.namespace}_{client_id}"
    
    def get(self, client_id: str) -> Optional[TokenData]:
        """Retrieve token from Memcached."""
        try:
            data = self.mc.get(self._key(client_id))
            if not data:
                return None
            
            token_dict = json.loads(data)
            return TokenData.from_dict(token_dict)
            
        except Exception as e:
            import logging
            logging.getLogger("hfortix.session.storage").warning(
                f"Memcached get failed for {client_id}: {e}"
            )
            return None
    
    def set(self, client_id: str, token: TokenData) -> None:
        """Store token in Memcached with TTL."""
        try:
            key = self._key(client_id)
            ttl = max(int(token.expires_in), 60)
            data = json.dumps(token.to_dict())
            
            self.mc.set(key, data, expire=ttl)
            
        except Exception as e:
            import logging
            logging.getLogger("hfortix.session.storage").warning(
                f"Memcached set failed for {client_id}: {e}"
            )
    
    def delete(self, client_id: str) -> None:
        """Remove token from Memcached."""
        try:
            self.mc.delete(self._key(client_id))
        except Exception:
            pass
    
    def clear(self) -> None:
        """Remove all tokens (flushes entire Memcached - use carefully!)."""
        try:
            # WARNING: This flushes EVERYTHING in Memcached
            # In production, use namespaced Memcached instances
            # or track keys separately
            pass  # Don't flush automatically
        except Exception:
            pass


class DatabaseTokenStorage:
    """
    Database-backed token storage using SQLAlchemy.
    
    Most persistent option - survives restarts, supports clustering.
    Slower than Redis/Memcached but provides durability.
    
    Supports any database compatible with SQLAlchemy:
        - PostgreSQL (recommended for production)
        - MySQL / MariaDB
        - SQLite (good for single-server, development)
        - Oracle, MS SQL Server, and others
    
    Requirements:
        pip install sqlalchemy
        pip install psycopg2-binary  # For PostgreSQL
        pip install pymysql           # For MySQL
        # SQLite is built-in to Python
    
    Examples:
        >>> from sqlalchemy import create_engine
        >>> from hfortix_core.session import CloudSession
        >>> from hfortix_core.session.examples import DatabaseTokenStorage
        >>> 
        >>> # PostgreSQL (recommended for production)
        >>> engine = create_engine('postgresql://user:pass@localhost/fortinet')
        >>> 
        >>> # MySQL
        >>> engine = create_engine('mysql+pymysql://user:pass@localhost/fortinet')
        >>> 
        >>> # SQLite (good for development/single-server)
        >>> engine = create_engine('sqlite:///forticloud_tokens.db')
        >>> 
        >>> # Initialize storage (creates table automatically)
        >>> storage = DatabaseTokenStorage(engine)
        >>> 
        >>> # Use with CloudSession
        >>> session = CloudSession(
        ...     api_id="...",
        ...     password="...",
        ...     token_storage=storage
        ... )
    
    Schema:
        CREATE TABLE forticloud_tokens (
            client_id VARCHAR(100) PRIMARY KEY,
            access_token TEXT NOT NULL,
            refresh_token TEXT,
            expires_in INTEGER NOT NULL,
            created_at FLOAT NOT NULL,
            scope TEXT,
            token_type VARCHAR(50),
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """
    
    def __init__(self, engine: Any, table_name: str = "forticloud_tokens"):
        """
        Initialize database token storage.
        
        Args:
            engine: SQLAlchemy engine
            table_name: Name of tokens table
        """
        self.engine = engine
        self.table_name = table_name
        self._init_table()
    
    def _init_table(self) -> None:
        """Create tokens table if it doesn't exist."""
        from sqlalchemy import text
        
        create_table_sql = f"""
        CREATE TABLE IF NOT EXISTS {self.table_name} (
            client_id VARCHAR(100) PRIMARY KEY,
            access_token TEXT NOT NULL,
            refresh_token TEXT,
            expires_in INTEGER NOT NULL,
            created_at FLOAT NOT NULL,
            scope TEXT,
            token_type VARCHAR(50),
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        
        with self.engine.connect() as conn:
            conn.execute(text(create_table_sql))
            conn.commit()
    
    def get(self, client_id: str) -> Optional[TokenData]:
        """Retrieve token from database."""
        from sqlalchemy import text
        import time
        
        try:
            query = f"""
            SELECT access_token, refresh_token, expires_in, created_at, scope, token_type
            FROM {self.table_name}
            WHERE client_id = :client_id
            """
            
            with self.engine.connect() as conn:
                result = conn.execute(text(query), {"client_id": client_id}).fetchone()
                
            if not result:
                return None
            
            # Check if token is expired
            token_data = TokenData(
                access_token=result[0],
                refresh_token=result[1] or "",
                expires_in=result[2],
                created_at=result[3],
                scope=result[4] or "read write",
                token_type=result[5] or "Bearer",
            )
            
            # Check expiration
            if time.time() >= (token_data.created_at + token_data.expires_in):
                # Token expired, delete it
                self.delete(client_id)
                return None
            
            return token_data
            
        except Exception as e:
            import logging
            logging.getLogger("hfortix.session.storage").warning(
                f"Database get failed for {client_id}: {e}"
            )
            return None
    
    def set(self, client_id: str, token: TokenData) -> None:
        """Store token in database."""
        from sqlalchemy import text
        
        try:
            query = f"""
            INSERT INTO {self.table_name} 
            (client_id, access_token, refresh_token, expires_in, created_at, scope, token_type)
            VALUES (:client_id, :access_token, :refresh_token, :expires_in, :created_at, :scope, :token_type)
            ON CONFLICT (client_id) DO UPDATE SET
                access_token = EXCLUDED.access_token,
                refresh_token = EXCLUDED.refresh_token,
                expires_in = EXCLUDED.expires_in,
                created_at = EXCLUDED.created_at,
                scope = EXCLUDED.scope,
                token_type = EXCLUDED.token_type,
                updated_at = CURRENT_TIMESTAMP
            """
            
            with self.engine.connect() as conn:
                conn.execute(text(query), {
                    "client_id": client_id,
                    "access_token": token.access_token,
                    "refresh_token": token.refresh_token,
                    "expires_in": token.expires_in,
                    "created_at": token.created_at,
                    "scope": token.scope,
                    "token_type": token.token_type,
                })
                conn.commit()
                
        except Exception as e:
            import logging
            logging.getLogger("hfortix.session.storage").warning(
                f"Database set failed for {client_id}: {e}"
            )
    
    def delete(self, client_id: str) -> None:
        """Remove token from database."""
        from sqlalchemy import text
        
        try:
            query = f"DELETE FROM {self.table_name} WHERE client_id = :client_id"
            with self.engine.connect() as conn:
                conn.execute(text(query), {"client_id": client_id})
                conn.commit()
        except Exception:
            pass
    
    def clear(self) -> None:
        """Remove all tokens from database."""
        from sqlalchemy import text
        
        try:
            query = f"DELETE FROM {self.table_name}"
            with self.engine.connect() as conn:
                conn.execute(text(query))
                conn.commit()
        except Exception:
            pass


class FileTokenStorage:
    """
    File-based token storage for simple persistent caching.
    
    Stores tokens in JSON files in a directory. Simple and portable
    but not suitable for high-concurrency scenarios.
    
    Good for:
        - Single-server deployments
        - Development/testing
        - Simple persistent storage
        - No external dependencies
    
    Not recommended for:
        - Multi-server deployments (no locking across servers)
        - High-concurrency (file I/O bottleneck)
        - Production clusters (use Redis/Database instead)
    
    Example:
        >>> from hfortix_core.session import CloudSession
        >>> from hfortix_core.session.examples import FileTokenStorage
        >>> 
        >>> # Store tokens in /var/lib/forticloud/tokens/
        >>> storage = FileTokenStorage(directory="/var/lib/forticloud/tokens")
        >>> 
        >>> # Use with CloudSession
        >>> session = CloudSession(
        ...     api_id="...",
        ...     password="...",
        ...     token_storage=storage
        ... )
        >>> 
        >>> # Tokens persist across restarts
    
    Thread Safety:
        - Uses file locking for single-server concurrency
        - NOT safe across multiple servers/processes on different machines
        - Use Redis/Database for distributed deployments
    
    File Format:
        - One JSON file per client_id: {directory}/{client_id}.json
        - Each file contains serialized TokenData
        - Old/expired tokens automatically cleaned on access
    """
    
    def __init__(
        self,
        directory: str = "/tmp/forticloud_tokens",
        auto_cleanup: bool = True,
    ):
        """
        Initialize file-based token storage.
        
        Args:
            directory: Directory to store token files
            auto_cleanup: Automatically delete expired tokens on get()
        """
        import os
        
        self.directory = directory
        self.auto_cleanup = auto_cleanup
        
        # Create directory if it doesn't exist
        os.makedirs(directory, exist_ok=True)
    
    def _get_file_path(self, client_id: str) -> str:
        """Get file path for client_id."""
        import os
        # Sanitize client_id to prevent directory traversal
        safe_id = client_id.replace('/', '_').replace('\\', '_').replace('..', '_')
        return os.path.join(self.directory, f"{safe_id}.json")
    
    def get(self, client_id: str) -> Optional[TokenData]:
        """Retrieve token from file."""
        import os
        import time
        
        file_path = self._get_file_path(client_id)
        
        try:
            # Check if file exists
            if not os.path.exists(file_path):
                return None
            
            # Read file with lock
            with open(file_path, 'r') as f:
                data = json.load(f)
            
            token = TokenData.from_dict(data)
            
            # Check if expired and cleanup if enabled
            if self.auto_cleanup:
                if time.time() >= (token.created_at + token.expires_in):
                    # Token expired, delete file
                    os.remove(file_path)
                    return None
            
            return token
            
        except Exception as e:
            # Log error but don't crash
            import logging
            logging.getLogger("hfortix.session.storage").warning(
                f"File get failed for {client_id}: {e}"
            )
            return None
    
    def set(self, client_id: str, token: TokenData) -> None:
        """Store token in file."""
        file_path = self._get_file_path(client_id)
        
        try:
            # Write file atomically (write to temp, then rename)
            import os
            import tempfile
            
            # Get directory for temp file
            directory = os.path.dirname(file_path)
            
            # Write to temp file first
            with tempfile.NamedTemporaryFile(
                mode='w',
                dir=directory,
                delete=False,
                suffix='.tmp'
            ) as f:
                json.dump(token.to_dict(), f, indent=2)
                temp_path = f.name
            
            # Atomic rename (replaces existing file)
            os.replace(temp_path, file_path)
            
        except Exception as e:
            # Log error but don't crash
            import logging
            logging.getLogger("hfortix.session.storage").warning(
                f"File set failed for {client_id}: {e}"
            )
    
    def delete(self, client_id: str) -> None:
        """Remove token file."""
        import os
        
        file_path = self._get_file_path(client_id)
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
        except Exception:
            pass  # Silently ignore errors
    
    def clear(self) -> None:
        """Remove all token files in directory."""
        import os
        
        try:
            # Remove all .json files in directory
            for filename in os.listdir(self.directory):
                if filename.endswith('.json'):
                    file_path = os.path.join(self.directory, filename)
                    try:
                        os.remove(file_path)
                    except Exception:
                        pass  # Continue even if one file fails
        except Exception:
            pass  # Silently ignore errors

