Methods and Usage
=================

Learn how to use the FortiOS SDK methods to interact with 1,348 endpoints across CMDB, Monitor, Log, and Service categories.

Available Methods
-----------------

.. grid:: 1
    :gutter: 3

    .. grid-item-card:: 📚 API Reference
        :link: /fortios/api-reference/index
        :link-type: doc

        Complete endpoint documentation (1,348 endpoints).
        
        Direct HTTP methods: .get(), .post(), .put(), .delete(), .set()

Usage Patterns
--------------

**Direct API Access** - Use the typed endpoint methods:

.. code-block:: python

   # Create a firewall policy
   fgt.api.cmdb.firewall.policy.post(
       name='Allow-Web',
       srcintf=[{'name': 'port1'}],
       dstintf=[{'name': 'port2'}],
       service=[{'name': 'HTTP'}, {'name': 'HTTPS'}],
       action='accept'
   )

   # Or use request() for zero-translation
   fgt.request(
       method='POST',
       path='/api/v2/cmdb/firewall/policy',
       data={
           'name': 'Allow-Web',
           'srcintf': [{'name': 'port1'}],
           'dstintf': [{'name': 'port2'}],
           'service': [{'name': 'HTTP'}, {'name': 'HTTPS'}],
           'action': 'accept'
       }
   )

**Custom Wrappers** - Build your own convenience abstractions:

.. code-block:: python

   # Create your own wrapper functions
   def create_policy(fgt, name, src, dst, services):
       return fgt.api.cmdb.firewall.policy.post(
           name=name,
           srcintf=[{'name': src}],
           dstintf=[{'name': dst}],
           service=[{'name': s} for s in services],
           action='accept'
       )

   # Use your wrapper
   create_policy(fgt, 'Allow-Web', 'port1', 'port2', ['HTTP', 'HTTPS'])

See :doc:`/fortios/guides/custom-wrappers` for complete custom wrapper examples.

Documentation Sections
----------------------

.. toctree::
   :maxdepth: 3

   ../api-reference/index

API Endpoint Categories
-----------------------

Complete endpoint documentation organized by category:

- **CMDB API** - 886 configuration endpoints across 37 categories
- **Monitor API** - 295 status/statistics endpoints across 32 categories
- **Log API** - 38 log endpoints across 5 categories
- **Service API** - Special service endpoints

See :doc:`../api-reference/index` for complete endpoint documentation.

Related Documentation
---------------------

- :doc:`/fortios/guides/custom-wrappers` - Create your own convenience wrappers
- :doc:`/fortios/user-guide/endpoint-methods` - Available HTTP methods
- :doc:`/fortios/guides/fmg-proxy` - FortiManager proxy usage
