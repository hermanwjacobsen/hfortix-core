# SSH and SSL Proxy Wrappers Guide

**Version:** 0.4.2+  
**Status:** Production Ready (with API limitations)

Comprehensive SSH and SSL/TLS proxy wrappers for FortiOS traffic inspection, providing secure SSH certificate management and SSL/TLS cipher configuration.

## Table of Contents

- [Overview](#overview)
- [SSH Proxy Wrappers](#ssh-proxy-wrappers)
  - [SSH Host Key](#ssh-host-key)
  - [SSH Local CA](#ssh-local-ca)
  - [SSH Local Key](#ssh-local-key)
  - [SSH Settings](#ssh-settings)
- [SSL Proxy Wrappers](#ssl-proxy-wrappers)
  - [SSL Settings](#ssl-settings)
- [FortiOS API Limitations](#fortios-api-limitations)
- [Common Patterns](#common-patterns)
- [Complete Examples](#complete-examples)
- [Related Documentation](#related-documentation)

---

## Overview

SSH and SSL proxy wrappers enable secure traffic inspection and proxying capabilities:

- **SSH Proxy**: Inspect and control SSH traffic, manage certificates and keys
- **SSL Proxy**: Configure SSL/TLS inspection settings and cipher suites

### Important: FortiOS API Limitations

⚠️ **Not all SSH/SSL proxy operations are supported via the FortiOS REST API.** See [FortiOS API Limitations](#fortios-api-limitations) below for detailed restrictions.

**Key Restrictions:**
- SSH Host-Keys and Local-Keys: **Read-only** (cannot create/update/delete via API)
- SSH Local-CAs: **Cannot delete or update** via API (FortiOS security restriction)
- SSL Settings: **Fully supported** for read and update operations

---

## SSH Proxy Wrappers

All SSH proxy wrappers are accessible via `fgt.firewall.ssh_*`:

| Wrapper | Access Path | Primary Use | API Support |
|---------|-------------|-------------|-------------|
| **SSH Host Key** | `fgt.firewall.ssh_host_key` | Manage discovered SSH server keys | ⚠️ Read-only |
| **SSH Local CA** | `fgt.firewall.ssh_local_ca` | Configure SSH certificate authorities | ⚠️ Create + Read only |
| **SSH Local Key** | `fgt.firewall.ssh_local_key` | Manage SSH proxy keys | ⚠️ Read-only |
| **SSH Settings** | `fgt.firewall.ssh_setting` | Global SSH proxy configuration | ✅ Full support |

### SSH Host Key

**Purpose:** Manage SSH host keys discovered during traffic inspection.

**API Limitations:** ⚠️ **Read-only** - Cannot create, update, or delete via API.

```python
from hfortix import FortiOS

fgt = FortiOS(host="fortigate.example.com", token="your_token", verify=False)

# ✅ GET - List all discovered SSH host keys
result = fgt.firewall.ssh_host_key.get()
for key in result:
    print(f"Host: {key['hostname']}, Type: {key['type']}")

# ✅ GET - Get specific host key
result = fgt.firewall.ssh_host_key.get(name="server1.example.com")
print(f"Key: {result['public-key']}")

# ✅ CHECK - Check if host key exists
exists = fgt.firewall.ssh_host_key.exists(name="server1.example.com")

# ❌ CREATE/UPDATE/DELETE - Not supported by FortiOS API
# These operations will fail with error -651 or -3
```

**Why Read-only?** SSH host keys are automatically discovered when FortiGate inspects SSH traffic. They cannot be manually created via the API.

---

### SSH Local CA

**Purpose:** Manage SSH certificate authorities for signing SSH certificates used in proxy operations.

**API Limitations:** ⚠️ **Can create and read, but CANNOT update or delete via API** (FortiOS security restriction).

```python
# ✅ CREATE - Create new SSH Local CA
result = fgt.firewall.ssh_local_ca.create(
    name="company-ssh-ca",
    password="SecureP@ssw0rd123",
    source_type="built-in",
    source="CA_RSA2K"
)

# ✅ GET - List all SSH Local CAs
result = fgt.firewall.ssh_local_ca.get()
for ca in result:
    print(f"CA: {ca['name']}, Source: {ca['source']}")

# ✅ GET - Get specific CA
result = fgt.firewall.ssh_local_ca.get(name="company-ssh-ca")

# ✅ CHECK - Check if CA exists
exists = fgt.firewall.ssh_local_ca.exists(name="company-ssh-ca")

# ❌ UPDATE - Not supported (Error -14: Permission denied)
# Cannot modify existing CAs via API

# ❌ DELETE - Not supported (Error -14: Permission denied)
# Cannot delete CAs via API even with super_admin privileges
```

**Why No Delete/Update?** This is a **FortiOS security restriction** to prevent accidental CA deletion that could impact:
- Active SSH proxy policies
- Certificate-based SSH authentication
- Production SSH inspection configurations

**Workaround for Deletion:**
```bash
# Use FortiGate CLI
config firewall ssh local-ca
    delete company-ssh-ca
end

# Or use FortiGate Web GUI:
# Security Fabric > Certificates > SSH Local CA > Delete
```

**Available Built-in CA Sources:**
- `CA_RSA2K` - RSA 2048-bit
- `CA_RSA4K` - RSA 4096-bit
- `CA_ECDSA256` - ECDSA P-256
- `CA_ECDSA384` - ECDSA P-384
- `CA_ECDSA521` - ECDSA P-521
- `CA_ED25519` - ED25519

---

### SSH Local Key

**Purpose:** Manage SSH keys used by FortiGate for SSH proxying.

**API Limitations:** ⚠️ **Read-only** - Cannot create, update, or delete via API.

```python
# ✅ GET - List all SSH local keys
result = fgt.firewall.ssh_local_key.get()
for key in result:
    print(f"Key: {key['name']}, Source: {key.get('source', 'N/A')}")

# ✅ GET - Get specific key
result = fgt.firewall.ssh_local_key.get(name="RSA2K")

# ✅ CHECK - Check if key exists
exists = fgt.firewall.ssh_local_key.exists(name="RSA2K")

# ❌ CREATE/UPDATE/DELETE - Not supported by FortiOS API
# These operations will fail with error -651
```

**Why Read-only?** SSH local keys are typically pre-configured or generated via CLI. The API does not support key creation due to security and format requirements.

**Available Built-in Keys** (typically present on FortiOS):
- `RSA2K` - RSA 2048-bit
- `RSA4K` - RSA 4096-bit
- `ECDSA256` - ECDSA P-256
- `ECDSA384` - ECDSA P-384
- `ECDSA521` - ECDSA P-521
- `ED25519` - ED25519

---

### SSH Settings

**Purpose:** Configure global SSH proxy behavior and certificate validation.

**API Support:** ✅ **Fully supported** - Read and update operations work.

```python
# ✅ GET - Retrieve current SSH settings
result = fgt.firewall.ssh_setting.get()
print(f"Host Trust Check: {result.get('host-trusted-checking', 'N/A')}")
print(f"CA Certificate: {result.get('caname', 'N/A')}")

# ✅ UPDATE - Enable host trust checking with specific CA
result = fgt.firewall.ssh_setting.update(
    host_trusted_checking="enable",
    caname="company-ssh-ca"
)

# ✅ UPDATE - Disable host trust checking
result = fgt.firewall.ssh_setting.update(
    host_trusted_checking="disable"
)

# ✅ UPDATE - Configure multiple settings
result = fgt.firewall.ssh_setting.update(
    host_trusted_checking="enable",
    caname="company-ssh-ca",
    untrusted_caname="backup-ca"
)
```

**Common Settings:**
- `host_trusted_checking`: Enable/disable SSH host verification (`"enable"` or `"disable"`)
- `caname`: Primary SSH CA for trusted certificates
- `untrusted_caname`: CA for untrusted/unverified connections
- `host_key_type`: Preferred host key types (e.g., `["RSA", "ECDSA", "ED25519"]`)

---

## SSL Proxy Wrappers

### SSL Settings

**Purpose:** Configure global SSL/TLS proxy settings, cipher suites, and performance parameters.

**API Support:** ✅ **Fully supported** - Read and update operations work.

```python
from hfortix import FortiOS

fgt = FortiOS(host="fortigate.example.com", token="your_token", verify=False)

# ✅ GET - Retrieve current SSL settings
result = fgt.firewall.ssl_setting.get()
print(f"Proxy Timeout: {result.get('proxy-connect-timeout', 'N/A')}s")
print(f"SSL DH Bits: {result.get('ssl-dh-bits', 'N/A')}")

# ✅ UPDATE - Configure connection timeout
result = fgt.firewall.ssl_setting.update(
    proxy_connect_timeout=30  # seconds
)

# ✅ UPDATE - Configure Diffie-Hellman key size
result = fgt.firewall.ssl_setting.update(
    ssl_dh_bits="2048"  # Options: "768", "1024", "1536", "2048"
)

# ✅ UPDATE - Configure certificate caching
result = fgt.firewall.ssl_setting.update(
    cert_cache_capacity=300,      # Max cached certificates
    cert_cache_timeout=10,        # Cache timeout in minutes
    session_cache_capacity=500,   # SSL session cache size
    session_cache_timeout=20      # Session cache timeout in minutes
)

# ✅ UPDATE - Performance tuning
result = fgt.firewall.ssl_setting.update(
    ssl_queue_threshold=64,       # SSL processor queue threshold
    kxp_queue_threshold=32,       # Key exchange processor threshold
    abbreviate_handshake="enable" # Enable abbreviated handshakes
)

# ✅ UPDATE - Cipher configuration
result = fgt.firewall.ssl_setting.update(
    no_matching_cipher_action="bypass",  # or "drop"
    ssl_send_empty_frags="enable",       # Security enhancement
    ssl_static_key_ciphers="enable"      # Allow static key ciphers
)

# ✅ UPDATE - Bulk configuration
result = fgt.firewall.ssl_setting.update(
    proxy_connect_timeout=30,
    ssl_dh_bits="2048",
    cert_cache_capacity=300,
    session_cache_capacity=500,
    abbreviate_handshake="enable",
    no_matching_cipher_action="bypass"
)
```

**Common SSL Settings:**

**Connection & Timeout:**
- `proxy_connect_timeout`: Connection timeout (1-60 seconds)
- `ssl_dh_bits`: Diffie-Hellman key size (`"768"`, `"1024"`, `"1536"`, `"2048"`)

**Certificate Caching:**
- `cert_cache_capacity`: Max cached certificates (0-500)
- `cert_cache_timeout`: Cache expiration (1-120 minutes)
- `cert_cache_manager`: Certificate manager caching (`"enable"` or `"disable"`)
- `short_lived_certificate`: Short-lived cert handling

**Session Caching:**
- `session_cache_capacity`: SSL session cache size (0-1000)
- `session_cache_timeout`: Session cache TTL (1-60 minutes)

**Performance Tuning:**
- `ssl_queue_threshold`: SSL processor queue threshold
- `kxp_queue_threshold`: Key exchange processor threshold  
- `abbreviate_handshake`: Enable abbreviated SSL handshakes (`"enable"` or `"disable"`)

**Cipher Behavior:**
- `no_matching_cipher_action`: Action when no cipher match (`"bypass"` or `"drop"`)
- `ssl_send_empty_frags`: Send empty fragments for security (`"enable"` or `"disable"`)
- `ssl_static_key_ciphers`: Allow static key ciphers

**Note on Performance Fields:** Some performance tuning fields (`ssl_queue_threshold`, `kxp_queue_threshold`) may not be returned in GET responses on all FortiOS versions, even after successful updates.

---

## FortiOS API Limitations

### Summary of Restrictions

| Component | Create | Read | Update | Delete | Notes |
|-----------|--------|------|--------|--------|-------|
| **SSH Host Key** | ❌ | ✅ | ❌ | ❌ | Auto-discovered only |
| **SSH Local CA** | ✅ | ✅ | ❌ | ❌ | Security restriction |
| **SSH Local Key** | ❌ | ✅ | ❌ | ❌ | CLI/built-in only |
| **SSH Settings** | N/A | ✅ | ✅ | N/A | Global config |
| **SSL Settings** | N/A | ✅ | ✅ | N/A | Global config |

### Detailed Limitations

#### 1. SSH Host Keys - Read-Only

**What:** SSH host keys discovered during traffic inspection.

**Limitation:** Cannot create, update, or delete via API.

**API Errors:**
- Create: `-651` (Input value is invalid)
- Update: `-3` (Entry not found)
- Delete: `-3` (Entry not found)

**Why:** Host keys are automatically discovered when FortiGate inspects SSH connections. Manual creation is not supported.

**Workaround:** None needed - keys are auto-discovered during SSH inspection.

---

#### 2. SSH Local Keys - Read-Only

**What:** SSH keys used by FortiGate for SSH proxy operations.

**Limitation:** Cannot create, update, or delete via API.

**API Error:** `-651` (Input value is invalid)

**Why:** Keys require specific cryptographic formats and are typically pre-configured or generated via CLI for security reasons.

**Workaround:** Use FortiGate CLI to generate keys:
```bash
config firewall ssh local-key
    edit "custom-rsa-key"
        set password "YourSecurePassword"
    next
end
```

---

#### 3. SSH Local CAs - No Delete/Update

**What:** SSH certificate authorities for signing certificates.

**Limitation:** Can create and read, but **CANNOT update or delete** via API.

**API Error:** `-14` (Permission denied) - even with `super_admin` privileges

**Why:** This is a **FortiOS security restriction** to prevent accidental CA deletion that could:
- Break active SSH proxy policies
- Disrupt certificate-based SSH authentication
- Impact production SSH inspection
- Require manual certificate reissuance

**Impact:** Test CAs created via API accumulate and cannot be cleaned up programmatically.

**Workaround for Deletion:**

**Method 1 - CLI:**
```bash
config firewall ssh local-ca
    delete pytest-test-ca
    delete company-ssh-ca
end
```

**Method 2 - Web GUI:**
1. Navigate to: **Security Fabric > Certificates > SSH Local CA**
2. Select the CA to delete
3. Click **Delete** button
4. Confirm deletion

**Best Practice:**
- Use unique, timestamped names for test CAs
- Document CAs created during testing
- Schedule regular manual cleanup
- Use production-like CA names sparingly in testing

---

#### 4. SSL Settings - Queue Threshold Fields

**What:** Performance tuning fields for SSL processing queues.

**Limitation:** Fields may not appear in GET responses after update.

**Fields Affected:**
- `ssl-queue-threshold`
- `kxp-queue-threshold`

**Why:** These fields may not be returned by the API on all FortiOS versions, even though updates succeed.

**Workaround:** Verify update success via status code rather than GET validation:
```python
result = fgt.firewall.ssl_setting.update(ssl_queue_threshold=64)
if result["status"] == "success":
    print("Update successful")
    # Don't rely on GET to verify these specific fields
```

---

### Testing Implications

**Test Results from Comprehensive Suite:**
- **SSH Proxy Tests:** 15 passed, 24 skipped (39 total)
- **SSL Proxy Tests:** 28 passed, 0 failed

**Skipped Tests:** Tests for unsupported API operations (create/update/delete on read-only objects).

**Passing Tests:** All supported operations (GET, EXISTS, and SSH Settings/SSL Settings updates).

**Orphaned Test Data:** SSH Local CAs created during testing remain in FortiGate config and require manual cleanup.

---

## Common Patterns

### Pattern 1: Read-Only Object Inspection

```python
# List all SSH host keys discovered
keys = fgt.firewall.ssh_host_key.get()
for key in keys:
    print(f"Host: {key['hostname']}")
    print(f"  Type: {key['type']}")
    print(f"  Status: {key.get('status', 'unknown')}")
    print(f"  Public Key: {key.get('public-key', 'N/A')[:50]}...")

# Check if specific host key exists
if fgt.firewall.ssh_host_key.exists(name="server1.example.com"):
    key = fgt.firewall.ssh_host_key.get(name="server1.example.com")
    print(f"Found key for {key['hostname']}")
```

### Pattern 2: SSH CA Management (Create + Read Only)

```python
# Create CA (one-time operation - cannot delete via API!)
ca_name = f"production-ca-{datetime.now().strftime('%Y%m%d')}"

result = fgt.firewall.ssh_local_ca.create(
    name=ca_name,
    password="SecureP@ssw0rd123",
    source_type="built-in",
    source="CA_RSA2K"
)

if result["status"] == "success":
    print(f"✅ Created CA: {ca_name}")
    print("⚠️  Remember: Cannot delete this via API!")
    
    # Configure SSH settings to use this CA
    fgt.firewall.ssh_setting.update(
        host_trusted_checking="enable",
        caname=ca_name
    )
```

### Pattern 3: SSL Settings Configuration

```python
# High-performance SSL configuration
result = fgt.firewall.ssl_setting.update(
    proxy_connect_timeout=60,
    ssl_dh_bits="2048",
    cert_cache_capacity=500,
    cert_cache_timeout=30,
    session_cache_capacity=1000,
    session_cache_timeout=60,
    abbreviate_handshake="enable",
    no_matching_cipher_action="bypass"
)

if result["status"] == "success":
    print("✅ SSL settings updated for high performance")
    
    # Verify settings
    settings = fgt.firewall.ssl_setting.get()
    print(f"Timeout: {settings['proxy-connect-timeout']}s")
    print(f"DH Bits: {settings['ssl-dh-bits']}")
    print(f"Cert Cache: {settings['cert-cache-capacity']}")
```

### Pattern 4: Security-Hardened SSL Configuration

```python
# Security-focused SSL configuration
result = fgt.firewall.ssl_setting.update(
    ssl_dh_bits="2048",                    # Strong DH key
    no_matching_cipher_action="drop",      # Drop weak ciphers
    ssl_send_empty_frags="enable",         # Security enhancement
    ssl_static_key_ciphers="disable",      # Disable weak ciphers
    abbreviate_handshake="disable"         # Full handshakes for security
)

if result["status"] == "success":
    print("✅ SSL settings hardened for security")
```

---

## Complete Examples

### Example 1: SSH Inspection Setup (Read-Only Operations)

```python
from hfortix import FortiOS

fgt = FortiOS(
    host="fortigate.example.com",
    token="your_token",
    verify=False,
    error_mode="raise"
)

print("=== SSH Inspection Status ===\n")

# Check SSH settings
settings = fgt.firewall.ssh_setting.get()
print(f"Host Trust Checking: {settings.get('host-trusted-checking', 'unknown')}")
print(f"Primary CA: {settings.get('caname', 'none')}\n")

# List discovered host keys
print("Discovered SSH Host Keys:")
host_keys = fgt.firewall.ssh_host_key.get()
for key in host_keys:
    print(f"  • {key['hostname']} ({key['type']})")

# List available local keys
print("\nAvailable SSH Local Keys:")
local_keys = fgt.firewall.ssh_local_key.get()
for key in local_keys:
    print(f"  • {key['name']}")

# List configured CAs
print("\nConfigured SSH CAs:")
cas = fgt.firewall.ssh_local_ca.get()
for ca in cas:
    print(f"  • {ca['name']} (Source: {ca.get('source', 'unknown')})")
```

### Example 2: SSL Inspection Configuration

```python
from hfortix import FortiOS

fgt = FortiOS(
    host="fortigate.example.com",
    token="your_token",
    verify=False,
    error_mode="raise"
)

print("=== Configuring SSL Inspection ===\n")

# Get current settings
current = fgt.firewall.ssl_setting.get()
print(f"Current DH Bits: {current.get('ssl-dh-bits', 'unknown')}")
print(f"Current Timeout: {current.get('proxy-connect-timeout', 'unknown')}s\n")

# Apply balanced configuration
print("Applying balanced SSL configuration...")
result = fgt.firewall.ssl_setting.update(
    proxy_connect_timeout=30,
    ssl_dh_bits="2048",
    cert_cache_capacity=300,
    cert_cache_timeout=15,
    session_cache_capacity=500,
    session_cache_timeout=30,
    abbreviate_handshake="enable",
    no_matching_cipher_action="bypass",
    ssl_send_empty_frags="enable"
)

if result["status"] == "success":
    print("✅ SSL configuration updated successfully\n")
    
    # Verify changes
    updated = fgt.firewall.ssl_setting.get()
    print("Updated Settings:")
    print(f"  DH Bits: {updated.get('ssl-dh-bits')}")
    print(f"  Timeout: {updated.get('proxy-connect-timeout')}s")
    print(f"  Cert Cache: {updated.get('cert-cache-capacity')}")
    print(f"  Session Cache: {updated.get('session-cache-capacity')}")
else:
    print(f"❌ Update failed: {result}")
```

### Example 3: SSH CA Creation with Error Handling

```python
from hfortix import FortiOS
from datetime import datetime

fgt = FortiOS(
    host="fortigate.example.com",
    token="your_token",
    verify=False,
    error_mode="return"  # Return errors instead of raising
)

# Generate unique CA name with timestamp
ca_name = f"prod-ssh-ca-{datetime.now().strftime('%Y%m%d-%H%M%S')}"

print(f"=== Creating SSH CA: {ca_name} ===\n")

# Create CA
result = fgt.firewall.ssh_local_ca.create(
    name=ca_name,
    password="SecureP@ssw0rd123!",
    source_type="built-in",
    source="CA_RSA4K"  # Use RSA 4096 for extra security
)

if result.get("status") == "success":
    print(f"✅ CA '{ca_name}' created successfully")
    print(f"⚠️  IMPORTANT: This CA cannot be deleted via API!")
    print(f"   Use CLI or GUI for deletion if needed.\n")
    
    # Configure SSH settings to use new CA
    print("Configuring SSH settings...")
    settings_result = fgt.firewall.ssh_setting.update(
        host_trusted_checking="enable",
        caname=ca_name
    )
    
    if settings_result.get("status") == "success":
        print("✅ SSH settings updated to use new CA")
        
        # Verify configuration
        settings = fgt.firewall.ssh_setting.get()
        print(f"\nCurrent SSH Configuration:")
        print(f"  Trust Checking: {settings.get('host-trusted-checking')}")
        print(f"  Primary CA: {settings.get('caname')}")
    else:
        print(f"❌ Failed to update settings: {settings_result}")
else:
    print(f"❌ Failed to create CA: {result}")
    if result.get("http_status") == 400:
        print("   Check if CA name already exists or password requirements")
```

### Example 4: Comprehensive SSL Performance Tuning

```python
from hfortix import FortiOS

fgt = FortiOS(
    host="fortigate.example.com",
    token="your_token",
    verify=False,
    error_mode="raise"
)

def configure_ssl_profile(profile_name: str):
    """Configure SSL settings based on named profile."""
    
    profiles = {
        "high-performance": {
            "proxy_connect_timeout": 60,
            "ssl_dh_bits": "2048",
            "cert_cache_capacity": 500,
            "cert_cache_timeout": 30,
            "session_cache_capacity": 1000,
            "session_cache_timeout": 60,
            "ssl_queue_threshold": 96,
            "kxp_queue_threshold": 48,
            "abbreviate_handshake": "enable",
            "no_matching_cipher_action": "bypass"
        },
        "security-hardened": {
            "proxy_connect_timeout": 10,
            "ssl_dh_bits": "2048",
            "cert_cache_capacity": 200,
            "cert_cache_timeout": 5,
            "session_cache_capacity": 500,
            "session_cache_timeout": 10,
            "abbreviate_handshake": "disable",
            "no_matching_cipher_action": "drop",
            "ssl_send_empty_frags": "enable",
            "ssl_static_key_ciphers": "disable"
        },
        "balanced": {
            "proxy_connect_timeout": 30,
            "ssl_dh_bits": "2048",
            "cert_cache_capacity": 300,
            "cert_cache_timeout": 15,
            "session_cache_capacity": 500,
            "session_cache_timeout": 30,
            "abbreviate_handshake": "enable",
            "no_matching_cipher_action": "bypass",
            "ssl_send_empty_frags": "enable"
        }
    }
    
    if profile_name not in profiles:
        raise ValueError(f"Unknown profile: {profile_name}")
    
    config = profiles[profile_name]
    
    print(f"=== Applying '{profile_name}' SSL Profile ===\n")
    
    result = fgt.firewall.ssl_setting.update(**config)
    
    if result["status"] == "success":
        print(f"✅ '{profile_name}' profile applied successfully\n")
        
        # Show configuration
        settings = fgt.firewall.ssl_setting.get()
        print("Active SSL Settings:")
        for key, value in config.items():
            api_key = key.replace("_", "-")
            actual = settings.get(api_key, "N/A")
            status = "✅" if str(actual) == str(value) else "⚠️"
            print(f"  {status} {key}: {actual}")
    else:
        print(f"❌ Failed to apply profile: {result}")

# Apply different profiles
configure_ssl_profile("balanced")
```

---

## Related Documentation

### Core Documentation
- [Convenience Wrappers Guide](CONVENIENCE_WRAPPERS.md) - Overview of all wrappers
- [API Coverage](../API_COVERAGE.md) - Complete API endpoint coverage
- [Error Handling](../ERROR_HANDLING_CONFIG.md) - Error modes and handling

### SSH/SSL Specific
- [Firewall Policy Wrapper](FIREWALL_POLICY_WRAPPER.md) - Firewall policies using SSH/SSL profiles
- [Validation Guide](../VALIDATION_GUIDE.md) - Input validation for all parameters

### Testing
- Test Suite: `.dev/pytests/firewall/ssh_proxy.py` (SSH tests)
- Test Suite: `.dev/pytests/firewall/ssl_proxy.py` (SSL tests)
- Test Summary: `.dev/SSH_TEST_SUMMARY.md` (Detailed API limitations)

### FortiOS References
- FortiOS REST API Documentation
- FortiOS CLI Reference (for manual CA deletion)
- FortiOS Administration Guide (SSH/SSL inspection)

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 0.4.2 | 2026-01-02 | Initial SSH/SSL proxy wrapper documentation |
| 0.4.2 | 2026-01-02 | Documented FortiOS API limitations |
| 0.4.2 | 2026-01-02 | Added comprehensive test coverage notes |

---

**Need Help?**

- Check test files for working examples: `.dev/pytests/firewall/ssh_proxy.py`, `.dev/pytests/firewall/ssl_proxy.py`
- Review API limitations: [SSH_TEST_SUMMARY.md](../../../.dev/SSH_TEST_SUMMARY.md)
- See error handling guide: [ERROR_HANDLING_CONFIG.md](../ERROR_HANDLING_CONFIG.md)
