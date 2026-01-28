HFortix - Python SDK for Fortinet Products
===========================================

.. image:: https://badge.fury.io/py/hfortix.svg
   :target: https://pypi.org/project/hfortix/
   :alt: PyPI version

.. image:: https://img.shields.io/badge/python-3.10+-blue.svg
   :target: https://www.python.org/downloads/
   :alt: Python 3.10+

.. image:: https://img.shields.io/badge/License-Proprietary-blue.svg
   :target: https://github.com/hermanwjacobsen/hfortix/blob/main/LICENSE
   :alt: License

.. image:: https://img.shields.io/badge/typing-typed-green.svg
   :target: https://peps.python.org/pep-0561/
   :alt: Typing: Typed

**HFortix** is a modern, fully-typed Python SDK ecosystem for Fortinet products.

.. grid:: 2
   :gutter: 3

   .. grid-item-card:: 🔥 FortiOS/FortiGate
      :link: fortios/index
      :link-type: doc

      Complete FortiOS API client with 1,219 endpoints (886 CMDB + 295 Monitor + 38 Log).
      **Available Now** - v0.5.146 Beta

   .. grid-item-card:: ⚙️ Core Framework
      :link: core/index
      :link-type: doc

      Foundation HTTP client and exception handling.
      **Available Now** - v0.5.146 Beta

Key Features
------------

✨ **Complete API Coverage**
   100% coverage of FortiOS 7.6.5 API (1,219 endpoints: 886 CMDB + 295 Monitor + 38 Log)

🎯 **Fully Typed**
   Complete type hints with .pyi stubs for excellent IDE support. 100% coverage for CMDB endpoints; some Monitor/Log endpoints may have incomplete response fields due to FortiOS schema documentation limitations.

⚡ **Modern & Fast**
   Async/await support with httpx, HTTP/2, connection pooling, and circuit breakers

🛡️ **Production Ready**
   Comprehensive error handling, validation, retry logic, and structured logging

🔄 **Flexible Interface**
   Dual-pattern syntax supporting both dictionary and keyword arguments

🎨 **Direct API Access** *(New in v0.5.0)*
   Use ``request()`` method for zero-translation workflow - copy JSON from FortiGate GUI, paste into Python

🔍 **Enhanced Debugging**
   Connection pool monitoring, request inspection, debug sessions, and performance profiling

📊 **Advanced Observability**
   Structured logging, multi-tenant support, request tracing, and SIEM integration

Quick Example - FortiOS
-----------------------

.. code-block:: python

   from hfortix_fortios import FortiOS

   # Connect to FortiGate
   fgt = FortiOS("192.168.1.99", token="your_token_here")

   # Create firewall address - Direct API method
   fgt.api.cmdb.firewall.address.create(
       name='web-server',
       subnet='192.0.2.100/32',
       comment='Production web server'
   )

   # Create firewall policy - Direct API method
   fgt.api.cmdb.firewall.policy.create(
       name='Allow-Web',
       srcintf=[{'name': 'internal'}],
       dstintf=[{'name': 'wan1'}],
       srcaddr=[{'name': 'all'}],
       dstaddr=[{'name': 'web-server'}],
       service=[{'name': 'HTTPS'}],
       action='accept',
       nat='enable'
   )

   # Or use request() for zero-translation workflow
   # Copy JSON from FortiGate GUI, paste here:
   fgt.request(
       method='POST',
       path='/api/v2/cmdb/firewall/policy',
       data={
           'name': 'Allow-Web',
           'srcintf': [{'name': 'internal'}],
           'dstintf': [{'name': 'wan1'}],
           'srcaddr': [{'name': 'all'}],
           'dstaddr': [{'name': 'web-server'}],
           'service': [{'name': 'HTTPS'}],
           'action': 'accept',
           'nat': 'enable'
       }
   )

See :doc:`/fortios/getting-started/quickstart` for more examples.

Installation
------------

.. code-block:: bash

   # Install all available packages
   pip install hfortix
   
   # Or install specific packages
   pip install hfortix-fortios  # FortiOS/FortiGate
   pip install hfortix-core     # Core framework only

See :doc:`/getting-started/installation` for detailed instructions.

Documentation
-------------

.. toctree::
   :maxdepth: 2

   getting-started/overview
   getting-started/installation
   core/index
   fortios/index

.. toctree::
   :maxdepth: 1
   :caption: Additional Information

   changelog
   security
   license

Coverage Status
---------------

**FortiOS 7.6.5 API Coverage (December 2025)**

.. grid:: 2
   :gutter: 2

   .. grid-item-card:: CMDB API
      :class-header: bg-success text-white

      886 endpoints
      ^^^^^^^^^^^^^^^^^^^
      **100% coverage** - Configuration database management
      
      🔷 v0.5.0 Beta

   .. grid-item-card:: Monitor API
      :class-header: bg-success text-white

      295 endpoints
      ^^^^^^^^^^^^^^^^^^^
      **100% coverage** - Real-time monitoring and statistics
      
      🔷 v0.5.0 Beta

   .. grid-item-card:: Log API
      :class-header: bg-success text-white

      38 endpoints
      ^^^^^^^^^^^^^^^^^^
      **100% coverage** - Log retrieval with full parameterization
      
      🔷 v0.5.0 Beta

**Overall: 1,219 API methods across all categories (100% coverage)** 🎉

- **886 CMDB endpoints** - Configuration database management
- **295 Monitor endpoints** - Real-time monitoring and statistics
- **38 Log endpoints** - Log retrieval and analysis
- **100% auto-generated** - Complete swagger coverage with fallback

Package Status
--------------

.. list-table::
   :header-rows: 1
   :widths: 30 15 15 40

   * - Package
     - Version
     - Status
     - Description
   * - ``hfortix`` (meta)
     - 0.5.0
     - Beta
     - Meta package - installs all available packages
   * - ``hfortix-core``
     - 0.5.0
     - Beta
     - HTTP client, error handling, circuit breaker, observability
   * - ``hfortix-fortios``
     - 0.5.0
     - Beta
     - FortiOS/FortiGate SDK - 1,219 endpoints (886 CMDB + 295 Monitor + 38 Log)

Community & Support
-------------------

- **GitHub**: https://github.com/hermanwjacobsen/hfortix
- **Issues**: https://github.com/hermanwjacobsen/hfortix/issues
- **PyPI**: https://pypi.org/project/hfortix/

License
-------

Proprietary license. See the :doc:`/license` page for details.

Indices and Tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
