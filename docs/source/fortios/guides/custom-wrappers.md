# Creating Custom Wrappers and Aliases

Learn how to create your own convenience wrappers and aliases for common operations.

## Overview

While HFortix doesn't include built-in convenience wrappers, you can easily create your own custom wrappers, aliases, and helper functions tailored to your specific needs.

## Why Create Custom Wrappers?

- **Simplify repetitive tasks** - Abstract away complex API calls
- **Domain-specific logic** - Add business logic specific to your organization
- **Parameter validation** - Add custom validation before API calls
- **Type safety** - Create strongly-typed interfaces for your use cases
- **Reusability** - Share common patterns across your team

## Simple Aliases

Create simple aliases for frequently used endpoints:

```python
from hfortix_fortios import FortiOS

class MyFortiGate(FortiOS):
    """Custom FortiGate client with aliases."""
    
    @property
    def addresses(self):
        """Quick access to firewall addresses."""
        return self.api.cmdb.firewall.address
    
    @property
    def policies(self):
        """Quick access to firewall policies."""
        return self.api.cmdb.firewall.policy
    
    @property
    def interfaces(self):
        """Quick access to system interfaces."""
        return self.api.cmdb.system.interface

# Usage
fgt = MyFortiGate(host="192.168.1.99", api_token="your-token")

# Much shorter! (Note: this uses the property shortcuts, not built-in methods)
address = fgt.addresses.post(name="server", subnet="10.0.1.5 255.255.255.255")
policies = fgt.policies.get()
```

## Wrapper Functions

Create standalone wrapper functions for common operations:

```python
from hfortix_fortios import FortiOS
from typing import List

def create_address_group(
    fgt: FortiOS,
    name: str,
    members: List[str],
    comment: str = ""
) -> dict:
    """
    Create a firewall address group with simple member list.
    
    Args:
        fgt: FortiOS client instance
        name: Name of the address group
        members: List of member address names
        comment: Optional comment
        
    Returns:
        API response with created group details
    """
    return fgt.api.cmdb.firewall.addrgrp.post(
        name=name,
        member=[{"name": m} for m in members],
        comment=comment
    )

# Usage
fgt = FortiOS(host="192.168.1.99", api_token="your-token")
group = create_address_group(
    fgt,
    name="web-servers",
    members=["web1", "web2", "web3"],
    comment="Production web servers"
)
```

## Custom Wrapper Class

Create a full wrapper class with business logic:

```python
from hfortix_fortios import FortiOS
from typing import List, Optional

class FirewallManager:
    """High-level firewall policy management."""
    
    def __init__(self, fgt: FortiOS):
        self.fgt = fgt
        self.policies = fgt.api.cmdb.firewall.policy
    
    def create_web_policy(
        self,
        name: str,
        source_zones: List[str],
        dest_zones: List[str],
        allow_http: bool = True,
        allow_https: bool = True,
        enable_logging: bool = True
    ) -> dict:
        """
        Create a standardized web access policy.
        
        This enforces your organization's standards:
        - Always logs connections
        - Uses standard service objects
        - Includes security profiles
        """
        services = []
        if allow_http:
            services.append({"name": "HTTP"})
        if allow_https:
            services.append({"name": "HTTPS"})
        
        return self.policies.post(
            name=name,
            srcintf=[{"name": z} for z in source_zones],
            dstintf=[{"name": z} for z in dest_zones],
            srcaddr=[{"name": "all"}],
            dstaddr=[{"name": "all"}],
            service=services,
            action="accept",
            logtraffic="all" if enable_logging else "disable",
            # Add your org's required security profiles
            av_profile={"name": "default"},
            webfilter_profile={"name": "default"},
            ips_sensor={"name": "default"}
        )
    
    def bulk_disable_policies(self, policy_ids: List[int]) -> List[dict]:
        """Disable multiple policies at once."""
        results = []
        for policy_id in policy_ids:
            result = self.policies.put(
                policyid=policy_id,
                status="disable"
            )
            results.append(result)
        return results
    
    def find_policies_by_address(self, address_name: str) -> List[dict]:
        """Find all policies using a specific address."""
        all_policies = self.policies.get().results
        
        matching = []
        for policy in all_policies:
            # Check source addresses
            for addr in policy.get('srcaddr', []):
                if addr.get('name') == address_name:
                    matching.append(policy)
                    break
            # Check dest addresses
            for addr in policy.get('dstaddr', []):
                if addr.get('name') == address_name:
                    matching.append(policy)
                    break
        
        return matching

# Usage
fgt = FortiOS(host="192.168.1.99", api_token="your-token")
fw = FirewallManager(fgt)

# Create standardized policy
policy = fw.create_web_policy(
    name="Internal-to-DMZ-Web",
    source_zones=["internal"],
    dest_zones=["dmz"],
    allow_http=True,
    allow_https=True
)

# Bulk operations
fw.bulk_disable_policies([10, 11, 12, 13])

# Find dependencies
policies = fw.find_policies_by_address("old-server")
```

## Async Wrappers

Create async wrappers for concurrent operations:

```python
from hfortix_fortios import AsyncFortiOS
from typing import List
import asyncio

class AsyncFirewallManager:
    """Async firewall operations."""
    
    def __init__(self, fgt: AsyncFortiOS):
        self.fgt = fgt
    
    async def bulk_create_addresses(
        self,
        addresses: List[dict]
    ) -> List[dict]:
        """Create multiple addresses concurrently."""
        tasks = [
            self.fgt.api.cmdb.firewall.address.post(**addr)
            for addr in addresses
        ]
        return await asyncio.gather(*tasks)
    
    async def get_all_objects(self) -> dict:
        """Fetch multiple object types concurrently."""
        tasks = {
            'addresses': self.fgt.api.cmdb.firewall.address.get(),
            'groups': self.fgt.api.cmdb.firewall.addrgrp.get(),
            'services': self.fgt.api.cmdb.firewall.service.custom.get(),
            'policies': self.fgt.api.cmdb.firewall.policy.get(),
        }
        
        results = {}
        for key, task in tasks.items():
            results[key] = await task
        
        return results

# Usage
async def main():
    async with AsyncFortiOS(
        host="192.168.1.99",
        api_token="your-token"
    ) as fgt:
        fw = AsyncFirewallManager(fgt)
        
        # Create 100 addresses concurrently
        addresses = [
            {"name": f"host-{i}", "subnet": f"10.0.1.{i} 255.255.255.255"}
            for i in range(100)
        ]
        results = await fw.bulk_create_addresses(addresses)
        
        # Fetch all objects at once
        all_objects = await fw.get_all_objects()

asyncio.run(main())
```

## Domain-Specific Wrappers

Create wrappers for your specific infrastructure:

```python
from hfortix_fortios import FortiOS
from dataclasses import dataclass
from typing import List

@dataclass
class Branch:
    """Branch office configuration."""
    name: str
    subnet: str
    vpn_endpoint: str
    allowed_services: List[str]

class BranchOfficeManager:
    """Manage branch office configurations."""
    
    def __init__(self, fgt: FortiOS):
        self.fgt = fgt
    
    def provision_branch(self, branch: Branch) -> dict:
        """
        Complete branch office provisioning.
        
        Creates:
        1. Address object for branch subnet
        2. Address group for branch
        3. Firewall policy for branch access
        4. VPN configuration (if needed)
        """
        results = {}
        
        # Create address object
        results['address'] = self.fgt.api.cmdb.firewall.address.post(
            name=f"{branch.name}-subnet",
            subnet=branch.subnet,
            comment=f"{branch.name} branch office network"
        )
        
        # Create address group
        results['group'] = self.fgt.api.cmdb.firewall.addrgrp.post(
            name=f"{branch.name}-networks",
            member=[{"name": f"{branch.name}-subnet"}],
            comment=f"{branch.name} branch networks"
        )
        
        # Create policy
        results['policy'] = self.fgt.api.cmdb.firewall.policy.post(
            name=f"{branch.name}-to-HQ",
            srcintf=[{"name": "vpn-tunnel"}],
            dstintf=[{"name": "internal"}],
            srcaddr=[{"name": f"{branch.name}-subnet"}],
            dstaddr=[{"name": "HQ-networks"}],
            service=[{"name": svc} for svc in branch.allowed_services],
            action="accept",
            logtraffic="all"
        )
        
        return results

# Usage
fgt = FortiOS(host="192.168.1.99", api_token="your-token")
manager = BranchOfficeManager(fgt)

branch = Branch(
    name="London",
    subnet="10.10.1.0 255.255.255.0",
    vpn_endpoint="london-fw.example.com",
    allowed_services=["HTTP", "HTTPS", "DNS", "SMTP"]
)

results = manager.provision_branch(branch)
```

## Validation Wrappers

Add custom validation before API calls:

```python
from hfortix_fortios import FortiOS
from hfortix_core.exceptions import APIError, ResourceNotFoundError
import ipaddress

class ValidatedFirewallManager:
    """Firewall manager with validation."""
    
    def __init__(self, fgt: FortiOS):
        self.fgt = fgt
    
    def create_address_with_validation(
        self,
        name: str,
        subnet: str,
        comment: str = ""
    ) -> dict:
        """
        Create address with validation.
        
        Validates:
        - Name follows naming convention
        - Subnet is valid CIDR
        - Address doesn't already exist
        """
        # Validate name
        if not name.replace('-', '').replace('_', '').isalnum():
            raise ValueError(f"Invalid name: {name}. Use only alphanumeric, dash, underscore")
        
        # Validate subnet
        try:
            # Convert FortiOS format to CIDR
            ip, mask = subnet.split()
            network = ipaddress.IPv4Network(f"{ip}/{mask}", strict=False)
        except ValueError as e:
            raise ValueError(f"Invalid subnet: {subnet}") from e
        
        # Check if exists
        try:
            existing = self.fgt.api.cmdb.firewall.address.get(mkey=name)
            raise ValueError(f"Address '{name}' already exists")
        except ResourceNotFoundError:
            pass  # Address doesn't exist, we can create it
        except APIError as e:
            raise  # Re-raise other API errors
        
        # Create if validation passes
        return self.fgt.api.cmdb.firewall.address.post(
            name=name,
            subnet=subnet,
            comment=comment
        )

# Usage
fgt = FortiOS(host="192.168.1.99", api_token="your-token")
manager = ValidatedFirewallManager(fgt)

try:
    addr = manager.create_address_with_validation(
        name="web-server-01",
        subnet="192.168.1.100 255.255.255.255",
        comment="Production web server"
    )
except ValueError as e:
    print(f"Validation error: {e}")
```

## Best Practices

1. **Start simple** - Begin with basic aliases and grow complexity as needed
2. **Type hints** - Use Python type hints for better IDE support
3. **Documentation** - Document your wrappers with docstrings
4. **Error handling** - Wrap API calls in try/except blocks
5. **Reusability** - Design wrappers to be reused across projects
6. **Testing** - Test your wrappers thoroughly
7. **Keep it DRY** - Don't repeat yourself - create wrappers for repeated patterns

## Example: Complete Custom Module

Here's a complete example you can use as a template:

```python
# my_fortios_helpers.py
"""
Custom FortiOS helper functions and wrappers.
"""

from hfortix_fortios import FortiOS
from typing import List, Optional, Dict, Any
from hfortix_core.exceptions import HTTPError

class FortiOSHelper:
    """Collection of helper methods for common FortiOS operations."""
    
    def __init__(self, host: str, api_token: Optional[str] = None, **kwargs):
        """Initialize helper with FortiOS connection."""
        self.fgt = FortiOS(host=host, api_token=api_token, **kwargs)
    
    # Shortcuts
    @property
    def addr(self):
        """Shortcut to firewall addresses."""
        return self.fgt.api.cmdb.firewall.address
    
    @property
    def pol(self):
        """Shortcut to firewall policies."""
        return self.fgt.api.cmdb.firewall.policy
    
    # Helper methods
    def create_simple_policy(
        self,
        name: str,
        src_zone: str,
        dst_zone: str,
        services: List[str],
        **kwargs
    ) -> Dict[str, Any]:
        """Create a simple any-to-any policy with specified services."""
        return self.pol.post(
            name=name,
            srcintf=[{"name": src_zone}],
            dstintf=[{"name": dst_zone}],
            srcaddr=[{"name": "all"}],
            dstaddr=[{"name": "all"}],
            service=[{"name": s} for s in services],
            action="accept",
            **kwargs
        )
    
    def __enter__(self):
        """Context manager support."""
        return self
    
    def __exit__(self, *args):
        """Cleanup on context exit."""
        self.fgt.close()

# Usage
with FortiOSHelper(host="192.168.1.99", api_token="your-token") as fgt:
    # Use shortcuts
    addr = fgt.addr.post(name="test", subnet="10.0.0.1 255.255.255.255")
    
    # Use helpers
    policy = fgt.create_simple_policy(
        name="Allow-Web",
        src_zone="internal",
        dst_zone="wan",
        services=["HTTP", "HTTPS"]
    )
```

## Related

- [FortiOS Client Guide](/fortios/user-guide/client.rst) - Client basics
- [API Reference](/fortios/api-reference/index.rst) - Complete API documentation
- [Async Guide](/fortios/user-guide/async-usage.md) - Async operations
