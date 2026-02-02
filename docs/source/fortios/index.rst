FortiOS
=======

Complete Python SDK for FortiOS/FortiGate automation with 100% API coverage (1,348 endpoints: 561 CMDB + 490 Monitor + 286 Log + 11 Service).

.. grid:: 2
    :gutter: 3

    .. grid-item-card:: ⚡ Quick Start
        :link: getting-started/quickstart
        :link-type: doc

        Get up and running in 5 minutes - install, connect, and make your first API calls.

    .. grid-item-card:: 🎨 Custom Wrappers
        :link: guides/custom-wrappers
        :link-type: doc

        Build your own convenience wrappers - aliases, validation, domain-specific abstractions.

    .. grid-item-card:: � User Guide
        :link: user-guide/index
        :link-type: doc

        Learn core concepts and patterns.

    .. grid-item-card:: � API Documentation
        :link: api-documentation/index
        :link-type: doc

        Complete endpoint reference and API patterns.

    .. grid-item-card:: � FortiManager Proxy
        :link: guides/fmg-proxy
        :link-type: doc

        Manage multiple FortiGates through FortiManager with seamless API routing.

    .. grid-item-card:: 📋 Topic Guides
        :link: guides/index
        :link-type: doc

        Advanced topics and patterns.

.. toctree::
   :maxdepth: 1
   :hidden:

   getting-started/quickstart
   getting-started/authentication
   user-guide/index
   api-documentation/index
   guides/index
   examples/index

Quick Example
-------------

.. code-block:: python

    from hfortix_fortios import FortiOS

    # Connect to FortiGate
    fgt = FortiOS(host="192.168.1.99", token="your-api-token")

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

    # Close connection when done
    fgt.close()

**Or use context manager for automatic cleanup:**

.. code-block:: python

    from hfortix_fortios import FortiOS

    # Context manager automatically closes connection
    with FortiOS(host="192.168.1.99", token="your-api-token") as fgt:
        # Create resources
        fgt.api.cmdb.firewall.address.post(
            name="web-server",
            subnet="10.0.1.100/32"
        )
        
        # Query data
        addresses = fgt.api.cmdb.firewall.address.get()
        
    # Connection automatically closed after with block

    # Get system status
    status = fgt.api.monitor.system.status.get()
    print(f"Hostname: {status['hostname']}")
    print(f"Version: {status['version']}")

Key Features
------------

**Complete API Coverage**
    All 1,219 FortiOS 7.6.5 API endpoints: 886 CMDB + 295 Monitor + 38 Log endpoints.

**Dual Interface Patterns**
    Use dict-style or kwargs-style - choose what fits your workflow.

**Full Async Support**
    All endpoints available in async/await with ``_async`` suffix.

**Direct API Access** *(New in v0.5.0)*
    Use ``request()`` method for zero-translation workflow - copy JSON from FortiGate GUI, paste into Python.

**Production Ready**
    Circuit breaker pattern, automatic retries, connection pooling, comprehensive validation.

**Developer Friendly**
    100% type hints with .pyi stubs, extensive documentation, rich error messages, validation framework.

Supported FortiOS Versions
---------------------------

- **FortiOS 7.6.x** - Full support
- **FortiOS 7.4.x** - Compatible
- **FortiOS 7.2.x** - Compatible
- **FortiOS 7.0.x** - Compatible
- **FortiOS 6.x** - Most features work

API Categories
--------------

The FortiOS API is organized into four main types:

**CMDB (Configuration)**
    886 endpoints for managing firewall configuration: addresses, policies, routes, VPN, system settings, etc.

**Monitor (Status/Stats)**
    295 endpoints for real-time monitoring: system status, interface stats, routing tables, VPN status, etc.

**Log (Historical Data)**
    38 endpoints for accessing historical logs and events with full parameterization support.

See :doc:`/fortios/api-reference/index` for complete category listing.

Next Steps
----------

1. **Install** - :doc:`/getting-started/installation`
2. **Quick Start** - :doc:`/fortios/getting-started/quickstart`
3. **Authentication** - :doc:`/fortios/getting-started/authentication`
4. **Browse Examples** - :doc:`/fortios/examples/index`
5. **Explore API** - :doc:`/fortios/api-reference/index`
