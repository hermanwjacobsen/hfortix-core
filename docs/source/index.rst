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

      Complete FortiOS API client with 1,348 endpoints (561 CMDB + 490 Monitor + 286 Log + 11 Service).
      **Available Now** - v0.5.154 Beta

   .. grid-item-card:: ⚙️ Core Framework
      :link: core/index
      :link-type: doc

      Foundation HTTP client and exception handling.
      **Available Now** - v0.5.154 Beta

Key Features
------------

✨ **Complete API Coverage**
   100% coverage of FortiOS 7.6.5 API (1,348 endpoints: 561 CMDB + 490 Monitor + 286 Log + 11 Service)

🎯 **Fully Typed**
   Complete type hints with .pyi stubs for excellent IDE support. 100% type coverage for CMDB endpoints; partial coverage for Monitor/Log endpoints.

⚡ **Modern & Fast**
   Async/await support with httpx, HTTP/2, connection pooling, and circuit breakers

🛡️ **Production Ready**
   Comprehensive error handling, validation, retry logic, rate limiting, and 1,447+ schema validator tests

🔄 **Flexible Interface**
   Simple list format auto-converts to FortiOS dict format - use ``["internal"]`` instead of ``[{"name": "internal"}]``

🔄 **Batch Transactions** (v0.5.152+)
   Atomic configuration changes with automatic commit/rollback support (FortiOS 6.4.0+)

🔍 **API Request Inspection** (v0.5.152+)
   Debug and audit API interactions with ``http_api_request`` and ``fmg_api_request`` properties

📦 **Enhanced Developer Experience**
   - FortiObject responses with attribute access (``addr.subnet`` instead of ``addr['subnet']``)
   - Multiple response formats (``.dict``, ``.json``, ``.raw``)
   - Built-in validation and error handling
   - FortiManager proxy support for managing multiple devices

Quick Example - FortiOS
-----------------------

.. code-block:: python

   from hfortix_fortios import FortiOS

   # Connect with context manager (automatic cleanup)
   with FortiOS(host="192.168.1.99", token="your-api-token") as fgt:
       # Create firewall address
       fgt.api.cmdb.firewall.address.post(
           name="web-server",
           subnet="10.0.1.100/32",
           comment="Production web server"
       )

       # Create firewall policy - simple list format (auto-converted)
       fgt.api.cmdb.firewall.policy.post(
           name="Allow-Web-Traffic",
           srcintf=["internal"],      # Converted to [{"name": "internal"}]
           dstintf=["wan1"],          # Converted to [{"name": "wan1"}]
           srcaddr=["all"],           # Converted to [{"name": "all"}]
           dstaddr=["web-server"],    # Converted to [{"name": "web-server"}]
           service=["HTTP", "HTTPS"], # Converted to [{"name": "..."}]
           action="accept",
           nat="enable"
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

**FortiOS 7.6.5 API Coverage (February 2026)**

.. grid:: 2
   :gutter: 2

   .. grid-item-card:: CMDB API
      :class-header: bg-success text-white

      561 endpoints
      ^^^^^^^^^^^^^^^^^^^
      **100% coverage** - Configuration database management (100% type coverage)
      
      🔷 v0.5.154 Beta

   .. grid-item-card:: Monitor API
      :class-header: bg-success text-white

      490 endpoints
      ^^^^^^^^^^^^^^^^^^^
      **100% coverage** - Real-time monitoring and statistics (partial type coverage)
      
      🔷 v0.5.154 Beta

   .. grid-item-card:: Log API
      :class-header: bg-success text-white

      286 endpoints
      ^^^^^^^^^^^^^^^^^^
      **100% coverage** - Log retrieval with full parameterization (partial type coverage)
      
      🔷 v0.5.154 Beta

   .. grid-item-card:: Service API
      :class-header: bg-success text-white

      11 endpoints
      ^^^^^^^^^^^^^^^^^^
      **100% coverage** - Service operations (100% type coverage)
      
      🔷 v0.5.154 Beta

**Overall: 1,348 API methods across all categories (100% coverage)** 🎉

- **561 CMDB endpoints** - Configuration database management (100% typed)
- **490 Monitor endpoints** - Real-time monitoring and statistics (partial types)
- **286 Log endpoints** - Log retrieval and analysis (partial types)
- **11 Service endpoints** - Service operations (100% typed)
- **100% auto-generated** - Complete schema coverage with intelligent generation

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
     - 0.5.154
     - Beta
     - Meta package - installs all available packages
   * - ``hfortix-core``
     - 0.5.154
     - Beta
     - HTTP client, error handling, circuit breaker, observability
   * - ``hfortix-fortios``
     - 0.5.154
     - Beta
     - FortiOS/FortiGate SDK - 1,348 endpoints (561 CMDB + 490 Monitor + 286 Log + 11 Service)

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
