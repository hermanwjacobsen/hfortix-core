Quickstart
==========

Installation
------------

Install HFortix-Core via pip:

.. code-block:: bash

   pip install hfortix-core

Basic Usage
-----------

Observable HTTP Client
~~~~~~~~~~~~~~~~~~~~~~

The observable HTTP client provides event-driven monitoring of HTTP requests:

.. code-block:: python

   from hfortix_core import ObservableHTTPClient, HTTPRequestEvent

   # Create client
   client = ObservableHTTPClient(base_url="https://api.example.com")

   # Subscribe to events
   def on_request(event: HTTPRequestEvent):
       print(f"Request: {event.method} {event.url}")
       print(f"Status: {event.status_code}")

   client.subscribe(on_request)

   # Make requests
   response = await client.get("/endpoint")

Next Steps
----------

* Read the :doc:`api/index` for detailed API documentation
* Check out `hfortix-fortios <https://hfortix-fortios.readthedocs.io/>`_ for FortiOS automation
