FortiOS Client
==============

The main FortiOS client class for connecting to FortiGate devices.

Client Class
------------

.. autoclass:: hfortix_fortios.FortiOS
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__

Usage
-----

Basic Connection
^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS

   # Connect with API token (recommended)
   fgt = FortiOS(
       host='192.168.1.99',
       token='your-api-token',
       verify=False  # Use True in production
   )

   # Connect with username/password (FortiOS ≤7.4 only)
   fgt = FortiOS(
       host='192.168.1.99',
       username='admin',
       password='password',
       verify=False
   )

Optimized Settings
^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # For high-performance scenarios
   fgt = FortiOS(
       host='192.168.1.99',
       token='your-token',
       max_connections=60,
       max_keepalive_connections=30,
       connect_timeout=10.0,
       read_timeout=300.0
   )

API Namespaces
--------------

The FortiOS client provides access to all API categories through organized namespaces.

API Namespace
^^^^^^^^^^^^^

.. autoclass:: hfortix_fortios.api.API
   :members:
   :undoc-members:
   :show-inheritance:

The ``api`` namespace provides access to:

- ``api.cmdb`` - Configuration Management Database (886 endpoints)
- ``api.monitor`` - Monitoring and status (295 endpoints)  
- ``api.log`` - Log queries (38 endpoints with full parameterization)

Examples
--------

Using CMDB API
^^^^^^^^^^^^^^

.. code-block:: python

   # List firewall addresses
   addresses = fgt.api.cmdb.firewall.address.get()

   # Create firewall address
   fgt.api.cmdb.firewall.address.post(
       name='web-server',
       subnet='10.0.1.100/32'
   )

   # Update firewall address
   fgt.api.cmdb.firewall.address.put(
       name='web-server',
       comment='Production server'
   )

   # Delete firewall address
   fgt.api.cmdb.firewall.address.delete(name='web-server')

Using Monitor API
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get system status
   status = fgt.api.monitor.system.status.get()

   # Get firewall sessions
   sessions = fgt.api.monitor.firewall.session.get()

   # Get interface statistics
   stats = fgt.api.monitor.system.interface.get()

Using Direct API Methods
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Create firewall policy (using post)
   policy = fgt.api.cmdb.firewall.policy.post(
       name='Allow-Web',
       srcintf=[{"name": "internal"}],
       dstintf=[{"name": "wan1"}],
       srcaddr=[{"name": "all"}],
       dstaddr=[{"name": "web-server"}],
       service=[{"name": "HTTP"}, {"name": "HTTPS"}],
       action='accept'
   )

   # Check if policy exists
   if fgt.api.cmdb.firewall.policy.exists(policyid='1'):
       print("Policy exists!")

See Also
--------

- :doc:`/fortios/api-reference/cmdb/index` - CMDB API reference
- :doc:`/fortios/api-reference/monitor/index` - Monitor API reference
- :doc:`/fortios/user-guide/fortios-overview` - User guide
- :doc:`/fortios/getting-started/quickstart` - Quick start guide
