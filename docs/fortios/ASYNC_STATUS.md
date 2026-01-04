# Async Support Status

## ✅ Already Fully Implemented

Async support is **already complete** in the HFortix SDK. No additional code generation is needed.

### How It Works

1. **Core HTTP Clients**:
   - `HTTPClient`: Synchronous implementation using `httpx.Client`
   - `AsyncHTTPClient`: Asynchronous implementation using `httpx.AsyncClient`

2. **IHTTPClient Protocol**:
   ```python
   def get(self, ...) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
   ```
   - All methods return `Union[dict, Coroutine]`
   - Supports both sync and async modes transparently

3. **Generated Endpoints**:
   - All generated endpoint methods already return `Union[dict, Coroutine]`
   - No special async methods needed
   - Same codebase works for both sync and async

### Usage Examples

#### Synchronous Mode
```python
from hfortix_fortios import FortiOS

# Creates sync HTTPClient internally
fgt = FortiOS(host="192.168.1.99", token="your-token")

# All methods return dict immediately
addresses = fgt.api.cmdb.firewall.address.get()
print(f"Found {len(addresses)} addresses")
```

#### Asynchronous Mode
```python
import asyncio
from hfortix_fortios import FortiOS

async def main():
    # Create async client
    async with FortiOS(
        host="192.168.1.99",
        token="your-token",
        async_mode=True  # Uses AsyncHTTPClient
    ) as fgt:
        # All methods return Coroutine - must await
        addresses = await fgt.api.cmdb.firewall.address.get()
        print(f"Found {len(addresses)} addresses")
        
        # Concurrent requests
        results = await asyncio.gather(
            fgt.api.cmdb.firewall.address.get(),
            fgt.api.cmdb.firewall.policy.get(),
            fgt.api.cmdb.system.interface.get(),
        )

asyncio.run(main())
```

### Benefits

1. **Single Codebase**: Same generated code works for both sync and async
2. **Type Safety**: Return type is `Union[dict, Coroutine]` - type checkers understand both modes
3. **No Duplication**: Don't need separate `get()` and `get_async()` methods
4. **Protocol-Based**: Users can provide custom async HTTP client implementations

### Implementation Details

**Core Module** (`hfortix_core/http/`):
- `interface.py`: Defines `IHTTPClient` protocol
- `client.py`: Synchronous `HTTPClient` implementation
- `async_client.py`: Asynchronous `AsyncHTTPClient` implementation
- `base.py`: Shared base class for both implementations

**Generated Endpoints**:
```python
class Address:
    def __init__(self, client: "IHTTPClient"):
        self._client = client
    
    def get(self, ...
) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        return self._client.get("cmdb", "/firewall/address", ...)
```

The method signature automatically supports both modes because:
- If `client` is `HTTPClient`, returns `dict` immediately
- If `client` is `AsyncHTTPClient`, returns `Coroutine` to await

### Verification

Check any generated endpoint file:
```bash
grep -A2 "def get" packages/fortios/hfortix_fortios/api/v2/cmdb/firewall/address.py
```

You'll see:
```python
def get(
    self, ...
) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
```

## Conclusion

✅ **No action needed** - async support is fully implemented via the `IHTTPClient` protocol pattern.

The design is elegant:
- Single codebase for both modes
- No code duplication
- Type-safe
- Extensible (users can provide custom async clients)

This is **better** than generating separate async methods because:
1. Less code to maintain
2. No sync/async drift
3. Cleaner API surface
4. More flexible (protocol-based)
