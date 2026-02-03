# FortiOS Advanced API Features

**File uploads/downloads, batch transactions, VDOMs, and certificate management**

This document covers advanced FortiOS API capabilities that may be implemented in future versions (v0.6.0+).

---

## Table of Contents

1. [File Upload/Download](#file-uploaddownload)
2. [Batch Transactions](#batch-transactions)
3. [VDOM Support](#vdom-support)
4. [Certificate Management](#certificate-management)

---

## File Upload/Download

**Supported by:** Monitor API endpoints  
**Use cases:** VM licenses, CA certificates, configuration backup/restore, debug reports

### Uploading Files

Two methods supported for uploading files:

#### Method 1: JSON Data (Base64 Encoded)

**Requirements:**
- File must be Base64 encoded
- Use `file_content` field in JSON body

**Example: Upload (restore) configuration file**
```python
import base64

with open("vd1.conf.txt", "r") as f:
    file_content = base64.b64encode(f.read().encode()).decode()

response = fgt._client.post(
    "monitor",
    "/system/config/restore",
    params={"vdom": "vdom1"},
    data={
        "source": "upload",
        "scope": "vdom",
        "file_content": file_content
    }
)
```

#### Method 2: Multi-Part File (No Encoding)

**Requirements:**
- File does NOT need Base64 encoding
- Use HTTP multi-part file upload

**Example: Upload (restore) configuration file**
```python
response = fgt._client.post(
    "monitor",
    "/system/config/restore",
    params={"vdom": "vdom1"},
    data={
        "source": "upload",
        "scope": "vdom",
    },
    files=[
        ('file', ('config.conf', open("vd1.conf.txt", "r"), 'text/plain'))
    ]
)
```

### Downloading Files

**Response format:** File in raw content (not JSON)  
**Header indicator:** `Content-Disposition: attachment`

#### Method 1: Browser

Browser automatically downloads file when `Content-Disposition: attachment` header present.

**Example: Download debug report**
```
https://192.168.1.99/api/v2/monitor/system/debug/download?access_token=******
```

#### Method 2: Script

Script must:
1. Check response headers for `Content-Disposition: attachment`
2. Write response content to local file

**Example: Download using Python**
```python
response = fgt._client.get(
    "monitor",
    "/system/debug/download",
    raw_json=True  # Get full response
)

# Check if file download
if response.headers.get('Content-Disposition', '').startswith('attachment'):
    with open('debug_report.tar.gz', 'wb') as f:
        f.write(response.content)
```

### Implementation Notes (Future)

For generator implementation (v0.6.0+):

1. **Detect file upload endpoints** from schema
2. **Add upload helper methods:**
   ```python
   def upload_config(self, file_path: str, vdom: str = "root", scope: str = "vdom"):
       """Upload configuration file for restore."""
       with open(file_path, 'rb') as f:
           file_content = base64.b64encode(f.read()).decode()
       
       return self._client.post(
           "monitor",
           "/system/config/restore",
           params={"vdom": vdom},
           data={
               "source": "upload",
               "scope": scope,
               "file_content": file_content
           }
       )
   ```

3. **Add download helper methods:**
   ```python
   def download_debug_report(self, save_path: str) -> bool:
       """Download debug report for technical support."""
       response = self._client.get(
           "monitor",
           "/system/debug/download",
           raw_json=True
       )
       
       if response.headers.get('Content-Disposition', '').startswith('attachment'):
           with open(save_path, 'wb') as f:
               f.write(response.content)
           return True
       return False
   ```

**Priority:** ⭐ Nice to have (v0.6.0+)

---

## Batch Transactions

**Added in:** FortiOS 6.4.0  
**Supported by:** Configuration API (CMDB)  
**Purpose:** Submit multiple configuration commands in a single atomic transaction with rollback support

### Key Concepts

- **Atomic operations:** All succeed or all fail
- **Rollback capability:** Abort transaction if any request fails
- **Multiple concurrent transactions:** Allowed if not modifying same tables
- **Table locking:** When transaction modifies a table, that table is locked until commit/abort
- **Timeout:** Transactions expire if not committed within timeout period

### Basic Transaction Workflow

```
1. transaction-start (returns transaction-id)
2. Request 1 (with transaction-id in header)
3. Request 2 (with transaction-id in header)
4. Request N (with transaction-id in header)
5. transaction-show (optional - view cached commands, FortiOS 7.4.1+)
6. transaction-commit OR transaction-abort
```

### Example: Successful Transaction

Create VLAN and policy that references it:

```python
# 1. Start transaction
response = fgt._client.post(
    "cmdb",
    "?action=transaction-start",
    params={"vdom": "root"},
    data={"timeout": 60}
)
transaction_id = response["results"]["transaction-id"]  # e.g., 19

# 2. Create VLAN (with transaction-id in header)
fgt._client.post(
    "cmdb",
    "/system/interface",
    headers={"X-TRANSACTION-ID": str(transaction_id)},
    data={
        "name": "officeNetwork",
        "vdom": "root",
        "vlanid": 10,
        "mode": "static",
        "ip": "192.168.9.1/24",
        "interface": "port6"
    }
)

# 3. Create policy referencing new VLAN (with transaction-id in header)
fgt._client.post(
    "cmdb",
    "/firewall/policy",
    headers={"X-TRANSACTION-ID": str(transaction_id)},
    data={
        "policyid": 0,
        "srcintf": [{"name": "officeNetwork"}],
        "srcaddr": [{"name": "all"}],
        "dstintf": [{"name": "port3"}],
        "dstaddr": [{"name": "all"}],
        "service": [{"name": "ALL"}],
        "schedule": "always",
        "action": "accept",
        "nat": "enable"
    }
)

# 4. View cached commands (optional, FortiOS 7.4.1+)
cached = fgt._client.get(
    "cmdb",
    "?action=transaction-show",
    params={"transaction-id": transaction_id}
)
# Returns CLI commands that will be executed

# 5. Commit transaction
fgt._client.post(
    "cmdb",
    "?action=transaction-commit",
    params={"vdom": "root"},
    data={"transaction-id": transaction_id}
)
```

### Example: Failed Transaction with Rollback

```python
# 1. Start transaction
response = fgt._client.post(
    "cmdb",
    "?action=transaction-start",
    params={"vdom": "root"},
    data={"timeout": 60}
)
transaction_id = response["results"]["transaction-id"]  # e.g., 23

# 2. Create VLAN (succeeds)
fgt._client.post(
    "cmdb",
    "/system/interface",
    headers={"X-TRANSACTION-ID": str(transaction_id)},
    data={...}
)

# 3. Create policy with non-existent interface (fails)
try:
    fgt._client.post(
        "cmdb",
        "/firewall/policy",
        headers={"X-TRANSACTION-ID": str(transaction_id)},
        data={
            "srcintf": [{"name": "homeNetwork"}],  # Does not exist!
            ...
        }
    )
except Exception as e:
    # 4. Abort transaction (rollback all changes)
    fgt._client.post(
        "cmdb",
        "?action=transaction-abort",
        params={"vdom": "root"},
        data={"transaction-id": transaction_id}
    )
    # VLAN is NOT created because transaction was aborted
```

### Transaction API Commands

#### transaction-start

**Method:** POST  
**Endpoint:** `/api/v2/cmdb?action=transaction-start`  
**Parameters:**
- `timeout` (int) - Transaction timeout in seconds

**Returns:** `transaction-id`

#### transaction-show

**Method:** GET (FortiOS 7.4.1+)  
**Endpoint:** `/api/v2/cmdb?action=transaction-show`  
**Parameters:**
- `transaction-id` (int) - Transaction ID

**Returns:** List of cached CLI commands (not yet committed)

#### transaction-commit

**Method:** POST  
**Endpoint:** `/api/v2/cmdb?action=transaction-commit`  
**Parameters:**
- `transaction-id` (int) - Transaction ID to commit

**Effect:** Applies all cached commands to configuration

#### transaction-abort

**Method:** POST  
**Endpoint:** `/api/v2/cmdb?action=transaction-abort`  
**Parameters:**
- `transaction-id` (int) - Transaction ID to abort

**Effect:** Discards all cached commands (rollback)

#### transaction-list

**Method:** GET  
**Endpoint:** `/api/v2/cmdb?action=transaction-list`  
**Returns:** List of all active transactions

### Limitations

1. **Table locking:** Multiple transactions cannot modify the same table simultaneously
2. **Not all tables support transactions:** Some tables will return error
3. **Transaction expiration:** Must commit within timeout period or transaction expires
4. **Concurrent modification:** If another transaction locks a table you need, error returned

### Implementation Notes (Future)

For generator implementation (v0.7.0+):

```python
class Transaction:
    """Context manager for batch transactions."""
    
    def __init__(self, client: IHTTPClient, vdom: str = "root", timeout: int = 60):
        self._client = client
        self._vdom = vdom
        self._timeout = timeout
        self._transaction_id: int | None = None
    
    def __enter__(self):
        # Start transaction
        response = self._client.post(
            "cmdb",
            "?action=transaction-start",
            params={"vdom": self._vdom},
            data={"timeout": self._timeout}
        )
        self._transaction_id = response["results"]["transaction-id"]
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            # Exception occurred - abort transaction
            self.abort()
            return False
        else:
            # Success - commit transaction
            self.commit()
            return True
    
    def commit(self):
        """Commit transaction."""
        if self._transaction_id is None:
            raise ValueError("No active transaction")
        
        self._client.post(
            "cmdb",
            "?action=transaction-commit",
            params={"vdom": self._vdom},
            data={"transaction-id": self._transaction_id}
        )
    
    def abort(self):
        """Abort transaction (rollback)."""
        if self._transaction_id is None:
            return
        
        self._client.post(
            "cmdb",
            "?action=transaction-abort",
            params={"vdom": self._vdom},
            data={"transaction-id": self._transaction_id}
        )
    
    def show(self) -> list[str]:
        """Show cached commands (FortiOS 7.4.1+)."""
        if self._transaction_id is None:
            raise ValueError("No active transaction")
        
        response = self._client.get(
            "cmdb",
            "?action=transaction-show",
            params={"transaction-id": self._transaction_id}
        )
        return response.get("results", [])
    
    @property
    def transaction_id(self) -> int:
        """Get transaction ID for manual header usage."""
        if self._transaction_id is None:
            raise ValueError("No active transaction")
        return self._transaction_id


# Usage example:
with Transaction(fgt._client, vdom="root", timeout=120) as txn:
    # All requests automatically include transaction ID in headers
    fgt.api.cmdb.system.interface.post(
        name="vlan10",
        vlanid=10,
        interface="port1",
        _transaction_id=txn.transaction_id  # Pass to method
    )
    
    fgt.api.cmdb.firewall.policy.post(
        srcintf=[{"name": "vlan10"}],
        ...,
        _transaction_id=txn.transaction_id
    )
    
    # View cached commands before commit
    print(txn.show())
    
    # If any exception, transaction is automatically aborted
    # If success, transaction is automatically committed
```

**Priority:** ⭐ Future (v0.7.0+) - depends on FortiOS support and user demand

---

## VDOM Support

**Virtual Domains** allow logical partitioning of a single FortiGate into multiple virtual instances.

### Default Behavior

If VDOMs enabled, queries use **management VDOM** by default.

Response shows which VDOM was queried:
```json
{
  "vdom": "root",
  "path": "firewall",
  "name": "policy",
  "status": "success"
}
```

### VDOM Parameter

Use `vdom` parameter to specify which VDOM(s) to query or modify:

#### Single VDOM
```python
# Query specific VDOM
policies = fgt.api.cmdb.firewall.policy.get(vdom="vdom1")
```

URL: `/api/v2/cmdb/firewall/policy/?vdom=vdom1`

#### Multiple VDOMs
```python
# Query multiple VDOMs
policies = fgt.api.cmdb.firewall.policy.get(vdom="vdom1,vdom2")
```

URL: `/api/v2/cmdb/firewall/policy/?vdom=vdom1,vdom2`

#### All VDOMs
```python
# Query ALL VDOMs (that admin has access to)
policies = fgt.api.cmdb.firewall.policy.get(vdom="*")
```

URL: `/api/v2/cmdb/firewall/policy/?vdom=*`

### Permission Handling

**Important:** `vdom=*` only returns results from VDOMs the authenticated admin has access to.

If admin lacks access to specified VDOM, permission error returned:
```json
{
  "http_status": 403,
  "error": "permission denied"
}
```

### Implementation Notes

VDOM support **already implemented** in `hfortix_core`:

```python
# From HTTPClient interface
def get(
    self,
    api_type: str,
    endpoint: str,
    params: dict[str, Any] | None = None,
    vdom: str | bool | None = None,  # ✅ Already supported!
    raw_json: bool = False,
) -> dict[str, Any]:
    ...
```

**Usage:**
```python
# Single VDOM
addresses = fgt.api.cmdb.firewall.address.get(vdom="vdom1")

# Multiple VDOMs
addresses = fgt.api.cmdb.firewall.address.get(vdom="vdom1,vdom2")

# All VDOMs
addresses = fgt.api.cmdb.firewall.address.get(vdom="*")

# Skip VDOM parameter (use default)
addresses = fgt.api.cmdb.firewall.address.get(vdom=False)
```

**Status:** ✅ Already implemented in core - just document in generated code

**Priority:** N/A (already available)

---

## Certificate Management

**Purpose:** Upload CA certificates, CRLs, local certificates, remote certificates via API

**Requirement:** Certificates must be Base64 encoded

### Certificate Upload Endpoints

#### 1. CA Certificate Import

**Endpoint:** `/api/v2/monitor/vpn-certificate/ca/import`

**Methods:**
- File upload (Base64 encoded)
- SCEP (Simple Certificate Enrollment Protocol)

**Parameters:**
```json
{
  "import_method": "file|scep",
  "scep_url": "string",           // If import_method=scep
  "scep_ca_id": "string",         // If import_method=scep
  "scope": "vdom|global",         // Default: vdom
  "file_content": "string"        // Base64 encoded certificate
}
```

**Example:**
```python
import base64

# Read CA certificate
with open("ca_cert.pem", "rb") as f:
    ca_content = base64.b64encode(f.read()).decode()

# Upload CA certificate
response = fgt.api.monitor.vpn_certificate.ca.import_certificate(
    import_method="file",
    scope="global",
    file_content=ca_content
)
```

#### 2. CRL Import

**Endpoint:** `/api/v2/monitor/vpn-certificate/crl/import`

**Parameters:**
```json
{
  "scope": "vdom|global",
  "file_content": "string"        // Base64 encoded CRL
}
```

**Example:**
```python
with open("ca.crl", "rb") as f:
    crl_content = base64.b64encode(f.read()).decode()

response = fgt.api.monitor.vpn_certificate.crl.import_certificate(
    scope="vdom",
    file_content=crl_content
)
```

#### 3. Local Certificate Import

**Endpoint:** `/api/v2/monitor/vpn-certificate/local/import`

**Types:**
- `local` - Standard certificate + key
- `pkcs12` - PKCS#12 bundle (.p12/.pfx)
- `regular` - Certificate only

**Parameters:**
```json
{
  "type": "local|pkcs12|regular",
  "certname": "string",
  "password": "string",           // For PKCS#12
  "key_file_content": "string",   // Base64 encoded private key (if type=local)
  "scope": "vdom|global",
  "acme-domain": "string",        // For ACME/Let's Encrypt
  "acme-email": "string",
  "acme-ca-url": "string",
  "acme-rsa-key-size": 0,
  "acme-renew-window": 0,
  "file_content": "string"        // Base64 encoded certificate
}
```

**Example: Upload PKCS#12 Certificate**
```python
import base64

# Read PKCS#12 file
with open("certificate.p12", "rb") as f:
    p12_content = base64.b64encode(f.read()).decode()

# Upload
response = fgt.api.monitor.vpn_certificate.local.import_certificate(
    type="pkcs12",
    certname="my_certificate",
    password="cert_password",
    scope="global",
    file_content=p12_content
)
```

**Example: Upload Certificate + Key**
```python
# Read certificate
with open("server.crt", "rb") as f:
    cert_content = base64.b64encode(f.read()).decode()

# Read private key
with open("server.key", "rb") as f:
    key_content = base64.b64encode(f.read()).decode()

# Upload
response = fgt.api.monitor.vpn_certificate.local.import_certificate(
    type="local",
    certname="web_server",
    file_content=cert_content,
    key_file_content=key_content,
    scope="vdom"
)
```

#### 4. Remote Certificate Import

**Endpoint:** `/api/v2/monitor/vpn-certificate/remote/import`

**Parameters:**
```json
{
  "scope": "vdom|global",
  "file_content": "string"
}
```

#### 5. CSR Generation

**Endpoint:** `/api/v2/monitor/vpn-certificate/csr/generate`

**Parameters:**
```json
{
  "certname": "string",
  "subject": "string",
  "keytype": "rsa|ec",
  "keysize": 1024|1536|2048|4096,     // If keytype=rsa
  "curvename": "secp256r1|secp384r1|secp521r1",  // If keytype=ec
  "orgunits": ["string"],
  "org": "string",
  "city": "string",
  "state": "string",
  "countrycode": "string",
  "email": "string",
  "sub_alt_name": "string",
  "password": "string",
  "scep_url": "string",
  "scep_password": "string",
  "scope": "vdom|global"
}
```

**Example: Generate CSR**
```python
response = fgt.api.monitor.vpn_certificate.csr.generate(
    certname="web_server",
    subject="CN=example.com,OU=IT,O=Example Corp,L=Seattle,ST=WA,C=US",
    keytype="rsa",
    keysize=2048,
    email="admin@example.com",
    sub_alt_name="DNS:www.example.com,DNS:example.com",
    scope="global"
)

# Response contains generated CSR
csr = response["results"]["csr"]
```

### PowerShell Base64 Encoding Example

```powershell
# Change to working directory
cd C:\users\username\desktop

# Read certificate file
$pkcs12cert = Get-Content 'C:\users\path\to\certificate.p12' -Encoding Byte

# Encode to Base64 and save
[System.Convert]::ToBase64String($pkcs12cert) | Out-File 'base64encodedcert.txt'
```

### Implementation Notes (Future)

For generator implementation (v0.6.0+):

```python
class VpnCertificateCA:
    """CA certificate management."""
    
    def import_certificate(
        self,
        file_path: str | None = None,
        file_content: str | None = None,
        import_method: Literal["file", "scep"] = "file",
        scope: Literal["vdom", "global"] = "vdom",
        scep_url: str | None = None,
        scep_ca_id: str | None = None,
        vdom: str | bool | None = None,
    ) -> dict[str, Any]:
        """
        Import CA certificate.
        
        Args:
            file_path: Path to certificate file (auto-encoded to Base64)
            file_content: Pre-encoded Base64 certificate content
            import_method: 'file' or 'scep'
            scope: 'vdom' or 'global'
            scep_url: SCEP server URL (if import_method='scep')
            scep_ca_id: SCEP CA ID (if import_method='scep')
        
        Returns:
            API response
        
        Example:
            >>> # Upload from file (auto Base64 encode)
            >>> result = fgt.api.monitor.vpn_certificate.ca.import_certificate(
            ...     file_path="ca_cert.pem",
            ...     scope="global"
            ... )
            
            >>> # Upload pre-encoded content
            >>> result = fgt.api.monitor.vpn_certificate.ca.import_certificate(
            ...     file_content=base64_encoded_content,
            ...     scope="global"
            ... )
        """
        import base64
        
        # Encode file if path provided
        if file_path and not file_content:
            with open(file_path, "rb") as f:
                file_content = base64.b64encode(f.read()).decode()
        
        if not file_content:
            raise ValueError("Either file_path or file_content required")
        
        data = {
            "import_method": import_method,
            "scope": scope,
            "file_content": file_content,
        }
        
        if import_method == "scep":
            if scep_url:
                data["scep_url"] = scep_url
            if scep_ca_id:
                data["scep_ca_id"] = scep_ca_id
        
        return self._client.post(
            "monitor",
            "/vpn-certificate/ca/import",
            data=data,
            vdom=vdom
        )
```

**Priority:** ⭐⭐ Nice to have (v0.6.0+) - common use case

---

## Summary

### Already Implemented

- ✅ **VDOM Support** - Already in `hfortix_core.HTTPClient`
  - Just document in generated code docstrings

### Future Implementation (v0.6.0+)

- ⭐⭐ **File Upload/Download** - Common use case
  - Helper methods for config backup/restore
  - Certificate upload with auto-Base64 encoding
  
- ⭐⭐ **Certificate Management** - Common use case
  - Import CA/CRL/local/remote certificates
  - Generate CSRs
  - Auto Base64 encoding from file paths

### Future Implementation (v0.7.0+)

- ⭐ **Batch Transactions** - Advanced use case
  - Transaction context manager
  - Automatic commit/abort
  - View cached commands
  - Helpful but not essential for most users

---

## References

- FortiOS REST API Documentation
- GENERATOR_DESIGN.md - Main architecture
- OUT_OF_SCOPE.md - Features not in v0.5.0
- ADDITIONAL_SUGGESTIONS.md - Enhancement ideas
