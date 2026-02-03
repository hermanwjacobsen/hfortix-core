HFortix-Core Documentation
==========================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   quickstart
   api/index

Welcome to HFortix-Core
-----------------------

**HFortix-Core** provides the foundational utilities, protocols, and base classes for the HFortix ecosystem.

Features
--------

* Observable HTTP client infrastructure
* Event-driven monitoring and observability
* Base abstractions for Fortinet API clients
* High-performance async/await support
* Production-ready error handling

Installation
------------

.. code-block:: bash

   pip install hfortix-core

Quick Start
-----------

.. code-block:: python

   from hfortix_core import ObservableHTTPClient, HTTPRequestEvent

   # Create observable HTTP client
   client = ObservableHTTPClient(base_url="https://api.example.com")

   # Subscribe to request events
   def log_requests(event: HTTPRequestEvent):
       print(f"{event.method} {event.url} - {event.status_code}")

   client.subscribe(log_requests)

   # Make requests
   response = await client.get("/status")

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
