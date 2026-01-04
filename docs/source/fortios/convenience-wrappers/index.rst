Convenience Wrappers
====================

.. danger::
   **DEPRECATED IN v0.5.0 - REMOVED**
   
   All convenience wrappers have been **REMOVED** in v0.5.0.
   
   **Migration Required:**
   
   - ❌ ``fgt.firewall.policy.create()`` - NO LONGER EXISTS
   - ✅ ``fgt.api.cmdb.firewall.policy.create()`` - Use direct API method
   - ✅ ``fgt.request(method='POST', path='/api/v2/cmdb/firewall/policy', data={...})`` - Use request() method
   
   See :doc:`/fortios/getting-started/quickstart` for updated examples.

Why Were They Removed?
----------------------

Convenience wrappers were removed in v0.5.0 for the following reasons:

1. **Maintenance Burden** - Required manual updates for every FortiOS schema change
2. **API Drift** - Wrapper behavior could diverge from actual FortiOS API behavior
3. **Limited Coverage** - Only covered ~20 endpoints out of 1,219 total
4. **Type Safety Issues** - Harder to maintain accurate type hints for translations
5. **Zero-Translation Alternative** - The ``request()`` method provides a better workflow

Migration Guide
---------------

Old convenience wrapper code:

.. code-block:: python

   # v0.4.0 - NO LONGER WORKS
   fgt.firewall.policy.create(
       name='Allow-Web',
       srcintf=['port1'],
       dstintf=['port2'],
       srcaddr=['all'],
       dstaddr=['all'],
       service=['HTTP', 'HTTPS'],
       action='accept'
   )

New direct API code (v0.5.0+):

.. code-block:: python

   # v0.5.0 - Direct API method
   fgt.api.cmdb.firewall.policy.create(
       name='Allow-Web',
       srcintf=[{'name': 'port1'}],
       dstintf=[{'name': 'port2'}],
       srcaddr=[{'name': 'all'}],
       dstaddr=[{'name': 'all'}],
       service=[{'name': 'HTTP'}, {'name': 'HTTPS'}],
       action='accept'
   )

   # Or use request() method (copy JSON from FortiGate GUI):
   fgt.request(
       method='POST',
       path='/api/v2/cmdb/firewall/policy',
       data={
           'name': 'Allow-Web',
           'srcintf': [{'name': 'port1'}],
           'dstintf': [{'name': 'port2'}],
           'srcaddr': [{'name': 'all'}],
           'dstaddr': [{'name': 'all'}],
           'service': [{'name': 'HTTP'}, {'name': 'HTTPS'}],
           'action': 'accept'
       }
   )

Previously Available Wrappers (v0.4.0)
---------------------------------------

The following wrappers existed in v0.4.0 but are **REMOVED** in v0.5.0:

Firewall & Objects
~~~~~~~~~~~~~~~~~~

- ``fgt.firewall.policy`` - Firewall policies (use ``fgt.api.cmdb.firewall.policy`` now)
- ``fgt.firewall.schedule`` - Schedules (use ``fgt.api.cmdb.firewall.schedule.*`` now)
- ``fgt.firewall.service`` - Custom services (use ``fgt.api.cmdb.firewall.service.custom`` now)
- ``fgt.firewall.shaper`` - Traffic shapers (use ``fgt.api.cmdb.firewall.shaper.*`` now)
- ``fgt.firewall.ipmac_binding`` - IP/MAC bindings (use ``fgt.api.cmdb.firewall.ipmacbinding.table`` now)

For the complete list of 1,219 available endpoints, see :doc:`/fortios/api-reference/index`.

Direct API Access (Recommended)
--------------------------------

Instead of convenience wrappers, use direct API access:

**API Endpoint Methods:**

- ``create(name=..., **params)`` - Create resource with parameters
- ``update(mkey=..., **params)`` - Update resource by key
- ``delete(mkey=...)`` - Delete resource by key
- ``get(mkey=None, **params)`` - Get one resource or list all
- ``exists(mkey=...)`` - Check if resource exists

**request() Method (Zero-Translation):**

The ``request()`` method lets you copy JSON directly from FortiGate GUI and use it in Python:

.. code-block:: python

   # Copy JSON from FortiGate GUI, paste here - zero translation needed
   fgt.request(
       method='POST',
       path='/api/v2/cmdb/firewall/policy',
       data={...}  # Exact JSON from GUI
   )

See Also
--------

- :doc:`/fortios/getting-started/quickstart` - Updated quick start guide for v0.5.0
- :doc:`/fortios/api-reference/index` - Complete endpoint reference (1,219 endpoints)
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
