Custom Wrappers
===============

.. note::
   **Looking for convenience wrappers?**
   
   Built-in convenience wrappers were removed in v0.5.0, but you can easily create your own!
   
   This page shows examples from simple to advanced. See :doc:`/fortios/guides/custom-wrappers` 
   for the complete guide.

Why Create Custom Wrappers?
----------------------------

HFortix provides direct API access, giving you the flexibility to create custom wrappers
that match your organization's specific requirements:

- **No maintenance burden** - You control what you need
- **Perfect fit** - Tailored to your exact use cases  
- **Full flexibility** - Add your own validation, business logic, and patterns
- **Type safety** - Create strongly-typed interfaces for your workflows

Examples: Simple to Advanced
------------------------------

Example 1: Simple Property Shortcuts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The simplest approach - just add property shortcuts to commonly used endpoints:

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   class MyFortiGate(FortiOS):
       """FortiGate client with shortcuts."""
       
       @property
       def addresses(self):
           """Quick access to firewall addresses."""
           return self.api.cmdb.firewall.address
       
       @property  
       def policies(self):
           """Quick access to firewall policies."""
           return self.api.cmdb.firewall.policy
   
   # Usage - shorter paths!
   fgt = MyFortiGate(host="192.168.1.99", api_token="your-token")
   
   # Before: fgt.api.cmdb.firewall.address.post(...)
   # After:  fgt.addresses.post(...)
   address = fgt.addresses.post(
       name="server",
       subnet="10.0.1.5 255.255.255.255"
   )
   
   # Before: fgt.api.cmdb.firewall.policy.get()
   # After:  fgt.policies.get()
   policies = fgt.policies.get()

Example 2: Wrapper Functions with Simplified Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create functions that simplify complex API calls:

.. code-block:: python

   from hfortix_fortios import FortiOS
   from typing import List
   
   def create_address_group(
       fgt: FortiOS,
       name: str,
       members: List[str],
       comment: str = ""
   ) -> dict:
       """
       Create address group with simple member list.
       
       Instead of: members=[{"name": "addr1"}, {"name": "addr2"}]
       Just use:   members=["addr1", "addr2"]
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
       members=["web1", "web2", "web3"],  # Simple list!
       comment="Production web servers"
   )

Example 3: Helper Methods with Standard Patterns
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add helper methods for common operations:

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   class FortiGateHelper(FortiOS):
       """FortiGate with common helper methods."""
       
       def create_simple_policy(
           self,
           name: str,
           src_zone: str,
           dst_zone: str,
           services: list[str],
           log: bool = True,
           **kwargs
       ):
           """Create a simple any-to-any policy."""
           return self.api.cmdb.firewall.policy.post(
               name=name,
               srcintf=[{"name": src_zone}],
               dstintf=[{"name": dst_zone}],
               srcaddr=[{"name": "all"}],
               dstaddr=[{"name": "all"}],
               service=[{"name": s} for s in services],
               action="accept",
               logtraffic="all" if log else "disable",
               **kwargs
           )
       
       def find_address(self, pattern: str) -> list:
           """Find addresses matching a pattern."""
           all_addrs = self.api.cmdb.firewall.address.get()
           return [
               addr for addr in all_addrs 
               if pattern.lower() in addr.get('name', '').lower()
           ]
   
   # Usage
   fgt = FortiGateHelper(host="192.168.1.99", api_token="your-token")
   
   # Simple policy creation
   policy = fgt.create_simple_policy(
       name="Allow-Web-Access",
       src_zone="internal",
       dst_zone="wan",
       services=["HTTP", "HTTPS"]
   )
   
   # Find addresses
   web_servers = fgt.find_address("web")

Example 4: Domain-Specific Wrapper Class
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a complete wrapper for your specific use case:

.. code-block:: python

   from hfortix_fortios import FortiOS
   from dataclasses import dataclass
   
   @dataclass
   class WebServer:
       name: str
       ip: str
       allow_http: bool = True
       allow_https: bool = True
   
   class WebServerManager:
       """Manage web server configurations."""
       
       def __init__(self, fgt: FortiOS):
           self.fgt = fgt
       
       def deploy_webserver(self, server: WebServer) -> dict:
           """Deploy complete web server configuration."""
           results = {}
           
           # Create address object
           results['address'] = self.fgt.api.cmdb.firewall.address.post(
               name=server.name,
               subnet=f"{server.ip} 255.255.255.255",
               comment=f"Web server: {server.name}"
           )
           
           # Create service group
           services = []
           if server.allow_http:
               services.append({"name": "HTTP"})
           if server.allow_https:
               services.append({"name": "HTTPS"})
           
           # Create firewall policy
           results['policy'] = self.fgt.api.cmdb.firewall.policy.post(
               name=f"Access-{server.name}",
               srcintf=[{"name": "internal"}],
               dstintf=[{"name": "dmz"}],
               srcaddr=[{"name": "all"}],
               dstaddr=[{"name": server.name}],
               service=services,
               action="accept",
               logtraffic="all"
           )
           
           return results
   
   # Usage
   fgt = FortiOS(host="192.168.1.99", api_token="your-token")
   mgr = WebServerManager(fgt)
   
   # Deploy complete web server config with one call
   server = WebServer(
       name="prod-web-01",
       ip="192.168.10.50",
       allow_http=True,
       allow_https=True
   )
   
   result = mgr.deploy_webserver(server)

Example 5: Validation and Error Handling
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add custom validation before making API calls:

.. code-block:: python

   from hfortix_fortios import FortiOS
   from hfortix_core.exceptions import HTTPError
   import ipaddress
   import re
   
   class ValidatedFortiGate(FortiOS):
       """FortiGate client with input validation."""
       
       def create_address_safe(
           self,
           name: str,
           subnet: str,
           comment: str = ""
       ):
           """Create address with validation."""
           
           # Validate name format
           if not re.match(r'^[a-zA-Z0-9_-]+$', name):
               raise ValueError(
                   f"Invalid name '{name}'. "
                   "Use only alphanumeric, dash, underscore"
               )
           
           # Validate subnet format
           try:
               ip, mask = subnet.split()
               ipaddress.IPv4Network(f"{ip}/{mask}", strict=False)
           except Exception as e:
               raise ValueError(f"Invalid subnet '{subnet}': {e}")
           
           # Check if exists
           try:
               existing = self.api.cmdb.firewall.address.get(mkey=name)
               raise ValueError(f"Address '{name}' already exists")
           except HTTPError as e:
               if e.status_code != 404:
                   raise
           
           # Create if validation passed
           return self.api.cmdb.firewall.address.post(
               name=name,
               subnet=subnet,
               comment=comment
           )
   
   # Usage
   fgt = ValidatedFortiGate(host="192.168.1.99", api_token="your-token")
   
   try:
       addr = fgt.create_address_safe(
           name="web-server-01",
           subnet="192.168.1.100 255.255.255.255",
           comment="Production web server"
       )
       print("✓ Address created successfully")
   except ValueError as e:
       print(f"✗ Validation error: {e}")

Example 6: Async Wrapper for Bulk Operations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use async for concurrent operations:

.. code-block:: python

   from hfortix_fortios import AsyncFortiOS
   import asyncio
   
   class AsyncBulkManager:
       """Async operations for bulk tasks."""
       
       def __init__(self, fgt: AsyncFortiOS):
           self.fgt = fgt
       
       async def bulk_create_addresses(
           self,
           addresses: list[dict]
       ) -> list:
           """Create multiple addresses concurrently."""
           tasks = [
               self.fgt.api.cmdb.firewall.address.post(**addr)
               for addr in addresses
           ]
           return await asyncio.gather(*tasks)
       
       async def backup_all_policies(self) -> list:
           """Retrieve all policy-related objects."""
           results = await asyncio.gather(
               self.fgt.api.cmdb.firewall.policy.get(),
               self.fgt.api.cmdb.firewall.address.get(),
               self.fgt.api.cmdb.firewall.addrgrp.get(),
               self.fgt.api.cmdb.firewall.service.custom.get(),
           )
           return {
               'policies': results[0],
               'addresses': results[1],
               'addr_groups': results[2],
               'services': results[3]
           }
   
   # Usage
   async def main():
       async with AsyncFortiOS(
           host="192.168.1.99",
           api_token="your-token"
       ) as fgt:
           mgr = AsyncBulkManager(fgt)
           
           # Create 100 addresses concurrently
           addresses = [
               {
                   "name": f"host-{i}",
                   "subnet": f"10.0.1.{i} 255.255.255.255"
               }
               for i in range(100)
           ]
           results = await mgr.bulk_create_addresses(addresses)
           print(f"Created {len(results)} addresses")
           
           # Backup all configs concurrently
           backup = await mgr.backup_all_policies()
           print(f"Backed up {len(backup['policies'])} policies")
   
   asyncio.run(main())

Learn More
----------

:doc:`/fortios/guides/custom-wrappers`
   Complete guide with more examples, best practices, and advanced patterns.

:doc:`/fortios/user-guide/endpoint-methods`
   Learn about available HTTP methods: .get(), .post(), .put(), .delete(), .set()

:doc:`/fortios/api-reference/index`
   Complete API reference with 1,219 endpoints to build your wrappers on.

:doc:`/fortios/getting-started/quickstart`
   Get started with the direct API methods.

See Also
--------

:doc:`/fortios/guides/custom-wrappers`
   Complete guide to creating custom wrappers, aliases, and helper functions.
   Includes examples for simple aliases, validation wrappers, async operations,
   and domain-specific wrappers.

:doc:`/fortios/api-reference/index`
   Complete API reference with 1,219 endpoints to build your wrappers on.

:doc:`/fortios/getting-started/quickstart`
   Get started with the direct API methods.

See Also
--------

- :doc:`/fortios/guides/fmg-proxy` - FortiManager proxy for managing multiple devices
- :doc:`/fortios/user-guide/index` - Core concepts and patterns
- :doc:`/fortios/api-reference/index` - Complete API documentation
