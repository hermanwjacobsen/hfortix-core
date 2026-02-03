# FortiOS API Coverage

**SDK Version:** 0.5.154  
**FortiOS Version:** 7.6.5  
**Schema Version:** 1.7.0  
**Last Updated:** February 2026

---

## 🎯 Summary

**Total Coverage: 1,348 Endpoints (100%)**

| Category | Endpoints | Status | Description |
|----------|-----------|--------|-------------|
| **CMDB** | 561 | ✅ Complete | Configuration management (all config objects) |
| **Monitor** | 490 | ✅ Complete | Monitoring and status endpoints |
| **Log** | 286 | ✅ Complete | Log query endpoints (5 destinations) |
| **Service** | 11 | ✅ Complete | Service endpoints |
| **Total** | **1,348** | ✅ **100%** | All documented FortiOS 7.6.5 API endpoints |

All endpoints are **100% auto-generated** from FortiOS API schemas with:
- Complete `.py` implementation files (2,129 files)
- Complete `.pyi` type stub files (2,129 files)
- Schema-based validators
- Auto-generated tests

---

## 🚀 Key Features

### 1. Dual-Pattern Interface

All create/update methods support flexible syntax:

```python
# Dictionary pattern
fgt.api.cmdb.firewall.address.post(payload_dict={'name': 'x', 'subnet': '10.0.0.0/24'})

# Keyword pattern
fgt.api.cmdb.firewall.address.post(name='x', subnet='10.0.0.0/24')

# Mixed pattern
fgt.api.cmdb.firewall.address.post(payload_dict=base_config, name='override')
```

### 2. Response Formatting (v0.5.44+)

Built-in `fmt` module with 13 formatters:

```python
from hfortix_core import fmt

# Get data and format it
result = fgt.api.cmdb.firewall.address.get()

# Multiple output formats
print(fmt.to_json(result))           # JSON
print(fmt.to_yaml(result))           # YAML
print(fmt.to_csv(result))            # CSV
print(fmt.to_table(result))          # ASCII table
print(fmt.to_markdown_table(result)) # Markdown table
```

### 3. Key Normalization (v0.5.42+)

Automatic snake_case to camelCase conversion:

```python
# Both work identically:
fgt.api.cmdb.firewall.policy.post(srcintf=["port1"])  # snake_case
fgt.api.cmdb.firewall.policy.post(srcIntf=["port1"])  # camelCase
```

### 4. Complete Type Safety

Full `.pyi` stub files for IDE autocomplete and type checking:

```python
from hfortix_fortios import FortiOS

fgt = FortiOS(host="192.168.1.99", token="...")

# IDE shows all available endpoints and parameters
result = fgt.api.cmdb.firewall.address.post(
    name="test",      # IDE autocomplete shows all valid parameters
    subnet="10.0.0.0/24",
    type="ipmask",
)
```

---

## �� API Categories

### CMDB (Configuration Management) - 561 Endpoints

Configuration and management of FortiOS objects:

| Category | Endpoints | Description |
|----------|-----------|-------------|
| firewall | 89 | Firewall policies, addresses, services, schedules |
| system | 145 | System settings, interfaces, DNS, NTP |
| router | 26 | Routing configuration |
| user | 24 | User and authentication |
| vpn | 19 | VPN tunnels and settings |
| switch-controller | 48 | Switch management |
| wireless-controller | 44 | Wi-Fi management |
| log | 56 | Logging configuration |
| *other* | 110 | Other configuration areas |

### Monitor - 490 Endpoints

Real-time monitoring and status:

| Category | Endpoints | Description |
|----------|-----------|-------------|
| firewall | 44 | Session info, policy stats |
| system | 143 | Status, performance, resources |
| router | 33 | Routing tables, BGP status |
| vpn | 29 | Tunnel status, traffic |
| wifi | 53 | Wireless clients, status |
| *other* | 188 | Other monitoring areas |

### Log - 286 Endpoints

Log query endpoints across 5 destinations:

| Destination | Endpoints | Description |
|-------------|-----------|-------------|
| disk | 57 | Local disk logs |
| memory | 57 | Memory buffer logs |
| fortianalyzer | 57 | FortiAnalyzer logs |
| forticloud | 57 | FortiCloud logs |
| fortiai | 57 | FortiAI logs |
| *base* | 1 | Base log operations |

### Service - 11 Endpoints

System service operations:

| Endpoint | Description |
|----------|-------------|
| security-rating | Run security ratings |
| packet-capture | Packet capture operations |
| sniffer | Network sniffer |
| others | 8 additional service operations |

---

## 🔌 Method Reference

All endpoints support these standard methods:

| Method | HTTP | Description |
|--------|------|-------------|
| `.get()` | GET | Retrieve data/configuration |
| `.post()` | POST | Create new objects or execute operations |
| `.put()` | PUT | Update existing objects |
| `.delete()` | DELETE | Remove objects |
| `.exists()` | GET | Check if object exists (CMDB only) |

### Example Usage

```python
from hfortix_fortios import FortiOS

fgt = FortiOS(host="192.168.1.99", token="your-token")

# CMDB: Create firewall address
fgt.api.cmdb.firewall.address.post(
    name="web-server",
    subnet="192.168.1.100/32",
    comment="Production web server"
)

# CMDB: Get all addresses
addresses = fgt.api.cmdb.firewall.address.get()

# CMDB: Update address
fgt.api.cmdb.firewall.address.put(
    name="web-server",
    comment="Updated comment"
)

# CMDB: Check existence
if fgt.api.cmdb.firewall.address.exists("web-server"):
    print("Address exists!")

# CMDB: Delete address
fgt.api.cmdb.firewall.address.delete(name="web-server")

# Monitor: Get system status
status = fgt.api.monitor.system.status.get()

# Log: Query traffic logs
logs = fgt.api.log.disk.traffic.forward.get(rows=100)
```

---

## 📚 Related Documentation

- [Endpoint Methods](ENDPOINT_METHODS.md) - Complete endpoint listing
- [Filtering Guide](FILTERING_GUIDE.md) - Filter syntax and examples
- [Async Guide](ASYNC_GUIDE.md) - Async/await support
- [Error Handling](ERROR_HANDLING_CONFIG.md) - Error handling configuration
