Custom Wrappers
===============

.. note::
   **Looking for convenience wrappers?**
   
   Built-in convenience wrappers were removed in v0.5.0, but you can easily create your own!
   
   See :doc:`/fortios/guides/custom-wrappers` to learn how to create custom wrappers, aliases, 
   and helper functions tailored to your specific needs.

Creating Your Own Wrappers
---------------------------

HFortix provides direct API access, giving you the flexibility to create custom wrappers
that match your organization's specific requirements. This approach offers:

- **No maintenance burden** - You control what you need
- **Perfect fit** - Tailored to your exact use cases  
- **Full flexibility** - Add your own validation, business logic, and patterns
- **Type safety** - Create strongly-typed interfaces for your workflows

Quick Example
-------------

Here's a simple custom wrapper example:

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   class MyFortiGate(FortiOS):
       """Custom FortiGate client with shortcuts."""
       
       @property
       def addresses(self):
           """Quick access to firewall addresses."""
           return self.api.cmdb.firewall.address
       
       @property  
       def policies(self):
           """Quick access to firewall policies."""
           return self.api.cmdb.firewall.policy
   
   # Usage
   fgt = MyFortiGate(host="192.168.1.99", api_token="your-token")
   
   # Much shorter!
   address = fgt.addresses.create(
       name="server",
       subnet="10.0.1.5 255.255.255.255"
   )
   policies = fgt.policies.list()

Learn More
----------

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
