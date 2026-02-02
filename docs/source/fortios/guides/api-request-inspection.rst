API Request Inspection
======================

The HFortix SDK provides powerful request inspection capabilities to help you debug, audit, and understand API interactions with FortiOS devices.

Overview
--------

The request inspection feature allows you to:

- **Debug API calls**: See exactly what was sent and received
- **Audit operations**: Track all configuration changes
- **Troubleshoot errors**: Understand why requests fail
- **Learn the API**: See how high-level operations translate to HTTP requests
- **Build custom tools**: Access raw request/response data

Quick Start
-----------

Basic Usage
~~~~~~~~~~~

.. code-block:: python

   from hfortix import FortiOS

   fgt = FortiOS("192.168.1.99", token="your_token")

   # Make an API call
   response = fgt.api.cmdb.firewall.address.get("server1")

   # Inspect the last request
   last_request = fgt.http_api_request()

   print(f"Method: {last_request['method']}")
   print(f"URL: {last_request['url']}")
   print(f"Status: {last_request['status_code']}")
   print(f"Response: {last_request['response']}")

FortiManager Inspection
~~~~~~~~~~~~~~~~~~~~~~~

For FortiManager, use ``fmg_api_request()``:

.. code-block:: python

   from hfortix import FortiManager

   fmg = FortiManager("192.168.1.100", username="admin", password="password")

   # Make an API call
   response = fmg.dvmdb.adom.get()

   # Inspect the last request
   last_request = fmg.fmg_api_request()

   print(f"JSON-RPC ID: {last_request['id']}")
   print(f"Method: {last_request['method']}")
   print(f"URL: {last_request['url']}")
   print(f"Response: {last_request['response']}")

Request Object Structure
------------------------

FortiOS Request Object
~~~~~~~~~~~~~~~~~~~~~~

The ``http_api_request()`` method returns a dictionary with:

.. code-block:: python

   {
       'method': str,           # HTTP method (GET, POST, PUT, DELETE)
       'url': str,              # Full request URL
       'headers': dict,         # Request headers
       'body': dict,            # Request body (for POST/PUT)
       'status_code': int,      # HTTP status code
       'response': dict,        # Parsed response body
       'duration': float,       # Request duration in seconds
       'timestamp': str         # ISO timestamp of request
   }

FortiManager Request Object
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``fmg_api_request()`` method returns a dictionary with:

.. code-block:: python

   {
       'id': int,               # JSON-RPC request ID
       'method': str,           # JSON-RPC method (get, set, add, etc.)
       'url': str,              # API endpoint URL
       'params': list,          # JSON-RPC params array
       'response': dict,        # Full JSON-RPC response
       'result': dict,          # Response result object
       'status': dict,          # Response status (code, message)
       'duration': float,       # Request duration in seconds
       'timestamp': str         # ISO timestamp of request
   }

Common Use Cases
----------------

1. Debugging Failed Requests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from hfortix import FortiOS, APIError

   fgt = FortiOS("192.168.1.99", token="your_token")

   try:
       # This might fail
       fgt.api.cmdb.firewall.policy.post({
           "policyid": 100,
           "name": "test-policy"
           # Missing required fields
       })
   except APIError as e:
       # Inspect what went wrong
       last_req = fgt.http_api_request()
       
       print(f"Request failed:")
       print(f"  Method: {last_req['method']}")
       print(f"  URL: {last_req['url']}")
       print(f"  Body: {last_req['body']}")
       print(f"  Status: {last_req['status_code']}")
       print(f"  Error: {last_req['response']}")

2. Audit Trail
~~~~~~~~~~~~~~

.. code-block:: python

   import json
   from datetime import datetime

   # Store all API operations for audit
   audit_log = []

   fgt = FortiOS("192.168.1.99", token="your_token")

   # Create address
   fgt.api.cmdb.firewall.address.post({
       "name": "server1",
       "subnet": "10.0.1.10 255.255.255.255"
   })
   audit_log.append(fgt.http_api_request())

   # Update address
   fgt.api.cmdb.firewall.address.put("server1", {
       "comment": "Production server"
   })
   audit_log.append(fgt.http_api_request())

   # Delete address
   fgt.api.cmdb.firewall.address.delete("server1")
   audit_log.append(fgt.http_api_request())

   # Save audit log
   with open("audit.json", "w") as f:
       json.dump(audit_log, f, indent=2)

3. Performance Analysis
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import statistics

   fgt = FortiOS("192.168.1.99", token="your_token")

   durations = []

   # Test multiple requests
   for i in range(10):
       fgt.api.cmdb.firewall.address.get()
       req = fgt.http_api_request()
       durations.append(req['duration'])

   print(f"Average latency: {statistics.mean(durations):.3f}s")
   print(f"Min latency: {min(durations):.3f}s")
   print(f"Max latency: {max(durations):.3f}s")

4. Learning the API
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Make a high-level call
   fgt = FortiOS("192.168.1.99", token="your_token")

   response = fgt.api.cmdb.firewall.policy.post({
       "policyid": 100,
       "name": "allow-web",
       "srcintf": [{"name": "internal"}],
       "dstintf": [{"name": "wan1"}],
       "srcaddr": [{"name": "all"}],
       "dstaddr": [{"name": "all"}],
       "action": "accept",
       "schedule": "always",
       "service": [{"name": "HTTP"}]
   })

   # See exactly what was sent
   req = fgt.http_api_request()

   print("To create this policy, the SDK sent:")
   print(f"  {req['method']} {req['url']}")
   print(f"  Body: {json.dumps(req['body'], indent=2)}")

Integration Examples
--------------------

Logging Integration
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import logging
   import json

   logging.basicConfig(
       level=logging.DEBUG,
       format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
   )
   logger = logging.getLogger('fortios_api')

   fgt = FortiOS("192.168.1.99", token="your_token")

   # Make API call
   fgt.api.cmdb.firewall.address.get("server1")

   # Log the request
   req = fgt.http_api_request()
   logger.info(
       f"API Request: {req['method']} {req['url']} - "
       f"Status: {req['status_code']} - "
       f"Duration: {req['duration']:.3f}s"
   )

   # Log full details at debug level
   logger.debug(f"Full request: {json.dumps(req, indent=2)}")

Transaction Inspection
~~~~~~~~~~~~~~~~~~~~~~

When using transactions, you can inspect individual operations:

.. code-block:: python

   from hfortix import FortiOS

   fgt = FortiOS("192.168.1.99", token="your_token")

   with fgt.transaction() as txn:
       # First operation
       fgt.api.cmdb.firewall.address.post({"name": "addr1", "subnet": "10.0.1.1/32"})
       req1 = fgt.http_api_request()
       print(f"Op 1: {req1['method']} {req1['url']}")
       
       # Second operation
       fgt.api.cmdb.firewall.address.post({"name": "addr2", "subnet": "10.0.1.2/32"})
       req2 = fgt.http_api_request()
       print(f"Op 2: {req2['method']} {req2['url']}")
       
       # Show transaction details (FortiOS 7.4.1+)
       details = txn.show()
       print(f"Transaction commands: {details}")

   # After commit, you can still inspect the last operation
   final_req = fgt.http_api_request()
   print(f"Final operation: {final_req['method']} {final_req['url']}")

Best Practices
--------------

1. Always Check After Critical Operations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Create important object
   fgt.api.cmdb.firewall.policy.post({...})

   # Verify it succeeded
   req = fgt.http_api_request()
   if req['status_code'] != 200:
       logger.error(f"Policy creation failed: {req['response']}")
       raise Exception("Failed to create policy")

2. Use for Debugging, Not Production Logic
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # ❌ Bad: Don't rely on http_api_request for application logic
   response = fgt.api.cmdb.firewall.address.get("server1")
   req = fgt.http_api_request()
   if req['status_code'] == 200:
       # Use response directly, not req['response']
       
   # ✅ Good: Use for debugging and monitoring
   try:
       response = fgt.api.cmdb.firewall.address.get("server1")
       # Use response here
   except APIError as e:
       # Use http_api_request to understand the error
       req = fgt.http_api_request()
       logger.debug(f"Request details: {req}")

3. Sanitize Before Logging
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   def sanitize_request(request):
       """Remove sensitive data from request"""
       sanitized = request.copy()
       
       # Remove authentication headers
       if 'headers' in sanitized:
           headers = sanitized['headers'].copy()
           headers.pop('Authorization', None)
           headers.pop('X-CSRFTOKEN', None)
           sanitized['headers'] = headers
       
       # Remove sensitive fields from body
       if 'body' in sanitized and isinstance(sanitized['body'], dict):
           body = sanitized['body'].copy()
           body.pop('password', None)
           body.pop('secret', None)
           sanitized['body'] = body
       
       return sanitized

   # Always remove sensitive data before logging/storing
   req = fgt.http_api_request()
   safe_req = sanitize_request(req)
   logger.info(f"Request: {safe_req}")

Limitations
-----------

Only Last Request
~~~~~~~~~~~~~~~~~

The SDK stores only the **most recent request**. For multiple requests, implement your own history:

.. code-block:: python

   # This only shows the last request
   fgt.api.cmdb.firewall.address.get("addr1")
   fgt.api.cmdb.firewall.address.get("addr2")
   req = fgt.http_api_request()  # Only shows addr2 request

FortiOS vs FortiManager
~~~~~~~~~~~~~~~~~~~~~~~

Use the correct method for each platform:

- FortiOS: ``fgt.http_api_request()``
- FortiManager: ``fmg.fmg_api_request()``

See Also
--------

- :doc:`/fortios/guides/transactions` - Batch transactions
- :doc:`/fortios/guides/error-handling` - Error handling patterns
- :doc:`/fortios/guides/debugging` - Advanced debugging techniques
- :doc:`/fortios/guides/audit-logging` - Enterprise audit logging
