User Guide
==========

Comprehensive guide to using HFortix for FortiOS/FortiGate automation.

.. toctree::
   :maxdepth: 2

   client
   fortios-overview
   endpoint-methods
   response-objects
   error-handling
   async-usage

Overview
--------

The User Guide covers core concepts and essential features of HFortix:

**FortiOS Client**
   The main client class for connecting to FortiGate devices. Covers connection setup,
   authentication methods (API tokens and username/password), and client configuration.

**FortiOS Overview**
   Introduction to the FortiOS API architecture, usage patterns, and best practices.

**Endpoint Methods**
   Understanding the low-level API endpoint methods (``.get()``, ``.post()``, ``.put()``, 
   ``.delete()``) for interacting with FortiOS.

**Response Objects**
   Understanding ``FortiObject`` and ``FortiObjectList`` response types, including metadata
   properties like ``fgt_revision_changed`` for detecting actual configuration changes.

**Error Handling**
   Configurable error handling modes, exception types, and best practices for robust
   error management.

**Async Usage**
   Asynchronous programming with HFortix using async/await for concurrent operations
   and improved performance.

For Topic-Specific Guides
--------------------------

See the :doc:`/fortios/guides/index` section for detailed guides on:

- Firewall policies
- Schedules (recurring, onetime, groups)
- Traffic shapers
- Services (custom, groups, categories)
- Filtering and queries
- Validation
- Performance optimization

Quick Links
-----------

- :doc:`/fortios/getting-started/quickstart` - Get started in 5 minutes
- :doc:`/fortios/guides/index` - Topic-specific guides
- :doc:`/fortios/examples/index` - Code examples
