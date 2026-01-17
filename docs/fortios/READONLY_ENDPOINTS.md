# Read-Only Endpoints

This document lists all FortiOS API endpoints that are marked as read-only.
These endpoints provide reference data and do not support POST, PUT, or DELETE operations.

**Generated:** 2026-01-17 18:39:32 UTC  
**Total Read-Only Endpoints:** 38

---

## Table of Contents

- [CMDB](#cmdb)

---

## CMDB

**Count:** 38 endpoints

| Path | Description | Primary Key |
|------|-------------|-------------|
| `application/name` | Configure application signatures. | `name` |
| `application/rule-settings` | Configure application rule settings. | `id` |
| `firewall/city` | Define city table. | `id` |
| `firewall/country` | Define country table. | `id` |
| `firewall/internet-service` | Show Internet Service application. | `id` |
| `firewall/internet-service-botnet` | Show Internet Service botnet. | `id` |
| `firewall/internet-service-ipbl-reason` | IP block list reason. | `id` |
| `firewall/internet-service-ipbl-vendor` | IP block list vendor. | `id` |
| `firewall/internet-service-list` | Internet Service list. | `id` |
| `firewall/internet-service-owner` | Internet Service owner. | `id` |
| `firewall/internet-service-reputation` | Show Internet Service reputation. | `id` |
| `firewall/internet-service-sld` | Internet Service Second Level Domain. | `id` |
| `firewall/internet-service-subapp` | Show Internet Service sub app ID. | `id` |
| `firewall/region` | Define region table. | `id` |
| `firewall/vendor-mac` | Show vendor and the MAC address they have. | `id` |
| `firewall/vendor-mac-summary` | Vendor MAC database summary. | `—` |
| `ips/decoder` | Configure IPS decoder. | `name` |
| `ips/rule` | Configure IPS rules. | `name` |
| `ips/rule-settings` | Configure IPS rule setting. | `id` |
| `ips/view-map` | Configure IPS view-map. | `id` |
| `rule/fmwp` | Show FMWP signatures. | `name` |
| `rule/iotd` | Show IOT detection signatures. | `name` |
| `rule/otdt` | Show OT detection signatures. | `name` |
| `rule/otvp` | Show OT patch signatures. | `name` |
| `system.replacemsg/admin` | Replacement messages. | `msg-type` |
| `system.replacemsg/alertmail` | Replacement messages. | `msg-type` |
| `system.replacemsg/auth` | Replacement messages. | `msg-type` |
| `system.replacemsg/automation` | Replacement messages. | `msg-type` |
| `system.replacemsg/fortiguard-wf` | Replacement messages. | `msg-type` |
| `system.replacemsg/http` | Replacement messages. | `msg-type` |
| `system.replacemsg/mail` | Replacement messages. | `msg-type` |
| `system.replacemsg/nac-quar` | Replacement messages. | `msg-type` |
| `system.replacemsg/spam` | Replacement messages. | `msg-type` |
| `system.replacemsg/sslvpn` | Replacement messages. | `msg-type` |
| `system.replacemsg/traffic-quota` | Replacement messages. | `msg-type` |
| `system.replacemsg/utm` | Replacement messages. | `msg-type` |
| `system/geoip-country` | Define geoip country name-ID table. | `id` |
| `system/timezone` | Show timezone. | `name` |

---

## Usage Notes

### Read-Only Endpoints

Read-only endpoints provide reference data that cannot be modified through the API:

- ✅ **GET** operations are supported
- ❌ **POST** operations are not supported (cannot create)
- ❌ **PUT** operations are not supported (cannot update)
- ❌ **DELETE** operations are not supported (cannot delete)

### Common Read-Only Endpoint Types

1. **Internet Service Tables**: FortiGuard-managed service definitions
   - `firewall/internet-service`
   - `firewall/internet-service-botnet`
   - `firewall/internet-service-reputation`

2. **Geographic Reference Data**: Country, city, and region information
   - `firewall/country`
   - `firewall/city`
   - `firewall/region`

3. **Vendor/Product References**: MAC address vendor lookups, etc.
   - `firewall/vendor-mac`
   - `firewall/vendor-mac-summary`

### Example Usage

```python
from hfortix_fortios import FortiOS

# Connect to FortiGate
fgt = FortiOS(host='192.168.1.99', token='your-token')

# Query read-only reference data
internet_services = fgt.api.cmdb.firewall.internet_service.get()

# Filter results
google_services = fgt.api.cmdb.firewall.internet_service.get(
    filter='name=@Google'
)

# These operations will fail (read-only):
# fgt.api.cmdb.firewall.internet_service.post(...)  # Not supported
# fgt.api.cmdb.firewall.internet_service.put(...)   # Not supported
```
