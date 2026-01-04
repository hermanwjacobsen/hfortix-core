# FortiOS API Coverage - v0.5.0-beta# API Coverage



**Last Updated:** January 4, 2026This document tracks the implementation status of FortiOS API endpoints in the Fortinet Python SDK.

**SDK Version:** 0.5.0-beta

**FortiOS Version:** 7.6.5**Last Updated:** 2025-12-20  

**SDK Version:** 0.3.17  

## 🎯 Summary**FortiOS Version:** 7.6.5



**Total Coverage: 1,219 Endpoints (100%)**## 🎯 Key Features



| Category | Endpoints | Status | Description |### raw_json Parameter ✨

|----------|-----------|--------|-------------|**All API methods support raw_json parameter for full response access:**

| **CMDB** | 886 | ✅ Complete | Configuration management (all config objects) |- **Default Behavior**: `get('name')` → returns just the results

| **Monitor** | 295 | ✅ Complete | Monitoring and status endpoints |- **Full Response**: `get('name', raw_json=True)` → returns complete API response with status codes

| **Log** | 38 | ✅ Complete | Log query endpoints (5 destinations) |- **Coverage**: 100% of all implemented methods across all 863 endpoints

| **Total** | **1,219** | ✅ **100%** | All documented FortiOS 7.6.5 API endpoints |

### Dual-Pattern Interface ✨

All endpoints are **100% auto-generated** from FortiOS API schemas with complete type stubs, validators, and tests.**All create/update methods support flexible syntax:**

- **Dictionary Pattern**: `create(payload_dict={'name': 'x', 'subnet': '10.0.0.0/24'})`

## 🚀 Code Generation Features (v0.5.0)- **Keyword Pattern**: `create(name='x', subnet='10.0.0.0/24')`

- **Mixed Pattern**: `create(payload_dict=base, name='override')`

### Advanced Generator Capabilities

**Coverage**: All POST and PUT methods across 863 endpoint modules

1. **Swagger Fallback System**:

   - Automatically uses Swagger/OpenAPI documentation when API unavailable---

   - Handles HTTP 400, 404, 405, 424, 500, 503 errors gracefully

   - Handles JSON parse errors for binary endpoints## 📊 Overall Progress

   - Creates valid schemas with metadata tracking (`fallback_reason` field)

   - Ensures 100% endpoint coverage even on virtual FortiGates (hardware-specific features)**⚠️ BETA STATUS**: All current implementations are in beta. APIs are functional but may have incomplete parameter coverage or undiscovered edge cases.



2. **Smart Path Conversion**:**FortiOS Version:** 7.6.5

   - Automatically handles 3-part CMDB paths (e.g., `system.snmp/community`)

   - Converts to proper API format: `/api/v2/cmdb/system.snmp/community`| API Category | Status | Implemented | Total Available | Coverage |

   - Supports all path variations (2-part, 3-part, nested structures)|--------------|--------|-------------|-----------------|----------|

| **Configuration (CMDB)** | 🔷 Beta | 37 categories | 37 categories | 100% |

3. **Parameterized Log Endpoints**:| **Monitoring** | 🔷 Beta | 32 categories | 32 categories | 100% |

   - Specialized generator for log query endpoints| **Logging** | 🔷 Beta | 5 categories | 5 categories | 100% |

   - Nested class structure for organized access| **Service** | 🔷 Beta | 3 categories | 3 categories | 100% |

   - Supports all 5 log destinations (disk, memory, fortianalyzer, forticloud, search)| **Overall** | 🔷 Beta | **77 categories** | **77 categories** | **100%** 🎉 |

   - Handles event and traffic subtypes dynamically

**🎉 100% API COVERAGE ACHIEVED** (December 2025)

4. **Complete Type Safety**:- **CMDB API**: All 37 documented categories (100% coverage) - 500+ endpoints

   - Full `.pyi` stub files for all 1,219 endpoints- **Monitor API**: All 32 documented categories (100% coverage) - 200+ endpoints

   - Perfect IDE autocomplete (VS Code, PyCharm, etc.)- **Log API**: All 5 categories (100% coverage)

   - Type hints for all parameters and return values- **Service API**: All 3 categories (100% coverage)

   - Docstrings with parameter descriptions- **Total**: 77 of 77 documented FortiOS 7.6.5 API categories with 750+ API methods



5. **Auto-Generated Tests**:**Test Coverage:** 226 test files (145 CMDB, 81 Monitor) with 75%+ pass rate (~50% of generated endpoints tested)

   - Basic smoke tests for all endpoints

   - GET operation testing (safe, read-only)**Note:** All implementations are in beta status and will remain so until version 1.0.0 with comprehensive unit test coverage. Four CMDB categories (ssh-filter, telemetry-controller, wanopt, extender-controller) are not yet documented on FNDN.

   - VDOM and filter parameter testing

   - exists() method testing for CMDB endpoints**Legend:**

   - Validator import and structure testing- 🔷 **Beta** - Implemented and functional (all endpoints remain in beta until v1.0.0)

- 🚧 **In Progress** - Partially implemented

6. **Schema-Based Validation**:- ⏸️ **Not Started** - Not yet implemented

   - 1,219 validator modules with comprehensive validation- 🚫 **Not Applicable** - Read-only or special endpoint

   - Enum, length, range, pattern, and type validation- 🔧 **Hardware Required** - Requires physical hardware or specific licenses

   - Required field validation

   - Two-stage validation: required fields → field values---

   - Clear error messages with valid options

## 🔧 CMDB (Configuration Management Database)

## 📊 Detailed Coverage

### Implemented Categories (23 categories, 200+ endpoints)

### CMDB API - 886 Endpoints

#### 1. Alert Email (alertemail/)

Configuration management endpoints covering all FortiGate configuration objects:| Endpoint | Status | Methods | Notes |

|----------|--------|---------|-------|

**Major Categories** (examples):| `/cmdb/alertemail/setting` | 🔷 Beta | GET, PUT | Email alert configuration |

- **Firewall**: ~150 endpoints (addresses, policies, schedules, shapers, VIPs, etc.)

- **System**: ~120 endpoints (interfaces, admin, SNMP, DNS, NTP, etc.)#### 2. Antivirus (antivirus/)

- **User**: ~30 endpoints (local users, LDAP, RADIUS, groups, etc.)| Endpoint | Status | Methods | Notes |

- **VPN**: ~40 endpoints (IPsec, SSL-VPN, L2TP, PPTP, etc.)|----------|--------|---------|-------|

- **Router**: ~60 endpoints (static, policy routes, BGP, OSPF, RIP, etc.)| `/cmdb/antivirus/profile` | 🔷 Beta | GET, POST, PUT, DELETE | Antivirus profiles |

- **Switch-Controller**: ~80 endpoints (managed switches, VLANs, QoS, etc.)| `/cmdb/antivirus/settings` | 🔷 Beta | GET, PUT | Global AV settings |

- **Wireless-Controller**: ~70 endpoints (WTPs, VAPs, profiles, etc.)| `/cmdb/antivirus/quarantine` | 🔷 Beta | GET, POST, PUT, DELETE | Quarantine configuration |

- **WAF**: ~25 endpoints (web application firewall profiles)| `/cmdb/antivirus/exempt-list` | 🔷 Beta | GET, POST, PUT, DELETE | AV exemption list |

- **Security**: ~50 endpoints (IPS, Application Control, Web Filter, etc.)

- **Log**: ~30 endpoints (syslog, FortiAnalyzer, disk/memory settings, etc.)#### 3. Application (application/)

| Endpoint | Status | Methods | Notes |

**All Endpoint Types**:|----------|--------|---------|-------|

- Multi-value endpoints (lists): GET (all), GET (specific), POST, PUT, DELETE| `/cmdb/application/name` | 🔷 Beta | GET | Read-only application database |

- Singleton endpoints (global config): GET, PUT| `/cmdb/application/list` | 🔷 Beta | GET, POST, PUT, DELETE | Application filter lists |

- Special operations: move (policy reordering), clone, etc.| `/cmdb/application/group` | 🔷 Beta | GET, POST, PUT, DELETE | Application groups |

| `/cmdb/application/custom` | 🔷 Beta | GET, POST, PUT, DELETE | Custom applications |

### Monitor API - 295 Endpoints

#### 4. Authentication (authentication/)

Monitoring and status endpoints for real-time FortiGate state:| Endpoint | Status | Methods | Notes |

|----------|--------|---------|-------|

**Major Categories** (examples):| `/cmdb/authentication/scheme` | 🔷 Beta | GET, POST, PUT, DELETE | Auth schemes |

- **System**: ~60 endpoints (resources, performance, interfaces, etc.)| `/cmdb/authentication/rule` | 🔷 Beta | GET, POST, PUT, DELETE | Auth rules |

- **Firewall**: ~40 endpoints (sessions, policies stats, shaper stats, etc.)| `/cmdb/authentication/setting` | 🔷 Beta | GET, PUT | Global auth settings |

- **VPN**: ~25 endpoints (IPsec status, SSL-VPN sessions, tunnels, etc.)

- **Router**: ~30 endpoints (routing table, BGP neighbors, OSPF neighbors, etc.)#### 5. Automation (automation/)

- **User**: ~15 endpoints (firewall users, banned users, quarantine, etc.)| Endpoint | Status | Methods | Notes |

- **WiFi**: ~20 endpoints (client status, rogue APs, spectral analysis, etc.)|----------|--------|---------|-------|

- **Switch**: ~25 endpoints (managed switch status, VLANs, ACLs, etc.)| `/cmdb/automation/setting` | 🔷 Beta | GET, PUT | Automation configuration |

- **Endpoint**: ~15 endpoints (FortiClient EMS, endpoint compliance, etc.)

- **UTM**: ~20 endpoints (virus logs, IPS events, web filter stats, etc.)#### 6. CASB (casb/)

- **License**: ~10 endpoints (license status, VM license, FortiGuard services, etc.)| Endpoint | Status | Methods | Notes |

|----------|--------|---------|-------|

**Common Operations**:| `/cmdb/casb/saas-application` | 🔷 Beta | GET, POST, PUT, DELETE | SaaS app definitions |

- GET (retrieve status/statistics)| `/cmdb/casb/user-activity` | 🔷 Beta | GET, POST, PUT, DELETE | User activity controls |

- POST (trigger actions like disconnect session, clear counters, etc.)| `/cmdb/casb/profile` | 🔷 Beta | GET, POST, PUT, DELETE | CASB profiles |

| `/cmdb/casb/attribute-match` | 🔷 Beta | GET | Attribute matching |

### Log API - 38 Endpoints

#### 7. Certificate (certificate/)

Parameterized log query endpoints for all log types:| Endpoint | Status | Methods | Notes |

|----------|--------|---------|-------|

**Log Destinations** (5):| `/cmdb/certificate/ca` | 🔷 Beta | GET | CA certificates (read-only, imported via GUI/CLI) |

- `log.disk.*` - Logs stored on local disk| `/cmdb/certificate/local` | 🔷 Beta | GET | Local certificates (read-only, imported via GUI/CLI) |

- `log.memory.*` - Logs in RAM (buffer)| `/cmdb/certificate/remote` | 🔷 Beta | GET | Remote certificates (read-only, imported via GUI/CLI) |

- `log.fortianalyzer.*` - Logs on FortiAnalyzer| `/cmdb/certificate/crl` | 🔷 Beta | GET | Certificate revocation lists (read-only) |

- `log.forticloud.*` - Logs in FortiCloud| `/cmdb/certificate/hsm-local` | 🔷 Beta | GET, POST, PUT, DELETE | HSM-stored certificates (full CRUD) |

- `log.search.*` - Search across all destinations

#### 8. Diameter Filter (diameter_filter/)

**Event Log Subtypes** (12):| Endpoint | Status | Methods | Notes |

- `event.vpn` - VPN connection events|----------|--------|---------|-------|

- `event.user` - User authentication events| `/cmdb/diameter-filter/profile` | 🔷 Beta | GET, POST, PUT, DELETE | Diameter filter profiles |

- `event.system` - System events

- `event.ha` - High Availability events#### 9. DLP (dlp/) - 🔷 Beta (8 endpoints)

- `event.router` - Routing events| Endpoint | Status | Methods | Notes |

- `event.wireless` - Wireless events|----------|--------|---------|-------|

- `event.wad` - Web proxy events| `/cmdb/dlp/data-type` | 🔷 Beta | GET, POST, PUT, DELETE | Predefined data type patterns |

- `event.endpoint` - FortiClient endpoint events| `/cmdb/dlp/dictionary` | 🔷 Beta | GET, POST, PUT, DELETE | Custom DLP dictionaries |

- `event.fortiextender` - FortiExtender events| `/cmdb/dlp/exact-data-match` | 🔷 Beta | GET, POST, PUT, DELETE | Fingerprinting for exact data matching |

- `event.connector` - Connector events| `/cmdb/dlp/filepattern` | 🔷 Beta | GET, POST, PUT, DELETE | File type and pattern matching |

- `event.compliance_check` - Compliance check events| `/cmdb/dlp/label` | 🔷 Beta | GET, POST, PUT, DELETE | Classification labels |

- `event.security_rating` - Security rating events| `/cmdb/dlp/profile` | 🔷 Beta | GET, POST, PUT, DELETE | DLP policy profiles |

| `/cmdb/dlp/sensor` | 🔷 Beta | GET, POST, PUT, DELETE | DLP sensor configuration |

**Traffic Log Subtypes** (6):| `/cmdb/dlp/settings` | 🔷 Beta | GET, PUT | Global DLP settings |

- `traffic.forward` - Forward traffic logs

- `traffic.local` - Local-in/local-out traffic#### 10. DNS Filter (dnsfilter/) - 🔷 Beta (2 endpoints)

- `traffic.multicast` - Multicast traffic| Endpoint | Status | Methods | Notes |

- `traffic.sniffer` - Sniffer/packet capture|----------|--------|---------|-------|

- `traffic.fortiview` - FortiView traffic logs| `/cmdb/dnsfilter/domain-filter` | 🔷 Beta | GET, POST, PUT, DELETE | Custom domain filtering lists |

- `traffic.threat` - Threat traffic logs| `/cmdb/dnsfilter/profile` | 🔷 Beta | GET, POST, PUT, DELETE | DNS filtering profiles |



**Query Parameters**:#### 11. Email Filter (emailfilter/) - 🔷 Beta (8 endpoints)

- `rows` - Number of log entries to retrieve| Endpoint | Status | Methods | Notes |

- `filter` - FortiOS filter syntax (e.g., `srcip==10.0.0.1`)|----------|--------|---------|-------|

- `session_id` - Session identifier for pagination| `/cmdb/emailfilter/block-allow-list` | 🔷 Beta | GET, POST, PUT, DELETE | Email sender block/allow lists |

| `/cmdb/emailfilter/bword` | 🔷 Beta | GET, POST, PUT, DELETE | Banned word filtering |

**Example Usage**:| `/cmdb/emailfilter/dnsbl` | 🔷 Beta | GET, POST, PUT, DELETE | DNS-based blacklist checking |

| `/cmdb/emailfilter/fortishield` | 🔷 Beta | GET, POST, PUT, DELETE | FortiShield spam filtering |

```python| `/cmdb/emailfilter/iptrust` | 🔷 Beta | GET, POST, PUT, DELETE | Trusted IP addresses |

# Get VPN event logs from disk| `/cmdb/emailfilter/mheader` | 🔷 Beta | GET, POST, PUT, DELETE | Email header filtering rules |

vpn_logs = fgt.api.log.disk.event.vpn.get(| `/cmdb/emailfilter/options` | 🔷 Beta | GET, PUT | Global email filter options |

    rows=50,| `/cmdb/emailfilter/profile` | 🔷 Beta | GET, POST, PUT, DELETE | Email filtering profiles |

    filter="user=='john.doe'"

)#### 12. Endpoint Control (endpoint-control/) - 🔷 Beta (3 endpoints)

| Endpoint | Status | Methods | Notes |

# Get forward traffic from memory|----------|--------|---------|-------|

traffic = fgt.api.log.memory.traffic.forward.get(| `/cmdb/endpoint-control/fctems` | 🔷 Beta | GET, PUT | FortiClient EMS integration (pre-allocated slots) |

    rows=100,| `/cmdb/endpoint-control/fctems-override` | 🔷 Beta | GET, PUT | EMS override configurations |

    filter="dstip==192.168.1.100"| `/cmdb/endpoint-control/settings` | 🔷 Beta | GET, PUT | Endpoint control settings |

)

#### 13. Ethernet OAM (ethernet-oam/) - 🔧 Hardware Required (1 endpoint)

# Search across all destinations| Endpoint | Status | Methods | Notes |

results = fgt.api.log.search.event.system.get(|----------|--------|---------|-------|

    rows=200,| `/cmdb/ethernet-oam/cfm` | 🔧 Hardware | GET, POST, PUT, DELETE | Connectivity Fault Management (requires physical FortiGate) |

    filter="subtype=='admin'"

)#### 14. Extension Controller (extension-controller/) - 🔷 Beta (6 endpoints)

```| Endpoint | Status | Methods | Notes |

|----------|--------|---------|-------|

## 🎯 Access Patterns| `/cmdb/extension-controller/dataplan` | 🔷 Beta | GET, POST, PUT, DELETE | FortiExtender data plan configuration |

| `/cmdb/extension-controller/extender` | 🔷 Beta | GET, POST, PUT, DELETE | FortiExtender controller settings |

All endpoints follow consistent patterns:| `/cmdb/extension-controller/extender-profile` | 🔷 Beta | GET, POST, PUT, DELETE | FortiExtender profiles |

| `/cmdb/extension-controller/extender-vap` | 🔷 Beta | GET, POST, PUT, DELETE | FortiExtender WiFi VAP |

```python| `/cmdb/extension-controller/fortigate` | 🔷 Beta | GET, POST, PUT, DELETE | FortiGate controller configuration |

# CMDB (Configuration)| `/cmdb/extension-controller/fortigate-profile` | 🔷 Beta | GET, POST, PUT, DELETE | FortiGate connector profiles |

fgt.api.cmdb.{category}.{endpoint}.{method}()

#### 15. File Filter (file-filter/) - 🔷 Beta (1 endpoint)

# Monitor (Status/Stats)| Endpoint | Status | Methods | Notes |

fgt.api.monitor.{category}.{endpoint}.{method}()|----------|--------|---------|-------|

| `/cmdb/file-filter/profile` | 🔷 Beta | GET, POST, PUT, DELETE | File content filtering profiles |

# Log (Query)

fgt.api.log.{destination}.{log_type}.{subtype}.get()#### 16. Firewall (firewall/) - 🔷 Beta (29 endpoints)

```| Endpoint | Status | Methods | Notes |

|----------|--------|---------|-------|

**Examples**:| **DoS-policy** | 🔷 Beta | GET, POST, PUT, DELETE | IPv4 DoS protection policies |

| **DoS-policy6** | 🔷 Beta | GET, POST, PUT, DELETE | IPv6 DoS protection policies |

```python| **access-proxy** | 🔷 Beta | GET, POST, PUT, DELETE | IPv4 reverse proxy/WAF |

# Configuration endpoints| **access-proxy6** | 🔷 Beta | GET, POST, PUT, DELETE | IPv6 reverse proxy/WAF |

fgt.api.cmdb.firewall.address.get()| **access-proxy-ssh-client-cert** | 🔷 Beta | GET, POST, PUT, DELETE | SSH client certificates |

fgt.api.cmdb.firewall.policy.create(...)| **access-proxy-virtual-host** | 🔷 Beta | GET, POST, PUT, DELETE | Virtual host configuration |

fgt.api.cmdb.system.interface.update(name="wan1", ...)| **ipmacbinding/setting** | 🔷 Beta | GET, PUT | IP/MAC binding settings |

fgt.api.cmdb.user.local.delete(name="user1")| **ipmacbinding/table** | 🔷 Beta | GET, POST, PUT, DELETE | IP/MAC binding table |

| **schedule/group** | 🔷 Beta | GET, POST, PUT, DELETE | Schedule groups |

# Monitor endpoints| **schedule/onetime** | 🔷 Beta | GET, POST, PUT, DELETE | One-time schedules |

fgt.api.monitor.firewall.session.get()| **schedule/recurring** | 🔷 Beta | GET, POST, PUT, DELETE | Recurring schedules |

fgt.api.monitor.system.resource.usage.get()| **service/category** | 🔷 Beta | GET, POST, PUT, DELETE | Service categories |

fgt.api.monitor.router.bgp.neighbors.get()| **service/custom** | 🔷 Beta | GET, POST, PUT, DELETE | Custom services |

| **service/group** | 🔷 Beta | GET, POST, PUT, DELETE | Service groups |

# Log endpoints| **shaper/per-ip-shaper** | 🔷 Beta | GET, POST, PUT, DELETE | Per-IP traffic shaper |

fgt.api.log.disk.event.vpn.get(rows=50)| **shaper/traffic-shaper** | 🔷 Beta | GET, POST, PUT, DELETE | Shared traffic shaper |

fgt.api.log.memory.traffic.forward.get(rows=100)| **ssh/host-key** | 🔷 Beta | GET, POST, PUT, DELETE | SSH proxy host keys |

```| **ssh/local-ca** | 🔷 Beta | GET, POST, PUT, DELETE | SSH proxy local CA |

| **ssh/local-key** | 🔷 Beta | GET, POST, PUT, DELETE | SSH proxy local keys |

## 📝 Type Stub Coverage| **ssh/setting** | 🔷 Beta | GET, PUT | SSH proxy settings |

| **ssl/setting** | 🔷 Beta | GET, PUT | SSL proxy settings |

**100% Type Stub Coverage** - All 1,219 endpoints have complete `.pyi` stub files:| **wildcard-fqdn/custom** | 🔷 Beta | GET, POST, PUT, DELETE | Wildcard FQDN addresses |

| **wildcard-fqdn/group** | 🔷 Beta | GET, POST, PUT, DELETE | Wildcard FQDN groups |

- Full method signatures with type hints

- Parameter types and return types**Sub-categories Implemented:** 7 (ipmacbinding, schedule, service, shaper, ssh, ssl, wildcard-fqdn)  

- Optional vs required parameters**Flat Endpoints Implemented:** 6 (DoS-policy, DoS-policy6, access-proxy, access-proxy6, access-proxy-ssh-client-cert, access-proxy-virtual-host)  

- Docstrings with descriptions**Test Coverage:** 186 tests (100% pass rate)  

- Perfect IDE autocomplete support**Pattern:**

- Nested: `fgt.api.cmdb.firewall.[subcategory].[endpoint]`

**Example**:- Flat: `fgt.api.cmdb.firewall.[endpoint]`



```python**Key Features:**

# Your IDE will show complete type information:- Simplified API with automatic type conversion

result = fgt.api.cmdb.firewall.address.create(- DoS policies include comprehensive anomaly detection (18 types)

    name: str,              # Required- Access-proxy supports reverse proxy/WAF with VIP integration

    subnet: str | None,     # Optional (IP/netmask)- All endpoints lazy-loaded via @property pattern

    type: str | None,       # Optional (ipmask, iprange, fqdn, etc.)

    comment: str | None,    # Optional**Remaining Firewall Endpoints (83):**

    vdom: str | None        # Optional (default: 'root')- address, address6, addrgrp, addrgrp6 - Address management

) -> dict[str, Any]- policy, security-policy - Policy configuration

```- vip, vip6, vipgrp, vipgrp6 - Virtual IP configuration

- ippool, ippool6 - IP pool configuration

## ✅ Validation Coverage- proxy-address, proxy-addrgrp, proxy-policy - Proxy configuration

- interface-policy, interface-policy6 - Interface policies

**100% Validator Coverage** - All 1,219 endpoints have schema-based validators:- local-in-policy, local-in-policy6 - Local-in policies

- multicast-address, multicast-policy - Multicast configuration

1. **Required Field Validation**:- ssl-server, ssl-ssh-profile - SSL/SSH profiles

   - Validates all required fields are present- And 60+ more endpoints...

   - Clear error messages listing missing fields

#### 17. FTP Proxy (ftp-proxy/) - 🔷 Beta (1 endpoint)

2. **Value Validation**:| Endpoint | Status | Methods | Notes |

   - Enum validation (valid option lists)|----------|--------|---------|-------|

   - Range validation (min/max values)| `/cmdb/ftp-proxy/explicit` | 🔷 Beta | GET, PUT | Explicit FTP proxy configuration |

   - Length validation (string lengths)

   - Pattern validation (regex patterns)**Features:**

   - Type validation (string, integer, array, etc.)- Enable/disable explicit FTP proxy

- Configure incoming/outgoing IP and port

3. **Two-Stage Process**:- Security default action (accept/deny)

   - Stage 1: Check required fields- Server data mode (client/passive)

   - Stage 2: Validate field values- FTPS support with SSL configuration

- SSL certificate selection and DH bits

**Example**:- Singleton endpoint (no POST/DELETE)



```python#### 18. ICAP (icap/) - 🔷 Beta (3 endpoints)

# Automatic validation on create/update| Endpoint | Status | Methods | Notes |

result = fgt.api.cmdb.firewall.address.create(|----------|--------|---------|-------|

    name="test",| `/cmdb/icap/profile` | 🔷 Beta | GET, POST, PUT, DELETE | ICAP profiles with 30+ parameters |

    type="invalid-type"  # ← ValidationError| `/cmdb/icap/server` | 🔷 Beta | GET, POST, PUT, DELETE | ICAP server configuration |

)| `/cmdb/icap/server-group` | 🔷 Beta | GET, POST, PUT, DELETE | ICAP server groups |



# Error message shows valid options:**Features:**

# "Field 'type' has invalid value 'invalid-type'.- Complete parameter coverage from FortiOS 7.6.5 API

#  Valid options: ['ipmask', 'iprange', 'fqdn', 'geography', ...]"- Request/response modification support

```- SSL/TLS ICAP connections

- Preview, streaming, and bypass options

## 🧪 Test Coverage

#### 19. IPS (ips/) - 🔷 Beta (8 endpoints)

**1,200+ Auto-Generated Tests** - Basic smoke tests for all endpoints:| Endpoint | Status | Methods | Notes |

|----------|--------|---------|-------|

**Test Types**:| `/cmdb/ips/custom` | 🔷 Beta | GET, POST, PUT, DELETE | Custom IPS signatures |

- GET operations (list all, get specific)| `/cmdb/ips/decoder` | 🔷 Beta | GET, POST, PUT, DELETE | Protocol decoders |

- VDOM parameter testing| `/cmdb/ips/global` | 🔷 Beta | GET, PUT | Global IPS settings (singleton) |

- Filter parameter testing (CMDB)| `/cmdb/ips/rule` | 🔷 Beta | GET, POST, PUT, DELETE | IPS rules |

- exists() method testing| `/cmdb/ips/rule-settings` | 🔷 Beta | GET, POST, PUT, DELETE | IPS rule settings |

- Validator import testing| `/cmdb/ips/sensor` | 🔷 Beta | GET, POST, PUT, DELETE | IPS sensors (main profiles) |

- Enum validation testing| `/cmdb/ips/settings` | 🔷 Beta | GET, PUT | VDOM IPS settings (singleton) |

| `/cmdb/ips/view-map` | 🔷 Beta | GET, POST, PUT, DELETE | IPS view-map configuration |

**Test Structure**:

**Features:**

```- Custom signature creation

.tests/pytests/api/- Protocol decoder configuration

├── cmdb/- Sensor-based IPS profiles

│   ├── firewall/- Rate-based and anomaly-based detection

│   │   ├── auto_test_address.py

│   │   ├── auto_test_policy.py#### 20. Log (log/) - 🔷 Beta (56 endpoints)

│   │   └── ...| Endpoint | Status | Methods | Notes |

│   └── ...|----------|--------|---------|-------|

├── monitor/| **disk/filter** | 🔷 Beta | GET, PUT | Disk log filtering (12 params) |

│   └── ...| **disk/setting** | 🔷 Beta | GET, PUT | Disk log settings (28 params) |

└── log/| **memory/filter** | 🔷 Beta | GET, PUT | Memory log filtering (12 params) |

    ├── test_disk.py| **memory/global-setting** | 🔷 Beta | GET, PUT | Memory log global settings (4 params) |

    ├── test_memory.py| **memory/setting** | 🔷 Beta | GET, PUT | Memory log settings (1 param) |

    └── ...| **fortianalyzer-cloud/filter** | 🔷 Beta | GET, PUT | FortiAnalyzer Cloud log filter |

```| **fortianalyzer-cloud/override-filter** | 🔷 Beta | GET, PUT | FAC override filter |

| **fortianalyzer-cloud/override-setting** | 🔷 Beta | GET, PUT | FAC override settings |

**Running Tests**:| **fortianalyzer-cloud/setting** | 🔷 Beta | GET, PUT | FAC log settings |

| **fortianalyzer/filter** | 🔷 Beta | GET, PUT | FortiAnalyzer log filter |

```bash| **fortianalyzer/override-filter** | 🔷 Beta | GET, PUT | FA override filter |

# Test specific endpoint| **fortianalyzer/override-setting** | 🔷 Beta | GET, PUT | FA override settings |

pytest .tests/pytests/api/cmdb/firewall/auto_test_address.py| **fortianalyzer/setting** | 🔷 Beta | GET, PUT | FA log settings |

| **fortianalyzer2/** | 🔷 Beta | GET, PUT | FortiAnalyzer 2 (4 endpoints) |

# Test all CMDB| **fortianalyzer3/** | 🔷 Beta | GET, PUT | FortiAnalyzer 3 (4 endpoints) |

pytest .tests/pytests/api/cmdb/| **fortiguard/filter** | 🔷 Beta | GET, PUT | FortiGuard log filter |

| **fortiguard/override-filter** | 🔷 Beta | GET, PUT | FG override filter |

# Test all| **fortiguard/override-setting** | 🔷 Beta | GET, PUT | FG override settings |

pytest .tests/pytests/| **fortiguard/setting** | 🔷 Beta | GET, PUT | FG log settings |

```| **null-device/filter** | 🔷 Beta | GET, PUT | Null device log filter (12 params) |

| **null-device/setting** | 🔷 Beta | GET, PUT | Null device settings (1 param) |

## 🔄 Generator Architecture| **syslogd/filter** | 🔷 Beta | GET, PUT | Syslog filter (12 params) |

| **syslogd/override-filter** | 🔷 Beta | GET, PUT | Syslog override filter (12 params) |

The v0.5.0 generator is a complete rewrite with modular architecture:| **syslogd/override-setting** | 🔷 Beta | GET, PUT | Syslog override settings (18 params) |

| **syslogd/setting** | 🔷 Beta | GET, PUT | Syslog settings (17 params) |

**Components**:| **syslogd2/** | 🔷 Beta | GET, PUT | Syslog server 2 (4 endpoints) |

| **syslogd3/** | 🔷 Beta | GET, PUT | Syslog server 3 (4 endpoints) |

1. **Schema Downloader** (`download_schemas.py`):| **syslogd4/** | 🔷 Beta | GET, PUT | Syslog server 4 (4 endpoints) |

   - Downloads schemas from FortiGate API| **tacacs+accounting/filter** | 🔷 Beta | GET, PUT | TACACS+ accounting filter (3 params) |

   - Implements Swagger fallback for unavailable endpoints| **tacacs+accounting/setting** | 🔷 Beta | GET, PUT | TACACS+ accounting settings (7 params) |

   - Handles HTTP errors and JSON parse errors| **tacacs+accounting2/** | 🔷 Beta | GET, PUT | TACACS+ server 2 (2 endpoints) |

   - Tracks metadata (source, timestamp, fallback reason)| **tacacs+accounting3/** | 🔷 Beta | GET, PUT | TACACS+ server 3 (2 endpoints) |

| **webtrends/filter** | 🔷 Beta | GET, PUT | WebTrends log filter (12 params) |

2. **Schema Parser** (`schema_parser.py`):| **webtrends/setting** | 🔷 Beta | GET, PUT | WebTrends settings (2 params) |

   - Parses JSON schemas into structured format| **custom-field** | 🔷 Beta | GET, POST, PUT, DELETE | Custom log fields (CRUD) |

   - Extracts fields, types, options, required fields| **eventfilter** | 🔷 Beta | GET, PUT | Event filter configuration (17 params) |

   - Identifies multi-key vs singleton endpoints| **gui-display** | 🔷 Beta | GET, PUT | GUI display settings (3 params) |

   - Handles all edge cases| **setting** | 🔷 Beta | GET, PUT | General log settings (29 params) |

| **threat-weight** | 🔷 Beta | GET, PUT | Threat weight settings (11 params) |

3. **Endpoint Generator** (`generators/endpoint_generator.py`):

   - Generates endpoint classes from schemas**Architecture:**

   - Creates methods: get(), create(), update(), delete(), exists(), move()- **Nested object pattern** for sub-categories: `fgt.api.cmdb.log.disk.filter.get()`

   - Handles all HTTP methods and special operations- **51 nested endpoints** across 9 intermediate classes

- **5 singleton endpoints** at root level

4. **Validator Generator** (`generators/validator_generator.py`):- Test Coverage: 12 test files, 47 test cases (100% pass rate)

   - Generates validation functions from schemas

   - Implements enum, range, length, pattern validation**Key Features:**

   - Two-stage validation logic- Multiple FortiAnalyzer server support (1/2/3)

- Multiple syslog server support (1/2/3/4)

5. **Type Stub Generator** (`generators/pyi_generator.py`):- Multiple TACACS+ accounting server support (1/2/3)

   - Generates `.pyi` stub files for all endpoints- Custom field management for log enrichment

   - Creates validator stubs- Comprehensive filtering and override capabilities

   - Full type hints and docstrings

#### 21. Monitoring (monitoring/) - 🔷 Beta (1 endpoint)

6. **Test Generator** (`helpers/generate_tests.py`):| Endpoint | Status | Methods | Notes |

   - Generates basic smoke tests|----------|--------|---------|-------|

   - Template-based test creation| `/cmdb/monitoring/npu-hpe` | 🔷 Beta | GET, PUT | NPU-HPE monitoring configuration (3 params) |

   - Covers all common operations

**Features:**

7. **Log Generator** (`generators/log_generator.py`):- NPU-HPE performance monitoring settings

   - Specialized generator for parameterized log endpoints- Interval, multipliers, and status configuration

   - Creates nested class structure- Requires hardware NPU support

   - Handles all destinations and subtypes

#### 22. Report (report/) - 🔷 Beta (2 endpoints)

**Template Engine**:| Endpoint | Status | Methods | Notes |

- Jinja2 templates for all code generation|----------|--------|---------|-------|

- Templates in `.dev/generator/templates/`| `/cmdb/report/layout` | 🔷 Beta | GET, POST, PUT, DELETE | Report layouts with CRUD (17 params) |

- Consistent code style across all endpoints| `/cmdb/report/setting` | 🔷 Beta | GET, PUT | Report settings (5 params) |



## 📈 Statistics**Features:**

- Custom report layout creation

- **Total Endpoints**: 1,219- Email scheduling support

- **Type Stubs**: 1,219 `.pyi` files- PDF report generation

- **Validators**: 1,219 validator modules- FortiView and web browsing report settings

- **Tests**: 1,200+ test files

- **Lines of Code**: ~500,000 (auto-generated)---

- **Generator Success Rate**: 100% (0 failures with Swagger fallback)

- **Generation Time**: ~10-15 minutes (0.2s delay per endpoint)### Not Yet Implemented (16 Categories Remaining)



## 🚧 Beta Status**FortiOS 7.6.5 CMDB Categories Not Yet Implemented:**



All implementations remain in **BETA** until version 1.0.0:<details>

<summary><strong>Click to expand full list of remaining CMDB categories</strong></summary>

- APIs are functional and tested

- May have incomplete parameter coverage for some endpoints1. **rule** - Traffic shaping and QoS rules

- Edge cases may exist2. **sctp-filter** - Stream Control Transmission Protocol filtering

- Feedback welcome via GitHub issues3. **ssh-filter** - SSH protocol filtering

4. **switch-controller** - FortiSwitch management and configuration

**Roadmap to v1.0.0**:5. **system** - 🔥 **HIGH PRIORITY** - System-wide settings (admin, interface, zone, HA, etc.)

1. Expand test coverage (currently basic smoke tests)6. **telemetry-controller** - Telemetry and monitoring integration

2. Add integration tests7. **user** - 🔥 **HIGH PRIORITY** - User authentication and LDAP/RADIUS servers

3. Community testing and feedback8. **videofilter** - Video streaming filtering

4. Bug fixes and edge case handling9. **virtual-patch** - Virtual patching for vulnerabilities

5. Performance optimization10. **voip** - VoIP inspection and SIP configuration

6. Documentation enhancements11. **vpn** - 🔥 **HIGH PRIORITY** - VPN configuration (IPsec, SSL-VPN, tunnels)

12. **waf** - Web Application Firewall profiles

## 📚 Related Documentation13. **wanopt** - WAN optimization configuration

14. **web-proxy** - Explicit web proxy configuration

- **[README.md](../../README.md)** - Main project documentation15. **webfilter** - 🔥 **HIGH PRIORITY** - Web filtering and URL categories

- **[QUICKSTART.md](../../QUICKSTART.md)** - Quick start guide16. **wireless-controller** - FortiAP wireless management

- **[CHANGELOG.md](../../CHANGELOG.md)** - Version history17. **ztna** - Zero Trust Network Access configuration

- **[MIGRATION_v0.5.0.md](../../MIGRATION_v0.5.0.md)** - Migration guide from v0.4.x

- **[VALIDATION_GUIDE.md](VALIDATION_GUIDE.md)** - Validation documentation**Note:** All 24 implemented CMDB categories are in beta status.

- **[ENDPOINT_METHODS.md](ENDPOINT_METHODS.md)** - Endpoint method documentation

---

## 🔗 Previous Version

## 📝 Configuration API (CMDB) - Complete List

For v0.4.x API coverage, see [API_COVERAGE_v0.4.md](API_COVERAGE_v0.4.md).

**FortiOS 7.6.5 Configuration API - All 40 Categories:**

| # | Category | Status | Notes |
|---|----------|--------|-------|
| 1 | alertemail | 🔷 Beta | Email alerts |
| 2 | antivirus | 🔷 Beta | Antivirus profiles |
| 3 | application | 🔷 Beta | Application control |
| 4 | authentication | 🔷 Beta | Authentication schemes |
| 5 | automation | 🔷 Beta | Automation stitch |
| 6 | casb | 🔷 Beta | CASB profiles |
| 7 | certificate | 🔷 Beta | Certificate management |
| 8 | diameter-filter | 🔷 Beta | Diameter filtering |
| 9 | dlp | 🔷 Beta | Data loss prevention |
| 10 | dnsfilter | 🔷 Beta | DNS filtering |
| 11 | emailfilter | 🔷 Beta | Email filtering |
| 12 | endpoint-control | 🔷 Beta | Endpoint control |
| 13 | ethernet-oam | 🔷 Beta | Ethernet OAM |
| 14 | extension-controller | 🔷 Beta | FortiExtender |
| 15 | file-filter | 🔷 Beta | File filtering |
| 16 | firewall | 🔷 Beta | Firewall objects & policies |
| 17 | ftp-proxy | 🔷 Beta | FTP proxy |
| 18 | icap | 🔷 Beta | ICAP integration |
| 19 | ips | 🔷 Beta | IPS sensors |
| 20 | log | 🔷 Beta | Log configuration |
| 21 | monitoring | 🔷 Beta | Monitoring config |
| 22 | report | 🔷 Beta | Report configuration |
| 23 | router | 🔷 Beta | Routing protocols (⚠️ singleton pattern) |
| 24 | rule | ⏸️ Not Started | Traffic rules |
| 25 | sctp-filter | ⏸️ Not Started | SCTP filtering |
| 26 | ssh-filter | ⏸️ Not Started | SSH filtering |
| 27 | switch-controller | ⏸️ Not Started | FortiSwitch |
| 28 | system | ⏸️ Not Started | System settings |
| 29 | telemetry-controller | ⏸️ Not Started | Telemetry |
| 30 | user | ⏸️ Not Started | User management |
| 31 | videofilter | ⏸️ Not Started | Video filtering |
| 32 | virtual-patch | ⏸️ Not Started | Virtual patching |
| 33 | voip | ⏸️ Not Started | VoIP profiles |
| 34 | vpn | ⏸️ Not Started | VPN configuration |
| 35 | waf | ⏸️ Not Started | WAF profiles |
| 36 | wanopt | ⏸️ Not Started | WAN optimization |
| 37 | web-proxy | ⏸️ Not Started | Web proxy |
| 38 | webfilter | ⏸️ Not Started | Web filtering |
| 39 | wireless-controller | ⏸️ Not Started | FortiAP |
| 40 | ztna | ⏸️ Not Started | ZTNA |

**Implementation Status:**
- 🔷 **Beta (Implemented):** 24 categories (60.0%)
- ⏸️ **Not Started:** 16 categories (40.0%)

**Note:** All implemented categories remain in beta status until v1.0.0 with comprehensive unit test coverage.

---

## 📊 Log API - FortiOS 7.6.5

**Status:** 🔷 Beta - 5 of 5 categories implemented (100%)

| # | Category | Status | Notes |
|---|----------|--------|-------|
| 1 | disk | 🔷 Beta | Read logs from disk |
| 2 | fortianalyzer | 🔷 Beta | Read logs from FortiAnalyzer |
| 3 | memory | 🔷 Beta | Read logs from memory |
| 4 | forticloud | 🔷 Beta | Read logs from FortiCloud |
| 5 | search | 🔷 Beta | Log search sessions |

**Note:** The `/log/*` API endpoints are for **reading logs**, not configuring logging. For logging configuration, use `/cmdb/log/*` endpoints (already implemented - see category #19 above). All endpoints remain in beta until v1.0.0.

---

## 🔍 Monitor API - FortiOS 7.6.5

**Status:** 🔷 Beta - 6 of 33 categories implemented (18%)

### Implemented Categories (6 categories, 39+ endpoints)

#### 1. Azure (azure/)
| Endpoint | Status | Methods | Notes |
|----------|--------|---------|-------|
| `/monitor/azure/application-list` | 🔷 Beta | GET | List Azure applications |

#### 2. CASB (casb/)
| Endpoint | Status | Methods | Notes |
|----------|--------|---------|-------|
| `/monitor/casb/saas-application` | 🔷 Beta | GET | SaaS application statistics |

#### 3. Endpoint Control (endpoint-control/)
| Endpoint | Status | Methods | Notes |
|----------|--------|---------|-------|
| `/monitor/endpoint-control/ems-status` | 🔷 Beta | GET | EMS connection status |
| `/monitor/endpoint-control/ems-status-summary` | 🔷 Beta | GET | EMS status summary |
| `/monitor/endpoint-control/installer` | 🔷 Beta | GET, POST | FortiClient installer management |
| `/monitor/endpoint-control/profile-xml` | 🔷 Beta | GET | FortiClient XML profiles |
| `/monitor/endpoint-control/record-list` | 🔷 Beta | GET | Endpoint control records |
| `/monitor/endpoint-control/registration-password` | 🔷 Beta | POST | Generate registration passwords |
| `/monitor/endpoint-control/summary` | 🔷 Beta | GET | Endpoint control summary |

#### 4. Extender Controller (extender-controller/)
| Endpoint | Status | Methods | Notes |
|----------|--------|---------|-------|
| `/monitor/extender-controller/extender` | 🔷 Beta | GET | FortiExtender status |

#### 5. Extension Controller (extension-controller/)
| Endpoint | Status | Methods | Notes |
|----------|--------|---------|-------|
| `/monitor/extension-controller/extender` | 🔷 Beta | GET | Extension controller status |
| `/monitor/extension-controller/fortigate` | 🔷 Beta | GET | FortiGate connector status |

#### 6. Firewall (firewall/) - 39 endpoints
| Endpoint | Status | Methods | Notes |
|----------|--------|---------|-------|
| `/monitor/firewall/acl` | 🔷 Beta | GET, POST | IPv4 ACL counters |
| `/monitor/firewall/acl6` | 🔷 Beta | GET, POST | IPv6 ACL counters |
| `/monitor/firewall/address` | 🔷 Beta | GET | Address objects statistics |
| `/monitor/firewall/address-dynamic` | 🔷 Beta | GET | Dynamic address statistics |
| `/monitor/firewall/address-fqdn` | 🔷 Beta | GET | FQDN address resolution |
| `/monitor/firewall/address-fqdn6` | 🔷 Beta | GET | IPv6 FQDN resolution |
| `/monitor/firewall/address6` | 🔷 Beta | GET | IPv6 address statistics |
| `/monitor/firewall/carrier-endpoint-bwl` | 🔷 Beta | GET | Carrier endpoint bandwidth limits |
| `/monitor/firewall/check-addrgrp-exclude-mac-member` | 🔷 Beta | GET | Check address group MAC exclusions |
| `/monitor/firewall/clearpass-address` | 🔷 Beta | POST | ClearPass address management |
| `/monitor/firewall/consolidate-policy` | 🔷 Beta | GET | Policy consolidation analysis |
| `/monitor/firewall/gtp-runtime-statistics` | 🔷 Beta | GET | GTP protocol statistics |
| `/monitor/firewall/gtp-statistics` | 🔷 Beta | GET | GTP statistics summary |
| `/monitor/firewall/health` | 🔷 Beta | GET | Firewall health status |
| `/monitor/firewall/internet-service-match` | 🔷 Beta | GET | Internet service matching |
| `/monitor/firewall/internet-service-reputation` | 🔷 Beta | GET | Internet service reputation |
| `/monitor/firewall/iprope` | 🔷 Beta | GET | IP reputation |
| `/monitor/firewall/load-balance` | 🔷 Beta | GET | Load balancing statistics |
| `/monitor/firewall/local-in` | 🔷 Beta | GET | Local-in policy statistics |
| `/monitor/firewall/local-in6` | 🔷 Beta | GET | IPv6 local-in statistics |
| `/monitor/firewall/multicast-policy` | 🔷 Beta | GET | Multicast policy statistics |
| `/monitor/firewall/multicast-policy6` | 🔷 Beta | GET | IPv6 multicast statistics |
| `/monitor/firewall/network-service-dynamic` | 🔷 Beta | GET | Dynamic network services |
| `/monitor/firewall/per-ip-shaper` | 🔷 Beta | GET, POST | Per-IP shaper statistics |
| `/monitor/firewall/policy` | 🔷 Beta | GET | Policy statistics |
| `/monitor/firewall/policy-lookup` | 🔷 Beta | GET (Callable) | Policy lookup by packet |
| `/monitor/firewall/policy6` | 🔷 Beta | GET | IPv6 policy statistics |
| `/monitor/firewall/proute` | 🔷 Beta | GET | Policy-based routing |
| `/monitor/firewall/proute6` | 🔷 Beta | GET | IPv6 policy routing |
| `/monitor/firewall/proxy-policy` | 🔷 Beta | GET | Proxy policy statistics |
| `/monitor/firewall/saas-application` | 🔷 Beta | GET | SaaS application statistics |
| `/monitor/firewall/sdn-connector-filters` | 🔷 Beta | GET | SDN connector filters |
| `/monitor/firewall/security-policy` | 🔷 Beta | GET | Security policy statistics |
| `/monitor/firewall/sessions` | 🔷 Beta | GET | Active firewall sessions |
| `/monitor/firewall/shaper` | 🔷 Beta | GET, POST | Traffic shaper statistics |
| `/monitor/firewall/shaper-multi-class-shaper` | 🔷 Beta | GET | Multi-class shaper stats |
| `/monitor/firewall/uuid` | 🔷 Beta | GET | UUID-based objects |
| `/monitor/firewall/vip-overlap` | 🔷 Beta | GET | VIP overlap detection |
| `/monitor/firewall/ztna-firewall-policy` | 🔷 Beta | POST | ZTNA policy counters |

**Test Coverage:** 39 test files with 100% pass rate

### Not Yet Implemented (27 categories)

| # | Category | Status | Notes |
|---|----------|--------|-------|
| 7 | firmware | ⏸️ Not Started | Firmware status |
| 8 | fortiguard | ⏸️ Not Started | FortiGuard services |
| 9 | fortiview | ⏸️ Not Started | FortiView data |
| 10 | geoip | ⏸️ Not Started | GeoIP database |
| 11 | ips | ⏸️ Not Started | IPS statistics |
| 12 | license | ⏸️ Not Started | License information |
| 13 | log | ⏸️ Not Started | Log statistics |
| 14 | network | ⏸️ Not Started | Network statistics |
| 15 | registration | ⏸️ Not Started | Device registration |
| 16 | router | ⏸️ Not Started | Routing tables |
| 17 | sdwan | ⏸️ Not Started | SD-WAN metrics |
| 18 | service | ⏸️ Not Started | Service status |
| 19 | switch-controller | ⏸️ Not Started | FortiSwitch monitoring |
| 20 | system | 🔷 Beta | System resources (partial via CMDB) |
| 21 | user | ⏸️ Not Started | Active users |
| 22 | utm | ⏸️ Not Started | UTM statistics |
| 23 | videofilter | ⏸️ Not Started | Video filter stats |
| 24 | virtual-wan | ⏸️ Not Started | Virtual WAN |
| 25 | vpn | ⏸️ Not Started | VPN status |
| 26 | vpn-certificate | ⏸️ Not Started | VPN certificates |
| 27 | wanopt | ⏸️ Not Started | WAN optimization |
| 28 | web-ui | ⏸️ Not Started | Web UI sessions |
| 29 | webcache | ⏸️ Not Started | Web cache stats |
| 30 | webfilter | ⏸️ Not Started | Web filter stats |
| 31 | webproxy | ⏸️ Not Started | Web proxy stats |
| 32 | wifi | ⏸️ Not Started | WiFi statistics |

**Note:** Monitor API category #20 (system) partially implemented via monitoring/npu-hpe configuration endpoint.

---

## ⚙️ Service API - FortiOS 7.6.5

**Status:** 🔷 Beta - 3 of 3 categories implemented (100%)

| # | Category | Status | Methods | Notes |
|---|----------|--------|---------|-------|
| 1 | sniffer | 🔷 Beta | GET, POST, DELETE | Packet capture |
| 2 | security-rating | 🔷 Beta | GET | Security Fabric rating |
| 3 | system | 🔷 Beta | Various | System operations (reboot, backup) |

**Note:** All service endpoints remain in beta until v1.0.0 with comprehensive unit test coverage.

---

## 📊 API Scope Summary

**FortiOS 7.6.5 Coverage Overview:**

| API Type | Implemented | Total Available | Coverage |
|----------|-------------|-----------------|----------|
| **Configuration (CMDB)** | 18 categories | 40 categories | 45% |
| **Monitoring** | 1 category (partial) | 33 categories | 3% |
| **Logging** | 5 categories | 5 categories | 100% |
| **Services** | 3 categories | 3 categories | 100% |
| **Overall** | **27 categories** | **77 categories** | **35%** |

**Endpoint Level Detail:**
- **CMDB Endpoints:** 150+ endpoints implemented across 18 categories
- **Log Endpoints:** 42 methods (configuration only)
- **Service Endpoints:** 21 methods  
- **Total Methods:** 200+ API methods available

**Recent Additions (v0.3.10-beta):**
- ✅ **Log category:** 56 endpoints with nested object pattern (disk, memory, fortianalyzer, syslogd, tacacs+, webtrends)
- ✅ **Monitoring category:** NPU-HPE configuration
- ✅ **Report category:** Layout management and settings
- ✅ **ICAP category:** Complete with 30+ parameters per endpoint
- ✅ **IPS category:** All 8 endpoints (custom signatures, sensors, decoders, rules)
- ✅ **Firewall category:** 29 endpoints with nested object pattern
- ✅ raw_json parameter added to all 200+ API methods
- ✅ Code quality: 100% PEP 8 compliance (black + isort + flake8)
- ✅ Comprehensive error handling with 387 error codes
- ✅ Full type hints and docstrings

---

## 🤝 Contributing

Want to help implement more endpoints? Contributions are welcome!

### How to Add Coverage

1. Check FortiOS API documentation for endpoint details
2. Implement endpoint following existing patterns
3. Test your implementation thoroughly
4. Update this file with implementation status
5. Update CHANGELOG.md
6. Submit a pull request
6. Submit pull request

---

## 📚 Resources

- [FortiOS REST API Guide](https://docs.fortinet.com/document/fortigate/7.6.0/administration-guide)
- [Fortinet Developer Network](https://fndn.fortinet.net)
- [API Reference](https://fndn.fortinet.net/index.php?/fortiapi/1-fortios/)

---

**Note:** This coverage map is for FortiOS 7.6.x. Some endpoints may vary in different FortiOS versions.
