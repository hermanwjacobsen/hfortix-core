Batch Transactions
==================

Batch transactions allow you to group multiple API operations into a single atomic unit. All changes are applied together on commit, or rolled back on abort.

.. note::
   **Requires:** FortiOS 6.4.0 or later

Overview
--------

FortiOS batch transactions provide:

- **Atomic operations**: All changes succeed or fail together
- **Rollback capability**: Undo all changes if something goes wrong
- **Performance**: Reduced configuration application overhead
- **Consistency**: Ensure related changes are applied simultaneously

.. important::
   Only one transaction can be active at a time per connection.

Quick Start
-----------

Basic Usage - Context Manager
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The simplest way to use transactions is with a context manager:

.. code-block:: python

   from hfortix import FortiOS

   fgt = FortiOS("192.168.1.99", token="your_token")

   # All changes in this block are atomic
   with fgt.transaction() as txn:
       # Create interface
       fgt.api.cmdb.system.interface.post({
           "name": "dmz",
           "vdom": "root",
           "mode": "static",
           "ip": "10.0.1.1 255.255.255.0"
       })
       
       # Create firewall address
       fgt.api.cmdb.firewall.address.post({
           "name": "dmz-server",
           "subnet": "10.0.1.10 255.255.255.255"
       })
       
       # Create firewall policy
       fgt.api.cmdb.firewall.policy.post({
           "policyid": 100,
           "name": "allow-dmz",
           "srcintf": [{"name": "internal"}],
           "dstintf": [{"name": "dmz"}],
           "srcaddr": [{"name": "all"}],
           "dstaddr": [{"name": "dmz-server"}],
           "action": "accept",
           "schedule": "always",
           "service": [{"name": "HTTP"}]
       })

   # Transaction automatically commits on success
   # Automatically aborts if any exception occurs

Decorator Pattern
~~~~~~~~~~~~~~~~~

For reusable transactional functions:

.. code-block:: python

   @fgt.transactional(timeout=120)
   def setup_network_infrastructure():
       """All operations in this function run in a transaction"""
       fgt.api.cmdb.system.interface.post({
           "name": "dmz",
           "ip": "10.0.1.1 255.255.255.0"
       })
       
       fgt.api.cmdb.firewall.address.post({
           "name": "dmz-network",
           "subnet": "10.0.1.0 255.255.255.0"
       })
       
       return {"status": "success"}

   # Call the function - transaction auto-commits on success
   result = setup_network_infrastructure()

Transaction Lifecycle
---------------------

Automatic Behavior
~~~~~~~~~~~~~~~~~~

By default, transactions use **auto-commit** and **auto-abort**:

.. code-block:: python

   with fgt.transaction() as txn:
       # Make changes...
       fgt.api.cmdb.firewall.address.post({...})
       # Success: auto-commits when exiting context

If an exception occurs:

.. code-block:: python

   with fgt.transaction() as txn:
       fgt.api.cmdb.firewall.address.post({...})
       raise ValueError("Something went wrong")
       # Exception: transaction automatically aborts (rolls back)

Manual Control
~~~~~~~~~~~~~~

Disable auto-commit/abort for manual control:

.. code-block:: python

   with fgt.transaction(auto_commit=False, auto_abort=False) as txn:
       try:
           # Make changes
           fgt.api.cmdb.system.interface.post({...})
           fgt.api.cmdb.firewall.policy.post({...})
           
           # Validate changes
           if validation_passes():
               txn.commit()  # Manually commit
           else:
               txn.abort()   # Manually abort
               
       except Exception as e:
           print(f"Error: {e}")
           txn.rollback()  # rollback() is alias for abort()

Transaction Properties
~~~~~~~~~~~~~~~~~~~~~~

Check transaction state:

.. code-block:: python

   txn = fgt.transaction(auto_commit=False, auto_abort=False)
   txn.start()

   print(f"Transaction ID: {txn.transaction_id}")
   print(f"Is active: {txn.is_active}")
   print(f"Is committed: {txn.is_committed}")
   print(f"Is aborted: {txn.is_aborted}")

   txn.commit()

Advanced Features
-----------------

Custom Timeout
~~~~~~~~~~~~~~

Set a custom timeout for long-running transactions:

.. code-block:: python

   # Default timeout is 60 seconds
   # For complex changes, increase the timeout
   with fgt.transaction(timeout=300) as txn:
       # Transaction expires after 5 minutes if not committed
       for i in range(100):
           fgt.api.cmdb.firewall.address.post({
               "name": f"host-{i}",
               "subnet": f"10.0.1.{i} 255.255.255.255"
           })

Show Transaction Details (FortiOS 7.4.1+)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

View cached commands before committing:

.. code-block:: python

   with fgt.transaction(auto_commit=False) as txn:
       fgt.api.cmdb.firewall.address.post({
           "name": "test-address",
           "subnet": "192.168.1.0 255.255.255.0"
       })
       
       # Preview what will be applied
       details = txn.show()
       print(details['results'])  # Shows FortiOS CLI commands
       
       # Decide whether to commit
       txn.commit()

List Active Transactions (FortiOS 7.4.1+)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See all active transactions on the FortiGate:

.. code-block:: python

   # List all active transactions
   transactions = fgt.list_transactions()

   for txn in transactions:
       print(f"Transaction ID: {txn.get('transaction_id')}")
       print(f"VDOM: {txn.get('vdom')}")

Best Practices
--------------

1. Use Transactions for Related Changes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Group logically related configuration changes:

.. code-block:: python

   # Good: Related firewall configuration
   with fgt.transaction() as txn:
       fgt.api.cmdb.firewall.address.post({...})      # Address object
       fgt.api.cmdb.firewall.addrgrp.post({...})      # Address group
       fgt.api.cmdb.firewall.policy.post({...})       # Policy using both

2. Keep Transactions Short
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Avoid long-running operations in transactions:

.. code-block:: python

   # Avoid: Don't include delays or external API calls
   with fgt.transaction() as txn:
       fgt.api.cmdb.firewall.address.post({...})
       time.sleep(30)  # Bad: wastes transaction time
       external_api.validate()  # Bad: external dependency

3. Set Appropriate Timeouts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Match timeout to complexity:

.. code-block:: python

   # Simple changes: default 60s is fine
   with fgt.transaction() as txn:
       fgt.api.cmdb.firewall.address.post({...})

   # Complex changes: increase timeout
   with fgt.transaction(timeout=300) as txn:
       # Bulk operations
       for addr in addresses:
           fgt.api.cmdb.firewall.address.post(addr)

Common Patterns
---------------

Bulk Object Creation
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   addresses = [
       {"name": f"host-{i}", "subnet": f"10.0.1.{i} 255.255.255.255"}
       for i in range(1, 101)
   ]

   with fgt.transaction(timeout=180) as txn:
       for addr in addresses:
           fgt.api.cmdb.firewall.address.post(addr)

Configuration Migration
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   @fgt.transactional(timeout=300)
   def migrate_config(old_vdom, new_vdom):
       """Migrate configuration from one VDOM to another"""
       # Get objects from old VDOM
       addresses = fgt.api.cmdb.firewall.address.get(vdom=old_vdom)
       
       # Create in new VDOM (all in transaction)
       for addr in addresses:
           addr['vdom'] = new_vdom
           fgt.api.cmdb.firewall.address.post(addr, vdom=new_vdom)

   migrate_config("old-vdom", "new-vdom")

Conditional Rollback
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   with fgt.transaction(auto_commit=False, auto_abort=False) as txn:
       # Make changes
       result = fgt.api.cmdb.firewall.policy.post({...})
       
       # Check if policy was created successfully
       policy_id = result.get('mkey')
       verification = fgt.api.cmdb.firewall.policy.get(policy_id)
       
       if verification and verification.get('status') == 'enable':
           print("Policy verified, committing")
           txn.commit()
       else:
           print("Policy verification failed, rolling back")
           txn.rollback()

API Reference
-------------

FortiOS.transaction()
~~~~~~~~~~~~~~~~~~~~~

Create a transaction context manager.

**Parameters:**

- ``timeout`` (int): Transaction timeout in seconds (default: 60)
- ``vdom`` (str): VDOM for transaction (default: client's VDOM)
- ``auto_commit`` (bool): Auto-commit on successful exit (default: True)
- ``auto_abort`` (bool): Auto-abort on exception (default: True)

**Returns:** ``Transaction`` object

FortiOS.transactional()
~~~~~~~~~~~~~~~~~~~~~~~~

Decorator to run a function within a transaction.

**Parameters:**

- ``timeout`` (int): Transaction timeout in seconds (default: 60)
- ``vdom`` (str): VDOM for transaction (default: client's VDOM)

**Returns:** Decorator function

Transaction Methods
~~~~~~~~~~~~~~~~~~~

- ``start()``: Start the transaction (returns transaction ID)
- ``commit()``: Commit all cached changes
- ``abort()``: Abort and rollback all changes
- ``rollback()``: Alias for abort()
- ``show()``: Show cached commands (FortiOS 7.4.1+)

Transaction Properties
~~~~~~~~~~~~~~~~~~~~~~

- ``transaction_id``: Unique transaction identifier
- ``is_active``: True if transaction is active
- ``is_committed``: True if transaction has been committed
- ``is_aborted``: True if transaction has been aborted

See Also
--------

- :doc:`/fortios/guides/error-handling` - Error handling patterns
- :doc:`/fortios/guides/api-request-inspection` - Request debugging
- `FortiOS Transaction API Documentation <https://docs.fortinet.com/document/fortigate/latest/cli-reference/854620/transaction>`_
