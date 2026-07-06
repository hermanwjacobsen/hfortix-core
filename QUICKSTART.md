# HFortix-Core — Quickstart

`hfortix-core` is the shared foundation of the HFortix ecosystem. It is
installed automatically as a dependency of the higher-level packages, and
most users should start there:

```bash
pip install hfortix-fortios        # FortiOS / FortiGate
pip install hfortix-fortimanager   # FortiManager
pip install hfortix-fortianalyzer  # FortiAnalyzer
pip install hfortix-forticare      # FortiCare asset management
pip install hfortix-fortiztp       # FortiZTP provisioning
pip install hfortix                # Meta-package (core + fortios)
```

To use core directly (HTTP clients, exceptions, `CloudSession`, caching,
formatting):

```bash
pip install hfortix-core
```

```python
from hfortix_core.http import HTTPClient
from hfortix_core import APIError

client = HTTPClient(url="https://192.168.1.99", token="your-api-token")
try:
    policies = client.get("cmdb", "firewall/policy")
except APIError as e:
    print(f"API error: {e.message}")
finally:
    client.close()
```

## Where to go next

- **[README.md](README.md)** — overview of everything the package provides
- **[EXAMPLES.md](EXAMPLES.md)** — verified, copy-paste ready examples for
  all core components
- **[Full documentation](https://hfortix-core.readthedocs.io/)** — complete
  API reference
